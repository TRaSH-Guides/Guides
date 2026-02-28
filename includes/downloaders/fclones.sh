#!/bin/bash
# ================================
# Script: fclones run
# Version: 1.1.0
# Updated: 20260223
# ================================

# When running this script standalone, ensure that the mover-tuning.cfg file is in the same folder as the script.
# Update the fclones run script settings section in the mover-tuning.cfg file.

# Get the directory where the script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Source the config from the same directory
source "$SCRIPT_DIR/mover-tuning.cfg"

# Script version and update check URLs
readonly SCRIPT_VERSION="1.1.0"
readonly MIN_CONFIG_VERSION="1.2.0"
readonly GIST_RAW_URL="https://raw.githubusercontent.com/TRaSH-Guides/Guides/refs/heads/master/includes/downloaders/fclones.sh"

# Notification delay in seconds
NOTIFICATION_DELAY=2

# Set default path separator if not set (for backward compatibility)
EFFECTIVE_PATH_SEPARATOR="${PATH_SEPARATOR:- }"

# Initialize variables
start_time=$(date +%s)
timestamp=$(date -d "@$start_time" +%Y%m%d_%H%M%S)
processed_groups=0
successful_groups=0
total_space_saved=0
clean_folders=()
hardlink_folders=()
error_folders=()

# ================================
# FUNCTIONS
# ================================

# Function to send notifications with delay
send_notification() {
    local icon="$1"
    local subject="$2"
    local description="$3"

    /usr/local/emhttp/plugins/dynamix/scripts/notify -i "$icon" -s "$subject" -d "$description"
    sleep "$NOTIFICATION_DELAY"
}

# Function to log output to both console and file
log_msg() {
    local level="$1"
    shift
    local ts
    ts=$(date '+%Y-%m-%d %H:%M:%S')

    # Build one formatted line (keep intentional blank lines unprefixed)
    local line
    if [[ $# -eq 0 || -z "$*" ]]; then
        line=""
    else
        line="[$ts] [$level] $*"
    fi

    if [[ -n "$LOG_FILE" ]]; then
        if [[ "$level" == "ERROR" || "$level" == "WARN" ]]; then
            printf '%s\n' "$line" | tee -a "$LOG_FILE" >&2
        else
            printf '%s\n' "$line" | tee -a "$LOG_FILE"
        fi
    else
        if [[ "$level" == "ERROR" || "$level" == "WARN" ]]; then
            printf '%s\n' "$line" >&2
        else
            printf '%s\n' "$line"
        fi
    fi
}

# Function to check for script updates
check_script_version() {
    log_msg INFO "Checking for script updates..."

    # Check if version check is enabled
    if [[ "${ENABLE_VERSION_CHECK:-true}" != "true" ]]; then
        log_msg INFO "Version check disabled"
        return 0
    fi

    # Check for curl or wget
    local fetch_cmd
    if command -v curl &>/dev/null; then
        fetch_cmd="curl -s"
    elif command -v wget &>/dev/null; then
        fetch_cmd="wget -qO-"
    else
        log_msg WARN "⚠ Cannot check version: curl or wget not found (continuing anyway)"
        return 0
    fi

    # Fetch the latest version from the Gist raw URL
    local remote_content
    remote_content=$($fetch_cmd "$GIST_RAW_URL" 2>/dev/null) || true

    if [[ -z "$remote_content" ]]; then
        log_msg WARN "⚠ Could not fetch latest version from Gist (continuing anyway)"
        return 0
    fi

    # Extract version from the remote script - try multiple patterns
    local latest_version
    # Try pattern 1: readonly SCRIPT_VERSION="x.x.x"
    latest_version=$(printf '%s\n' "$remote_content" | grep -m1 "readonly SCRIPT_VERSION=" | sed 's/^.*readonly SCRIPT_VERSION="\([^"]*\)".*$/\1/' 2>/dev/null) || true

    # If that didn't work, try pattern 2: SCRIPT_VERSION="x.x.x" (without readonly)
    if [[ -z "$latest_version" ]]; then
        latest_version=$(printf '%s\n' "$remote_content" | grep -m1 "SCRIPT_VERSION=" | sed 's/^.*SCRIPT_VERSION="\([^"]*\)".*$/\1/' 2>/dev/null) || true
    fi

    if [[ -z "$latest_version" ]]; then
        log_msg WARN "⚠ Could not parse version from Gist (continuing anyway)"
        return 0
    fi

    log_msg INFO "Current version: $SCRIPT_VERSION"
    log_msg INFO "Latest version: $latest_version"

    # Compare versions
    if [[ "$SCRIPT_VERSION" != "$latest_version" ]]; then
        # Simple version comparison (works for semantic versioning)
        if printf '%s\n' "$latest_version" "$SCRIPT_VERSION" | sort -V | head -n1 | grep -q "^$SCRIPT_VERSION$" 2>/dev/null || true; then
            log_msg WARN "⚠ New version available: $latest_version"
            send_notification "normal" "fclones Script Update" "Version $latest_version available (current: $SCRIPT_VERSION)<br><br><b>To upgrade:</b><br>1. Remove the fclones.sh script from $SCRIPT_DIR<br>2. Running the mover-tuning-end script will automatically install the latest version"
        fi
    else
        log_msg INFO "✓ Script is up to date"
    fi

    return 0
}

# Set up logging
setup_logging() {
    if [[ ! -d "$LOG_PATH" ]]; then
        mkdir -p "$LOG_PATH" || {
            log_msg ERROR "Failed to create log directory: $LOG_PATH"
            return 1
        }
    fi
    LOG_FILE="${LOG_PATH}/fclones_${timestamp}.log"
}

# Set up folder for group output temp file
setup_temp_dir() {
    TEMP_PATH="${TEMP_PATH:-/tmp/fclones}"
    if [[ ! -d "$TEMP_PATH" ]]; then
        mkdir -p "$TEMP_PATH" || {
            log_msg ERROR "Failed to create temp directory: $TEMP_PATH"
            return 1
        }
    fi
}

# Set up cache directory if configured
setup_cache_dir() {
    [[ -z "$CACHE_PATH" ]] && return 0

    mkdir -p "$CACHE_PATH" || {
        log_msg ERROR "Failed to create CACHE_PATH directory: $CACHE_PATH"
        return 1
    }

    [[ -w "$CACHE_PATH" ]] || {
        log_msg ERROR "CACHE_PATH directory is not writable: $CACHE_PATH"
        return 1
    }
}

# Clean up (delete) old files if retention > 0 (0 = keep forever)
cleanup_old_files() {
    local dir="$1"
    local pattern="$2"
    local retention_days="$3"

    ((retention_days > 0)) || return 0
    log_msg INFO "Cleaning up files older than $retention_days in $dir..."

    local retention_minutes=$((retention_days * 24 * 60))
    find "$dir" -name "$pattern" -type f -mmin +"$retention_minutes" -delete 2>/dev/null
}

# Validation functions
validate_configuration() {
    local errors=0

    # Validate config version
    local current_config_version="${CONFIG_VERSION:-unknown}"
    if [[ "$current_config_version" == "unknown" ]]; then
        log_msg WARN "CONFIG_VERSION is not set in mover-tuning.cfg (recommended minimum: $MIN_CONFIG_VERSION)"
    else
        local oldest_version
        oldest_version=$(printf '%s\n' "$MIN_CONFIG_VERSION" "$current_config_version" | sort -V | head -n1)
        # If current version sorts first and is not equal, it is older than required
        if [[ "$oldest_version" == "$current_config_version" && "$current_config_version" != "$MIN_CONFIG_VERSION" ]]; then
            log_msg WARN "Config version $current_config_version is older than recommended minimum $MIN_CONFIG_VERSION"
            log_msg WARN "Please update mover-tuning.cfg to ensure compatibility with this script version"
        fi
    fi

    # Validate folder groups - THIS IS THE CRITICAL CHECK BEFORE other validation
    if [[ ${#folders[@]} -eq 0 ]]; then
        log_msg INFO ""
        log_msg ERROR "No search folder groups configured!"
        log_msg INFO ""
        log_msg INFO "Please edit mover-tuning.cfg and configure at least one folder group."
        log_msg INFO "Examples:"
        log_msg INFO ' readonly PATH_SEPARATOR="|"'
        log_msg INFO ' folders["Series"]="/mnt/user/data/torrents/tv/|/mnt/user/data/media/tv/"'
        log_msg INFO ' folders["Series"]="/mnt/user/data/torrents/tv/"'
        log_msg INFO ' folders["Series"]="/mnt/user/data/torrents/tv/|/mnt/user/data/media/tv/|/mnt/user/data/torrents/series_linkdir/"'
        log_msg INFO ""
        log_msg INFO "Legacy format (space-separated) is still supported when PATH_SEPARATOR is not set."
        log_msg INFO ""

        # Send error notification
        send_notification "warning" "fclones - Configuration Error" \
            "⚠️ <b>No search folder groups configured!</b><br><br>Please edit <b>mover-tuning.cfg</b> and configure at least one folder group.<br><br>Example:<br><code>folders[\"Series\"]=\"/mnt/user/data/torrents/tv/|/mnt/user/data/media/tv/\"</code><br><br>Script execution was aborted."

        log_msg ERROR "No folder groups configured"
        ((errors++))
    fi

    # Validate EFFECTIVE_PATH_SEPARATOR is not empty (if set)
    if [[ -z "$EFFECTIVE_PATH_SEPARATOR" ]]; then
        log_msg ERROR "EFFECTIVE_PATH_SEPARATOR must not be empty"
        ((errors++))
    fi

    # Validate MAX_FILES_DISPLAY is a number
    if ! [[ "$MAX_FILES_DISPLAY" =~ ^[0-9]+$ ]]; then
        log_msg ERROR "MAX_FILES_DISPLAY must be a number (got: $MAX_FILES_DISPLAY)"
        ((errors++))
    fi

    # Validate MAX_FILENAME_LENGTH is a number
    if ! [[ "$MAX_FILENAME_LENGTH" =~ ^[0-9]+$ ]]; then
        log_msg ERROR "MAX_FILENAME_LENGTH must be a number (got: $MAX_FILENAME_LENGTH)"
        ((errors++))
    fi

    # Validate LOG_RETENTION_DAYS is a number
    if ! [[ "$LOG_RETENTION_DAYS" =~ ^[0-9]+$ ]]; then
        log_msg ERROR "LOG_RETENTION_DAYS must be a number (got: $LOG_RETENTION_DAYS)"
        ((errors++))
    fi

    # Validate TEMP_RETENTION_DAYS is a number
    if ! [[ "$TEMP_RETENTION_DAYS" =~ ^[0-9]+$ ]]; then
        log_msg ERROR "TEMP_RETENTION_DAYS must be a number (got: $TEMP_RETENTION_DAYS)"
        ((errors++))
    fi

    # Check if fclones is available
    if [[ -z "$FCLONES_PATH" ]]; then
        # If empty, check if fclones is in PATH
        if ! command -v fclones &>/dev/null; then
            log_msg ERROR "fclones command not found in PATH"
            ((errors++))
        else
            FCLONES_PATH="fclones" # Use the command from PATH
        fi
    elif ! command -v "$FCLONES_PATH" &>/dev/null; then
        log_msg ERROR "fclones command not found at: $FCLONES_PATH"
        ((errors++))
    fi

    return $errors
}

# Function to format bytes into human readable format
format_bytes() {
    local bytes=$1
    if [[ $bytes -lt 1024 ]]; then
        echo "${bytes}B"
    elif [[ $bytes -lt 1048576 ]]; then
        echo "$((bytes / 1024))KB"
    elif [[ $bytes -lt 1073741824 ]]; then
        echo "$((bytes / 1048576))MB"
    else
        local gb=$((bytes / 1073741824))
        local remainder=$(((bytes % 1073741824) / 10737418))
        if [[ $remainder -gt 0 ]]; then
            echo "${gb}.${remainder}GB"
        else
            echo "${gb}GB"
        fi
    fi
}

# Function to safely get file size
get_file_size() {
    local file_path="$1"
    local size

    if [[ ! -f "$file_path" ]]; then
        echo "0"
        return 1
    fi

    # Try different stat formats for cross-platform compatibility
    size=$(stat -f%z "$file_path" 2>/dev/null || stat -c%s "$file_path" 2>/dev/null || echo "0")

    if [[ ! "$size" =~ ^[0-9]+$ ]]; then
        echo "0"
        return 1
    fi

    echo "$size"
    return 0
}

# Function to build notification content
build_notification() {
    local content=""

    if [[ ${#hardlink_folders[@]} -gt 0 ]]; then
        # Build detailed file listing
        for folder_data in "${hardlink_folders[@]}"; do
            # Parse folder data: folder_name:file_count:files_string
            local folder_name="${folder_data%%:*}"
            local rest="${folder_data#*:}"
            local file_count="${rest%%:*}"
            local files_part="${rest#*:}"

            content+="🔗 <b>${folder_name}:</b><br>"

            # Show individual files
            IFS='|' read -ra file_array <<<"$files_part"
            local display_count=0
            local actual_file_count=0

            # First, count actual files (excluding "+X more" entries)
            for file in "${file_array[@]}"; do
                if [[ "$file" != +*more ]]; then
                    ((actual_file_count++))
                fi
            done

            # Now display files
            for file in "${file_array[@]}"; do
                if [[ "$file" == +*more ]]; then
                    # This is already a "+X more" entry from the truncation, display it
                    content+="... ${file}<br>"
                else
                    ((display_count++))
                    if [[ $MAX_FILES_DISPLAY -eq 0 ]] || [[ $display_count -le $MAX_FILES_DISPLAY ]]; then
                        # Escape special characters but be more careful with truncation
                        escaped_file=$(printf '%s' "$file" | sed 's/&/&amp;/g; s/</&lt;/g; s/>/&gt;/g; s/"/&quot;/g')

                        # Truncate based on original filename length, not escaped length
                        if [[ ${#file} -gt $MAX_FILENAME_LENGTH ]]; then
                            # Truncate the original filename first, then escape
                            local truncate_at=$((MAX_FILENAME_LENGTH - 3))
                            truncated_original="${file:0:$truncate_at}..."
                            escaped_truncated=$(printf '%s' "$truncated_original" | sed 's/&/&amp;/g; s/</&lt;/g; s/>/&gt;/g; s/"/&quot;/g')
                            content+="• ${escaped_truncated}<br>"
                        else
                            content+="• ${escaped_file}<br>"
                        fi
                    fi
                fi
            done

            # If we have more files than displayed, show the remainder
            # Use the actual file_count stored in the data structure, not the array count
            if [[ $MAX_FILES_DISPLAY -gt 0 ]] && [[ $file_count -gt $MAX_FILES_DISPLAY ]]; then
                content+="... +$((file_count - MAX_FILES_DISPLAY)) more<br>"
            fi
        done

        # Add clean folders if any
        if [[ ${#clean_folders[@]} -gt 0 ]]; then
            content+="<br>✅ <b>No duplicates:</b> $(
                IFS=', '
                echo "${clean_folders[*]}"
            )<br>"
        fi

        # Add summary line
        content+="<br>📊 <b>Summary:</b> ${processed_groups}/${total_groups} processed • ${time_formatted}"

        # Add total space saved if any hardlinks were created
        if [[ $total_space_saved -gt 0 ]]; then
            local formatted_total_space
            formatted_total_space=$(format_bytes "$total_space_saved")
            content+="<br>💾 <b>Space Saved:</b> ${formatted_total_space}"
        fi
    elif [[ ${#error_folders[@]} -gt 0 ]]; then
        content="❌ <b>Errors:</b> $(
            IFS=', '
            echo "${error_folders[*]}"
        )"
        if [[ ${#clean_folders[@]} -gt 0 ]]; then
            content+="<br>✅ <b>No duplicates:</b> $(
                IFS=', '
                echo "${clean_folders[*]}"
            )"
        fi
        content+="<br>⏱️ ${time_formatted}"
    else
        content="✅ <b>No duplicates found:</b> $(
            IFS=', '
            echo "${clean_folders[*]}"
        )<br>📊 <b>Processed:</b> ${processed_groups}/${total_groups} folders<br>⏱️ ${time_formatted}"
    fi

    echo "$content"
}

# ================================
# MAIN SCRIPT
# ================================

# Set up logging and temp file first (before any validation)
if ! setup_logging; then
    echo "Failed to set up logging. Exiting."
    exit 1
fi
if ! setup_temp_dir; then
    log_msg ERROR "Failed to set up temp file. Exiting."
    exit 1
fi

# Validation
if ! validate_configuration; then
    log_msg INFO "========================================"
    log_msg INFO "fclones Configuration Error"
    log_msg INFO "Started: $(date '+%Y-%m-%d %H:%M:%S')"
    log_msg INFO "Configuration validation failed. Exiting."
    log_msg INFO "========================================"
    exit 1
fi

# Begin processing
total_groups=${#folders[@]}

log_msg INFO "========================================"
log_msg INFO "fclones Hardlink Creation Process"
log_msg INFO "Started: $(date '+%Y-%m-%d %H:%M:%S')"
log_msg INFO "Log file: $LOG_FILE"
log_msg INFO "========================================"
log_msg INFO ""

# Check for script updates
check_script_version
log_msg INFO ""

# Cleanup old files before starting the process (after validation and logging setup)
cleanup_old_files "$TEMP_PATH" "fclones_groups_*.txt" "$TEMP_RETENTION_DAYS"
cleanup_old_files "$LOG_PATH" "fclones_*.log" "$LOG_RETENTION_DAYS"
log_msg INFO ""

# Set up cache directory if configured
if ! setup_cache_dir; then
    log_msg ERROR "Cache setup failed. Exiting."
    exit 1
fi

log_msg INFO "Starting fclones hardlink creation process..."
log_msg INFO "Processing $total_groups folder groups"
log_msg INFO ""

# Set up environment for background execution
# Fix HOME if it's empty or just "/"
if [[ -z "$HOME" ]] || [[ "$HOME" == "/" ]]; then
    export HOME="/root"
fi
export USER="${USER:-root}"

# Loop through each group of folders
for group_name in "${!folders[@]}"; do
    ((processed_groups++))

    unset seen_files
    declare -A seen_files

    # Split configured dirs for the group into an array based on the EFFECTIVE_PATH_SEPARATOR (default to space if not set)
    raw_value="${folders[$group_name]}"
    if [[ "$EFFECTIVE_PATH_SEPARATOR" == " " ]]; then
        read -r -a group_dirs <<<"$raw_value"
        if [[ "$raw_value" == *"'"* ]]; then
            log_msg WARN "folders[$group_name] contains single quotes inside the value; this does not protect spaces in paths."
        fi
    else
        IFS="$EFFECTIVE_PATH_SEPARATOR" read -r -a group_dirs <<<"$raw_value"
        if [[ "$raw_value" != *"$EFFECTIVE_PATH_SEPARATOR"* ]]; then
            log_msg WARN "folders[$group_name] does not contain EFFECTIVE_PATH_SEPARATOR ('$EFFECTIVE_PATH_SEPARATOR'); check config format."
        fi
    fi

    log_msg INFO "[$processed_groups/$total_groups] Processing: $group_name"
    log_msg INFO "  Dirs: ${group_dirs[*]}"

    # Check if group has at least one dir
    if [[ ${#group_dirs[@]} -eq 0 ]]; then
        error_folders+=("$group_name")
        log_msg ERROR "  No directories configured for group"
        log_msg INFO ""
        continue
    fi

    # Check if all dirs exist
    missing_dir=0
    for dir in "${group_dirs[@]}"; do
        if [[ ! -d "$dir" ]]; then
            log_msg ERROR "  Directory not found: $dir"
            missing_dir=1
        fi
    done
    if [[ $missing_dir -eq 1 ]]; then
        error_folders+=("$group_name")
        log_msg INFO ""
        continue
    fi

    # Build and run fclones group and save output to temp file for processing and linking
    # Note: This will not use eval but an array to avoid issues with spaces in paths and arguments.
    # See https://www.shellcheck.net/wiki/SC2089 for details.
    log_msg INFO "  Analyzing duplicates..."
    # Create a safe filename for the group report by replacing non-alphanumeric characters with underscores
    safe_group_name=$(printf '%s' "$group_name" | tr -cs '[:alnum:]_.-' '_')
    group_report_file="${TEMP_PATH}/fclones_groups_${timestamp}_${processed_groups}_${safe_group_name}.txt"
    # Build fclones group command as an array (no eval)
    group_cmd=("$FCLONES_PATH" group)
    # Add args from FCLONES_ARGS if any (split by space, but this assumes no spaces in individual args)
    for arg in $FCLONES_ARGS; do
        group_cmd+=("$arg")
    done
    # Add file patterns as separate --name arguments
    for pattern in $FILE_PATTERNS; do
        group_cmd+=(--name "$pattern")
    done
    # Add cache if configured
    if [[ -n "$CACHE_PATH" ]]; then
        group_cmd+=(--cache "$CACHE_PATH")
    fi
    # Add folder paths of the group
    group_cmd+=("${group_dirs[@]}")

    # Run the group command and capture stderr for error handling, while saving stdout to the report file
    # Note: Since arguments are parsed left to right, stderr is captured in group_stderr before stdout redirection to the report file.
    # stdin is redirected from /dev/null to prevent fclones from waiting for input if it tries to read from stdin for any reason.
    group_stderr="$("${group_cmd[@]}" 2>&1 >"$group_report_file" </dev/null)"
    group_exit_code=$?

    # Skip further processing if fclones group command failed, and log the error details for this group
    if [[ $group_exit_code -ne 0 ]]; then
        error_folders+=("$group_name")
        log_msg ERROR "  fclones group failed (exit code: $group_exit_code)"
        log_msg ERROR "  $group_stderr"
        log_msg INFO ""
        continue
    fi

    # Read report and filter out non-report noise just in case
    result=$(<"$group_report_file")
    result=$(printf '%s\n' "$result" | grep -vE '^\[|fclones:|Initializing|Scanning files|Grouping by|Fetching extents|^#' || true)

    # Skip further processing if no duplicates found
    if [[ -z "$result" ]]; then
        clean_folders+=("$group_name")
        log_msg INFO "  Result: No duplicates found"
        log_msg INFO ""
        continue
    fi

    # Process the report to extract file paths and calculate space savings, while preparing the list of linked files for the notification.
    # Hardlinks will be created from the saved group report (no second group run)
    log_msg INFO "  Creating hardlinks..."

    space_saved_this_group=0
    linked_files=()
    current_group_files=()

    while IFS= read -r line; do
        # Trim whitespace
        line=$(printf '%s' "$line" | sed 's/^[[:space:]]*//;s/[[:space:]]*$//')

        # Skip empty lines and hash/metadata lines
        if [[ -z "$line" || "$line" =~ ^[a-f0-9]+,.*\*[[:space:]]*[0-9]+: ]]; then
            # This is either empty or a group header line, process previous group if exists
            if [[ ${#current_group_files[@]} -gt 1 ]]; then
                first_file="${current_group_files[0]}"
                if [[ -f "$first_file" ]]; then
                    file_size=$(get_file_size "$first_file")
                    if [[ $? -eq 0 && $file_size -gt 0 ]]; then
                        space_saved_group=$(((${#current_group_files[@]} - 1) * file_size))
                        space_saved_this_group=$((space_saved_this_group + space_saved_group))

                        # Only add the first file from the group (represents the duplicate set)
                        filename=$(basename "$first_file")
                        if [[ "$SHOW_FILE_EXTENSIONS" == "true" ]]; then
                            display_name="$filename"
                        else
                            display_name="${filename%.*}"
                        fi

                        # Only add if we haven't seen this filename before
                        if [[ -z "${seen_files[$display_name]}" ]]; then
                            linked_files+=("$display_name")
                            seen_files["$display_name"]=1
                        fi
                    fi
                fi
            fi
            current_group_files=()
            continue
        fi

        # Check if line is a file path (starts with /)
        if [[ "$line" =~ ^/ && -f "$line" ]]; then
            current_group_files+=("$line")
        fi
    done <<<"$result"

    # Handle last group if exists
    if [[ ${#current_group_files[@]} -gt 1 ]]; then
        first_file="${current_group_files[0]}"
        if [[ -f "$first_file" ]]; then
            file_size=$(get_file_size "$first_file")
            if [[ $? -eq 0 && $file_size -gt 0 ]]; then
                space_saved_group=$(((${#current_group_files[@]} - 1) * file_size))
                space_saved_this_group=$((space_saved_this_group + space_saved_group))

                # Only add the first file from the group (represents the duplicate set)
                filename=$(basename "$first_file")
                if [[ "$SHOW_FILE_EXTENSIONS" == "true" ]]; then
                    display_name="$filename"
                else
                    display_name="${filename%.*}"
                fi

                # Only add if we haven't seen this filename before
                if [[ -z "${seen_files[$display_name]}" ]]; then
                    linked_files+=("$display_name")
                    seen_files["$display_name"]=1
                fi
            fi
        fi
    fi

    # Only create hardlinks if we found duplicates
    if [[ ${#linked_files[@]} -eq 0 ]]; then
        clean_folders+=("$group_name")
        log_msg INFO "  Result: No valid duplicates found"
        log_msg INFO ""
        continue
    fi

    # Link from the saved group report (no second group run)
    link_result=$("$FCLONES_PATH" link <"$group_report_file" 2>&1)
    link_exit_code=$?

    if [[ $link_exit_code -eq 0 ]]; then
        ((successful_groups++))
        total_space_saved=$((total_space_saved + space_saved_this_group))
        file_count=${#linked_files[@]}

        # Print each linked file on a separate line
        log_msg INFO "  Linked files:"
        for linked_file in "${linked_files[@]}"; do
            log_msg INFO "    - $linked_file"
        done

        # Store folder with file list for notification (truncated if needed, but without "+X more")
        if [[ $MAX_FILES_DISPLAY -gt 0 && ${#linked_files[@]} -gt $MAX_FILES_DISPLAY ]]; then
            truncated_files=("${linked_files[@]:0:$MAX_FILES_DISPLAY}")
            files_string="$(
                IFS='|'
                echo "${truncated_files[*]}"
            )"
        else
            files_string=$(
                IFS='|'
                echo "${linked_files[*]}"
            )
        fi

        # Store folder with file count for summary (use actual count, not truncated)
        hardlink_folders+=("$group_name:$file_count:$files_string")

        formatted_space=$(format_bytes "$space_saved_this_group")
        log_msg INFO "  Result: Hardlinks created for $file_count files, saved $formatted_space"
    else
        error_folders+=("$group_name")
        log_msg ERROR "  Failed to create hardlinks (exit code: $link_exit_code)"
        log_msg ERROR "  $link_result"
    fi
    log_msg INFO ""
done

# Calculate execution time
end_time=$(date +%s)
execution_time=$((end_time - start_time))
if [[ $execution_time -ge 60 ]]; then
    minutes=$((execution_time / 60))
    seconds=$((execution_time % 60))
    time_formatted="${minutes}m${seconds}s"
else
    time_formatted="${execution_time}s"
fi

# Build notification
if [[ ${#hardlink_folders[@]} -gt 0 ]]; then
    icon="normal"
    title="fclones - Hardlinks Created"
elif [[ ${#error_folders[@]} -gt 0 ]]; then
    icon="warning"
    title="fclones - Errors Found"
else
    icon="normal"
    title="fclones - No duplicates"
fi

notification_content=$(build_notification)

# Send the notification
send_notification "$icon" "$title" "$notification_content"

# Calculate total files linked and extract folder names
total_files_linked=0
folders_with_hardlinks=()

for folder_data in "${hardlink_folders[@]}"; do
    # Extract folder name (before the first colon)
    folder_name="${folder_data%%:*}"
    folders_with_hardlinks+=("$folder_name")

    # Extract file count (between first and second colon)
    rest="${folder_data#*:}"
    file_count="${rest%%:*}"

    # Add to total count
    total_files_linked=$((total_files_linked + file_count))
done

# Console output
log_msg INFO "========================================"
log_msg INFO "fclones Process Completed"
log_msg INFO "========================================"
log_msg INFO ""

if [[ ${#clean_folders[@]} -gt 0 ]]; then
    log_msg INFO "Clean folders: $(
        IFS=', '
        echo "${clean_folders[*]}"
    )"
fi

if [[ $total_files_linked -gt 0 ]]; then
    log_msg INFO "Total files linked: $total_files_linked"
    log_msg INFO "Folders with hardlinks: $(
        IFS=', '
        echo "${folders_with_hardlinks[*]}"
    )"
fi

if [[ ${#error_folders[@]} -gt 0 ]]; then
    log_msg INFO "Error folders: $(
        IFS=', '
        echo "${error_folders[*]}"
    )"
fi

log_msg INFO "Total space saved: $(format_bytes $total_space_saved)"
log_msg INFO "Execution time: $time_formatted"
log_msg INFO ""
log_msg INFO "Completed: $(date '+%Y-%m-%d %H:%M:%S')"
log_msg INFO "========================================"

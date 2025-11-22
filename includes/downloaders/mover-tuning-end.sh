#!/bin/bash
set -euo pipefail # Exit on error, undefined variables, and pipe failures

# =====================================
# Script: qBittorrent Cache Mover - End
# Version: 1.0.0
# Updated: 20251121
# =====================================

# Script version and update check URLs
readonly SCRIPT_VERSION="1.0.0"
readonly SCRIPT_RAW_URL="https://raw.githubusercontent.com/TRaSH-Guides/Guides/refs/heads/master/includes/downloaders/mover-tuning-end.sh"

# Get the directory where the script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Source the config from the same directory
source "$SCRIPT_DIR/mover-tuning.cfg"

# Notification delay in seconds (helps ensure all notifications appear in Unraid)
NOTIFICATION_DELAY=2

# ================================
# UTILITY FUNCTIONS
# ================================
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $*"
}

error() {
    log "ERROR: $*" >&2
    exit 1
}

notify() {
    local subject="$1"
    local description="$2"
    local notify_cmd="/usr/local/emhttp/plugins/dynamix/scripts/notify"

    if [[ -x "$notify_cmd" ]]; then
        "$notify_cmd" -s "$subject" -d "$description"
        # Add delay after each notification to prevent dropping
        sleep "$NOTIFICATION_DELAY"
    fi
}

# ================================
# VERSION CHECK FUNCTION
# ================================
check_script_version() {
    log "Checking for script updates..."

    # Check if version check is enabled
    if [[ "${ENABLE_VERSION_CHECK:-true}" != "true" ]]; then
        log "Version check disabled"
        return 0
    fi

    # Check for curl or wget
    local fetch_cmd
    if command -v curl &> /dev/null; then
        fetch_cmd="curl -s"
    elif command -v wget &> /dev/null; then
        fetch_cmd="wget -qO-"
    else
        log "⚠ Cannot check version: curl or wget not found (continuing anyway)"
        return 0
    fi

    # Fetch the latest version from the raw script URL
    local remote_content
    remote_content=$($fetch_cmd "$SCRIPT_RAW_URL" 2>/dev/null) || true

    if [[ -z "$remote_content" ]]; then
        log "⚠ Could not fetch latest version from GitHub (continuing anyway)"
        return 0
    fi

    # Extract version from the remote script
    local latest_version
    latest_version=$(echo "$remote_content" | grep -m1 "^readonly SCRIPT_VERSION=" | sed 's/readonly SCRIPT_VERSION="\(.*\)"/\1/' 2>/dev/null) || true

    if [[ -z "$latest_version" ]]; then
        log "⚠ Could not parse version from remote script (continuing anyway)"
        return 0
    fi

    log "Current version: $SCRIPT_VERSION"
    log "Latest version: $latest_version"

    # Compare versions
    if [[ "$SCRIPT_VERSION" != "$latest_version" ]]; then
        # Simple version comparison (works for semantic versioning)
        if printf '%s\n' "$latest_version" "$SCRIPT_VERSION" | sort -V | head -n1 | grep -q "^$SCRIPT_VERSION$" 2>/dev/null || true; then
            log "⚠ New version available: $latest_version"
            notify "mover-tuning-end.sh Update" "Version $latest_version available (current: $SCRIPT_VERSION)<br><br>📖 Visit the TRaSH-Guides for the latest version"
        fi
    else
        log "✓ Script is up to date"
    fi

    return 0
}

# ================================
# AUTO-INSTALLER FUNCTIONS
# ================================
install_fclones_binary() {
    log "Installing/updating fclones binary..."

    # fclones configuration
    local FCLONES_BIN="/usr/local/bin/fclones"
    local BOOT_DIR="/boot/config/plugins/fclones/usr/bin"
    local GO_FILE="/boot/config/go"
    local DEFAULT_VERSION="0.35.0"

    # Current installed version
    local CURRENT_VERSION=""
    if [[ -x "$FCLONES_BIN" ]]; then
        CURRENT_VERSION=$($FCLONES_BIN --version 2>/dev/null | awk '{print $2}') || true
        log "✓ Found fclones version $CURRENT_VERSION"
    else
        log "✗ fclones not found"
    fi

    # Check for curl or wget
    local GITHUB_API_CMD
    if command -v curl >/dev/null 2>&1; then
        GITHUB_API_CMD="curl -s https://api.github.com/repos/pkolaczk/fclones/releases/latest"
    elif command -v wget >/dev/null 2>&1; then
        GITHUB_API_CMD="wget -qO- https://api.github.com/repos/pkolaczk/fclones/releases/latest"
    else
        log "✗ Neither curl nor wget is available (continuing anyway)"
        return 0
    fi

    # Fetch latest release from GitHub
    local LATEST_VERSION
    LATEST_VERSION=$($GITHUB_API_CMD 2>/dev/null | grep -Po '"tag_name": "\K.*?(?=")') || true
    if [[ -z "$LATEST_VERSION" ]]; then
        log "⚠ Could not fetch latest release, using default version $DEFAULT_VERSION (continuing anyway)"
        LATEST_VERSION="$DEFAULT_VERSION"
    else
        log "Latest fclones release: $LATEST_VERSION"
    fi

    # Compare and install if missing or outdated
    if [[ "$CURRENT_VERSION" != "$LATEST_VERSION" ]]; then
        log "Installing/updating fclones to $LATEST_VERSION..."

        local TMP_DIR
        TMP_DIR=$(mktemp -d)

        # Remove leading 'v' from filename
        local VERSION_NO_V="${LATEST_VERSION#v}"
        local DOWNLOAD_URL="https://github.com/pkolaczk/fclones/releases/download/$LATEST_VERSION/fclones-$VERSION_NO_V-linux-glibc-x86_64.tar.gz"

        if ! wget -O "$TMP_DIR/fclones.tar.gz" "$DOWNLOAD_URL" 2>/dev/null; then
            log "✗ Failed to download fclones from $DOWNLOAD_URL (continuing anyway)"
            rm -rf "$TMP_DIR"
            return 0
        fi

        if ! tar -xzf "$TMP_DIR/fclones.tar.gz" -C "$TMP_DIR" 2>/dev/null; then
            log "✗ Failed to extract fclones archive (continuing anyway)"
            rm -rf "$TMP_DIR"
            return 0
        fi

        mkdir -p "$BOOT_DIR" || true
        cp "$TMP_DIR/usr/bin/fclones" "$BOOT_DIR/fclones" 2>/dev/null || true
        chmod +x "$BOOT_DIR/fclones" 2>/dev/null || true

        # Copy to /usr/local/bin immediately
        cp "$BOOT_DIR/fclones" /usr/local/bin/fclones 2>/dev/null || true
        chmod +x /usr/local/bin/fclones 2>/dev/null || true

        # Add boot-time copy and PATH setup if not already in /boot/config/go
        if ! grep -q "fclones boot-time setup" "$GO_FILE" 2>/dev/null; then
            if [ -w "$GO_FILE" ]; then
                echo "" >> "$GO_FILE"
                echo "# fclones boot-time setup" >> "$GO_FILE"
                echo "export PATH=/usr/local/bin:\$PATH" >> "$GO_FILE"
                echo "cp $BOOT_DIR/fclones /usr/local/bin/fclones" >> "$GO_FILE"
            else
                log "⚠ Cannot write to $GO_FILE. Please check permissions. (continuing anyway)"
            fi
        fi

        rm -rf "$TMP_DIR"
        log "✓ fclones $VERSION_NO_V installed successfully"
        return 0
    else
        log "✓ fclones is up to date ($CURRENT_VERSION)"
        return 0
    fi
}

install_fclones_script() {
    log "Installing fclones.sh script..."

    local raw_script_url="https://gist.githubusercontent.com/BaukeZwart/b570ce6b6165c4f0b64c5b98d9d3af1e/raw"
    local script_path="${QBIT_MOVER_PATH}fclones.sh"

    # Create directory if needed
    mkdir -p "$QBIT_MOVER_PATH"

    # Download script
    if command -v curl &> /dev/null; then
        if ! curl -fsSL "$raw_script_url" -o "$script_path" 2>/dev/null; then
            log "✗ Failed to download fclones.sh script"
            return 1
        fi
    elif command -v wget &> /dev/null; then
        if ! wget -q "$raw_script_url" -O "$script_path" 2>/dev/null; then
            log "✗ Failed to download fclones.sh script"
            return 1
        fi
    else
        log "✗ Neither curl nor wget is available"
        return 1
    fi

    # Set permissions
    chmod +x "$script_path"
    chown nobody:users "$script_path" 2>/dev/null || \
        log "⚠ Warning: Could not set ownership to nobody:users"

    log "✓ fclones.sh script installed at $script_path"
    return 0
}

check_and_install_fclones() {
    log "Checking fclones installation..."

    local need_install=false

    # Check binary
    if ! command -v fclones &> /dev/null; then
        log "✗ fclones binary not found"
        if ! install_fclones_binary; then
            notify "fclones Auto-Installer" "Failed to install binary @ $(date +%H:%M:%S)"
            return 1
        fi
        need_install=true
    else
        # Check if update is needed
        if ! install_fclones_binary; then
            log "⚠ Failed to check/update fclones binary (continuing anyway)"
        fi
    fi

    # Check script
    if [[ ! -f "${QBIT_MOVER_PATH}fclones.sh" ]]; then
        log "✗ fclones.sh script not found"
        if ! install_fclones_script; then
            notify "fclones Auto-Installer" "Failed to install script @ $(date +%H:%M:%S)"
            return 1
        fi
        need_install=true
    else
        log "✓ fclones.sh script found"
    fi

    if [[ "$need_install" == true ]]; then
        log "✓ fclones installation completed"
        notify "fclones Auto-Installer" "Installation completed @ $(date +%H:%M:%S)"
    fi

    return 0
}

# ================================
# VALIDATION
# ================================
validate_config() {
    log "Validating configuration..."

    # Check required commands
    local missing_cmds=()
    for cmd in python3 date; do
        command -v "$cmd" &> /dev/null || missing_cmds+=("$cmd")
    done

    if [[ ${#missing_cmds[@]} -gt 0 ]]; then
        error "Missing required commands: ${missing_cmds[*]}"
    fi

    # Check docker if needed
    if [[ "$ENABLE_QBIT_MANAGE" == true ]] && ! command -v docker &> /dev/null; then
        error "docker is required when ENABLE_QBIT_MANAGE=true"
    fi

    # Validate paths and values
    [[ "$DAYS_FROM" -ge 2 ]] || error "DAYS_FROM must be at least 2"
    [[ "$DAYS_TO" -ge "$DAYS_FROM" ]] || error "DAYS_TO must be >= DAYS_FROM"
    [[ -d "$CACHE_MOUNT" ]] || error "Cache mount not found: $CACHE_MOUNT"
    [[ -f "${QBIT_MOVER_PATH}mover.py" ]] || error "mover.py not found: ${QBIT_MOVER_PATH}mover.py"

    # Validate duplicate finder if enabled
    if [[ "$ENABLE_DUPLICATE_FINDER" == true ]]; then
        if [[ "$ENABLE_AUTO_INSTALLER" == true ]]; then
            check_and_install_fclones || return 1
        else
            [[ -f "${QBIT_MOVER_PATH}fclones.sh" ]] || \
                error "Duplicate finder script not found: ${QBIT_MOVER_PATH}fclones.sh"
            [[ -x "${QBIT_MOVER_PATH}fclones.sh" ]] || \
                error "Duplicate finder script not executable: ${QBIT_MOVER_PATH}fclones.sh"
        fi
    fi

    log "✓ Validation completed"
}

# ================================
# PROCESS QBITTORRENT INSTANCE
# ================================
process_qbit_instance() {
    local name="$1"
    local host="$2"
    local user="$3"
    local password="$4"

    log "Processing $name..."

    # Determine Python command
    local python_cmd
    if [[ -f "${QBIT_MOVER_PATH}.venv/bin/python3" ]]; then
        python_cmd="${QBIT_MOVER_PATH}.venv/bin/python3"
        log "✓ Using virtual environment"
    elif python3 -c "import qbittorrentapi" 2>/dev/null; then
        python_cmd="python3"
        log "✓ Using system Python"
    else
        log "✗ qbittorrent-api not found"
        return 1
    fi

    # Execute mover script
    if "$python_cmd" "${QBIT_MOVER_PATH}mover.py" \
        --resume \
        --host "$host" \
        --user "$user" \
        --password "$password" \
        --days_from "$DAYS_FROM" \
        --days_to "$DAYS_TO"; then
        log "✓ Successfully resumed torrents for $name"
        notify "$name" "Resumed @ $(date +%H:%M:%S)"
        return 0
    else
        log "✗ Failed to resume torrents for $name"
        return 1
    fi
}

# ================================
# MAIN EXECUTION
# ================================
main() {
    local failed_instances=0
    local date_str
    date_str=$(date --date="$DAYS_FROM day ago" +%F)

    log "========================================"
    log "Starting torrent resume process"
    log "Age range: $DAYS_FROM-$DAYS_TO days (from $date_str)"
    log "========================================"

    # Check for script updates
    check_script_version

    # Validate configuration
    validate_config || exit 1

    # Process primary instance
    process_qbit_instance "$QBIT_NAME_1" "$QBIT_HOST_1" "$QBIT_USER_1" "$QBIT_PASS_1" || \
        ((failed_instances++))

    # Process secondary instance if enabled
    if [[ "$ENABLE_QBIT_2" == true ]]; then
        log "Processing secondary instance..."
        process_qbit_instance "$QBIT_NAME_2" "$QBIT_HOST_2" "$QBIT_USER_2" "$QBIT_PASS_2" || \
            ((failed_instances++))
    else
        log "Secondary instance disabled"
    fi

    # Run duplicate finder if enabled
    if [[ "$ENABLE_DUPLICATE_FINDER" == true ]]; then
        log "Running duplicate finder..."
        if bash "${QBIT_MOVER_PATH}fclones.sh"; then
            log "✓ $DUPLICATE_FINDER_NAME completed"
            notify "$DUPLICATE_FINDER_NAME" "Completed @ $(date +%H:%M:%S)"
        else
            log "⚠ $DUPLICATE_FINDER_NAME failed"
            notify "$DUPLICATE_FINDER_NAME" "Failed @ $(date +%H:%M:%S)"
        fi
    fi

    # Start qBit-Manage if enabled
    if [[ "$ENABLE_QBIT_MANAGE" == true ]]; then
        log "Starting qBit-Manage container..."
        if docker start "$QBIT_MANAGE_CONTAINER" &> /dev/null; then
            log "✓ qBit-Manage started"
            notify "qBit-Manage" "Started @ $(date +%H:%M:%S)"
        else
            log "⚠ Failed to start qBit-Manage"
        fi
    fi

    # Summary
    log "========================================"
    if [[ $failed_instances -eq 0 ]]; then
        log "✓ All operations completed successfully"
        exit 0
    else
        log "⚠ Completed with $failed_instances failed instance(s)"
        exit 1
    fi
}

# Run main function
main

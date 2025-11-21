#!/bin/bash
set -euo pipefail # Exit on error, undefined variables, and pipe failures

# =======================================
# Script: qBittorrent Cache Mover - Start
# Version: 1.0.0
# Updated: 20251121
# =======================================

# Script version and update check URLs
readonly SCRIPT_VERSION="1.0.0"
readonly SCRIPT_RAW_URL="https://raw.githubusercontent.com/TRaSH-Guides/Guides/refs/heads/master/includes/downloaders/mover-tuning-start.sh"
readonly CONFIG_RAW_URL="https://raw.githubusercontent.com/TRaSH-Guides/Guides/refs/heads/master/includes/downloaders/mover-tuning.cfg"

# Get the directory where the script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Source the config from the same directory
source "$SCRIPT_DIR/mover-tuning.cfg"

readonly VENV_PATH="${QBIT_MOVER_PATH}.venv"
readonly MOVER_SCRIPT="${QBIT_MOVER_PATH}mover.py"
readonly MOVER_URL="https://raw.githubusercontent.com/StuffAnThings/qbit_manage/develop/scripts/mover.py"

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

check_command() {
    command -v "$1" &> /dev/null
}

set_ownership() {
    chown -R nobody:users "$1" 2>/dev/null || log "⚠ Warning: Could not set ownership for $1"
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
            notify "mover-tuning-start.sh Update" "Version $latest_version available (current: $SCRIPT_VERSION)<br><br>📖 Visit the TRaSH-Guides for the latest version"
        fi
    else
        log "✓ Script is up to date"
    fi

    return 0
}

check_config_version() {
    log "Checking for config file updates..."

    # Check if version check is enabled
    if [[ "${ENABLE_VERSION_CHECK:-true}" != "true" ]]; then
        log "Config version check disabled"
        return 0
    fi

    # Check for curl or wget
    local fetch_cmd
    if command -v curl &> /dev/null; then
        fetch_cmd="curl -s"
    elif command -v wget &> /dev/null; then
        fetch_cmd="wget -qO-"
    else
        log "⚠ Cannot check config version: curl or wget not found (continuing anyway)"
        return 0
    fi

    # Fetch the latest config from GitHub
    local remote_config
    remote_config=$($fetch_cmd "$CONFIG_RAW_URL" 2>/dev/null) || true

    if [[ -z "$remote_config" ]]; then
        log "⚠ Could not fetch latest config from GitHub (continuing anyway)"
        return 0
    fi

    # Extract version from the remote config
    local remote_config_version
    remote_config_version=$(echo "$remote_config" | grep -m1 "^readonly CONFIG_VERSION=" | sed 's/readonly CONFIG_VERSION="\([^"]*\)".*/\1/' 2>/dev/null) || true

    if [[ -z "$remote_config_version" ]]; then
        log "⚠ Could not parse version from remote config (continuing anyway)"
        return 0
    fi

    # Get current config version (handle case where it might not be set)
    local current_config_version="${CONFIG_VERSION:-unknown}"

    log "Current config version: $current_config_version"
    log "Latest config version: $remote_config_version"

    # Compare versions
    if [[ "$current_config_version" != "$remote_config_version" ]]; then
        # Simple version comparison (works for semantic versioning)
        if printf '%s\n' "$remote_config_version" "$current_config_version" | sort -V | head -n1 | grep -q "^$current_config_version$" 2>/dev/null || true; then
            log "⚠ New config version available: $remote_config_version"
            notify "mover-tuning.cfg Update" "Config version <b>$remote_config_version</b> available<br>Current version: <b>$current_config_version</b><br><br>📖 Visit the TRaSH-Guides for the latest version"
        fi
    else
        log "✓ Config is up to date"
    fi

    return 0
}

# ================================
# AUTO INSTALLER FUNCTION
# ================================
run_auto_installer() {
    log "========================================"
    log "Running qBit-Api and qBit-Mover Auto Installer"
    log "========================================"

    # Create QBIT_MOVER_PATH directory if needed
    if [[ ! -d "$QBIT_MOVER_PATH" ]]; then
        mkdir -p "$QBIT_MOVER_PATH" || error "Failed to create $QBIT_MOVER_PATH"
        set_ownership "$QBIT_MOVER_PATH"
        log "✓ Created $QBIT_MOVER_PATH"
    fi

    # Create virtual environment if needed
    if [[ ! -d "$VENV_PATH" ]]; then
        log "Creating virtual environment..."
        python3 -m venv "$VENV_PATH" || error "Failed to create virtual environment"
        set_ownership "$VENV_PATH"
        log "✓ Virtual environment created"
    else
        log "✓ Virtual environment exists"
    fi

    # Activate virtual environment
    # shellcheck source=/dev/null
    source "${VENV_PATH}/bin/activate" || error "Failed to activate virtual environment"

    # Upgrade pip if needed
    log "Checking pip version..."
    if pip3 install --upgrade pip --quiet 2>&1 | grep -q "Successfully installed"; then
        log "✓ Pip upgraded to $(pip3 --version | awk '{print $2}')"
        set_ownership "$VENV_PATH"
    else
        log "✓ Pip is up to date"
    fi

    # Install/upgrade qbittorrent-api
    if python3 -c "import qbittorrentapi" 2>/dev/null; then
        log "✓ qbittorrent-api installed ($(pip3 show qbittorrent-api 2>/dev/null | awk '/Version:/ {print $2}'))"

        # Check for updates
        if pip3 install --dry-run --upgrade qbittorrent-api 2>&1 | grep -q "Would install"; then
            log "Upgrading qbittorrent-api..."
            pip3 install qbittorrent-api --upgrade --quiet || log "⚠ Warning: Failed to upgrade qbittorrent-api"
            set_ownership "$VENV_PATH"
            log "✓ qbittorrent-api upgraded"
        else
            log "✓ qbittorrent-api is up to date"
        fi
    else
        log "Installing qbittorrent-api..."
        pip3 install qbittorrent-api --quiet || error "Failed to install qbittorrent-api"
        set_ownership "$VENV_PATH"
        log "✓ qbittorrent-api installed"
    fi

    deactivate

    # Download mover.py if needed
    if [[ ! -f "$MOVER_SCRIPT" ]]; then
        log "Downloading mover.py..."
        if curl -sSL "$MOVER_URL" -o "$MOVER_SCRIPT"; then
            chmod +x "$MOVER_SCRIPT"
            set_ownership "$MOVER_SCRIPT"
            log "✓ mover.py downloaded"
        else
            error "Failed to download mover.py"
        fi
    else
        log "✓ mover.py exists"
    fi

    log "========================================"
    log "Auto Installer completed"
    log "========================================"
}

# ================================
# VALIDATION
# ================================
validate_config() {
    log "Validating configuration..."

    # Check required commands
    for cmd in python3 date curl; do
        check_command "$cmd" || error "$cmd is not installed"
    done

    # Validate docker if needed
    if [[ "$ENABLE_QBIT_MANAGE" == true ]]; then
        check_command docker || error "docker is required when ENABLE_QBIT_MANAGE=true"
    fi

    # Validate settings
    [[ "$DAYS_FROM" -ge 2 ]] || error "DAYS_FROM must be at least 2"
    [[ "$DAYS_TO" -ge "$DAYS_FROM" ]] || error "DAYS_TO must be >= DAYS_FROM"
    [[ -d "$CACHE_MOUNT" ]] || error "Cache mount does not exist: $CACHE_MOUNT"
}

# ================================
# PROCESS QBITTORRENT INSTANCE
# ================================
process_qbit_instance() {
    local name="$1" host="$2" user="$3" password="$4"

    log "Processing $name..."

    # Determine Python command
    local python_cmd
    if [[ -f "${VENV_PATH}/bin/python3" ]]; then
        python_cmd="${VENV_PATH}/bin/python3"
    elif python3 -c "import qbittorrentapi" 2>/dev/null; then
        python_cmd="python3"
    else
        log "✗ qbittorrent-api not found for $name"
        return 1
    fi

    # Run mover script
    if $python_cmd "$MOVER_SCRIPT" \
        --pause \
        --host "$host" \
        --user "$user" \
        --password "$password" \
        --cache-mount "$CACHE_MOUNT" \
        --days_from "$DAYS_FROM" \
        --days_to "$DAYS_TO" 2>&1 | while IFS= read -r line; do
            log "  $line"
        done; then
        log "✓ Successfully processed $name"
        notify "$name" "Paused @ $(date +%H:%M:%S)"
        return 0
    else
        log "✗ Failed to process $name"
        return 1
    fi
}

# ================================
# MAIN EXECUTION
# ================================
main() {
    local failed_instances=0
    readonly date_from=$(date --date="$DAYS_FROM day ago" +%F)

    log "========================================"
    log "qBittorrent Cache Mover Started"
    log "Date range: $DAYS_FROM-$DAYS_TO days (from $date_from)"
    log "========================================"

    # Check for script updates
    check_script_version

    # Check for config updates
    check_config_version

    # Run auto installer if enabled
    [[ "$ENABLE_AUTO_INSTALLER" == true ]] && run_auto_installer

    # Validate configuration
    validate_config
    [[ -f "$MOVER_SCRIPT" ]] || error "mover.py not found at: $MOVER_SCRIPT"

    # Stop qBit-Manage if enabled
    if [[ "$ENABLE_QBIT_MANAGE" == true ]]; then
        log "Stopping $QBIT_MANAGE_CONTAINER..."
        if docker stop "$QBIT_MANAGE_CONTAINER" &> /dev/null; then
            log "✓ Stopped qBit-Manage"
            notify "qBit-Manage" "Stopped @ $(date +%H:%M:%S)"
            sleep "$QBIT_MANAGE_WAIT"
        else
            log "⚠ Warning: Failed to stop $QBIT_MANAGE_CONTAINER"
        fi
    fi

    # Process instances
    process_qbit_instance "$QBIT_NAME_1" "$QBIT_HOST_1" "$QBIT_USER_1" "$QBIT_PASS_1" || ((failed_instances++))

    if [[ "$ENABLE_QBIT_2" == true ]]; then
        process_qbit_instance "$QBIT_NAME_2" "$QBIT_HOST_2" "$QBIT_USER_2" "$QBIT_PASS_2" || ((failed_instances++))
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

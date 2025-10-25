#!/bin/bash
set -euo pipefail  # Exit on error, undefined variables, and pipe failures

# ================================
# Script: qBittorrent Cache Mover
# Updated: 20251025
# ================================

# ================================
# USER CONFIGURATION
# ================================
readonly DAYS_FROM=25  # Minimum age (days) before torrents are paused and moved
readonly DAYS_TO=99    # Maximum age (days) for torrent selection
readonly CACHE_MOUNT="/mnt/cache/"  # Cache mount point in Unraid
readonly QBIT_MOVER_PATH="/mnt/user/appdata/qbt-mover/"  # Path to mover.py

# Primary qBittorrent instance (REQUIRED)
readonly QBIT_NAME_1="qBit-Movies"  # qBittorrent instance name
readonly QBIT_HOST_1="192.168.2.200:8800"  # qBittorrent host:port
readonly QBIT_USER_1="admin"  # qBittorrent username
readonly QBIT_PASS_1="qbt1-password"  # qBittorrent password

# Secondary qBittorrent instance (OPTIONAL)
readonly ENABLE_QBIT_2=true  # Set to true to enable secondary instance
readonly QBIT_NAME_2="qBit-TV"  # qBittorrent instance name
readonly QBIT_HOST_2="192.168.2.200:8811"  # qBittorrent host:port
readonly QBIT_USER_2="admin"  # qBittorrent username
readonly QBIT_PASS_2="qbt2-password"  # qBittorrent password

# qBit-Manage integration (OPTIONAL)
readonly ENABLE_QBIT_MANAGE=true  # Set to true to enable qBit-Manage
readonly QBIT_MANAGE_CONTAINER="qbit-manage"  # qBit-Manage Docker container name

# Duplicate finder script (OPTIONAL) Replace copies with hardlinks
# fclones => https://gist.github.com/BaukeZwart/b570ce6b6165c4f0b64c5b98d9d3af1e
# jdupes => https://codeberg.org/jbruchon/jdupes
readonly ENABLE_DUPLICATE_FINDER=true  # Set to true to enable duplicate finder
readonly DUPLICATE_FINDER_SCRIPT="/mnt/user/appdata/qbt-mover/fclones.sh"  # Full path to jdupes or fclones script (e.g., "/mnt/user/appdata/qbt-mover/fclones.sh")
readonly DUPLICATE_FINDER_NAME="Duplicate Finder"  # Name for logging/notifications

# ============================================
# <----- DO NOT MODIFY BELOW THIS POINT ----->
# ============================================
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
    if command -v /usr/local/emhttp/plugins/dynamix/scripts/notify &> /dev/null; then
        /usr/local/emhttp/plugins/dynamix/scripts/notify -s "$subject" -d "$description"
    fi
}

# ================================
# VALIDATION
# ================================
log "Validating configuration and dependencies..."

# Validate required commands
for cmd in python3 date; do
    command -v "$cmd" &> /dev/null || error "$cmd is not installed or not in PATH"
done

# Validate docker if qBit-Manage is enabled
if [[ "$ENABLE_QBIT_MANAGE" == true ]]; then
    command -v docker &> /dev/null || error "docker is required when ENABLE_QBIT_MANAGE=true"
fi

# Validate duplicate finder script if enabled
if [[ "$ENABLE_DUPLICATE_FINDER" == true ]]; then
    [[ -n "$DUPLICATE_FINDER_SCRIPT" ]] || error "DUPLICATE_FINDER_SCRIPT must be set when ENABLE_DUPLICATE_FINDER=true"
    [[ -f "$DUPLICATE_FINDER_SCRIPT" ]] || error "Duplicate finder script not found: $DUPLICATE_FINDER_SCRIPT"
    [[ -x "$DUPLICATE_FINDER_SCRIPT" ]] || error "Duplicate finder script is not executable: $DUPLICATE_FINDER_SCRIPT"
fi

# Validate configuration
[[ "$DAYS_FROM" -ge 2 ]] || error "DAYS_FROM must be at least 2"
[[ "$DAYS_TO" -ge "$DAYS_FROM" ]] || error "DAYS_TO must be greater than or equal to DAYS_FROM"
[[ -d "$CACHE_MOUNT" ]] || error "Cache mount directory does not exist: $CACHE_MOUNT"
[[ -f "${QBIT_MOVER_PATH}mover.py" ]] || error "mover.py not found at: ${QBIT_MOVER_PATH}mover.py"

# ================================
# PROCESS QBITTORRENT INSTANCE
# ================================
process_qbit_instance() {
    local name="$1"
    local host="$2"
    local user="$3"
    local password="$4"

    log "Processing $name instance..."

    if python3 "${QBIT_MOVER_PATH}mover.py" \
        --resume \
        --host "$host" \
        --user "$user" \
        --password "$password" \
        --cache-mount "$CACHE_MOUNT" \
        --days_from "$DAYS_FROM" \
        --days_to "$DAYS_TO"; then

        log "✓ Successfully resumed paused torrents for $name"
        notify "$name" "Resumed paused @ $(date +%H:%M:%S)"
        return 0
    else
        log "✗ Failed to resume paused torrents for $name"
        return 1
    fi
}

# ================================
# MAIN SCRIPT
# ================================
readonly DATE=$(date --date="$DAYS_FROM day ago" +%F)
log "Starting torrent resume process for torrents between $DAYS_FROM and $DAYS_TO days (from $DATE)"

# Track overall success
failed_instances=0

# Process primary instance
process_qbit_instance \
    "$QBIT_NAME_1" \
    "$QBIT_HOST_1" \
    "$QBIT_USER_1" \
    "$QBIT_PASS_1" || ((failed_instances++))

# Process secondary instance if enabled
if [[ "$ENABLE_QBIT_2" == true ]]; then
    log "Secondary instance enabled, processing $QBIT_NAME_2..."
    process_qbit_instance \
        "$QBIT_NAME_2" \
        "$QBIT_HOST_2" \
        "$QBIT_USER_2" \
        "$QBIT_PASS_2" || ((failed_instances++))
else
    log "Secondary instance disabled, skipping $QBIT_NAME_2"
fi

# Run duplicate finder script if enabled
if [[ "$ENABLE_DUPLICATE_FINDER" == true ]]; then
    log "Running duplicate finder script: $DUPLICATE_FINDER_SCRIPT"
    if bash "$DUPLICATE_FINDER_SCRIPT"; then
        log "✓ Successfully completed $DUPLICATE_FINDER_NAME"
        notify "$DUPLICATE_FINDER_NAME" "Completed @ $(date +%H:%M:%S)"
    else
        log "⚠ Warning: $DUPLICATE_FINDER_NAME script failed or returned non-zero exit code"
        notify "$DUPLICATE_FINDER_NAME" "Failed @ $(date +%H:%M:%S)"
    fi
else
    log "Duplicate finder disabled, skipping"
fi

# Start qBit-Manage if enabled
if [[ "$ENABLE_QBIT_MANAGE" == true ]]; then
    log "Starting qBit-Manage container: $QBIT_MANAGE_CONTAINER"
    if docker start "$QBIT_MANAGE_CONTAINER" &> /dev/null; then
        log "✓ Successfully started qBit-Manage"
        notify "qBit-Manage" "Started @ $(date +%H:%M:%S)"
    else
        log "⚠ Warning: Failed to start qBit-Manage container"
    fi
else
    log "qBit-Manage disabled, skipping"
fi

# Final summary
log "========================================"
if [[ $failed_instances -eq 0 ]]; then
    log "✓ All operations completed successfully"
    exit 0
else
    log "⚠ Completed with $failed_instances failed instance(s)"
    exit 1
fi

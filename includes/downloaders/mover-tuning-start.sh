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
readonly ENABLE_QBIT_MANAGE=true  # Set to false to disable qBit-Manage
readonly QBIT_MANAGE_CONTAINER="qbit-manage"  # qBit-Manage Docker container name

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
        --pause \
        --host "$host" \
        --user "$user" \
        --password "$password" \
        --cache-mount "$CACHE_MOUNT" \
        --days_from "$DAYS_FROM" \
        --days_to "$DAYS_TO"; then

        log "✓ Successfully paused torrents for $name"
        notify "$name" "Paused @ $(date +%H:%M:%S)"
        return 0
    else
        log "✗ Failed to pause torrents for $name"
        return 1
    fi
}

# ================================
# MAIN SCRIPT
# ================================
readonly DATE=$(date --date="$DAYS_FROM day ago" +%F)
log "Starting torrent pause process for torrents between $DAYS_FROM and $DAYS_TO days (from $DATE)"

# Track overall success
failed_instances=0

# Stop qBit-Manage if enabled
if [[ "$ENABLE_QBIT_MANAGE" == true ]]; then
    log "Stopping qBit-Manage container: $QBIT_MANAGE_CONTAINER"
    if docker stop "$QBIT_MANAGE_CONTAINER" &> /dev/null; then
        log "✓ Successfully stopped qBit-Manage"
        notify "qBit-Manage" "Stopped @ $(date +%H:%M:%S)"

        # Wait a moment for qBit-Manage to initialize
        log "Waiting for qBit-Manage to process..."
        sleep 5
    else
        log "⚠ Warning: Failed to stop qBit-Manage container"
    fi
else
    log "qBit-Manage disabled, skipping"
fi

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

# Final summary
log "========================================"
if [[ $failed_instances -eq 0 ]]; then
    log "✓ All operations completed successfully"
    exit 0
else
    log "⚠ Completed with $failed_instances failed instance(s)"
    exit 1
fi

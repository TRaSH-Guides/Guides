#!/bin/bash

# ================================
# <----- USER CONFIGURATION ----->
# ================================

QBIT_MOVER_PATH="/mnt/user/appdata/qbt-mover/"

# ============================================
# <----- DO NOT MODIFY BELOW THIS POINT ----->
# ============================================

VENV_PATH="${QBIT_MOVER_PATH}/.venv"

# Create QBIT_MOVER_PATH directory if it doesn't exist and set ownership
if [ ! -d "${QBIT_MOVER_PATH}" ]; then
    mkdir -p "${QBIT_MOVER_PATH}"
    chown nobody:users "${QBIT_MOVER_PATH}"
    echo "Created ${QBIT_MOVER_PATH} with nobody:users ownership"
fi

# Check if virtual environment exists
if [ ! -d "${VENV_PATH}" ]; then
    echo "Virtual environment not found. Creating..."
    python3 -m venv "${VENV_PATH}"
    echo "Virtual environment created at ${VENV_PATH}"
    chown -R nobody:users "${VENV_PATH}"
    echo "Ownership set to nobody:users for ${VENV_PATH}"
else
    echo "Virtual environment already exists"
fi

# Activate virtual environment
source "${VENV_PATH}/bin/activate"

# Check and upgrade pip if needed
echo "Checking pip version..."
CURRENT_PIP=$(pip3 --version | awk '{print $2}')
echo "Current pip version: $CURRENT_PIP"

pip3 install --upgrade pip --quiet 2>&1 | grep -q "Successfully installed" && {
    NEW_PIP=$(pip3 --version | awk '{print $2}')
    echo "Pip upgraded to version: $NEW_PIP"
    chown -R nobody:users "${VENV_PATH}"
    echo "Ownership updated for ${VENV_PATH}"
} || {
    echo "Pip is already up to date"
}

# Check if qbittorrent-api is installed
if python3 -c "import qbittorrentapi" 2>/dev/null; then
    echo "qbittorrent-api is already installed"

    # Get current version using pip
    CURRENT_VERSION=$(pip3 show qbittorrent-api 2>/dev/null | grep "Version:" | awk '{print $2}')
    if [ -n "${CURRENT_VERSION}" ]; then
        echo "Current version: ${CURRENT_VERSION}"
    else
        echo "Could not determine current version"
    fi

    # Check for updates
    echo "Checking for updates..."
    pip3 install --dry-run --upgrade qbittorrent-api 2>&1 | grep -q "Would install" && {
        echo "Update available. Upgrading..."
        pip3 install qbittorrent-api --upgrade
        chown -R nobody:users "${VENV_PATH}"
        echo "Ownership updated for ${VENV_PATH}"
    } || {
        echo "Already up to date"
    }
else
    echo "qbittorrent-api not found. Installing..."
    pip3 install qbittorrent-api
    chown -R nobody:users "${VENV_PATH}"
    echo "Ownership set for ${VENV_PATH}"
fi

# Deactivate virtual environment
deactivate

# Check if mover.py exists
MOVER_SCRIPT="${QBIT_MOVER_PATH}mover.py"
if [ ! -f "${MOVER_SCRIPT}" ]; then
    echo "mover.py not found. Downloading..."

    # Create directory if it doesn't exist (already handled above, but kept for safety)
    mkdir -p "${QBIT_MOVER_PATH}"

    # Download mover.py from GitHub (raw URL)
    curl -sSL "https://raw.githubusercontent.com/StuffAnThings/qbit_manage/develop/scripts/mover.py" -o "${MOVER_SCRIPT}"

    if [ -f "${MOVER_SCRIPT}" ]; then
        # Make it executable and set ownership
        chmod +x "${MOVER_SCRIPT}"
        chown nobody:users "${MOVER_SCRIPT}"
        echo "mover.py downloaded, made executable, and ownership set to nobody:users"
    else
        echo "ERROR: Failed to download mover.py"
    fi
fi

echo "Done!"


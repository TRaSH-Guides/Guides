#!/bin/bash
# =================================================
# fclones auto-install & update check for Unraid
# =================================================

FCLONES_BIN="/usr/local/bin/fclones"
BOOT_DIR="/boot/config/plugins/fclones/usr/bin"
GO_FILE="/boot/config/go"
DEFAULT_VERSION="0.35.0"

check_and_install_fclones() {
    echo "Checking fclones installation..."

    # Current installed version
    if [[ -x "$FCLONES_BIN" ]]; then
        CURRENT_VERSION=$($FCLONES_BIN --version 2>/dev/null | awk '{print $2}')
        echo "Found fclones version $CURRENT_VERSION"
    else
        CURRENT_VERSION=""
        echo "fclones not found, installing..."
    fi

    # Check for curl or wget
    if command -v curl >/dev/null 2>&1; then
        GITHUB_API_CMD="curl -s https://api.github.com/repos/pkolaczk/fclones/releases/latest"
    elif command -v wget >/dev/null 2>&1; then
        GITHUB_API_CMD="wget -qO- https://api.github.com/repos/pkolaczk/fclones/releases/latest"
    else
        echo "Error: Neither 'curl' nor 'wget' is installed. Please install one of them to continue."
        exit 1
    fi

    # Fetch latest release from GitHub
    LATEST_VERSION=$($GITHUB_API_CMD | grep -Po '"tag_name": "\K.*?(?=")')
    if [[ -z "$LATEST_VERSION" ]]; then
        echo "Could not fetch latest release, using default version $DEFAULT_VERSION"
        LATEST_VERSION="$DEFAULT_VERSION"
    else
        echo "Latest fclones release: $LATEST_VERSION"
    fi

    # Compare and install if missing or outdated
    if [[ "$CURRENT_VERSION" != "$LATEST_VERSION" ]]; then
        echo "Installing/updating fclones to $LATEST_VERSION..."
        TMP_DIR=$(mktemp -d)
        # Remove leading 'v' from filename
        VERSION_NO_V="${LATEST_VERSION#v}"
        DOWNLOAD_URL="https://github.com/pkolaczk/fclones/releases/download/$LATEST_VERSION/fclones-$VERSION_NO_V-linux-glibc-x86_64.tar.gz"

        wget -O "$TMP_DIR/fclones.tar.gz" "$DOWNLOAD_URL"
        if [[ $? -ne 0 ]]; then
            echo "ERROR: Failed to download fclones from $DOWNLOAD_URL"
            rm -rf "$TMP_DIR"
            return 1
        fi

        tar -xzf "$TMP_DIR/fclones.tar.gz" -C "$TMP_DIR"
        mkdir -p "$BOOT_DIR"
        cp "$TMP_DIR/usr/bin/fclones" "$BOOT_DIR/fclones"
        chmod +x "$BOOT_DIR/fclones"

        # Copy to /usr/local/bin immediately
        cp "$BOOT_DIR/fclones" /usr/local/bin/fclones
        chmod +x /usr/local/bin/fclones

        # Add boot-time copy and PATH setup if not already in /boot/config/go
        if ! grep -q "fclones boot-time setup" "$GO_FILE"; then
            if [ ! -w "$GO_FILE" ]; then
                echo "Error: Cannot write to $GO_FILE. Please check permissions." >&2
                exit 1
            fi
            echo "" >> "$GO_FILE"
            echo "# fclones boot-time setup" >> "$GO_FILE"
            echo "export PATH=/usr/local/bin:\$PATH" >> "$GO_FILE"
            echo "cp $BOOT_DIR/fclones /usr/local/bin/fclones" >> "$GO_FILE"
        fi

        rm -rf "$TMP_DIR"
        echo "fclones $VERSION_NO_V installed successfully."
    else
        echo "fclones is up to date ($CURRENT_VERSION)."
    fi
}

# Call function before running main script
check_and_install_fclones

#!/usr/bin/env python3

##############################################################################
### NZBGET SCAN SCRIPT                                                     ###

# Clean NZB name.
#
# Removes the following suffixes from NZB name:
# NZBgeek / Obfuscated / BUYMORE / Scrambled.
#
# NOTE: This script requires Python to be installed on your system.

### NZBGET SCAN SCRIPT                                                     ###
##############################################################################

from __future__ import print_function
import os, re, sys

# Exit codes used by NZBGet
POSTPROCESS_SUCCESS = 93
POSTPROCESS_ERROR = 94
POSTPROCESS_SKIP = 95

# Check if the script is called from NZBGet 13.0 or later
if not "NZBOP_SCRIPTDIR" in os.environ:
    print("*** NZBGet post-processing script ***")
    print("This script is supposed to be called from NZBGet (13.0 or later).")
    sys.exit(POSTPROCESS_ERROR)

if not "NZBNP_NZBNAME" in os.environ:
    print("[WARN] Filename not found in environment")
    sys.exit(POSTPROCESS_ERROR)

fwp = os.environ["NZBNP_NZBNAME"]
fwp = re.sub(r"(?i)-4P\.nzb$", ".nzb", fwp)
fwp = re.sub(r"(?i)-4Planet\.nzb$", ".nzb", fwp)
fwp = re.sub(r"(?i)-AlternativeToRequested\.nzb$", ".nzb", fwp)
fwp = re.sub(r"(?i)-AlteZachen\.nzb$", ".nzb", fwp)
fwp = re.sub(r"(?i)-AsRequested\.nzb$", ".nzb", fwp)
fwp = re.sub(r"(?i)-AsRequested-xpost\.nzb$", ".nzb", fwp)
fwp = re.sub(r"(?i)-BUYMORE\.nzb$", ".nzb", fwp)
fwp = re.sub(r"(?i)-Chamele0n\.nzb$", ".nzb", fwp)
fwp = re.sub(r"(?i)-GEROV\.nzb$", ".nzb", fwp)
fwp = re.sub(r"(?i)-iNC0GNiTO\.nzb$", ".nzb", fwp)
fwp = re.sub(r"(?i)-NZBGeek\.nzb$", ".nzb", fwp)
fwp = re.sub(r"(?i)-Obfuscated\.nzb$", ".nzb", fwp)
fwp = re.sub(r"(?i)-Obfuscation\.nzb$", ".nzb", fwp)
fwp = re.sub(r"(?i)-postbot\.nzb$", ".nzb", fwp)
fwp = re.sub(r"(?i)-Rakuv[a-z0-9]*\.nzb$", ".nzb", fwp)
fwp = re.sub(r"(?i)-RePACKPOST\.nzb$", ".nzb", fwp)
fwp = re.sub(r"(?i)-Scrambled\.nzb$", ".nzb", fwp)
fwp = re.sub(r"(?i)-WhiteRev\.nzb$", ".nzb", fwp)
fwp = re.sub(r"(?i)-WRTEAM\.nzb$", ".nzb", fwp)
fwp = re.sub(r"(?i)-CAPTCHA\.nzb$", ".nzb", fwp)
fwp = re.sub(r"(?i)-Z0iDS3N\.nzb$", ".nzb", fwp)
fwp = re.sub(r"(?i)\[eztv([ ._-]re)?\]\.nzb$", ".nzb", fwp)
fwp = re.sub(r"(?i)\[TGx\]\.nzb$", ".nzb", fwp)
fwp = re.sub(r"(?i)\[ettv\]\.nzb$", ".nzb", fwp)
fwp = re.sub(r"(?i)\[TGx\]-xpost\.nzb$", ".nzb", fwp)
fwp = re.sub(r"(?i).mkv-xpost\.nzb$", ".nzb", fwp)
fwp = re.sub(r"(?i)-xpost\.nzb$", ".nzb", fwp)
fwp = re.sub(r"(?i)(-D-Z0N3|\-[^-.\n]*)(\-.{4})?\.nzb$", r"\1.nzb", fwp)
if fwp:
    print("[NZB] NZBNAME=", fwp, sep="")

sys.exit(POSTPROCESS_SUCCESS)

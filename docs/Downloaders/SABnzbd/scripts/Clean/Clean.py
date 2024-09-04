#!/usr/bin/python3 -OO

##################################################################
### SABnzbd - Clean NZB Renamer                                 ##
##################################################################
##                                                              ##
## Removes the suffixes from NZB name used by bots:             ##
## examples: NZBgeek / Obfuscated / BUYMORE / Scrambled, etc..  ##
##                                                              ##
## NOTE: This script requires Python 3                          ##
##                                                              ##
## Install:                                                     ##
## 1. Copy script to SABnzbd's script folder                    ##
## 2. run: sudo chmod +x Clean.py                               ##
## 3. in SABnzbd go to Config > Switches                        ##
## 4. Change Pre-queue user script and select: Clean.py         ##
##################################################################

import sys
import re

# normalize argv to scriptname and just first 8 arguments to maintain compatibility
sys.argv = sys.argv[:9]
try:
    # Parse the input variables for SABnzbd version >= 4.2.0
    (
        scriptname,
        nzbname,
        postprocflags,
        category,
        script,
        prio,
        downloadsize,
        grouplist,
    ) = sys.argv
except:
    sys.exit(1)  # exit with 1 causes SABnzbd to ignore the output of this script

fwp = nzbname
fwp = re.sub(r"(?i)-4P$", "", fwp)
fwp = re.sub(r"(?i)-4Planet$", "", fwp)
fwp = re.sub(r"(?i)-AlternativeToRequested$", "", fwp)
fwp = re.sub(r"(?i)-AlteZachen$", "", fwp)
fwp = re.sub(r"(?i)-AsRequested$", "", fwp)
fwp = re.sub(r"(?i)-AsRequested-xpost$", "", fwp)
fwp = re.sub(r"(?i)-BUYMORE$", "", fwp)
fwp = re.sub(r"(?i)-Chamele0n$", "", fwp)
fwp = re.sub(r"(?i)-GEROV$", "", fwp)
fwp = re.sub(r"(?i)-iNC0GNiTO$", "", fwp)
fwp = re.sub(r"(?i)-NZBGeek$", "", fwp)
fwp = re.sub(r"(?i)-Obfuscated$", "", fwp)
fwp = re.sub(r"(?i)-Obfuscation$", "", fwp)
fwp = re.sub(r"(?i)-postbot$", "", fwp)
fwp = re.sub(r"(?i)-Rakuv[a-z0-9]*$", "", fwp)
fwp = re.sub(r"(?i)-RePACKPOST$", "", fwp)
fwp = re.sub(r"(?i)-Scrambled$", "", fwp)
fwp = re.sub(r"(?i)-WhiteRev$", "", fwp)
fwp = re.sub(r"(?i)-WRTEAM$", "", fwp)
fwp = re.sub(r"(?i)-CAPTCHA$", "", fwp)
fwp = re.sub(r"(?i)-Z0iDS3N$", "", fwp)
fwp = re.sub(r"(?i)\[eztv([ ._-]re)?\]$", "", fwp)
fwp = re.sub(r"(?i)\[TGx\]$", "", fwp)
fwp = re.sub(r"(?i)\[ettv\]$", "", fwp)
fwp = re.sub(r"(?i)\[TGx\]-xpost$", "", fwp)
fwp = re.sub(r"(?i).mkv-xpost$", "", fwp)
fwp = re.sub(r"(?i)-xpost$", "", fwp)
fwp = re.sub(r"(?i)(-D-Z0N3|\-[^-.\n]*)(\-.{4})?$", r"\1", fwp)

print("1")  # Accept
print(fwp)
print()
print()
print()
print()
print()
# 0 means OK
sys.exit(0)

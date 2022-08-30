#!/usr/bin/python3 -OO

##################################################################
### SABnzbd - Clean NZB Renamer                                 ##
##################################################################
## NOTE: This script is considered ALPHA!                       ##
##                                                              ##
## Removes the suffixes from NZB name used by bots:             ##
## examples: NZBgeek / Obfuscated / BUYMORE / Scrambled, etc..  ##
##                                                              ##
## NOTE: This script requires Python 3                          ##
##                                                              ##
## Install:                                                     ##
## 1. Copy script to sabnzbd's script folder                    ##
## 2. run: sudo chmod +x Clean.py                               ##
## 3. in SABnzbd go to Config > Switches                        ##
## 4. Change Pre-queue user script and select: Clean.py         ##
##################################################################

import sys
import re

try:
    (scriptname, nzbname, postprocflags, category, script, prio, downloadsize, grouplist, showname, season, episodenumber, episodename) = sys.argv
    downloadsize = int(downloadsize)
except:
    sys.exit(1)    # exit with 1 causes SABnzbd to ignore the output of this script

fwp = nzbname
fwp = re.sub('(?i)-4P$', '', fwp)
fwp = re.sub('(?i)-4Planet$', '', fwp)
fwp = re.sub('(?i)-AlternativeToRequested$', '', fwp)
fwp = re.sub('(?i)-AlteZachen$', '', fwp)
fwp = re.sub('(?i)-AsRequested$', '', fwp)
fwp = re.sub('(?i)-AsRequested-xpost$', '', fwp)
fwp = re.sub('(?i)-BUYMORE$', '', fwp)
fwp = re.sub('(?i)-Chamele0n$', '', fwp)
fwp = re.sub('(?i)-GEROV$', '', fwp)
fwp = re.sub('(?i)-iNC0GNiTO$', '', fwp)
fwp = re.sub('(?i)-NZBGeek$', '', fwp)
fwp = re.sub('(?i)-Obfuscated$', '', fwp)
fwp = re.sub('(?i)-Obfuscation$', '', fwp)
fwp = re.sub('(?i)-postbot$', '', fwp)
fwp = re.sub('(?i)-Rakuv[a-z0-9]*$', '', fwp)
fwp = re.sub('(?i)-RePACKPOST$', '', fwp)
fwp = re.sub('(?i)-Scrambled$', '', fwp)
fwp = re.sub('(?i)-WhiteRev$', '', fwp)
fwp = re.sub('(?i)-WRTEAM$', '', fwp)
fwp = re.sub('(?i)-CAPTCHA$', '', fwp)
fwp = re.sub('(?i)-Z0iDS3N$', '', fwp)
fwp = re.sub('(?i)\[eztv\]$', '', fwp)
fwp = re.sub('(?i)\[TGx\]$', '', fwp)
fwp = re.sub('(?i)\[ettv\]$', '', fwp)
fwp = re.sub('(?i)\[TGx\]-xpost$', '', fwp)
fwp = re.sub('(?i).mkv-xpost$', '', fwp)
fwp = re.sub('(?i)-xpost$', '', fwp)
fwp = re.sub(r'(?i)(-D-Z0N3|\-[^-.\n]*)(\-.{4})?$', r'\1', fwp)

print("1")    # Accept
print(fwp)
print()
print()
print()
print() 
print()
# 0 means OK
sys.exit(0)
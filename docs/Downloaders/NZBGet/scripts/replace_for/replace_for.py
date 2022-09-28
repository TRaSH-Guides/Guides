#!/usr/bin/env python3
#

##############################################################################
### NZBGET POST-PROCESSING SCRIPT                                          ###

# Replace underscore with dot.
#
# Author: miker
#
#
# Copy script to NZBGet's script folder.
# Run sudo chmod +x replace_for.py
#
#
# NOTE: This script requires Python to be installed on your system.

### NZBGET POST-PROCESSING SCRIPT                                          ###
##############################################################################

from __future__ import print_function
import os, re, sys

# Exit codes used by NZBGet
POSTPROCESS_SUCCESS=93
POSTPROCESS_ERROR=94
POSTPROCESS_SKIP=95


directory = os.environ['NZBPP_DIRECTORY']
print('Directory used is: ',directory)

for path, currentDirectory, files in os.walk(directory):
    for file in files:
        if file.find("_") !=-1:
            dst = file.replace('_', '.')
            os.rename (os.path.join(path,file),os.path.join(path,dst) )
            print('Result: ',file," renamed to ",dst)

sys.exit(POSTPROCESS_SUCCESS)
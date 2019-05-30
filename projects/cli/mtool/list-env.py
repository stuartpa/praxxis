import os
import sys

# Include the mtool subfolder folder
#
sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(__file__)), "mtool"))

import mtool

m = mtool.MTool(sys.argv)
m.log.header("Environment variables for all libraries")
m.list_env()

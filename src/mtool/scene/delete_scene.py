"""
This file calls the function to delete the current scene.

Dependencies within mtool: mtool/mtool.py
"""

import os
import sys

from mtool.cli import mtool

def delete_scene(args):
    """Deletes a scene"""
    m = mtool.MTool(args)
    name = m.delete_scene()
    m.log.info("New Current Scene", name)
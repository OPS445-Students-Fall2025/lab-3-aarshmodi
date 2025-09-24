#!/usr/bin/env python3
# lab3d.py - Lab 3, Investigation 2, Part 2

import subprocess

def free_space():
    """Return the free disk space of root (/) as a string, e.g., '8.0G'."""
    result = subprocess.run(['df', '-h', '/'], capture_output=True, text=True)
    # Get the second line, split into columns, and return the 'Avail' column
    lines = result.stdout.splitlines()
    # lines[0] is header, lines[1] has the data
    free = lines[1].split()[3]  # 0:Filesystem, 1:Size, 2:Used, 3:Avail
    return free



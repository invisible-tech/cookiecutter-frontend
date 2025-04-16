#!/usr/bin/env python
import os
import shutil
import glob

# Delete node_modules if it exists
node_modules_path = os.path.join(os.getcwd(), 'node_modules')
if os.path.exists(node_modules_path):
    print(f"Removing node_modules directory: {node_modules_path}")
    shutil.rmtree(node_modules_path)

# Find and remove all bun.lock files
for bun_lock_file in glob.glob('**/bun.lock', recursive=True):
    if os.path.exists(bun_lock_file):
        print(f"Removing bun.lock file: {bun_lock_file}")
        os.remove(bun_lock_file) 
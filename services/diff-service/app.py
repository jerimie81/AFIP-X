import hashlib
import os

def hash_file(path):

    h = hashlib.sha256()

    with open(path, "rb") as f:
        h.update(f.read())

    return h.hexdigest()

def diff_dirs(dir1, dir2):

    changes = []

    files = set(os.listdir(dir1)) & set(os.listdir(dir2))

    for f in files:
        if hash_file(f"{dir1}/{f}") != hash_file(f"{dir2}/{f}"):
            changes.append(f)

    return changes

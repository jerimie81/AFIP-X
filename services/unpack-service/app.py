import tarfile
import os

def unpack_firmware(path, output="/data/unpacked"):

    os.makedirs(output, exist_ok=True)

    with tarfile.open(path) as tar:
        tar.extractall(output)

    return output

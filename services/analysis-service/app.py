import os
import subprocess

def extract_kernel_info(boot_img):

    output = subprocess.getoutput(f"strings {boot_img} | grep Linux")

    return output

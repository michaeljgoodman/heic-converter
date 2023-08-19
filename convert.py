from PIL import Image
from pillow_heif import register_heif_opener

import os

register_heif_opener()


def convert_heic(target, destination):
    print(f"[-] Converting {target} to {destination}")
    image = Image.open(target)
    image.convert("RGB").save(destination)


target_dir = "./heic/"

# Create output directory
new_dir = os.path.abspath(target_dir) + "_converted"

if not os.path.exists(new_dir):
    print("[-] Generating output path %s" % new_dir)
    os.mkdir(new_dir)

for path, dirnames, filenames in os.walk(target_dir):
    for file in filenames:
        if ".heic" in file.lower():
            print(f"[+] Found HEIC file: {file}")
            # Create new relative path in the output directory
            relative_path = os.path.relpath(os.path.join(path, file), target_dir)
            print(f"[-] Relative path: {relative_path}")
            new_path = os.path.join(new_dir, relative_path)
            print(f"[-] New path: {new_path}")
            convert_heic(os.path.join(path, file), new_path + ".jpg")

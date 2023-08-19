import argparse
from PIL import Image
from pillow_heif import register_heif_opener
import os

register_heif_opener()

def convert_heic(target, destination):
    print(f"[-] Converting {target} to {destination}")
    image = Image.open(target)
    image.convert("RGB").save(destination)

def is_image_file(file_path):
    try:
        image = Image.open(file_path)
        return True
    except Exception:
        return False

def convert_files(input_dir, output_dir, input_format, output_format):
    for root, _, filenames in os.walk(input_dir):
        for file in filenames:
            if input_format and file.lower().endswith("." + input_format):
                relative_path = os.path.relpath(root, input_dir)
                new_path = os.path.join(output_dir, relative_path)
                
                if not os.path.exists(new_path):
                    os.makedirs(new_path)
                
                input_file_path = os.path.join(root, file)
                output_file_path = os.path.join(new_path, os.path.splitext(file)[0] + ".jpg")
                convert_heic(input_file_path, output_file_path)
            elif not input_format and is_image_file(os.path.join(root, file)):
                relative_path = os.path.relpath(root, input_dir)
                new_path = os.path.join(output_dir, relative_path)
                
                if not os.path.exists(new_path):
                    os.makedirs(new_path)
                
                input_file_path = os.path.join(root, file)
                output_file_path = os.path.join(new_path, os.path.splitext(file)[0] + ".jpg")
                convert_heic(input_file_path, output_file_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert image files to JPEG format")
    parser.add_argument("--input-dir", required=True, help="Input directory containing files to convert")
    parser.add_argument("--output-dir", default="./converted_images", help="Output directory for converted files")
    parser.add_argument("--input-format", help="Input format (e.g., heic)")
    parser.add_argument("--output-format", required=True, help="Output format (e.g., jpg)")
    
    args = parser.parse_args()
    
    convert_files(args.input_dir, args.output_dir, args.input_format, args.output_format)

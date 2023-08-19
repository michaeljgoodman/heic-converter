# Image Converter
## Description
This simple python utility lets you walk a directory and convert any image files found to a desired format. It will recreate the target directory structure in your chosen output directory.

## Requirements
- Python 3.x
- Pillow library: pip install pillow
- pillow_heif addon: pip install pillow_heif

## Usage
Run the script with the desired arguments:

`python convert.py --input-dir /path/to/input_directory --output-dir /path/to/output_directory --input-format heic --output-format jpg`

Replace the following arguments:

```
--input-dir: The input directory containing the image files to convert.
--output-dir: The output directory where the converted files will be saved.
--input-format: The format of the input files (e.g., heic).
--output-format: The desired output format (e.g., jpg).
```


If you omit the --input-format argument, the script will process any valid image files found in the input directory, ignoring non-image files.
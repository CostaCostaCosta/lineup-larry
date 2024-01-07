-------------------------------------------------------------------------------
                           Lineup Larry: Image Tiling Tool
-------------------------------------------------------------------------------

OVERVIEW
Lineup Larry is a Python script designed to combine multiple .png images into a single, horizontally elongated rectangular image. It is particularly useful for creating image collages or visual summaries from a set of images. The script also features the functionality to overlay a small 'j' on images whose names end with '-j'.

FEATURES
- Combines multiple .png images into a single rectangular image.
- The resulting image is longer in width than in height.
- Option to overlay a 'j' on specific images.
- Resizes images to maintain a uniform grid.

PREREQUISITES
- Python 3.x
- Pillow library (Python Imaging Library Fork)

INSTALLATION
To use Lineup Larry, you need to have Python and Pillow installed. If you don't have Pillow installed, you can install it using pip:
  pip install Pillow

USAGE
To use Lineup Larry, place the script in a directory and follow these steps:
1. Prepare Your Images: Save all the .png images you want to combine in a single folder. Name any image you want to mark with a 'j' with a '-j' at the end of the filename (before the file extension).
2. Run the Script: Use the command line to navigate to the directory containing the script and run:
   python lineup_larry.py /path/to/your/image/folder
   Replace /path/to/your/image/folder with the path to your folder containing the .png images.
3. View the Result: After running the script, check the input folder for a new image file named after the folder itself. This file is the combined image.

CUSTOMIZATION
If you need to adjust the script for different behaviors (e.g., changing the overlay character or altering the tiling pattern), you can modify the lineup_larry.py script. Basic Python knowledge is recommended for customization.

CONTRIBUTING
Contributions to Lineup Larry are welcome. Feel free to fork the repository, make changes, and submit pull requests. If you find any bugs or have suggestions for improvement, please open an issue in the project repository.

LICENSE
MIT


-------------------------------------------------------------------------------

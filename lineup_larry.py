from PIL import Image, ImageDraw, ImageFont
import os
import sys
import math


def lineup_larry(folder):
    # Get a list of .png files in the specified folder
    input_files = [
        f for f in os.listdir(folder) if os.path.splitext(f)[1].lower() == ".png"
    ]
    if not input_files:
        print("No PNG files found in the folder.")
        return

    num_images = len(input_files)

    # Calculate the number of rows and columns for a horizontally elongated rectangle
    num_columns = math.ceil(math.sqrt(num_images))
    num_rows = math.ceil(num_images / num_columns)

    # Ensure that the rectangle is wider than it is tall
    if num_rows > num_columns:
        num_rows, num_columns = num_columns, num_rows

    # Sort input_files in alphabetical order
    input_files.sort()

    # Determine the size of each tile
    max_width = max_height = 0
    for file in input_files:
        with Image.open(os.path.join(folder, file)) as img:
            max_width = max(max_width, img.width)
            max_height = max(max_height, img.height)

    # Create a new image with the calculated dimensions
    output_image = Image.new(
        "RGB", (num_columns * max_width, num_rows * max_height), "white"
    )

    current_row = current_column = 0
    for file in input_files:
        with Image.open(os.path.join(folder, file)) as img:
            # Resize image if necessary
            img = img.resize((max_width, max_height), Image.Resampling.LANCZOS)

            x_offset = current_column * max_width
            y_offset = current_row * max_height
            output_image.paste(img, (x_offset, y_offset))

            if file.endswith("-j"):
                draw_j(output_image, x_offset, y_offset, max_width, max_height)

            current_row += 1
            if current_row == num_rows:
                current_row = 0
                current_column += 1

    # Save the output image in the same directory with the folder name as the file name
    folder_name = os.path.basename(os.path.normpath(folder))  # Extract the folder name
    output_file_name = os.path.join(
        folder, folder_name + ".png"
    )  # Create the output file path
    print("Saving image to: " + output_file_name)
    output_image.save(output_file_name)


def draw_j(image, x_offset, y_offset, img_width, img_height):
    # Load the Arial font, or use default font if not found
    try:
        font = ImageFont.truetype("arial.ttf", 25)
    except IOError:
        font = ImageFont.load_default()

    draw = ImageDraw.Draw(image)  # Create a drawing context
    text = "j"  # Text to be drawn

    # Position the text at the bottom right of the current image
    draw.text(
        (x_offset + img_width - 30, y_offset + img_height - 30),
        text,
        fill="black",
        font=font,
    )


if __name__ == "__main__":
    # Command line argument handling
    if len(sys.argv) < 2:
        print("Usage: python lineup_larry.py /path/to/input/folder")
    else:
        folder = sys.argv[1]
        if not os.path.exists(folder):
            print("The specified folder does not exist.")
        else:
            lineup_larry(folder)

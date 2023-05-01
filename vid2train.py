# vid2train
# Author: Rich K. MLS github.com/richkmls
# Date: 04/30/2023
# Description: A Python script to extract frames from a video for AI training.

# Import modules
import argparse
import os
import time
import random
import string
import cv2
import numpy as np
from PIL import Image
from torchvision.transforms import RandomCrop, Resize

def transform_video(src_vid: str, out: str, cropsize: int, brightmin: int,
                    brightmax: int, filetime: int, FPS: float) -> None:
    """Extract and transform frames from a video file at 1 FPS.

    Extract one frame per second from a video file and apply image transformations,
    such as cropping, resizing and color conversion. Save the transformed frames to
    a destination directory if they meet the brightness criteria.

    Args:
        src_vid: The path to the video file to be processed.
        out: The path to the out directory where the transformed frames
            will be saved.
        cropsize: size of the final image that will be cropped from vid
        brightmin: minimum brightness level of video frame
        brightmax: maximum brightness level of video frame
        filetime: timestamp that will be included in the image filenames
        FPS: value defining the total seconds that elapse between each frame

    Returns:
        None
    """
    image_count = 0 # Initialize the image counters
    skipped_count = 0
    cap = cv2.VideoCapture(src_vid) # Open the video file
    fps = cap.get(cv2.CAP_PROP_FPS) # Get the frames per second

    # Loop over all frames
    for count in range(int((cap.get(cv2.CAP_PROP_FRAME_COUNT) / fps) * FPS)):

        # Set the current frame position
        cap.set(cv2.CAP_PROP_POS_FRAMES, int((count * fps) / FPS))

        # Read the frame
        success, image = cap.read()
        
        # Check if the frame is valid
        if success:

            # Convert the color space from BGR to RGB
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

            # Read a grayscale image for brightness check
            brightness_check = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
            avg_brightness = np.mean(brightness_check)

            # Check if the brightness is within the range
            if brightmin < avg_brightness < brightmax:

                # Convert the array to an image object
                image = Image.fromarray(image)

                # Choose a crop size randomly between cropsize and the image's minimum dimension
                crop_size = (
                    min(image.size)
                    if min(image.size) < cropsize
                    else random.randint(cropsize, min(image.size))
                )
                # Crop the image randomly
                image = RandomCrop((crop_size, crop_size))(image)

                # Resize the image to cropsize by cropsize
                image = Resize((cropsize, cropsize))(image)

                # Generate a random file name with image_count as prefix
                file_name = f"{image_count}-{filetime}.png"

                # Join the out directory and the file name
                file_path = os.path.join(out, file_name)

                # Save the image to the file path
                image.save(file_path)

                # Increment the image counter
                image_count += 1
            
            else:
                # Increment the image skipped counter
                skipped_count  += 1
  
    # Release the video capture object
    cap.release()

    print(f"Total images created: {image_count}")
    print(f"Total frames skipped: {skipped_count}")

def confirm_prompt(question: str) -> bool:
    """
    Ask the user a yes/no question and return a boolean value.

    Parameters:
        question (str): The question to ask the user.

    Returns:
        bool: True if the user answers 'y', False otherwise.
    """

    # Get the user's answer in lowercase
    answer = input(f"{question} (y/n): ").lower()

    # Validate the user's input and repeat the question if invalid
    while answer not in {"y", "n"}:
        print("Invalid input. Please enter 'y' or 'n'.")
        answer = input(f"{question} (y/n): ").lower()

    # Return the boolean value of the user's answer
    return answer == "y"

def main() -> None:
    """
    Extract images from a video file according to the user's input and output preferences.
    """
    
    # Define constants
    CROP_SIZE = 512 # Image final crop size
    BRIGHTNESS_MIN = 20 # Minimum and Maximum Brightness levels 0-256
    BRIGHTNESS_MAX = 236
    FPS = 1 # Total images extracted per second of video

    # Parser object with optional args for input/output paths & constants
    parser = argparse.ArgumentParser(
        prog="vid2train",
        description="Extract frames from a video for AI training."
    )
    # Input video file path
    parser.add_argument("--input", type=str, help="Input video path.")
    # Output directory path
    parser.add_argument("--output", type=str, help="Output directory path.")
    # Image final crop size in pixels
    parser.add_argument(
        "--crop_size",
        type=int,
        default=CROP_SIZE,
        help="Image crop size in px."
    )
    # Minimum brightness level in range 0-256
    parser.add_argument(
        "--bright_min",
        type=int,
        default=BRIGHTNESS_MIN,
        help="Min brightness level."
    )
    # Maximum brightness level in range 0-256
    parser.add_argument(
        "--bright_max",
        type=int,
        default=BRIGHTNESS_MAX,
        help="Max brightness level."
    )
    # Total images extracted per second of video
    parser.add_argument(
        "--fps",
        type=float,
        default=FPS,
        help="Images per second."
    )
    args = parser.parse_args()

    
    # Update constants with parser arguments:
    CROP_SIZE = args.crop_size
    BRIGHTNESS_MIN = args.bright_min
    BRIGHTNESS_MAX = args.bright_max
    FPS = args.fps
    FILE_TIME = str(int(time.time()))[4:]

    # Use the user's input path if given; otherwise, request it
    src_vid = args.input or input("Enter the source video file path: ")
    print(f"The input video file path is {src_vid}.")

    # Use the user's output path if given; otherwise, generate a new folder with a timestamp
    output_dir = args.output or os.path.join(os.path.dirname(src_vid),
        os.path.splitext(os.path.basename(src_vid))[0] + "_" + FILE_TIME)
    print(f"The output directory path is {output_dir}.")

    # Confirm the settings with the user and proceed if yes
    if confirm_prompt("Do you want to proceed with these settings?"):
        # Create the output directory if it does not exist
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
            print(f"The directory path {output_dir} has been created.")
        transform_video(src_vid, output_dir, CROP_SIZE, BRIGHTNESS_MIN,
                        BRIGHTNESS_MAX, FILE_TIME, FPS)
    else:
        print("Operation aborted.")

if __name__ == "__main__":
    main()

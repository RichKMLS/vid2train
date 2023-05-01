# vid2train: A Video Processing Tool for AI Training

vid2train is a video processing tool that can extract and transform frames from a video file at a specified rate and save them as images for AI training. The motivation behind this project was to create a simple and efficient way of generating image datasets from video sources, which can be useful for various computer vision and machine learning applications. The problem that it solves is the tedious and manual process of selecting and cropping frames from videos, which can be time-consuming and error-prone. The main features of vid2train are:

- It can take any video file as input and output a directory of images with a unique name and timestamp.
- It can crop the images to a desired size in pixels, which can help reduce the file size and improve the performance of the AI model.
- It can filter out images that are too dark or too bright based on a minimum and maximum brightness level, which can help improve the quality and diversity of the dataset.
- It can adjust the frequency of extracting images based on a frames per second (FPS) parameter, which can help control the number and variety of images in the dataset.

## Installation

To use vid2train, you need to have Python 3 installed on your system. You also need the following libraries: argparse, os, time, random, string, cv2, numpy, PIL, and torchvision.

## Usage

To execute vid2train, open a terminal or command prompt and go to the folder where vid2train.py is stored. Then type the following command:

```
python vid2train.py --input <input_video_path> --output <output_directory_path> --crop_size <crop_size_in_px> --bright_min <min_brightness_level> --bright_max <max_brightness_level> --name_length <filename_char_length> --fps <images_per_second>
```

You can also skip all the flags and enter your input video path when prompted. A new output folder with the same name as your video file + timestamp will be created and the default parameters will be applied:

```
- crop_size: 512
- bright_min: 20
- bright_max: 236
- name_length: 3
- fps: 1
```

The program will then ask you to confirm your settings before proceeding with the extraction and transformation process. After, you will see a message indicating how many images were saved in the output directory. You can then use these images for your AI training purposes.

## Feedback and support

If you have any issues, suggestions, or questions about this script, please feel free to [open an issue](https://github.com/richkmls/vid2train/issues).

## Disclaimer

This script is provided "as is" without any warranty. The author is not responsible for any damage or loss caused by using this script. 
See License for more info.

## Citation
If you use vid2train in your research or project, please cite it as follows:

Rich K. MLS (2023). vid2train: A Tool for Extracting Frames from Video for AI Training. GitHub repository, https://github.com/richkmls/

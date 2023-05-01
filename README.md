<h1 align="center">vid2train</h1>

#### <p align="center">A Software Tool for Extracting Images from a Video for Artificial Intelligence Training.</p><br>

vid2train is a tool that enables users to create image datasets from video files for AI training purposes. It simplifies and streamlines the process of extracting and transforming frames from videos, which can otherwise be a tedious and error-prone task. 

vid2train provides the following features:

- It supports any video file format as input and outputs a folder of images with unique names and timestamps.
- It allows users to customize the image size in pixels, with a default value of 512x512.
- It filters out images that are too dark or too bright, which can improve the quality and diversity of the dataset.
- It lets users adjust the extraction rate based on a frames per second (FPS) parameter, which can influence the number and variety of images in the dataset.

## Installation

To use vid2train, you need to have Python 3 installed on your system. You also need the following libraries: argparse, os, time, random, string, cv2, numpy, PIL, and torchvision.

## Usage

To execute vid2train, open a terminal or command prompt and go to the folder where vid2train.py is stored. Then type the following command:

```
python vid2train.py \
--input <input_video_path> \
--output <output_directory_path> \
--crop_size <crop_size_in_px> \
--bright_min <min_brightness_level> \
--bright_max <max_brightness_level> \
--name_length <filename_char_length> \
--fps <images_per_second>
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
To acknowledge the use of vid2train in your research or project, please cite the following reference in your publications:

Rich K. MLS (2023). vid2train: A Software Tool for Extracting Images from a Video for Artificial Intelligence Training. GitHub repository. Available at: https://github.com/richkmls/vid2train

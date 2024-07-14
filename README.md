# Video2ASCII

T
# Video to ASCII Art Converter

This project converts a video file into a series of ASCII art frames and then assembles those frames into a video.

## Demo

![Demo 1 - Made with Clipchamp](https://github.com/user-attachments/assets/378fc9be-2f73-42a7-9c80-e2be9a3041fa)

## Requirements

- Python 3.x
- OpenCV
- NumPy
- Pillow

You can install the required Python packages using:

```
pip install opencv-python numpy pillow
```

## Project Structure

The project contains the following directories:

- `images/`: Stores the extracted frames from the input video.
- `ascii/`: Stores the converted ASCII art frames.

## Usage

1. Place your video file in the project directory.
2. Update the video file path in the script.
3. Run the script to generate ASCII frames and assemble them into a video:

```
python Ascii_Video.py
```

The resulting video will be saved as `output_video.avi`.

![Demo](https://github.com/user-attachments/assets/8f712f5b-6bdc-4a9d-8953-bc59192f2964)

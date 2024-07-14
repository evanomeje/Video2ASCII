import cv2
import os
import numpy as np
from PIL import Image, ImageDraw, ImageFont


directories = ['images', 'ascii']
for directory in directories:
    if not os.path.exists(directory):
        os.mkdir(directory)
    else:
        print(f"Directory '{directory}' already exists.")


vidObj = cv2.VideoCapture("kelela.mp4")  #choose a sample video
count = 0
flag = True

while flag:
    flag, image = vidObj.read()
    if flag:
        cv2.imwrite(f"images/frame{count}.jpg", image)
        count += 1

# ASCII characters to use (You can customize)
ASCII = ['@', '%', '#', '*', '+', '=', '-', ':', '.', ' ']

def resize_image(image, new_width=150):  
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return resized_image

def grayfy(image):
    grayscale_image = image.convert("L")
    return grayscale_image

def pixels_to_ascii(image):
    pixels = image.getdata()
    characters = "".join([ASCII[pixel // 25] for pixel in pixels])
    return characters

def convert_to_ascii(image_path, output_path):
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(image_path, "Image not found:", e)
        return

    new_image_data = pixels_to_ascii(grayfy(resize_image(image)))
    pixel_count = len(new_image_data)
    ascii_image = "\n".join(new_image_data[i:(i+150)] for i in range(0, pixel_count, 150))  

    with open(output_path, "w") as f:
        f.write(ascii_image)

    print(f"Converted {image_path} to ASCII and saved to {output_path}")


for frame_num in range(count):
    input_path = f"images/frame{frame_num}.jpg"
    output_path = f"ascii/frame{frame_num}.txt"
    convert_to_ascii(input_path, output_path)
    print(f"Converted {input_path} to ASCII and saved to {output_path}")


def load_ascii_image(filepath):
    with open(filepath, 'r') as f:
        ascii_art = f.read()
    return ascii_art


ascii_folder = 'ascii/'
output_video_path = 'output_video.avi'


ascii_files = sorted([os.path.join(ascii_folder, file) for file in os.listdir(ascii_folder) if file.endswith('.txt')])


frame_width, frame_height = None, None
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = None

for ascii_file in ascii_files:
 
    ascii_art = load_ascii_image(ascii_file)

  
    ascii_lines = ascii_art.split('\n')
    max_width = max(len(line) for line in ascii_lines)
    max_height = len(ascii_lines)
    font_size = 10
    image_width = max_width * font_size
    image_height = max_height * font_size

    
    image = Image.new('L', (image_width, image_height), color=255)
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()

    y = 0
    for line in ascii_lines:
        draw.text((0, y), line, fill=0, font=font)
        y += font_size

    frame = np.array(image)

    if frame_width is None or frame_height is None:
        frame_height, frame_width = frame.shape

    if out is None:
        out = cv2.VideoWriter(output_video_path, fourcc, 30, (frame_width, frame_height), isColor=False)

   
    out.write(frame)


out.release()
print(f"ASCII video saved to {output_video_path}")




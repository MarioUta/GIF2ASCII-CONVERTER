from PIL import Image, ImageEnhance, ImageSequence
import numpy as np
import time
from os import system
import sys

def converter(image):
    image=image.convert("L")
    
    new_width = 50
    image = image.resize((new_width, int(image.height * (new_width / image.width))))

    brightness_factor=0.75
    brightner=ImageEnhance.Brightness(image)
    brightned_image=brightner.enhance(brightness_factor)

    contrast_factor = 1
    contraster = ImageEnhance.Contrast(brightned_image)
    contrast_image = contraster.enhance(contrast_factor)


    special_characters=['@','#','G','$','O','>','|','/','^','~',':','*',"'",'.','`']
    data=np.array(contrast_image.getdata())

    intervals=np.linspace(np.max(data),np.min(data),num=len(special_characters)+1)
    intervals = np.array([intervals[:-1], intervals[1:]]).transpose()

    my_ascii=[]
    for i in data:
        for interval, character in zip (intervals,special_characters):
            if  interval[0]>=i>=interval[1]:
                my_ascii.append(character)
                my_ascii.append(' ')
                break

    width,height=contrast_image.size
    my_ascii=np.array(my_ascii).reshape(height,width*2)
    return my_ascii


def print_frame(array):
    for row in array:
        print("".join(row))


gif=Image.open(r'/home/mario/Pictures/WhatsAppVideo2025-03-02at18.53.48-ezgif.com-video-to-gif-converter.gif')

print("Converting..")
my_frames=[]
for frame in ImageSequence.Iterator(gif):
    my_frames.append(converter(frame))
print("Finish")


np.set_printoptions(threshold=sys.maxsize)
while True:
    for my_ascii in my_frames:
        print_frame(my_ascii)
        time.sleep(0.05)
        print("\033[H")



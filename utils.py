from PIL import Image, ImageEnhance, ImageSequence
import numpy as np
from math import floor, ceil


def build_pixel_categories(image):
    special_characters=['@','#','G','$','O','>','|','/','^','~',':','*',"'",'.','`']
    data=np.array(image.getdata())

    intervals=np.linspace(np.max(data),np.min(data),num=len(special_characters)+1)
    intervals = np.array([intervals[:-1], intervals[1:]]).transpose()

    pixel_categories={}
    for character, interval in zip(special_characters,intervals):
        pixel_categories.update( {i:character for i in range((floor(interval[1])),ceil(interval[0])+1)})

    return pixel_categories


def transformer(image):
    image=image.convert("L")
    
    new_width = 100
    image = image.resize((new_width, int(image.height * (new_width / image.width))))

    brightness_factor=0.75
    brightner=ImageEnhance.Brightness(image)
    brightned_image=brightner.enhance(brightness_factor)

    contrast_factor = 1
    contraster = ImageEnhance.Contrast(brightned_image)
    contrast_image = contraster.enhance(contrast_factor)
    return contrast_image



def converter(image):
    image=transformer(image)
    data=np.array(image.getdata())
    pixel_categories=build_pixel_categories(image)
    my_ascii=[]
    for i in data:
        character=pixel_categories[i]
        my_ascii.append(character)
        my_ascii.append(' ')

    width,height=image.size
    my_ascii=np.array(my_ascii).reshape(height,width*2)
    return my_ascii


def print_frame(array):
    for row in array:
        print("".join(row))
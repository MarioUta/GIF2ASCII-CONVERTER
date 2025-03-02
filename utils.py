from PIL import Image, ImageEnhance, ImageSequence
import numpy as np
from math import floor, ceil

pixel_categories={}
images_data=[]
width=0
height=0

def build_pixel_categories(images):

    mini=256
    maxi=-1
    for image in images:
        
        data=np.array(transformer(image).getdata()) 
        images_data.append(data)
        mini=min(np.min(np.array(data)),mini)
        maxi=max(np.max(np.array(data)),maxi)

    special_characters=['@','#','G','$','O','>','|','/','^','~',':','*',"'",'.','`']
    intervals=np.linspace(maxi,mini,num=len(special_characters)+1)
    intervals=[round(i) for i in intervals]
    intervals = np.array([intervals[:-1], intervals[1:]]).transpose()
    
    for character, interval in zip(special_characters,intervals):
        pixel_categories.update( {i:character for i in range((floor(interval[1])),ceil(interval[0])+1)})



def transformer(image):
    image=image.convert("L")
    
    new_width = 100
    image = image.resize((new_width, int(image.height * (new_width / image.width))))

    global width,height
    width,height=image.size

    brightness_factor=0.75
    brightner=ImageEnhance.Brightness(image)
    brightned_image=brightner.enhance(brightness_factor)

    contrast_factor = 1
    contraster = ImageEnhance.Contrast(brightned_image)
    contrast_image = contraster.enhance(contrast_factor)
    return contrast_image



def converter(images):

    build_pixel_categories(images)
    
    my_frames=[]
    for images in images_data:
        my_ascii=[]
        for i in images:
            character=pixel_categories[i]
            my_ascii.append(character)
            my_ascii.append(' ')
        my_ascii=np.array(my_ascii).reshape(height,width*2)
        my_frames.append(my_ascii)
    
    return my_frames


def print_frame(array):
    for row in array:
        print("".join(row))
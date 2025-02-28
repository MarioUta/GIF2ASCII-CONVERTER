from PIL import Image, ImageEnhance
import numpy as np

image=Image.open(r'/home/mario/Pictures/a961aa14-b035-40a9-a5bb-354662eb1b67.jpeg')
image=image.convert("L")

brightness_factor=0.75
brightner=ImageEnhance.Brightness(image)
brightned_image=brightner.enhance(brightness_factor)

contrast_factor = 1
contraster = ImageEnhance.Contrast(brightned_image)
contrast_image = contraster.enhance(contrast_factor)


special_characters=['@','#','G','$','O','>','|','/','^','~',':','*',"'",'.','`']
data=np.array(contrast_image.getdata())

#contrast_image.show()

intervals=np.linspace(np.max(data),np.min(data),num=len(special_characters)+1)
intervals = np.array([intervals[:-1], intervals[1:]]).transpose()

#print(intervals)
my_ascii=[]
for i in data:
    for interval, character in zip (intervals,special_characters):
        if  interval[0]>=i>=interval[1]:
            my_ascii.append(character)
            my_ascii.append(' ')
            break

width,height=contrast_image.size
my_ascii=np.array(my_ascii).reshape(height,width*2)

with open('my_ascii.txt','w') as f:
    for i in my_ascii:
        for j in i:
            f.write(j)
        f.write('\n')



from PIL import Image, ImageEnhance, ImageSequence
from tkinter import filedialog as fd
from utils import converter, print_frame, build_pixel_categories
import numpy as np
import time
import sys

if __name__=="__main__":

    filetypes = (("gif files", "*.gif"), )

    file = fd.askopenfilename(filetypes=filetypes)
    gif=Image.open(file)

    print("Converting..")

    my_frames=converter(ImageSequence.Iterator(gif))
    
    print("Finish")


    np.set_printoptions(threshold=sys.maxsize)
    while True:
        for my_ascii in my_frames:
            print_frame(my_ascii)
            time.sleep(0.05)
            print("\033[H")



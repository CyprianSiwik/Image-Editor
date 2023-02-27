from PIL import Image, ImageEnhance, ImageFilter
import os
import sys

from PIL import Image
from urllib.request import urlopen  #accepts copy image link

# Prompt to get the image link of the image
url = str(input("Please enter the image link of the image you would like to be altered: "))


#IF STATEMENT THAT ACCOUNTS FOR ALL POSSIBLE CHOICES
while True:  # this will make it so that the prompt is displayed again if the input is not applicable

    app1 = str(input("Please select the filters and alterations to the image you would like to apply:\n \nSharpen (Filter) \nBlack & White (Filter) \nRotate \nBrightness\nContrast \n"))
    app1 = app1.lower() #makes input lowercase

    if app1 == "sharpen": # SELECTION FOR SHARPEN FILTER
        img = Image.open(urlopen(url))  # opens image, doesnt display it though
        img = img.filter(ImageFilter.SHARPEN)
        img.show()
        sys.exit()

    elif app1 == "black & white" or app1 == "black": # SELECTION FOR BLACK WHITE FILTER
        img = Image.open(urlopen(url))  # opens image, doesnt display it though
        img = img.convert('L')
        img.show()
        sys.exit()

    elif app1 == "rotate": # SELECTION FOR ROTATION
        rot = int(input("Enter the amount of rotation as a number: "))
        img = Image.open(urlopen(url))  # opens image, doesnt display it though
        img = img.rotate(rot)
        img.show()
        sys.exit()

    elif app1 == "brightness": # SELECTION FOR BRIGHTNESS
        mag = int(input("Please enter your factor of designated brightness: Note: 0.0 returns black, a factor of 1.0 increases the brightness: \n"))
        img = Image.open(urlopen(url))  # opens image, doesnt display it though
        imgE = ImageEnhance.Brightness(img)
        imgE.enhance(mag).show()
        sys.exit()


    elif app1 == "contrast": # SELECTION FOR CONTRAST
        mag = int(input("Please enter your factor of designated contrast: Note: 0.0 returns grey, a factor of 1.0 increases the contrast: \n"))
        img = Image.open(urlopen(url))  # opens image, doesnt display it though
        imgE = ImageEnhance.Contrast(img)
        imgE.enhance(mag).show()
        sys.exit()


    else :
        print("Error: appropriate selection not made")



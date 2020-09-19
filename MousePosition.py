import pyautogui as pg
# import PIL #pip install pillow
from PIL import Image, ImageGrab
import time




if __name__ == "__main__":
    time.sleep(3)
    print("game start in 5 sec !!!")
    image = ImageGrab.grab().convert('L')
    data = image.load()
    # while True:
    #     image = ImageGrab.grab()
    #     # img = takeScreenshot()    
    #     data = image.load()
    #     if isCollide(data):
    #         hit('up')

    #typing text
    for i in range(770,786):
        for j in range(965,966):
            data[i,j] = 255
    #typing name
    for i in range(267,290):
        for j in range(223,224):
            data[i,j] = 255

    #name of person
    for i in range(375,420):
        for j in range(383,384):
            data[i,j] = 255      
    image.show()
    print(pg.position())          

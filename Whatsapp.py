import pyautogui as pg
# import PIL #pip install pillow
from PIL import Image, ImageGrab
import time
import webbrowser
# name1 = str(input("enter the name of a person : "))
# string1 = input("enter the messege : \n")
# val = int(input("Enter no. of times : "))

def website():
    url = 'https://web.whatsapp.com'
    webbrowser.register('chrome',
        None,
        webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
    webbrowser.get('chrome').open(url)

def person(name):
    pg.click(x=267,y=223)
    # name = input("enter the name of a person : ")
    pg.write(name, interval=0.08)

def clickName():
    pg.click(x=375,y=383,clicks=2)
    # pg.write(name, interval=0.00)

def mess():
    pg.click(x=770,y=965,clicks=1)

def messege(string):
    # pg.click(x=770,y=965,clicks=1)
    pg.write(string,interval=0.0)

if __name__ == "__main__":
    website()
    time.sleep(10)
    person("name1")
    clickName()
    mess()

    time.sleep(3)
    for i in range(val):
        messege("string1")
        pg.hotkey('enter')
        i+=1

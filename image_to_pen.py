import cv2
import sys
import tkinter as tk
from tkinter.filedialog import askopenfilename
import inquirer
from inquirer.themes import GreenPassion
import time

def main():
    image_choice = askopenfilename()
    image = cv2.imread(image_choice)
    grayimage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    grayimageInv = 255 - grayimage
    grayimageInv = cv2.GaussianBlur(grayimageInv, (21, 21), 0)
    output = cv2.divide(grayimage, 255-grayimageInv, scale=256.0)
    cv2.namedWindow("image", cv2.WINDOW_AUTOSIZE)
    cv2.namedWindow("pencilsketch", cv2.WINDOW_AUTOSIZE)
    cv2.imshow("image", image)
    cv2.imshow("pencilsketch", output)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def intro():
    print("""
  ___                       _____      ___             _ _  
 |_ _|_ __  __ _ __ _ ___  |_   _|__  | _ \___ _ _  __(_) | 
  | || '  \/ _` / _` / -_)   | |/ _ \ |  _/ -_) ' \/ _| | | 
 |___|_|_|_\__,_\__, \___|   |_|\___/ |_| \___|_||_\__|_|_| 
                |___/                                       
    Transformez vos images avec un style pencil / dessin

    By Deucalion
    github : https://github.com/deucalionn
   
    """)
    time.sleep(1)

    introd = [
        inquirer.List('introd',
        message="Que voulez vous faire ? ",
        choices=['Transformer une image', 'Quitter'],
        default='Transformer une image'),
    ]
    answers = inquirer.prompt(introd, theme=GreenPassion())
    if answers.get('introd') == "Transformer une image":
        main()
    else:
        quit()
    

intro()
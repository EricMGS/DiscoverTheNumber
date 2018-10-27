##          Program: You need to discover the secret number with 10 tentatives
##          Author: EricMGS
##          Date: 18/03/2018
##          Signature: ./.-./../-.-./--/--./...
###############################################################################################################
#########################################################################################################3#####

import random
import sys
from tkinter import Tk, Entry, CENTER, Label, Button, messagebox
from PIL import Image, ImageTk #library to import background image

answer = random.randrange(1000)
smaller = 0
bigger = 1000
tentatives = 10

def again (): #redefine the initial values
    global answer
    global smaller
    global bigger
    global tentatives

    answer = random.randrange(1000)
    smaller = 0
    bigger = 1000
    tentatives = 10
    lbl_tentatives.configure (text = 'Tentatives: ' + str(tentatives))
    lbl_tip.configure (text = 'Discover the number between ' + str(smaller) + ' and ' + str(bigger))

#verify if the entry value is equal the answer and atualize the tip
def verify ():
    global smaller
    global bigger
    global tentatives
    for x in range(smaller + 1, bigger): #verify if the entry value is between smaller and bigger
        if int(ent_value.get()) == x:

            if tentatives > 0:
            
                if int(ent_value.get()) < answer: 
                    smaller = int(ent_value.get())
                elif int(ent_value.get()) > answer:
                    bigger = int(ent_value.get ())
                else:
                    if messagebox.askyesno ('You won', 'Congratulations\nThe secret number is: ' + str(answer) + '\n\nDo you wanna play again?') == 0:
                        sys.exit()
                    else:
                        return again()
                    
                tentatives -= 1
                lbl_tentatives.configure (text = 'Tentatives: ' + str(tentatives))
                lbl_tip.configure (text = 'Discover the number between ' + str(smaller) + ' and ' + str(bigger))

            else:
                if messagebox.askyesno ('You lost', 'I am sorry\nNo more tentatives\n\nDo you wanna play again?') == 0:
                    sys.exit()
                else:
                    return again()

window = Tk()
window.geometry ('300x300')
window.resizable (0,0)
window.title('Discover the number')

#RGB color
mycolor = '#%02x%02x%02x' % (153, 217, 234)

#import background image
image = Image.open('interrogation.png')
photo_image = ImageTk.PhotoImage(image)

#Label
lbl_image = Label (image = photo_image, width = 300, height = 300) #background image
lbl_image.place (relx = 0.5, rely = 0.5, anchor = CENTER)

lbl_tentatives = Label (font = 'impact', bg = mycolor)
lbl_tentatives.configure (text = 'Tentatives: ' + str(tentatives))
lbl_tentatives.place(relx = 0.02, rely = 0.08)

lbl_tip = Label(text = 'Discover the number between ' + str(smaller) + ' and ' + str(bigger), bg = mycolor, font = 'impact') 
lbl_tip.place (relx = 0.5, rely = 0.05, anchor = CENTER)

#Entry
ent_value = Entry(width = 10, justify = 'center', font = 'impact')
ent_value.place (relx = 0.5, rely = 0.5, anchor = CENTER)

#Button
btn_anwser = Button (width = 10, text = 'Awnser', command = verify, font = 'impact')
btn_anwser.place (relx = 0.5, rely = 0.9, anchor = CENTER)

window.mainloop ()

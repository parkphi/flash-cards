#Project 4: Independent Project
#December 2, 2016
#Philip Park
#The code below will construct a graphical user interface, then put up 4 of the final exam problems. 

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import PhotoImage
import os

#import pygame
#from pygame.locals import *
#from breezypythongui import *

LARGE_FONT= ("Verdana", 12)


class FlashCards(tk.Tk):
    
    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, "FlashCards")

        
        main = tk.Frame(self)
        main.pack(side="top", fill="both", expand = True)
        
        
        main.grid_rowconfigure(0, weight = 1)
        main.grid_columnconfigure(0, weight = 1)      

        self.frames = {}

        for S in (Intro, Slide_1, Slide_2, Slide_3, Slide_4, Slide_end, ReadMe):
            frame = S(main, self)
            self.frames[S] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Intro)


    def show_frame(self, cont):
        
        frame = self.frames[cont]
        frame.tkraise()

def slides(parameter):
    print(parameter)


class Intro(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Final Exam Review: One-Sided Flash Cards", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button_1 = ttk.Button(self, text = "Let's Start!",
                             command = lambda: controller.show_frame(Slide_1))
        button_1.pack()

        button_2 = ttk.Button(self, text = "Help",
                             command = lambda: controller.show_frame(ReadMe))
        button_2.pack()

class Slide_1(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        #label = tk.Label(self, text="Question 1", font=LARGE_FONT)
        label = tk.Label(self, text="Explain the difference between each of the following pieces of Python Code. \n x = 2       x ! = 2", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

    #def showImg(self):
        #load = Image.open('exam1.png')
        #render = ImageTK.PhotoImage(load)

        #img = Label(self, image=render)
        #img.image = render
        #img.place(x=10, y=10)
        #img.pack()

        button_3 = ttk.Button(self, text = "Next",
                             command = lambda: controller.show_frame(Slide_2))
        button_3.pack()

        button_4 = ttk.Button(self, text = "Back to Home",
                             command = lambda: controller.show_frame(Intro))
        button_4.pack()

class Slide_2(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        #label = tk.Label(self, text="Question 2", font=LARGE_FONT)
        label = tk.Label(self, text="Circle the following Boolean expressions that are False and explain why. \n '1' == 1                    1 >= 2 \n '1' == ""1""                    2 > 1 \nTrue != False            1 != 2 \n              (1 > 5) == (1 + 1 == 3)       False == ((4 < 2) or (2 <= 2))", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        
        button_5 = ttk.Button(self, text = "Next",
                             command = lambda: controller.show_frame(Slide_3))
        button_5.pack()

        button_6 = ttk.Button(self, text = "Previous",
                             command = lambda: controller.show_frame(Slide_1))
        button_6.pack()

class Slide_3(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="What is the output of the following code snippet? \n\n         x = 6 + 7//2 \n print(x)", font=LARGE_FONT)
        label.pack(pady=10, padx=10)


        button_7 = ttk.Button(self, text = "Next",
                             command = lambda: controller.show_frame(Slide_4))
        button_7.pack()

        button_8 = ttk.Button(self, text = "Previous",
                             command = lambda: controller.show_frame(Slide_2))
        button_8.pack()

class Slide_4(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Write a piece of Python code to read in a value from the user and then print out the \nname of the number. If the number is between 0 and 10 inclusive and if it is not \nprint 'out of range' (Note: Don't use more than 1 if statement).", font=LARGE_FONT)
        label.pack(pady=10, padx=10)


        button_9 = ttk.Button(self, text = "Next",
                             command = lambda: controller.show_frame(Slide_end))
        button_9.pack()

        button_10 = ttk.Button(self, text = "Previous",
                             command = lambda: controller.show_frame(Slide_3))
        button_10.pack()

class Slide_end(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Are you ready for the exam?", font = LARGE_FONT)
        label.pack(pady=10, padx=10) #center of the screen, but has to be a positive number

        button_c = ttk.Button(self, text = "Yes",
                              command=quit)
        button_c.pack()

        button_d = ttk.Button(self, text ="No, I want to review again.",
                              command = lambda: controller.show_frame(Slide_1))
        button_d.pack()


class ReadMe(tk.Frame):

    def __init__(self, parent, controller):
        tk. Frame.__init__(self, parent)
        label = tk.Label(self, text="For each slide, read and answer the question. When ready, proceed to the next slide. \n *Note, this is only one-sided, therefore, you must come up with your own answers.")
        label.pack(pady=10, padx=5)

        button_a = ttk.Button(self, text = "Back to Home",
                             command = lambda: controller.show_frame(Intro))
        button_a.pack()



        
app = FlashCards()
app.mainloop()

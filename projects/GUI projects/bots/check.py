import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
import random
import pyautogui
import time

# Root window
root = tk.Tk()
root.title('Display a Text File')
root.resizable(False, False)
root.geometry('550x250')

# Text editor
text = tk.Text(root, height=12)
text.grid(column=0, row=0, sticky='nsew')


def open_text_file():
    # file type
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )
    # show the open file dialog
    f = fd.askopenfile(filetypes=filetypes)
    # read the text file and show its content on the Text
    # text.insert('1.0', f.readlines())
    # str = str(f)
    # arr = f.read()
    # words = list(map(str, arr.split()))
    # time.sleep(5)
    # pyautogui.write(finalValue, interval=0.10)
    # print(words)
    # print(random.choice(words))
    # print([f'{f.read()}'])
    allText = f.read()
    # words = list(map(str, allText.split()))
    allText2 = ' '.join(allText.split())
    # print(allText2)
    # print random string
    randomize = random.choice(allText2)
    print(randomize)




# open file button
open_button = ttk.Button(
    root,
    text='Open a File',
    command=open_text_file
)

open_button.grid(column=0, row=1, sticky='w', padx=10, pady=10)


root.mainloop()




# a = input('Type : ')
# str = str(a)

# arr = str.split(',')
# print(arr)


# import random
# import time


# while True:
#     time.sleep(1)
#     allText = "hello my name is zuzie the zuzie with the z,once upon a time i am fine"
#     words = list(map(str, allText.split()))
    
#         # print random string
#     print(random.choice(allText))


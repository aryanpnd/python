# import tkinter

# window = tkinter.Tk()       # creating the window object
# window.title('my first GUI program')

y= float(input("ENTER YOUR TERM ONE MARKS: "))
total_t= float(input("ENTER YOUR TOTAL MARKS: "))
choice_c= int(input("SELECT YOUR FULL MARKS HERE (35 or 40): "))
if choice_c == 35 :
    term_2= ((7*total_t) - (6*y))/14
if choice_c == 40 :
    term_2= ((4*total_t) - (3*y))/7
print(f"your marks {term_2}")    


# window.mainloop()           # keeping the window until we close it
# modules
from tkinter import *
from tkcalendar import Calendar

# clear function
def clear_inputs():
    startDate.delete(0, 'end')
    endDate.delete(0, 'end')
    totalDateCount.delete(0, 'end')
    numberOfStudent.delete(0, 'end')
    pricePerHead.delete(0, 'end')

ws = Tk()
ws.title('School lunch bill generator')
ws.geometry('400x300')
ws.config(bg='#456')

f = ('sans-serif', 13)
btn_font = ('sans-serif', 10)
bgcolor = 'gray'

'''
genvar = StringVar()
genopt = ['Male', 'Female']
genvar.set('Male')
'''

# frames
frame = Frame(ws, padx=20, pady=20, bg=bgcolor)
frame.pack(expand=True, fill=BOTH)


# label widgets
Label(
    frame, 
    text="Start date",
    font=f,
    bg=bgcolor
).grid(row=0, column=0, sticky='w')

Label(
    frame,
    text="End date",
    font=f,
    bg=bgcolor
).grid(row=1, column=0, sticky='w')

Label(
    frame,
    text="Total date count",
    font=f,
    bg=bgcolor
).grid(row=2, column=0, sticky='w')

Label(
    frame,
    text="Number of student",
    font=f,
    bg=bgcolor
).grid(row=3, column=0, sticky='w')

Label(
    frame,
    text="Price per head per day",
    font=f,
    bg=bgcolor
).grid(row=4, column=0, sticky='w')
'''
Label(
    frame,
    text='Gender',
    font=f,
    bg=bgcolor
).grid(row=5, column=0, sticky='w')
'''

# entry widgets
startDate = Entry(frame, width=20, font=f)
startDate.grid(row=0, column=1)

endDate = Entry(frame, width=20, font=f)
endDate.grid(row=1, column=1)

totalDateCount = Entry(frame, width=20, font=f)
totalDateCount.grid(row=2, column=1)

numberOfStudent = Entry(frame, width=20, font=f)
numberOfStudent.grid(row=3, column=1)

pricePerHead = Entry(frame, width=20, font=f)
pricePerHead.grid(row=4, column=1)

'''
gender = OptionMenu(
    frame, 
    genvar,
    *genopt
)
gender.grid(row=5, column=1, pady=(5,0))
gender.config(width=15, font=f)
'''
btn_frame = Frame(frame, bg=bgcolor)
btn_frame.grid(columnspan=2, pady=(50, 0))


# default inputs for testing
startDate.insert(0,'E1008')
endDate.insert(0, 'Vineet Singh')
totalDateCount.insert(0, 'Python Developer')
numberOfStudent.insert(0, 'Aug 3rd, 2020')
pricePerHead.insert(0, 'July 31st, 2021')

# action buttons
submit_btn = Button(
    btn_frame,
    text='Generate Word',
    command=None, #generate,
    font=btn_font,
    padx=10, 
    pady=5
)
submit_btn.pack(side=LEFT, expand=True, padx=(15, 0))

clear_btn = Button(
    btn_frame,
    text='Clear',
    command=clear_inputs,
    font=btn_font,
    padx=10, 
    pady=5,
    width=7
)
clear_btn.pack(side=LEFT, expand=True, padx=15)

exit_btn = Button(
    btn_frame,
    text='Exit',
    command=lambda:ws.destroy(),
    font=btn_font,
    padx=10, 
    pady=5
)
exit_btn.pack(side=LEFT, expand=True)

# mainloop
ws.mainloop()
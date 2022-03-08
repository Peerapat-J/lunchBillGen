# modules
from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar

# clear function
def clear_inputs():
    startDate.insert(0,'')
    endDate.insert(0, '')
    totalDateCount.insert(0, '')
    numberOfStudent.insert(0, '')
    pricePerHead.insert(0, '')
    startDate.delete(0, 'end')
    endDate.delete(0, 'end')
    totalDateCount.delete(0, 'end')
    numberOfStudent.delete(0, 'end')
    pricePerHead.delete(0, 'end')

window = Tk()
window.title('School lunch bill generator')
window.geometry('600x600')
window.resizable(False, False)
#window.config(bg='#456')

f = ('sans-serif', 16)
btn_font = ('sans-serif', 16)
#bgcolor = 'gray'

optVar = StringVar()
optList = ['Select option', 'Opt1', 'Opt2']
optVar.set('Select option')

# frames
#frame = Frame(window, padx=20, pady=20, bg=bgcolor)

# the fuck is this part mean ?
frame = ttk.Frame(window, padding = "20 20 60 60")
frame.pack(expand=True, fill=BOTH)

# label widgets
Label(
    frame, 
    text="Start date",
    font=f,
    #bg=bgcolor
).grid(row=0, column=0, sticky='w')

Label(
    frame,
    text="End date",
    font=f,
    #bg=bgcolor
).grid(row=1, column=0, sticky='w')

Label(
    frame,
    text="Total date count",
    font=f,
    #bg=bgcolor
).grid(row=2, column=0, sticky='w')

Label(
    frame,
    text="Number of student",
    font=f,
    #bg=bgcolor
).grid(row=3, column=0, sticky='w')

Label(
    frame,
    text="Price per head",
    font=f,
    #bg=bgcolor
).grid(row=4, column=0, sticky='w')

Label(
    frame,
    text='Approver',
    font=f,
    #bg=bgcolor
).grid(row=5, column=0, sticky='w')

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

gender = OptionMenu(
    frame, 
    optVar,
    *optList
)
gender.grid(row=5, column=1, pady=(5,0))
gender.config(width=15, font=f)

#btn_frame = Frame(frame, bg=bgcolor)
btn_frame = Frame(frame)
btn_frame.grid(columnspan=6, pady=(50, 0))

# default inputs
startDate.insert(0,'')
endDate.insert(0, '')
totalDateCount.insert(0, '')
numberOfStudent.insert(0, '')
pricePerHead.insert(0, '')

# action buttons
submit_btn = Button(
    btn_frame,
    text='Generate Word',
    command=None, #generate,
    font=btn_font,
    padx=10, 
    pady=5
)
submit_btn.pack(side=LEFT, expand=True, pady=15)

clear_btn = Button(
    btn_frame,
    text='Clear',
    command=None,
    font=btn_font,
    padx=10, 
    pady=5,
    #width=7
)
clear_btn.pack(side=LEFT, expand=True, padx=15)

test_btn = Button(
    btn_frame,
    text='Test',
    command=None,
    font=btn_font,
    padx=10, 
    pady=5,
    #width=7
)
test_btn.pack(side=LEFT, expand=True, padx=15)

exit_btn = Button(
    btn_frame,
    text='Exit',
    command=lambda:window.destroy(),
    font=btn_font,
    padx=10, 
    pady=5
)
exit_btn.pack(side=LEFT, expand=True)

#ttk.Button(window, text="test", command=None)
# mainloop
window.mainloop()
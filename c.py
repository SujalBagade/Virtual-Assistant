from tkinter import *

root = Tk()
root.title("Simple Calculator")

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def button_clear():
    e.delete(0, END)


def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    e.delete(0, END)


def button_equal():
    second_number = e.get()
    e.delete(0, END)
    if math == "addition":
        e.insert(0, f_num + int(second_number))
    if math == "subtraction":
        e.insert(0, f_num - int(second_number))
    if math == "multiplication":
        e.insert(0, f_num * int(second_number))
    if math == "divide":
        e.insert(0, f_num / int(second_number))


def button_subtract():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    e.delete(0, END)


def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    e.delete(0, END)


def button_divide():
    first_number = e.get()
    global f_num
    global math
    math = "divide"
    f_num = int(first_number)
    e.delete(0, END)


button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
button_add = Button(root, text="+", padx=39, pady=20, command=button_add)
button_equal = Button(root, text="=", padx=87, pady=20, command=button_equal)
button_clear = Button(root, text="clear", padx=78, pady=20, command=button_clear)
button_subtract = Button(root, text="-", padx=40, pady=20, command=button_subtract)
button_multiply = Button(root, text="*", padx=40, pady=20, command=button_multiply)
button_divide = Button(root, text="/", padx=40, pady=20, command=button_divide)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1, columnspan=2)
button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)

button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)
root.mainloop()


"""from tkinter import *
from tkinter import ttk

y = 0
a = ttk.Notebook()
frame1 = ttk.Frame(a)
frame2 = ttk.Frame(a)
frame3 = ttk.Frame(a)
frame4 = ttk.Frame(a)
frame5 = ttk.Frame(a)

root = ttk.Frame(a)


def quiz(y):
    a.add(frame1, text="Q1")
    a.add(frame2, text="Q2")
    a.add(frame3, text="Q3")
    a.add(frame4, text="Q4")
    a.add(frame5, text="Q5")

    Label(frame1, text="What is Capital of Australia ?", font=("Arial", 40, "bold")).grid(row=2, column=2)
    Button(frame1, text="Sydney", font=("Arial", 20, "bold"), bg="light blue", command=a1_wrong).grid(row=3, column=1)
    Button(frame1, text="Melbourn", font=("Arial", 20, "bold"), bg="light green", command=a1_right).grid(row=3,
                                                                                                         column=2)
    Button(frame1, text="Perth", font=("Arial", 20, "bold"), bg="light pink", command=a1_wrong).grid(row=3, column=3)

    Label(frame2, text="There are how many squares in a chess board?", font=("Arial", 32, "bold")).grid(row=2, column=2)
    Button(frame2, text="128", font=("Arial", 20, "bold"), bg="light blue", command=a2_wrong).grid(row=3, column=1)
    Button(frame2, text="64", font=("Arial", 20, "bold"), bg="light green", command=a2_wrong).grid(row=3, column=2)
    Button(frame2, text="204", font=("Arial", 20, "bold"), bg="light pink", command=a2_right).grid(row=3, column=3)

    Label(frame3, text="Which country's flag is known as mother of all flags?", font=("Arial", 30, "bold")).grid(row=2,
                                                                                                                 column=2)
    Button(frame3, text="USA", font=("Arial", 20, "bold"), bg="light blue", command=a3_wrong).grid(row=3, column=1)
    Button(frame3, text="Russia", font=("Arial", 20, "bold"), bg="light green", command=a3_wrong).grid(row=3, column=2)
    Button(frame3, text="Norway", font=("Arial", 20, "bold"), bg="light pink", command=a3_right).grid(row=3, column=3)

    Label(frame4, text="Who gave the theory of everything?", font=("Arial", 30, "bold")).grid(row=2, column=2)
    Button(frame4, text="Stephen hawking", font=("Arial", 20, "bold"), bg="light blue", command=a4_right).grid(row=3,
                                                                                                               column=1)
    Button(frame4, text="Albert einstein", font=("Arial", 20, "bold"), bg="light green", command=a4_wrong).grid(row=3,
                                                                                                                column=2)
    Button(frame4, text="Nicolaus Copernicus", font=("Arial", 20, "bold"), bg="light pink", command=a4_wrong).grid(
        row=3, column=3)

    Label(frame5, text="Who is the author of the book 'Freedom Behind Bars '?", font=("Arial", 25, "bold")).grid(row=2,
                                                                                                                 column=2)
    Button(frame5, text="Sheikh Abdullah", font=("Arial", 20, "bold"), bg="light blue", command=a5_wrong).grid(row=3,
                                                                                                               column=1)
    Button(frame5, text="Kiran Bedi", font=("Arial", 20, "bold"), bg="light green", command=a5_right).grid(row=3,
                                                                                                           column=2)
    Button(frame5, text="Jawaharlal Nehru", font=("Arial", 20, "bold"), bg="light pink", command=a5_wrong).grid(row=3,
                                                                                                                column=3)


def a1_right():
    Label(frame1, text="Correct", font=("Arial", 20, "bold"), background="green", fg="yellow").grid(row=1, column=2)
    Label(frame1, text="Marks obtained : 1", font=("Arial", 20, "bold"), background="black", fg="white").grid(row=1,
                                                                                                              column=3)


def a1_wrong():
    Label(frame1, text="Incorrect", font=("Arial", 20, "bold"), background="red", fg="yellow").grid(row=1, column=2)
    Label(frame1, text="Marks obtained : 0", font=("Arial", 20, "bold"), background="black", fg="white").grid(row=1,
                                                                                                              column=3)


def a2_right():
    Label(frame2, text="Correct", font=("Arial", 20, "bold"), background="green", fg="yellow").grid(row=1, column=2)
    Label(frame2, text="Marks obtained : 1", font=("Arial", 20, "bold"), background="black", fg="white").grid(row=1,
                                                                                                              column=3)


def a2_wrong():
    Label(frame2, text="Incorrect", font=("Arial", 20, "bold"), background="red", fg="yellow").grid(row=1, column=2)
    Label(frame2, text="Marks obtained : 0", font=("Arial", 20, "bold"), background="black", fg="white").grid(row=1,
                                                                                                              column=3)


def a3_right():
    Label(frame3, text="Correct", font=("Arial", 20, "bold"), background="green", fg="yellow").grid(row=1, column=2)
    Label(frame3, text="Marks obtained : 1", font=("Arial", 20, "bold"), background="black", fg="white").grid(row=1,
                                                                                                              column=3)


def a3_wrong():
    Label(frame3, text="Incorrect", font=("Arial", 20, "bold"), background="red", fg="yellow").grid(row=1, column=2)
    Label(frame3, text="Marks obtained : 0", font=("Arial", 20, "bold"), background="black", fg="white").grid(row=1,
                                                                                                              column=3)


def a4_right():
    Label(frame4, text="Correct", font=("Arial", 20, "bold"), background="green", fg="yellow").grid(row=1, column=2)
    Label(frame4, text="Marks obtained : 1", font=("Arial", 20, "bold"), background="black", fg="white").grid(row=1,
                                                                                                              column=3)


def a4_wrong():
    Label(frame4, text="Incorrect", font=("Arial", 20, "bold"), background="red", fg="yellow").grid(row=1, column=2)
    Label(frame4, text="Marks obtained : 0", font=("Arial", 20, "bold"), background="black", fg="white").grid(row=1,
                                                                                                              column=3)


def a5_right():
    Label(frame5, text="Correct", font=("Arial", 20, "bold"), background="green", fg="yellow").grid(row=1, column=2)
    Label(frame5, text="Marks obtained : 1", font=("Arial", 20, "bold"), background="black", fg="white").grid(row=1,
                                                                                                              column=3)


def a5_wrong():
    Label(frame5, text="Incorrect", font=("Arial", 20, "bold"), background="red", fg="yellow").grid(row=1, column=2)
    Label(frame5, text="Marks obtained : 0", font=("Arial", 20, "bold"), background="black", fg="white").grid(row=1,
                                                                                                              column=3)


quiz(y)
a.pack()
a.mainloop()"""













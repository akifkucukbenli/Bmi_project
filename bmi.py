import tkinter

window = tkinter.Tk()
window.minsize(400, 400)
window.title("body mass index")
window.config(bg="aliceblue")

my_label = tkinter.Label(text="BMI Calculator", font=("Courier", 25, "bold"))
my_label.config(padx=5, pady=5, bg="aquamarine")
my_label.pack()

my_label_2 = tkinter.Label(text="Enter Your Weight (kg)", font=("arial", 12, "bold"), bg="light grey")
my_label_2.pack()

my_entry = tkinter.Entry()

my_entry.pack()

my_label_3 = tkinter.Label(text="Enter Your Height (cm)", font=("arial", 12, "bold"), bg="light grey")
my_label_3.config(padx=5, pady=5)
my_label_3.pack()

my_entry_2 = tkinter.Entry()

my_entry_2.pack()


def input_calculate():
    y = my_entry_2.get()
    x = my_entry.get()
    # print(x)
    # print(y)

    a = float(x) * 10 ** 4 / float(y) ** 2
    print(a)
    if a < 18.5:
        message_ =  tkinter.Message(text="Your BMI is {:.2f}.You are underweight.".format(a))
        message_.config(width=350, bg="aliceblue")
        message_.place(x=70, y=300)
    elif 18.5<=a<=25:
        message_1 = tkinter.Message(text="Your BMI is {:.2f}.You are normal weight.".format(a) )
        message_1.config(width=350, bg="aliceblue")
        message_1.place(x=70, y=300)
    elif 25 <a<=30:
        message_2 = tkinter.Message(text="Your BMI is {:.2f}.You are overweight.".format(a))
        message_2.config(width=350,bg="aliceblue")
        message_2.place(x=70, y=300)
    elif 30<a<40:
        message_3 = tkinter.Message(text="Your BMI is {:.2f}.You are obese.".format(a))
        message_3.config(width=350, bg="aliceblue")
        message_3.place(x=70, y=300)
    else:
        message_4 = tkinter.Message(text="Your BMI is {:.2f}.You are morbidly obese.".format(a))
        message_4.config(width=350, bg="aliceblue")
        message_4.place(x=70, y=300)







my_button = tkinter.Button(text="Calculate", command=input_calculate)
my_button.place(x=175, y=200)

window.mainloop()

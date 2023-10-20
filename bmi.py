import tkinter

#make a tkinter window
window = tkinter.Tk()
window.minsize(400,400)
window.title("bmi_calculator")
window.config(pady=30,padx=30)


#x = weight
#y = height
#a = bmi

#ui

# ui title
title_label = tkinter.Label(text="BMI Calculator", font=("Courier", 25, "bold"))
title_label.config(bg="aquamarine")
title_label.pack()

# calculate bmi function with get a height and weight
def calculate_bmi():
    x = weight_input_entry.get()
    y = height_input_entry.get()
#normally calculate and handling erors method
    if x == "" or y == "":
        result_label.config(text="Enter both weight and height!..", bg="aliceblue")
    else:
        try:
            a = float(x) / (float(y)/100)**2
            result_string = write_result(a)
            result_label.config(text=result_string, bg="aliceblue")

        except:
            result_label.config(text="Enter a valid number!..", bg="aliceblue")






# make a label for entry-weight
weight_input_label = tkinter.Label(text="Enter your weight (kg)", font=("arial", 12, "bold"),bg="light grey")
weight_input_label.pack()
#make a entry for weight
weight_input_entry = tkinter.Entry(width=30)
weight_input_entry.pack()
#make a label for entry-height
height_input_label = tkinter.Label(text="Enter your height (cm)",font=("arial", 12, "bold"),bg="light grey")
height_input_label.pack()
#make a entry for height
height_input_entry = tkinter.Entry(width=30)
height_input_entry.pack()
#make calculate button for calculate bmi
calculate_button = tkinter.Button(text="Calculate",command=calculate_bmi)
calculate_button.pack()
#make the result label
result_label = tkinter.Label()
result_label.pack()
# the function for result label with bmi result
def write_result(a):
    result_string = f" Your BMI is: {round(a,2)} . You are "
    if a <= 16:
        result_string += "severely thinnes."

    elif 16 < a < 17:
        result_string += "moderate thinnes."
    elif 17 <= a < 18.5:
        result_string += "mild thinnes."
    elif 18.5 <= a <= 25:
        result_string += "normal weight."

    elif 25 < a <= 30:
        result_string += "overweight."
    elif 30 < a <= 35:
        result_string += "class 1 obesity."
    elif 35 < a <= 40:
        result_string += "class 2 obesity."
    else:
        result_string += "morbidly obesity."
    return result_string



window.mainloop()
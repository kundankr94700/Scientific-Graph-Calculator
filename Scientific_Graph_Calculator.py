from tkinter import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter.font import  Font
from math import *

root_g = Tk()

root_g.title("Scientific Graph Calculator                                                                                         Copyright @ Kundan Kumar")
root_g.geometry("1260x550+50+100")

figure1 = plt.Figure(figsize=(6, 5), dpi=100)
ax1 = figure1.add_subplot(1, 1, 1)
bar1 = FigureCanvasTkAgg(figure1, root_g)
bar1.get_tk_widget().pack(side=RIGHT, fill=BOTH)
y1 = np.arange(-15, 15, 0.1)
x1 = [0] * len(y1)
x2 = np.arange(-15, 15, 0.1)
y2 = [0] * len(x2)

ax1.plot(x1, y1)
ax1.plot(x2, y2)

convert_constant = 1
inverse_convert_constant = 1
def plot_():
    loc = []
    y = []
    domain_ = []
    xx = np.arange(-10, 10, 0.1)
    pp = list(text_input.get())
    def More_details():
        root_p.destroy()

        def View_plot():
            root1.destroy()
            y = []
            domain_ = []
            xmin=int(ge1.get())
            xmax=int(ge2.get())
            fig = plt.figure(0, figsize=(6, 6.1))
            xx = np.arange(xmin,xmax, 0.1)

            for i in xx:
                for k in loc:
                    pp[k] = str(i)
                pp1 = ''.join(xp for xp in pp)
                try:
                    result = eval(pp1)
                    y.append(result)
                    domain_.append(i)
                except:
                    pass

            fig.canvas.set_window_title('Scientific Graph Calculator')
            plt.title('Scientific Graph Calculator')
            plt.plot(domain_, y)
            plt.show()

        ge1=StringVar()
        ge2 = StringVar()
        f4 = Font(family="Time New Roman", size=11, weight="bold")
        root1 = Toplevel()
        root1.title('Person_Count_Application')
        root1.geometry('350x150+715+100')

        l3 = Label(root1, text="Machine Learning Training Project", fg='brown', font=f4).place(x=40, y=10)
        l = Label(root1, text='   Enter Range Of X -Axis ', fg='DarkGreen', font=f4).place(x=80, y=40)
        Entry(root1,textvariable=ge1,width=10).place(x=100,y=80)
        Entry(root1, textvariable=ge2, width=10).place(x=260, y=80)
        Label(root1, text='X_Min :', fg='red', font=f4).place(x=20, y=80)
        Label(root1, text='X_Max :', fg='red', font=f4).place(x=200, y=80)
        b2 = Button(root1, text='Plot', command=View_plot, width=15, height=1, bg='brown', font=f4).place(x=110, y=110)
        root1.mainloop()

    if 'x' in pp:

        for j in range(len(pp)):
            if pp[j] == 'x':
                loc.append(j)
    for i in xx:
        for k in loc:
            pp[k] = str(i)
        pp1 = ''.join(xp for xp in pp)
        try:
            result = eval(pp1)
            y.append(result)
            domain_.append(i)


        except:
            pass

    root_p = Toplevel()
    root_p.geometry('600x550+715+100')
    root_p.title("Scientific Graph Calculator")

    figure1 = plt.Figure(figsize=(6, 5), dpi=100)
    ax1 = figure1.add_subplot(1, 1, 1)
    bar1 = FigureCanvasTkAgg(figure1, root_p)
    bar1.get_tk_widget().pack(side=RIGHT, fill=BOTH)

    try:
        y1 = y
        x2 = domain_

        ax1.plot(domain_, y)
        x1 = [0] * len(y1)
        y2 = [0] * len(x2)
        ax1.plot(x1, y1)
        ax1.plot(x2, y2)


    except ZeroDivisionError:
        text_input.set('ZeroDivisionError: division by zero')
    except:
        text_input.set('Error')
    f1 = Font(family="Time New Roman", size=11, weight="bold", underline=1)
    b = Button(root_p, text='Exit', width=18, height=1, command=root_p.destroy,font=f1).place(x=400, y=515)
    b = Button(root_p, text='More Details', width=18, height=1, command=More_details,font=f1).place(x=250, y=515)
    root_p.resizable(False, False)
    root_p.mainloop()


def btn_equal():
    global expression
    try:
        x11 = text_input.get()
        sum_up = str(eval(x11))
        text_input.set(sum_up)
        expression = sum_up
    except Exception as E:
        text_input.set(E.args[0])


def btn_click(expression_val):
    global expression
    if len(expression) >= 23:
        expression = expression
        text_input.set(expression)
    else:
        expression = expression + str(expression_val)
        text_input.set(expression)


def btn_clear_all():
    global expression
    expression = ""
    text_input.set("")


def btn_clear1():
    global expression
    expression = expression[:-1]
    text_input.set(expression)


def change_signs():
    global expression
    expression = expression + '-'
    text_input.set(expression)


default = {
    'padx': 16,
    'pady': 1,
    'bd': 4,
    'fg': 'Black',
    'bg': 'white',
    'font': ('arial', 18),
    'width': 2,
    'height': 2,
    'relief': 'flat',

}

default_ = {
    'padx': 16,
    'pady': 1,
    'bd': 4,
    'fg': 'white',
    'bg': 'darkblue',
    'font': ('arial', 18),
    'width': 2,
    'height': 2,
    'relief': 'flat',

}
expression = ""

text_input = StringVar()
master = root_g
top_frame = Frame(master, width=650, height=20, bd=4, relief='flat', bg='darkBlue')
top_frame.pack(side=TOP)
bottom_frame = Frame(master, width=650, height=470, bd=4, relief='flat', bg='darkblue')
bottom_frame.pack(side=BOTTOM)
my_item = Label(top_frame, text="Simple Scientific Calculator", font=('arial', 20), fg='white', width=26,
                bg='darkblue')
my_item.pack()
txt_display = Entry(top_frame, font=('arial', 36), relief='flat', bg='grey', fg='white', textvariable=text_input,
                    width=60, bd=4, justify='right')
txt_display.pack()

btn_left_brack = Button(bottom_frame, **default, text="(", command=lambda: btn_click('('))
btn_left_brack.grid(row=0, column=0)

btn_right_brack = Button(bottom_frame, **default, text=")", command=lambda: btn_click(')'))
btn_right_brack.grid(row=0, column=1)

btn_exp = Button(bottom_frame, **default, text="exp", command=lambda: btn_click('exp('))
btn_exp.grid(row=0, column=2)

btn_pi = Button(bottom_frame, **default, text="π", command=lambda: btn_click('pi'))
btn_pi.grid(row=0, column=3)
btn_clear = Button(bottom_frame, **default, text="C", command=btn_clear_all)
btn_clear.grid(row=0, column=4)

btn_del = Button(bottom_frame, **default, text="del", command=btn_clear1)
btn_del.grid(row=0, column=5)

btn_change_sign = Button(bottom_frame, **default, text="+/-", command=change_signs)
btn_change_sign.grid(row=0, column=6)

btn_div = Button(bottom_frame, **default, text="/", command=lambda: btn_click('/'))
btn_div.grid(row=0, column=7)

btn_sqrt = Button(bottom_frame, **default, text="sqrt", command=lambda: btn_click('sqrt('))
btn_sqrt.grid(row=0, column=8)

cube = Button(bottom_frame, **default, text=u"x\u00B3", command=lambda: btn_click('**3'))
cube.grid(row=1, column=2)

btn_abs = Button(bottom_frame, **default, text="abs", command=lambda: btn_click('abs' + '('))
btn_abs.grid(row=1, column=3)
btn_7 = Button(bottom_frame, **default_, text="7", command=lambda: btn_click(7))
btn_7.grid(row=1, column=4)

btn_8 = Button(bottom_frame, **default_, text="8", command=lambda: btn_click(8))

btn_8.grid(row=1, column=5)

btn_9 = Button(bottom_frame, **default_, text="9", command=lambda: btn_click(9))
btn_9.grid(row=1, column=6)

btn_mult = Button(bottom_frame, **default, text="x", command=lambda: btn_click('*'))
btn_mult.grid(row=1, column=7)

btn_x = Button(bottom_frame, **default, text="X", command=lambda: btn_click('x'))
btn_x.grid(row=1, column=8)

btn_sin = Button(bottom_frame, **default, text="sin", command=lambda: btn_click('sin('))
btn_sin.grid(row=2, column=0)

btn_cos = Button(bottom_frame, **default, text="cos", command=lambda: btn_click('cos('))
btn_cos.grid(row=2, column=1)

btn_tan = Button(bottom_frame, **default, text="tan", command=lambda: btn_click('tan('))
btn_tan.grid(row=2, column=2)

btn_log = Button(bottom_frame, **default, text="log", command=lambda: btn_click('log('))
btn_log.grid(row=2, column=3)

btn_4 = Button(bottom_frame, **default_, text="4", command=lambda: btn_click(4))
btn_4.grid(row=2, column=4)

btn_5 = Button(bottom_frame, **default_, text="5", command=lambda: btn_click(5))
btn_5.grid(row=2, column=5)

btn_6 = Button(bottom_frame, **default_, text="6", command=lambda: btn_click(6))

btn_6.grid(row=2, column=6)

btnSub = Button(bottom_frame, **default, text="-", command=lambda: btn_click('-'))
btnSub.grid(row=2, column=7)

btn_Gr = Button(bottom_frame, **default, text=">", command=lambda: btn_click('>'))
btn_Gr.grid(row=2, column=8)

btn_sin_inverse = Button(bottom_frame, **default, text=u"sin-\u00B9", command=lambda: btn_click('asin('))
btn_sin_inverse.grid(row=3, column=0)

btn_cos_inverse = Button(bottom_frame, **default, text=u"cos-\u00B9", command=lambda: btn_click('acos('))
btn_cos_inverse.grid(row=3, column=1)

btn_tan_inverse = Button(bottom_frame, **default, text=u"tan-\u00B9", command=lambda: btn_click('atan('))
btn_tan_inverse.grid(row=3, column=2)

btn_ln = Button(bottom_frame, **default, text="ln", command=lambda: btn_click('ln('))
btn_ln.grid(row=3, column=3)

btn_1 = Button(bottom_frame, **default_, text="1", command=lambda: btn_click(1))

btn_1.grid(row=3, column=4)

btn_2 = Button(bottom_frame, **default_, text="2", command=lambda: btn_click(2))

btn_2.grid(row=3, column=5)

btn_3 = Button(bottom_frame, **default_, text="3", command=lambda: btn_click(3))

btn_3.grid(row=3, column=6)

btn_add = Button(bottom_frame, **default, text="+", command=lambda: btn_click('+'))
btn_add.grid(row=3, column=7)

btn_lt = Button(bottom_frame, **default, text="<", command=lambda: btn_click('<'))
btn_lt.grid(row=3, column=8)

btn_fact = Button(bottom_frame, **default, text="n!", command=lambda: btn_click('factorial('))
btn_fact.grid(row=4, column=0)

btn_sqr = Button(bottom_frame, **default, text=u"x\u00B2", command=lambda: btn_click('**2'))
btn_sqr.grid(row=4, column=1)

btn_power = Button(bottom_frame, **default, text="x^y", command=lambda: btn_click('**'))
btn_power.grid(row=4, column=2)

btn_ans = Button(bottom_frame, **default, text=".", command=lambda: btn_click('.'))
btn_ans.grid(row=4, column=3)

btn_0 = Button(bottom_frame, **default_, text="0", command=lambda: btn_click(0))

btn_0.grid(row=4, column=4, columnspan=2)

btn_eq = Button(bottom_frame, **default_, text="=", command=btn_equal)
btn_eq.grid(row=4, column=6)

btn_dec = Button(bottom_frame, **default, text="Plot", command=plot_)
btn_dec.grid(row=4, column=7)

btn_comma = Button(bottom_frame, **default, text=",", command=lambda: btn_click(','))
btn_comma.grid(row=4, column=8)

b = Button(root_g, text='Exit', width=18, height=1, command=root_g.destroy).place(x=1100, y=610)

root_g.mainloop()
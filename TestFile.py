import datetime
from pyexpat import model
from tkinter.ttk import Combobox
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from openpyxl import load_workbook
from tkinter import *
import sys
import os
from sklearn.metrics import r2_score
import ml_metrics as metrics
import pandas as pd
import matplotlib.pyplot as plt

file = "Information.xlsx"
wb = load_workbook(file)
wb.active = 0
sheet = wb.active
m_y = []
dataX = [datetime.date(year=2020, month=1, day=1), datetime.date(year=2021, month=1, day=1)]
def plot():
    fig = Figure(figsize=(5, 5), dpi=100)
    y = m_y
    x = dataX
    plot1 = fig.add_subplot(111)
    plot1.plot(x, y)
    plot1.plot(figsize=(12, 6))
    plot1.plot(style='r--')
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    canvas.get_tk_widget().pack()
    toolbar = NavigationToolbar2Tk(canvas, window)
    toolbar.update()
    canvas.get_tk_widget().pack()

def areaContr():
    num = 0
    for i in range(3, len(sheet['A']) + 1):
        area = str(sheet['B' + str(i)].value)
        if area == "Восточно-Казахстанская область" and comboA.get() == "Восточно-Казахстанская область":
            num += 1
            lblArea.config(text=num)
        if area == "Павлодарская область" and comboA.get() == "Павлодарская область":
            num += 1
            lblArea.config(text=num)
    m_y.append(num)

def analitics2022():
    analitics = sum(m_y) / len(m_y)
    dataX.append(datetime.date(year=2022, month=1, day=1))
    m_y.append(analitics)

window = Tk()
window.title("Аналитика заболевших Covid-19")
window.geometry('500x600')

lblYears = Label(master=window, text="Область", font=("Arial Bold", 10))
lblYears.pack()
comboA = Combobox(master=window)
comboA['values'] = ('Павлодарская область', 'Восточно-Казахстанская область')
comboA.current(0)
comboA.pack()

btnAdd = Button(master=window, text="Записать", command=areaContr)
btnAdd.pack()
lblArea = Label(master=window, text="0000", font=("Arial Bold", 10))
lblArea.pack()

btnAdd = Button(master=window, text="Добавить аналитику на 2022", command=analitics2022)
btnAdd.pack()

btnPlot = Button(master=window,
                     command=plot,
                     height=2,
                     width=10,
                     text="График")
btnPlot.pack()
window.mainloop()
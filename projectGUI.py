from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

root=Tk()
  
canvas1 = Canvas(root, width = 1000, height = 350)
canvas1.pack()

    

enter_date = StringVar()
entry1 = Entry (root,textvariable=enter_date)
canvas1.create_window(80, 50, window=entry1)
enter_date.set("Wed May 21 00:00:00 EDT 2008")


# 1)Plot a graph indicating total number sales on date: May ’21 2008
def sale_data():
    cardata = pd.read_csv("C:\Phani\Python Project\Sacramentorealestatetransactions.csv")
    my_date=enter_date.get()
    #print(my_date);
    #print(cardata)

    bysaledata = cardata[cardata['sale_date']==my_date]
    print(bysaledata)
    plt.scatter(bysaledata['sale_date'], bysaledata['price'])
    plt.xlabel('Sale Date')
    plt.ylabel('Price')
    plt.title("Scatter Plot on "+my_date)
    plt.show()

#2)Plot a graph indicating based on location
# information like longitude and latitude of Sacramento city and
# indicate the total sales for that city.
def latitude():
    cardata = pd.read_csv("C:\Phani\Python Project\Sacramentorealestatetransactions.csv")
    my_date = enter_date.get()

    bysaledata = cardata[cardata['sale_date'] == my_date]
    plt.plot(bysaledata['price'], bysaledata['latitude'])
    plt.xlabel('price')
    plt.ylabel('latitude')
    plt.title("Plot of Latitude VS Price ")
    plt.show()

def longitude():
    cardata = pd.read_csv("C:\Phani\Python Project\Sacramentorealestatetransactions.csv")
    my_date = enter_date.get()

    bysaledata = cardata[cardata['sale_date'] == my_date]
    plt.plot(bysaledata['price'], bysaledata['longitude'])
    plt.xlabel('price')
    plt.ylabel('longitude')
    plt.title("Plot of Longitude VS Price ")
    plt.show()

#3)	Plot a graph indicating number of beds for that city
def beds():
    cardata = pd.read_csv("C:\Phani\Python Project\Sacramentorealestatetransactions.csv")
    my_date = enter_date.get()

    bysaledata = cardata[cardata['sale_date'] == my_date]
    #bysaledata['çity']
    bycity = bysaledata.groupby(['city']).sum()
    plt.plot(bycity['beds'])
    #print(bycity['beds'])
    plt.xlabel('city')
    plt.xticks(rotation=45)
    plt.ylabel('beds')
    plt.title("Plot of Beds VS city ")
    plt.show()

def pie():
    cardata = pd.read_csv("C:\Phani\Python Project\Sacramentorealestatetransactions.csv")
    my_date = enter_date.get()

    bysaledata = cardata[cardata['sale_date'] == my_date]
    #bysaledata['çity']
    bycity = bysaledata.groupby(['zip']).sum()
    plt.pie(bycity['price'], labels=bycity['price'].keys())
    #print(bycity['beds'])

    plt.title("Plot of Total Sales by Zip")
    plt.show()


def RA():
    cardata = pd.read_csv("C:\Phani\Python Project\Sacramentorealestatetransactions.csv")
    my_date = enter_date.get()

    bysaledata = cardata[cardata['sale_date'] == my_date]
    bysaledata = bysaledata[bysaledata['type'] == 'Residential']
    bycity = bysaledata.groupby(['city']).sum()
    plt.plot(bycity['sq__ft'])
    print(bycity['sq__ft'])
    plt.xlabel('city')
    plt.xticks(rotation=45)
    plt.ylabel('Total Residential Area')
    plt.title("Plot of Total Residential Area VS city ")
    plt.show()

button2 = Button(root, text='sale data on date ', command=sale_data)
canvas1.create_window(80, 80, window=button2)
button3 = Button(root, text='latitude vs price ', command=latitude)
canvas1.create_window(80, 120, window=button3)
button4 = Button(root, text='longitude vs price ', command=longitude)
canvas1.create_window(80, 160, window=button4)
button5= Button(root, text='beds vs city ', command=beds)
canvas1.create_window(80, 200, window=button5)
button6= Button(root, text='Total Residential Area vs city ', command=RA)
canvas1.create_window(80, 240, window=button6)
button7= Button(root, text='Pie of Total Sales by zip code ', command=pie)
canvas1.create_window(80, 280, window=button7)
root.mainloop()

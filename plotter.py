import os
import csv
import sys
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm, rcParams
from config import *

#Information for nasalization font.
FONT_PATH = os.path.join(rcParams["datapath"], os.path.abspath(FONT_PATH))
FONT_PROPS = fm.FontProperties(fname=FONT_PATH)

#Index's for data points in .csv
TYPE_INDEX = 0
MASS_INDEX = 1
LUMINOSITY_INDEX = 2
TEMP_INDEX = 4

#Values for latter analysis.
min_temp = float('inf')
min_lum = float('inf')
min_mass = float('inf')
max_lum = 0
max_mass = 0
max_temp = 0

#Dark background theme
plt.style.use('dark_background')


#Data dictionary for each value.
category_mapping = {
    "O": {"X": [], "Y": [], "Color": 'tab:blue'},
    "B": {"X": [], "Y": [], "Color": 'tab:orange'},
    "A": {"X": [], "Y": [], "Color": 'tab:purple'},
    "F": {"X": [], "Y": [], "Color": 'tab:green'},
    "G": {"X": [], "Y": [], "Color": 'tab:pink'},
    "K": {"X": [], "Y": [], "Color": 'tab:red'},
    "M": {"X": [], "Y": [], "Color": 'tab:cyan'},

}


#Read the csv and get relevant data
with open(CSV_PATH) as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        print(row)
        luminos = float(row[LUMINOSITY_INDEX])
        temp = int(row[TEMP_INDEX])
        category = (row[TYPE_INDEX][0])
        if category not in category_mapping:
            pass
        else:
            category_mapping[category]['X'].append(temp)
            category_mapping[category]['Y'].append(luminos)


#Get data
fig, ax = plt.subplots()

#Iterate over categories in data dict and plot points.
for i in category_mapping:
    temp_vals = category_mapping[i]["X"]
    luminos_vals = category_mapping[i]["Y"]
    color = category_mapping[i]['Color']
    ax.scatter(x=temp_vals, y=luminos_vals, s=5, label=i, c=color)

#Set scaling information for graph.
ax.set_yscale('log')
ax.set_xticks([2000, 5000, 10000, 20000, 40000])
ax.set_ylim([0.0001,1000000])
ax.set_xlim([0, 42000])
ax.legend(prop=FONT_PROPS)
lims = plt.xlim()
plt.xlim([lims[1], lims[0]]) 


#Set graph text information
plt.xlabel("Temperature in Kelvin", fontproperties=FONT_PROPS)
plt.ylabel("Luminosity", fontproperties=FONT_PROPS)
plt.title("HR Diagram with Stellar Classification", fontproperties=FONT_PROPS)
plt.yticks(fontproperties=FONT_PROPS, fontsize=10)
plt.xticks(fontproperties=FONT_PROPS, fontsize=7)

#Save off a file for infographic
plt.savefig("imgs/hr_diagram.png")

#Show the plot of the data
if SHOW_GRAPH:
    plt.show()


import os
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm, rcParams
from config import *


#Information for nasalization font.
FONT_PATH_CONFIGURED = os.path.join(rcParams["datapath"], os.path.abspath(FONT_PATH))
FONT_PROPS = fm.FontProperties(fname=FONT_PATH_CONFIGURED)

#Dark background theme
plt.style.use('dark_background')

#Objects to plot
objects = 'O', 'B', 'A', 'F', 'G', 'K', 'M'
y_pos = np.arange(len(objects))
#Percentages for each
percentages = [0.00001, 0.1, 0.7, 2, 3.5, 8, 80]

#Configure individual values.
fig, ax = plt.subplots()
for i, v in enumerate(percentages):
    ax.text(v + 3, i, str(v) + ' %', color='white', fontproperties=FONT_PROPS)

#Plot the bar and configure axis
plt.barh(y_pos, percentages, align='center', alpha=0.5, color = 'aqua')
plt.yticks(y_pos, objects)
plt.xticks([i*10 for i in range(0,11)])


#Set graph text information
plt.xlabel("Percentage", fontproperties=FONT_PROPS)
plt.ylabel("Stellar Class", fontproperties=FONT_PROPS)
plt.title("Estimated Stellar Class Percentage", fontproperties=FONT_PROPS)
plt.yticks(fontproperties=FONT_PROPS, fontsize=10)
plt.xticks(fontproperties=FONT_PROPS, fontsize=10)

#Save off a file for infographic
plt.savefig("imgs/stellar_percentages.png")

#Show the plot of the data
if SHOW_GRAPH:
    plt.show()


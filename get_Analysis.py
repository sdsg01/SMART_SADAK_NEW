#import time
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
from database1 import *

class get_analysis:
    def show_data(self):
        list1 = []
        list2 = []
        start = input("enter the starting timestamp: ")
        end = input("enter the starting timestamp: ")
       # print(type(start)
        #print(end)
        for i in range(0,start, end):
            list1.append(str(i) + '-' + str(i + 1))
        for i in range(0,start, end):
            x = str(i) + '0000'
            y = str(i + 1) + '0000'
            x = [x[i:i + 2] for i in range(0, len(x), 2)]
            y = [y[i:i + 2] for i in range(0, len(y), 2)]
            # print(x)
            list2.append(get_count(join_string(x), join_string(y)))
        plt.bar(list1, list2, align='center', alpha=0.5)
        plt.xticks(list1)
        plt.ylabel('No of Vehicles')
        plt.title('Traffic Congestion Data')

        plt.show()





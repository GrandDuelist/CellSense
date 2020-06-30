import pandas as pd
import matplotlib.pyplot as plt
from cpssdk import CPSPlot
from matplotlib.ticker import FuncFormatter
import numpy as np
from matplotlib import rcParams
import math
rcParams['font.family'] = 'Times New Roman'


class CDRPlotter():
    def __init__(self,plotdata):
        self.cpsplot = CPSPlot()
        self.plotdata = plotdata

    def plotNewLocationCDF(self,filepath):
        ax = self.plotdata.plot(kind="line",fontsize =25,style=['ks-'],grid='True',\
            x="New Locations (#)", y = "Users (%)", lw=2,ms=10,legend=None,\
            markerfacecolor='white',markevery=1)

        plt.gca().yaxis.set_major_formatter(FuncFormatter(lambda y, _: int(y*100)))
        # plt.gca().xaxis.set_major_formatter(FuncFormatter(lambda y, _: int(y/3600.0)))
        ax.set_ylabel("CDF (%)",fontsize=25)
        ax.set_xlabel("New Locations (#)",fontsize=25)
        plt.yticks(np.arange(0,1.1,0.2))
        plt.xlim(-2,50)
        plt.savefig(filepath, bbox_inches='tight')
        plt.show()

    def locationCountToCDF(self):
        (ys,xs) = self.cpsplot.binCount(self.plotdata['count'].tolist(),100)
        self.plotdata =  pd.DataFrame(data={'New Locations (#)':xs, "Users (%)": ys})
        print(self.plotdata)


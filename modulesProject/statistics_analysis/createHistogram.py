'''
clase que permite hacer un histograma de un set de datos...
recibe el set de datos y una key asociada a la columna correspondiente...
ademas del nombre del archivo para alojar el resultado...
'''

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sys
import seaborn as sns
from pandas.tools.plotting import parallel_coordinates
from sklearn.preprocessing import MinMaxScaler
import pandas.tools.plotting as pdplt

class histograme(object):

    def __init__(self, dataSet):

        self.dataSet = dataSet

    #funcion que permite crear un histograma...
    def generateHistogram(self, key, exportName, title):

        #plt.figure()
        sns.set(color_codes=True)
        sns.set(style="ticks")
        sns_plot = sns.distplot(self.dataSet[key] , color="olive", label=key, kde=False, rug=True)
        sns.plt.legend()
        sns.plt.title(title)
        sns_plot.figure.savefig(exportName)

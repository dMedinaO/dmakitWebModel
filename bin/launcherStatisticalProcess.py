'''
script que permite hacer diversas llamadas a las clases de los modulos de estadistica con respecto a la solicitud que genere el
usuario
'''

import sys
import pandas as pd

from modulesProject.statistics_analysis import createPieChartFromDataSet
from modulesProject.statistics_analysis import getValuesInDataSet

#recibimos los datos de entrada...
option = int(sys.argv[1])
user = sys.argv[2]#viene desde variable de sesion
job = sys.argv[3]#viene desde variable de sesion
nameFile = sys.argv[4] #viene desde variable de sesion

dataSet = pd.read_csv("/home/dmedina/Escritorio/proyects/smartTraining/dataStorage/"+user+"/"+job+"/"+nameFile)

if option == 1:#pie chart
    keyData = sys.argv[5]
    pieChartObject = createPieChartFromDataSet.pieChart(dataSet, keyData)
    pieChartObject.createExport()

if option == 2:#histogram
    keyData = sys.argv[5]
    histogram = getValuesInDataSet.searchData(dataSet, keyData)
    histogram.searchValues()

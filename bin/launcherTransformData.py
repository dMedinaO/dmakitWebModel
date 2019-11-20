'''
script que permite aplicar la transformacion de los datos segun el tipo de requerimiento que desee
'''

from modulesProject.utils import ScaleDataSetLog
from modulesProject.utils import ScaleMinMax
from modulesProject.utils import ScaleNormalScore
from modulesProject.utils import ScaleLogNormalScore
from modulesProject.utils import transformFrequence

import sys

user = sys.argv[1]#test with 1
job = sys.argv[2]#test with 1
dataSet = sys.argv[3]#test with testingFeature.csv
pathResponse = sys.argv[4] #donde se almacenara el nuevo set de datos
optionProcess = int(sys.argv[5]) # opciones de cambios posibles
kindDataSet = sys.argv[6]#tipo de set de datos, si es con clases o sin clases...

if optionProcess == 1:#escalar en logaritmica

    #generamos el set de datos transformado...
    nameFile = pathResponse+user+"/"+job+"/"+"transformLogScale_"+job+".csv"
    scaleLog = ScaleDataSetLog.applyLogScale(dataSet, nameFile, kindDataSet)

if optionProcess == 2:#escalar en min max scaler
    nameFile = pathResponse+user+"/"+job+"/"+"transformMinMaxScale_"+job+".csv"
    scaleNormal = ScaleMinMax.applyMinMaxScaler(dataSet, nameFile, kindDataSet)

if optionProcess == 3:#escalar en z score
    nameFile = pathResponse+user+"/"+job+"/"+"transformNormalScale_"+job+".csv"
    scaleNormal = ScaleNormalScore.applyNormalScale(dataSet, nameFile, kindDataSet)

if optionProcess == 4:#escalar en log z score
    nameFile = pathResponse+user+"/"+job+"/"+"transformLogNormalScale_"+job+".csv"
    scaleNormal = ScaleLogNormalScore.applyLogNormalScale(dataSet, nameFile, kindDataSet)

if optionProcess == 5:#transformar a frecuencias
    nameFile = pathResponse+user+"/"+job+"/"+"transformFrequenceData_"+job+".csv"
    scaleNormal = transformFrequence.frequenceData(dataSet, nameFile, kindDataSet)

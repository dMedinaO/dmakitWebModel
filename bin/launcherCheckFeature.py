'''
script que permite hacer la insercion de las features en la BD con respecto al tipo de feature
# NOTE: este proceso solo se hace en el analisis estadistico
'''

from modulesProject.checks_module import getKindFeaturesInDataSet
import sys

dataSet = sys.argv[1]
idDataSet = sys.argv[2]

execError =0

#instanciamos al objeto...
kindFeatures = getKindFeaturesInDataSet.checkDataSet(dataSet, idDataSet)
kindFeatures.insertFeaturesDB()

'''
launcher asociado al proceso de test estadisticos, es capaz de representar diferentes test con respecto a la opcion a desarrollar
'''

import sys
import json
from modulesProject.statistical_test import launcherStatisticalTest

#recibimos la data de interes...
dataSet = sys.argv[1]
optionProcess = sys.argv[2]

#hacemos la instancia al objeto y ejecutamos el proceso
launcherProcess = launcherStatisticalTest.statisticalTest(dataSet, optionProcess)
launcherProcess.checkExec()

print json.dumps(launcherProcess.response)

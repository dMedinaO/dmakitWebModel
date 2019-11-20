from modulesProject.statistical_test import getResultsFromTest
import pandas as pd
import json

#definicion de la clase
class statisticalTest(object):

    def __init__(self, dataSet, optionProcess):

        self.dataSet = dataSet
        self.optionProcess = int(optionProcess)
        self.data = pd.read_csv(dataSet)
        self.listKey = []
        for element in self.data:
            self.listKey.append(element)
        self.response = {}

    def checkExec(self):
        if self.optionProcess == 1:#Coeficiente de pearson
            try:
                dataObject1 = getResultsFromTest.ResultsFromTest()
                ResultFromPearson=dataObject1.Pearson(self.data[self.listKey[0]], self.data[self.listKey[1]])
                self.response.update({"stadistic": ResultFromPearson[0]})
                self.response.update({"p_value": ResultFromPearson[1]})
                self.response.update({"exec": "OK"})
            except:
                self.response.update({"exec": "ERROR"})
                pass

        elif self.optionProcess == 2:#Coeficiente de spearman
            try:
                dataObject2 = getResultsFromTest.ResultsFromTest()
                ResultFromSpearman=dataObject2.Spearman(self.data[self.listKey[0]], self.data[self.listKey[1]])
                self.response.update({"stadistic": ResultFromSpearman[0]})
                self.response.update({"p_value": ResultFromSpearman[1]})
                self.response.update({"exec": "OK"})
            except:
                self.response.update({"exec": "ERROR"})
                pass

        elif self.optionProcess == 3:#Coeficiente kendalltau
            try:
                dataObject3 = getResultsFromTest.ResultsFromTest()
                ResultFromKendalltau=dataObject3.Kendalltau(self.data[self.listKey[0]], self.data[self.listKey[1]])
                self.response.update({"stadistic": ResultFromKendalltau[0]})
                self.response.update({"p_value": ResultFromKendalltau[1]})
                self.response.update({"exec": "OK"})
            except:
                self.response.update({"exec": "ERROR"})
                pass

        elif self.optionProcess == 4:#Mann Whitney
            try:
                dataObject4 = getResultsFromTest.ResultsFromTest()
                ResultFromMannWhitney=dataObject4.MannWhitney(self.data[self.listKey[0]], self.data[self.listKey[1]])
                self.response.update({"stadistic": ResultFromMannWhitney[0]})
                self.response.update({"p_value": ResultFromMannWhitney[1]})
                self.response.update({"exec": "OK"})
            except:
                self.response.update({"exec": "ERROR"})
                pass

        elif self.optionProcess == 5:#Kolmogorov
            try:
                dataObject5 = getResultsFromTest.ResultsFromTest()
                ResultFromKolmogorov=dataObject5.Kolmogorov(self.data[self.listKey[0]])
                self.response.update({"stadistic": ResultFromKolmogorov[0]})
                self.response.update({"p_value": ResultFromKolmogorov[1]})
                self.response.update({"exec": "OK"})
            except:
                self.response.update({"exec": "ERROR"})
                pass

        elif self.optionProcess == 6:#Shapiro
            try:
                dataObject6 = getResultsFromTest.ResultsFromTest()
                ResultFromShapiro=dataObject6.Shapiro(self.data[self.listKey[0]])
                self.response.update({"stadistic": ResultFromShapiro[0]})
                self.response.update({"p_value": ResultFromShapiro[1]})
                self.response.update({"exec": "OK"})
            except:
                self.response.update({"exec": "ERROR"})
                pass

        elif self.optionProcess == 7:#ANOVA
            try:
                dataObject7 = getResultsFromTest.ResultsFromTest()
                matrix=self.data.values
                ResultFromANOVA=dataObject7.ANOVA(matrix)
                self.response.update({"stadistic": ResultFromANOVA[0]})
                self.response.update({"p_value": ResultFromANOVA[1]})
                self.response.update({"exec": "OK"})
            except:
                self.response.update({"exec": "ERROR"})
                pass

        else:#T test
            try:
                dataObject8 = getResultsFromTest.ResultsFromTest()
                ResultFromT_test=dataObject8.T_test(self.data[self.listKey[0]], self.data[self.listKey[1]])
                self.response.update({"stadistic": ResultFromT_test[0]})
                self.response.update({"p_value": ResultFromT_test[1]})
                self.response.update({"exec": "OK"})
            except:
                self.response.update({"exec": "ERROR"})
                pass

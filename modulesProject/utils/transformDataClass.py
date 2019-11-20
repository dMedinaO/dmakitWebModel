'''
clase que permite transformar un arreglo de las clases en datos numericos segun el orden de aparicion
en el set de datos
'''

class transformClass(object):

    def __init__(self, arrayData):

        self.arrayData = arrayData
        self.transformData, self.dictTransform = self.transformClassData(self.arrayData)

    #metodo que permite definir el tipo de data...
    def checkData(self, array):
        response = 0

        try:
            for i in array:
                data = float(i)
        except:
            response = 1
        return response

    #metodo que transforma la clase en valores continuos desde el 0 hasta el n...
    def transformClassData(self, array):

        #preguntamos si la clase es letras o numeros
        valueClass = list(set(array))
        dictResponse = {}
        dataResponse = []

        if self.checkData(array) == 1:
            index=0
            for value in valueClass:
                dictResponse.update({value:index})
                index+=1
            for i in array:
                dataResponse.append(dictResponse[i])
        else:
            dataResponse = array

        return dataResponse, dictResponse

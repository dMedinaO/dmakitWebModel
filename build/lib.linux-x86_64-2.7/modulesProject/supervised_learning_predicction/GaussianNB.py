
'''
Author:
mailto:
Name Classs:
Description:
Dependences:
'''

from sklearn.naive_bayes import GaussianNB

class Gaussian(object):

    def __init__(self,dataset,response):
        self.dataset=dataset
        self.response=response        

    def trainingMethod(self):

        self.model=GaussianNB()
        self.GaussianNBAlgorithm=self.model.fit(self.dataset,self.response)
        self.predicctions = self.GaussianNBAlgorithm.predict(self.dataset)
        self.r_score = self.GaussianNBAlgorithm.score(self.dataset, self.response)
        print self.r_score

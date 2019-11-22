from sklearn import linear_model

class multiTaskElastic(object):

    def __init__(self, dataset, target):

        self.dataset = dataset
        self.target = target

    def trainingMethod(self):
         self.model= linear_model.MultiTaskElasticNet()
         self.multiTaskElasticModel =self.model.fit(self.dataset,self.target)
         self.predicctions = self.multiTaskElasticModel.predict(self.dataset)
         self.r_score = self.multiTaskElasticModel.score(self.dataset, self.target)

from sklearn import linear_model

class larsLasso(object):

    def __init__(self, dataset, target):

        self.dataset = dataset
        self.target = target

    def trainingMethod(self):
         self.model= linear_model.LassoLars()
         self.lassoLarsModel =self.model.fit(self.dataset,self.target)
         self.predicctions = self.lassoLarsModel.predict(self.dataset)
         self.r_score = self.lassoLarsModel.score(self.dataset, self.target)

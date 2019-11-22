from sklearn import linear_model

class lassoModel(object):

    def __init__(self, dataset, target):

        self.dataset = dataset
        self.target = target

    def trainingMethod(self):
         self.model= linear_model.Lasso()
         self.lassoModelO =self.model.fit(self.dataset,self.target)
         self.predicctions = self.lassoModelO.predict(self.dataset)
         self.r_score = self.lassoModelO.score(self.dataset, self.target)

from sklearn import linear_model

class bayessionRegression(object):

    def __init__(self, dataset, target):

        self.dataset = dataset
        self.target = target        

    def trainingMethod(self):
         self.model= linear_model.BayesianRidge()
         self.bayesianModel =self.model.fit(self.dataset,self.target)
         self.predicctions = self.bayesianModel.predict(self.dataset)
         self.r_score = self.bayesianModel.score(self.dataset, self.target)

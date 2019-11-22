from sklearn.linear_model import Ridge

class ridgeRegression(object):

    def __init__(self, dataset, target, solver, alpha):

        self.dataset = dataset
        self.target = target
        self.solver = solver
        self.alpha = alpha

    def trainingMethod(self):
         self.model= Ridge(alpha=self.alpha, solver=self.solver)
         self.ridgeModel =self.model.fit(self.dataset,self.target)
         self.predicctions = self.ridgeModel.predict(self.dataset)
         self.r_score = self.ridgeModel.score(self.dataset, self.target)

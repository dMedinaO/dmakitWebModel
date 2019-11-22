from sklearn import linear_model

class multiTaskLasso(object):

    def __init__(self, dataset, target):

        self.dataset=dataset
        self.target=target

    def trainingMethod(self):
         self.model= linear_model.MultiTaskLasso()
         self.multiTaskLassoModel =self.model.fit(self.dataset,self.target)
         self.predicctions = self.multiTaskLassoModel.predict(self.dataset)
         self.r_score = self.multiTaskLassoModel.score(self.dataset, self.target)

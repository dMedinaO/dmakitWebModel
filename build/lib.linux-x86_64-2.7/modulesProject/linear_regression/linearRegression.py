from sklearn import linear_model

class linearRegression(object):

    def __init__(self, dataset,target):

        self.dataset = dataset
        self.target = target

    def trainingMethod(self):
         self.model= linear_model.LinearRegression()
         self.linearModel =self.model.fit(self.dataset,self.target)
         self.predicctions = self.linearModel.predict(self.dataset)
         self.r_score = self.linearModel.score(self.dataset, self.target)

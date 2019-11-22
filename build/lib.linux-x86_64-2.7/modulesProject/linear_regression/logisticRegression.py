from sklearn.linear_model import LogisticRegression

class logisticRegression(object):

    def __init__(self, dataset, target):

        self.dataset = dataset
        self.target = target

    def trainingMethod(self):
         self.model= LogisticRegression(random_state=0, solver='lbfgs', multi_class='multinomial')
         self.logisticModel =self.model.fit(self.dataset,self.target)
         self.predicctions = self.logisticModel.predict(self.dataset)
         self.r_score = self.logisticModel.score(self.dataset, self.target)

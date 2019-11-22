from sklearn.linear_model import ElasticNet

class elasticNet(object):

    def __init__(self, dataset, target):

        self.dataset = dataset
        self.target = target

    def trainingMethod(self):
         self.model= ElasticNet(random_state=0)
         self.elasticModel =self.model.fit(self.dataset,self.target)
         self.predicctions = self.elasticModel.predict(self.dataset)
         self.r_score = self.elasticModel.score(self.dataset, self.target)

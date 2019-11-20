import numpy as np
import pandas as pd
from scipy import stats


class ResultsFromTest(object):
	def Pearson(self, x, y):#1
		return stats.pearsonr(x,y)

	def Spearman(self, x, y):#2
		return stats.spearmanr(x,y)

	def Kendalltau(self, x , y):#3
		return stats.kendalltau(x,y)

	def MannWhitney(self, x, y):#4
		return stats.mannwhitneyu(x,y)

	def Kolmogorov(self, x):#5
		return stats.kstest(x,'norm')

	def Shapiro(self, x):#6
		return stats.shapiro(x)

	def ANOVA(self, x):#7
		return stats.f_oneway(x)
		
	def T_test(self, x, y):#8
		return stats.ttest_ind(x,y)
from distutils.core import setup
import ConfigParser
import os

class SetupConfiguration:

    def __init__(self):

        self.setupInstall()

    def setupInstall(self):

        setup(name='projectDMAKit',
            version='alpha',
            description='DMAKit is a set of modules for create statistics and multiple analisys for machine learning',
            author='David Medina',
            author_email='david.medina@cebib.cl',
            license='Open GPL 3',
            packages=['modulesProject', 'modulesProject.clustering_analysis', 'modulesProject.checks_module', 'modulesProject.feature_analysis', 'modulesProject.statistics_analysis', 'modulesProject.supervised_learning_analysis', 'modulesProject.user_module', 'modulesProject.dataBase_module', 'modulesProject.supervised_learning_predicction', 'modulesProject.utils', 'modulesProject.statistical_test', 'modulesProject.linear_regression'],)

def main():

    setup = SetupConfiguration()
    return 0

if __name__ == '__main__':
    main()

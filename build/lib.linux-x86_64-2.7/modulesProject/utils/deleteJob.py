'''
clase que tiene la responsabilidad de eliminar un directorio
'''

import os
class removeDir(object):

    def __init__(self, path):

        command = "rm -rf %s" % path
        os.system(command)

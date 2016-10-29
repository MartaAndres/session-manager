# -*- coding: utf-8 -*-

from programs import abstract, utils
import sys

class ManualProgram(abstract.AbstractProgram):
    def names():
        return ()

    def save(directory, info):
        print('SAVING: '+info['title']+' ('+info['wid']+')')
        print('A dedicated class for the window could not be found.')
        print('Please enter shell commands to run when recovering program.')
        print(' (Press Ctrl+D to finish)')
        open(directory+'restore.sh','w').write(sys.stdin.read())

    def restore(directory):
        utils.launch('bash '+directory+'restore.sh')

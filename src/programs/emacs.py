# -*- coding: utf-8 -*-

from programs import abstract, utils

class EmacsProgram(abstract.AbstractProgram):
    def names():
        return ('emacs.Emacs',)

    def save(directory, info):
        keys = (('Ctrl','g'), ('meta','colon',), '(desktop-save "'+directory+'" t)', ('Return',))
        utils.window_input(info['wid'],keys)

    def restore(directory):
        utils.launch('emacs --eval=\'(desktop-read "' + directory + '")\'')

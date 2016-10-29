# -*- coding: utf-8 -*-

from programs import abstract, utils

class NautilusProgram(abstract.AbstractProgram):
    def names():
        return ('nautilus.Nautilus',)

    def save(directory, info):
        keys = (('Ctrl','l'),)
        utils.window_input(info['wid'],keys)
        open(directory+'path.txt','w').write(utils.command('xclip -o'))
        keys = (('Escape',),)
        utils.window_input(info['wid'],keys)

    def restore(directory):
        cmd = ('nautilus --new-window ' + open(directory+'path.txt').read())
        utils.launch(cmd)

# -*- coding: utf-8 -*-

from . import abstract, utils

class EvinceProgram(abstract.AbstractProgram):
    def names():
        return ('evince.Evince',)

    def save(directory, info):
        cmd = 'ps -h -o cmd -p '+info['pid']
        open(directory+'restore.sh','w').write(utils.command(cmd))

    def restore(directory):
        utils.launch('bash '+directory+'restore.sh')

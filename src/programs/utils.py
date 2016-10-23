# -*- coding: utf-8 -*-

import subprocess

def command(cmd):
    return subprocess.check_output(cmd.split()).decode('utf-8')

def launch(cmd):
    return subprocess.Popen(cmd.split())

def window_input(window, strings):
    # Modify strings with characters like :,-,/
    special = {
        ':':'colon',
        '-':'minus',
        '/':'slash',
        ',':'comma',
        '.':'period',
        '_':'underscore',
        '(':'parenleft',
        ')':'parenright',
        '"':'quotedbl',
        '   ':' space ' # this one is special
    }

    keys = ' '.join(y for x in strings for y in x)
    for k in special:
        keys = keys.replace(k,special[k])

    cmd = 'xdotool key --window ' + window + ' ' + keys
    command(cmd)


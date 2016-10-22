# -*- coding: utf-8 -*-

import subprocess

def command(cmd):
    return subprocess.check_output(cmd.split()).decode('utf-8')

def launch(cmd):
    return subprocess.Popen(cmd.split())

def window_input(window, strings):
    cmd = 'xdotool key --window ' + window + ' ' + ' '.join(y for x in strings for y in x)
    command(cmd)

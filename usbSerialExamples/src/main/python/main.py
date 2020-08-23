import java

persistent_terminal = None

def addTwo(a,b):
	return a+b

def get_ready(t):
    persistent_terminal = t

def loop():
    persistent_terminal.send('1')
    if persistent_terminal.read() == '0':
        return 'gotem'
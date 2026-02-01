"""grienetsiis.wiskunde.polynoom"""


def polynoom(x, *args):
    return sum(arg * x**(len(args)-1 - macht) for macht, arg in enumerate(args))
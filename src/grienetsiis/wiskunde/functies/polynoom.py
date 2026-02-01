"""grienetsiis.wiskunde.polynoom"""


def polynoom(x, *args):
    return sum(arg * x**macht for macht, arg in enumerate(args))
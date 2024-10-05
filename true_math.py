import math
from multiprocessing.forkserver import get_inherited_fds


def divide(first, second):
    if second == 0:
        from math import inf
        print(math.inf)
        return math.inf
    else:
        print(first/second)
        gh = first/second
        return gh
    print(gf)












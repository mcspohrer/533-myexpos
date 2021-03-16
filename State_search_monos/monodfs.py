#!/usr/bin/python3
# Monopoles Solved
# Matthew Spohrer

import sys


def check(rs):
    for i in rs:
        for j in i:
            for k in i:
                if k != j and j+k in i:
                    print("j: ", j, "k: ", k, "i: ", i)
    print("true")


def pretty_print(rs):
    i, stop = 0, len(rs)
    while i < stop:
        print(*rs[i])
        i += 1


def dfs(rs, todo, n, ri):
    if ri == n:
        return 0

    t = todo.pop(0)
    # search the current room to see if the current monopole
    # can be added to it
    can_add, i, t2 = 1, 0, t/2
    while can_add == 1 and i < len(rs[ri]) and rs[ri][i] < t2+1:
        to_check = t - rs[ri][i]
        if to_check in rs[ri] and to_check != rs[ri][i]:
            can_add = 0
        i += 1

    ret = 0
    if can_add == 1:
        rs[ri].append(t)
        if len(todo) == 0:
            return rs

        ret = dfs(rs, todo, n, 0)

        if ret == 0:
            rs[ri].remove(t)

    if ret == 0:
        todo.insert(0, t)
        ret = dfs(rs, todo, n, ri+1)

    return ret


def main():
    m = int(sys.argv[1])
    n = int(sys.argv[2])

    ms = range(1, m + 1)
    rs = [[] for i in range(n)]
    todo = [*ms]

    rs = dfs(rs, todo, n, 0)
    if rs == 0:
        print("unsat")
    else:
        pretty_print(rs)

    check(rs)


if __name__ == '__main__':
    main()

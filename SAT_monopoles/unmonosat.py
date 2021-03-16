#!/usr/bin/python3
# After monosat creates the CNF clauses, minisat either deterimines
# there is no solution, or UNSAT, or minisat determines satisfiability
# and provides a clause configuration which satisfies the CNF clauses
# created in monosat.
# This program interprets the minisat results and kind of pretty
# prints them.

import sys

# monos = number of monopoles, first arg passed by user
monos = int(sys.argv[1])
# rooms = number of rooms, second arg passed by user
rooms = int(sys.argv[2])

soln = []
for line in sys.stdin:
    # reads in from stdin which has been redirected
    # to a file supplied at the command line
    soln.append(line.strip())

if soln[0] == 'SAT':
    # converts the read in string of numbers to a list of ints
    soln_list = list(map(int, soln[1].split()))

    for room in range(0, rooms):
        # goes through each room and prints all of the monopoles
        # in each room, calculating the monopole from the positive
        # clause numbers
        i = room * monos
        while i < ((room + 1) * monos):
            if soln_list[i] > 0:
                print(soln_list[i] - (monos * room), end=' ')
            i += 1
        print()
else:
    print('UNSAT')

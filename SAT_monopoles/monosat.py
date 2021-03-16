#!/usr/bin/python3
# Matthew Spohrer
# Monopoles Solved with via SAT
# Problem: m number of Monopoles need to be put into n number
#          of rooms. No two monopoles can add up to another
#          monopole in the same room. i.e. 1 and 2 can be in
#          the same room but not with 3 because 1 + 2 = 3 (in
#          case you didn't know)
# Problem with the code: there are so many friggin nested loops, I was
# cringing the entire process of writing this code.
# This program converts the monopole constraints to DIMACS CNF format
# to be used by minisat.

import sys

# monos = number of monopoles, first arg passed by user
monos = int(sys.argv[1])
# rooms = number of rooms, second arg passed by user
rooms = int(sys.argv[2])


def one_room(clauses):
    # creates the atoms responsible for ensuring every monopole is in exactly
    # one room. I know, I know. It's pretty dirty, I just ran out of time.
    # clauses is a list of all CNF clauses to be passed to miniSAT
    # monos is the number of monopoles to be processed
    # rooms is an upper bound to the number of rooms to be checked

    for mono in range(1, monos + 1):
        # ensures each monopole is in a room. e.g. For monopole 1 with
        # three rooms it creates the clause:
        # (in room 1 or in room 2 or in room 3)
        clause = []

        for room in range(0, rooms):
            clause.append((room * monos) + mono)

        clauses.append(clause)

    for mono in range(1, monos + 1):
        # for each monopole, this code makes sure the monopole is only in
        # one room. e.g. If 3 rooms, for monopole 1, it will create the
        # clauses: (not room=1 or not room=2) and (not room=1 or not room=3)
        # and (not room =2 or not room=3)
        for room1 in range(0, rooms):
            # room1 is the first monopole-room state pair being added to the
            # list of clauses
            current_room = room1 * monos + mono
            for room2 in range(room1 + 1, rooms):
                # room2 is the 2nd monopole-room state pair being added to the
                # list of clauses
                other_room = (room2 * monos + mono)
                clauses.append([-current_room, -other_room])


def monopole(clauses):
    # divides the monopoles so no two monopoles can be added
    # together to equal a third in the same room
    # clauses is a list of all clauses to be passed to miniSAT
    # monos is the number of monopoles to be processed
    # rooms is an upper bound to the number of rooms to be checked

    monos_stop = monos // 2
    if monos % 2 == 1:
        monos_stop += 1

    for m in range(1, monos_stop):
        # for all trios of monopoles in all room, this creates a clause
        # preventing all three from being in the same room.
        # e.g For monopoles 3,4,7, the clause (not 3 or not 4 or not 7)
        # will be created, preventing all three from being in the same room.
        for r in range(0, rooms):
            i_start = (monos * r) + m + 1
            i_stop = (monos * r) + monos - m + 1
            for i in range(i_start, i_stop):
                clauses.append([-(i_start - 1), -i, -(m + i)])




def main():
    clauses = []
    num_atoms = monos * rooms

    one_room(clauses)
    monopole(clauses)

    print("p cnf", num_atoms, len(clauses))
    for c in clauses:
        print(*c, '0')


if __name__ == '__main__':
    main()

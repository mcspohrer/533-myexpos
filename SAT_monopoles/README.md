# Monopoles using a SAT solver
Matthew Spohrer

> I know you said a plain-text is fine but the homework description
> says to do it in markdown and I didn't know if there was just one 
> person grading.

## Monopole via SAT: My endless repetition of nested for loops in Python

The following steps should be taken to get the full functionality of my 
programs. All of these are assuming they are being ran on a PSU Linux machine:

1. Run monosat by entering 
"./monosat <# of monopoles> <# of rooms> > <filename>".
This will redirect stdout to the file to be used by minisat.

2. Run minisat with the file from step 1: 
"minisat <file from step 1> <file to write results to>"

3. Unmonosat those results by entering 
"./unmonosat <# of monopoles> <# of rooms> <<file written to in step 2>".
Note the '<' redirecting stdin to the file written to in step 2.

### ~~What the code actually does.~~ What the code hopefully does

#### monosat:
monosat takes the number of monopoles and number of rooms to fit them in as 
arguments. It takes those arguments and forms a series of clauses in DIMAC's 
CNF format. These clause represents a description of the final state. For 
example, let's consider 3 monopoles with 3 rooms available. Monopoles 
1,2, and 3: cannot be in the same room so monosat creates the clauses
in the following fashion:

A bit of explanation is needed. 3 monopoles, 1,2,3, and three rooms, 1,2,3, means 
for monopole/room relations to be represented as a single integer.

- monopole 1 will be 1 in room 1, 4 in room 2, and 7 in room 3; 
- monopole 2 will be 2 in room 1, 5 in room 2, and 8 in room 3; 
- monopole 1 will be 3 in room 1, 6 in room 2, and 9 in room 3; 

1. monosat first creates the clauses indicating each monopole has to be in a
room. 
    - (1 or 4 or 7) and (2 or 5 or 8) and (3 or 6 or 9)

2. monosat then goes through each possible monopole/room relation and prevents
a monopole from being in more than one room by or'ing the negation of each
possible monopole/room relation. 
    - (-1 or -4) and (-1 or -7) and (-4 or -7),
    - (-2 or -5) and (-2 or -8) and (-5 or -8),
    - (-3 or -6) and (-3 or -9) and (-6 or -9),
    
3. monosat then iterates through all of the combinations of illegal placements
of monopoles and creates clauses for them.
    - (-1 or -2 or -3) and (-4 or -5 or -6) and (-7 or -8 or -9)

4. Finally we're done with the meat and potatoes of my stupid monosat. From here,
monosat just prints the results in DIMAC's format and exits.

#### minisat
Not my code but I'm assuming it magically finds a solution, if there is one,
to the clauses monosat produced.

#### unmonosat
unmonosat take the results from minisat and prints them in a user-friendly way
by doing the following:

1. Assuming the user is smarter than I and knows how to redirect stdin from 
the command line, unmonosat reads in from the results of the minisat run.

2. If the problem is unsatisfiable, it prints UNSAT; otherwise it goes through
each room, finds all of the not negated atoms and prints out the corresponding
monopole. For example, with 3 monopoles in 3 rooms, using the clauses created
from monosat, a possible solution could be: only monopole 3 is in room 1 
while room 2 has monopoles 1 and 2 and none are in room 3. This result will look
resemble the following:

> SAT
>
> -1 -2 3 4 5 -6 -7 -8 -9

unmonosat will print 
> 3
>
> 1 2
>
>

## The laughable development Process

Basically, once I wrapped my head around what exactly I needed monosat to do,
writing the program was super simple. Although, I originally forgot to account 
for not allowing them to be in only one room and took a few hours trying to 
debug the "illegal placement" clauses which were fine. I'm kind of an idiot that 
way. unmonosat was even easier, I spent more time on this lengthy README then I
did working on unmonosat.

## How it went

The hardest part of this assignment was my own stupidity, trying to debug a 
functional function. It was really cool thinking of familiar problem in a CNF 
format.

## Left to do

For the assignment, I think I did everything. Maybe for my sanity I could stand 
to clean up the code a bit.
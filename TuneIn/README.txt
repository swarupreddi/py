The solution, "gol.py", is a Python script written in Python 2.7.12.
To run the script:
    > python gol.py

The game of life "glider" is a cyclic configuration, repeating every 4 ticks.
The script calculates 16 ticks of the game of life world, outputting it every 4 ticks.
So, the output is the same configuration moving to the south-west.

To see every world in the sequence, change line 81
from
    if i%4 == 0:
to
    if True:

To see a different configuration in the sequence repeated, 
replace the '0' in that line with 1, 2, or 3.


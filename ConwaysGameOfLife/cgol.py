"""              Conway's Game of Life
The classic cellular automata simulation. Press Ctlr+C to stop.
"""

import copy,random,sys,time

# Set up the constants :
WIDTH = 79  # The width of the cell grid.
HEIGHT = 20 # The height of the cell grid.
ALIVE = 'O' # The character representing a living cell.
DEAD  = ' ' # The character representing a dead cell.
# The cells and nextCells variable are dictionaries for the state of the game.
# Their keys are (x,y) tuples of the cell coordinates and their values are one 
# of the ALIVE or DEAD values.
nextCells = {}

# Put random living and dead cells into nextCells to start:
for x in range(WIDTH): # Loop over every possible column.
    for y in range(HEIGHT): # Loop over every possible row.
        # 50/50 chance of a starting cell being alive or dead.
        if random.randint(0,1) == 0: 
            nextCells[(x,y)] = ALIVE # Add a living cell
        else:
            nextCells[(x,y)] = DEAD # Add a dead cell

while True: # Main Program loop
    # Each iteration of this loop is a step of the simulation
    print('\n'*50) # 'Clear' the screen by printing a bunch of newlines.

    # The cells of the next step should become the cells of this current step.
    cells = copy.deepcopy(nextCells)

    # Print the cells on the screen 
    for y in range(HEIGHT): # Loop over each row
        for x in range(WIDTH): # Loop over each column
            # Do not print a new line, so set end='':
            print(cells[(x,y)],end='') # Print the O or space for living/dead cell
        print() # Print a new line at the end of each row
    print('Press Ctrl-C to quit.')

    # Calculate the next step's cells based on the current step's cells:
    for x in range(WIDTH):
        for y in range(HEIGHT):
            # Get the neignboring coordinates of (x,y), even if they wrap around the edge of the grid.
            left  = (x - 1) % WIDTH 
            right = (x + 1) % WIDTH
            above = (y - 1) % HEIGHT
            below = (y + 1) % HEIGHT

            # Count the number of living neighbors:
            numNeighbors = 0
            if cells[(left,above)] == ALIVE:
                numNeighbors += 1 # Top-left neighbor is alive
            if cells[(x,above)] == ALIVE:
                numNeighbors += 1 # Top neighbor is alive
            if cells[(right,above)] == ALIVE:
                numNeighbors += 1 # Top-right neighbor is alive
            if cells[(left,y)] == ALIVE:
                numNeighbors += 1 # Left neighbor is alive
            if cells[(right,y)] == ALIVE:
                numNeighbors += 1 # Right neighbor is alive
            if cells[(left,below)] == ALIVE:
                numNeighbors += 1 # Bottom-left neighbor is alive
            if cells[(x,below)] == ALIVE:
                numNeighbors += 1 # Bottom neighbor is alive
            if cells[(right,below)] == ALIVE:
                numNeighbors += 1 # Bottom-right neighbor is alive
            
            # Set cells based on Conway's Game of Life rules:
            if cells[(x,y)] == ALIVE and (numNeighbors == 2 or numNeighbors == 3):
                # Living cells with 2 or 3 neighbors stay alive:
                nextCells[(x,y)] = ALIVE
            elif cells[(x,y)] == ALIVE and numNeighbors == 3:
                # Dead cells with 3 neighbors become alive:
                nextCells[(x,y)] = ALIVE
            else:
                # Everything else dies or stays dead:
                nextCells[(x,y)] = DEAD
    
    try:
        time.sleep(1) # Add a 1 second pause to reduce flickering
    except KeyboardInterrupt:
        print('Conway\'s Game of Life')
        sys.exit() # When Ctrl-C is pressed, close the program.

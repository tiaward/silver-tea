# Function to define minesweeper counter as grid
def minesweeper_counter(grid):
    for row_index, row in enumerate(grid): # Looping through each row
        for col_index, col in enumerate(row): # Subsequently looping through each column 
            if col == "-":
                counter = 0   # Dashes counter set to zero for future count

                # If north is #, plus one to counter where dash was 
                if row_index > 0 and grid[row_index - 1][col_index] == "#":
                    counter += 1

                # North east
                if row_index > 0 and col_index < len(row) - 1 and grid[row_index - 1][col_index + 1] == "#":
                    counter += 1

                # East
                if col_index < len(row) - 1 and grid[row_index][col_index + 1] == "#":
                    counter += 1

                # South east
                if row_index < len(grid) - 1 and col_index < len(row) - 1 and grid[row_index + 1][col_index + 1] == "#":
                    counter += 1

                # South
                if row_index < len(grid) - 1 and grid[row_index + 1][col_index] == "#":
                    counter += 1

                # South west
                if row_index < len(grid) - 1 and col_index > 0 and grid[row_index + 1][col_index - 1] == "#":
                    counter += 1

                # West
                if col_index > 0 and grid[row_index][col_index - 1] == "#":
                    counter += 1

                # North west
                if row_index > 0 and col_index > 0 and grid[row_index - 1][col_index - 1] == "#":
                    counter += 1

                grid[row_index][col_index] = str(counter)  # Converting to string for print

    for row in grid:  # Printing the new format from function
        print(row)

# The input of mines and spaces in "minesweeper_counter"
minesweeper_counter([
    ["-", "-", "-", "#"],
    ["-", "#", "#", "-"],
    ["#", "-", "-", "-"],
    ["-", "#", "-", "#"]
])




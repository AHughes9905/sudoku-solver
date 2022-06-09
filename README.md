# sudoku-solver

This is a sudoku solver that uses a backtracking algorithm.

It finds the first blank space then tries a number 1 through 9. If a number works, it goes to the next blank space and repeats.
If no number fits in a blank space, it goes back to the last blank and changes what number it contained. It goes through
this process until there is no blank space or the puzzle is unsolvable.
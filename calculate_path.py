# Calculate the shortest route to move a chess piece from one position to another

import os
import sys

class CalculatePath():
    """ Calculates shortest path to destination on a Chess Board """
    def __init__(self):
        # The chess board, mapped to a 2D List
        self.grid = [[ 0, 1, 2, 3, 4, 5, 6, 7 ],
                     [ 8, 9,10,11,12,13,14,15 ],
                     [16,17,18,19,20,21,22,23 ],
                     [24,25,26,27,28,29,30,31 ],
                     [32,33,34,35,36,37,38,39 ],
                     [40,41,42,43,44,45,46,47 ],
                     [48,49,50,51,52,53,54,55 ],
                     [56,57,58,59,60,61,62,63 ]]
                     
       # How the knight moves on the Board
       self.knight_moves = {"up2-left1": [-2, -1], "up2-right1": [-2, 1],
                            "down2-left1": [2, -1], "down2-right1": [2, 1],
                            "left2-up1": [-1, -2], "left2-down1": [1, -2],
                            "right2-up1": [-1, 2], "right2-down1": [1, 2]}
                            
                            
   def _explore_current_level(starting_point, possible_moves)
       """ Discover possible moves from current location that respect board boundaries

       Input:
           starting_point - The current location on the board
           possible_moves - Piece movement capability, i.e. self.knight_moves
           self.grid - The 2D list representing the board
       Output:
           available_moves - A list of moves possible from the current location
       """
       available_moves = []

       # Find the coordinates of the starting point in the chess grid
       grid_row, grid_column = _find_index(starting_point, self.grid)

       for move in possible_moves:
           try:
               if grid_row + possible_moves[move][0] < 0:
                   # Do not allow negative indices
                   continue
               elif grid_column + possible_moves[move][1] < 0
                   # Do not allow negative indices
                   continue
               possible = self.grid[grid_row + possible_moves[move][0]][grid_column + possible_moves[move][1]]
               available_moves.append(possible)
           except:
               # Move not possible!
               pass

        return available_moves


    def _find_index(board_position):
        """ This function locates the position of a number on the chess grid

        Input:
            board_position - An integer representing a position on board (0-63)
            self.grid - The 2D list representing the board
        Output:
            row, column - The row and column in the 2D list that matches the position
                          number on the board
        """
        for row_iteration in self.grid:
            try:
                column = row_iteration.index(board_position)
                row = self.grid.index(row_iteration)
                return row, column
            except:
                # Didn't find it in this row, continue
                pass


    def breadth_first(start, target, possible_moves):
        """ Performs breadth first search.

        An expedient way to find the shortest route, is to explore all possible routes
        from our current "depth" and check for the target destination in this list. This
        is performed many times until the destination is discovered.

        Input:
            start - The starting point given for the chess piece
            target - The destination given for the chess piece
            self.grid - The 2D list representing the board
            possible_moves - The list of moves possible for a the current chess piece
        Output:
            list_of_paths - A list containing many paths, one of which is the shortest
        """
        list_of_paths = []
        count = 1
        depth = 0
        queue = []
        destinations = explore_current_level(start, possible_moves)

        for dest in destinations:
            list_of_paths.append([dest])
        queue = list_of_paths
        break_flag = False

        for path in list_of_paths:
            queue = list_of_paths
            for value in queue:
                if target in value:
                    break_flag = True
                    break
                destinations = explore_current_level(value[-1], possible_moves)
                for dest in destinations:
                    list_of_paths.append(value + [dest])
            if break_flag == True:
                break
        return list_of_paths

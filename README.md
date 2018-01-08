# ChessPathing
Practice code that uses breadth-first searching on a Chess board to discover the available paths from a starting point to a destination.

To execute code, clone code to a directory and then run the following command in that directory:
```python
python ./
```

The higher level portion of the code is contained in `__main__.py`

Currently only supports Knight movement; can be expanded to support the other pieces by adding in their movement patterns. For now, the Knight's movement pattern can be found in the class variable `self.knight` inside `chess_path.py`.

Output you should see if you were to enter `Knight`, `15`, `15`:
```python
The shortest routes are:
[15, 21, 15]
[15, 5, 15]
[15, 30, 15]
```python

Where the numbers in this list correspond to the numbers on the chess board grid:
```python
self.grid = [[ 0, 1, 2, 3, 4, 5, 6, 7 ],
             [ 8, 9,10,11,12,13,14,15 ],
             [16,17,18,19,20,21,22,23 ],
             [24,25,26,27,28,29,30,31 ],
             [32,33,34,35,36,37,38,39 ],
             [40,41,42,43,44,45,46,47 ],
             [48,49,50,51,52,53,54,55 ],
             [56,57,58,59,60,61,62,63 ]]
```

As you can see, at first glance it may seem odd to only view 3 paths for the Knight. However, his movements are being restricted by the boundary of the board. By using a list of lists, we can use the fact that trying to move outside this matrix will cause an error to detected when an illegal move is attempted. This way, we don't display bogus paths.

The Knight's movement follows an L shaped pattern, and by using the grid above we can set the Knight's movements like this:
```python
# How the knight moves on the Board
self.knight = {"up2-left1": [-2, -1], "up2-right1": [-2, 1],
               "down2-left1": [2, -1], "down2-right1": [2, 1],
               "left2-up1": [-1, -2], "left2-down1": [1, -2],
               "right2-up1": [-1, 2], "right2-down1": [1, 2]}
```

For example, `up2` means to move up two spaces in the 2D grid, for example from `38` to `22`. The `left1` however means to move left one space on the grid, from `14` to `13` for example.

import os
import sys

import chess_path

explored_paths = []
discovered_paths = []
path_lengths = []
cleaned_paths = []

piece = raw_input("Enter the name of the piece.\nCurrent options: [Knight]\n>")
start = int(raw_input("Enter a starting point for the piece.\n>"))
dest = int(raw_input("Enter a destination for the piece.\n>"))

pathObject = chess_path.CalculatePath() 
explored_paths = pathObject.breadth_first(piece.lower(), start, dest)

for path in explored_paths:
	if dest in path:
		path.insert(0, start)
		discovered_paths.append(path)

if not discovered_paths:
	print("[Error]: No paths were discovered.")
	sys.exit(1)

print("The shortest routes are:")
for path in discovered_paths:
	print(path)

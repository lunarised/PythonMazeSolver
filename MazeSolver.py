import MazeLoader, MazeAlgorithms
print ('<')
m = MazeLoader.Maze("smallMaze.png")

print(m)

MazeAlgorithms.DepthFirstSolve(m.image)
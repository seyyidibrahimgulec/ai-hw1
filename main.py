import sys

from modules.best_first_search import bfs
from modules.astar import astar


if __name__ == "__main__":
    choice = input(
        'Please enter "b" for best first search, "a" for a star without quotes: '
    )
    if choice == "b":
        bfs()
    elif choice == "a":
        astar()
    else:
        sys.exit('Please type one of "b" or "b".')

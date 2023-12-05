import json
import window
import sys


if __name__ == "__main__":
    file_name = sys.argv[1]
    f = open(file_name)
    board_data = json.load(f)
    f.close()
    x = window.Board(board_data)
    x.run()

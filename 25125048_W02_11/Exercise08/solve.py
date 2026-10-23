import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_PATH = os.path.join(SCRIPT_DIR, "input.txt")

if os.path.exists(INPUT_PATH):
    sys.stdin = open(INPUT_PATH, "r")
input = sys.stdin.readline


def solve():
    s = input().strip()
    if not s:
        return
    
    moves = {
        'L': (-1, 0),
        'R': (1, 0),
        'U': (0, 1),
        'D': (0, -1)
    }
    
    curr = (0, 0)
    path = [curr]
    coord_to_step = {curr: 0}
    
    for step_idx, move in enumerate(s, start=1):
        dx, dy = moves[move]
        curr = (curr[0] + dx, curr[1] + dy)
        
        # If revisited an existing point, shortest path is violated
        if curr in coord_to_step:
            print("BUG")
            return
        
        coord_to_step[curr] = step_idx
        path.append(curr)
        
    # Check if any two non-consecutive visited cells are adjacent
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for idx, (x, y) in enumerate(path):
        for dx, dy in directions:
            neighbor = (x + dx, y + dy)
            if neighbor in coord_to_step:
                neighbor_idx = coord_to_step[neighbor]
                if abs(neighbor_idx - idx) > 1:
                    print("BUG")
                    return
                    
    print("OK")


def main():
    solve()


if __name__ == "__main__":
    main()

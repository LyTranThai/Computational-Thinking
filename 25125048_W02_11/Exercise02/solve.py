import sys
import os
from collections import defaultdict

# Setup local input reading if input.txt is present
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_PATH = os.path.join(SCRIPT_DIR, "input.txt")

if os.path.exists(INPUT_PATH):
    sys.stdin = open(INPUT_PATH, "r")
input = sys.stdin.readline


def solve():
    line = input().strip()
    if not line:
        return
    n = int(line)
    
    rounds = []
    final_scores = defaultdict(int)
    
    for _ in range(n):
        parts = input().split()
        name = parts[0]
        points = int(parts[1])
        rounds.append((name, points))
        final_scores[name] += points
        
    max_score = max(final_scores.values())
    candidates = {name for name, score in final_scores.items() if score == max_score}
    
    curr_scores = defaultdict(int)
    for name, points in rounds:
        curr_scores[name] += points
        if name in candidates and curr_scores[name] >= max_score:
            print(name)
            return


def main():
    solve()


if __name__ == "__main__":
    main()

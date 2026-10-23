import sys
import os
import math

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_PATH = os.path.join(SCRIPT_DIR, "input.txt")

if os.path.exists(INPUT_PATH):
    sys.stdin = open(INPUT_PATH, "r")
input = sys.stdin.readline


def solve():
    line1 = input().split()
    if not line1:
        return
    n, vb, vs = int(line1[0]), float(line1[1]), float(line1[2])
    
    x = list(map(int, input().split()))
    xu, yu = map(int, input().split())
    
    best_stop = 2
    min_time = float("inf")
    min_dist = float("inf")
    
    # The student cannot get off at stop 1 (index 0)
    for i in range(1, n):
        xi = x[i]
        t_bus = xi / vb
        dist = math.hypot(xi - xu, yu)
        t_run = dist / vs
        total_time = t_bus + t_run
        
        if total_time < min_time - 1e-9:
            min_time = total_time
            min_dist = dist
            best_stop = i + 1
        elif abs(total_time - min_time) <= 1e-9:
            if dist < min_dist:
                min_dist = dist
                best_stop = i + 1
                
    print(best_stop)


def main():
    solve()


if __name__ == "__main__":
    main()

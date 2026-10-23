import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_PATH = os.path.join(SCRIPT_DIR, "input.txt")

if os.path.exists(INPUT_PATH):
    sys.stdin = open(INPUT_PATH, "r")


def solve():
    tokens = sys.stdin.read().split()
    if not tokens:
        return
    n = int(tokens[0])
    k = int(tokens[1])
    groups = [int(x) for x in tokens[2:2 + n]]
    
    center = (k + 1) // 2
    taken = [[False] * (k + 1) for _ in range(k + 1)]
    
    for m in groups:
        best_cost = float("inf")
        best_r = -1
        best_l = -1
        best_right = -1
        
        for r in range(1, k + 1):
            dr = abs(r - center)
            for l in range(1, k - m + 2):
                right = l + m - 1
                
                # Check consecutive seat availability
                free = True
                for c in range(l, right + 1):
                    if taken[r][c]:
                        free = False
                        break
                        
                if free:
                    cost = 0
                    for c in range(l, right + 1):
                        cost += dr + abs(c - center)
                    if cost < best_cost:
                        best_cost = cost
                        best_r = r
                        best_l = l
                        best_right = right
                        
        if best_r != -1:
            for c in range(best_l, best_right + 1):
                taken[best_r][c] = True
            print(f"{best_r} {best_l} {best_right}")
        else:
            print(-1)


def main():
    solve()


if __name__ == "__main__":
    main()

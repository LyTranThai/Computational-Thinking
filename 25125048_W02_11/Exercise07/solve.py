import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_PATH = os.path.join(SCRIPT_DIR, "input.txt")

if os.path.exists(INPUT_PATH):
    sys.stdin = open(INPUT_PATH, "r")
input = sys.stdin.readline


def solve():
    line = input().strip()
    if not line:
        return
    t, m = map(int, line.split())
    
    mem = [0] * m
    next_id = 1
    
    for _ in range(t):
        cmd_parts = input().split()
        if not cmd_parts:
            continue
        op = cmd_parts[0]
        
        if op == "alloc":
            n = int(cmd_parts[1])
            found_idx = -1
            consecutive = 0
            for i in range(m):
                if mem[i] == 0:
                    consecutive += 1
                    if consecutive == n:
                        found_idx = i - n + 1
                        break
                else:
                    consecutive = 0
            
            if found_idx != -1:
                allocated_id = next_id
                next_id += 1
                for i in range(found_idx, found_idx + n):
                    mem[i] = allocated_id
                print(allocated_id)
            else:
                print("NULL")
                
        elif op == "erase":
            x = int(cmd_parts[1])
            if x <= 0 or x not in mem:
                print("ILLEGAL_ERASE_ARGUMENT")
            else:
                for i in range(m):
                    if mem[i] == x:
                        mem[i] = 0
                        
        elif op == "defragment":
            non_zeros = [val for val in mem if val != 0]
            mem = non_zeros + [0] * (m - len(non_zeros))


def main():
    solve()


if __name__ == "__main__":
    main()

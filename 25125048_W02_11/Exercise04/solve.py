import sys
import os

# Equivalent to std::ios_base::sync_with_stdio(false); cin.tie(nullptr);

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_PATH = os.path.join(SCRIPT_DIR, "input.txt")

if os.path.exists(INPUT_PATH):
    sys.stdin = open(INPUT_PATH, "r")
    # sys.stdout = open("output.txt", "w")
input = sys.stdin.readline

def solve():
    # Regular competitive programming logic
    # while True:
    #     line = input()
    #     if not line:  # Triggers only on EOF
    #         break
        
    #     # Process the line
    #     line = line.strip()
    #     print(line)
    x = int(input())
    if x - 2 > 0 and x % 2 == 0 : 
        print("YES")
    else: 
        print("NO")


def main():
    # print("Hello world")
    solve()
    # If multiple test cases (t = int(input()))
    # t_str = input().strip()
    # if not t_str:
    #     return
    # t = int(t_str)
    # for _ in range(t):
    #     solve()

if __name__ == "__main__":
    main()
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
    n = int(input())
    # Correct type annotation
    l: dict[str, list[int, int, int]] = {}
    
    ans = "AAA"
    c = 0
    for i in range(n) :
        name, p = input().split()
        p = int(p)
        if name in l: 
            t = 0
        else: 
            l[name] = [0,0,c]

        l[name][0] += p
        if(l[name][0] >= l[name][1]) :
            l[name][2] = c
            l[name][1] = l[name][0]
        c += 1
        for j in range(3):
            print(name, l[name][j], end = " ")
        print()
    m = -10000000000
    cc = 100000000
    for i in l :
        if(l[i][0] == m) :
            if(l[i][2] < cc) :
                ans = i
                cc = l[i][2]
        elif l[i][0] > m :
            m = l[i][0]
            ans = i
        # print(ans)

    print(ans)

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
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
    p1 = input().strip()
    p2 = input().strip()
    x1 = ord(p1[0]) - ord('a')
    x2 = ord(p2[0]) - ord('a')
    y1 = int(p1[1])
    y2 = int(p2[1])
    dx = abs(x1- x2)
    dy = abs(y1 - y2)
    ans = max(dx, dy)
    P = ""
    D = ""
    print (ans)
    if(x2 >= x1 and y2 >= y1) :
        for i in range(min(dx,dy)) :
            print ("RU")
        d = min(dx, dy)
        while(x1 + d < x2) :
            x1 += 1
            print("R")
        
        while(y1 + d < y2) :
            y1 += 1
            print("U")
        

    if(x2 < x1 and y2 >= y1) :
        for i in range(min(dx,dy)) :
            print ("LU")
        d = min(dx, dy)
        while(x1 - d > x2) :
            x1 -= 1
            print("L")
        
        while(y1 + d < y2) :
            y1 += 1
            print("U")
    
    if(x2 >= x1 and y2 < y1) :
        for i in range(min(dx,dy)) :
            print ("RD")
        d = min(dx, dy)
        while(x1 + d < x2) :
            x1 += 1
            print("R")
        while(y1 - d > y2) :
            y1 -= 1;
            print("D")
    

    if(x2 < x1 and y2 < y1) :
        for i in range(min(dx,dy)) :
            print ("LD")
        d = min(dx, dy)
        while(x1 - d > x2) :
            x1 -= 1;
            print("L")
        
        while(y1 - d > y2) :
            y1 -= 1;
            print("D")


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
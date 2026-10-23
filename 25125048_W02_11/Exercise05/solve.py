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
    x = 0
    ans = 0

    while True:
        s = input().strip()
        if s == "":  # readline() returns an empty string at EOF
            break
        if s[0] == '+' :
            x += 1
            continue
        elif s[0] == '-':
            x -= 1
            continue
        else: 
            i = 0
            while(i < len(s) and s[i] != ':') :
                i += 1
            ans += x * (len(s) - 1 - i)
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
import sys
import os
import string

# Equivalent to std::ios_base::sync_with_stdio(false); cin.tie(nullptr);

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_PATH = os.path.join(SCRIPT_DIR, "input.txt")

if os.path.exists(INPUT_PATH):
    sys.stdin = open(INPUT_PATH, "r")
    # sys.stdout = open("output.txt", "w")
input = sys.stdin.readline
dp = [[0 for _ in range(100)] for _ in range(100)]
def solve():
    n, m, c = input().split()
    n = int(n)
    m = int(m)
    c = int(ord(c[0]) - ord('\0'))

    for i in range(n):
        s = input().strip()
        for j in range(m):
            dp[i][j] = int(ord(s[j]) - ord('\0'))
            

    # while ei + 1 < n and dp[ei + 1][ej] == c :
    #     ei += 1
    # while ej + 1 < m and dp[ei][ej + 1] == c :
    #     ej += 1
    ans = set()
    dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for i in range(n):
        for j in range(m):
            if(dp[i][j] == c):
                
                for di, dj in dir:
                    ni, nj = i + di, j + dj
                    if(0 <= ni < n) and (0 <= nj < m):
                        cur = dp[ni][nj]
                        if cur != c and cur != 46:
                            ans.add(cur)
    print(len(ans))


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
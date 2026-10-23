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
# dp = [[0 for _ in range(100)] for _ in range(100)]
dp = [0 for _ in range(101)]
id = [0 for _ in range(101)]
l = [0 for _ in range(101)]
mem = [[0 for _ in range(2)] for _ in range(100)]
def solve():
    t, m = input().split()
    t = int(t)
    m = int(m)
    c = 0
    cur = 0
    for g in range(t):
        data = input().split()
        if len(data) == 1:
            for i in range(c):
                if l[i] == 0:
                    continue
                id[i] = cur
                for j in range(l[i]):
                    dp[cur] = 1
                    cur += 1
        elif data[0] == "alloc":
            length = int(data[1])
            for i in range(m):
                if dp[i] == 0:
                    save = i
                    run = i
                    count = 0
                    while dp[run] == 0:
                        count += 1
                        if(count == length):
                            # success
                            for k in range(count):
                                dp[save + k] = 1
                            id[c]=save
                            l[c] = length
                            c += 1
                            print(c+1)
                            break
            print("NULL")
        else:
            pos = int(data[1])
            if(pos >= c or l[pos] == 0):
                print("ILLEGAL_ERASE_ARGUMENT")
                continue
            for i in range(l[pos]):
                dp[id[pos] + i] = 0
            l[pos] = 0

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
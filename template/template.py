import sys

def solve(file_name):
    ans = 0
    with open(file_name, "r") as f:
        for line in f:
            l = line.split()
            
    return ans

if __name__ == "__main__":
    file_name = str(sys.argv[1])
    ans = solve(file_name)
    print(f"Answer: {ans} ")



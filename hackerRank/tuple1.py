def solve(n):
    return hash(n)
if __name__ == '__main__':
    n = int(input())
    integer_list = tuple(map(int, input().split()))
    print(solve(integer_list))
    
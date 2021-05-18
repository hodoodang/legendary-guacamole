# -*- coding: utf-8 -*-
"""N과 M (1)

자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

- 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열

첫째 줄에 자연수 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)

한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다.
중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.

수열은 사전 순으로 증가하는 순서로 출력해야 한다.

Example:
    def solution():
        result = do_something()
        return result

    if __name__ == '__main__':

        solution()

"""
from itertools import permutations


def solution(n: int, m: int):
    for t in permutations([i for i in range(1, n+1)], m):
        print(*t)


def short_code():
    """숏 코드
    """
    N, M = map(int, input().split())
    for p in permutations(range(1, N + 1), M): print(*p)


if __name__ == '__main__':
    n, m = map(int, input().split())
    solution(n, m)

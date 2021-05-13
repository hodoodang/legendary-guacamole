# -*- coding: utf-8 -*-
"""통계학

수를 처리하는 것은 통계학에서 상당히 중요한 일이다.
통계학에서 N개의 수를 대표하는 기본 통계값에는 다음과 같은 것들이 있다. 단, N은 홀수라고 가정하자.

1. 산술평균 : N개의 수들의 합을 N으로 나눈 값
2. 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
3. 최빈값 : N개의 수들 중 가장 많이 나타나는 값
4. 범위 : N개의 수들 중 최댓값과 최솟값의 차이

N개의 수가 주어졌을 때, 네 가지 기본 통계값을 구하는 프로그램을 작성하시오.

첫째 줄에 수의 개수 N(1 ≤ N ≤ 500,000)이 주어진다. 단, N은 홀수이다.
그 다음 N개의 줄에는 정수들이 주어진다. 입력되는 정수의 절댓값은 4,000을 넘지 않는다.

첫째 줄에는 산술평균을 출력한다. 소수점 이하 첫째 자리에서 반올림한 값을 출력한다.
둘째 줄에는 중앙값을 출력한다.
셋째 줄에는 최빈값을 출력한다. 여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력한다.
넷째 줄에는 범위를 출력한다.

Example:
    def solution():
        result = do_something()
        return result

    if __name__ == '__main__':

        solution()

"""
import sys
from collections import Counter


def solution():
    n = int(sys.stdin.readline())

    numbers = [int(sys.stdin.readline()) for i in range(n)]
    numbers.sort()
    count = Counter(numbers)
    avg = round(sum(numbers) / n)
    print(avg)
    print(numbers[n//2])
    if n > 1:
        most = count.most_common(2)
        if most[0][1] == most[1][1]:
            print(most[1][0])
        else:
            print(most[0][0])
    else:
        print(numbers[0])
    print(numbers[-1] - numbers[0])


def short_code():
    """숏 코드
    """
    n, *m = map(int, open(0))
    m.sort()
    q = Counter(m).most_common(2) * 2
    print(*(round(sum(m) / n), m[n // 2], q[q[0][1] == q[1][1]][0], m[-1] - m[0]))


if __name__ == '__main__':
    solution()
    # short_code()

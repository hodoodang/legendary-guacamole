# -*- coding: utf-8 -*-
"""나이순 정렬

온라인 저지에 가입한 사람들의 나이와 이름이 가입한 순서대로 주어진다.
이때, 회원들을 나이가 증가하는 순으로, 나이가 같으면 먼저 가입한 사람이 앞에 오는 순서로 정렬하는 프로그램을 작성하시오.

첫째 줄에 온라인 저지 회원의 수 N이 주어진다. (1 ≤ N ≤ 100,000)

둘째 줄부터 N개의 줄에는 각 회원의 나이와 이름이 공백으로 구분되어 주어진다.
나이는 1보다 크거나 같으며, 200보다 작거나 같은 정수이고,
이름은 알파벳 대소문자로 이루어져 있고,
길이가 100보다 작거나 같은 문자열이다. 입력은 가입한 순서로 주어진다.

첫째 줄부터 총 N개의 줄에 걸쳐 온라인 저지 회원을 나이 순,
나이가 같으면 가입한 순으로 한 줄에 한 명씩 나이와 이름을 공백으로 구분해 출력한다.

Example:
    def solution():
        result = do_something()
        return result

    if __name__ == '__main__':

        solution()

"""


def solution(members: list):
    members.sort(key=lambda x: (int(x[1][0]), x[0]))
    return members


def short_code():
    """숏 코드
    """
    print(*sorted([*open(0)][1:],key=lambda a:int(a.split()[0])),sep='')


if __name__ == '__main__':
    for j, m in solution([(i, input().split()) for i in range(int(input()))]):
        print(*m)

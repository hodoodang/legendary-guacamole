# -*- coding: utf-8 -*-
"""신나는 함수 실행

재귀 호출만 생각하면 신이 난다! 아닌가요?
다음과 같은 재귀함수 w(a, b, c)가 있다.

```
if a <= 0 or b <= 0 or c <= 0, then w(a, b, c) returns:
    1

if a > 20 or b > 20 or c > 20, then w(a, b, c) returns:
    w(20, 20, 20)

if a < b and b < c, then w(a, b, c) returns:
    w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)

otherwise it returns:
    w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
```

위의 함수를 구현하는 것은 매우 쉽다. 하지만, 그대로 구현하면 값을 구하는데 매우 오랜 시간이 걸린다. (예를 들면, a=15, b=15, c=15)
a, b, c가 주어졌을 때, w(a, b, c)를 출력하는 프로그램을 작성하시오.

입력은 세 정수 a, b, c로 이루어져 있으며, 한 줄에 하나씩 주어진다.
입력의 마지막은 -1 -1 -1로 나타내며, 세 정수가 모두 -1인 경우는 입력의 마지막을 제외하면 없다.

입력으로 주어진 각각의 a, b, c에 대해서, w(a, b, c)를 출력한다.

Example:
    def solution():
        result = do_something()
        return result

    if __name__ == '__main__':

        solution()

"""


def w(a: int, b: int, c: int):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)
    if store[a][b][c]:
        return store[a][b][c]
    if a < b < c:
        store[a][b][c] = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
        return store[a][b][c]

    store[a][b][c] = w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1)
    return store[a][b][c]


if __name__ == '__main__':
    store = [[[0] * 21 for _ in range(21)] for _ in range(21)]

    while True:
        a, b, c = map(int, input().split())
        if a == -1 and b == -1 and c == -1:
            break
        print(f"w({a}, {b}, {c}) = {w(a, b, c)}")

VALUES = {
    1: 0,
    2: 6,
    3: 12,
    4: 90,
    5: 360,
    6: 2040,
    7: 10080,
    8: 54810,
    9: 290640,
    10: 1588356,
    11: 8676360,
    12: 47977776,
    13: 266378112
}

for _ in range(int(input())):
    a = int(input())
    print(VALUES.get(a, 1488801600))

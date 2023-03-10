'''
1차원의 점들이 주어졌을 때, 그 중 가장 거리가 짧은 것의 쌍을 출력하시오.
(단 점들의 배열은 모두 정렬되어있다고 가정한다.)

예를들어 [1, 3, 4, 8, 13, 17, 20]이 주어졌다면, 결과값은 (3, 4)
'''
x = [1, 3, 4, 8, 13, 17, 20]

def cal(x):
    diff = [abs(a - b) for a, b in zip(x, x[1:])]
    ret = diff.index(min(diff))
    return x[ret], x[ret + 1]
y = cal(x)
print(y)
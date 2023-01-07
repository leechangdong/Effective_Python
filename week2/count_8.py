'''
1 부터 10000까지 8이라는 숫자가 총 몇번 나오는지 구하시오

ex) 8808은 3, 8888은 4로 카운팅
'''
counts = 0

x = (i for i in range(1,10001))

for i in range(10000):    # enumerate(x)
    count = str(next(x)).count('8')
    counts += count

print(counts)

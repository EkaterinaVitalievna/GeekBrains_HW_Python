# 30). Вычислить число π c заданной точностью d
# Пример:
# при d = 0.001,π = 3.141 10^(-1)≤d≤10^(-10)

from math import pi


def precision_pi(prn):
    prsn = len(str(prn))
    return float(str(pi)[:prsn])


d = 0.001

print(pi)
print('Точность: ', d)
print('Число pi заданной точности: ', precision_pi(d))
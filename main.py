import numpy as np
import scipy.integrate
import math
import BuildPlot
import MidSquare

#1 вариант
#WolframAlpha: интеграл на отрезке = 1.19862
checkValue = 1.19862
segment = [1.4,5.0]
def f(x):
    a  = (1.0+x)*(1.0+x)
    b = math.pow(x,3)*math.sqrt(2.0+x)
    return a/b


step = 0.01
t = MidSquare.calculateIntegral(f,segment,step)
print("Отрезок: ",segment," Шаг: ",step)
print("WolframAlpha: ",checkValue)
print("Метод средних прямоугольников: ",t)
print("разница: ",checkValue - t)

print("----------------------------------")
step = 0.1
t = MidSquare.calculateIntegral(f,segment,step)
print("Отрезок: ",segment," Шаг: ",step)
print("WolframAlpha: ",checkValue)
print("Метод средних прямоугольников: ",t)
print("разница: ",checkValue - t)

print("----------------------------------")
step = 1
t = MidSquare.calculateIntegral(f,segment,step)
print("Отрезок: ",segment," Шаг: ",step)
print("WolframAlpha: ",checkValue)
print("Метод средних прямоугольников: ",t)
print("разница: ",checkValue - t)
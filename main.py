import math
import MidSquare
import NewtonCotes
import Trapezium

# 1 вариант
# WolframAlpha: интеграл на отрезке = 1.19862
checkValueWolframAlpha = 1.19862
segment = [1.4, 5.0]
def f(x):
    a = (1.0 + x) * (1.0 + x)
    b = math.pow(x, 3) * math.sqrt(2.0 + x)
    return a / b


def experiment(func, segment, step, description):
    checkValue = 1.19862
    value = func(f, segment, step)
    print("Отрезок: ", segment, " Шаг: ", step)
    print("WolframAlpha: ", checkValue)
    print(description + ": ", value)
    print("разница: ", checkValue - value)
    print("----------------------------------")


def experimentNC(func, segment, step, k, description):
    checkValue = 1.19862
    value = func(f, segment, step, k)
    print("Отрезок: ", segment, " Шаг: ", step, " K: ", k)
    print("WolframAlpha: ", checkValue)
    print(description + ": ", value)
    print("разница: ", checkValue - value)
    print("----------------------------------")


experiment(MidSquare.calculateIntegral, segment, 0.01, "Метод средних прямоугольников")
experiment(MidSquare.calculateIntegral, segment, 0.1, "Метод средних прямоугольников")
experiment(MidSquare.calculateIntegral, segment, 1, "Метод средних прямоугольников")

experiment(Trapezium.calculateIntegral, segment, 0.01, "Метод Трапеций")
experiment(Trapezium.calculateIntegral, segment, 0.1, "Метод Трапеций")
experiment(Trapezium.calculateIntegral, segment, 1, "Метод Трапеций")

experimentNC(NewtonCotes.calculateIntegral, segment, 0.01, 3, "Метод Ньютона-Котеса")
experimentNC(NewtonCotes.calculateIntegral, segment, 0.1, 3, "Метод Ньютона-Котеса")
experimentNC(NewtonCotes.calculateIntegral, segment, 1, 3, "Метод Ньютона-Котеса")

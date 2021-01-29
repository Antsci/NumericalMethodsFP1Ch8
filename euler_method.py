from math import *
def euler_ode(derivative: str, x: float, y: float, iter_num: int, end_point: float)  -> float:
    iter_num = int(iter_num)
    h = (end_point-x)/iter_num
    derivative = derivative.replace('^','**')
    derivative = derivative.replace('ln(','log(')
    for n in range(iter_num):
        print(f"(x_{n},y_{n}) = {x,y}")
        num_der = eval(derivative)
        print(f"derivative = {num_der}")
        print(f"y_{n+1} = y_{n} + (h * derivative) = {y + (h*num_der)}")
        y += (h*num_der)
        x += h
    print(f"f({x}) = {y}")
der = input("derivative: str ")
args = [float(item) for item in input("x: float, y: float, iter_num: int, end_point: float ").split()] 
euler_ode(der, *args)
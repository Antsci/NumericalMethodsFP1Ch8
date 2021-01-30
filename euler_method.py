from math import *
def euler_ode_method(derivative: str, x: float, y: float, iter_num: int, end_point: float)  -> float:
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


def midpoint_method(derivative: str, x: float, y: float, step_length: float, end_point: float)  -> float:
    derivative = derivative.replace('^','**')
    derivative = derivative.replace('ln(','log(')
    n = 0
    print(f"(x_{n},y_{n}) = {x,y}")
    num_der = eval(derivative)
    print(f"derivative = {num_der}")
    print(f"y_{n+1} = y_{n} + (h * derivative) = {y + (step_length*num_der)}")
    y_prev = y
    y += (step_length*num_der)
    x += step_length
    for n in range(int((end_point-x)/step_length)):
        print(f"(x_{n},y_{n}) = {x,y}")
        num_der = eval(derivative)
        print(f"derivative = {num_der}")
        print(f"y_{n+1} = y_{n-1} + (2*h * derivative) = {y + (2*step_length*num_der)}")
        hold = y
        y = y_prev + (2*step_length*num_der)
        y_prev = hold
        x += step_length
    print(f"f({x}) = {y}")

der = input("derivative: str ")
args = [float(item) for item in input("x: float, y: float, iter_num/step_length: int/float, end_point: float ").split()] 
midpoint_method(der, *args)
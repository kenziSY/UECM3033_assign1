import sympy as sy
import numpy as np

def fun_1( your_id ):
    ans = hex(your_id)
    return ans

def my_integral():
    x = sy.Symbol('x')
    ans = ans = sy.integrate( sy.ln(sy.sqrt(x/(x-2))), (x,0,1))
    return ans

def my_solution():
    A = np.array( [[-1,9,8,8,0,9,1,3,2,-6],
                   [0,-1,2,4,2,7,7,5,-6,1], 
                   [2,0,-1,2,0,5,0,-2,2,6],
                   [0,1,7,-5,1,6,-9,5,3,1],
                   [9,9,8,6,-7,-8,0,8,6,5],
                   [0,1,2,4,-3,-3,5,9,8,3],
                   [5,3,0,-3,1,8,-5,2,1,5],
                   [0,1,-3,1,7,6,9,-4,4,8],
                   [9,-3,0,2,0,5,5,4,-6,5],
                   [-6,3,0,1,1,4,5,0,8,-4]] )
    b = np.array([66,42,28,20,72,52,34,58,42,24])
    x = np.linalg.solve(A,b) # Solve Ax = b
    return x


if __name__ == '__main__':
    your_id = 1308097
    print('Hexadecimal representation of %d is %s'%( your_id, fun_1( your_id) ))
    print('Integral = ', my_integral())
    print('Solution = ', my_solution())

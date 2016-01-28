import sympy as sy
import numpy as np

def fun_1( your_id ):
    ans = hex(your_id)
    return ans

def my_integral():
    x = sy.Symbol('x')
    ans = sy.integrate( sy.exp(-x)*sy.sin(2*x), (x, 0, sy.pi))
    return ans

def my_solution():
    A = np.array( [ [1,9,9,9,9,9,9,9,9,9],[1,1,8,8,8,8,8,8,8,8],
                    [1,1,1,7,7,7,7,7,7,7],[1,1,1,1,6,6,6,6,6,6],
                    [1,1,1,1,1,5,5,5,5,5],[1,1,1,1,1,1,4,4,4,4],
                    [1,1,1,1,1,1,1,3,3,3],[1,1,1,1,1,1,1,1,2,2],
                    [1,1,1,1,1,1,1,1,1,2],[1,1,1,1,1,1,1,1,1,1] ] )
    
    b = np.array([194,192,210,126,150,144,120,80,72,66])
    x = np.linalg.solve(A,b) # Solve Ax = b
    return x


if __name__ == '__main__':
    your_id = 1308250
    print('Hexadecimal representation of %d is %s'%( your_id, fun_1( your_id) ))
    print('Integral = ', my_integral())
    print('Solution = ', my_solution())

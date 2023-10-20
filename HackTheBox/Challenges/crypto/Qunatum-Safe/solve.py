import numpy as np
import math
def get_constants():
    f = open("/home/abdelilah/Downloads/CTFs/HackTheBox/crypto/Quantum Safe/crypto_quantum_safe/enc.txt","r")
    constants = (f.read()).split("\n")
    sets = []
    for constant in constants:
        values = constant[1:-1].split(',')
        numbers = [int(value) for value in values]
        number_set = tuple(numbers)
        sets.append(number_set)
    return sets
def solve_linear_system(const):
    pubkey = [[47, -49, 57],[-77, 78, -78],[-85, 50, 99]]
    coefficients = np.array(pubkey)
    # Define the constants on the right-hand side of the equations
    constants = np.array(list(const))
    # Solve the system of equations
    solution = np.linalg.solve(coefficients, constants)
    return solution
r = 12
constants = get_constants()
flag = ""
for const in constants:
    sol = solve_linear_system(const=const)
    flag+=chr(math.floor(sol[0])+12)
print(flag)

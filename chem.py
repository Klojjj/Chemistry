def calculate_entropy(a_r, b_r, c_r, t_1, t_2, n):
    from math import log
    entropy = 0
    for i in range(n):
        print('Please, enter initial entropy #', i, ' :', sep='')
        entropy_initial = float(input().replace(',', '.'))
        entropy += entropy_initial
    entropy_delta = a_r * log(t_2 / t_1) + b_r * (t_2 - t_1) + c_r / 2 * (t_2 ** -2 - t_1 ** -2)
    entropy += entropy_delta
    return entropy


def calculate_enthalpy(a_r, b_r, c_r, t_1, t_2, n):
    enthalpy = 0
    for i in range(n):
        print('Please, enter initial enthalpy #', i, ' :', sep='')
        enthalpy_initial = float(input().replace(',', '.'))
        enthalpy += enthalpy_initial
    enthalpy_delta = (a_r * (t_2 - t_1) + b_r / 2 * (t_2 ** 2 - t_1 ** 2) + c_r * (1 / t_2 - 1 / t_1)) / 10 ** 3
    enthalpy += enthalpy_delta
    return enthalpy


def calculate_gibbs_energy(entropy, enthalpy):
    print('Please, enter current temperature:')
    t_current = int(input().replace(',', '.'))
    gibbs_energy = enthalpy - t_current * entropy / 10 ** 3
    gibbs_energy = gibbs_energy * 10 ** 4 // 10 / 10 ** 3
    return gibbs_energy


def calculate_capacity(n):
    a_r, b_r, c_r = 0, 0, 0
    for i in range(n):
        print('Please, enter "a #', i, '" :', sep='')
        a = float(input().replace(',', '.'))
        print('Please, enter "b #', i, '" :', sep='')
        b = float(input().replace(',', '.')) / 10 ** 3
        print('Please, enter "c #', i, '" :', sep='')
        c = float(input().replace(',', '.')) * 10 ** 5
        a_r += a
        b_r += b
        c_r += c
    return a_r, b_r, c_r

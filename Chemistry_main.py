import chem

print('This program will help you to solve simple tasks with thermodynamics')
print('Please, enter initial and final temperatures:')
t_1 = int(input())
t_2 = int(input())
print('Please, enter number of reaction components:')
n = int(input())
print('PLEASE, ENTER REACTANT AMOUNT OF SUBSTANCE WITH OPPOSITE SIGN!!!')
a_r, b_r, c_r, k = chem.calculate_capacity(n)
print('Choose one option:')
print('1 - calculate entropy', '2 - calculate enthalpy', "3 - calculate Gibb's energy", '4 - all', sep='\n')
flag = int(input())
if flag in (1, 3, 4):
    entropy = chem.calculate_entropy(a_r, b_r, c_r, t_1, t_2, n, k)
    if flag in (1, 4):
        print("Entropy = ", entropy * 10 ** 4 // 10 / 10 ** 3, "J")
if flag in (2, 3, 4):
    enthalpy = chem.calculate_enthalpy(a_r, b_r, c_r, t_1, t_2, n, k)
    if flag in (2, 4):
        print("Enthalpy = ", enthalpy * 10 ** 4 // 10 / 10 ** 3, "kJ")
if flag in (3, 4):
    gibbs_energy = chem.calculate_gibbs_energy(entropy, enthalpy, t_2)
    print("Gibb's energy = ", gibbs_energy, "kJ")
else:
    print('ERROR: WRONG INPUT')

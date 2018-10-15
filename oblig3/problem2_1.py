import numpy as np

T = 300 #K
k = 8.617*1e-5 #eV/K
kT = k*T#eV

print("---------------------------------------------------")
epsilon = np.array([-0.1, -0.05, 0, 0.05, 0.1]) # eV
print()
print("For the energies:")
print(epsilon, "in eV")
print("we get the following results:")

Z = 0
for i in epsilon:
    Z += np.exp(-i/kT)

print("The partition fuction four our system is:", Z)

sum_prob = 0
for i in epsilon:
    prob = np.exp(-i/kT)/Z
    print("Probability of measuring energy = ", i, "is ", prob)
    sum_prob += prob

print("the sum of Probabilities: ", sum_prob)
print("")
print("")

print("---------------------------------------------------")
epsilon = np.array([-0.1, -0.05, 0, 0.05, 0.1])+0.1 # eV
print()
print("For the energies:")
print(epsilon, "in eV")
print("we get the following results")

Z = 0
for i in epsilon:
    Z += np.exp(-i/kT)

print("The partition fuction four our system is:", Z)

sum_prob = 0
for i in epsilon:
    prob = np.exp(-i/kT)/Z
    print("Probability of measuring energy = ", i, "is ", prob)
    sum_prob += prob

print("the sum of Probabilities: ", sum_prob)

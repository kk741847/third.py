R = 0.08206
P = float(input("P in atm : "))
V = float(input("V in litre : "))
T = float(input("T in kelvin : "))
n = (P*V)/(R*T)
print("No. of moles in gas : ",n)

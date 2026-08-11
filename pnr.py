principal = input("Enter Your Principle Amount :")
rate = input("Enter Your Rate of Interest :")
time = input("Enter Your Time in Years :")

principal = float(principal)
rate = float(rate)
time = float(time)

interest = (principal * rate * time)

print("Simple Interest is :", interest)
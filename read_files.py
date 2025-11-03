

filo = open("filo_pilo", "r")
for employee in filo.readlines():
    print(employee)

filo.close()
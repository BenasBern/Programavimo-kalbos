# Funkcija sudeda
def sudetis(x, y):
    return x + y

# Funkcija atima
def atimtis(x, y):
    return x - y

# Funkcija padaugina
def daugyba(x, y):
    return x * y

# Funkcija padalina
def dalyba(x, y):
    return x / y

print("Pasirinkimai: ")
print("Sudetis: ")
print("Atimtis: ")
print("Daugyba: ")
print("Dalyba: ")

while True:
    # Irasas is vartotojo
    pasirinkimas = input("Pasirinkimas (1/2/3/4): ")

    # Patikrinimas ar tai yra vienas is pasirinkimu
    if pasirinkimas in ('1', '2', '3', '4'):
        try:
            pirmas = int(intput("Pirmas numeris:"))
            antras = int(intput("Antras numeris:"))
        except ValueError:
            print("Netinkamas. Prasom irasyti numeri")
            continue


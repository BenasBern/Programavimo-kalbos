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
    if (y==0):
        return
    else:
        return x / y

print("Pasirinkimai: ")
print("Sudetis: ")
print("Atimtis: ")
print("Daugyba: ")
print("Dalyba: ")

while True:
    # Irasas is vartotojo
    pasirinkimas = input("Pasirinkimas (1/2/3/4): ")

    # Patikrinimas, ar tai yra vienas is pasirinkimu
    if pasirinkimas in ('1', '2', '3', '4'):
        try:
            pirmas = float(intput("Pirmas numeris:"))
            antras = float(intput("Antras numeris:"))
        except ValueError:
            print("Netinkamas. Prasom irasyti numeri")
            continue

        if pasirinkimas == '1':
            print(pirmas, "+", antras, "=", sudetis(pirmas, antras))
        elif pasirinkimas == '2':
            print(pirmas, "-", antras, "=", atimtis(pirmas, antras))
        elif pasirinkimas == '3':
            print(pirmas, "*", antras, "=", daugyba(pirmas, antras))
        elif pasirinkimas == '4':
            print(pirmas, "/", antras, "=", dalyba(pirmas, antras))

        # Paklausti ar vartotojas nori kito veiksmo
        # Sustabdyti programa, jei atsakymas - ne
        kitasskaiciavimas = input("Ar atlikti kita skaiciavima? (taip/ne): ")
        if kitasskaiciavimas == "ne":
          break
    else:
        print("Netinkama ivestis")

from flask import Flask, request
app = Flask(__name__)


skaicius = 0 #apsirasom kintamaji (Globalus)

@app.route("/") # Route 1
def hello_world():

    return f"<h1>Hello, World! </h1> {skaicius}"


@app.route("/labas") # Route 2
def sakyk_labas():
    global skaicius #Naudoju globalu kintamaji
    skaicius = skaicius +1 #kaskart atidare pridedam 1
    return f"Labas {skaicius}"

@app.route("/skaicius") #Route 3
def skaiciavimo():
    #Uzklausa. Argumentai. Metodas() 
    skaicius = request.args.get("test") #Pasiimam argumenta is URL pvz.: /skaicius?test=100

    return f"Tavo ivestas skaicius: {skaicius}"




if __name__ == "__main__":
    app.run()










# 1. Susiediegiame Flask
    # pip3 install Flask

# 2. Importuojame











'''
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
            pirmas = float(input("Pirmas numeris: "))
            antras = float(input("Antras numeris: "))
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
        '''
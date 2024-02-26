from flask import Flask, request
import string
app = Flask(__name__)


skaicius = 0 #apsirasom kintamaji (Globalus)
zenklas = '+'

def sudetis(x,y):
        return x+y

@app.route("/") # Route 1
def hello_world():

    return f"""
                <form action="/skaicius">
                    <label for="test">Skaičius 1</label><br>
                        <input type="text" id="test" name="test" value=""><br>
                        </br></br>

                    <label for="test2">Skaičius 2</label><br>
                        <input type="text" id="test2" name="test2" value=""><br>
                        </br></br>
                        
                    <label for="zenklas">Ženklas</label><br>   
                        <input type="text" id="zenklas" name="zenklas" value=""><br>
                        </br></br>

                    <input type="submit" value="Pateikti">
                </form> 
            """


'''@app.route("/labas") # Route 2
def sakyk_labas():
    global skaicius #Naudoju globalu kintamaji
    skaicius = skaicius +1 #kaskart atidare pridedam 1
    return f"Labas {skaicius}"'''

@app.route("/skaicius") # Route 3
def skaiciavimo():
    #UZKLAUSA. ARGUMENTAI. METODAS()
    skaicius = request.args.get("test") ### Pasiimam argumenta is URL pvz.: /skaicius?test=100
    skaicius2 = request.args.get("test2") ### Pasiimam argumenta 2 is URL pvz.: /skaicius?test2=100
    #zenklas = request.args.get("zenklas") ### Pasiimam zenkla is URL

    suma = sudetis(int(skaicius2),int(skaicius),string(zenklas))

    return f"Tavo įvestas skaičius: {suma}"


if __name__ == "__main__":
    app.run()

# 1. Susiediegiame Flask
    # pip3 install Flask

# 2. Importuojame

'''<form>
  <label for="test">Pirmas skaičius:</label><br>
  <input type="text" id="test" name="fname"><br>
  <label for="test2">Antras skaičius:</label><br>
  <input type="text" id="test2" name="lname">
</form>'''


'''# Funkcija sudeda
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
        print("Netinkama ivestis")'''

from flask import Flask, request

app = Flask(__name__)

operations_history = []

def sudetis(x, y):
    return x + y

def atimtis(x, y):
    return x - y

def daugyba(x, y):
    return x * y

def dalyba(x, y):
    if (y==0):
        return
    else:
        return x / y

@app.route("/")  # Route 1
def hello_world(latest_result=None):
    history_html = "<ul>"
    for operation in operations_history:
        history_html += f"<li>{operation}</li>"
    history_html += "</ul>"

    # Rodyti paskutine operacija, jei ji egzistuoja
    latest_result_html = f"{latest_result}" if latest_result else ""

    return f"""
                <form action="/skaicius">
                    <label for="test">Skaičius 1</label><br>
                        <input type="text" id="test" name="test" value=""><br>
                        </br></br>

                    <label for="test2">Skaičius 2</label><br>
                        <input type="text" id="test2" name="test2" value=""><br>
                        </br></br>
                        
                    <label for="zenklas">Ženklas (+, -, *, /)</label><br>   
                        <input type="text" id="zenklas" name="zenklas" value=""><br>
                        </br></br>

                    <input type="submit" value="Pateikti">
                </form>
                <h2>Rezultatas</h2>
                {latest_result_html}
                <h2>Praeitos operacijos</h2>
                {history_html}
            """

@app.route("/skaicius")  # Route 2
def skaiciavimo():
    if not request.args.get("test") or not request.args.get("test2"):
        return "Nera argumento"
    skaicius1 = request.args.get("test", type=int)  # Gauti ir pakeisti i int
    skaicius2 = request.args.get("test2", type=int)  # Gauti ir pakeisti i int
    zenklas = request.args.get("zenklas")  # Gauti simboli

    # Atlikti operacija, pagal tan tikra simboli
    if zenklas == '+':
        rezultatas = sudetis(skaicius1, skaicius2)
    elif zenklas == '-':
        rezultatas = atimtis(skaicius1, skaicius2)
    elif zenklas == '*':
        rezultatas = daugyba(skaicius1, skaicius2)
    elif zenklas == '/':
        rezultatas = dalyba(skaicius1, skaicius2)
    else:
        rezultatas = "Nepalaikomas veiksmas"
    #return hello_world(f"Atliktos operacijos rezultatas: {rezultatas}")
        
    # Isaugo operacijas i atminti, kad galetu jas pateikti
    operations_history.append(f"{skaicius1} {zenklas} {skaicius2} = {rezultatas}")
    
    # Iskviesti hello_world, kad rodyti paskutini veiksma pati pirma
    return hello_world(latest_result=f"{rezultatas}")

if __name__ == "__main__":
    app.run(debug=True)

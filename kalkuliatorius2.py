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
def hello_world():
 
    history_html = "<ul>"
    for operation in operations_history:
        history_html += f"<li>{operation}</li>"
    history_html += "</ul>"

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
                <h2>Praeitos operacijos</h2>
                {history_html}
            """

@app.route("/skaicius")  # Route 2
def skaiciavimo():
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
    f"Atliktos operacijos rezultatas: {rezultatas}"
        
    # Isaugo operacijas i atminti, kad galetu jas pateikti
    operations_history.append(f"{skaicius1} {zenklas} {skaicius2} = {rezultatas}")
    
    #return hello_world()  # Perkelti atgal i pagrindini puslapi, kad rodytu rezultata ir senus veiksmus

if __name__ == "__main__":
    app.run(debug=True)

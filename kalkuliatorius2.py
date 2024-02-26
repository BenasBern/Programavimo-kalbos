from flask import Flask, request

app = Flask(__name__)

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
            """

@app.route("/skaicius")  # Route 3
def skaiciavimo():
    skaicius1 = request.args.get("test", type=int)  # Retrieve and convert to integer
    skaicius2 = request.args.get("test2", type=int)  # Retrieve and convert to integer
    zenklas = request.args.get("zenklas")  # Retrieve the symbol

    # Perform operation based on the symbol
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
    return f"Atliktos operacijos rezultatas: {rezultatas}"

if __name__ == "__main__":
    app.run(debug=True)

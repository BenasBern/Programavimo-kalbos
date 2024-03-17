from flask import Flask, jsonify, request, render_template

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
    history_html = ""
    for operation in operations_history:
        history_html += f"{operation}"
    history_html += ""

    # Rodyti paskutine operacija, jei ji egzistuoja
    latest_result = f"{latest_result}" if latest_result else ""

    return render_template('index.html', latest_result = latest_result, history_html = operations_history)

@app.route("/skaicius")  # Route 2
def skaiciavimo():
    if request.method == "DELETE":
        # Process the DELETE request to clear a specific operation
        data = request.json
        operation_id = int(data.get('id')) - 1  # Adjusting because list indexes start at 0
        if 0 <= operation_id < len(operations_history):
            operations_history.pop(operation_id)
            return jsonify({"success": True, "message": "Operation cleared."}), 200
        else:
            return jsonify({"success": False, "message": "Invalid operation ID."}), 400

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
        
    # Isaugo operacijas i atminti, kad galetu jas pateikti
    operations_history.append(f"{skaicius1} {zenklas} {skaicius2} = {rezultatas}")
    
    # Iskviesti hello_world, kad rodyti paskutini veiksma pati pirma
    return hello_world(latest_result=f"{rezultatas}")

if __name__ == "__main__":
    app.run(debug=True)

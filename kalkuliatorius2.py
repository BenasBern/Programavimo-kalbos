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
        return "Negalimas veiksmas"
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

@app.route("/skaicius", methods=["GET", "POST", "DELETE"])
def handle_operation():
    if request.method == "DELETE":
        data = request.get_json()
        operation_id = int(data.get('id', 0)) - 1  # Adjusting for 0-based indexing
        if 0 <= operation_id < len(operations_history):
            del operations_history[operation_id]
            return jsonify({"success": True}), 200
        else:
            return jsonify({"success": False, "message": "Invalid operation ID."}), 400

    # Handling for POST request
    if request.method == "POST":
        data = request.form  # Accessing form data for POST requests
        skaicius1 = data.get("test", type=int)
        skaicius2 = data.get("test2", type=int)
    else:
        # Fallback for GET request, keeping the original mechanism
        skaicius1 = request.args.get("test", type=int)
        skaicius2 = request.args.get("test2", type=int)
    
    zenklas = request.values.get("zenklas")  # This works for both GET and POST

    if skaicius1 is None or skaicius2 is None or zenklas is None:
        return "Nėra argumento"

    # Check if the operation is division by zero
    if zenklas == '/' and skaicius2 == 0:
        # Return "Negalimas veiksmas" without adding to history
        return hello_world(latest_result="Negalimas veiksmas")

    # Continue with other operations
    if zenklas == '+':
        rezultatas = sudetis(skaicius1, skaicius2)
    elif zenklas == '-':
        rezultatas = atimtis(skaicius1, skaicius2)
    elif zenklas == '*':
        rezultatas = daugyba(skaicius1, skaicius2)
    elif zenklas == '/':
        rezultatas = dalyba(skaicius1, skaicius2)
    else:
        rezultatas = "Negalimas veiksmas"

    # Add operation to history only if valid
    operations_history.append(f"{skaicius1} {zenklas} {skaicius2} = {rezultatas}")

    # Show the result
    return hello_world(latest_result=f"{rezultatas}")

@app.route('/modify_answer', methods=['POST'])
def modify_answer():
    data = request.json
    original_answer = float(data.get('original_answer', 0))
    modification = data.get('modification', '')
    
    # Assuming a simple operation format like "+10"
    try:
        operation, value = modification[0], float(modification[1:])
        if operation == '+':
            modified_answer = original_answer + value
        elif operation == '-':
            modified_answer = original_answer - value
        elif operation == '*':
            modified_answer = original_answer * value
        elif operation == '/':
            if value == 0:
                return jsonify({'error': 'Division by zero'}), 400
            modified_answer = original_answer / value
        else:
            return jsonify({'error': 'Invalid operation'}), 400

        return jsonify(modified_answer=modified_answer)
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)
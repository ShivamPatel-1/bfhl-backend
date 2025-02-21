from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/bfhl', methods=['POST'])
def process_data():
    try:
        data = request.get_json()
        if not data or "data" not in data:
            return jsonify({"is_success": False, "message": "Invalid input"}), 400
        
        input_data = data["data"]
        numbers = [x for x in input_data if x.isdigit()]
        alphabets = [x for x in input_data if x.isalpha()]
        highest_alphabet = [max(alphabets, key=lambda x: x.upper())] if alphabets else []

        response = {
            "is_success": True,
            "user_id": "shivampatel_26042003",  # Replace with your name and DOB
            "email": "shivampatel.260403@gmail.com",
            "roll_number": "22BAI71388",
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_alphabet": highest_alphabet
        }
        return jsonify(response)

    except Exception as e:
        return jsonify({"is_success": False, "message": str(e)}), 500


@app.route('/bfhl', methods=['GET'])
def get_operation_code():
    return jsonify({"operation_code": 1})

if __name__ == '__main__':
    app.run(debug=True)

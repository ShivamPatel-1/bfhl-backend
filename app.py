from flask import Flask, request, jsonify

app = Flask(__name__)

# POST /bfhl - Process Data
@app.route('/bfhl', methods=['POST'])
def process_data():
    try:
        # Get JSON data from request
        data = request.get_json()
        
        # Validate input format
        if not data or "data" not in data:
            return jsonify({"is_success": False, "message": "Invalid input"}), 400
        
        input_data = data["data"]
        
        # Separate numbers and alphabets
        numbers = [x for x in input_data if x.isdigit()]
        alphabets = [x for x in input_data if x.isalpha()]
        
        # Find the highest alphabet (case insensitive)
        highest_alphabet = [max(alphabets, key=lambda x: x.upper())] if alphabets else []

        # Construct the response
        response = {
            "is_success": True,
            "user_id": "shivam_patel_26042003",  # Replace with your full name and date of birth (e.g., john_doe_17091999)
            "email": "shivampatel.260403@gmail.com",  # Replace with your college email
            "roll_number": "22BAI71388",  # Replace with your roll number
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_alphabet": highest_alphabet
        }
        return jsonify(response)

    except Exception as e:
        return jsonify({"is_success": False, "message": str(e)}), 500

# GET /bfhl - Return operation_code
@app.route('/bfhl', methods=['GET'])
def get_operation_code():
    return jsonify({"operation_code": 1})

# Run the application
import os

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))  # Use Render's provided port or default to 10000
    app.run(host='0.0.0.0', port=port)


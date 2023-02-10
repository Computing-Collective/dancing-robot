# Group: 24
# Names: Divy, Elio, Kelvin, Matthew

from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

"""
For individual move selection
    -1:  Return to sequence
    1-6: Specific move
"""
move = -1


@app.route('/move', methods=['GET'], defaults={'path': ''})
def get_move(path):
    """Returns the current move as a string"""
    global move
    return str(move)


@app.route('/move', methods=['POST'], defaults={'path': ''})
def post_move(path):
    """Sets the current move"""
    global move
    if request.is_json:
        content = request.json
        field = content['move']
        print(f"Received: {field}")
        if isinstance(field, int) and field >= 1 and field <= 6:
            move = field
            return f"Move {field} Sent"
        elif field == -1:
            move = field
            return "Returning to sequence"
        else:
            return "Invalid move"
    else:
        return "Not JSON"


if __name__ == '__main__':
    app.run(port=5000, host="192.168.137.1")

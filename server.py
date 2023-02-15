# Group: 24
# Names: Divy, Elio, Kelvin, Matthew

from flask import Flask, request
from flask_cors import CORS

"""
Server that runs on a laptop and controls the robot's movement.
Devices can sent and receive data from the server via connecting
to the server's IP address and port 5000 via the laptop's wifi
hotspot.
"""

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
        if content is not None:
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
            return "Invalid JSON"
    else:
        return "Not JSON"


if __name__ == '__main__':
    app.run(port=5000, host="192.168.137.1")

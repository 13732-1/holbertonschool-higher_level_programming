#!/usr/bin/python3
import json
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/items')
def items():
    try:
        # Open and load the JSON file
        with open('items.json', 'r') as f:
            data = json.load(f)
            # Extract the list associated with the key "items"
            items_list = data.get("items", [])
    except FileNotFoundError:
        # If the file is missing, we pass an empty list
        items_list = []

    return render_template('items.html', items=items_list)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

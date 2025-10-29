import os
import random
from flask import Flask, render_template

app = Flask(__name__)

def get_sides():
    sides = os.getenv("DICE_SIDES", "6")
    try:
        sides_int = int(sides)
        if sides_int < 1:
            raise ValueError
        return sides_int
    except ValueError:
        return 6

@app.route("/")
def index():
    sides = get_sides()
    result = random.randint(1, sides)
    return render_template("index.html", result=result, sides=sides)


@app.route("/health")
def health():
    return {"status": "ok"}


if __name__ == "__main__":
    
    app.run(host="0.0.0.0", port=5000)

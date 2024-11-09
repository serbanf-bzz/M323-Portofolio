from flask import Flask

app = Flask(__name__)


unpure_sum = 0
@app.route("/function/unpure")
def unpure():
    # Diese Funktion verändert den Zustand einer externen Variable und ist somit unpure..
    global unpure_sum
    unpure_sum += 1
    return unpure_sum

@app.route("/function/pure/<number>")
def pure(number):
    addition = int(number) + 1
    return str(addition)

@app.route("/hello")
def print_hello():
    # Dies ist eine Prozedur da nur eine Ausgabe gemacht und nichts zurückgegben wird
    print("Hello, World!")

@app.route("/immutable")
def immutable_example():
    # es ist nicht möglich immutable variables wie tuples anzupassen mit metheoden wie append()
    original_tuple = (1, 2, 3)
    new_tuple = original_tuple + (4,)
    return new_tuple

if __name__ == "__main__":
    app.run()
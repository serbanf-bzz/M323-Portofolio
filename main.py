from flask import Flask
from functools import reduce

app = Flask(__name__)

unpure_sum = 0


@app.route("/A1G/function/unpure")
def unpure():
    # Diese Funktion verändert den Zustand einer externen Variable und ist somit unpure..
    global unpure_sum
    unpure_sum += 1
    return unpure_sum


@app.route("/A1G/function/pure/<number>")
def pure(number):
    addition = int(number) + 1
    return str(addition)


@app.route("/A1G/hello")
def print_hello():
    # Dies ist eine Prozedur da nur eine Ausgabe gemacht und nichts zurückgegben wird
    print("Hello, World!")


@app.route("/A1F/immutable")
def immutable_example():
    # es ist nicht möglich immutable variables wie tuples anzupassen mit metheoden wie append()
    original_tuple = (1, 2, 3)
    new_tuple = original_tuple + (4,)
    return new_tuple


@app.route("/A1F/mutable")
def mutable_example():
    mutable_list = [1, 2, 3]
    mutable_list[0] = 4  # Die Liste wird geändert
    print(mutable_list)
    return


@app.route("/A1E/OOP")
def oop_example():
    class Animal:
        def __init__(self, name):
            self.name = name

        def speak(self):
            pass

    class Dog(Animal):
        def speak(self):
            return "Woof!"


@app.route("/A1E/proc")
def procedural_example():
    def add_numbers(a, b):
        return a + b

    return add_numbers(1, 2)


@app.route("/A1E/func")
def functional_example():
    def factorial(n):
        return 1 if n == 0 else n * factorial(n - 1)

    return factorial(5)


@app.route("/B1G/bubble")
def bubble_example():
    def bubble_sort(arr):
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr

    return bubble_sort([1, 8, 4, 11, 12, 6, 2])


@app.route("/B1F/bubble/divided")
def bubble_divided_example():
    def needs_swap(a, b):
        return a > b

    def swap(arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]

    def bubble_sort(arr):
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                if needs_swap(arr[j], arr[j + 1]):
                    swap(arr, j, j + 1)
        return arr

    return bubble_sort([1, 8, 4, 11, 12, 6, 2])


@app.route("/B1E/factorial")
def factorial_segmented():
    def calculate_product(numbers):
        product = 1
        for number in numbers:
            product *= number
        return product

    def factorial(n):
        if n == 0 or n == 1:
            return 1
        numbers = list(range(1, n + 1))
        return calculate_product(numbers)

    return factorial(5)


@app.route("/B2G/firstclass")
def first_class_functions():
    def double(x):
        return x * 2

    # Funktion wird in Variable gespeichert
    my_function = double

    # Function wird als Parameter an weiter Funktion gegeben
    def apply_function(func, value):
        return func(value)

    result = apply_function(double, 5)

    def multiplier(factor):
        def multiply_by(value):
            # Funktion errinert sich an den Factor Parameter von alleine
            return value * factor

        return multiply_by

    res2 = multiplier(5)
    return my_function(2), result, res2(2)


@app.route("/B2F/func_in_args")
def func_in_args():
    # Function wird als Parameter an weitere Funktion gegeben
    def square(x):
        return x * x

    numbers = [1, 2, 3, 4]
    squared_numbers = map(square, numbers)
    return list(squared_numbers)


@app.route("/B2E/closures")
def closure():
    def make_multiplier(factor):
        def multiplier(number):
            # Diese Funktion nachdem sie selbst zurückgegeben wird erinnert sich an den wert von factor
            return number * factor

        return multiplier

    res = make_multiplier(3)
    return res(4)  # Das wird jetzt 12 geben


@app.route("/B3G/lambda")
def lambda_example():
    square = lambda x: x ** 2
    return square


@app.route("/B3F/lambda_args")
def lambda_args_example():
    average = lambda x, y: (x + y) / 2
    concat = lambda a, b: a + " " + b
    sum_three = lambda x, y, z: x + y + z

    return average(2, 3), concat("Hallo", "Leute"), sum_three(1, 2, 3)


@app.route("/B3E/lambda_flow")
def lambda_flow_example():
    numbers = [5, 1, 9, 3, 7]
    sorted_numbers = sorted(numbers, key=lambda x: -x)
    return sorted_numbers


@app.route("/B4G/map_filter")
def map_filter():
    even_squared = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers)))
    return even_squared


@app.route("/B4F/map_filter_reduce")
def map_filter_reduce():
    numbers = [1, 2, 3, 4, 5, 6]

    even_numbers = filter(lambda x: x % 2 == 0, numbers)
    squared_even_numbers = map(lambda x: x ** 2, even_numbers)
    product = reduce(lambda x, y: x * y, squared_even_numbers)

    return product


@app.route("/B4E/map_filter_reduce_transform")
def map_filter_reduce_transform():
    # Sigma
    products = [
        {'name': 'Produkt A', 'price': 15},
        {'name': 'Produkt B', 'price': 30},
        {'name': 'Produkt C', 'price': 45},
        {'name': 'Produkt D', 'price': 10}
    ]

    total_discounted_price = reduce(
        lambda x, y: x + y,
        map(
            lambda p: p * 0.9,
            map(
                lambda item: item['price'],
                filter(lambda item: item['price'] > 20, products)
            )
        )
    )
    return total_discounted_price


@app.route("/C1G/codestandards")
def code_standard():
    radius = 5
    pi = 3.14159
    area = pi * radius ** 2

    price = 200
    discount_rate = 0.9
    discounted_price = price * discount_rate

    DISCOUNT_THRESHOLD = 100
    DISCOUNT_RATE = 0.9
    price = 120
    final_price = price * DISCOUNT_RATE if price > DISCOUNT_THRESHOLD else price


    points = 60
    status = "Invalid points" if points < 0 else "Gold" if points > 100 else "Silver" if points > 50 else "Bronze"

    prices = [50, 150, 250]
    total = sum(price * 0.9 for price in prices if price > 100)

    return area, discounted_price, final_price, status, total


@app.route("/C1F/codestandards")
def code_standard_used():
    def calculate_discounted_price(price):
        DISCOUNT_THRESHOLD = 100
        DISCOUNT_RATE = 0.9
        return price * DISCOUNT_RATE if price > DISCOUNT_THRESHOLD else price

    def calculate_total_price(o):
        total_price = sum(map(lambda item: calculate_discounted_price(item['price']), o['items']))
        return f"Total: {total_price: .2f}"

    order = {
        'items': [
            {'name': 'Produkt A', 'price': 120},
            {'name': 'Produkt B', 'price': 80},
            {'name': 'Produkt C', 'price': 150},
            {'name': 'Produkt D', 'price': 50}
        ]
    }

    return calculate_total_price(order)


@app.route("/C1E/codestandards2")
def code_standards_sideeffects():
    TAX_RATE = 0.08

    def add_tax(price):
        return price + (price * TAX_RATE)

    def display_total_price(price):
        total_price = add_tax(price)
        return f"Total price with tax: {total_price: .2f}"

    return display_total_price(500)


if __name__ == "__main__":
    app.run()

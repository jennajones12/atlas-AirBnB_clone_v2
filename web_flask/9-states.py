#!/usr/bin/python3
""" Task 10 """

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def root():
    return "Hello HBNB!"


@app.route('/hnbn', strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    return f"C {text.replace('_', '')}"


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text="is cool"):
    return f"Python {text.replace('_', ' ')}"


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n: int):
    value = 'even' if n % 2 == 0 else 'odd'
    return render_template('6-number_odd_or_even.html', n=n, value=value)


@app.route('/states_list', strict_slashes=False)
def states_list():
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda state: state.name)
    return render_template('7-states_list.html', states=sorted_states)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda state: state.name)
    cities = storage.all(City).values()
    sorted_cities = sorted(cities, key=lambda city: city.name)
    return render_template('8-cities_by_states.html',
                           states=sorted_states,
                           cities=sorted_cities)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def state(id=None):
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda state: state.name)
    state_obj = next(iter([s for s in states if s.id == id]), None)
    cities = storage.all(City).values()
    sorted_cities = sorted([c for c in cities if c.state_id == id],
                           key=lambda city: city.name) if id else None

    if not state_obj:
        return render_template(
            '9-states.html',
            states=sorted_states,
            error="Not found!")

    return render_template(
        '9-states.html',
        states=sorted_states,
        cities=sorted_cities,
        state_name=state_obj.name)


@app.teardown_appcontext
def teardown(exc):
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

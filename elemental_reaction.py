from flask import Flask, url_for, redirect, request, render_template
app = Flask(__name__)

@app.route('/')
def lobby():
    return render_template('search.html')

@app.route('/fail/<false_element>')
def fail(false_element):
    return f'Element "{false_element}" does not exist!'

@app.route('/<element>')
def reaction_list(element):
    if element == 'pyro':
        return 'Melt, Vaporize, Overload, Swirl, Crystallize, Burning'
    elif element == 'hydro':
        return 'Vaporize, Frozen, Electro-Charge, Swirl, Crystallize'
    elif element == 'cryo':
        return 'Melt, Frozen, Superconduct, Swirl, Crystallize'
    elif element == 'electro':
        return 'Overload, Electro-Charge, Superconduct, Swirl, Crystallize'
    elif element == 'anemo':
        return 'Swirl'
    elif element == 'geo':
        return 'Crystallize'
    elif element == 'dendro':
        return 'Burning'
    else:
        return redirect(url_for('fail', false_element = element))

@app.route('/search', methods = ['POST', 'GET'])
def search():
    if request.method == 'POST':
        ele_entered = request.form['ele']
        return redirect(url_for('reaction_list', element = ele_entered))
    else:
        ele_entered = request.args.get('ele')
        return redirect(url_for('reaction_list', element = ele_entered))

if __name__ == '__main__':
    app.run(debug = True)

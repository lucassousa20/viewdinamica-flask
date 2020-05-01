from aplicacao import app
from flask import render_template


@app.route('/')
def index():
    context = {'titulo':'Pagina flask',
                'outro': 'Novo tex'}
    retorno = render_template('index.html', **context)
    print('Pagina acessada')
    return retorno


@app.route('/segundapagina')
def segundaindex():
    retorno = render_template('segundaindex.html')
    print('Pagina acessada')
    return retorno
app.run(debug=True)

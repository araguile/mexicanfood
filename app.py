from flask import Flask, render_template, request, url_for, redirect,flash

app = Flask(__name__)

integrantes= [{'nombre':"Julio Santillan",'correo':"jsantillan@orale.com"},              
              {'nombre':"Jorge Freire",'correo':"jfreire@orale.com"},
              {'nombre':"Blanca Hidalgo",'correo':"bhidalgo@orale.com"},
              {'nombre':"Alexandra Morales",'correo':"amorales@orale.com"},
              {'nombre':"Alexander Morales",'correo':"amorales@orale.com"}]
             
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/nuevo')
def formularios():
    return render_template('nuevo.html')

@app.route('/productos')
def tablas():
    return render_template('productos.html')

@app.route('/equipo')
def tarjetas():
    return render_template('equipo.html',data=integrantes)

@app.route('/contactanos')
def contactanos():
    return render_template('contactanos.html')

@app.route('/obtenerDatos', methods=['GET','POST'])
def guardarDatos():
    if request.method == 'POST':  
            name = request.form['nombre'] + " " + request.form['apellido']
            email = request.form['email']
            integrantes.append({'nombre':name,'correo':email})
            msg = 'OK'
            return render_template('nuevo.html', mensaje=msg)
    else:
        return redirect(url_for('nuevo'))

if __name__ =='__main__':
	app.run(debug=True,port=5000)

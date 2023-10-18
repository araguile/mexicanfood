from flask import Flask, render_template, request, url_for, redirect,flash

app = Flask(__name__)

integrantes= [{'nombre':"Julio Santillan",'correo':"jsantillan@example.com"},              
              {'nombre':"Jorge Freire",'correo':"jfreire@example.com"},
              {'nombre':"Blanca Hidalgo",'correo':"bhidalgo@exaple.com"},
              {'nombre':"Alexandra Morales",'correo':"amorales@example.com"},
              {'nombre':"Alexander Morales",'correo':"amorales@example.com"},
              {'nombre':"Alex Aguilera",'correo':"aaguilera@example.com"}]
             
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/formularios')
def formularios():
    return render_template('formularios.html')

@app.route('/tablas')
def tablas():
    return render_template('tablas.html')

@app.route('/tarjetas')
def tarjetas():
    return render_template('tarjetas.html',data=integrantes)

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
            return render_template('formularios.html', error=msg)
    else:
        return redirect(url_for('formularios'))

if __name__ =='__main__':
	app.run(debug=True,port=5000)

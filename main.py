from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('Home.html')

# Ejercicio 1
@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    promedio = None
    estado = None

    nota1 = nota2 = nota3 = asistencia = ''

    if request.method == 'POST':
        nota1 = int(request.form['nota1'])
        nota2 = int(request.form['nota2'])
        nota3 = int(request.form['nota3'])
        asistencia = int(request.form['asistencia'])

        promedio = round((nota1 + nota2 + nota3) / 3, 1)
        estado = "APROBADO" if promedio >= 40 and asistencia >= 75 else "REPROBADO"

    return render_template(
        'Ejercicio1.html',
        promedio=promedio,
        estado=estado,
        nota1=nota1,
        nota2=nota2,
        nota3=nota3,
        asistencia=asistencia
    )

# Ejercicio2
@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    nombre_mayor = None
    longitud = None

    n1 = n2 = n3 = ''

    if request.method == 'POST':
        n1 = request.form['nombre1']
        n2 = request.form['nombre2']
        n3 = request.form['nombre3']

        nombres = [n1, n2, n3]
        nombre_mayor = max(nombres, key=len)
        longitud = len(nombre_mayor)

    return render_template(
        'Ejercicio2.html',
        nombre_mayor=nombre_mayor,
        longitud=longitud,
        nombre1=n1,
        nombre2=n2,
        nombre3=n3
    )

# Ejecución
if __name__ == '__main__':
    app.run(debug=True)

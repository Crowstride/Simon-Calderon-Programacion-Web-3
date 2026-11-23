from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        try:
            nota1 = float(request.form['nota1'])
            nota2 = float(request.form['nota2'])
            nota3 = float(request.form['nota3'])
            asistencia = int(request.form['asistencia'])
            

            if not (10 <= nota1 <= 70 and
                    10 <= nota2 <= 70 and
                    10 <= nota3 <= 70):
                raise ValueError("Las notas deben tener un valor entre 10 y 70. Intente otra vez.")

            if not 0 <= asistencia <= 100:
                raise ValueError("La asistencia debe ser un valor entre 0 y 100.")

            promedio = sum([nota1, nota2, nota3]) / 3
            if promedio >= 40 and asistencia >= 75:
                aprobado = True
            else:
                aprobado = False

            return render_template(
                'ejercicio1.html',
                promedio = round(promedio, 2),
                aprobado = aprobado
            )
        except ValueError as error:
            return render_template('ejercicio1.html', error=str(error))
    return render_template('ejercicio1.html')

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    if request.method == 'POST':
        nombre1 = request.form['nombre1'].strip()
        nombre2 = request.form['nombre2'].strip()
        nombre3 = request.form['nombre3'].strip()
        
        nombres = [nombre1, nombre2, nombre3]

        if any(not nombre for nombre in nombres):
            return render_template(
                'ejercicio2.html',
                error="Se deben ingresar tres nombres."
            )

        if len(set(nombre.lower() for nombre in nombres)) != 3:
            return render_template(
            'ejercicio2.html',
            error="Los tres nombres deben ser diferentes."
            )

        cantidad = max(len(nombre) for nombre in nombres)

        nombres_mayores = [
            nombre for nombre in nombres
            if len(nombre) == cantidad
        ]

        return render_template(
            'ejercicio2.html',
            nombres_mayores=nombres_mayores,
            cantidad=cantidad
        )

    return render_template('ejercicio2.html')

if __name__ == '__main__':
    app.run(debug=True)


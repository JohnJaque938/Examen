from flask import Flask, request, render_template

app = Flask(__name__)
# Configuración de la clave secreta para la aplicación
app.config['SECRET_KEY'] = 'mi_clave_secreta'
# Diccionario de usuarios y contraseñas
users = {
    "juan": "admin",
    "pepe": "user"
}

@app.route('/') # Se establece la ruta para la página de inicio
def inicio():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST']) # Se establece la ruta 'ejercicio1' y permite los métodos GET y POST
def calculocompras():
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        numero = int(request.form['numero'])
        tarros = numero * 9000
        # Se aplica el descuento según la edad
        if edad >= 18 and edad <= 30:
            descuento = tarros * 0.15
        elif edad > 30:
            descuento = tarros * 0.25
        else:
            descuento = 0
        pagar = tarros - descuento
        return render_template('ejercicio1.html', nombre=nombre, edad=edad, numero=numero, tarros=tarros, descuento=descuento, pagar=pagar)
    return render_template('ejercicio1.html')

@app.route('/ejercicio2', methods=['GET', 'POST']) # Se establece la ruta 'ejercicio2' y permite los métodos GET y POST
def sesion():
    if request.method == 'POST':
        usuario = request.form['usuario']
        password = request.form['password']
        if usuario in users and users[usuario] == password:
            # Mensaje de bienvenida específico según el usuario ingresado
            if usuario == "juan":
                mensaje = "Bienvenido Administrador juan"
            else:
                mensaje = "Bienvenido Usuario pepe"
        else:
            mensaje = "Usuario o contraseña incorrectos"
        return render_template('ejercicio2.html', usuario=usuario, password=password, mensaje=mensaje)
    return render_template('ejercicio2.html')

if __name__ == '__main__':
    app.run() # Inicia el servidor web de Flask
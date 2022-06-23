import os
from flask import Flask, jsonify,request
import uuid
import re

app = Flask(__name__)


from conexiondb import ConexionFirebase


conexion_firebase = ConexionFirebase(
    "K:/UP/Cuatrimestre 8/Mantenimiento de software/Corte 2/Proyecto\Backend/backend-bioapp/tokkioedit-firebase-adminsdk-x4apd-2678ed0d77.json",
    "https://tokkioedit-default-rtdb.firebaseio.com/"
)


conexion_firebase.init_firebase()

@app.route("/")
def rutaRaiz():
    return jsonify({
        "status":"raiz"
    })


@app.route("/add-user",methods=["POST"])
def addUser():
    json_response = request.get_json(force=True)
    name = json_response['name']
    password = json_response['password']

    return jsonify({
        "status": "true",
        "key": conexion_firebase.add_user2(name,password)
    })

@app.route("/login")
def login():
    name = request.args['name']
    if validarNombre(name)[1]:
        password = request.args['password']
        data = conexion_firebase.login(name,password)
        status = data["status"]
        id = data["id"]
    else :
        status = False
        id = ''

    return jsonify({
        "status": status,
        "id": id
    })

def validarNombre(name):
    expresion = re.compile(r'^[a-zA-Z][a-zA-Z]*$')
    if expresion.match(name):
        return ['Nombre valido', True]
    return ['Nombre incorrecto', False]

@app.route("/busqueda",methods=["POST"])
def prueba():
    json_response = request.get_json(force=True)
    palabra = json_response["palabra"]
    return jsonify({
        "status": "true",
        "value":conexion_firebase.busqueda(palabra)
    })

@app.route("/add-paciente",methods=["POST"])
def registrarPaciente():
    json_response = request.get_json(force=True)
    
    idp = json_response["id"]
    nombreVeterinario = json_response["nombre-veterinario"]
    nombreMascota = json_response["nombre-mascota"]
    edadMascota = json_response["edad-mascota"]
    pesoMascota = json_response["peso-mascota"]
    razaMascota = json_response["raza-mascota"]
    sexoMascota = json_response["sexo-mascota"]
    razonMascota = json_response["razon-mascota"]
    estadoMascota = json_response["estado-mascota"]
    nombreMueño = json_response["nombre-dueño"]
    numeroContacto = json_response["numero-contacto"]
    direccion = json_response["direccion"]
    key=conexion_firebase.add_pasiente(
        idp,
        nombreVeterinario,
        nombreMascota,
        edadMascota,
        pesoMascota,
        razaMascota,
        sexoMascota,
        razonMascota,
        estadoMascota,
        nombreMueño,
        numeroContacto,
        direccion
        )
    return jsonify({
        "status": "true",
        "key": key
    })
    pass
def iniciarServe():
    app.run(host="0.0.0.0")




if __name__ == "__main__":
    iniciarServe()
import os
from flask import Flask, jsonify,request
from conexiondb import ConexionFirebase
from validacion_datos import Validacion_datos
import uuid

app = Flask(__name__)

validar = Validacion_datos()
conexion_firebase = ConexionFirebase(
    "K:/UP/Cuatrimestre 8/Mantenimiento de software/Corte 2/Proyecto\Backend/backend-bioapp/tokkioedit-firebase-adminsdk-x4apd-2678ed0d77.json",
    "https://tokkioedit-default-rtdb.firebaseio.com/"
)


conexion_firebase.init_firebase()

@app.route("/")
def rutaRaiz():
    return jsonify({
        "status":"En ejecucion"
    })


@app.route("/add-user",methods=["POST"])
def addUser():

    status = False
    datos = ''

    json_response = request.get_json(force=True)
    name = json_response['name']
    password = json_response['password']

    if validar.validar_nombre(name)[1]:
        datos = conexion_firebase.add_user2(name, password)
        status = True

    return jsonify({
        "status": status,
        "key": datos
    })

@app.route("/login")
def login():
    status = False
    id = ''
    name = request.args['name']
    if validar.validar_nombre(name)[1]:
        password = request.args['password']
        data = conexion_firebase.login(name, password)
        status = data["status"]
        id = data["id"]

    return jsonify({
        "status": status,
        "id": id
    })

@app.route("/busqueda", methods=["POST"])
def busqueda():
    status = False
    dato = ''

    json_response = request.get_json(force=True)
    palabra = json_response["palabra"]

    if validar.validar_palabra(palabra):
        status = True
        dato = conexion_firebase.busqueda(palabra)

    return jsonify({
        "status": status,
        "value": dato
    })

@app.route("/add-paciente",methods=["POST"])
def registrarPaciente():
    json_response = request.get_json(force=True)

    status = False
    key = ""
    
    idp = json_response["id"]
    nombreVeterinario = json_response["nombre-veterinario"]
    nombreMascota = json_response["nombre-mascota"]
    edadMascota = json_response["edad-mascota"]
    pesoMascota = json_response["peso-mascota"]
    razaMascota = json_response["raza-mascota"]
    sexoMascota = json_response["sexo-mascota"]
    razonMascota = json_response["razon-mascota"]
    estadoMascota = json_response["estado-mascota"]
    nombreDue??o = json_response["nombre-due??o"]
    numeroContacto = json_response["numero-contacto"]
    direccion = json_response["direccion"]

    statusNV = validar.validar_string_add_paciente(nombreVeterinario)
    statusNM = validar.validar_string_add_paciente(nombreMascota)
    statusND = validar.validar_string_add_paciente(nombreDue??o)

    statusEM = validar.validar_edad_y_numero(edadMascota)
    statusPM = validar.validar_peso(pesoMascota)
    statusNC = validar.validar_edad_y_numero(numeroContacto)

    if (statusNV and statusNM and statusND and statusEM and statusPM and statusNC):
        status = True
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
            nombreDue??o,
            numeroContacto,
            direccion
            )
    return jsonify({
        "status": status,
        "key": key
    })

@app.route("/add-datos-paciente", methods=["POST"])
def datos():
    json_response = request.get_json(force=True)
    datos = list()
    datos.append(json_response['id'])
    datos.append(json_response['ecg']) #ecg = json_response['ecg']
    datos.append(json_response['temperatura']) #temperatura = json_response['temperatura']
    datos.append(json_response['vpm']) #vpm = json_response['vpm']
    datos.append(json_response['saturacionOxigeno']) #saturacionOxigeno = json_response['saturacion-oxigeno']
    datos.append(json_response['pam']) #pam = json_response['pam']
    datos.append(json_response['indice-shock']) #indiceShock = json_response['indice-shock']

    conexion_firebase.add_datos_paciente(datos)

    return jsonify({'status':True})

def iniciarServe():
    app.run(host="0.0.0.0")

if __name__ == "__main__":
    iniciarServe()
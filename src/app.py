from flask import Flask
from decouple import config
from modelo.Medicos import ModeloMedico
from config import config

app = Flask(__name__)

# RUTA PARA PETICION GET

@app.route("/")
def hello_world():
    return  " hola mundo "

#mostrar todos los medicos
@app.route("/medicos", methods=['GET'])
def listar_medicos():
    resul=ModeloMedico.listar_Medico()
    return resul

#buscar solo un medico
@app.route("/medicos/:<codigo>", methods=['GET'])
def lista_medico(codigo):
    resul=ModeloMedico.lista_Medico(codigo)
    return resul

#registrar medico
@app.route("/medicos",methods=['POST'])
def guardar_medico():
    resul=ModeloMedico.registrar_medico()
    return resul


#actualizar medico
@app.route("/medicos/:<codigo>",methods=['PUT'])
def actualizxar_medico(codigo):
    resul=ModeloMedico.actualizar_medico(codigo)
    return resul


#eliminar medico
@app.route("/medicos/:<codigo>",methods=['DELETE'])
def elimineycion_medico(codigo):
    resul=ModeloMedico.eliminar_medico(codigo)
    return resul

def pag_noencontrada(error):
    return "<h1>Página no Encontrada</h1>", 404

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(404,pag_noencontrada)
    app.run(host='0.0.0.0')
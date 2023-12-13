from modelo.Coneccion import conexion2023
from flask import jsonify, request

def buscar_medi(codigo):
    try:
        conn = conexion2023()
        cur = conn.cursor()
        cur.execute("""select * FROM medico WHERE ci = %s""", (codigo,))
        datos = cur.fetchone()
        conn.close()

        if datos != None:
            medi = {'cedula_identidad': datos[0], 'nombre': datos[1],
                       'apellido': datos[2], 'especialidad': datos[3],
                       'telefono': datos[4]}
            return medi
        else:
            return None
    except Exception as ex:
            raise ex
    

class ModeloMedico():
    @classmethod
    def listar_Medico(self):
        try:
            conn = conexion2023()
            cursor=conn.cursor()
            cursor.execute("SELECT * FROM medico")
            datos = cursor.fetchall()
            medicos = []

            for fila in datos:
                medi = {'cedula_identidad': fila[0],
                       'nombre': fila[1],
                       'apellido': fila[2],
                       'especialidad': fila[3],
                       'telefono': fila[4]}
                medicos.append(medi)

            conn.close()

            return jsonify({'medicos': medicos, 'mensaje': "medicos listados.", 'exito': True})
        except Exception as ex:
            return jsonify({'mensaje': "Errorr", 'exito': False})
    
    @classmethod
    def lista_Medico(self,codigo):
        try:
            usuario = buscar_medi(codigo)
            if usuario != None:
                return jsonify({'usuarios': usuario, 'mensaje': "usuario encontrado.", 'exito': True})
            else:
                return jsonify({'mensaje': "Usuario no encontrado.", 'exito': False})
        except Exception as ex:
            return jsonify({'mensaje': "Error", 'exito': False})

    @classmethod
    def registrar_medico(self):
        try:
            usuario = buscar_medi(request.json['ci_e'])
            if usuario != None:
                return jsonify({'mensaje': "Cedula de identidad  ya existe, no se puede duplicar.", 'exito': False})
            else:
                conn = conexion2023()
                cur = conn.cursor()
                cur.execute('INSERT INTO medico values(%s,%s,%s,%s,%s)', (request.json['ci_e'], request.json['nombre_e'], request.json['apellido_e'],
                                                                            request.json['especialidad_e'], request.json['telefono_e']))
                conn.commit()
                conn.close()
                return jsonify({'mensaje': "Usuario registrado.", 'exito': True})
        except Exception as ex:
            return jsonify({'mensaje': "Error", 'exito': False})
    
    @classmethod
    def actualizar_medico(self,codigo):
        try:
            usuario = buscar_medi(codigo)
            if usuario != None:
                conn = conexion2023()
                cur = conn.cursor()
                cur.execute("""UPDATE medico SET nombre=%s, apellido=%s, especialidad=%s,
                telefono=%s WHERE ci=%s""",
                        (request.json['nombre_e'], request.json['apellido_e'], request.json['especialidad_e'], request.json['telefono_e'], codigo))
                conn.commit()
                conn.close()
                return jsonify({'mensaje': "medico actualizado.", 'exito': True})
            else:
                return jsonify({'mensaje': "medico  no encontrado.", 'exito': False})
        except Exception as ex:
                return jsonify({'mensaje': "Error", 'exito': False})
        
    @classmethod
    def eliminar_medico(self,codigo):
        try:
            usuario = buscar_medi(codigo)
            if usuario != None:
                conn = conexion2023()
                cur = conn.cursor()
                cur.execute("DELETE FROM medico WHERE ci = %s", (codigo,))
                conn.commit()
                conn.close()
                return jsonify({'mensaje': "medico eliminado.", 'exito': True})
            else:
                return jsonify({'mensaje': "medico no encontrado.", 'exito': False})
        except Exception as ex:
            return jsonify({'mensaje': "Error", 'exito': False})
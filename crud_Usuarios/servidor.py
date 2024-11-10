import grpc
import usuarios_pb2_grpc
import usuarios_pb2
from concurrent import futures
import db  

class Usuarios(usuarios_pb2_grpc.UsuarioServiceServicer):
    
    def CrearUsuario(self, request, context):
        nombre = request.nombre
        email = request.email
        exito, mensaje, id_usuario = db.agregar_usuario(nombre, email)

        if exito:
            return usuarios_pb2.CrearUsuarioResponse(
                exito=True,
                mensaje=mensaje,
                usuario=usuarios_pb2.Usuario(
                    id=id_usuario,
                    nombre=nombre,
                    email=email
                )
            )
        
        return usuarios_pb2.CrearUsuarioResponse(
            exito=False,
            mensaje=mensaje
        )

    def ObtenerUsuarios(self, request, context):
        usuarios = db.obtener_usuarios()
        response = usuarios_pb2.ObtenerUsuariosResponse()
        
        for usuario in usuarios:
            response.usuarios.add(
                id=usuario[0],
                nombre=usuario[1],
                email=usuario[2]
            )
        
        return response

    def ActualizarUsuario(self, request, context):
        usuario_id = request.id
        nombre = request.nombre
        email = request.email
        exito, mensaje = db.actualizar_usuario(usuario_id, nombre, email)

        if exito:
            return usuarios_pb2.ActualizarUsuarioResponse(
                exito=True,
                mensaje=mensaje,
                usuario=usuarios_pb2.Usuario(
                    id=usuario_id,
                    nombre=nombre,
                    email=email
                )
            )

        return usuarios_pb2.ActualizarUsuarioResponse(
            exito=False,
            mensaje=mensaje
        )

    def EliminarUsuario(self, request, context):
        usuario_id = request.id
        exito, mensaje = db.eliminar_usuario(usuario_id)
        
        return usuarios_pb2.EliminarUsuarioResponse(
            exito=exito,
            mensaje=mensaje
        )

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    usuarios_pb2_grpc.add_UsuarioServiceServicer_to_server(Usuarios(), server)
    server.add_insecure_port('[::]:50053')
    server.start()
    print("Servidor gRPC de usuarios escuchando en el puerto 50053...")
    server.wait_for_termination()

if __name__ == '__main__':
    db.init_db()
    serve()

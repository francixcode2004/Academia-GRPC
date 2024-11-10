import grpc
import usuarios_pb2_grpc
import usuarios_pb2
from google.protobuf import empty_pb2

def run():
    # Crear canal de comunicación con el servidor
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = usuarios_pb2_grpc.UsuarioServiceStub(channel)

        # Crear un nuevo usuario
        print("Creando usuario...")
        response = stub.CrearUsuario(usuarios_pb2.CrearUsuarioRequest(
            nombre="Juan Pérez",
            email="juan.perez@example.com"
        ))
        print(f"Respuesta: {response.mensaje}, ID del Usuario: {response.usuario.id}")

        # Obtener todos los usuarios
        print("\nObteniendo todos los usuarios...")
        # Aquí, no necesitamos pasar ningún parámetro, solo usamos el mensaje vacío
        response = stub.ObtenerUsuarios(empty_pb2.Empty())
        print("Usuarios:")
        for usuario in response.usuarios:
            print(f"ID: {usuario.id}, Nombre: {usuario.nombre}, Email: {usuario.email}")

        # Actualizar un usuario
        print("\nActualizando usuario...")
        usuario_id = response.usuarios[0].id  # Suponemos que el primer usuario es el que vamos a actualizar
        response = stub.ActualizarUsuario(usuarios_pb2.ActualizarUsuarioRequest(
            id=usuario_id,
            nombre="Juan Pérez Actualizado",
            email="juan.perez.updated@example.com"
        ))
        print(f"Respuesta: {response.mensaje}")

        print("\nEliminando usuario...")
        response = stub.EliminarUsuario(usuarios_pb2.EliminarUsuarioRequest(id=usuario_id))
        print(f"Respuesta: {response.mensaje}")

if __name__ == '__main__':
    run()

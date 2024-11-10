import grpc
from concurrent import futures
import inscripcion_pb2
import inscripcion_pb2_grpc
from db_inscripciones import init_db, inscribir_usuario_en_curso, obtener_cursos_por_usuario, crear_tabla

class InscripcionService(inscripcion_pb2_grpc.InscripcionServiceServicer):
    def __init__(self):
        # Conectar a la base de datos y crear las tablas si no existen
        self.conn = init_db()
        crear_tabla(self.conn)

    def InscribirUsuarioEnCurso(self, request, context):
        # Inscribir al usuario en un curso usando la función definida en db_inscripciones.py
        inscribir_usuario_en_curso(self.conn, request.usuario_id, request.curso_id)
        return inscripcion_pb2.InscribirUsuarioResponse(exito=True, mensaje="Usuario inscrito exitosamente")

    def ObtenerCursosPorUsuario(self, request, context):
        # Obtener los cursos del usuario usando la función definida en db_inscripciones.py
        cursos = obtener_cursos_por_usuario(self.conn, request.usuario_id)
        cursos_response = [
            inscripcion_pb2.Curso(id=row[0], nombreCurso=row[1], nombreProfesor=row[2])
            for row in cursos
        ]
        return inscripcion_pb2.ObtenerCursosPorUsuarioResponse(curso=cursos_response)

def serve():
    # Crear el servidor GRPC y agregar el servicio InscripcionService
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    inscripcion_pb2_grpc.add_InscripcionServiceServicer_to_server(InscripcionService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Servidor GRPC en ejecución en el puerto 50051")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()

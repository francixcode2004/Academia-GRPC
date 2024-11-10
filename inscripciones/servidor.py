import grpc
from concurrent import futures
import inscripcion_pb2
import inscripcion_pb2_grpc
from db_inscripciones import init_db, inscribir_usuario_en_curso, obtener_cursos_por_usuario, crear_tabla

class InscripcionService(inscripcion_pb2_grpc.InscripcionServiceServicer):
    def __init__(self):
        # Establecer conexión a la base de datos
        self.conn = init_db()
        # Crear las tablas si no existen
        crear_tabla(self.conn)

    def InscribirUsuarioEnCurso(self, request, context):
        """Método para inscribir al usuario en un curso"""
        try:
            inscribir_usuario_en_curso(self.conn, request.usuario_id, request.curso_id)
            return inscripcion_pb2.InscribirUsuarioResponse(
                exito=True, mensaje="Usuario inscrito exitosamente"
            )
        except Exception as e:
            return inscripcion_pb2.InscribirUsuarioResponse(
                exito=False, mensaje=f"Error al inscribir: {str(e)}"
            )

    def ObtenerCursosPorUsuario(self, request, context):
        """Método para obtener los cursos en los que un usuario está inscrito"""
        try:
            cursos = obtener_cursos_por_usuario(self.conn, request.usuario_id)
            cursos_response = [
                inscripcion_pb2.Curso(id=row[0], nombreCurso=row[1], nombreProfesor=row[2])
                for row in cursos
            ]
            return inscripcion_pb2.ObtenerCursosPorUsuarioResponse(curso=cursos_response)
        except Exception as e:
            context.set_details(f"Error al obtener cursos: {str(e)}")
            context.set_code(grpc.StatusCode.INTERNAL)
            return inscripcion_pb2.ObtenerCursosPorUsuarioResponse()

def serve():
    """Configurar y arrancar el servidor gRPC"""
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    inscripcion_pb2_grpc.add_InscripcionServiceServicer_to_server(InscripcionService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Servidor GRPC en ejecución en el puerto 50051")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()

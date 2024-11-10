import grpc
from concurrent import futures
import cursos_pb2
import cursos_pb2_grpc
from google.protobuf import empty_pb2
import bd_cursos

class CursoService(cursos_pb2_grpc.CursoServiceServicer):
    
    def InsertarCurso(self, request, context):
        curso_id = bd_cursos.insertar_curso(
            request.nombreCurso,
            request.descripcion,
            request.nombreProfesor,
            request.numeroDeHoras
        )
        
        return cursos_pb2.InsertarCursoResponse(
            exito=True,
            mensaje="Curso insertado correctamente",
            curso=cursos_pb2.Curso(
                id=curso_id,
                nombreCurso=request.nombreCurso,
                descripcion=request.descripcion,
                nombreProfesor=request.nombreProfesor,
                numeroDeHoras=request.numeroDeHoras
            )
        )
    
    def ObtenerCursos(self, request, context):
        cursos_data = bd_cursos.obtener_cursos()

        response = cursos_pb2.ObtenerCursosResponse()
        for curso in cursos_data:
            response.cursos.add(
                id=curso[0],
                nombreCurso=curso[1],
                descripcion=curso[2],
                nombreProfesor=curso[3],
                numeroDeHoras=curso[4]
            )
        return response

    def ObtenerCurso(self, request, context):
        curso = bd_cursos.obtener_curso_por_id(request.id)
        
        if curso:
            return cursos_pb2.ObtenerCursoResponse(
                exito=True,
                mensaje="Curso encontrado",
                curso=cursos_pb2.Curso(
                    id=curso[0],
                    nombreCurso=curso[1],
                    descripcion=curso[2],
                    nombreProfesor=curso[3],
                    numeroDeHoras=curso[4]
                )
            )
        else:
            return cursos_pb2.ObtenerCursoResponse(exito=False, mensaje="Curso no encontrado")

    def ActualizarCurso(self, request, context):
        actualizado = bd_cursos.actualizar_curso(
            request.id,
            request.nombreCurso,
            request.descripcion,
            request.nombreProfesor,
            request.numeroDeHoras
        )
        
        if actualizado:
            return cursos_pb2.ActualizarCursoResponse(
                exito=True,
                mensaje="Curso actualizado correctamente",
                curso=cursos_pb2.Curso(
                    id=request.id,
                    nombreCurso=request.nombreCurso,
                    descripcion=request.descripcion,
                    nombreProfesor=request.nombreProfesor,
                    numeroDeHoras=request.numeroDeHoras
                )
            )
        else:
            return cursos_pb2.ActualizarCursoResponse(exito=False, mensaje="Curso no encontrado")

    def EliminarCurso(self, request, context):
        eliminado = bd_cursos.eliminar_curso(request.id)
        
        if eliminado:
            return cursos_pb2.EliminarCursoResponse(exito=True, mensaje="Curso eliminado correctamente")
        else:
            return cursos_pb2.EliminarCursoResponse(exito=False, mensaje="Curso no encontrado")

def serve():
    bd_cursos.init_db()  # Crear la base de datos si no existe
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    cursos_pb2_grpc.add_CursoServiceServicer_to_server(CursoService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print('Servidor de cursos iniciado')
    server.wait_for_termination()

if __name__ == '__main__':
    serve()

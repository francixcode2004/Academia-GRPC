import grpc
import cursos_pb2
import cursos_pb2_grpc
from google.protobuf import empty_pb2

def insertar_curso(stub, nombreCurso, descripcion, nombreProfesor, numeroDeHoras):
    request = cursos_pb2.InsertarCursoRequest(
        nombreCurso=nombreCurso,
        descripcion=descripcion,
        nombreProfesor=nombreProfesor,
        numeroDeHoras=numeroDeHoras
    )
    response = stub.InsertarCurso(request)
    if response.exito:
        print(f"Curso insertado correctamente: {response.curso}")
    else:
        print("Error al insertar el curso")

def obtener_cursos(stub):
    response = stub.ObtenerCursos(empty_pb2.Empty())
    if response.cursos:
        print("Lista de cursos:")
        for curso in response.cursos:
            print(f"ID: {curso.id}, Nombre: {curso.nombreCurso}, Profesor: {curso.nombreProfesor}")
    else:
        print("No se encontraron cursos")

def obtener_curso(stub, curso_id):
    request = cursos_pb2.ObtenerCursoRequest(id=curso_id)
    response = stub.ObtenerCurso(request)
    if response.exito:
        curso = response.curso
        print(f"Curso encontrado: ID={curso.id}, Nombre={curso.nombreCurso}, Profesor={curso.nombreProfesor}")
    else:
        print("Curso no encontrado")

def actualizar_curso(stub, curso_id, nombreCurso, descripcion, nombreProfesor, numeroDeHoras):
    request = cursos_pb2.ActualizarCursoRequest(
        id=curso_id,
        nombreCurso=nombreCurso,
        descripcion=descripcion,
        nombreProfesor=nombreProfesor,
        numeroDeHoras=numeroDeHoras
    )
    response = stub.ActualizarCurso(request)
    if response.exito:
        print(f"Curso actualizado correctamente: {response.curso}")
    else:
        print("Error al actualizar el curso")

def eliminar_curso(stub, curso_id):
    request = cursos_pb2.EliminarCursoRequest(id=curso_id)
    response = stub.EliminarCurso(request)
    if response.exito:
        print("Curso eliminado correctamente")
    else:
        print("Error al eliminar el curso")

def run():
    # Conectar al servidor
    with grpc.insecure_channel('localhost:50052') as channel:
        stub = cursos_pb2_grpc.CursoServiceStub(channel)
        
        # Insertar un curso
        insertar_curso(stub, "Matemáticas Avanzadas", "Curso de cálculo avanzado", "Dr. Juan Pérez", 40)
        
        # Obtener todos los cursos
        obtener_cursos(stub)
        
        # Obtener un curso específico por ID
        obtener_curso(stub, 1)
        
        # Actualizar un curso existente
        actualizar_curso(stub, 1, "Matemáticas Básicas", "Curso introductorio de matemáticas", "Dr. Ana López", 30)
        
        # Obtener todos los cursos después de la eliminación
        obtener_cursos(stub)
        
        # Eliminar un curso
        eliminar_curso(stub, 1)
if __name__ == '__main__':
    run()

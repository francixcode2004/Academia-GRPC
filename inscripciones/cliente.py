import grpc
import crud_Usuarios.usuarios_pb2_grpc
import crud_Usuarios.usuarios_pb2
import cursos.cursos_pb2_grpc
import cursos.cursos_pb2
import inscripcion_pb2_grpc
import inscripcion_pb2


def obtener_canales():
    """Establece las conexiones gRPC para los servicios de Usuarios, Cursos e Inscripciones"""
    usuario_channel = grpc.insecure_channel('localhost:50051')
    cursos_channel = grpc.insecure_channel('localhost:50051')
    inscripcion_channel = grpc.insecure_channel('localhost:50051')
    return usuario_channel, cursos_channel, inscripcion_channel


def menu_admin():
    """Muestra el menú para el admin"""
    print("\n--- Menú Admin ---")
    print("1. Cursos")
    print("2. Usuarios")
    print("3. Salir")
    opcion = int(input("Seleccione una opción: "))
    return opcion


def menu_cursos():
    """Muestra el menú de opciones de Cursos para el Admin"""
    print("\n--- Menú de Cursos ---")
    print("1. Insertar Curso")
    print("2. Obtener Cursos")
    print("3. Obtener Curso por ID")
    print("4. Actualizar Curso")
    print("5. Eliminar Curso")
    print("6. Regresar")
    opcion = int(input("Seleccione una opción: "))
    return opcion


def menu_usuarios():
    """Muestra el menú de opciones de Usuarios para el Admin"""
    print("\n--- Menú de Usuarios ---")
    print("1. Crear Usuario")
    print("2. Obtener Usuarios")
    print("3. Actualizar Usuario")
    print("4. Eliminar Usuario")
    print("5. Regresar")
    opcion = int(input("Seleccione una opción: "))
    return opcion


def menu_usuario():
    """Muestra el menú de opciones para el Usuario"""
    print("\n--- Menú Usuario ---")
    print("1. Listar Cursos")
    print("2. Inscribirse en un Curso")
    print("3. Salir")
    opcion = int(input("Seleccione una opción: "))
    return opcion


def ejecutar_admin(usuario_channel, cursos_channel):
    """Ejecuta las opciones del menú de administrador"""
    while True:
        opcion = menu_admin()
        if opcion == 1:
            # Submenú Cursos
            opcion_curso = menu_cursos()

            if opcion_curso == 1:
                # Insertar Curso
                insertar_curso(cursos_channel)
            elif opcion_curso == 2:
                # Obtener todos los Cursos
                obtener_cursos(cursos_channel)
            elif opcion_curso == 3:
                # Obtener Curso por ID
                obtener_curso_por_id(cursos_channel)
            elif opcion_curso == 4:
                # Actualizar Curso
                actualizar_curso(cursos_channel)
            elif opcion_curso == 5:
                # Eliminar Curso
                eliminar_curso(cursos_channel)
            elif opcion_curso == 6:
                break

        elif opcion == 2:
            # Submenú Usuarios
            opcion_usuario = menu_usuarios()

            if opcion_usuario == 1:
                # Crear Usuario
                crear_usuario(usuario_channel)
            elif opcion_usuario == 2:
                # Obtener Usuarios
                obtener_usuarios(usuario_channel)
            elif opcion_usuario == 3:
                # Actualizar Usuario
                actualizar_usuario(usuario_channel)
            elif opcion_usuario == 4:
                # Eliminar Usuario
                eliminar_usuario(usuario_channel)
            elif opcion_usuario == 5:
                break

        elif opcion == 3:
            break
def ejecutar_usuario(inscripcion_channel):
    """Ejecuta las opciones del menú de Usuario"""
    while True:
        opcion = menu_usuario()
        if opcion == 1:
            # Listar Cursos
            listar_cursos(inscripcion_channel)

        elif opcion == 2:
            # Inscribirse en un Curso
            inscribirse_curso(inscripcion_channel)

        elif opcion == 3:
            break


def crear_usuario(usuario_channel):
    """Crea un nuevo usuario"""
    nombre = input("Ingrese el nombre del usuario: ")
    email = input("Ingrese el correo del usuario: ")
    stub = usuarios_pb2_grpc.UsuarioServiceStub(usuario_channel)
    response = stub.CrearUsuario(usuarios_pb2.CrearUsuarioRequest(nombre=nombre, email=email))
    print(f"Exito: {response.exito}, Mensaje: {response.mensaje}")


def obtener_usuarios(usuario_channel):
    """Obtiene todos los usuarios"""
    stub = usuarios_pb2_grpc.UsuarioServiceStub(usuario_channel)
    response = stub.ObtenerUsuarios(usuarios_pb2.ObtenerUsuariosRequest())
    for usuario in response.usuarios:
        print(f"ID: {usuario.id}, Nombre: {usuario.nombre}, Email: {usuario.email}")


def actualizar_usuario(usuario_channel):
    """Actualiza un usuario"""
    usuario_id = int(input("Ingrese el ID del usuario a actualizar: "))
    nombre = input("Ingrese el nuevo nombre del usuario: ")
    email = input("Ingrese el nuevo correo del usuario: ")
    stub = usuarios_pb2_grpc.UsuarioServiceStub(usuario_channel)
    response = stub.ActualizarUsuario(usuarios_pb2.ActualizarUsuarioRequest(
        id=usuario_id,
        nombre=nombre,
        email=email
    ))
    print(f"Exito: {response.exito}, Mensaje: {response.mensaje}")


def eliminar_usuario(usuario_channel):
    """Elimina un usuario"""
    usuario_id = int(input("Ingrese el ID del usuario a eliminar: "))
    stub = usuarios_pb2_grpc.UsuarioServiceStub(usuario_channel)
    response = stub.EliminarUsuario(usuarios_pb2.EliminarUsuarioRequest(id=usuario_id))
    print(f"Exito: {response.exito}, Mensaje: {response.mensaje}")


def insertar_curso(cursos_channel):
    """Inserta un curso"""
    nombre_curso = input("Ingrese el nombre del curso: ")
    descripcion = input("Ingrese la descripción del curso: ")
    nombre_profesor = input("Ingrese el nombre del profesor: ")
    numero_de_horas = int(input("Ingrese el número de horas del curso: "))
    stub = cursos_pb2_grpc.CursoServiceStub(cursos_channel)
    response = stub.InsertarCurso(cursos_pb2.InsertarCursoRequest(
        nombreCurso=nombre_curso,
        descripcion=descripcion,
        nombreProfesor=nombre_profesor,
        numeroDeHoras=numero_de_horas
    ))
    print(f"Exito: {response.exito}, Mensaje: {response.mensaje}")


def obtener_cursos(cursos_channel):
    """Obtiene todos los cursos"""
    stub = cursos_pb2_grpc.CursoServiceStub(cursos_channel)
    response = stub.ObtenerCursos(cursos_pb2.ObtenerCursosRequest())
    for curso in response.cursos:
        print(f"ID: {curso.id}, Nombre: {curso.nombreCurso}, Profesor: {curso.nombreProfesor}")


def obtener_curso_por_id(cursos_channel):
    """Obtiene un curso por ID"""
    curso_id = int(input("Ingrese el ID del curso a obtener: "))
    stub = cursos_pb2_grpc.CursoServiceStub(cursos_channel)
    response = stub.ObtenerCurso(cursos_pb2.ObtenerCursoRequest(id=curso_id))
    if response.exito:
        print(f"Curso encontrado: {response.curso.nombreCurso} ({response.curso.nombreProfesor})")
    else:
        print(response.mensaje)


def actualizar_curso(cursos_channel):
    """Actualiza un curso"""
    curso_id = int(input("Ingrese el ID del curso a actualizar: "))
    nombre_curso = input("Ingrese el nuevo nombre del curso: ")
    descripcion = input("Ingrese la nueva descripción del curso: ")
    nombre_profesor = input("Ingrese el nuevo nombre del profesor: ")
    numero_de_horas = int(input("Ingrese el nuevo número de horas del curso: "))
    stub = cursos_pb2_grpc.CursoServiceStub(cursos_channel)
    response = stub.ActualizarCurso(cursos_pb2.ActualizarCursoRequest(
        id=curso_id,
        nombreCurso=nombre_curso,
        descripcion=descripcion,
        nombreProfesor=nombre_profesor,
        numeroDeHoras=numero_de_horas
    ))
    print(f"Exito: {response.exito}, Mensaje: {response.mensaje}")


def eliminar_curso(cursos_channel):
    """Elimina un curso"""
    curso_id = int(input("Ingrese el ID del curso a eliminar: "))
    stub = cursos_pb2_grpc.CursoServiceStub(cursos_channel)
    response = stub.EliminarCurso(cursos_pb2.EliminarCursoRequest(id=curso_id))
    print(f"Exito: {response.exito}, Mensaje: {response.mensaje}")


def listar_cursos(inscripcion_channel):
    """Listar todos los cursos"""
    stub = inscripcion_pb2_grpc.InscripcionServiceStub(inscripcion_channel)
    response = stub.ObtenerCursosPorUsuario(inscripcion_pb2.ObtenerCursosPorUsuarioRequest(usuario_id=1))
    for curso in response.curso:
        print(f"ID: {curso.id}, Nombre: {curso.nombreCurso}, Profesor: {curso.nombreProfesor}")


def inscribirse_curso(inscripcion_channel):
    """Inscribirse en un curso"""
    curso_id = int(input("Ingrese el ID del curso al que desea inscribirse: "))
    usuario_id = int(input("Ingrese su ID de usuario: "))
    stub = inscripcion_pb2_grpc.InscripcionServiceStub(inscripcion_channel)
    response = stub.InscribirseCurso(inscripcion_pb2.InscribirseCursoRequest(
        usuario_id=usuario_id,
        curso_id=curso_id
    ))
    print(f"Inscripción exitosa: {response.exito}, Mensaje: {response.mensaje}")
    
def main():
    """Función principal"""
    usuario_channel, cursos_channel, inscripcion_channel = obtener_canales()
    while True:
        print("\n--- Menú Principal ---")
        print("1. Administrador")
        print("2. Usuario")
        print("3. Salir")
        opcion = int(input("Seleccione una opción: "))
        if opcion == 1:
            ejecutar_admin(usuario_channel, cursos_channel)
        elif opcion == 2:
            ejecutar_usuario(inscripcion_channel)
        elif opcion == 3:
            break
if __name__ == "__main__":
    main()
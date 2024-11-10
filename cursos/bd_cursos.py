import sqlite3

def init_db():
    conn = sqlite3.connect('academia.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cursos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombreCurso TEXT NOT NULL,
            descripcion TEXT,
            nombreProfesor TEXT,
            numeroDeHoras INTEGER
        )
    ''')
    conn.commit()
    conn.close()

def insertar_curso(nombreCurso, descripcion, nombreProfesor, numeroDeHoras):
    conn = sqlite3.connect('cursos.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO cursos (nombreCurso, descripcion, nombreProfesor, numeroDeHoras)
        VALUES (?, ?, ?, ?)
    ''', (nombreCurso, descripcion, nombreProfesor, numeroDeHoras))
    conn.commit()
    curso_id = cursor.lastrowid
    conn.close()
    return curso_id

def obtener_cursos():
    conn = sqlite3.connect('cursos.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM cursos')
    cursos = cursor.fetchall()
    conn.close()
    return cursos

def obtener_curso_por_id(curso_id):
    conn = sqlite3.connect('cursos.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM cursos WHERE id = ?', (curso_id,))
    curso = cursor.fetchone()
    conn.close()
    return curso


def curso_existe(id):
    """Verifica si un curso existe por su ID."""
    conn = sqlite3.connect('cursos.db')
    cursor = conn.cursor()
    cursor.execute("SELECT 1 FROM cursos WHERE id = ?", (id,))
    existe = cursor.fetchone() is not None
    conn.close()
    return existe

def nombre_curso_existe(nombreCurso, id=None):
    """Verifica si ya existe un curso con el mismo nombre (excluyendo el ID dado)."""
    conn = sqlite3.connect('cursos.db')
    cursor = conn.cursor()
    if id:
        cursor.execute("SELECT 1 FROM cursos WHERE nombreCurso = ? AND id != ?", (nombreCurso, id))
    else:
        cursor.execute("SELECT 1 FROM cursos WHERE nombreCurso = ?", (nombreCurso,))
    existe = cursor.fetchone() is not None
    conn.close()
    return existe

def actualizar_curso(id, nombreCurso, descripcion, nombreProfesor, numeroDeHoras):
    """Actualiza un curso si existe y el nombre del curso no está duplicado."""
    
    # Verifica si el curso existe
    if not curso_existe(id):
        return False, "Curso no encontrado."

    # Verifica si el nombre del curso ya existe en otro registro
    if nombre_curso_existe(nombreCurso, id):
        return False, "El nombre del curso ya está registrado."

    # Realiza la actualización
    conn = sqlite3.connect('cursos.db')
    cursor = conn.cursor()
    try:
        cursor.execute('''
            UPDATE cursos
            SET nombreCurso = ?, descripcion = ?, nombreProfesor = ?, numeroDeHoras = ?
            WHERE id = ?
        ''', (nombreCurso, descripcion, nombreProfesor, numeroDeHoras, id))
        conn.commit()
        
        # Verifica si se realizó la actualización
        if cursor.rowcount == 0:
            return False, "Curso no encontrado o sin cambios."
    except sqlite3.IntegrityError as e:
        conn.close()
        return False, f"Error al actualizar el curso: {e}"
    
    conn.close()
    return True, "Curso actualizado exitosamente."

def eliminar_curso(id):
    conn = sqlite3.connect('cursos.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM cursos WHERE id = ?', (id,))
    conn.commit()
    cambios = cursor.rowcount
    conn.close()
    return cambios > 0

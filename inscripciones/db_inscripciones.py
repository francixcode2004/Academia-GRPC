import sqlite3

def init_db():
    # Conectar a la base de datos
    conn = sqlite3.connect('academia.db')
    conn.row_factory = sqlite3.Row
    return conn

def crear_tabla(conn):
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS inscripciones (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario_id INTEGER,
            curso_id INTEGER,
            FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE CASCADE,
            FOREIGN KEY (curso_id) REFERENCES cursos(id) ON DELETE CASCADE
        )
    """)
    conn.commit()
def inscribir_usuario_en_curso(conn, usuario_id, curso_id):
    """Inscribir a un usuario en un curso"""
    try:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO inscripciones (usuario_id, curso_id) 
            VALUES (?, ?)
        """, (usuario_id, curso_id))
        conn.commit()
    except sqlite3.IntegrityError as e:
        print(f"Error al inscribir usuario: {e}")
        conn.rollback()

def obtener_cursos_por_usuario(conn, usuario_id):
    """Obtener los cursos en los que está inscrito un usuario"""
    cursor = conn.cursor()
    cursor.execute("""
        SELECT c.id, c.nombreCurso, c.nombreProfesor 
        FROM inscripciones i
        JOIN cursos c ON i.curso_id = c.id
        WHERE i.usuario_id = ?
    """, (usuario_id,))
    return cursor.fetchall()
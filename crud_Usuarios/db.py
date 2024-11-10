import sqlite3

def init_db():
    conn = sqlite3.connect('academia.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    email TEXT NOT NULL UNIQUE)''')
    conn.commit()
    conn.close()

def email_existe(email):
    conn = sqlite3.connect('academia.db')
    c = conn.cursor()
    c.execute("SELECT id FROM usuarios WHERE email = ?", (email,))
    existe = c.fetchone() is not None
    conn.close()
    return existe

def agregar_usuario(nombre, email):    
    conn = sqlite3.connect('academia.db')
    c = conn.cursor()
    try:
        c.execute("INSERT INTO usuarios (nombre, email) VALUES (?, ?)", (nombre, email))
        conn.commit()
        id_usuario = c.lastrowid
    except sqlite3.IntegrityError as e:
        conn.close()
        return False, f"Error al agregar usuario: {e}", None
    conn.close()
    return True, "Usuario creado exitosamente.", id_usuario

def obtener_usuarios():
    
    conn = sqlite3.connect('academia.db')
    c = conn.cursor()
    c.execute("SELECT * FROM usuarios")
    usuarios = c.fetchall()
    conn.close()
    return usuarios

def eliminar_usuario(id):

    conn = sqlite3.connect('academia.db')
    c = conn.cursor()
    c.execute("DELETE FROM usuarios WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return True, "Usuario eliminado exitosamente."

def obtener_usuario(id):

    conn = sqlite3.connect('academia.db')
    c = conn.cursor()
    c.execute("SELECT * FROM usuarios WHERE id = ?", (id,))
    usuario = c.fetchone()
    conn.close()
    return usuario

def usuario_existe(id):

    conn = sqlite3.connect('academia.db')
    c = conn.cursor()
    c.execute("SELECT id FROM usuarios WHERE id = ?", (id,))
    existe = c.fetchone() is not None
    conn.close()
    return existe

def actualizar_usuario(id, nombre, email):
    
    if not usuario_existe(id):
        return False, "Usuario no encontrado."
    

    if email_existe(email):
        return False, "El email ya está registrado."

    conn = sqlite3.connect('academia.db')
    c = conn.cursor()
    try:
        c.execute("UPDATE usuarios SET nombre = ?, email = ? WHERE id = ?", (nombre, email, id))
        conn.commit()
        if c.rowcount == 0:
            return False, "Usuario no encontrado."
    except sqlite3.IntegrityError as e:
        conn.close()
        return False, f"Error al actualizar usuario: {e}"
    conn.close()
    return True, "Usuario actualizado exitosamente."

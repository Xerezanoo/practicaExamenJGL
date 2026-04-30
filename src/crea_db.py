'''
docstring del módulo 
'''

import db
from models_db import Student

if __name__ == '__main__':
    db.Base.metadata.create_all(db.engine)

    lista = [
        ("JGL", 20),
        ("Prueba2", 40),
        ("Marina", 32),
        ("Arturo", 34),
        ("Alfredo", 49)
    ]
    for x in lista:
        db.session.add(Student(x[0], x[1]))
    db.session.commit()

    # READ Consultas
    todos = db.session.query(Student).all()
    print("Todos: \n ", todos)

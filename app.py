from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
from person import Person
import jwt
app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'app_flask_db'
app.config['MYSQL_PASSWORD'] ='1234'
app.config['MYSQL_DB'] = 'db_flask_1'

app.config['SECRET_KEY'] = 'key1234'


mysql = MySQL(app)

@app.route('/login', methods = ['POST'])
def login():
    return jsonify({'index'})



@app.route('/persons', methods = ['GET'])
def get_all_persons():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM person')
    data = cur.fetchall()
    personList = []
    for row in data:
        objetopersona = Person(row)
        personList.append(objetopersona.toJson())
    return jsonify({'persons':[]})


@app.route('/persons', methods = ['POST'])
def create_persons():
    body = request.get_json()
    name = body['name']
    surname = body['surname']

    dni = body['dni']
    email = body['email']

    cur = mysql.connect.cursor()


    cur.execute('SELECT * FROM person WHERE email= %s', (email,) )
    row = cur.fetchone()
    if row:
        return jsonify({'message': "Ya existe el email"})


    cur.execute('INSERT INTO person (name, surname, dni, email) VALUES (%s, %s, %s, %s)', (name, surname, dni, email))
    mysql.connection.commit()    

    # obtener el id del registro creado

    cur.execute('SELECT LAST_INSERT_ID()')
    row =cur.fetchone()
    print(row) 

    return jsonify({'data':'creada','name':name, 'surname': surname, 'dni': dni, 'email': email, 'id': 100 })

@app.route('/persons/<int:id>', methods = ['GET'])
def get_persons_by_id(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM person WHERE id = {0}'.format(id))
    data = cur.fetchall()
    if len(data) > 0:
        return jsonify({"person": data[0]})

    
    return jsonify({"message": "id not found"})

@app.route('/persons/<int:id>', methods = ['POST'])
def update(id):
    body = request.get_json()
    name = body['name']
    surname = body['surname']
    dni = body['dni']
    email = body['email']
    cur = mysql.connection.cursor()
    cur.execute('UPDATE person SET name = %s, surname = %s, dni = %s,  email = %s, where id = %s' (name, surname, dni, email, id))
    mysql.connection.commit()
    return jsonify({'id':id,'name':name, 'surname': surname, 'dni': dni, 'email': email })

@app.route('/persons/<int:id>', methods = ['DELETE'])
def delete(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE ')
    return jsonify({'message': 'delete'})


if __name__ == '__main__':
    app.run(debug=True, port=4500)
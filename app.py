from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
from person import Person
app = Flask(__name__)

app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'user_flask'
app.config['MYSQL_PASSWORD'] ='1234'
app.config['MYSQL_DB'] = 'db_flask_2'


mysql = MySQL(app)

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
    cur.execute('INTo To person (name, surname, dni, email) VALUES (%s, %s, %s, %s)', (name, surname, dni, email))
    mysql.connection.commit()    

    return jsonify({'data':'creada','name':name, 'surname': surname, 'dni': dni, 'email': email })

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
    
    return jsonify({'id':id,'name':name, 'surname': surname, 'dni': dni, 'email': email })

@app.route('/persons/<int:id>', methods = ['DELETE'])
def delete(id):
    return jsonify({'message': 'delete'})


if __name__ == '__main__':
    app.run(debug=True, port=4500)
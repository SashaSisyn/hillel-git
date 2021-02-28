from flask import Flask, request
from utils import encrypt_message
from utils import decrypt_message
import string
import random
import requests
import sqlite3

app = Flask(__name__)


def generate_password(length: int = 10) -> str:
    choices = string.ascii_letters
    password = ''

    for i in range(length):
        password += random.choice(choices)

    return password


@app.route('/')
def hello_world():
    length = int (request.args.get('length') or 10)
    name = request.args.get('name', 'DEFAULT')
    age = request.args.get('age', 'DEFAULT_AGE')
    return  f'{name} {age}, here is your password {generate_password(length)}'

@app.route('/exp/')
def exp():
    return "exp"


#@app.route('/encrypt-message/')
#def encrypt_message_route():
#    message = request.args['message']
 #   return encrypt_message(message)


#@app.route('/fizz-buzz/')
#def fizz_buzz():
 #   num = request.args['num']
#    return fizz_buzz(num)


#@app.route('/decrypt-message/')
#def decrypt_message_route():
#    message = request.args['message']
 #   return decrypt_message(message)




#@app.route('/space/')
#def space():
#    response = requests.get('http://api.open-notify.org/astros.json')
#    num = response.json()['number']
  #  return str(num)


@app.route('/users/list/')
def users_list():
    import sqlite3

    try:
        connection = sqlite3.connect('./db.sqlite3')
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM users;")
        result = cursor.fetchall()

        connection.commit()
    finally:
        connection.close()

    return str(result)


@app.route('/users/create/')
def users_create():
    import sqlite3

    first_name = request.args['firstName']
    last_name = request.args['lastName']
    is_student = int(request.args['isStudent'] == 'true')
    ID = random.randint(1, 100_000)

    try:
        connection = sqlite3.connect('./db.sqlite3')
        cursor = connection.cursor()

        query = f"INSERT INTO users VALUES ({ID}, '{first_name}', '{last_name}', {is_student});"
        print(query)
        cursor.execute(query)
        connection.commit()
    finally:
        connection.close()

    return "OK"


@app.route('/phones/list/')
def phones_list():
    import sqlite3

    try:
        connection = sqlite3.connect('./db.sqlite3')
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM phones;")
        result = cursor.fetchall()

        connection.commit()
    finally:
        connection.close()

    return str(result)


@app.route('/phones/create/')
def phones_create():
    import sqlite3

    phone_value = request.args['phoneValue']
    user_id = request.args['userId']

    try:
        connection = sqlite3.connect('./db.sqlite3')
        cursor = connection.cursor()

        query = f"INSERT INTO phones VALUES (null, '{phone_value}', {user_id});"
        print(query)
        cursor.execute(query)
        connection.commit()
    finally:
        connection.close()

    return "OK"


@app.route('/users/phones/')
def users_phones():

    try:
        connection = sqlite3.connect('./db.sqlite3')
        cursor = connection.cursor()

        query = f"""
        SELECT phones.id, phones.value, users.first_name,users.last_name
        FROM phones
        INNER JOIN users ON phones.user_id = user_id;
        """
        cursor.execute(query)
        result = cursor.fetchall()

        connection.commit()
    finally:
        connection.close()

    return str(result)


@app.route('/emails/list/')
def emails_list():
    import sqlite3

    try:
        connection = sqlite3.connect('./db.sqlite3')
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM emails;")
        result = cursor.fetchall()

        connection.commit()
    finally:
        connection.close()

    return str(result)


@app.route('/emails/create/')
def emails_create():

    email_value = request.args['emailValue']
    user_id = request.args['userId']

    try:
        connection = sqlite3.connect('./db.sqlite3')
        cursor = connection.cursor()

        query = f"INSERT INTO emails VALUES (null, '{email_value}', {user_id});"
        print(query)
        cursor.execute(query)
        connection.commit()
    finally:
        connection.close()

    return "OK"


@app.route('/users/emails/')
def users_emails():

    try:
        connection = sqlite3.connect('./db.sqlite3')
        cursor = connection.cursor()

        query = f"""
        SELECT emails.id, emails.value
        FROM emails
        INNER JOIN users ON emails.user_id = user_id;
        """
        cursor.execute(query)
        result = cursor.fetchall()

        connection.commit()
    finally:
        connection.close()

    return str(result)





if __name__ == '__main__':
    app.run(debug=True)

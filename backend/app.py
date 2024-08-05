from flask import Flask, request, jsonify
from mongoengine import connect, Document, StringField
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "http://localhost:5173"}})

# Connect to MongoDB
connect(db='stat_scribe', host='mongodb', port=27017, username='root', password='rootpassword')

# Define User Document
class User(Document):
    username = StringField(required=True, unique=True)
    email = StringField(required=True, unique=True)
    password = StringField(required=True)

@app.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if not username or not email or not password:
        return jsonify({'error': 'Missing required fields'}), 400

    if User.objects(username=username).first():
        return jsonify({'error': 'Username already exists'}), 400

    if User.objects(email=email).first():
        return jsonify({'error': 'Email already exists'}), 400

    user = User(username=username, email=email, password=password)
    user.save()

    return jsonify({'message': 'User created successfully'}), 201

# Define Document for test
class Test(Document):
    test = StringField()

@app.route('/api/test', methods=['GET'])
def get_test_data():
    test_data = Test.objects().first()  # Fetch first document in 'test' collection
    if test_data:
        return jsonify({'test': test_data.test}), 200
    else:
        return jsonify({'error': 'No data found'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
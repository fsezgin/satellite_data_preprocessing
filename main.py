import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from flask import Flask

app = Flask(__name__)

# Fetch the service account key JSON file contents
cred = credentials.Certificate("serviceAccountKey.json")

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://satellite-data-4f84c-default-rtdb.europe-west1.firebasedatabase.app/'
})

# Get data
ref = db.reference('/data')
data = ref.get()
#print(data)
@app.route('/satellite-data', methods = ['GET'])
def satellite_data_get():
    return data

if __name__ == '__main__':
    app.run(host='0.0.0.0', port= 5000)
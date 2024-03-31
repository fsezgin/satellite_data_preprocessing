import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Fetch the service account key JSON file contents
cred = credentials.Certificate("serviceAccountKey.json")

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://satellite-data-4f84c-default-rtdb.europe-west1.firebasedatabase.app/'
})

# Get data
for node_number in range (0,20):
    ref = db.reference('/{node_number}'.format(node_number=node_number))
    print(ref.get())




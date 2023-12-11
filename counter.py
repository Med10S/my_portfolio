import firebase_admin
from firebase_admin import credentials, db
from flask import Flask, render_template

app = Flask(__name__)

# Téléchargez la clé privée JSON de votre projet Firebase et placez-la dans le même dossier que ce script.
cred = credentials.Certificate('path/to/your/firebase/credentials.json')
firebase_admin.initialize_app(cred, {'databaseURL': 'https://your-firebase-project-id.firebaseio.com/'})

def get_count():
    ref = db.reference('visits')
    count = ref.get()
    return count if count else 0

def increment_count():
    ref = db.reference('visits')
    count = get_count() + 1
    ref.set(count)
    return count

@app.route('/')
def index():
    count = increment_count()
    return render_template('index.html', count=count)

if __name__ == '__main__':
    app.run(debug=True)

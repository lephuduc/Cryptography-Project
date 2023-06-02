from flask import Flask, jsonify, request, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import inspect
from dotenv import load_dotenv
import os
import json
from models import *

load_dotenv()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("POSTGRESSQL_URI")
db.init_app(app)

@app.route('/api/getAbout', methods=['GET'])
def get_about():
    n = int(request.args.get('n', 3))
    about_list = About.query.limit(n).all()
    about_data = [{'mssv': about.id, 'name': about.name, 'email': about.email, 'description': about.description} for about in about_list]
    json_data = json.dumps(about_data)
    return jsonify(json_data)

@app.route('/api/updateAbout', methods=['POST'])
def update_about():
    data = request.json
    updated_abouts = []
    success = False

    try:
        for item in data:
            about_id = item.get('id')
            about = About.query.get(about_id)

            if about:
                about.name = item.get('name', about.name)
                about.email = item.get('email', about.email)
                about.description = item.get('description', about.description)
                db.session.commit()
                updated_abouts.append({
                    'id': about.id,
                    'name': about.name,
                    'email': about.email,
                    'description': about.description
                })
                success = True

        db.session.close()

        if success:
            return jsonify({'message': 'Update successful', 'data': updated_abouts})
        else:
            return jsonify({'message': 'No updates performed'})

    except Exception as e:
        return jsonify({'message': 'An error occurred', 'error': str(e)})
    
def insert_about():
    data = [
        {
            'id': 21522000,
            'name': 'Hoang',
            'email': '2152xxxx@gm.uit.edu.vn',
            'description': 'I am a web developer with expertise in Flask and SQLAlchemy.'
        },
        {
            'id': 21522001,
            'name': 'Duc',
            'email': '2152xxxx@gm.uit.edu.vn',
            'description': 'I specialize in frontend development and UI/UX design.'
        },
        {
            'id': 21522002,
            'name': 'Duc',
            'email': '2152xxxx@gm.uit.edu.vn',
            'description': 'I am a web developer with expertise in Flask and SQLAlchemy.'
        }
    ]

    for item in data:
        id = item['id']
        name = item['name']
        email = item['email']
        description = item['description']

        about = About(id=id, name=name, email=email, description=description)
        db.session.add(about)
    db.session.commit()

def init():
    with app.app_context():
        if not inspect(db.engine).has_table(About.__tablename__):
            db.drop_all()
            db.create_all()
            insert_about()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)


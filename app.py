from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import logging

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://dbuser:yourpassword@terraform-20231230183411087700000001.c348g0womtbc.ap-southeast-2.rds.amazonaws.com/mydatabase'
                                    
db = SQLAlchemy(app)

class DevOpsData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(200), nullable=False)
    feature = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"<DevOpsData {self.id}>"

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    user_data = request.form.get('userData')
    devops_feature = request.form.get('devOpsFeature')
    print("Received data:", user_data, devops_feature)

    if user_data:
        new_entry = DevOpsData(data=user_data, feature=devops_feature)
        db.session.add(new_entry)
        db.session.commit()

        return jsonify({"status": "success", "message": "Your data has been successfully recorded!"})
    else:
        return jsonify({"status": "error", "message": "Please enter data."})

if __name__ == '__main__':
    with app.app_context():
        try:
            db.create_all()
        except Exception as e:
            logging.error("Error connecting to the database: %s", str(e))
    app.run(debug=True)
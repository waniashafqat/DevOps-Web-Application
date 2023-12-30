from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///devops_data.db'
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

    if user_data:
        new_entry = DevOpsData(data=user_data, feature=devops_feature)
        db.session.add(new_entry)
        db.session.commit()

        return jsonify({"status": "success", "message": "Your data has been successfully recorded!"})
    else:
        return jsonify({"status": "error", "message": "Please enter data."})


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)


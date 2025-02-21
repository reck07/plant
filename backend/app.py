from flask import Flask, render_template, request, redirect, url_for
from models import db, Plant

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///plants.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route('/')
def index():
    plants = Plant.query.all()
    return render_template('index.html', plants=plants)

@app.route('/add', methods=['GET', 'POST'])
def add_plant():
    if request.method == 'POST':
        new_plant = Plant(
            name=request.form['name'],
            light=request.form['light'],
            water=request.form['water'],
            description=request.form['description'],
            care=request.form['care'],
            image_url=request.form['image_url']
        )
        db.session.add(new_plant)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('create_plant.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
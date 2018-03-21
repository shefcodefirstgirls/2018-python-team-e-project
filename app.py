import os
import psycopg2
import api

from flask import Flask, flash, render_template, request,  redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename


DATABASE=os.getcwd()+'/theyshared.dat'

if not os.path.exists("uploads"):
    os.mkdir("uploads") # making a folder in code


UPLOAD_FOLDER = os.getcwd()+'/uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app = Flask("my_first_app")
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/share', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        name = request.values["name"]
        email = request.values["email"]
        food = request.values["food"]
        introduction = request.values["introduction"]

        with open("uploads/users.txt", "a+") as output_file:
        #a=append w=rewrite r=read +=if it's not there, can create it
            output_file.write(name + ",")
            output_file.write(email + ",")
            output_file.write(food + ",")
            output_file.write(introduction + "\n")
        # if user does not select file, browser also submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            os.rename(UPLOAD_FOLDER +"/"+ filename, UPLOAD_FOLDER+"/"+name+'.jpg')
            return render_template("hall.html")
            #return redirect(url_for('uploaded_file', filename=filename))
    return render_template("share.html")



@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)

@app.route("/hall")
def to_hall():
    f = open("uploads/users.txt", "r")
    all_input = [line.split(',') for line in f.readlines()]
    f.close()
    return render_template("hall.html", uinfo=all_input)

@app.route("/")
def say_hello():
    return render_template("index.html")

@app.route("/founders")
def to_founders():
    return render_template("founders.html")

@app.route("/webdevelopers")
def to_webdevelopers():
    return render_template("webdevelopers.html")

@app.route("/like/")
def like():
    return render_template("like.html")

@app.route("/recipe") #api is here
def recipes():
    recipe_title=api.get_title("veganrecipes")
    recipe_url=api.get_url("veganrecipes")
    recipe_link=api.get_link("veganrecipes")
    return render_template("recipes.html",
        recipe_title=recipe_title, recipe_url=recipe_url, recipe_link=recipe_link)

@app.errorhandler(404)
def to_error(error):
    return render_template("error.html")

"""
This piece of logic checks whether you are running the app locally or on Heroku
(make an account at https://www.heroku.com/ before the deployment session!). When
running the app on Heroku, the PORT environment/config variable is pre-populated by
Heroku to tell our app the correct port to run on.

"""
if "PORT" in os.environ:
    app.run(host="0.0.0.0", port=int(os.environ["PORT"]))
else:
    app.run(debug=True)

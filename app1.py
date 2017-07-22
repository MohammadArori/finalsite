from flask import Flask, render_template, request
import random
import dataset
app= Flask(__name__)
db= dataset.connect("postgres://xowcdbrmcsjkou:f88facb0af01e897c53199941adfe619d7679355e42cf50312b711a875c1a57c@ec2-46-137-97-169.eu-west-1.compute.amazonaws.com:5432/dvabm39fnp3b")

@app.route("/Home")
def Home():
	return render_template("home.html")

if __name__ == "__main__":
	app.run(debug = True)
from flask import Flask, render_template, request
import random
import dataset
app= Flask(__name__)
db= dataset.connect("postgres://ytrpkutfzviokx:521bcabd11d7f3fd266e295b3d643e4bed6c5d0f7e3719068180f06a0397b3f7@ec2-23-21-96-159.compute-1.amazonaws.com:5432/de62nrcbge44ss")

@app.route("/Home")
def Home():
	return render_template("home.html")

if __name__ == "__main__":
	app.run(debug = True)
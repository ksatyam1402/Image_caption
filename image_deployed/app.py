from flask import Flask, render_template,request, redirect
import Caption_it

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/', methods = ['POST'])

def marks():
	if request.method == 'POST':
		f = request.files['userfile']
		path = "./static/{}".format(f.filename)
		f.save(path)
		caption = Caption_it.caption_this_image(path)
		#print(caption)

	return render_template("index.html", your_caption = caption)		


if __name__ == '__main__':
	app.run(debug = True)
# -*- coding: utf-8 -*-
""" 
Make a web app
"""

import os
from flask import Flask, request, redirect, url_for, render_template, send_from_directory
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'static'
ALLOWED_EXTENSIONS = set(['vtk','nii','nii.gz', 'obj', 'stl'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/')
def index(home=None):
	return render_template('index.html', home='none')

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
		file = request.files['file']
		if file: #and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			return redirect(url_for('show_file', filename=filename))
		return file.filename

@app.route('/showing/<filename>')
def show_file(filename):
	return render_template("index.html", home=filename)

if __name__ == '__main__':
	app.run(debug=True)
	#app.run(host='0.0.0.0')


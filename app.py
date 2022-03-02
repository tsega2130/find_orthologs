import os, sys
from tempfile import NamedTemporaryFile
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import subprocess #put in args orthovar needs

app = Flask(__name__) 

 
#UPLOAD_FOLDER = 'Users\tsabera\Desktop\OrthoVar_Flask\UPLOAD_FOLDER'
#app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

#size restriction to prevent
app.config["MAX_CONTENT_LENGTH"] = 1024 * 1024
app.config["UPLOAD_EXTENSIONS"] = ['.txt', '.fasta']


@app.route("/")
def entry():
    return render_template("home.html")

@app.route('/', methods=['POST'])
#runs when browser sends POST request 
def upload_file():
    #gets file from multi-key dictionary 
    uploaded_file1 = request.files['Human_Fasta_File']
    uploaded_file2 = request.files['Orthologs_Fasta_File']
    
    # generate temporary files 
    human_file = NamedTemporaryFile('w')
    ortho_file = NamedTemporaryFile('w')

    # save uploads to temparay file locations
    uploaded_file1.save(human_file.name)
    uploaded_file2.save(ortho_file.name)
    
    # run orthovar with temp file input
    result=subprocess.run(
        [sys.executable, "OrthoVar.py", "-O", ortho_file.name, "-H", human_file.name],
        capture_output=True, 
        text=True
    )
    
    # check for errors
    if result.returncode > 0:
        print(result.stderr)
        raise Exception("Error non-zero return code from OrthoVar")
    
    # render template with output
    return render_template("uploader.html", output=result.stdout)


#check what type file is coming in as before passing into subprocess 

import os
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from jinja2 import Template
import subprocess #put in args orthovar needs

app = Flask(__name__) 

 
#UPLOAD_FOLDER = 'Users\tsabera\Desktop\OrthoVar_Flask\UPLOAD_FOLDER'
#app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

#size restriction to prevent overloading
app.config["MAX_CONTENT_LENGTH"] = 1024 * 1024

#check what type file is coming in as before passing into subprocess 
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

    human_file_string = str(uploaded_file1.read().decode("utf-8"))
    ortho_file_string = str(uploaded_file2.read().decode("utf-8"))

    human_file_string = human_file_string.split("\n")
    ortho_file_string = ortho_file_string.split("\n")
    #print(human_file_string)
    #print(ortho_file_string)
    print(type(ortho_file_string))

    hum_access = ''
    hum_access = human_file_string[0].split(" ")[0][1:]
    print(hum_access)

    #Why is the passed variable uploaded_file.filename?
    if uploaded_file1.filename != '':
        uploaded_file1.save(uploaded_file1.filename)
    if uploaded_file2.filename != "":
        uploaded_file2.save(uploaded_file2.filename)
    
    
    #print(subprocess.run(f"python test_OrthoVar.py -O {uploaded_file2.filename} -H {uploaded_file1.filename}", shell=True, capture_output=True))
    #print(subprocess.CompletedProcess(args=[f"python OrthoVar.py -O {uploaded_file2.filename} -H {uploaded_file1.filename}"]))
    
    #text captures it as a string 
    #using shell = true has shell injection security implications?

    #HERE!! Most recent test 
    result = subprocess.run(f"python OrthoVar.py -O {uploaded_file2.filename} -H {uploaded_file1.filename}", shell = True, text = True, capture_output = True)
    print(result)
    print("std.out:", result.stdout)
   
    #Testing to see if the issue is test_orthovar or subprocess
    wowza = subprocess.run("cat 'data.txt'", shell = True, text = True, capture_output = True)
    print(wowza.stdout)
    print("here")
    
    return render_template("uploader.html", output = wowza.stdout, download_file = wowza.stdout)



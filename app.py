import os 
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


#differnet route for human fasta?

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
    print(human_file_string)
    print(ortho_file_string)

    hum_access = ''
    hum_access = human_file_string[0].split(" ")[0][1:]
    print(hum_access)

    """ 
    for line in human_file_string:
        if line[0] == '>':
            line = line.strip('>')
            line = line.split(' ')
            hum_access = hum_access + line[0] 
    """
    
    if uploaded_file1.filename != '':
        uploaded_file1.save(uploaded_file1.filename)
    if uploaded_file2.filename != "":
        uploaded_file2.save(uploaded_file2.filename)
    return render_template("home.html")
    #return redirect(url_for('home.html')) 

""" 
#align both human fasta with orthlogs fasta
    with open("combined.fasta", "w") as output:
        #read human fasta file
        with open(human_file_string, "r") as f1:
            line = f1.readline()
            while line:
                output.write(line)
                line = f1.readline()
        #read orthologs file
        with open(filename2, "r") as f2:
            output.write('\n')
            line = f2.readline()
            while line:
                output.write(line)
                line = f2.readline()
 
#use hum acess to go through parse_clin_var.json
"""

#subprocess.run(f"python OrthoVar.py -H {uploaded_file1.filename} -O {uploaded_file2.filename}", shell=True, capture_output=True)


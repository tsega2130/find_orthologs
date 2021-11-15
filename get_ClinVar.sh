#! /bin/sh 

""" 
What we want it to do 
-Download clinvar FTP file variant summary 
-Unzip and (translate to json from xml?)
-Parse and move to where 

Dr. TS
-Go to FTP server (ftp)
-wget to get file to download to location 
-call orthovar_parser to make json dictionary

curl -O -u user:password ftp://example.com/some-file
curl -O -u anonymous:dethurtleschmidt@davidson.edu ftp.ncbi.nih.gov/pub/clinvar/tab_delimited/variant_summary.txt.gz
"""

curl -O -u anonymous:dethurtleschmidt@davidson.edu ftp://ftp.ncbi.nih.gov/pub/clinvar/tab_delimited/variant_summary.txt.gz
gzip -dk variant_summary.txt.gz
mv variant_summary.txt variant_summary2.txt
python parse_clin_var.py



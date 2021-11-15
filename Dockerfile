FROM node:latest 

RUN wget http://www.drive5.com/muscle/downloads3.8.31/muscle3.8.31_i86linux64.tar.gz
RUN tar xzvf muscle3.8.31_i86linux64.tar.gz 
RUN chmod a+x muscle3.8.31_i86linux64
RUN mv muscle3.8.31_i86linux64 /usr/bin/muscle 

RUN apt-get update
RUN apt-get install -y python3-pip
RUN pip3 install biopython
RUN pip3 install io

RUN wget https://ftp.ncbi.nlm.nih.gov/pub/clinvar/tab_delimited/variant_summary.txt.gz 
RUN gunzip variant_summary2.txt.gz 


COPY OrthoVar.py /root/OrthoVar.py
COPY parse_clin_var.py /root/parse_clin_var.py

#copy parse_clinvar 
#copy clin_var 

CMD ["bash", "-l"]
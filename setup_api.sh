#!/bin/bash

# This script automatically sets up the gene_suggest api to run on virtual environment
# Go through the SETUP_API.md before running this application

# Prerequisites
#	python2.7
# 	virtualenv
# 	git (optional)
#	

# Create Virtual Environment where applicatioon will run
# $ /home/GSA# virtualenv gsa_dtest

virtualenv gsa_dtest

# Activate the virtual environment
# $ /home/GSA# source gsa_dtest/bin/activate

source ./gsa_dtest/bin/activate

# Install the required packages
# (gsa_dtest) $ /home/GSA# pip install -r requirement.txt

pip install -r requirements.txt

# Go to the gene_suggest directory
# (gsa_dtest) $ /home/GSA# cd gene_suggest

cd gene_suggest

# Run the test suite to check the application 
# Ensure you are in gene_suggest directory befor running tests
python test_gene_suggest_api.py

# 8) Run Tests  	
# 	(gsa) $ /home/GSA/gene_suggest# python test_gene_suggest_api.py
# 	If all the tests are successfull then you will get following prompt.
# 	........
#	----------------------------------------------------------------------
#	Ran 8 tests in 2.309s

#	OK
	
# 8) Run application
# 	By default the application will run on port 5000
# 	To run application type python run.py <port_no>(optional)
# 	If port number is specified it will run on that port other wise it will run on default port 5000
# 	(gsa_dtest) $ /home/GSA/gene_suggest# python run.py
# 	 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

# 	 OR
#	(gsa_dtest) $ /home/GSA/gene_suggest# python run.py 8000
#	 * Running on http://127.0.0.1:8000/ (Press CTRL+C to quit)

# 9) Open another terminal and then curl
# 	Make sure to use appropriate port number

# 	curl 'http://localhost:5000/gene_suggest?query=BR&species=homo_sapiens&limit=10' -X GET -Haccept:application/json
#	{
#	  "gene_names": [
#	    "BRAF", 
#	    "BRAFP1", 
#	    "BRAP", 
#	    "BRAT1", 
#	    "BRCA1", 
#	    "BRCA2", 
#	    "BRCC3", 
#	    "BRCC3P1", 
#	    "BRD1", 
#	    "BRD2"
#	  ]
#	}
#
#	curl 'http://localhost:5000/gene_suggest?query=LMA&species=homo_sapiens&limit=5' -X GET -Haccept:application/json
#	{
#	  "gene_names": [
#	    "LMAN1", 
#	    "LMAN1L", 
#	    "LMAN2", 
#	    "LMAN2L"
#	  ]
#	}



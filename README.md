# Gene Suggest REST API
	
	The api provides an endpoint gene_suggest.
  When requested with query, species and limit parameter provides the at most limit number of gene names.
	The api provides the list of suggested gene names for the given query and target species.
	The __gene_suggest__ REST API developed using flask, flask-restful and sqlalchemy.

##	Requirements
##	OS
##	API Specifications
##	Application Directory Structure
##	How to Setup Application ?
##	How to run the application ? 
##	Testing 

## Requirements
* Python 2.7
* virtualenv
* git  (optional)

## Opetating System
  * Ubuntu Preferred or any Linux flavor

## API Specifications
Please refer to the **API.md**

## Application Directory Structure 

	<Working Directory>
    |-----gene_suggest_api (gene_suggest_api-master if extracted from zip)
			|
			|-----gene_suggest
			|	|-----settings
			|	|	  |-----db_settings.csv
			|	|
			|	|-----__init__.py
			|	|-----app.py
			|	|-----db_settings.py					
			|	|-----read_csv_to_dict.py
			|	|-----run.py
			|	|
			|	|-----test_gene_suggest_api.py
			|
			|-----API.md
			|-----README.md
			|-----SETUP_API.md
			|
			|-----setup_api.sh
			|-----run_api.sh
			|
			|-----requirements.txt


## Setup Application
Make sure you are in gene_suggest_api directory
Once in gene_suggest_api directory

Application can be setup by
* Execute **setup_api.sh** script **from gene_suggest_api directory**

			----- OR -----

* Manually
	Follow Instrunctions in **SETUP_API.md** file


## Run Application

* Using run_api.sh
  Make sure that application is setup correctly

  Once in gene_suggest_api directory on shell prompt type  

  To run application at default port 5000  
  $/home/GSA/gene_suggest_api# `./run_api.sh`         // This will run application on default port 5000

  To run application at specific port let's say 8000  
  $/home/GSA/gene_suggest_api# `./run_api.sh 8000`    // This will run application on default port 8000

* Manually  
  * Activate virtualenv  
  `source ./gsa_dtest/bin/activate`  
  * Go to gene_suggest directory  
  `cd gene_suggest`  
  `python run.py` 		    // Runs applicataion on default port 5000  
  `python run.py 8000`  	// Runs applicataion on default port 8000  

## Testing
As per the specification in API.md document 

Once the application is running. 
Ensure to use correct port number

* Valid Request : Get at most 10 gene names starting with BR for homo_sapiens species  
`curl 'http://localhost:5000/gene_suggest?query=BR&species=homo_sapiens&limit=10' -X GET -Haccept:text/json`

* Valid Request : Get at most 10 gene names starting with LAM for homo_sapiens species  
`curl 'http://localhost:5000/gene_suggest?query=LAM&species=homo_sapiens&limit=10' -X GET -Haccept:text/json`

* Missing query  
`curl 'http://localhost:5000/gene_suggest?species=homo_sapiens&limit=10' -X GET -Haccept:text/json`

* Missing species  
`curl 'http://localhost:5000/gene_suggest?query=LAM&limit=10' -X GET -Haccept:text/json`

* Missing query and species both  
`curl 'http://localhost:5000/gene_suggest?limit=10' -X GET -Haccept:text/json`

* POST Method not allowed  
`curl 'http://localhost:5000/gene_suggest?query=BR&species=homo_sapiens&limit=10' -X POST -Haccept:text/json`
	
* PUT Method not allowed  
`curl 'http://localhost:5000/gene_suggest?query=BR&species=homo_sapiens&limit=10' -X PUT -Haccept:text/json`
	
* DELETE Method not allowed  
`curl 'http://localhost:5000/gene_suggest?query=BR&species=homo_sapiens&limit=10' -X DELETE -Haccept:text/json`
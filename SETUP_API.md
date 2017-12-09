## Prerequisites
  * python 2.7
  * virtualenv
  * git (optional)

## Make sure python2.7, virtual environment  and git is already installed.

## Application Setup
  * To setup application you can run setup_api.sh
	
      -----------	or ---------
	
  * To setup manually follow the steps below

    1) Go to the gene_suggest_api directory  
      `cd gene_suggest_api` 
      
    2) Create Virtual Environment where applicatioon will run  
      `virtualenv gsa_dtest`
      
    3) Activate the virtual environment  
 	    `source gsa_dtest/bin/activate`

    4) Install the required packages  
 	    (gsa_dtest) `pip install -r requirements.txt`

    5) Go to the  app_directory_path  ( gene_suggest directory)   
 	    (gsa_dtest) `cd gene_suggest`
      
    6) Run Tests  
      (gsa_dtest) `python test_gene_suggest_api.py`  
      If all the tests are successfull then you will get following prompt.  
        ........         
      Ran 7 tests in 2.309s  
        
	    OK

    7) Run application  
        By default the application will run on port 5000  
        To run application type `python run.py <port_no>`(optional)  
        
        If port number is specified it will run on that port other wise it will run on default port 5000  
        (gsa_dtest) `python run.py`  
          * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)  
      
            ---------OR----------  
              
        (gsa_dtest) `python run.py 8000`
          * Running on http://127.0.0.1:8000/ (Press CTRL+C to quit)

    8) Open another terminal and then curl
      ####  Make sure to use appropriate port number
        curl 'http://localhost:5000/gene_suggest?query=BR&species=homo_sapiens&limit=10' -X GET -Haccept:application/json  

        It should give following output  
          {
          "gene_names": 
            ["BRAF", "BRAFP1", "BRAP", "BRAT1", "BRCA1", "BRCA2", "BRCC3", "BRCC3P1", "BRD1", "BRD2"]
          }

        curl 'http://localhost:5000/gene_suggest?query=LMA&species=homo_sapiens&limit=5' -X GET -Haccept:application/json  
        
        It should give following output  
          {
          "gene_names": [ "LMAN1", "LMAN1L", "LMAN2", "LMAN2L"]		
          }
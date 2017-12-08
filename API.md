# URL : 
		/gene_suggest?query=:query&species=:species&limit=:limit
 		Example : /gene_suggest?query=BR&species=homo_sapiens&limit=10

# Method : 
		GET

# URL Params :
 	Required : species=[string]	 	e.g. species=homo_sapiens   
			   query=[string]		e.g. query=BRC
	Optional : limit=[integer] 		e.g. limit=25	[default limit 10]

# Success Response : 
	## Get at most 10 Gene names starting with BR in homo-sapiens species
	REQUEST 	: GET /gene_suggest?query=BR&species=homo_sapiens&limit=10
				  Accept application/json
	RESPONSE 	: 200
				  { "gene_names": 
					["BRAF", "BRAFP1", "BRAP", "BRAT1", "BRCA1", "BRCA2", "BRCC3", "BRCC3P1", "BRD1", "BRD2"]
				  }

	## Get at most 5 Gene names starting with LMA in homo-sapiens species
	REQUEST 	: GET /gene_suggest?query=LMA&species=homo_sapiens&limit=5
				  Accept application/json
	RESPONSE 	: 200 OK
				  { "gene_names": 
					[ "LMAN1", "LMAN1L", "LMAN2", "LMAN2L"]
				  }

# Error Response :
	## Missing species parameter
	Request 	: GET /gene_suggest?query=BR&limit=10						
				  Accept application/json
	Response 	: 400 BAD REQUEST
					{'message':'One or more required URL parameter is missing. 
						Valid Syntax :'/gene_suggest?query=:query&species=:species&limit'}

	## Missing query parameter
	Request 	: GET /gene_suggest?species=homo_sapiens&limit=10			
				  Accept application/json
	Response 	: 400 BAD REQUEST
					{'message':'One or more required URL parameter is missing. 
						Valid Syntax :'/gene_suggest?query=:query&species=:species&limit'}

	## Missing query and species parameter
	Request 	: GET /gene_suggest?limit=10			
				  Accept application/json
	Response 	: 400 BAD REQUEST
					{'message':'One or more required URL parameter is missing. 
						Valid Syntax :'/gene_suggest?query=:query&species=:species&limit'}

	## Method POST not allowed
	Request 	: POST /gene_suggest?query=BR&species=homo_sapiens&limit=10	
	Response    : 405 METHOD NOT ALLOWED
					{"message": "The method is not allowed for the requested URL."}

	## Method PUT not allowed
	Request 	: PUT /gene_suggest?query=BR&species=homo_sapiens&limit=10	
	Response    : 405 METHOD NOT ALLOWED
					{"message": "The method is not allowed for the requested URL."}
					
	## Method DELETE not allowed
	Request 	: DELETE /gene_suggest?query=BR&species=homo_sapiens&limit=10	
	Response    : 405 METHOD NOT ALLOWED
					{"message": "The method is not allowed for the requested URL."}

# Sample Call :
	curl 'http://localhost:5002/gene_suggest?query=BR&species=homo_sapiens&limit=10' -X GET	-Haccept:application/json
	curl 'http://localhost:5002/gene_suggest?query=LMA&species=homo_sapiens&limit=5' -X GET	-Haccept:application/json
		
# Notes :
	The API will send response in JSON format only.
	The Gene name matching is case insensitive. e.g query=br or query=BR or query=Br all will produce same result.
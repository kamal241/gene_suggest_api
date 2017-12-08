# Flask imports
from flask import Flask,request, abort
from flask_restful import Resource, Api, reqparse
from flask_jsonpify import jsonify
from flask import Response

# SQLAlchemy imports
from sqlalchemy.engine.url import URL
from sqlalchemy import MetaData, Table
from sqlalchemy import inspect, select
from sqlalchemy.sql import and_
from sqlalchemy import create_engine

# Other imports
from json import dumps

# System/OS imports
import sys
from db_settings import db_host, db_port, db_name, db_username, db_password

# Database connection parameters
db_drivername = 'mysql+pymysql'

# Database connection URL
db_conn_url = URL(db_drivername,username=db_username, host=db_host, port=db_port, database=db_name)

# Create Database engine for the given URL
db_engine = create_engine(db_conn_url)
metadata = MetaData()

# Gene resource based on gene_autocomplete table in the database
class Gene(Resource):
	"""Gene Resourse"""
	valid_url_syntax = '/gene_suggest?query=:query&species=:species&limit=:limit'
	__tablename__ = 'gene_autocomplete'

	def _check_valid_accept(self,ctype):
		"""
		Purpose 	: Check If client has requested to accept resource other than JSON
		Arguments 	: ctype - MIMEType requested by client 
		Returns 	: Aborts with HTTP 406 if requested type is other than  JSON
					  True if requested type is unspecified or is JSON
		"""		
		if ctype:
			if ctype not in ['*/*','application/json','text/json', 'text/html', None]:							
				not_accepted_msg = '%s not supported. Supported types application/json, text/json' % ctype
				abort(406,not_accepted_msg)

		return True

	def _check_req_parameters_for_get(self,args):
		"""
		Check if query and species arguments are supplied in the request or not
		If required arguments are not supplied then respond with code 400 and message
		"""

		rquery, rspecies, rlimit = '', '', 10

		if args['query'] is not None:
			rquery = args['query']
		else:			
			abort(400,'One or more required URL parameter is missing')			

		if args['species'] is not None:
			rspecies = args['species']
		else:
			abort(400,'One or more required URL parameter is missing')
			
		if args['limit'] is not None:
			rlimit = args['limit']

		return rquery, rspecies, rlimit

	def handle_valid_request(self, gene_qp, species_qp, limit):
		# Connect to the database
		gconn = db_engine.connect()
		
		# Load table gene_autocomplete to extract data based on arguments
		genes_table = Table(self.__tablename__,metadata, autoload=True, autoload_with=db_engine)

		# Extract distinct gene name and corresponding species from genes_table
		match_genes_q = select([genes_table.c.display_label,genes_table.c.species]).distinct().where(\
		#match_genes_q = select([genes_table]).where(\
			and_(genes_table.c.display_label.like(gene_qp),
				genes_table.c.species.like(species_qp))).limit(limit)
		match_genes_raw_data = db_engine.execute(match_genes_q)
		
		# Parse resultset and generate list of matched gene names
		result = {'gene_names': [i[0] for i in match_genes_raw_data.cursor]}

		# Close database connection
		gconn.close()
		return result

	def get(self, **kwargs):
		"""GET method implementation """
		# Parse arguments sent with GET request
		parser = reqparse.RequestParser()
		parser.add_argument('query', type=str)
		parser.add_argument('species', type=str)
		parser.add_argument('limit', type=int)
		args = parser.parse_args()

		self._check_valid_accept(request.accept_mimetypes.best)

		rquery, rspecies, rlimit = self._check_req_parameters_for_get(args)
		
		# Prepare query paramters based on request arguments
		gene_qp = rquery + '%'
		species_qp = rspecies
		limit = rlimit
		
		result = self.handle_valid_request(gene_qp, species_qp, limit)

		# Return JSON response
		return jsonify(result)

app = Flask(__name__)
gene_suggest_api = Api(app)
gene_suggest_api.add_resource(Gene, '/gene_suggest', methods=['GET'])


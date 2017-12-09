import app
import unittest
from unittest import TestCase
import json
import os

class GeneSuggestTestCase(TestCase):
	
	BASE_URL = '/gene_suggest'

	def setUp(self):
		self.app = app.app.test_client()
		self.app.testing = True
		self.limit = 10

	def tearDown(self):
		pass

	def test_gene_suggest_valid_request(self):		
		req_paras = '?query=BR&species=homo_sapiens&limit=%d' % self.limit
		print "*"*50
		print "REQUEST:\n\tGET /gene_suggest" + req_paras
		rv = self.app.get(self.BASE_URL + req_paras)
		resp_satus_code = rv.status_code
		self.assertEqual(resp_satus_code,200)
		resp_data = json.loads(rv.data)
		print "RESPONSE :"
		print "\tStatus Code :", resp_satus_code
		print "\t", rv.data
		no_of_data = len(resp_data['gene_names'])		
		self.assertLessEqual(no_of_data,self.limit)

	def test_missing_species_in_request_params(self):
		req_paras = '?query=BR&limit=%d' % self.limit
		print "*"*50
		print "----MISSING SPECIES----"
		print "REQUEST:\n\tGET /gene_suggest" + req_paras
		rv = self.app.get(self.BASE_URL + req_paras)
		resp_satus_code = rv.status_code
		print "RESPONSE :"
		print "\tStatus Code :", resp_satus_code
		print "\t", rv.data
		self.assertEqual(resp_satus_code,400)

	def test_missing_query_in_request_params(self):
		req_paras = '?species=homo_sapiens&limit=%d' % self.limit
		print "*"*50
		print "----MISSING QUERY----"
		print "REQUEST:\n\tGET /gene_suggest" + req_paras		
		rv = self.app.get(self.BASE_URL + req_paras)
		resp_satus_code = rv.status_code
		print "RESPONSE :"
		print "\tStatus Code :", resp_satus_code
		print "\t", rv.data
		self.assertEqual(resp_satus_code,400)

	def test_missing_species_nd_query_in_request_params(self):
		req_paras = '?limit=%d' % self.limit
		print "*"*50
		print "----MISSING SPECIES and QUERY----"
		print "REQUEST:\n\tGET /gene_suggest" + req_paras				
		rv = self.app.get(self.BASE_URL + req_paras)
		resp_satus_code = rv.status_code
		self.assertEqual(resp_satus_code,400)

	def test_post_not_allowed(self):
		req_paras = '?query=BR&species=homo_sapiens&limit=%d' % self.limit
		print "*"*50
		print "----POST Not allowed----"
		print "REQUEST:\n\tPOST /gene_suggest" + req_paras				
		rv = self.app.post(self.BASE_URL + req_paras)		
		resp_satus_code = rv.status_code		
		print "RESPONSE :"
		print "\tStatus Code :", resp_satus_code
		print "\t", rv.data
		self.assertEqual(resp_satus_code,405)

	def test_put_not_allowed(self):
		req_paras = '?query=BR&species=homo_sapiens&limit=%d' % self.limit
		print "*"*50
		print "----PUT Not allowed----"
		print "REQUEST:\n\tPUT /gene_suggest" + req_paras				
		rv = self.app.put(self.BASE_URL + req_paras)
		resp_satus_code = rv.status_code
		print "RESPONSE :"
		print "\tStatus Code :", resp_satus_code
		print "\t", rv.data
		self.assertEqual(resp_satus_code,405)

	def test_delete_not_allowed(self):
		req_paras = '?query=BR&species=homo_sapiens&limit=%d' % self.limit
		print "*"*50
		print "----DELETE Not allowed----"
		print "REQUEST:\n\tDELETE /gene_suggest" + req_paras						
		rv = self.app.delete(self.BASE_URL + req_paras)
		resp_satus_code = rv.status_code		
		print "RESPONSE :"
		print "\tStatus Code :", resp_satus_code
		print "\t", rv.data
		self.assertEqual(resp_satus_code,405)		

if __name__ == '__main__':
	unittest.main()
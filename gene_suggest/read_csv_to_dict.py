import os
import csv

db_config = {}
gsa_home = os.environ.get('GSA_HOME')
if gsa_home is not None:
	dbs_path = os.path.join(gsa_home,"settings","db_settings.csv")
	if os.path.exists(dbs_path):
		with open(dbs_path) as dbsf:
			dbs_reader = csv.DictReader(dbsf)
			db_config = dbs_reader.next()
	else:
		print "Error : Could not find db_settings.csv"
		print "\tMake sure that you running application from gene_suggest directory."
		print "\tIf you are running from gene_suggest directory then check if settings/db_settings.csv exists?"
else:
	dbs_path = os.path.join("settings","db_settings.csv")	
	if os.path.exists(dbs_path):
		with open(dbs_path) as dbsf:
			dbs_reader = csv.DictReader(dbsf)
			db_config = dbs_reader.next()
	else:
		print "Error : Could not find db_settings.csv"
		print "\tMake sure that you running application from gene_suggest directory."
		print "\tIf you are running from gene_suggest directory then check if settings/db_settings.csv exists?"

#print "GSA_HOME environment variable not set. Set GSA_HOME and run appliction again"
#print "To set GSA_HOME type export GSA_HOME=<app_home_directory>"

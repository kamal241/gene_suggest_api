import sys
import os
from app import app

if __name__ == '__main__':
	port = '5000'
	gsa_home = None
	if len(sys.argv) == 2:
		port = sys.argv[1]
	app.run(port=port)

	
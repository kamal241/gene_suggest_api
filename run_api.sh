#!/bin/bash

port=5000
if [ $# -eq 0 ]; then
	echo "Using default port $port"
else
	port=$1
	echo "Application is runnung on port $port"
fi


venvdir=gsa_dtest
gsadir=gene_suggest
if [ -d "$gsadir" ]; then
	if [ -d "$venvdir" ]; then
		source ./gsa_dtest/bin/activate
		cd gene_suggest
		python run.py $port
	else
		echo "It seems that virtual environment does not exist"
		echo "Either run setup_api.sh or Follow the steps as per SETUP_API.md"		
	fi
else
	echo "gene_suggest_api does not Exists"
	echo "Either clone from git or download"
	echo "To clone type git clone https://github.com/kamal241/gene_suggest.git"
	echo "To Download zip https://github.com/kamal241/gene_suggest.git and download zip and extract it"
fi

import re
import os
import sys
import gzip

import numpy as np
import pandas as pd
from Bio import Entrez, Medline
from urllib.request import urlopen, urlretrieve

from hits_list import hits

HOMEDIR = os.getcwd()

def parse_soft(softzip):
	print("Softzip:", softzip)
	fin = gzip.open(softzip, 'r')

	results = {}
	suppfiles = []
	platform = ''
	
	data = fin.read().splitlines()
	data = [i.decode("utf-8") for i in data]

	for i,line in enumerate(data):
		if line.startswith('!Platform_title'):
				print("Found Platform!")
				index = line.find('= ')
				platform = str(line[index+2:])
				break

	for j,line in enumerate(data[:i]):
		if line.startswith('!Series_supplementary_file'):
				print("Found Supplementary!")
				index = line.find('= ')
				suppfiles.append("https" + line[index+5:].strip())
				break

	results['platform'] = platform.strip()
	results['suppfiles'] = suppfiles 

	return results

def dl_geo(data):

	for item in data:
		if item['suppfile'] != "":
			raw_data = "https://ftp.ncbi.nlm.nih.gov/geo/series/" + "GSE" + str(item['gse'][:-3]) + "nnn/GSE" + str(item['gse']) + "/suppl/"
		else:   
			raw_data = ''
		
		uniqueid =  "GSE" + str(item['gse'])
		newdir = HOMEDIR + "/" + uniqueid + "/"
		
		# Skip item if directory already exists
		if os.path.isdir(newdir) == True:
			print("Skipped " + uniqueid)
		
		else:
			os.makedirs(newdir) 
			print("uniqueid:", uniqueid)
			save_soft =	newdir + uniqueid + "_family.soft.gz"
			print("URL retrieve:", urlretrieve(item['soft_file'], save_soft))

			if urlretrieve(item['soft_file'], save_soft):
				print("Saved Soft!")
				soft_res = parse_soft(save_soft)
				print(soft_res)
				
				if raw_data != '':
					save_raw = newdir + uniqueid + "_RAW.tar"
					print("RAW data:", raw_data)
				
					for supf in soft_res['suppfiles']:
						print("supf:", supf)
						if supf != '':
							if urlretrieve(supf, newdir + supf.split("/")[-1]):
								print("supf:", supf)
								print(supf.split("/")[-1])
								urlretrieve(supf, newdir + supf.split("/")[-1])
	
				if item['platform'] == '':
					platf_name = soft_res['platform']
				else:
					platf_name = item['platform']
				
				geo_results = "GSE ID: " + str(item['gse']) + '\n' + \
								"PubDate: " + str(item['pubdate']) + '\n' + \
								"Number of Samples: " + str(item['n_samples']) + '\n' + \
								"Title: " + item['title'] + '\n' + \
								"Taxonomy: " + item['taxon'] + '\n' + \
								"PubMed: " + str(item['pubmed_ids']) + '\n' + \
								"SOFT downloaded from: " + item['soft_file'] + '\n' + \
								"Platform: " + platf_name + '\n' + \
								"Raw Data downloaded from: " + raw_data + "\n"
				filename = uniqueid + ".txt"
				f = open(newdir+filename, 'w')
				f.write(geo_results)
				f.close()
				os.chdir(HOMEDIR)
					
dl_geo(hits)
import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings("ignore")

def get_val(j):
	try:
		return int(j[1:-1])
	except:
		return (j[1:-1]) 

def get_mapping():
	df = pd.read_csv("../datasets/combined_annot.csv", index_col=0)
	
	id_list = list(df["ID"])
	geneid_list = list(df["Gene ID"])
	geneid_list = [[get_val(j) for j in i.replace("[", "").replace("]", "").split(", ")] for i in geneid_list]

	mapping = {}
	exclude_mapping = {}

	for i,j in zip(id_list, geneid_list):
		if j == [""]:
			exclude_mapping[i] = ""
		else:
			mapping[i] = min(j)

	print("Number of IDs excluded:", len(exclude_mapping))
	print("Number of genes mapped:", len(mapping))
	print("Number of unique gene IDs:", len(set(list(mapping.values()))))

	return mapping, exclude_mapping

if __name__ == "__main__":
	get_mapping()

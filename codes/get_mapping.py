import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings("ignore")

def get_val(j):
	try:
		return int(j[1:-1])
	except:
		return (j[1:-1]) 

def get_mapping(flag=False):
	df = pd.read_csv("../datasets/combined_annot.csv", index_col=0)
	
	id_list = list(df["ID"])
	geneid_list = list(df["Gene ID"])
	geneid_list = [[get_val(j) for j in i.replace("[", "").replace("]", "").split(", ")] for i in geneid_list]

	mapping = {}
	exclude_mapping = {}

	for i,j in zip(id_list, geneid_list):
		if j == [""]:
			exclude_mapping[i] = np.nan
		else:
			if len(j) == 1:
				mapping[i] = j[0]
			else:
				mapping[i] = "_".join(str(i) for i in tuple(frozenset(j)))

	if flag:
		values = mapping.values()
		set_values = [i for i in values]

		print("Number of IDs excluded:", len(exclude_mapping))
		print("Number of genes mapped:", len(mapping))
		print("Number of unique gene IDs:", len(set(set_values)))

	return mapping, exclude_mapping

if __name__ == "__main__":
	mapping, _ = get_mapping(True)
	for i,j in enumerate(mapping):
		print(j, mapping[j])
		if i>10:
			break

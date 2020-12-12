import numpy as np
import pandas as pd
from tqdm import tqdm

def get_annot(fname):
	fin = open("../datasets/"+fname)
	data = fin.read().splitlines()
	fin.close()

	pos = data.index("!platform_table_begin")

	data_section = data[pos+1:-1]
	split_data = [i.split("\t") for i in data_section]
	df = pd.DataFrame(split_data[1:], columns=split_data[0])

	list_to_split = ["Gene title", "Gene symbol", "Gene ID", "Chromosome annotation", "GO:Function", "GO:Component", "GO:Function ID", "GO:Process ID", "GO:Component ID"]
	for i in list_to_split:
		df[i] = df[i].str.split("///")
	
	return df

if __name__ == "__main__":
	fnames = ["GPL96.annot", "GPL570.annot"]
	df_list = []

	print("="*50)
	print("Getting the annotation files ...")
	for fname in tqdm(fnames):
		df = get_annot(fname)
		df_list.append(df)

	print("Annotation Shape 1:", df_list[0].shape, "\nAnnotation Shape 2:", df_list[1].shape)

	a = list(df_list[0]["ID"])
	b = list(df_list[1]["ID"])

	print("\nGetting the exclusive records from the smaller dataframe ...")
	exclusive_a = [i for i in tqdm(a) if i not in b]
	print("The Exclusive IDs are:")
	for i in exclusive_a:
		print(i)
	print("Number of exclusive IDs belonging to the smaller dataframe:", len(exclusive_a))

	a = df_list[0].to_dict('record')
	b = df_list[1].to_dict('record')

	for i in a:
		if i["ID"] in exclusive_a:
			b.append(i)

	df_new = pd.DataFrame(b)
	df_new.to_csv("../datasets/combined_annot.csv")
	print("\nCombined Annotation Shape:", df_new.shape)
	print("Saved the Combined annotation file as combined_annot.csv in datasets folder :)")
	print("Done")
	print("="*50)
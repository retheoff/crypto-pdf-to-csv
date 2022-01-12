
import numpy as np
from tabula import read_pdf
import pandas as pd

header_names = ['Date', 'Asset', 'Amount', 'Value (USD)', 'Type', 'Description']

def convert(source_filename, destination_filename):
	df_list = read_pdf(source_filename, pages=list(range(32,63)))
	for df in df_list:
		try:
			df.columns = header_names
		except Exception as e:
			df.columns = header_names[:-1]
			df['Description'] = ['' for _ in df['Date']]
	df = pd.concat(df_list)
	df.to_csv(destination_filename)


if __name__ == '__main__':
	convert('dumb-pdf.pdf', 'output.csv')


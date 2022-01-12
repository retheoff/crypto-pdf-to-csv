
from tabula import read_pdf
import pandas as pd

header_names = ['Date', 'Asset', 'Amount', 'Value (USD)', 'Type', 'Description']

def convert(source_filename, destination_filename, page_start, page_stop):
	df_list = read_pdf(source_filename, pages=list(range(page_start, page_stop+1)))
	for df in df_list:
		if len(df.columns) < len(header_names):
			df.columns = header_names[:-1]
			df['Description'] = ['' for _ in df['Date']]
		else:
			df.columns = header_names
	df = pd.concat(df_list)
	df.to_csv(destination_filename)


if __name__ == '__main__':
	convert(
		source_filename='dumb-pdf.pdf',
		destination_filename='output.csv',
		page_start=32,
		page_stop=62
	)


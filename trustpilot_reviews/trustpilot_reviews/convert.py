import pandas as pd

'''Converts given csv file to xlsx'''

read_file = pd.read_csv (r'trustpilot.csv')
read_file.to_excel (r'trustpilot.xlsx', index = None, header=True)
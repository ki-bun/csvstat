#!/usr/bin/env python

try:
	import pandas as pd
except ImportError:
	raise SystemExit("Missing dependency: pandas. Install with 'pip install pandas'")
import sys

if len(sys.argv) > 2:
	print("Only one argument is allowed.")
	exit
else: 
	csv = sys.argv[1]

	if csv.endswith('.csv'):
		df = pd.read_csv(csv)

		# Show list of headers
		print("CSV headers: \n")

		for index, i in enumerate(df.columns):
			print(f"{index} {i}")
		
		user_input = input("\nSelect header to examine: ")
		selected_header = df[df.columns[int(user_input)]]

		line = "_" * 40 + "\n"
		print(line)

		print(f"	Examining '{df.columns[int(user_input)].upper()}'\n")
		
		print(line)
		print(f"""{line}
{selected_header.head()}
\n{line}
{selected_header.describe()}
\n{line}
{selected_header.info()}
\n{line}
{selected_header.value_counts()}\n""")
	else:
		print("File must be a CSV")
		exit

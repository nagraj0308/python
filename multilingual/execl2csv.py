import pandas as pd

read_file = pd.read_excel("strings_in.xlsx")

read_file.to_csv("strings_out.csv",
                 index=None,
                 header=True)

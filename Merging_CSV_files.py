import pandas as pd
import zipfile as zf
import io
import os
from srcread import SRCRead


zipFile = SRCRead('source.txt')
zip_csv_file = zipFile.findPath('zip_file_path')

dataframes = []

with zf.ZipFile(zip_csv_file, 'r') as zip_ref:
    for file_name in zip_ref.namelist():
        if file_name.endswith('.csv'):
            with zip_ref.open(file_name) as csvfile:
                df = pd.read_csv(csvfile)
                dataframes.append(df)

merged_df = pd.concat(dataframes, axis=1)

output_buffer = io.StringIO()

merged_df.to_csv(output_buffer, index=False)

output_buffer.flush()

output_file_path = 'merged_output.csv' 

with open(output_file_path, 'w') as f:
    f.write(output_buffer.getvalue())

output_buffer.close()






















# first_file = True

# with zf.ZipFile(zip_csv_file, 'r') as zip_ref:
#     for file_name in zip_ref.namelist():
#         if file_name.endswith('.csv'):
#             with zip_ref.open(file_name) as csvfile:
#                 df = pd.read_csv(csvfile)                
#                 if first_file:
#                     df.to_csv(output_buffer, index=False)
#                     first_file = False
#                 else:
#                     df.iloc[:, 1:].to_csv(output_buffer, index=False, header=False)

# output_buffer.flush()

# output_file_path = 'merged_output.csv'  

# with open(output_file_path, 'w') as f:
#     f.write(output_buffer.getvalue())

# output_buffer.close()

import pandas as pd
import zipfile as zf
import io
from srcread import SRCRead

zipFile = SRCRead('source.txt')
zip_csv_file = zipFile.findPath('zip_file_path')

output_buffer = io.StringIO()

merged_df = None 

with zf.ZipFile(zip_csv_file, 'r') as zip_ref:
    for file_name in zip_ref.namelist():
        if file_name.endswith('.csv'):
            with zip_ref.open(file_name) as csvfile:
                df = pd.read_csv(csvfile)
                
                if merged_df is None:
                    merged_df = df
                else:
                    
                    merged_df = pd.concat([merged_df, df.iloc[:, 1:]], axis=1)

merged_df.to_csv(output_buffer, index=False)

output_file_path = 'merged_output.csv'

with open(output_file_path, 'w') as f:
    f.write(output_buffer.getvalue())

output_buffer.close()

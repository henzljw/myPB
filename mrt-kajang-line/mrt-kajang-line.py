# mrt-kajang-line.py
# Generate MRT Kajang line datasets in CSV output file format


# Import Python libraries
import pandas as pds
from datasets import generateDatasets

# Get datasets from generateDatasets() at datasets.py
getDatasets = generateDatasets()

# Convert datasets into Panda DataFrame
DataFrameConversion = pds.DataFrame(getDatasets)

# Fill missing values for any column(s) that declared from datasets.py
DataFrameConversion['station_code'] = DataFrameConversion['station_code'].fillna('N/A')
DataFrameConversion['station_name'] = DataFrameConversion['station_name'].fillna('N/A')
DataFrameConversion['working_name'] = DataFrameConversion['working_name'].fillna('N/A')
DataFrameConversion['provisional_station'] = DataFrameConversion['provisional_station'].fillna('N/A')
DataFrameConversion['shelved_station'] = DataFrameConversion['shelved_station'].fillna('N/A')
DataFrameConversion['park_and_ride'] = DataFrameConversion['park_and_ride'].fillna('N/A')
DataFrameConversion['malls'] = DataFrameConversion['malls'].fillna('N/A')
DataFrameConversion['tourist_attractions'] = DataFrameConversion['tourist_attractions'].fillna('N/A')
DataFrameConversion['hospitals'] = DataFrameConversion['hospitals'].fillna('N/A')
DataFrameConversion['universities'] = DataFrameConversion['universities'].fillna('N/A')
DataFrameConversion['government_agencies'] = DataFrameConversion['government_agencies'].fillna('N/A')
DataFrameConversion['cafes'] = DataFrameConversion['cafes'].fillna('N/A')

# Save as CSV output file format
DataFrameConversion.to_csv('mrt-kajang-line.csv', index=False)

# Print successful message in the output console
print('mrt-kajang-line.csv is successfully generated.')

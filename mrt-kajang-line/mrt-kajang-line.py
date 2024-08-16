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
DataFrameConversion['station_code'] = DataFrameConversion['station_code'].fillna('-')
DataFrameConversion['station_name'] = DataFrameConversion['station_name'].fillna('-')
DataFrameConversion['working_name'] = DataFrameConversion['working_name'].fillna('N/A')
DataFrameConversion['provisional_station'] = DataFrameConversion['provisional_station'].fillna('No')
DataFrameConversion['shelved_station'] = DataFrameConversion['shelved_station'].fillna('No')
DataFrameConversion['elevated_station'] = DataFrameConversion['elevated_station'].fillna('No')
DataFrameConversion['underground_station'] = DataFrameConversion['underground_station'].fillna('No')
DataFrameConversion['transit_hub_station'] = DataFrameConversion['transit_hub_station'].fillna('No')
DataFrameConversion['interchange_stations'] = DataFrameConversion['interchange_stations'].fillna('N/A')
DataFrameConversion['connecting_stations'] = DataFrameConversion['connecting_stations'].fillna('N/A')
DataFrameConversion['connecting_rail_lines'] = DataFrameConversion['connecting_rail_lines'].fillna('N/A')
DataFrameConversion['connecting_bus_lines'] = DataFrameConversion['connecting_bus_lines'].fillna('N/A')
DataFrameConversion['feeder_bus'] = DataFrameConversion['feeder_bus'].fillna('N/A')
DataFrameConversion['park_and_ride'] = DataFrameConversion['park_and_ride'].fillna('No')
DataFrameConversion['malls'] = DataFrameConversion['malls'].fillna('N/A')
DataFrameConversion['hypermarkets'] = DataFrameConversion['hypermarkets'].fillna('N/A')
DataFrameConversion['tourist_attractions'] = DataFrameConversion['tourist_attractions'].fillna('N/A')
DataFrameConversion['hospitals'] = DataFrameConversion['hospitals'].fillna('N/A')
DataFrameConversion['universities'] = DataFrameConversion['universities'].fillna('N/A')
DataFrameConversion['colleges'] = DataFrameConversion['colleges'].fillna('N/A')
DataFrameConversion['government_agencies'] = DataFrameConversion['government_agencies'].fillna('N/A')
DataFrameConversion['cafes'] = DataFrameConversion['cafes'].fillna('N/A')
DataFrameConversion['parks'] = DataFrameConversion['parks'].fillna('N/A')
DataFrameConversion['botanical_gardens'] = DataFrameConversion['botanical_gardens'].fillna('N/A')
DataFrameConversion['stadium'] = DataFrameConversion['stadium'].fillna('N/A')

# Save as CSV output file format
DataFrameConversion.to_csv('mrt-kajang-line-KG.csv', index=False)

# Print successful message in the output console
print('mrt-kajang-line-KG.csv is successfully generated.')

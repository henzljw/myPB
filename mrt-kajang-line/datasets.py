# datasets.py
# Dataset(s) of MRT Kajang line

# Dataset(s)
# 
# Please use the provided guidelines to insert dataset as attached below
# 
# {
#     'station_code': '', 
#     'station_name': '',
#     'working_name': '',
#     'provisional_station': None,
#     'shelved_station': None,
#     'elevated_station': None,
#     'underground_station': None,
#     'transit_hub_station': None,
#     'interchange_stations': None,
#     'connecting_stations': None,
#     'connecting_rail_lines': None,
#     'connecting_bus_lines': None,
#     'feeder_bus': None,
#     'park_and_ride': None,
#     'malls': None,
#     'hypermarkets': None,
#     'tourist_attractions': None,
#     'hospitals': None,
#     'universities': None,
#     'colleges': None,
#     'government_agencies': None,
#     'cafes': None,
#     'parks': None,
#     'botanical_gardens': None,
#     'stadium': None,
# },
# 
# Note: The above guidelines will change at anytime so should be ensure that all below datasets are
#       sync together with the guidelines that set on the top

datasets = [
    {
        'station_code': 'KG04', 
        'station_name': 'Kwasa Damansara',
        'working_name': 'Kota Damansara',
        'provisional_station': None,
        'shelved_station': None,
        'elevated_station': 'Yes',
        'underground_station': None,
        'transit_hub_station': None,
        'interchange_stations': 'PY01 Kwasa Damansara [MRT Putrajaya Line]',
        'connecting_stations': None,
        'connecting_rail_lines': 'MRT Putrajaya Line',
        'connecting_bus_lines': None,
        'feeder_bus': None,
        'park_and_ride': 'Yes',
        'malls': None,
        'hypermarkets': None,
        'tourist_attractions': None,
        'hospitals': None,
        'universities': None,
        'colleges': None,
        'government_agencies': 'Menara KWSP',
        'cafes': None,
        'parks': None,
        'botanical_gardens': None,
        'stadium': None,
    },
    {
        'station_code': 'KG05', 
        'station_name': 'Kwasa Sentral',
        'working_name': 'Taman Industri Sungai Buloh',
        'provisional_station': None,
        'shelved_station': None,
        'elevated_station': 'Yes',
        'underground_station': None,
        'transit_hub_station': None,
        'interchange_stations': None,
        'connecting_stations': None,
        'connecting_rail_lines': None,
        'connecting_bus_lines': "T772, T801, T802, T803, T804",
        'feeder_bus': 'T804 feeder bus to KS03 Terminal Skypark [KTM KL Sentral-Terminal Skypark Line]',
        'park_and_ride': 'Yes',
        'malls': None,
        'hypermarkets': None,
        'tourist_attractions': None,
        'hospitals': None,
        'universities': None,
        'colleges': None,
        'government_agencies': 'Rubber Research Institute of Malaysia (RRIM) Research Station',
        'cafes': None,
        'parks': None,
        'botanical_gardens': None,
        'stadium': None,
    },
    {
        'station_code': 'KG05A', 
        'station_name': 'Teknologi',
        'working_name': None,
        'provisional_station': 'Yes',
        'shelved_station': None,
        'elevated_station': None,
        'underground_station': None,
        'transit_hub_station': None,
        'interchange_stations': None,
        'connecting_stations': None,
        'connecting_rail_lines': None,
        'connecting_bus_lines': None,
        'feeder_bus': None,
        'park_and_ride': None,
        'malls': None,
        'hypermarkets': None,
        'tourist_attractions': None,
        'hospitals': None,
        'universities': None,
        'colleges': None,
        'government_agencies': None,
        'cafes': None,
        'parks': None,
        'botanical_gardens': None,
        'stadium': None,
    },
    {
        'station_code': 'KG06', 
        'station_name': 'Kota Damansara-Thomson Hospital',
        'working_name': 'PJU5',
        'provisional_station': None,
        'shelved_station': None,
        'elevated_station': 'Yes',
        'underground_station': None,
        'transit_hub_station': None,
        'interchange_stations': None,
        'connecting_stations': None,
        'connecting_rail_lines': None,
        'connecting_bus_lines': "T805, 780",
        'feeder_bus': None,
        'park_and_ride': None,
        'malls': None,
        'hypermarkets': None,
        'tourist_attractions': None,
        'hospitals': 'Thomson Hospital',
        'universities': 'SEGi University',
        'colleges': None,
        'government_agencies': None,
        'cafes': None,
        'parks': None,
        'botanical_gardens': None,
        'stadium': None,
    },
    {
        'station_code': 'KG07', 
        'station_name': 'Surian',
        'working_name': 'Dataran Sunway',
        'provisional_station': None,
        'shelved_station': None,
        'elevated_station': 'Yes',
        'underground_station': None,
        'transit_hub_station': None,
        'interchange_stations': None,
        'connecting_stations': None,
        'connecting_rail_lines': None,
        'connecting_bus_lines': "T807, T808, 780, 802",
        'feeder_bus': 'T807 feeder bus to KJ25 Lembah Subang [LRT Kelana Jaya Line]',
        'park_and_ride': None,
        'malls': "Tropicana Gardens Mall, Sunway Giza Mall",
        'hypermarkets': None,
        'tourist_attractions': None,
        'hospitals': None,
        'universities': None,
        'colleges': None,
        'government_agencies': None,
        'cafes': None,
        'parks': None,
        'botanical_gardens': None,
        'stadium': None,
    },
    {
        'station_code': 'KG08', 
        'station_name': 'Mutiara Damansara',
        'working_name': 'The Curve',
        'provisional_station': None,
        'shelved_station': None,
        'elevated_station': 'Yes',
        'underground_station': None,
        'transit_hub_station': None,
        'interchange_stations': None,
        'connecting_stations': None,
        'connecting_rail_lines': None,
        'connecting_bus_lines': "T809, T810, PJ06, 780, 801, 802",
        'feeder_bus': None,
        'park_and_ride': None,
        'malls': "IPC Shopping Centre, IKEA Damansara",
        'hypermarkets': 'Lotus Mutiara Damansara',
        'tourist_attractions': None,
        'hospitals': None,
        'universities': None,
        'colleges': None,
        'government_agencies': None,
        'cafes': None,
        'parks': None,
        'botanical_gardens': None,
        'stadium': None,
    },
    {
        'station_code': 'KG09', 
        'station_name': 'Bandar Utama',
        'working_name': 'One Utama',
        'provisional_station': None,
        'shelved_station': None,
        'elevated_station': 'Yes',
        'underground_station': None,
        'transit_hub_station': None,
        'interchange_stations': '(In Construction) SA01 Bandar Utama [LRT Shah Alam Line]',
        'connecting_stations': None,
        'connecting_rail_lines': '(In Construction) LRT Shah Alam Line',
        'connecting_bus_lines': "T811, T812, PJ05, PJ06, 780, 802",
        'feeder_bus': None,
        'park_and_ride': 'Yes',
        'malls': '1 Utama Shopping Centre',
        'hypermarkets': None,
        'tourist_attractions': None,
        'hospitals': None,
        'universities': None,
        'colleges': None,
        'government_agencies': None,
        'cafes': None,
        'parks': None,
        'botanical_gardens': None,
        'stadium': None,
    },
    {
        'station_code': 'KG10', 
        'station_name': 'Taman Tun Dr Ismail - Deloitte (TTDI)',
        'working_name': 'TTDI',
        'provisional_station': None,
        'shelved_station': None,
        'elevated_station': 'Yes',
        'underground_station': None,
        'transit_hub_station': None,
        'interchange_stations': None,
        'connecting_stations': None,
        'connecting_rail_lines': None,
        'connecting_bus_lines': "T813, T814",
        'feeder_bus': None,
        'park_and_ride': None,
        'malls': 'Glo Damansara Shopping Mall',
        'hypermarkets': None,
        'tourist_attractions': None,
        'hospitals': 'KPJ Damansara Specialist Hospital',
        'universities': None,
        'colleges': None,
        'government_agencies': None,
        'cafes': None,
        'parks': None,
        'botanical_gardens': None,
        'stadium': None,
    },
    {
        'station_code': 'KG11', 
        'station_name': 'Seksyen 17',
        'working_name': None,
        'provisional_station': None,
        'shelved_station': 'Yes',
        'elevated_station': None,
        'underground_station': None,
        'transit_hub_station': None,
        'interchange_stations': None,
        'connecting_stations': None,
        'connecting_rail_lines': None,
        'connecting_bus_lines': None,
        'feeder_bus': None,
        'park_and_ride': None,
        'malls': None,
        'hypermarkets': None,
        'tourist_attractions': None,
        'hospitals': None,
        'universities': None,
        'colleges': None,
        'government_agencies': None,
        'cafes': None,
        'parks': None,
        'botanical_gardens': None,
        'stadium': None,
    },
    {
        'station_code': 'KG12', 
        'station_name': 'Phileo Damansara',
        'working_name': 'Seksyen 16',
        'provisional_station': None,
        'shelved_station': None,
        'elevated_station': 'Yes',
        'underground_station': None,
        'transit_hub_station': None,
        'interchange_stations': None,
        'connecting_stations': None,
        'connecting_rail_lines': None,
        'connecting_bus_lines': "T815, T816",
        'feeder_bus': 'T815 feeder bus to Universiti Malaya (UM)',
        'park_and_ride': 'Yes',
        'malls': None,
        'hypermarkets': None,
        'tourist_attractions': None,
        'hospitals': None,
        'universities': 'Universiti Malaya (UM)',
        'colleges': None,
        'government_agencies': None,
        'cafes': None,
        'parks': None,
        'botanical_gardens': None,
        'stadium': None,
    },
    {
        'station_code': 'KG12A', 
        'station_name': 'Bukit Kiara Selatan',
        'working_name': None,
        'provisional_station': 'Yes',
        'shelved_station': None,
        'elevated_station': None,
        'underground_station': None,
        'transit_hub_station': None,
        'interchange_stations': None,
        'connecting_stations': None,
        'connecting_rail_lines': None,
        'connecting_bus_lines': None,
        'feeder_bus': None,
        'park_and_ride': None,
        'malls': None,
        'hypermarkets': None,
        'tourist_attractions': None,
        'hospitals': None,
        'universities': None,
        'colleges': None,
        'government_agencies': None,
        'cafes': None,
        'parks': None,
        'botanical_gardens': None,
        'stadium': None,
    },
    {
        'station_code': 'KG13', 
        'station_name': 'Pavilion Damansara Heights - Pusat Bandar Damansara',
        'working_name': "Pusat Bandar Damansara, Damansara City Mall (DC Mall)",
        'provisional_station': None,
        'shelved_station': None,
        'elevated_station': 'Yes',
        'underground_station': None,
        'transit_hub_station': None,
        'interchange_stations': None,
        'connecting_stations': None,
        'connecting_rail_lines': None,
        'connecting_bus_lines': "T817",
        'feeder_bus': 'T817 feeder bus to KB01 Mid Valley [KTM Batu Caves-Pulau Sebang Line]',
        'park_and_ride': 'Yes',
        'malls': 'Pavilion Damansara Heights Mall',
        'hypermarkets': None,
        'tourist_attractions': None,
        'hospitals': None,
        'universities': None,
        'colleges': None,
        'government_agencies': None,
        'cafes': None,
        'parks': None,
        'botanical_gardens': None,
        'stadium': None,
    },
    {
        'station_code': 'KG14', 
        'station_name': 'Semantan',
        'working_name': 'Semantan',
        'provisional_station': None,
        'shelved_station': None,
        'elevated_station': 'Yes',
        'underground_station': None,
        'transit_hub_station': None,
        'interchange_stations': None,
        'connecting_stations': None,
        'connecting_rail_lines': None,
        'connecting_bus_lines': "T818, T819, T820, T821, T822",
        'feeder_bus': 'T819 feeder bus to Hilton Kuala Lumpur and KL Sentral',
        'park_and_ride': None,
        'malls': None,
        'hypermarkets': None,
        'tourist_attractions': None,
        'hospitals': None,
        'universities': "HELP university, Perdana University",
        'colleges': None,
        'government_agencies': None,
        'cafes': None,
        'parks': None,
        'botanical_gardens': None,
        'stadium': None,
    },
    {
        'station_code': 'KG15',
        'station_name': 'Muzium Negara',
        'working_name': 'KL Sentral',
        'provisional_station': None,
        'shelved_station': None,
        'elevated_station': None,
        'underground_station': 'Yes',
        'transit_hub_station': 'KL Sentral',
        'interchange_stations': None,
        'connecting_stations': "KA01 KL Sentral [KTM Batu Caves-Pulau Sebang Line & KTM Tanjung Malim-Port Klang Line], KS01 KL Sentral [KTM KL Sentral-Terminal Skypark Line], KJ15 KL Sentral [LRT Kelana Jaya Line], KE01 KL Sentral [ERL KLIA Ekspres Line], KT01 KL Sentral [ERL KLIA Transit Line], MR01 KL Sentral [KL Monorail Line]",
        'connecting_rail_lines': "KTM Batu Caves-Pulau Sebang Line, KTM Tanjung Malim-Port Klang Line, KTM KL Sentral-Terminal Skypark Line, KTM ETS Gemas-Padang Besar Line, LRT Kelana Jaya Line, ERL KLIA Ekspres Line, ERL KLIA Transit Line, KL Monorail Line",
        'connecting_bus_lines': "GOKL 03",
        'feeder_bus': None,
        'park_and_ride': None,
        'malls': 'Nu Sentral',
        'hypermarkets': None,
        'tourist_attractions': "Planetarium Negara, Masjid Negara, Stesen Keretapi Kuala Lumpur, Muzium Negara, Little India Brickfields, Tugu Negara",
        'hospitals': None,
        'universities': None,
        'colleges': None,
        'government_agencies': None,
        'cafes': None,
        'parks': "Perdana Botanical park, Taman Rama-Rama Kuala Lumpur",
        'botanical_gardens': 'Perdana Botanical Garden',
        'stadium': None,
    },
    {
        'station_code': 'KG16', 
        'station_name': 'Pasar Seni',
        'working_name': 'Pasar Seni',
        'provisional_station': None,
        'shelved_station': None,
        'elevated_station': None,
        'underground_station': 'Yes',
        'transit_hub_station': None,
        'interchange_stations': 'KJ14 Pasar Seni [LRT Kelana Jaya Line]',
        'connecting_stations': "KA02 Kuala Lumpur [KTM Batu Caves-Pulau Sebang Line & KTM Tanjung Malim-Port Klang Line], KTM ETS Gemas-Padang Besar via pedestrian bridge",
        'connecting_rail_lines': "LRT Kelana Jaya Line, KTM Batu Caves-Pulau Sebang Line, KTM Tanjung Malim-Port Klang Line, KTM ETS Gemas-Padang Besar Line",
        'connecting_bus_lines': "GOKL 02, 180, 600, 640, 650, 750, 751, 770, 772, 780, 782, 821, 851",
        'feeder_bus': None,
        'park_and_ride': None,
        'malls': None,
        'hypermarkets': None,
        'tourist_attractions': "Central Market, Petaling Street, Kwai Chai Hong, REXKL",
        'hospitals': None,
        'universities': None,
        'colleges': None,
        'government_agencies': None,
        'cafes': None,
        'parks': None,
        'botanical_gardens': None,
        'stadium': None,
    },
    {
        'station_code': 'KG17', 
        'station_name': 'Merdeka',
        'working_name': 'Merdeka',
        'provisional_station': None,
        'shelved_station': None,
        'elevated_station': None,
        'underground_station': 'Yes',
        'transit_hub_station': None,
        'interchange_stations': "AG08 Plaza Rakyat [LRT Ampang Line], SP08 Plaza Rakyat [LRT Sri Petaling Line]",
        'connecting_stations': None,
        'connecting_rail_lines': None,
        'connecting_bus_lines': None,
        'feeder_bus': None,
        'park_and_ride': None,
        'malls': None,
        'hypermarkets': None,
        'tourist_attractions': 'Merdeka 118',
        'hospitals': None,
        'universities': None,
        'colleges': None,
        'government_agencies': None,
        'cafes': None,
        'parks': None,
        'botanical_gardens': None,
        'stadium': 'Stadium Merdeka',
    },
    {
        'station_code': 'KG18A', 
        'station_name': 'Pavilion Kuala Lumpur-Bukit Bintang',
        'working_name': 'Bukit Bintang Sentral',
        'provisional_station': None,
        'shelved_station': None,
        'elevated_station': None,
        'underground_station': 'Yes',
        'transit_hub_station': None,
        'interchange_stations': None,
        'connecting_stations': 'MR06 Bukit Bintang [KL Monorail Line]',
        'connecting_rail_lines': "KL Monorail Line, LRT Kelana Jaya Line via Pavilion Bukit Bintang's elevated walkway",
        'connecting_bus_lines': "GOKL 01, GOKL 02, GOKL 04, 400, 420, 421, 580",
        'feeder_bus': None,
        'park_and_ride': None,
        'malls': "Pavilion Kuala Lumpur, Fahrenheit 88, Lot 10, Sungei Wang Plaza, Starhill Square, Plaza Low Yat",
        'hypermarkets': None,
        'tourist_attractions': 'Jalan Alor Food Street',
        'hospitals': None,
        'universities': None,
        'colleges': None,
        'government_agencies': None,
        'cafes': None,
        'parks': None,
        'botanical_gardens': None,
        'stadium': None,
    },
    {
        'station_code': 'KG20', 
        'station_name': 'Tun Razak Exchange-Samsung Galaxy (TRX)',
        'working_name': 'Pasar Rakyat',
        'provisional_station': None,
        'shelved_station': None,
        'elevated_station': None,
        'underground_station': 'Yes',
        'transit_hub_station': None,
        'interchange_stations': 'PY23 Tun Razak Exchange-Samsung Galaxy (TRX) [MRT Putrajaya Line]',
        'connecting_stations': None,
        'connecting_rail_lines': 'MRT Putrajaya Line',
        'connecting_bus_lines': "T407, 402",
        'feeder_bus': None,
        'park_and_ride': None,
        'malls': 'The Exchange TRX',
        'hypermarkets': None,
        'tourist_attractions': None,
        'hospitals': None,
        'universities': None,
        'colleges': None,
        'government_agencies': None,
        'cafes': None,
        'parks': None,
        'botanical_gardens': None,
        'stadium': None,
    },
    {
        'station_code': 'KG21', 
        'station_name': 'Cochrane',
        'working_name': 'Cochrane',
        'provisional_station': None,
        'shelved_station': None,
        'elevated_station': None,
        'underground_station': 'Yes',
        'transit_hub_station': None,
        'interchange_stations': None,
        'connecting_stations': None,
        'connecting_rail_lines': None,
        'connecting_bus_lines': "T352, T400, T401, GOKL 11, 420",
        'feeder_bus': 'T401 feeder bus to SP12 Cheras [LRT Sri Petaling Line]',
        'park_and_ride': None,
        'malls': "MyTOWN Shopping Centre, IKEA Cheras",
        'hypermarkets': None,
        'tourist_attractions': None,
        'hospitals': None,
        'universities': None,
        'colleges': None,
        'government_agencies': None,
        'cafes': None,
        'parks': None,
        'botanical_gardens': None,
        'stadium': None,
    },
    {
        'station_code': 'KG22', 
        'station_name': 'AEON - Maluri',
        'working_name': 'Maluri',
        'provisional_station': None,
        'shelved_station': None,
        'elevated_station': None,
        'underground_station': 'Yes',
        'transit_hub_station': None,
        'interchange_stations': 'AG13 Maluri [LRT Ampang Line]',
        'connecting_stations': None,
        'connecting_rail_lines': 'LRT Ampang Line',
        'connecting_bus_lines': "T352, T400, T401, GOKL 10, GOKL 11, 400, 402, 450",
        'feeder_bus': 'T401 feeder bus to SP12 Cheras [LRT Sri Petaling Line]',
        'park_and_ride': 'Yes',
        'malls': "AEON Mall Taman Maluri, Sunway Velocity Mall",
        'hypermarkets': None,
        'tourist_attractions': None,
        'hospitals': None,
        'universities': None,
        'colleges': None,
        'government_agencies': None,
        'cafes': None,
        'parks': None,
        'botanical_gardens': None,
        'stadium': None,
    },
    {
        'station_code': 'KG23', 
        'station_name': 'Taman Pertama',
        'working_name': 'Taman Bukit Ria',
        'provisional_station': None,
        'shelved_station': None,
        'elevated_station': 'Yes',
        'underground_station': None,
        'transit_hub_station': None,
        'interchange_stations': None,
        'connecting_stations': None,
        'connecting_rail_lines': None,
        'connecting_bus_lines': "T305, 400, 405",
        'feeder_bus': None,
        'park_and_ride': None,
        'malls': None,
        'hypermarkets': None,
        'tourist_attractions': None,
        'hospitals': None,
        'universities': None,
        'colleges': None,
        'government_agencies': None,
        'cafes': None,
        'parks': None,
        'botanical_gardens': None,
        'stadium': None,
    },
    {
        'station_code': 'KG24', 
        'station_name': 'Taman Midah',
        'working_name': 'Taman Bukit Mewah',
        'provisional_station': None,
        'shelved_station': None,
        'elevated_station': 'Yes',
        'underground_station': None,
        'transit_hub_station': None,
        'interchange_stations': None,
        'connecting_stations': None,
        'connecting_rail_lines': None,
        'connecting_bus_lines': "T305, T402, 400, 450",
        'feeder_bus': 'T402 feeder bus to SP13 Salak Selatan [LRT Sri Petaling line] & Hospital Canselor Tuanku Muhriz UKM',
        'park_and_ride': 'Yes',
        'malls': None,
        'hypermarkets': 'Lotus Cheras',
        'tourist_attractions': None,
        'hospitals': 'Hospital Canselor Tuanku Muhriz UKM',
        'universities': None,
        'colleges': None,
        'government_agencies': None,
        'cafes': None,
        'parks': None,
        'botanical_gardens': None,
        'stadium': None,
    },
    {
        'station_code': 'KG25', 
        'station_name': 'Taman Mutiara',
        'working_name': 'Leisure Mall',
        'provisional_station': None,
        'shelved_station': None,
        'elevated_station': 'Yes',
        'underground_station': None,
        'transit_hub_station': None,
        'interchange_stations': None,
        'connecting_stations': None,
        'connecting_rail_lines': None,
        'connecting_bus_lines': "T408, T409, 400, 450",
        'feeder_bus': None,
        'park_and_ride': None,
        'malls': "EkoCheras Mall, Cheras LeisureMall",
        'hypermarkets': None,
        'tourist_attractions': None,
        'hospitals': None,
        'universities': None,
        'colleges': None,
        'government_agencies': None,
        'cafes': None,
        'parks': None,
        'botanical_gardens': None,
        'stadium': None,
    },
    {
        'station_code': 'KG26', 
        'station_name': 'Taman Connaught',
        'working_name': 'Plaza Phoenix',
        'provisional_station': None,
        'shelved_station': None,
        'elevated_station': 'Yes',
        'underground_station': None,
        'transit_hub_station': None,
        'interchange_stations': None,
        'connecting_stations': None,
        'connecting_rail_lines': None,
        'connecting_bus_lines': "T410, T411, T412, 450",
        'feeder_bus': 'T410 feeder bus to KB04 Bandar Tasik Selatan [KTM Batu Caves-Pulau Sebang Line], SP15 Bandar Tasik Selatan [LRT Sri Petaling Line], KT02 Bandar Tasik Selatan [ERL KLIA Transit Line]',
        'park_and_ride': None,
        'malls': 'Cheras Sentral Mall',
        'hypermarkets': None,
        'tourist_attractions': None,
        'hospitals': None,
        'universities': 'UCSI university',
        'colleges': None,
        'government_agencies': None,
        'cafes': None,
        'parks': None,
        'botanical_gardens': None,
        'stadium': None,
    },
    {
        'station_code': 'KG27', 
        'station_name': 'Taman Suntex',
        'working_name': 'Taman Suntex',
        'provisional_station': None,
        'shelved_station': None,
        'elevated_station': 'Yes',
        'underground_station': None,
        'transit_hub_station': None,
        'interchange_stations': None,
        'connecting_stations': None,
        'connecting_rail_lines': None,
        'connecting_bus_lines': "T413, T406, 450",
        'feeder_bus': None,
        'park_and_ride': 'Yes',
        'malls': None,
        'hypermarkets': 'NSK Trade City Taman Suntex',
        'tourist_attractions': None,
        'hospitals': None,
        'universities': None,
        'colleges': None,
        'government_agencies': None,
        'cafes': None,
        'parks': None,
        'botanical_gardens': None,
        'stadium': None,
    },
    {
        'station_code': 'KG28', 
        'station_name': 'Sri Raya',
        'working_name': 'Taman Cuepacs',
        'provisional_station': None,
        'shelved_station': None,
        'elevated_station': 'Yes',
        'underground_station': None,
        'transit_hub_station': None,
        'interchange_stations': None,
        'connecting_stations': None,
        'connecting_rail_lines': None,
        'connecting_bus_lines': "T414, T406, 450",
        'feeder_bus': None,
        'park_and_ride': 'Yes',
        'malls': None,
        'hypermarkets': None,
        'tourist_attractions': None,
        'hospitals': None,
        'universities': None,
        'colleges': None,
        'government_agencies': None,
        'cafes': None,
        'parks': None,
        'botanical_gardens': None,
        'stadium': None,
    },
    {
        'station_code': 'KG29', 
        'station_name': 'Bandar Tun Hussein Onn',
        'working_name': 'Bandar Tun Hussein Onn',
        'provisional_station': None,
        'shelved_station': None,
        'elevated_station': 'Yes',
        'underground_station': None,
        'transit_hub_station': None,
        'interchange_stations': None,
        'connecting_stations': None,
        'connecting_rail_lines': None,
        'connecting_bus_lines': "T415, KJ03",
        'feeder_bus': None,
        'park_and_ride': 'Yes',
        'malls': None,
        'hypermarkets': None,
        'tourist_attractions': None,
        'hospitals': None,
        'universities': None,
        'colleges': None,
        'government_agencies': None,
        'cafes': None,
        'parks': None,
        'botanical_gardens': None,
        'stadium': None,
    },
    {
        'station_code': 'KG30', 
        'station_name': 'Batu 11 Cheras',
        'working_name': 'Balakong',
        'provisional_station': None,
        'shelved_station': None,
        'elevated_station': 'Yes',
        'underground_station': None,
        'transit_hub_station': None,
        'interchange_stations': None,
        'connecting_stations': None,
        'connecting_rail_lines': None,
        'connecting_bus_lines': "T416, T417, T569, 450, 590",
        'feeder_bus': None,
        'park_and_ride': None,
        'malls': None,
        'hypermarkets': None,
        'tourist_attractions': None,
        'hospitals': None,
        'universities': None,
        'colleges': None,
        'government_agencies': None,
        'cafes': None,
        'parks': None,
        'botanical_gardens': None,
        'stadium': None,
    },
    {
        'station_code': 'KG31', 
        'station_name': 'Bukit Dukung',
        'working_name': 'Taman Koperasi',
        'provisional_station': None,
        'shelved_station': None,
        'elevated_station': 'Yes',
        'underground_station': None,
        'transit_hub_station': None,
        'interchange_stations': None,
        'connecting_stations': None,
        'connecting_rail_lines': None,
        'connecting_bus_lines': "T453, T454, T455, 450",
        'feeder_bus': None,
        'park_and_ride': 'Yes',
        'malls': None,
        'hypermarkets': None,
        'tourist_attractions': None,
        'hospitals': None,
        'universities': 'Universiti Tunku Abdul Rahman (UTAR)',
        'colleges': None,
        'government_agencies': None,
        'cafes': None,
        'parks': None,
        'botanical_gardens': None,
        'stadium': None,
    },
    {
        'station_code': 'KG32', 
        'station_name': 'Taman Mesra',
        'working_name': None,
        'provisional_station': None,
        'shelved_station': 'Yes',
        'elevated_station': None,
        'underground_station': None,
        'transit_hub_station': None,
        'interchange_stations': None,
        'connecting_stations': None,
        'connecting_rail_lines': None,
        'connecting_bus_lines': None,
        'feeder_bus': None,
        'park_and_ride': None,
        'malls': None,
        'hypermarkets': None,
        'tourist_attractions': None,
        'hospitals': None,
        'universities': None,
        'colleges': None,
        'government_agencies': None,
        'cafes': None,
        'parks': None,
        'botanical_gardens': None,
        'stadium': None,
    },
    {
        'station_code': 'KG33', 
        'station_name': 'Sungai Jernih',
        'working_name': 'Saujana Impian',
        'provisional_station': None,
        'shelved_station': None,
        'elevated_station': 'Yes',
        'underground_station': None,
        'transit_hub_station': None,
        'interchange_stations': None,
        'connecting_stations': None,
        'connecting_rail_lines': None,
        'connecting_bus_lines': "T456, 450",
        'feeder_bus': None,
        'park_and_ride': 'Yes',
        'malls': None,
        'hypermarkets': 'Lotus Kajang',
        'tourist_attractions': None,
        'hospitals': 'KPJ Kajang Specialist Hospital',
        'universities': None,
        'colleges': None,
        'government_agencies': None,
        'cafes': None,
        'parks': None,
        'botanical_gardens': None,
        'stadium': None,
    },
    {
        'station_code': 'KG34', 
        'station_name': 'Stadium Kajang',
        'working_name': 'Bandar Kajang',
        'provisional_station': None,
        'shelved_station': None,
        'elevated_station': 'Yes',
        'underground_station': None,
        'transit_hub_station': None,
        'interchange_stations': None,
        'connecting_stations': None,
        'connecting_rail_lines': None,
        'connecting_bus_lines': "T450, T451, T457, T458, T459, T460, KJ01, 450",
        'feeder_bus': 'T451 feeder bus to Universiti Kebangsaan Malaysia via KB06 Kajang & KB07 UKM [KTM Batu Caves-Pulau Sebang Line]',
        'park_and_ride': None,
        'malls': "Plaza Metro Kajang, Metro Point Kajang",
        'hypermarkets': 'Mydin Mart Kajang',
        'tourist_attractions': None,
        'hospitals': 'Hospital Kajang',
        'universities': 'Universiti Kebangsaan Malaysia',
        'colleges': 'Kolej Vokasional Kajang',
        'government_agencies': None,
        'cafes': None,
        'parks': None,
        'botanical_gardens': None,
        'stadium': 'Stadium Kajang',
    },
    {
        'station_code': 'KG35', 
        'station_name': 'Kajang',
        'working_name': 'Kajang',
        'provisional_station': None,
        'shelved_station': None,
        'elevated_station': 'Yes',
        'underground_station': None,
        'transit_hub_station': None,
        'interchange_stations': None,
        'connecting_stations': 'KB06 Kajang [KTM Batu Caves-Pulau Sebang Line]',
        'connecting_rail_lines': "KTM Batu Caves-Pulau Sebang Line, KTM ETS Gemas-Padang Besar Line",
        'connecting_bus_lines': "T451, T461, T462, T463, T464, 450, 451",
        'feeder_bus': None,
        'park_and_ride': 'Yes',
        'malls': None,
        'hypermarkets': None,
        'tourist_attractions': None,
        'hospitals': None,
        'universities': 'New Era University College',
        'colleges': None,
        'government_agencies': None,
        'cafes': None,
        'parks': None,
        'botanical_gardens': None,
        'stadium': None,
    },
]

# Return datasets in the function generateDatasets()
def generateDatasets():
    return datasets

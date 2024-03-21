"""
 This is the configuration (init) file for the utility aws2cosipy.
 Please make your changes here.
"""

#------------------------
# Declare variable names 
#------------------------

# Pressure
PRES_var = 'PRES_var'

# Temperature
T2_var = 'T2_var'
in_K = False

# Relative humidity
RH2_var = 'RH2_var'

# Incoming shortwave radiation
G_var = 'G_var'

# Precipitation
RRR_var = 'RRR_var'

# Wind velocity
U2_var = 'U2_var'

# Incoming longwave radiation
LWin_var = 'LWin_var'

# Snowfall
SNOWFALL_var = 'SNOWFALL_var'

# Cloud cover fraction
N_var = 'N'

# Ts from obs (modified)
# Ts_var = 'Tsurf'

# Albedo from obs (modified)
ALBEDO_var = 'ALBEDO_var'

#------------------------
# Aggregation to hourly data
#------------------------
aggregate = False
aggregation_step = 'H'

# Delimiter in csv file
delimiter = ','

# WRF non uniform grid
WRF = False

#------------------------
# Radiation module 
#------------------------
radiationModule = 'Wohlfahrt2016' # 'Moelg2009', 'Wohlfahrt2016', 'none'
LUT = False                   # If there is already a Look-up-table for topographic shading and sky-view-factor built for this area, set to True

dtstep = 3600*3               # time step (s)
stationLat = 46.84625000      # Latitude of station
tcart = 26                    # Station time correction in hour angle units (1 is 4 min)
timezone_lon = 10.71798889    # Longitude of station

# Zenit threshold (>threshold == zenit): maximum potential solar zenith angle during the whole year, specific for each location
zeni_thld = 89.0              # If you do not know the exact value for your location, set value to 89.0

#------------------------
# Point model 
#------------------------
point_model = True
plon = 10.71798889
plat = 46.84625000
hgt = 3499.0

#------------------------
# Interpolation arguments 
#------------------------
stationName = 'Weißseespitze'
stationAlt = 3499.0

lapse_T         = -0.006    # Temp K per  m
lapse_RH        =  0.000    # RH % per  m (0 to 1)
lapse_RRR       =  0.0000   # mm per m
lapse_SNOWFALL  =  0.0000   # Snowfall % per m (0 to 1)

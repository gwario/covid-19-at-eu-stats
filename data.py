from math import nan

# Here is external data like the worldbank data
data_dir = 'external_data_source/'


# The year to select from country stats
worldbank_data_column_date = '2018'
# The output file containing country data
worldbank_data_filename = 'country_data.csv'

# The output file containing infection/recovery/death data
hopkins_data_filename = 'covid19_data.csv'


# All generates graphs and tables go there
export_dir = 'export/'


at = 'Austria'
be = 'Belgium'
bg = 'Bulgaria'
hr = 'Croatia'
cy = 'Cyprus'
cz = 'Czech Republic'
dk = 'Denmark'
ee = 'Estonia'
fi = 'Finland'
fr = 'France'
de = 'Germany'
gr = 'Greece'
hu = 'Hungary'
ie = 'Ireland'
it = 'Italy'
lv = 'Latvia'
lt = 'Lithuania'
lu = 'Luxembourg'
mt = 'Malta'
nl = 'Netherlands'
pl = 'Poland'
pt = 'Portugal'
ro = 'Romania'
sk = 'Slovakia'
si = 'Slovenia'
es = 'Spain'
se = 'Sweden'
ch = 'Switzerland'
uk = 'UK'
rs = 'Serbia'
tr = 'Turkey'
sy = 'Syria'
ba = 'Bosnia and Herzegovina'
li = 'Liechtenstein'
us = 'US'
cn = 'China'
ir = 'Iran'
kr = 'South Korea'
jp = 'Japan'





at_neighbours = [at, de, it, cz, hu, si, sk, li]
at_nationalities = [at, de, hu, hr, ro, ba, rs, sy, tr]
at_travel_incomming = [at, de, it, cz, ch, uk, nl, li]
at_travel_outgoing = [at, de, it, ch, hr, gr, es ]

most_connected_austria = at_neighbours+at_nationalities+at_travel_incomming+at_travel_outgoing

all_countries_eu = [at, be, bg, hr, cy, cz, dk, ee, fi, fr, de, gr, hu, ie, it, lv, lt, lu,
                    mt, nl, pl, pt, ro, sk, si, es, se]

all_countries_eu_plus = [at, be, bg, hr, cy, cz, dk, ee, fi, fr, de, gr, hu, ie, it, lv, lt,
                         lu, mt, nl, pl, pt, ro, sk, si, es, se, ch, uk, rs, tr, sy, ba, li,
                         us, cn, ir, kr, jp]
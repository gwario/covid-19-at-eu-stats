
at = 'Austria'

de = 'Germany'
it = 'Italy'
cz = 'Czech Republic'
sk = 'Slovakia'
hu = 'Hungary'
ch = 'Switzerland'
uk = 'UK'
si = 'Slovenia'
hr = 'Croatia'
gr = 'Greece'
es = 'Spain'
rs = 'Serbia'
tr = 'Turkey'
nl = 'Netherlands'
sy = 'Syria'
ro = 'Romania'
ba = 'Bosnia and Herzegovina'
li = 'Liechtenstein'


at_neighbours = [at, de, it, cz, hu, si, sk, ] #+ 'Liechtenstein'
at_nationalities = [at, de, hu, hr, ro, ba, rs, ] #+ 'Syria', 'Turkey'
at_travel_incomming = [at, de, it, cz, ch, uk, nl, ] #+ 'Liechtenstein'
at_travel_outgoing = [at, de, it, ch, hr, gr, es ]


# Source: https://en.m.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population_density?wprov=sfla1
# pop./km²
country_population_density = {
    at: 106,
    de: 233,
    it: 200,
    uk: 429, # England only
    hu: 105,
    si: 103,
    sy: 93,
    es: 92,
    rs: 89,
    hr: 72,
    tr: 106,
    sk: 111,
    ro: 81,
    ba: 69,
    li: 240,
}
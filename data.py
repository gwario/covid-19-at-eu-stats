from math import nan

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

all_countries_of_interest = [at, de, it, cz, sk, hu, ch, uk, si, hr, gr, es, rs, tr, nl, sy, ro, ba, li]


# Source: https://en.m.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population_density?wprov=sfla1
# pop./km²
country_population_density = { 
    'Population Density': {
        at: 106,
        de: 233,
        it: 200,
        uk: 274,
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
        cz: 135,
        ch: 208,
        gr: 81,
        nl: 420,
        li: 240,
}}

# Source: https://data.worldbank.org/indicator/SP.POP.TOTL?name_desc=false&view=chart
population = {'Population, total in 2018': {'Austria': 8847037.0, 'Germany': 82927922.0, 'Italy': 60431283.0, 'Czech Republic': 10625695.0, 'Slovakia': 5447011.0, 'Hungary': 9768785.0, 'Switzerland': 8516543.0, 'UK': 66488991.0, 'Slovenia': 2067372.0, 'Croatia': 4089400.0, 'Greece': 10727668.0, 'Spain': 46723749.0, 'Serbia': 6982084.0, 'Turkey': 82319724.0, 'Netherlands': 17231017.0, 'Syria': 16906283.0, 'Romania': 19473936.0, 'Bosnia and Herzegovina': 3323929.0, 'Liechtenstein': 37910.0}, 'Population ages 0-14 (% of total population) in 2018': {'Austria': 14.297947632023302, 'Germany': 13.621030104535599, 'Italy': 13.3291160906398, 'Czech Republic': 15.586605519743399, 'Slovakia': 15.446136760331099, 'Hungary': 14.4119922134424, 'Switzerland': 14.910954769106901, 'UK': 17.678082068957302, 'Slovenia': 15.0217750478021, 'Croatia': 14.5119400058464, 'Greece': 14.071244865402301, 'Spain': 14.667001107535501, 'Serbia': 15.6896807521828, 'Turkey': 24.6494101390807, 'Netherlands': 16.108158709837802, 'Syria': 31.421540806855898, 'Romania': 15.534554960562598, 'Bosnia and Herzegovina': 14.7662176493152, 'Liechtenstein': nan}, 'Population ages 15-64 (% of total population) in 2018': {'Austria': 66.7004859083869, 'Germany': 64.9170079001335, 'Italy': 63.9192043068525, 'Czech Republic': 64.9925175870224, 'Slovakia': 68.9246167348919, 'Hungary': 66.4302824033255, 'Switzerland': 66.4658286661214, 'UK': 63.926052256896, 'Slovenia': 65.37134529801911, 'Croatia': 65.0426269817306, 'Greece': 64.2734830567542, 'Spain': 65.954491369965, 'Serbia': 65.964526556121, 'Turkey': 66.8673769209477, 'Netherlands': 64.69564865682351, 'Syria': 64.07533477166821, 'Romania': 66.1267436456077, 'Bosnia and Herzegovina': 68.7634648796227, 'Liechtenstein': nan}, 'Population ages 65 and above (% of total population) in 2018': {'Austria': 19.0015664595899, 'Germany': 21.4619619953309, 'Italy': 22.7516796025077, 'Czech Republic': 19.4208768932343, 'Slovakia': 15.629246504777, 'Hungary': 19.1577253832321, 'Switzerland': 18.6232165647717, 'UK': 18.395865674146602, 'Slovenia': 19.6068796541788, 'Croatia': 20.445433012423, 'Greece': 21.6552720778435, 'Spain': 19.3785075224995, 'Serbia': 18.3457926916963, 'Turkey': 8.4832129399716, 'Netherlands': 19.1961926333387, 'Syria': 4.50312442147583, 'Romania': 18.338701393829602, 'Bosnia and Herzegovina': 16.4703174710621, 'Liechtenstein': nan}}

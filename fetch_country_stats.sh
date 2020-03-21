# Setup
mkdir -p external_data_source
cd external_data_source
# Clean up
rm -r *

# Total population
curl -O https://api.worldbank.org/v2/country/all/indicator/SP.POP.TOTL?downloadformat=csv

# Male/female in % of total population
curl -O https://api.worldbank.org/v2/country/all/indicator/SP.POP.TOTL.FE.ZS?downloadformat=csv
curl -O https://api.worldbank.org/v2/country/all/indicator/SP.POP.TOTL.MA.ZS?downloadformat=csv

# Male/female age ranges in % of Male/female population
curl -O https://api.worldbank.org/v2/country/all/indicator/SP.POP.0004.FE.5Y?downloadformat=csv
curl -O https://api.worldbank.org/v2/country/all/indicator/SP.POP.0509.FE.5Y?downloadformat=csv
curl -O https://api.worldbank.org/v2/country/all/indicator/SP.POP.1014.FE.5Y?downloadformat=csv
curl -O https://api.worldbank.org/v2/country/all/indicator/SP.POP.1519.FE.5Y?downloadformat=csv
curl -O https://api.worldbank.org/v2/country/all/indicator/SP.POP.2024.FE.5Y?downloadformat=csv
curl -O https://api.worldbank.org/v2/country/all/indicator/SP.POP.2529.FE.5Y?downloadformat=csv
curl -O https://api.worldbank.org/v2/country/all/indicator/SP.POP.3034.FE.5Y?downloadformat=csv
curl -O https://api.worldbank.org/v2/country/all/indicator/SP.POP.3539.FE.5Y?downloadformat=csv
curl -O https://api.worldbank.org/v2/country/all/indicator/SP.POP.4044.FE.5Y?downloadformat=csv
curl -O https://api.worldbank.org/v2/country/all/indicator/SP.POP.4549.FE.5Y?downloadformat=csv
curl -O https://api.worldbank.org/v2/country/all/indicator/SP.POP.5054.FE.5Y?downloadformat=csv
curl -O https://api.worldbank.org/v2/country/all/indicator/SP.POP.5559.FE.5Y?downloadformat=csv
curl -O https://api.worldbank.org/v2/country/all/indicator/SP.POP.6064.FE.5Y?downloadformat=csv
curl -O https://api.worldbank.org/v2/country/all/indicator/SP.POP.6569.FE.5Y?downloadformat=csv
curl -O https://api.worldbank.org/v2/country/all/indicator/SP.POP.7074.FE.5Y?downloadformat=csv
curl -O https://api.worldbank.org/v2/country/all/indicator/SP.POP.7579.FE.5Y?downloadformat=csv
curl -O https://api.worldbank.org/v2/country/all/indicator/SP.POP.80UP.FE.5Y?downloadformat=csv

curl -O https://api.worldbank.org/v2/country/all/indicator/SP.POP.80UP.MA.5Y?downloadformat=csv
curl -O https://api.worldbank.org/v2/country/all/indicator/SP.POP.7579.MA.5Y?downloadformat=csv
curl -O https://api.worldbank.org/v2/country/all/indicator/SP.POP.7074.MA.5Y?downloadformat=csv
curl -O https://api.worldbank.org/v2/country/all/indicator/SP.POP.6569.MA.5Y?downloadformat=csv
curl -O https://api.worldbank.org/v2/country/all/indicator/SP.POP.6064.MA.5Y?downloadformat=csv
curl -O https://api.worldbank.org/v2/country/all/indicator/SP.POP.5559.MA.5Y?downloadformat=csv
curl -O https://api.worldbank.org/v2/country/all/indicator/SP.POP.5054.MA.5Y?downloadformat=csv
curl -O https://api.worldbank.org/v2/country/all/indicator/SP.POP.4549.MA.5Y?downloadformat=csv
curl -O https://api.worldbank.org/v2/country/all/indicator/SP.POP.4044.MA.5Y?downloadformat=csv
curl -O https://api.worldbank.org/v2/country/all/indicator/SP.POP.3539.MA.5Y?downloadformat=csv
curl -O https://api.worldbank.org/v2/country/all/indicator/SP.POP.3034.MA.5Y?downloadformat=csv
curl -O https://api.worldbank.org/v2/country/all/indicator/SP.POP.2529.MA.5Y?downloadformat=csv
curl -O https://api.worldbank.org/v2/country/all/indicator/SP.POP.2024.MA.5Y?downloadformat=csv
curl -O https://api.worldbank.org/v2/country/all/indicator/SP.POP.1519.MA.5Y?downloadformat=csv
curl -O https://api.worldbank.org/v2/country/all/indicator/SP.POP.1014.MA.5Y?downloadformat=csv
curl -O https://api.worldbank.org/v2/country/all/indicator/SP.POP.0509.MA.5Y?downloadformat=csv
curl -O https://api.worldbank.org/v2/country/all/indicator/SP.POP.0004.MA.5Y?downloadformat=csv

# Density
curl -O https://api.worldbank.org/v2/country/all/indicator/EN.POP.DNST?downloadformat=csv


# Rename
rename 's/(.*)\?.*/$1.zip/' *

# Extract
unzip \*.zip

# Clean up
rm *.zip
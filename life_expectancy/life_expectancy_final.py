amount=int()
country=''
country_avg=float()
country_avg_list=[]
country_flag=False
high_country=float()
life=float()
low_country=float()
low_year=int()
high_year=int()
max_country=''
max_total=float(0)
max_life=float(0)
min_country=''
min_total=float(200)
min_life=float(200)
sum_country=float()
sum_year=float()
which_country=input('Enter a country of interest: ').lower()
which_country_high=float(0)
which_country_low=float(200)
which_year=input('Enter the year of interest: ')
year=int()
year_avg=float()
year_avg_list=[]
year_flag=False

with open("life_expectancy/life-expectancy.csv") as lives:

    # Collecting data...

    # for line in lives:
    #     data = line.strip()
    #     data = data.split(',')
    #     country=data[0]
    #     life=data[3]
    #     year=data[2]
    #     if which_country==country.lower():
    #         country_flag=True
    #     if which_year==year:
    #         year_flag=True

    # Collecting data...

    for line in lives:
        data = line.strip()
        data = data.split(',')
        country=data[0]
        life=data[3]
        year=data[2]

        # Finding overall max and min:

        if life!='Life expectancy (years)':
            life=float(life)
            if life < min_total:
                min_total=life
                low_country=country
                low_year=year
            elif life > max_total:
                max_total=life
                high_country=country
                high_year=year

        # Finding max and min for which_country:

        if which_country==country.lower(): #and country_flag==True:
            country_avg_list.append(life)
            if life < which_country_low:
                which_country_low=life
            elif life > which_country_high:
                which_country_high=life

        # Finding max and min for which_year

        if which_year==year: #and year_flag==True:
            year_avg_list.append(life)
            if life < min_life:
                min_life=life
                min_country=country
            elif life > max_life:
                max_life=life
                max_country=country

# Finding averages
# if country_flag==True:
sum_country=sum(country_avg_list)
amount=len(country_avg_list)
country_avg=sum_country/amount
# if year_flag==True:
sum_year=sum(year_avg_list)
amount=len(year_avg_list)
year_avg=sum_year/amount

print()
print(f'The overall max life expectancy is {max_total:.2f} from {high_country} in {high_year}.')
print(f'The overall min life expectancy is {min_total:.2f} from {low_country} in {low_year}.')
print()
print(f'For the country {which_country.title()}:')
print(f'The average life expectancy for all years is {country_avg:.2f} years.')
print(f'The overall max life expectancy is {which_country_high:.2f} years.')
print(f'The overall min life expectancy is {which_country_low:.2f} years.')
print()
print(f'For the year {which_year}:')
print(f'The average life expectancy across all countries in {which_year} was: {year_avg:.2f}')
print(f'The max life expectancy was in {max_country} with {max_life}.')
print(f'The min life expectancy was in {min_country} with {min_life}.')
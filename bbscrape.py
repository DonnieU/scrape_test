import requests
from bs4 import BeautifulSoup
from datetime import datetime, date, time

site_id = '40' # Pampa
todays_date = datetime.today().strftime("%m%d%Y") # ex return: 01072021
# URL = "http://rain.ttu.edu/tech/1-output/site.php?id=40&date=01152021"
URL = "http://rain.ttu.edu/tech/1-output/site.php?id=" + site_id + "&date=" + todays_date
page = requests.get(URL)
# pp.pprint(page.content)

soup = BeautifulSoup(page.content, 'html.parser')
# print(soup.prettify())
# print(soup.title)
# print(soup.head)
# print(soup.thead)
thead = soup.thead
# print(thead.contents[0].split()[5])
obs_data_site = thead.contents[0].split()[3] # expect: 'Pampa'
obs_data_date = thead.contents[0].string.split()[5] # expect: today's date
print(obs_data_site)
print(obs_data_date)
obs_date = obs_data_date.split('/')
print(obs_date)
obs_date = date( int(obs_date[2]), int(obs_date[0]), int(obs_date[1]) ).strftime("%Y-%m-%d")
print(obs_date)
todays_date = datetime.today().strftime("%Y-%m-%d") # ex return: 2021-01-26 
print(obs_date == todays_date)

# print(soup.td)
all_td = soup.find_all('td')
# print(all_td)
print('\n\n\n')
# print(all_td.contents)
# print(len(all_td))

updated_time = all_td[0].string
# print(updated_time.string)
updated_date_time = obs_date + ' ' + updated_time
print(f'updated_time: {updated_date_time}')

# converts 12hr time to 24 hr time
#in_time = datetime.strptime(updated_time, "%I:%M %p")
in_time = datetime.strptime(updated_date_time, "%Y-%m-%d %I:%M %p")
out_time = datetime.strftime(in_time, "%H:%M")
print(f'in_time: {in_time}')
print(f'out_time: {out_time}')
test_time = "11:00"
# current_time = datetime.strftime(datetime.now(), "%H:%M")
# current_time = datetime.strptime(datetime.now(), "%H:%M")
current_time = datetime.now()
print(f'current time: {current_time}')
print(current_time < in_time)
#out_current_time = datetime.strptime(current_time, "%H:%M")
#print(f'out_current_time: {out_current_time}')
# print(f'current time: {datetime.strftime(datetime.now(), "%H:%M")}')
#print(f'time diff: {current_time - out_time}')
# print(current_time - out_time)
# t.strip("<td>")
# print(t)
# t.strip('<td>')
# print(t)
# index of wind direction, wind speed, wind gust
print(all_td[6].string)
wind_info = all_td[6].string.split()
rel_humidity = all_td[9].string
print(f'rel_humidity: {rel_humidity}')
solar_rad = all_td[11].string
print(f'solar_rad: {solar_rad}')
# print(wind_info.split())
print(wind_info)

wind_dir, wind_speed, wind_gust = wind_info
print(f'wind dir: {wind_dir}, wind speed: {wind_speed}, wind gust: {wind_gust}')

# print(soup.body)

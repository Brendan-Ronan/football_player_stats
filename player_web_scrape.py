from bs4 import BeautifulSoup
import sqlite3

# read in HTML file
html_file_path = '/Users/brendanronan/Desktop/python/project_01/current_Z.html'
with open(html_file_path, 'r', encoding='utf-8') as file:
    current_players_a = file.read()

# parse HTML with BeautifulSoup
soup = BeautifulSoup(current_players_a,'html.parser')

# create sqlite database and cursor
conn = sqlite3.connect('football_players')
cursor = conn.cursor()

# Create a database table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS players (
        player_name TEXT, 
        position TEXT, 
        team TEXT, 
        college TEXT
    )
''')

# extract the data we want from html and insert into database
rows = soup.find_all('div', class_= 'tr')
for row in rows:
    columns = row.find_all('div', class_='td')

    player_name = columns[0].text.strip()
    position = columns[1].text.strip()
    team = columns[2].text.strip()
    college = columns[3].text.strip()

    cursor.execute('''
    
    INSERT INTO players (player_name, position, team, college)
    VALUES (?, ?, ?, ?)
    ''', (player_name, position, team, college))

conn.commit()
conn.close()

print("Data parsed and stored in SQL database.")





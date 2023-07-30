

import json
from db_python2 import connect_to_db, insert, select

connect_to_db('pointsOfSale.db')

with open('pointsOfSale.json', encoding='utf-8') as soubor:
    data = json.load(soubor)
    for item in data:
        insert('prodejni_mista',
               id=item['id'],
               type=item['type'],
               name=item['name'],
               address=item['address'],
               lat=item['lat'],
               lon=item['lon'],
        )
        print('vytvořen záznam', item['id'])


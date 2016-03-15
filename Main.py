# Initial Commit

import pygbif as bgif
from pygbif import registry
from pygbif import species
from pygbif import occurrences
from bs4 import BeautifulSoup
import requests
import json

suggest = species.name_suggest(q="sparrow", rank='SPECIES')

# backbone = species.name_backbone(name='white tiger', kingdom='animalia')

# print(backbone)

# print(suggest)

# suggest = species.name_backbone(name='white tiger', kingdom='animals', limit=500)

suggest_data = suggest['data']['results']

print(suggest_data)

data = suggest_data

for o in data:
    # print(o)
    key = o['key']
    names = o['vernacularNames']
    for name in names:
        print(name)
    print(key)
    # vernacular = o['vernacularNames']
    # for v in vernacular:
    #     print(v)
    # print(key)
    # print(name)
    # occurs = occurrences.count(taxonKey=key)
    # print('Name: ' + '\nCount: ' + str(occurs))

# occurs = occurrences.search()

# print(suggest['data'])

# print(suggest)
#
# number = occurrences.search(taxonKey=5959227, limit=250)
# occurs = number
#
# country_count = dict
#
#
#
# for o in occurs['results']:
#     country = o['country']
#
#     # Reads image of occurrence
#     # Could be used for the GUI images
#     # image = o['media']['identifier']
#
#     print(country)
#
# print(number)

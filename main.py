from replit import db
import os

# store my name in the replit db
# db['name'] = 'ben'

print(db['name'])

keys = db .keys()

print(keys)


for key in db :
  print(db[key])



apiKEY = os.environ['apiKEY']
print(apiKEY)
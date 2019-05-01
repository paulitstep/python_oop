from person import Person, Manager

joey = Person('Joey Tribbiani')
rachel = Person('Rachel Green', job='waitress', pay=1500)
chandler = Manager('Chandler Bing', 50000)

import shelve
db = shelve.open('persondb')
for object in (joey, rachel, chandler):
    db[object.name] = object
db.close()


import shelve
db = shelve.open('persondb')
# print(len(db))
# print(list(db.keys()))
# joey = db['Joey Tribbiani']
# print(joey)
# print(joey.lastName())

# for key in db:
#     print(key, '=>', db[key])

for key in sorted(db):
    print(key, '=>', db[key])

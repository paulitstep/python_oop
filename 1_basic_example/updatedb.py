import shelve
db = shelve.open('persondb')

for key in sorted(db):
    print(key, '\t=>', db[key])

rachel = db['Rachel Green']
rachel.giveRaise(.10)
db['Rachel Green'] = rachel

db.close()

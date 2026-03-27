import sqlite3
import json
import codecs

conn = sqlite3.connect('CA_universities.sqlite')
cur = conn.cursor()

cur.execute('SELECT * FROM Universities')
fhand = codecs.open('ca_universities.js', 'w', "utf-8")
fhand.write("myData = [\n")
count = 0
for row in cur :
    data = str(row[1].decode())
    # data = row[1]
    # if isinstance(data, memoryview):  # support memoryview
    #     data = data.tobytes().decode()
    try: 
        js = json.loads(str(data))
    except: 
        continue

    if len(js['features']) == 0: continue
    # if 'features' not in js or len(js['features']) == 0:
    #     continue
    try:
        lat = js['features'][0]['geometry']['coordinates'][1]
        lng = js['features'][0]['geometry']['coordinates'][0]
        where = js['features'][0]['properties']['display_name']
        where = where.replace("'", "")
    except:
        # continue
        print('Unexpected format')
        print(js)

    try :
        print("📍", where, lat, lng)

        count = count + 1
        if count > 1 : fhand.write(",\n")
        output = "["+str(lat)+","+str(lng)+", '"+where+"']"
        fhand.write(output)
    except:
        continue

fhand.write("\n];\n")
cur.close()
fhand.close()
print(count, "records written to ca_universities.js")
print("Open where.html to view the data in a browser")


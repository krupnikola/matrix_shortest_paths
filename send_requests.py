import requests

xml_map = """<?xml version="1.0" encoding="UTF-8"?>
<map>
	<cells>
		<cell row="1" col= "1" />
		<cell row="1" col= "3" />
		<cell row="2" col= "1" />
		<cell row="2" col= "2" />
		<cell row="2" col= "3" />
		<cell row="3" col= "1" />
		<cell row="3" col= "2" />
	</cells>
	<start-point row="1" col= "1" />
	<end-point row="3" col= "2" />
</map>"""

headers = {'Content-Type': 'application/xml'}

r = requests.post('http://127.0.0.1:5000/api/map', data=xml_map, headers=headers)

print(r.json())

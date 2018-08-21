import json

myMovie = {"Iron Man": 9.8, "Infinite War": 9.0}
jsonStr = json.dumps(myMovie)
print(jsonStr)

myMovie2 = json.loads(jsonStr)
print(myMovie2)

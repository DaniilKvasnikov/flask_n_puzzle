import json


class Map:

    def __init__(self, map_size, map_count, map):
        self.map_size = map_size
        self.map_count = map_count
        self.map = map

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__)
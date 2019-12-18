from flask import Flask
import os

from app import path_example
from map import Map

dirname = os.path.dirname(__file__)
app = Flask(__name__)


def get_json():
    filename = os.path.join(dirname, path_example)
    with open(filename, "r") as f:
        size_puzzle = 0
        map_block = []
        map = []
        for line in f:
            if line[0] != '#':
                if line.find("#") != -1:
                    line = line[0:line.find("#")]
                if size_puzzle == 0:
                    size_puzzle = int(line)
                else:
                    map_block.append(line.split())
                    if len(map_block) == size_puzzle:
                        map.append(map_block.copy())
                        map_block.clear()
        map_obj = Map(size_puzzle, len(map), map)
        json_res = map_obj.toJSON()
        print(json_res)
        return json_res


@app.route('/')
def hello():
    return get_json()


if __name__ == '__main__':
    app.run()

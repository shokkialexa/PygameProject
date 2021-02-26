if __name__ == "main":
    pass
else:
    BOARD = [["field", "field", "field", "grass", "grass", "tree", "tree", "tree", "tree",
              "tree", "tree", "tree", "tree", "tree", "tree", "tree", "tree", "tree", "tree",
              "tree", "tree", "tree", "tree", "tree", "tree", "tree", "tree", "tree", "tree",
              "tree", "tree", "grass", "house", "house", "house", "grass", "grass", "grass",
              "grass", "grass", "grass", "grass", "grass", "grass", "cocostree"],

             ["field", "field", "field", "grass", "grass", "grass", "tree", "tree", "grass",
              "tree", "tree", "tree", "tree", "tree", "tree", "tree", "tree", "tree", "tree",
              "tree", "tree", "tree", "tree", "tree", "tree", "tree", "tree", "tree", "tree",
              "tree", "tree", "grass", "grass", "grass", "grass", "house", "grass", "grass",
              "grass", "grass", "cocostree", "cocostree", "grass", "grass", "grass"],

             ["field", "field", "field", "grass", "grass", "grass", "grass", "grass", "tree",
              "tree", "tree", "tree", "grass", "tree", "grass", "tree", "tree", "tree", "tree",
              "tree", "tree", "tree", "tree", "tree", "tree", "tree", "tree", "tree", "tree",
              "grass", "grass", "grass", "grass", "house", "house", "grass", "grass", "grass",
              "grass", "grass", "grass", " grass", "cocostree", "cocostree", "grass"],

             ["field", "field", "grass", "grass", "grass", "grass", "grass", "tree", "grass",
              "grass", "tree", "grass", "tree", "grass", "tree", "tree", "tree", "tree", "tree",
              "rock", "grass", "grass", " grass", "tree", "tree", "tree", "tree", "tree", "grass",
              "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass",
              "grass", "water", "grass", "cocostree", "grass", "crashedcocostree", "cocostree"],

             ["field", "grass", "grass", "grass", "field", "field", "field", "grass", "grass",
              "grass", "grass", "grass", "grass", "grass", "house", "grass", "tree", "tree", "grass",
              "grass", "grass", "grass", "tree", "tree", "tree", "grass", "tree", "tree", "tree", "tree",
              "grass", "grass", "grass", "grass", "grass", "grass", "grass", "water", "water", "water",
              "water", "water", "grass", "cocostree", "grass"],

             ["grass", "grass", "field", "field", "field", "field", "field", "field", "grass", "grass",
              "grass", "house", "house", "grass", "grass", "house", "grass", "tree", "tree", "well", "grass",
              "rock", "tree", "tree", "grass", "tree", "tree", "tree", "tree", "grass", "tree", "grass", "grass",
              "grass", "grass", "water", "water", "water", "water", "water", "water", "water", "water", "grass",
              "grass"],

             ["tree", "grass", "grass", "field", "field", "field", "field", "field", "field", "grass", "grass", "house",
              "grass", "house", "house", "grass", "grass", "tree", "tree", "tree", "grass", "grass", "tree", "tree",
              "tree", "tree", "tree", "tree", "grass", "grass", "grass", "grass", "grass", "grass", "water", "water",
              "water", "water", "water", "water", "water", "water", "water", "grass", "cocostree"],

             ["tree", "tree", "tree", "grass", "field", "field", "field", "field", "grass", "grass", "grass", "grass",
              "house", "house", "house", "house", "grass", "grass", "tree", "tree", "grass", "tree", "tree", "tree",
              "grass", "tree", "tree", "tree", "grass", "grass", "grass", "grass", "grass", "grass", "water", "water",
              "water", "water", "water", "water", "water", "water", "water", "grass", "grass"],

             ["tree", "tree", "grass", "field", "field", "grass", "field", "field", "grass", "grass", "grass", "grass",
              "grass", "grass", "grass", "grass", "grass", "grass", "tree", "grass", "grass", "grass", "tree",
              "tree", "grass", "tree", "tree", "grass", "grass", "grass", "grass", "grass", "grass", "grass",
              "water", "water", "water", "water", "water", "water", "water", "water", "grass", "grass", "grass"],

             ["tree", "grass", "grass", "field", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass",
              "grass", "store", "store", "store", "grass", "grass", "grass", "grass", "grass", "rock", "grass", "grass",
              "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass",
              "water",
              "water", "water", "water", "water", "water", "water", "grass", "crashedcocostree", "cocostree"],

             ["tree", "tree", "tree", "grass", "grass", "grass", "grass", "grass", "field", "grass", "grass", "grass",
              "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass",
              "grass",
              "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass",
              "bridge",
              "bridge", "bridge", "bridge", "bridge", "bridge", "grass", "grass", "grass", "grass"],

             ["tree", "tree", "grass", "grass", "grass", "grass", "grass", "grass", "field", "field", "grass", "field",
              "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass",
              "grass",
              "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "water",
              "water",
              "water", "water", "water", "grass", "grass", "grass", "cocostree", "cocostree", "cocostree"],

             ["tree", "tree", "tree", "grass", "tree", "grass", "grass", "grass", "grass", "field", "field", "field",
              "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass",
              "grass",
              "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "water", "water", "water",
              "water",
              "water", "water", "water", "water", "grass", "grass", "grass", "grass", "cocostree"],

             ["tree", "tree", "tree", "tree", "tree", "grass", "grass", "grass", "field", "field", "field", "field",
              "field", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass",
              "grass",
              "grass", "grass", "grass", "grass", "grass", "grass", "grass", "water", "water", "water", "water",
              "water",
              "water", "water", "water", "water", "grass", "grass", "grass", "cocostree", "grass"],

             ["tree", "tree", "tree", "tree", "tree", "tree", "grass", "grass", "grass", "grass", "field", "field",
              "field", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass",
              "grass",
              "grass", "grass", "grass", "grass", "grass", "grass", "grass", "water", "water", "water", "water",
              "water",
              "water", "water", "water", "water", "water", "water", "grass", "grass", "grass"],

             ["tree", "tree", "tree", "tree", "tree", "tree", "tree", "grass", "grass", "grass", "grass", "grass",
              "grass",
              "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass",
              "grass", "grass", "grass", "grass", "grass", "grass", "grass", "water", "water", "water", "water",
              "water",
              "water", "water", "water", "water", "water", "water", "grass", "grass", "grass"],

             ["tree", "tree", "tree", "tree", "tree", "tree", "tree", "tree", "grass", "grass", "grass", "grass",
              "grass",
              "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass",
              "grass", "grass", "grass", "grass", "grass", "grass", "water", "water", "water", "water", "water",
              "water",
              "water", "water", "water", "water", "water", "water", "water", "grass", "grass"],

             ["tree", "tree", "tree", "tree", "tree", "grass", "grass", "grass", "grass", "grass", "grass", "grass",
              "grass",
              "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass",
              "grass", "grass", "grass", "grass", "grass", "grass", "grass", "grass", "water", "water", "water",
              "water",
              "water", "water", "water", "water", "water", "water", "grass", "grass", "grass"]]

    CELL_SIZE = (16, 16)

    BOARD_SIZE = (45, 18)

    POKEMON_CHANCE = 5

    BOOST_CHANCE = 10
    POKEBALL_CHANCE = 10

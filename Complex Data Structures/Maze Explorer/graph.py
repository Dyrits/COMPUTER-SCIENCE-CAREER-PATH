from vertex import Vertex


class Graph:
    def __init__(self):
        self.graph_dict = {}

    def add_vertex(self, node):
        self.graph_dict[node.value] = node

    def add_edge(self, from_node, to_node, weight=0):
        self.graph_dict[from_node.value].add_edge(to_node.value, weight)
        self.graph_dict[to_node.value].add_edge(from_node.value, weight)

    def explore(self, current_room, path_total = 0):
        print("Exploring the castle....\n")
        #FILL IN EXPLORE METHOD BELOW
        print()
        print(f"You are at the {current_room}.")
        print()
        if current_room != "Treasure Room":
            node = self.graph_dict[current_room]
            for connected_room, weight in node.edges.items():
                print(f"Enter {connected_room[0]} for {connected_room}: {weight} moves")
            valid_choices = [connected_room[0] for connected_room in node.edges.keys()]
            print()
            print(f"You have accumulated: {path_total} moves")
            print()
            print()
            choice = input("Which room do you want to move to? ").upper()
            while choice not in valid_choices:
                choice = input(f"Please, select from these letters: {valid_choices} ").upper()
            for connected_room, weight in node.edges.items():
                if connected_room.startswith(choice):
                    current_room = connected_room
                    path_total += weight
            print()
            print(f"You moved to {current_room}.")
            print()
            self.explore(current_room, path_total)
        else:
            print(f"You made it to the Treasure Room with {path_total} moves!")
                

    def print_map(self):
        print("\nMAZE LAYOUT\n")
        for node_key in self.graph_dict:
            print("{0} connected to...".format(node_key))
            node = self.graph_dict[node_key]
            for adjacent_node, weight in node.edges.items():
                print("=> {0}: distance is {1}".format(adjacent_node, weight))
            print("")
        print("")


def build_graph():
    graph = Graph()

    # MAKE ROOMS INTO VERTICES BELOW...
    entrance = Vertex("Entrance")
    ante_chamber = Vertex("Ante Chamber")
    kings_room = Vertex("King's Room")
    grand_gallery = Vertex("Grand Gallery")
    little_gallery = Vertex("Little Gallery")
    dining_hall = Vertex("Dining Hall")
    stables = Vertex("Stables")
    minions_quarters = Vertex("Minions Quarters")
    underground_path = Vertex("Underground Path")
    treasure_room = Vertex("Treasure Room")
    # ADD ROOMS TO GRAPH BELOW...
    graph.add_vertex(entrance)
    graph.add_vertex(ante_chamber)
    graph.add_vertex(kings_room)
    graph.add_vertex(grand_gallery)
    graph.add_vertex(treasure_room)
    graph.add_vertex(dining_hall)
    graph.add_vertex(stables)
    graph.add_vertex(minions_quarters)
    graph.add_vertex(little_gallery)
    graph.add_vertex(underground_path)
    # ADD EDGES BETWEEN ROOMS BELOW...
    graph.add_edge(entrance, ante_chamber, 7)
    graph.add_edge(entrance, stables, 10)
    graph.add_edge(entrance, dining_hall, 2)
    graph.add_edge(ante_chamber, kings_room, 2)
    graph.add_edge(ante_chamber, grand_gallery, 2)
    graph.add_edge(stables, minions_quarters, 2)
    graph.add_edge(dining_hall, grand_gallery, 4)
    graph.add_edge(grand_gallery, little_gallery, 4)
    graph.add_edge(minions_quarters, underground_path, 1)
    graph.add_edge(little_gallery, kings_room, 2)
    graph.add_edge(underground_path, treasure_room, 1)
    graph.add_edge(kings_room, treasure_room, 1)
    # DON'T CHANGE THIS CODE
    graph.print_map()
    return graph

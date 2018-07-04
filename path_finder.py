import xml.etree.ElementTree as ET
import random
import networkx as nx
import time


class PathFinder:
    @staticmethod
    def get_shortest_paths(xml_file):
        start_time = time.time()
        tree = ET.parse(xml_file)
        root = tree.getroot()

        if root.tag == 'map' and root[0].tag == 'cells' and root[0][0].tag == 'cell':

            g = nx.Graph()

            start_row = int(root.find('start-point').attrib['row'])
            start_col = root.find('start-point').attrib['col']
            end_row = int(root.find('end-point').attrib['row'])
            end_col = root.find('end-point').attrib['col']

            start = (start_row, start_col)
            end = (end_row, end_col)

            for cell in root.iter('cell'):
                row = int(cell.attrib['row'])
                col = cell.attrib['col']
                # add nodes to graph
                g.add_node((row, col))

            def increment_char(ch):
                new = chr(ord(ch) + 1)
                return new

            def decrement_char(ch):
                new = chr(ord(ch) - 1)
                return new

            try:

                for node in g.nodes:
                    potential_neighbours = [(node[0] + 1, node[1]), (node[0], increment_char(node[1])), (node[0] - 1, node[1]),
                                            (node[0], decrement_char(node[1]))]

                    for pn in potential_neighbours:
                        if pn in g.nodes:
                            g.add_edge(node, pn)

                data = {
                    "execution_time": None,
                    "paths": []
                }

                # check if there are (shortest) paths available
                try:
                    paths = nx.all_shortest_paths(g, start, end)

                    for path in paths:
                        data["paths"].append({"points": [{"row": point[0], "col": point[1]} for point in path]})
                except nx.NetworkXNoPath:
                    data["paths"].append({"points": ["No paths found"]})

                data["execution_time"] = time.time() - start_time

                return data

            except nx.NodeNotFound:
                return "Start/End node not in matrix."
        else:
            return "Invalid content of .xml file."


def generate_test_matrix(g):
    for i in range(1000):
        for j in range(1000):
            g.add_node((random.randint(0, 999), random.randint(0, 999)))
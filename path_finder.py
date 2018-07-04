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

            start_row = root.find('start-point').attrib['row']
            start_col = root.find('start-point').attrib['col']
            end_row = root.find('end-point').attrib['row']
            end_col = root.find('end-point').attrib['col']

            # turning letters into numbers
            start_row = ord(start_row) - 64 if start_row.isalpha() else int(start_row)
            start_col = ord(start_col) - 64 if start_col.isalpha() else int(start_col)
            end_row = ord(end_row) - 64 if end_row.isalpha() else int(end_row)
            end_col = ord(end_col) - 64 if end_col.isalpha() else int(end_col)

            start = (start_row, start_col)
            end = (end_row, end_col)

            for cell in root.iter('cell'):
                row = cell.attrib['row']
                col = cell.attrib['col']

                row = ord(row) - 64 if row.isalpha() else int(row)
                col = ord(col) - 64 if col.isalpha() else int(col)

                # adding rest of the cells to the graph
                g.add_node((row, col))

            try:

                for node in g.nodes:
                    potential_neighbours = [(node[0] + 1, node[1]), (node[0], node[1] + 1), (node[0] - 1, node[1]),
                                            (node[0], node[1] - 1)]

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
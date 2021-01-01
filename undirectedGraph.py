import networkx
import matplotlib.pyplot as plt
import pandas
import numpy
numpy.seterr(divide='ignore')

# Vertex object
class Vertex(object):

    def __init__(self, key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self, neighbor, weight=0):
        self.connectedTo[neighbor] = weight

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self, neighbor):
        return self.connectedTo[neighbor]

    def __str__(self):
        return str(self.id)

# Graph object
class Graph(object):

    def __init__(self):
        self.masterList = {i: Vertex(i) for i in range(1, 24)}  # vertex id : Vertex obj  - 23 Vertices
        self.patient_name = None
        self.density = None
        self.shortest_paths = None
        self.modularity_matrix = None
        self.degree = None
        self.efficiency = None

    def getVertex(self, n):
        if n in self.masterList:
            return self.masterList[n]
        else:
            return None

    def addEdge(self, fromV, toV, weight=0):
        if (fromV == toV):
            return
        if toV not in self.getVertex(fromV).connectedTo:
            self.masterList[fromV].addNeighbor(toV, weight)
            self.masterList[toV].addNeighbor(fromV, weight)

    def __iter__(self):
        # this sepcial function allows us to iterate through master list
        return iter(self.masterList.values())

    def __contains__(self, n):
        # this special function allows us to use IN operator
        if n in self.masterList:
            return True
        else:
            return False

    def create_edges(self, patient_name):
        self.patient_name = patient_name
        file_csv = patient_name+'.csv'
        df = pandas.read_csv(file_csv)
        print(file_csv,"-> inside create edges")
        edges = []
        for col in range(0, 23):
            for row in range(0, 23):
                if df[str(col)][row] == 1:
                    edges.append((col + 1, row + 1))
        print(edges,"-> inside create edges")
        return edges

    def create_nodes(self, edges):
        G = networkx.Graph() # define G
        G.add_nodes_from(range(1,24))
        G.add_edges_from(edges)
        fixed_positions = { 1: (-3.5, 10), 2: (3.5, 10),
                            3: (-2.5, 8), 4: (-1.5, 8), 5:(-0.5, 8), 6: (0.5, 8), 7: (1.5,8), 8:(2.5,8),
                            9: (-4, 7), 10:(4,7),
                            11:(-2,6), 12: (0,6), 13:(2,6),
                            14: (-3, 4), 15:(-1,4), 16:(1,4), 17: (3,4),
                            18:(-2.5,2), 19:(-1.5,2), 20: (-0.5,2), 21:(0.5,2), 22:(1.5,2), 23: (2.5,2)
                            }

        fixed_nodes = fixed_positions.keys()
        pos = networkx.spring_layout(G, pos=fixed_positions, fixed=fixed_nodes)
        networkx.draw_networkx(G, pos)
        plt.savefig(self.patient_name+".png")
        plt.show()
        #   ----- Updating Local Parameters of the Graph ------ #
        self.density = self.density_calc(G)
        self.shortest_paths = self.shortets_path(G)
        self.modularity_matrix = self.modularity_matrix_calc(G)
        #   ----- Updating Local Parameters of the Graph ------ #
        self.degree = G.degree()
        self.efficiency = [networkx.global_efficiency(G.subgraph(set(G) - {i})) for i in range(1,24)]
        # divided = numpy.divide(1,list(networkx.single_source_shortest_path_length(G, 9).values()))
        # print(divided)
        # divided = numpy.where(divided==numpy.inf,numpy.nan,divided)
        # print(divided)
        # print(numpy.nansum(divided))
        # print("efficiency Node 9 -> ",(1/22)*(numpy.nansum(divided)))
        return G

    def density_calc(self, graph):
        """ d = 2m / n(n−1) when m = number of edges, n = number of nodes"""
        return networkx.density(graph)

    def shortets_path(self, graph):
        """ This function calculates the shortest paths between all the nodes using floyd-warshall algorithm"""
        return networkx.floyd_warshall(graph)

    def modularity_matrix_calc(self, graph):
        """ This function calculates the modularity matrix"""
        return networkx.modularity_matrix(graph)

if __name__ == '__main__':
    # patient = Patient("1","2",'3','4')
    # res = patient.data_section("C:/FinalProj/newdata/healthy/sub10_dc_clean.xlsx", 5)
    # resu_corr = patient.correlation_matrix(res)
    # resu_binary = patient.binary_matrix(resu_corr, 0.4)

    g = Graph()

    # for col in range(len(resu_binary)):
    #     for row in range(0, 23):
    #         if resu_binary[col][row] == 1:
    #             g.addEdge(col + 1, row + 1, 0)
    #
    # for vertex in g.masterList:
    #     print(vertex, " -> ", g.getVertex(vertex).getConnections())



    gra = g.create_nodes(g.create_edges('Uriel Lirr'))
    print(type(gra))
    print(g.density)
    floywarsh = g.shortest_paths
    print(floywarsh[1][11])
    shortpath = dict(networkx.all_pairs_shortest_path(gra))
    print(g.shortest_paths)
    print(g.shortest_paths[7][6])
    print(g.modularity_matrix[0,0])
    print("degree -> ",g.degree)
    print(g.degree[10])
    print("efficiency -> ", g.efficiency)
    print(g.efficiency[10])

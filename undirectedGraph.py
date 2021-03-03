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
        self.degrees = None
        self.locals_efficiency = None

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
        for row in range(0, 23):
            for col in range(0, 23):
                if df[str(row)][col] == 1:
                    edges.append((row + 1, col + 1))
        print("inside create edges -> ",edges)
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
        plt.savefig(self.patient_name+".png",format="PNG")
        plt.clf()
        # plt.show()
        #   ----- Updating Local Parameters of the Graph ------ #
        self.density = self.density_calc(G)
        self.shortest_paths = self.average_shortest_path(self.shortets_path(G)) # g.average_shortest_path(g.shortest_paths)
        self.modularity_matrix = self.modularity_matrix_calc(G)
        #   ----- Updating Local Parameters of the Graph ------ #
        self.degrees = self.nodes_degree(edges)
        self.locals_efficiency = self.local_efficiency(G)

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
        calc = networkx.floyd_warshall(graph)
        return calc

    def average_shortest_path(self, paths_dict):
        print("inside avg s. path")
        print(paths_dict[2])
        print(paths_dict[1][1])
        print(paths_dict[1][2])
        sum = 0
        full_sum = 0
        for dict in range(1,24):
            for node in paths_dict[dict]:
                if paths_dict[dict][node] == float("inf"):
                    continue
                else:
                    sum = sum + paths_dict[dict][node]
            print(sum)
            full_sum = full_sum + sum
            sum = 0
        avg_shortest_path = full_sum/(22*23)
        print(full_sum)
        return avg_shortest_path


    def modularity_matrix_calc(self, graph):
        """ This function calculates the modularity matrix"""
        return networkx.modularity_matrix(graph)

    def nodes_degree(self,edges):
        degree_matrix = [0] * 23
        print("graph edges -> ",edges)
        for node in edges:
            if(node[0] == node[1]):
                continue
            else:
                degree_matrix[node[0]-1] += 1
        print("degree matrix -> ",degree_matrix)
        return degree_matrix

    def local_efficiency(self, graph):
        from functools import reduce
        lst = []
        for i in range(1,24):
            kes = networkx.single_source_shortest_path_length(graph, i).values()
            if(len(kes)==1):
                lst.append(0)
            else:
                kes = filter(lambda x: x > 0, kes)
                redres = reduce(lambda x, y: x + (1 / y), kes)
                temp = 1 / (23 * 22)
                res = temp * redres
                lst.append(res)
        return lst

    def min_degree(self):
        min = 100
        for node in self.degrees:
            if node < min:
                min = node

        return min

    def max_degree(self):
        max = 0
        for node in self.degrees:
            if node > max:
                max = node

        return max


if __name__ == '__main__':
    # patient = Patient("1","2",'3','4')
    # res = patient.data_section("C:/FinalProj/newdata/healthy/sub10_dc_clean.xlsx", 5)
    # resu_corr = patient.correlation_matrix(res)
    # resu_binary = patient.binary_matrix(resu_corr, 0.4)

    g = Graph()

    gra = g.create_nodes(g.create_edges('Uriel5-D'))
    # print(g.degrees)
    # print(g.degrees[0])
    # print(g.degrees[22])
    # print(gra.number_of_edges(1,1))

    # print(g.local_efficiency(gra))
    # print(type(gra))
    # print(g.density)
    # floywarsh = g.shortest_paths
    # print(floywarsh[1][11])
    # shortpath = dict(networkx.all_pairs_shortest_path(gra))
    # print(gra.shortest_paths)
    # print(g.average_shortest_path(g.shortest_paths))
    print(g.shortets_path(gra))
    # print(g.modularity_matrix[0,0])
    # print("degree -> ",g.degree)
    # print(g.degree[10])
    # print("efficiency -> ", g.efficiency)
    # print(g.efficiency[10])

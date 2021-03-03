
from results import results
import undirectedGraph
import numpy
import pandas
import Research

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


if __name__ == '__main__':
    print_hi('PyCharm')
    # results_test = results("Uri", "C:\\FinalProj\\newdata\\healthy\\test.xlsx")
    # results_test.uploadResults()

# "numpy.einsum" - Evaluates the Einstein summation convention on the operands.
# Using the Einstein summation convention, many common multi-dimensional, linear algebraic array operations can be represented in a simple fashion. In implicit mode einsum computes these values.
# In explicit mode, einsum provides further flexibility to compute other array operations that might not be considered classical Einstein summation operations, by disabling, or forcing summation over specified subscript labels.
a = numpy.arange(36).reshape(6,6)
print(type(a))
# b = pandas.DataFrame(numpy.einsum('ijk->ik',a.reshape(-1,3,a.shape[1]))/3.0)
# print()
# print(a)
# print(b)
# # print(a.shape[1])
# print()
# print(numpy.einsum('ijk->ik',a.reshape(-1,3,a.shape[1])))
# results_test.chooseFile()

# "Choose a file" scenario
result = results("Uri")
# result.uploadResults(result.chooseFile())

# "Choose a data section" scenario with default section = 3
# result.data_section()

# "Choose a data section" scenario with chosen section
# result.data_section(2) # Data Section = 2
# result.data_section(3) # Data Section = 3
# result.data_section(4) # Data Section = 4
res = result.data_section(5) # Data Section = 5

# "Return the correlation matrix" scenario
resu_corr = result.correlation_matrix(res)
# print(resu_corr)

# "Return the binary matrix" scenario
resu_binary = result.binary_matrix(resu_corr, 0.4)
print(resu_binary)

# "Create graph and add Vertices" scenario
g = undirectedGraph.Graph()

for col in range(len(resu_binary)):
    for row in range(0,23):
        if resu_binary[col][row] == 1:
            g.addEdge(col+1, row+1, 0)

for vertex in g.masterList:
    print(vertex," -> ",g.getVertex(vertex).getConnections())

res = Research.research("testmain","testmain","Urimain")
df = pandas.read_csv('Uri.csv')
edges = []
for col in range(0,23):
    for row in range(0,23):
        if df[str(col)][row] == 1:
            edges.append((col+1,row+1))

res.create_nodes(edges)




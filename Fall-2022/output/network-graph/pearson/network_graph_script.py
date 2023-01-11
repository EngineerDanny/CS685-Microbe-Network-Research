import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import igraph as ig

title = 'Crohns Dataset Pearson Correlation Network Graph'
dataset_path = 'crohns_data_log_standard_scaled_transformed.csv'
threshold = 0.2
colors = ['#%06X' % np.random.randint(0, 0xFFFFFF) for i in range(20)]

df = pd.read_csv(dataset_path, header=0)
# take first 20 columns
# df = df.iloc[:, :10]
col_names_list = df.columns.str.replace('f__', '').to_list()
df.columns = [i for i in range(len(col_names_list))]
corr = df.corr()

links = corr.stack().reset_index()
links.columns = ['var1', 'var2', 'value']
links_filtered = links.loc[(links['var1'] != links['var2'] ) & (links['value'] > threshold) ]
links_filtered = links_filtered.reset_index(drop=True)

# number of unique variables in the links_filtered var1 and var2 columns
n_vertices = len(links_filtered['var1'].unique())   
edges = [(int (links_filtered['var1'][i]) , int(links_filtered['var2'][i])) for i in range(len(links_filtered))]
# filter edges list to remove same edges (i.e. (1,2) and (2,1) are the same edge)
edges_filtered = []
for edge in edges:
    (v1, v2) = edge
    if (v2, v1) not in edges_filtered:
         edges_filtered.append(edge)
# edges_filtered = []         
graph = ig.Graph(n_vertices, edges_filtered)
graph["title"] = title
graph.vs["name"] = col_names_list
# give each vertex a unique color

#generate 20 different colors using color codes
graph.vs["color"] = ['lightblue', 'orange', 'lightgreen', 'pink', 'gray']
#TODO: Check if this is the right way to do this
graph.es["sign"] = [ True if links_filtered['value'][i] > 0 else False for i in range(len(links_filtered)) ]
fig, ax = plt.subplots(figsize=(10,10))
ax.set_title(graph["title"], fontsize=25)

ig.plot(
    graph,
    target=ax,
    # layout="circle", # print nodes in a circular layout
    vertex_size=0.3,
    # vertex_color = graph.vs["color"],
    vertex_frame_width=0.2,
    vertex_frame_color="white",
    vertex_label=graph.vs["name"],
    vertex_label_size=19.0,
    edge_width=[2 if sign else 1 for sign in graph.es["sign"]],
    edge_color=["#C25A40" if sign else "#AAA" for sign in graph.es["sign"]],
    vertex_label_color = "white",
)
plt.show()

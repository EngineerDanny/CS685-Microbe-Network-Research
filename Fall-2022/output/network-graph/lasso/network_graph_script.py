import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import igraph as ig

data_list = [
    {
        'title': 'Crohns Dataset LassoCV Fold 0 Network Graph',
        'dataset_path': 'crohns_coef_2022-12-07_12:41_fold_0.csv'
    },
    {
        'title': 'Crohns Dataset LassoCV Fold 1 Network Graph',
        'dataset_path': 'crohns_coef_2022-12-07_12:41_fold_1.csv'
    },
      {
        'title': 'Crohns Dataset LassoCV Fold 2 Network Graph',
        'dataset_path': 'crohns_coef_2022-12-07_12:41_fold_2.csv'
    },
]


def network_graph(title, dataset_path):
    colors = ['#%06X' % np.random.randint(0, 0xFFFFFF) for i in range(20)]

    links = pd.read_csv(dataset_path, header=0)
    links_filtered = links[links['Value'] != 0]
    links_filtered = links_filtered.reset_index(drop=True)


    col_names_list = pd.read_csv('/home/da2343/cs685_fall22/data/crohns_data_log_standard_scaled_transformed.csv', header=0).columns.str.replace('f__', '').to_list()

    print(len(links_filtered))

    # col_names_list = df.columns
    # df.columns = [i for i in range(5)]


    # number of unique variables in the links_filtered var1 and var2 columns

    # loop through the rows of the links_filtered dataframe and add the edges to the graph

    n_vertices = 5
    edges_filtered = [(int(links_filtered['var1'][i]) , int(links_filtered['var2'][i])) for i in range(len(links_filtered))]
    # edges_filtered = []         
    graph = ig.Graph(n_vertices, edges_filtered)
    graph["title"] = title
    graph.vs["name"] = col_names_list
    # give each vertex a unique color

    #generate 20 different colors using color codes
    graph.vs["color"] = ['lightblue', 'orange', 'lightgreen', 'pink', 'gray']
    # graph.vs["color"] = colors

    # print(colors)

    #TODO: Check if this is the right way to do this
    graph.es["sign"] = [True if links_filtered['Value'][i] > 0 else False for i in range(len(links_filtered)) ]
    fig, ax = plt.subplots(figsize=(10,10))
    ax.set_title(graph["title"], fontsize=25)

    ig.plot(
        graph,
        target=ax,
        # layout="circle", # print nodes in a circular layout
        vertex_size=0.3,
        vertex_color = graph.vs["color"],
        vertex_frame_width=0.2,
        vertex_frame_color="white",
        vertex_label=graph.vs["name"],
        vertex_label_size=19.0,
        edge_width=[2 if sign else 1 for sign in graph.es["sign"]],
        edge_color=["#C25A40" if sign else "#5689A3" for sign in graph.es["sign"]],
        vertex_label_color = "white",
    )
    plt.show()
    
for data in data_list:
    title = data['title']
    dataset_path = data['dataset_path']
    network_graph(title, dataset_path)
    

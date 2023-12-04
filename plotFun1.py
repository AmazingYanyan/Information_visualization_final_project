import numpy as np
from matplotlib import pyplot as plt
import networkx as nx
from adjustText import adjust_text

def plotFun1(des_wea_rdic,res_objects,properties_count_dic):
    # initial networks
    G = nx.Graph()
    for key_i in des_wea_rdic.keys():
        for key_j in des_wea_rdic[key_i].keys():
            G.add_edge(key_i, key_j, weight=des_wea_rdic[key_i][key_j])
    print(len(G.nodes()),len(G.edges()))

    ss = [len(c) for c in sorted(nx.connected_components(G), key=len, reverse=True)]
    print(len(ss), max(ss))

    C = max(nx.connected_components(G), key=len)
    S = G.subgraph(C).copy()
    print(len(S.nodes()), len(S.edges()))

    posS = nx.spring_layout(S)
    xS, yS = np.array(list(posS.values())).T


    # plot
    if res_objects[0] == "Description":
        res_objects[0] = "Type"
    plt.figure(figsize=(10, 10))
    plt.scatter(xS, yS, s=20, zorder=2, alpha=0.9)
    for i, j in S.edges():
        xi, yi = posS[i]
        xj, yj = posS[j]
        plt.plot([xi, xj], [yi, yj], color='orange', zorder=1, alpha=0.8)
    plt.savefig(f'{res_objects[0]}_{res_objects[1]}_res.png')


    des_color = '#1f78b4'
    wea_color = '#33a02c'


    color_map = []
    for node in S:
        if node in properties_count_dic['Description']:
            color_map.append(des_color)
        else:
            color_map.append(wea_color)


    sizes = [S.degree(node) * 50 for node in S.nodes()]

    plt.figure(figsize=(15, 15))

    nx.draw_networkx_nodes(S, posS, node_color=color_map, node_size=sizes, alpha=0.8)
    nx.draw_networkx_edges(S, posS, width=1.0, alpha=0.5)

    nx.draw_networkx_labels(S, posS, font_size=10)

    plt.title(f'Relationship between Crime {res_objects[0]} and {res_objects[1]}', size=20)
    plt.axis('off')
    plt.savefig(f'enhanced_{res_objects[0]}_{res_objects[1]}_res.png', dpi=300)


    ###
    posS = nx.spring_layout(S, iterations=50)

    plt.figure(figsize=(15, 15))
    nx.draw_networkx_nodes(S, posS, node_color=color_map, node_size=sizes, alpha=0.8)
    nx.draw_networkx_edges(S, posS, width=1.0, alpha=0.5)

    texts = [plt.text(posS[node][0], posS[node][1], node, fontsize=10) for node in S.nodes()]
    adjust_text(texts)

    plt.title(f'Relationship between Crime {res_objects[0]} and {res_objects[1]}', size=20)
    plt.axis('off')
    plt.savefig(f'enhanced_text_adjusted_{res_objects[0]}_{res_objects[1]}_res.png', dpi=300)

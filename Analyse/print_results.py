import matplotlib.pyplot as plt
import numpy as np

def print_graphs_depends_P(X_origin,X_reconstruct,liste_P,nb_graphs):
    N,P = X_reconstruct[0].shape
    nb_p = len(liste_P)
    print("nb_p",nb_p,"nb_graphs",nb_graphs)
    x = range(N)

    liste_y_origin = X_origin
    liste_y_reconstruct = X_reconstruct

    fig = plt.figure()
    gs = fig.add_gridspec(nrows=nb_graphs ,ncols= nb_p, hspace=0.2, wspace=0)
    axs = gs.subplots(sharex='col', sharey='row')

    for index_P in range(nb_p):
        liste_y_reconstruct_p = liste_y_reconstruct[index_P]
        for index_graph in range(nb_graphs):
            if nb_p == 1:
                axs[index_graph].plot(x, liste_y_origin[:,index_graph],label='Signal Initial')
                axs[index_graph].plot(x, liste_y_reconstruct_p[:,index_graph],label='Signal Reconstruit')
                axs[index_graph].set_title('Graphe {}, P = {}'.format(index_graph,liste_P[index_P]))
            elif nb_graphs == 1:
                axs[index_P].plot(x, liste_y_origin[:,index_graph],label='Signal Initial')
                axs[index_P].plot(x, liste_y_reconstruct_p[:,index_graph],label='Signal Reconstruit')
                axs[index_P].set_title('Graphe {}, P = {}'.format(index_graph,liste_P[index_P]))
            elif nb_graphs>1 and nb_p>1:
                axs[index_graph,index_P].plot(x, liste_y_origin[:,index_graph],label='Signal Initial')
                axs[index_graph,index_P].plot(x, liste_y_reconstruct_p[:,index_graph],label='Signal Reconstruit')
                axs[index_graph,index_P].set_title('Graphe {}, P = {}'.format(index_graph,liste_P[index_P]))

    plt.show()
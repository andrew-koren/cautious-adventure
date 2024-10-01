# Mth 416 code storage for reusability
import networkx as nx
import random
import matplotlib.pyplot as plt
import numpy as np


# HW1
def ceaser_cipher(decoded, k):
    encoded = str()
    for symbol in decoded:
        if symbol == ' ':
            encoded += symbol
        elif ord(symbol)+k > ord('Z'):
            encoded += chr(ord(symbol)+k-26)
        else:
            encoded += chr(ord(symbol)+k)
    return encoded

# HW2    
def hierarchy_pos(G, root=None, width=1., vert_gap = 0.2, vert_loc = 0, xcenter = 0.5):

    '''
    From Joel's answer at https://stackoverflow.com/a/29597209/2966723.  
    Licensed under Creative Commons Attribution-Share Alike 
    
    If the graph is a tree this will return the positions to plot this in a 
    hierarchical layout.
    
    G: the graph (must be a tree)
    
    root: the root node of current branch 
    - if the tree is directed and this is not given, 
      the root will be found and used
    - if the tree is directed and this is given, then 
      the positions will be just for the descendants of this node.
    - if the tree is undirected and not given, 
      then a random choice will be used.
    
    width: horizontal space allocated for this branch - avoids overlap with other branches
    
    vert_gap: gap between levels of hierarchy
    
    vert_loc: vertical location of root
    
    xcenter: horizontal location of root
    '''
    if not nx.is_tree(G):
        raise TypeError('cannot use hierarchy_pos on a graph that is not a tree')

    if root is None:
        if isinstance(G, nx.DiGraph):
            root = next(iter(nx.topological_sort(G)))  #allows back compatibility with nx version 1.11
        else:
            root = random.choice(list(G.nodes))

    def _hierarchy_pos(G, root, width=1., vert_gap = 0.2, vert_loc = 0, xcenter = 0.5, pos = None, parent = None):
        '''
        see hierarchy_pos docstring for most arguments

        pos: a dict saying where all nodes go if they have been assigned
        parent: parent of this branch. - only affects it if non-directed

        '''
    
        if pos is None:
            pos = {root:(xcenter,vert_loc)}
        else:
            pos[root] = (xcenter, vert_loc)
        children = list(G.neighbors(root))
        if not isinstance(G, nx.DiGraph) and parent is not None:
            children.remove(parent)  
        if len(children)!=0:
            dx = width/len(children) 
            nextx = xcenter - width/2 - dx/2
            for child in children:
                nextx += dx
                pos = _hierarchy_pos(G,child, width = dx, vert_gap = vert_gap, 
                                    vert_loc = vert_loc-vert_gap, xcenter=nextx,
                                    pos=pos, parent = root)
        return pos

            
    return _hierarchy_pos(G, root, width, vert_gap, vert_loc, xcenter)

def make_edges_from_code(code, num_layers):
    layers = [['']]
    connections = []


    for i in range(num_layers):
        new_layer = []
        for layer in layers:
            for string in layer:
                left = string+'0'
                right = string+'1'

                if left in set(code.keys()):
                    connections.append((string, code[left]))
                else:
                    new_layer.append(left)
                    connections.append((string, left))

                if right in set(code.keys()):
                    connections.append((string, code[right]))
                else:
                    new_layer.append(right)
                    connections.append((string, right))

        layers.append(new_layer)
    
    return connections, layers

# HW3
def make_huffman(weights):
    assert sum(weights) == 1

    huffman = np.zeros((len(weights),len(weights)))
    huffman[0,:] = weights
    path = []

    for i, layer in enumerate(huffman):
        if i+1 != len(huffman):
            lcopy = np.copy(layer)
            min1 = lcopy.argmin()
            lcopy[min1] += 1
            min2 = lcopy.argmin()

            huffman[i+1] = layer
            huffman[i+1, min1] = 10
            huffman[i+1, min2] += layer.min()
            path.append((min1, min2))
    huffman[huffman==10] = 0

    return huffman, path
    
def path_to_binary(path):
    codewords = ['' for i in range(len(path)+1)]

    for item in np.flipud(path):
        codewords[item[0]] = codewords[item[1]] + '0'
        codewords[item[1]] += '1'

    return codewords
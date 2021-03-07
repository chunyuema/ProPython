from collections import Counter


class NodeTree(object):
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def children(self):
        return (self.left, self.right)


string = 'BCAADDDCCACACAC'
# Calculating frequency
freq = Counter(string)
freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
nodes = freq
# constructing the tree
while len(nodes) > 1:
    (key1, c1), (key2, c2) = nodes[-1], nodes[-2]
    nodes = nodes[:-2]
    node = NodeTree(key1, key2)
    nodes.append((node, c1 + c2))
    nodes = sorted(nodes, key=lambda x: x[1], reverse=True)

print(nodes)

# Main function implementing huffman coding
# update() method adds element(s) to the dictionary if the key is not in the dictionary.
# If the key is in the dictionary, it updates the key with the new value.


def huffman_code_tree(node, left=True, binString=''):
    if type(node) is not NodeTree:
        print(node, 'is string type')
        return {node: binString}
    (l, r) = node.children()
    d = dict()
    d.update(huffman_code_tree(l, True, binString + '0'))
    d.update(huffman_code_tree(r, False, binString + '1'))
    return d


print(nodes[0])
print(nodes[0][0])
huffmanCode = huffman_code_tree(nodes[0][0])
print(huffmanCode)

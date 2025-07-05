from ADT.TreeADT import Tree
from ADT.utils.makeTree import makeTree

tree_dict = {
    1: [2,3],
    2: [7,8],
    3: [5,6],
    5: [50, 60]
}

tree = makeTree(tree_dict)

def calHeight(tree: Tree):
    height = 0
    root = tree.root()
    q = [root]
    parent_depth = {root.element(): 0}
    while q:
        curr = q.pop(0)
        print(curr.element())
        for x in tree.children(curr):
            if tree.isInternal(x):
                q.append(x)
                height = parent_depth[curr.element()] + 1
                parent_depth[x.element()] = height
    print(parent_depth)
    result = []
    for k,v in parent_depth.items():
        if v == height:
            result.append(k)
    return result

print(calHeight(tree=tree))

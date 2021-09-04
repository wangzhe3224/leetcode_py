import collections


def dfs_stack(root) -> list:
    if not root:
        return []
    
    res, stack = [], [(root, "")]  # node + states, 状态记录了到达该节点经历的path
    while stack:
        node, path = stack.pop()
        if not node.left and not node.right:
            res.append(path+str(node.val))

        if node.right:
            stack.append((node.right, path+str(node.val)+'->'))

        if node.left:
            stack.append((node.left, path+str(node.val)+'->'))
    
    return res

def bfs_queue(root):
    if not root:
        return []
    
    res, queue = [], collections.deuqe([(root, "")])
    while queue:
        node, path = queue.popleft()
        if not node.left and not node.right:
            res.append(path+str(node.val))
        
        acc = path+str(node.val)+'->'
        if node.left:
            queue.append((node.left, acc))
        if node.right:
            queue.append((node.right, acc))
        
    return res


def dfs_rec(root, path, res):
    if (not root.left and not root.right):
        res.append(path+str(root.val))

    if root.left:
        dfs_rec(root.left, path+str(root.val)+"->", res)
    if root.right:
        dfs_rec(root.right, path+str(root.val)+"->", res)

def dfs2(root, path):
    if not root:
        return []

    path += str(root.val)

    if not root.left and not root.right:
        return [path]

    path += "->"

    return dfs2(root.left, path) + dfs2(root.right, path)
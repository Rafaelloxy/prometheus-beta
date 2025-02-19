class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def inorder_traversal(root):
    """
    Perform in-order traversal of a binary tree (left -> root -> right)
    
    Args:
        root (Node): Root of the binary tree
    
    Returns:
        list: List of node values in in-order traversal sequence
    """
    def _inorder(node, result):
        if node is None:
            return
        _inorder(node.left, result)
        result.append(node.value)
        _inorder(node.right, result)
    
    result = []
    _inorder(root, result)
    return result

def preorder_traversal(root):
    """
    Perform pre-order traversal of a binary tree (root -> left -> right)
    
    Args:
        root (Node): Root of the binary tree
    
    Returns:
        list: List of node values in pre-order traversal sequence
    """
    def _preorder(node, result):
        if node is None:
            return
        result.append(node.value)
        _preorder(node.left, result)
        _preorder(node.right, result)
    
    result = []
    _preorder(root, result)
    return result

def postorder_traversal(root):
    """
    Perform post-order traversal of a binary tree (left -> right -> root)
    
    Args:
        root (Node): Root of the binary tree
    
    Returns:
        list: List of node values in post-order traversal sequence
    """
    def _postorder(node, result):
        if node is None:
            return
        _postorder(node.left, result)
        _postorder(node.right, result)
        result.append(node.value)
    
    result = []
    _postorder(root, result)
    return result
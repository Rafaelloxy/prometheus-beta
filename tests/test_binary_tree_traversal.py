import pytest
from src.binary_tree_traversal import Node, inorder_traversal, preorder_traversal, postorder_traversal

def test_inorder_traversal():
    # Create a simple binary tree
    #       4
    #     /   \
    #    2     6
    #   / \   / \
    #  1   3 5   7
    root = Node(4)
    root.left = Node(2)
    root.right = Node(6)
    root.left.left = Node(1)
    root.left.right = Node(3)
    root.right.left = Node(5)
    root.right.right = Node(7)
    
    assert inorder_traversal(root) == [1, 2, 3, 4, 5, 6, 7]

def test_preorder_traversal():
    # Same tree structure as previous test
    root = Node(4)
    root.left = Node(2)
    root.right = Node(6)
    root.left.left = Node(1)
    root.left.right = Node(3)
    root.right.left = Node(5)
    root.right.right = Node(7)
    
    assert preorder_traversal(root) == [4, 2, 1, 3, 6, 5, 7]

def test_postorder_traversal():
    # Same tree structure as previous test
    root = Node(4)
    root.left = Node(2)
    root.right = Node(6)
    root.left.left = Node(1)
    root.left.right = Node(3)
    root.right.left = Node(5)
    root.right.right = Node(7)
    
    assert postorder_traversal(root) == [1, 3, 2, 5, 7, 6, 4]

def test_empty_tree():
    # Test with None (empty tree)
    assert inorder_traversal(None) == []
    assert preorder_traversal(None) == []
    assert postorder_traversal(None) == []

def test_single_node_tree():
    # Test with single node tree
    root = Node(1)
    
    assert inorder_traversal(root) == [1]
    assert preorder_traversal(root) == [1]
    assert postorder_traversal(root) == [1]
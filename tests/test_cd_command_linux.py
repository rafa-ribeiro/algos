import pytest
from algos.cd_command_linux import Node

def test__node_class():
    root = Node('home')
    root.append(Node('rafael'))
    dev_dir = Node('dev')
    root.append(dev_dir)
    root.append(Node('documents'))
    python_dir = Node('python_projects')
    dev_dir.append(python_dir)

    assert len(root.childs) == 3
    assert len(dev_dir.childs) == 1
    assert len(python_dir.childs) == 0

    assert root.pwd() == "/home"
    assert dev_dir.pwd() == "/home/dev"
    assert python_dir.pwd() == "/home/dev/python_projects"
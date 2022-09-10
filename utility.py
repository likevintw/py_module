
import json
from math import e
import os
import time
import hashlib


def check_sum(filename):
    result = None
    with open(filename, 'rb') as file:
        result = hashlib.md5(file.read()).hexdigest()
    # result = hashlib.md5(open(filename, 'rb').read()).hexdigest()
    return result


def replace_string_in_list(data_list, target, replaced):
    result = []
    for i in data_list:
        buffer = i.replace(target, replaced)
        result.append(buffer)
    return result


def remove_string_in_list(data_list, target):
    result = []
    for i in data_list:
        if not target in i:
            result.append(i)
    return result


def keep_string_in_list(data_list, target):
    result = []
    for i in data_list:
        if target in i:
            result.append(i)
    return result


def import_json_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data


def export_json_file(export_file_name, data):
    with open(export_file_name, 'w') as file:
        json.dump(data, file)


def import_file(file_path):
    result = []
    try:
        with open(file_path, mode='r') as ImportFile:
            data = ImportFile.readlines()  # Read whole line
        for i in data:
            i = i.strip()  # Remove '\n'
            result.append(i)

    except e:
        return None, "import_file() Error, {}".format(e)

    return result


def export_file(file_path, data):
    with open(file_path, mode='w') as file:
        for i in data:
            file.write(i+"\n")


def get_symbol_number_in_string(string, symbol):
    if len(symbol) != 1:
        return "len(symbol) must be 1"
    numbers = 0
    for i in string:
        if i == "/" or i == "\ ":
            numbers += 1
    return numbers


def run_single_search(folder_path):
    file_path = []
    direct_path = []
    try:
        for file_name in os.listdir(folder_path):
            if os.path.isdir(folder_path+'/'+file_name):
                direct_path.append(folder_path+'/'+file_name)
            else:
                file_path.append(folder_path+'/'+file_name)
    except:
        print("The is no file in the {}".format(folder_path))
    finally:
        return file_path, direct_path


def remove_last_slash(string):
    while True:
        if len(string) == 0:
            break
        elif string[-1] == "/":
            string = string[:len(string)-1]
        else:
            break
    return string


def get_file_and_direct_path(folder_path) -> list:
    folder_path = remove_last_slash(folder_path)
    file_list = []
    direct_list = []

    data = os.walk(folder_path)

    for location, direct, file in data:
        if len(file) > 0:
            for j in file:
                file_list.append("{}/{}".format(location, j))
        direct_list.append(location)
    return file_list, direct_list


def separate_date_and_title(string) -> list:
    pass


def get_time_elapse(function):
    deltaTime = time.perf_counter()
    time.sleep(function)
    deltaTime = time.perf_counter() - deltaTime
    return show_float_number(deltaTime, 3)


def show_float_number(float, show_number):
    return round(float, show_number)


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @staticmethod
    def turn_list_to_tree(input_list):
        root = None
        for i in input_list:
            root = TreeNode.insert(root, i)
        return root

    @staticmethod
    def insert(root, value):
        if not root:
            return TreeNode(value)
        if value <= root.val:
            root.left = TreeNode.insert(root.left, value)
        else:
            root.right = TreeNode.insert(root.right, value)
        return root

    @staticmethod
    def show_preorder_traversal(root):
        '''
        middle->left->right
        '''
        result = []

        def preorder_traversal(root):
            result.append(root.val)
            if root.left:
                preorder_traversal(root.left)
            if root.right:
                preorder_traversal(root.right)
        preorder_traversal(root)
        return result

    @staticmethod
    def show_inorder_traversal(root):
        '''
        left->middle->right
        '''
        result = []

        def inorder_traversal(root):
            if root.left:
                inorder_traversal(root.left)
            result.append(root.val)
            if root.right:
                inorder_traversal(root.right)
        inorder_traversal(root)
        return result

    @staticmethod
    def show_postorder_traversal(root):
        '''
        left->right->middle
        '''
        result = []

        def postorder_traversal(root):
            if root.left:
                postorder_traversal(root.left)
            if root.right:
                postorder_traversal(root.right)
            result.append(root.val)
        postorder_traversal(root)
        return result

    @staticmethod
    def traversal_BFS(root):
        '''
        Breadth First Search
        '''
        result = []
        queue = [root]
        while len(queue) > 0:
            cur = queue.pop(0)
            result.append(cur.val)
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)

        return result

    @staticmethod
    def traversal_DFS(root):
        '''
        Depth First Search
        '''
        result = []
        pass


class File(object):

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.open_file = open(self.filename, self.mode)
        return self.open_file

    def __exit__(self, type, value, traceback):
        self.open_file.close()

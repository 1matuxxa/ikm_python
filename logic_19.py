class TreeNode:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree: #бинарное дерево строится по заданным путям через узы бинарного дерева выше
    def __init__(self):
        #корень: 0
        self.root = TreeNode(0)

    def insert(self, value, path):
        """
        Вставка элемента по бинарному коду
        0 - переход к левому потомку, 1 - к правому
        """
        current = self.root
        
        for char in path:
            if char == '0':
                if current.left is None:
                    current.left = TreeNode()
                current = current.left
            elif char == '1':
                if current.right is None:
                    current.right = TreeNode()
                current = current.right
            else:
                raise ValueError(f"Недопустимый символ '{char}'. Разрешены только '0' и '1'")

        if current.value is not None:
            raise ValueError(f"Путь '{path}' уже занят значением {current.value}. Дерево не может быть построено")
        
        current.value = value

    def traverse_inorder(self, node): #симметричный обход (левый-корень-правый) для проверки структуры
        result = []
        if node:
            result.extend(self.traverse_inorder(node.left))
            if node.value is not None:
                result.append(node.value)
            result.extend(self.traverse_inorder(node.right))
        return result
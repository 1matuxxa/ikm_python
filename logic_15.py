class StackNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class CustomStack: #вызываем стек, основанный на односвязном списке
    def __init__(self):
        self.top = None

    def push(self, value):
        new_node = StackNode(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            raise IndexError("Стек пуст, недостаточно операндов")
        value = self.top.value
        self.top = self.top.next
        return value

def evaluate_postfix(expression: str): #вычисление обратной польской записи. Ввод чисел и знаков через пробел
    if not expression.strip():
        raise ValueError("Пустая строка. Вы ничего не ввели")
    stack = CustomStack()
    tokens = expression.split(' ')

    for token in tokens:
        if not token:
            continue
        if token in ('+', '-', '*', '/'):
            #извлекаем правый, затем левый операнд
            b = stack.pop()
            a = stack.pop()
            
            if token == '+':
                stack.push(a + b)
            elif token == '-':
                stack.push(a - b)
            elif token == '*':
                stack.push(a * b)
            elif token == '/':
                if b == 0:
                    raise ZeroDivisionError("Деление на ноль невозможно")
                stack.push(a / b)
        else:
            try:
                val = float(token)
                if val < 0:
                    raise ValueError(f"'{token}' не является положительным числом")
                stack.push(val)
            except ValueError as e:
                raise ValueError(f"Некорректный ввод: {token}. {e}")

    result = stack.pop()
    
    #проверка: если данные в стеке остались, то выражение было введено некорректно
    try:
        stack.pop()
        raise ValueError("Слишком много операндов и не хватает знаков операций")
    except IndexError:
        return result
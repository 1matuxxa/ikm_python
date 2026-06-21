import logic_19

def main():
    while True:
        print("="*45)
        print("МЕНЮ: ВАРИАНТ 19 (БИНАРНОЕ ДЕРЕВО КОДОВ)")
        print("="*45)
        print("1. Построить дерево и вывести обход")
        print("2. Выход")
        print("="*45)
        
        choice = input("Выберите действие (1-2): ")
        
        if choice == '1':
            try:
                n_str = input("Введите количество чисел для добавления: ")
                if not n_str.strip():
                    raise ValueError("Пустая строка. Вы ничего не ввели.")
                if not n_str.isdigit():
                    raise ValueError("Количество должно быть целым положительным числом")
                n = int(n_str)
                if n <= 0:
                    raise ValueError("N должно быть больше нуля")
                    
                tree = logic_19.BinaryTree()
                
                for i in range(n):
                    print(f"--- Элемент {i + 1} ---")
                    val_str = input("Значение (целое число): ")
                    if not val_str.strip():
                        print("Пустая строка. Вы ничего не ввели.")
                        continue
                    path = input("Двоичный код пути (0 и 1): ")
                    if not path.strip():
                        print("Пустая строка. Путь не может быть пустым.")
                        continue
                    
                    try:
                        val = int(val_str)
                        tree.insert(val, path)
                        print("-> Добавлено.")
                    except ValueError as e:
                        print(f"-> Ошибка при добавлении: Введите допустимое число!")
                        print("-> Попробуйте начать заново или продолжить с текущим деревом")
                        
                print("=== ИТОГ ===")
                print("Дерево построено")
                print(f"Симметричный обход: {tree.traverse_inorder(tree.root)}")
                
            except Exception as e:
                print(f"-> Ошибка: {e}")
                
        elif choice == '2':
            print("Завершение работы программы")
            break
        else:
            print("-> Ошибка: Неверный пункт меню")

if __name__ == "__main__":
    main()
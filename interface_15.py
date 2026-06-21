import logic_15

def main():
    while True:
        print("="*45)
        print("МЕНЮ: ВАРИАНТ 15 (ОБРАТНАЯ ПОЛЬСКАЯ ЗАПИСЬ)")
        print("="*45)
        print("1. Вычислить выражение")
        print("2. Выход")
        print("="*45)
        
        choice = input("Выберите действие (1-2): ")
        
        if choice == '1':
            print("Введите выражение. Числа и знаки разделяйте одним пробелом.")
            print("Пример: 5 2 / (означает 5 / 2)")
            expression = input("Ввод: ")
            try:
                result = logic_15.evaluate_postfix(expression)
                print(f"Результат: {result}")
            except Exception as e:
                print(f"Ошибка выполнения: {e}")
        elif choice == '2':
            print("Завершение работы программы.")
            break
        else:
            print("-> Ошибка: Неверный пункт меню.")

if __name__ == "__main__":
    main()
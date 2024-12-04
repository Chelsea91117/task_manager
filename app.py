from typing import List
from manager import TaskManager
from storage import Storage
from task_model import Task
from time import sleep


class App:
    def __init__(self, storage_path: str):
        """Инициализация приложения с заданным хранилищем."""
        self.manager = TaskManager(Storage(storage_path))

    def run(self):
        """Запуск главного цикла приложения."""
        while True:
            choice = self.display_menu()
            if choice == "1":
                self.handle_view_all_tasks()
            elif choice == "2":
                self.handle_view_tasks_by_category()
            elif choice == "3":
                self.handle_add_task()
            elif choice == "4":
                self.handle_edit_task()
            elif choice == "5":
                self.handle_edit_task_status()
            elif choice == "6":
                self.handle_delete_task_by_id()
            elif choice == "7":
                self.handle_delete_task_by_category()
            elif choice == "8":
                self.handle_search_tasks()
            elif choice == "9":
                print("Выход из программы.")
                break
            else:
                print("Неверный выбор. Попробуйте еще раз.")
                sleep(3)

    @staticmethod
    def display_menu() -> str:
        """Вывод меню и получение выбора пользователя."""
        border = "=" * 45
        print(f"""
    {border}
        Добро пожаловать в Менеджер задач!
    {border}
        1. Посмотреть все задачи
        2. Посмотреть все задачи по категориям
        3. Добавить задачу
        4. Изменить задачу
        5. Изменить статус задачи
        6. Удаление по ID
        7. Удаление по категории
        8. Поиск задачи по ключевому слову

        9. Выйти
    {border}    
        """)
        return input("Выберите действие: ")

    @staticmethod
    def display_tasks(tasks: List[Task]) -> None:
        """Форматированный вывод задач."""
        if not tasks:
            print("Список задач пуст.")
        else:
            for task in tasks:
                print(task)

    @staticmethod
    def get_task_input():
        """Запрашивает ввод пользователя для полей задачи."""
        title = input("Введите название задачи: ")
        description = input("Введите описание задачи: ")
        category = input("Введите категорию задачи: ")
        due_date = input("Введите дату выполнения задачи (ГГГГ-ММ-ДД): ")
        priority = input("Введите приоритет задачи (низкий, средний, высокий): ")
        return {"title": title, "description": description, "category": category, "due_date": due_date, "priority": priority}

    def handle_view_all_tasks(self):
        """Обработчик для отображения всех задач."""
        tasks = self.manager.view_tasks()
        self.display_tasks(tasks)
        sleep(3)

    def handle_view_tasks_by_category(self):
        """Обработчик для отображения задач по категориям."""
        tasks = self.manager.view_tasks_by_category()
        self.display_tasks(tasks)
        sleep(3)

    def handle_add_task(self):
        """Обработчик для добавления задачи."""
        try:
            task_data = self.get_task_input()
            new_task = self.manager.add_task(**task_data)
            print(f"Задача '{new_task.title}' успешно добавлена.")
        except ValueError as e:
            print(f"Ошибка: {e}")
        sleep(3)

    def handle_edit_task(self):
        """Обработчик для редактирования задачи."""
        try:
            task_id = int(input("Введите ID задачи для редактирования: "))
            task = self.manager.find_task_by_id(task_id)
            print(f"Текущие данные задачи: {task}")
            print("Оставьте поле пустым, если не хотите его изменять.")

            updates = self.get_task_input()
            # Удаляем пустые значения
            updates = {key: value for key, value in updates.items() if value.strip()}
            if updates:
                result = self.manager.edit_task(task_id, **updates)
                print(result)
            else:
                print("Изменений не внесено.")
        except ValueError as e:
            print(f"Ошибка: {e}")
        sleep(3)

    def handle_edit_task_status(self):
        """Обработчик для редактирования статуса задачи."""
        try:
            task_id = int(input("Введите ID задачи для редактирования статуса: "))
            new_status = input("Введите новый статус задачи (выполнена/не выполнена): ")
            result = self.manager.edit_task_status(task_id, new_status)
            print(result)
        except ValueError as e:
            print(f"Ошибка: {e}")

    def handle_delete_task_by_id(self):
        """Обработчик для удаления задачи по ID."""
        try:
            task_id = int(input("Введите ID задачи для удаления: "))
            message = self.manager.delete_task_by_id(task_id)
            print(message)
        except ValueError as e:
            print(f"Ошибка: {e}")
        sleep(3)

    def handle_delete_task_by_category(self):
        """Обработчик для удаления задач по категории."""
        category = input("Введите категорию для удаления задач: ")
        message = self.manager.delete_tasks_by_category(category)
        print(message)
        sleep(3)

    def handle_search_tasks(self):
        """Обработчик для поиска задач по ключу и значению."""
        key = input("Введите ключ для поиска (например, title, category, priority, status): ")
        value = input("Введите значение для поиска: ")
        try:
            results = self.manager.search_tasks(key, value)  # Ожидается список задач
            if not results:
                print(f"Нет задач по {key}: {value}.")
            else:
                print(f"Найдено {len(results)} задач:")
                for task in results:
                    print(task)
        except ValueError as e:
            print(f"Ошибка: {e}")
        sleep(3)


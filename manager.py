from typing import List
from task_model import Task
from storage import Storage

class TaskManager:
    def __init__(self, storage: Storage):
        self.storage = storage
        self.tasks: List[Task] = self.storage.load_data()

    def view_tasks(self) -> List[Task]:
        """Вывод всех задач."""
        return self.tasks

    def view_tasks_by_category(self) -> list:
        """Вывод всех задач по категориям."""
        # Сортируем задачи по категориям
        grouped_tasks = sorted(self.tasks, key=lambda t: t.category)

        # Формируем строку для отображения
        result = []
        current_category = None
        for task in grouped_tasks:
            if task.category != current_category:
                current_category = task.category
                result.append(f"\nКатегория: {current_category}")
            result.append(f"  - {task.title}: {task.description}")

        return result

    def add_task(self, title: str, description: str, category: str,
                 due_date: str, priority: str) -> Task:
        """Добавление новой задачи."""
        new_id = max((task.id for task in self.tasks), default=0) + 1
        new_status = "не выполнена"

        new_task = Task(
            id=new_id,
            title=title,
            description=description,
            category=category,
            due_date=due_date,
            priority=priority,
            status=new_status
        )

        self.tasks.append(new_task)
        self.storage.save_data(self.tasks)
        return new_task

    def find_task_by_id(self, task_id: int) -> Task:
        """Поиск задачи по id."""
        if not isinstance(task_id, int) or task_id < 1:
            raise ValueError("ID книги должен быть положительным числом.")

        for task in self.tasks:
            if task.id == task_id:
                return task

        raise ValueError(f"Задача с ID {task_id} не найдена.")

    def edit_task(self, task_id: int, **kwargs) -> str:
        """Изменение задачи с передачей новых данных."""
        task = self.find_task_by_id(task_id)

        try:
            task.update_fields(**kwargs)
        except ValueError as e:
            return str(e)

        self.storage.save_data(self.tasks)
        return f"Задача с ID {task_id} успешно обновлена."

    def edit_task_status(self, task_id: int, new_status: str) -> str:
        """Изменение статуса задачи."""
        task = self.find_task_by_id(task_id)

        try:
            task.update_fields(status=new_status)
        except ValueError as e:
            return str(e)

        self.storage.save_data(self.tasks)
        return f"Статус задачи {task_id} успешно обновлен на '{new_status}'."

    def search_tasks(self, key: str, value: str) -> List[Task]:
        """Ищет задачи по заданному ключу и значению."""
        tasks = self.storage.load_data()
        valid_keys = ["title", "category", "priority", "status"]

        if key not in valid_keys:
            raise ValueError(f"Ключ '{key}' недопустим. Возможные значения: {', '.join(valid_keys)}")
        # Фильтрация задач
        results = [task for task in tasks if getattr(task, key, None) == value]
        return results

    def delete_task_by_id(self, task_id: int) -> str:
        """Удаление задачи по идентификатору."""
        task = self.find_task_by_id(task_id)
        self.tasks.remove(task)
        self.storage.save_data(self.tasks)
        return f"Задача с ID {task_id} успешно удалена."

    def delete_tasks_by_category(self, category: str) -> str:
        """Удаление задач по категории."""
        category = category.strip().lower()
        filtered_tasks = [task for task in self.tasks if task.category == category]

        if not filtered_tasks:
            return f"Нет задач в категории '{category}' для удаления."

        for task in filtered_tasks:
            self.tasks.remove(task)
        self.storage.save_data(self.tasks)
        return f"Все задачи в категории '{category}' успешно удалены."

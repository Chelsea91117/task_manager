from datetime import datetime


class Task:
    ALLOWED_CATEGORIES = ["работа", "обучение", "личное"]
    ALLOWED_PRIORITIES = ["низкий", "средний", "высокий"]
    ALLOWED_STATUSES = ["выполнена", "не выполнена"]

    def __init__(self, id: int, title: str, description: str, category: str,
                 due_date: str, priority: str, status: str) -> None:
        """Инициализация новой задачи с предоставленными атрибутами."""
        self.id = id
        self.title = title
        self.description = description
        self.category = category
        self.due_date = due_date
        self.priority = priority
        self.status = status
        self.validate_fields()  # Проверяем поля при создании задачи

    def validate_fields(self) -> None:
        """Проверка всех полей задачи."""
        # Проверка id
        if self.id < 0:
            raise ValueError("ID задачи должен быть неотрицательным целым числом.")

        # Проверка названия
        if not self.title:
            raise ValueError("Название задачи должно быть непустой строкой.")

        # Проверка описания
        if not self.description:
            raise ValueError("Описание задачи должно быть непустой строкой.")

        # Проверка категории
        category = self.category.strip().lower()
        if category not in self.ALLOWED_CATEGORIES:
            raise ValueError(f"Недопустимая категория задачи: {category}. "
                             f"Допустимые значения: {', '.join(self.ALLOWED_CATEGORIES)}.")

        # Проверка даты выполнения
        try:
            due_date_obj = datetime.strptime(self.due_date, "%Y-%m-%d")
        except ValueError:
            raise ValueError(f"Ошибка: '{self.due_date}' не является корректной датой. Используйте формат ГГГГ-ММ-ДД.")

        if due_date_obj < datetime.now():
            raise ValueError(f"Ошибка: дата выполнения '{self.due_date}' не может быть в прошлом.")

        # Проверка приоритета
        priority = self.priority.strip().lower()
        if priority not in self.ALLOWED_PRIORITIES:
            raise ValueError(f"Недопустимый приоритет задачи: {priority}. "
                             f"Допустимые значения: {', '.join(self.ALLOWED_PRIORITIES)}.")

        # Проверка статуса
        status = self.status.strip().lower()
        if status not in self.ALLOWED_STATUSES:
            raise ValueError(f"Недопустимый статус задачи: {status}. "
                             f"Допустимые значения: {', '.join(self.ALLOWED_STATUSES)}.")

    def update_fields(self, title=None, description=None, category=None,
                      due_date=None, priority=None, status=None) -> None:
        """Обновляет поля задачи, если переданы новые значения."""
        if title is not None:
            self.title = title

        if description is not None:
            self.description = description

        if category is not None:
            self.category = category

        if due_date is not None:
            self.due_date = due_date

        if priority is not None:
            self.priority = priority

        if status is not None:
            self.status = status

        self.validate_fields()  # Проверяем поля после обновления

    def to_dict(self) -> dict:
        """Создает словарь из экземпляра."""
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "category": self.category,
            "due_date": self.due_date,
            "priority": self.priority,
            "status": self.status
        }

    @classmethod
    def from_dict(cls, data: dict) -> 'Task':
        """Создает экземпляр Task из словаря."""
        try:
            return cls(
                id=data["id"],
                title=data["title"],
                description=data["description"],
                category=data["category"],
                due_date=data["due_date"],
                priority=data["priority"],
                status=data["status"],
            )
        except KeyError as e:
            raise ValueError(f"Отсутствует необходимое поле '{e.args[0]}'.")

    def __str__(self) -> str:
        return (f"ID: {self.id:<3} | "
                f"Название: {self.title:<10} | "
                f"Описание: {self.description:<20} | "
                f"Категория: {self.category:<10} | "
                f"Срок: {self.due_date:<10} | "
                f"Приоритет: {self.priority:<10} | "
                f"Статус: {self.status:<10}")



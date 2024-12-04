from datetime import datetime


class Task:
    ALLOWED_CATEGORIES = {"работа", "обучение", "личное"}
    ALLOWED_PRIORITIES = {"низкий", "средний", "высокий"}
    ALLOWED_STATUSES = {"выполнена", "не выполнена"}

    def __init__(self, id: int, title: str, description: str, category: str,
                 due_date: str, priority: str, status: str) -> None:
        """Инициализация новой задачи с предоставленными атрибутами."""
        if id < 0:
            raise ValueError("ID задачи должен быть неотрицательным целым числом.")
        if not title:
            raise ValueError("Название задачи должно быть непустой строкой.")
        if not description:
            raise ValueError("Описание задачи должно быть непустой строкой.")

        category = category.strip().lower()
        if category not in self.ALLOWED_CATEGORIES:
            raise ValueError(f"Недопустимая категория задачи: {category}. "
                             f"Допустимые значения: {self.ALLOWED_CATEGORIES}.")

        try:
            due_date_obj = datetime.strptime(due_date, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Срок выполнения должен быть в формате 'YYYY-MM-DD'.")

        priority = priority.strip().lower()
        if priority not in self.ALLOWED_PRIORITIES:
            raise ValueError(f"Недопустимый приоритет задачи: {priority}. "
                             f"Допустимые значения: {self.ALLOWED_PRIORITIES}.")

        status = status.strip().lower()
        if status not in self.ALLOWED_STATUSES:
            raise ValueError(f"Недопустимый статус задачи: {status}. "
                             f"Допустимые значения: {self.ALLOWED_STATUSES}.")

        self.id = id
        self.title = title
        self.description = description
        self.category = category
        self.due_date = due_date_obj
        self.priority = priority
        self.status = status

    def to_dict(self) -> dict:
        """Создает словарь из экземпляра."""
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "category": self.category,
            "due_date": self.due_date.strftime("%Y-%m-%d"),
            "priority": self.priority,
            "status": self.status
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Task":
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
        return (f"Task(id={self.id}, title='{self.title}', description='{self.description}', "
                f"category='{self.category}', due_date={self.due_date.strftime('%Y-%m-%d')}, "
                f"priority='{self.priority}', status='{self.status}')")
import json
from typing import List
from task_model import Task

class Storage:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def load_data(self) -> List[Task]:
        """Загрузка данных из файла"""
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                data = json.load(file)
                return [Task.from_dict(task) for task in data]
        except FileNotFoundError:
            return []
        except json.decoder.JSONDecodeError:
            raise ValueError("Ошибка при чтении файла хранения данных.")
        except Exception as e:
            raise ValueError(f"Неизвестная ошибка: {e}")


    def save_data(self, tasks: List[Task]) -> None:
        """Сохранение данных в файл."""
        try:
            with open(self.file_path, "w", encoding="utf-8") as file:
                json.dump([task.to_dict() for task in tasks], file, ensure_ascii=False, indent=4)
        except OSError as e:
            raise IOError(f"Ошибка при записи данных в файл: {self.file_path}. {e}")

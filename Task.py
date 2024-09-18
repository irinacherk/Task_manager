from datetime import datetime

class Task:
    def __init__(self, description, deadline):
        self.description = description
        self.deadline = deadline
        self.completed = False  # По умолчанию задача не выполнена

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "Выполнено" if self.completed else "Не выполнено"
        return f"Задача: {self.description}, Срок: {self.deadline}, Статус: {status}"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, deadline):
        task = Task(description, deadline)
        self.tasks.append(task)

    def mark_task_completed(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].mark_completed()

    def get_current_tasks(self):
        # Возвращаем список невыполненных задач
        return [task for task in self.tasks if not task.completed]

    def show_tasks(self):
        for i, task in enumerate(self.tasks):
            print(f"{i}. {task}")


# Пример использования
manager = TaskManager()

# Добавим несколько задач с датами относительно 18 сентября 2024 года
manager.add_task("Закончить проект по Python", "2024-09-18")  # Сегодня
manager.add_task("Купить продукты", "2024-09-19")  # Завтра
manager.add_task("Позвонить клиенту", "2024-09-17")  # Вчера
manager.add_task("Подготовить презентацию", "2024-09-20")  # Через два дня
manager.add_task("Записаться к врачу", "2024-09-15")  # Истек срок

# Покажем все задачи
print("Все задачи:")
manager.show_tasks()

# Отметим несколько задач как выполненные
manager.mark_task_completed(0)  # Закончить проект по Python
manager.mark_task_completed(2)  # Позвонить клиенту

# Покажем все задачи еще раз, чтобы увидеть изменения
print("\nВсе задачи после выполнения некоторых:")
manager.show_tasks()

# Покажем только текущие (невыполненные) задачи
print("\nТекущие задачи (невыполненные):")
for task in manager.get_current_tasks():
    print(task)

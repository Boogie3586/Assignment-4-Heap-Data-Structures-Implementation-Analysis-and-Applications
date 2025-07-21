class Task:
    def __init__(self, task_id, priority, arrival_time, deadline):
        self.task_id = task_id
        self.priority = priority
        self.arrival_time = arrival_time
        self.deadline = deadline

    def __lt__(self, other):
        # Min-heap based on priority
        return self.priority < other.priority

    def __repr__(self):
        return f"Task(id={self.task_id}, priority={self.priority})"
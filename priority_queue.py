import heapq
from task import Task

class PriorityQueue:
    def __init__(self):
        self.heap = []

    def insert(self, task: Task):
        heapq.heappush(self.heap, task)

    def extract_min(self):
        return heapq.heappop(self.heap) if self.heap else None

    def decrease_key(self, task_index, new_priority):
        if 0 <= task_index < len(self.heap):
            self.heap[task_index].priority = new_priority
            heapq.heapify(self.heap)

    def is_empty(self):
        return len(self.heap) == 0
from heapsort import heapsort
from priority_queue import PriorityQueue
from task import Task

if __name__ == "__main__":
    # Heapsort example
    arr = [10, 3, 76, 34, 23, 32]
    print("Original array:", arr)
    heapsort(arr)
    print("Sorted array:", arr)

    # Priority Queue example
    pq = PriorityQueue()
    pq.insert(Task(1, 3, 0, 10))
    pq.insert(Task(2, 1, 1, 5))
    pq.insert(Task(3, 2, 2, 8))

    print("\nExtracting tasks by priority:")
    while not pq.is_empty():
        task = pq.extract_min()
        print(task)
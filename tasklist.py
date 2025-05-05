"""Represents a list of task objects
    Attributes:
        _tasklist (Task): list of task objects 
        _n (int) : counter for iterator
    """
import task
class Tasklist:
    def __init__(self):
        self._tasklist = []
        file = open("tasklist.txt")
        for line in file:
            line = line.strip()
            if line:
                description, date, time = line.split(',')
                self._tasklist.append(task.Task(description, date, time))
        self._tasklist.sort()

    def add_task(self, desc, date, time):
        new_task = task.Task(desc, date, time)
        self._tasklist.append(new_task)
        self._tasklist.sort()

    def get_current_task(self):
        return self._tasklist[0]
    
    def mark_complete(self):
        return self._tasklist.pop(0)
    
    def postpone_task(self, date, time):
        removed_task = self._tasklist.pop(0)
        self._tasklist.append(task.Task(removed_task.description, date, time))
        self._tasklist.sort()
    
    def save_file(self):
        file = open("tasklist.txt", "w")
        for task in self._tasklist:
            file.write(repr(task)+ '\n')
    
    def __len__(self): #returns the number of Task objects in the tasklist
        return len(self._tasklist)
    
    def __iter__(self): #initialize the iterator attributes n and return self
        self._n = 0
        return self
    
    def __next__(self): #iterate one position and stops it when iterator reaches the end of tasklist, otherwise return the task at the index.
        self._n += 1
        if self._n >= len(self._tasklist):
            raise StopIteration
        else:
            return self._tasklist[self._n]



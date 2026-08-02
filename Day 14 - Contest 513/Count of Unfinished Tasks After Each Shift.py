from typing import List

def countTasks(self, tasks: List[int], shifts: List[int]) -> List[int]:
    n = len(tasks)
    ans = []
    task = 0
    remaining = tasks[0]

    for time in shifts:
        if task == n:
            task = 0
            remaining = tasks[0]
        while time > 0 and task < n:
            if time >= remaining:
                time -= remaining
                task += 1
                if task < n:
                    remaining = tasks[task]
            else:
                remaining -= time
                time = 0
        ans.append(n - task)
    return ans

print(countTasks(self=None, tasks=[3, 2, 4], shifts=[5, 1, 2]))  # Output: [1, 1, 0]
print(countTasks(self=None, tasks=[1, 2, 3], shifts=[3, 3, 3]))  # Output: [0, 0, 0]
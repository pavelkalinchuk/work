tasks = []
with open('tasks.txt', 'r') as f:
    for i in f:
        tasks.append(i)
    # tasks = f.readlines()
    # tasks_list = tasks.split()
print(tasks)
# print(tasks_list)

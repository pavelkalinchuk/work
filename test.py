import json
import pathlib
from pathlib import Path

# tasks = []
# with open('tasks.txt', 'r') as f:
#     for i in f:
#         tasks.append(i)
#     # tasks = f.readlines()
#     # tasks_list = tasks.split()
# print(tasks)
# # print(tasks_list)


path = pathlib.Path.home()
# path_file = C:\Users\p.kalinchuk\work\autotest\test_motor_api\tests\4_mandatory_parameters\calculation_test_data.json
path_file = Path(path, 'work', 'b2b_motors', 'json',
                 'КАСКО.Котировка.Запрос.Дефект.json')

# path_file = Path(path, 'work', 'autotest', 'test_motor_api', 'tests', '4_mandatory_parameters', 'calculation_test_data.json')

with open(path_file, 'r', encoding="utf8") as f:
    test_data = json.load(f)

for i in (test_data['additional_service']):
    print(i)

print(test_data['additional_service'][0]['isn'])

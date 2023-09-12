import os
import jinja2
from jinja2 import Environment, FileSystemLoader

old_salary = 1200
workers = [
    {"name": "Alice", "bonus": 85},
    {"name": "Bob", "bonus": 40},
    {"name": "Charlie", "bonus": 92},
    {"name": "Dave", "bonus": 50},
]

environment = Environment(loader=FileSystemLoader(""))
template = environment.get_template("salary.txt")

for worker in workers:
    bonus = worker.get("bonus")
    content = template.render(
        name=worker.get("name"),
        bonus=bonus,
        salary=old_salary+bonus
    )
    print(content)

# content = template.render(
#     students=students,
#     max_score=max_score
# )

# with open('final_result.txt', 'w') as file:
#     file.write(content)

# file_size = os.path.getsize('final_result.txt')
# print(file_size)

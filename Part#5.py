"""my_dict = {
    "имя": "Николай",
    "возраст": 30,#yrs
    "пол": "мужской",
    "рост": 170,  # sm
    "вес": 75,    # kg
    "размер ноги": 43  # size
}

print(my_dict)"""
from typing import Dict, Union

"""5.2
my_dict = {
    "имя": "Николай",
    "возраст": 30,#yrs
    "пол": "мужской",
    "рост": 170,  # sm
    "вес": 75,    # kg
    "размер ноги": 43
}

for key, value in my_dict.items():
    print(f"{key}: {value}")"""

'''5.3
my_dict = {"имя": "Николай",
           "возраст": 30,
           "пол": "мужской",
           "рост": 170,
           "вес": 75,
           "размер ноги": 43
}
my_dict["размер ноги"] = 40
for key, value in my_dict.items():
    print(f"{key}: {value}")'''

5.4
my_dict = {"имя": "Николай",
           "возраст": 30,
           "пол": "мужской",
           "рост": 170,
           "вес": 75,
           "размер ноги": 43
}

del my_dict["возраст"]
for key, value in my_dict.items():
    print(f"{key}: {value}")






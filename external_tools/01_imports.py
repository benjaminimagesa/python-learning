import math 
import pandas as pd

result = math.sqrt(81)
print(result)

#import specific function
from math import pow, sqrt, pi
radius = 5
circumference = 2 * pi * radius
print(circumference)
circle_area = pi * pow(radius, 2)
print(circle_area)

data = {
    "name": ["Benjac", "Jacbae", "Mamito"],
    "age": [21, 20, 26],
    "city": ["Dar es Salaam", "Moshi", "Arusha"]
}
df = pd.DataFrame(data)
print(df)
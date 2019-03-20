import pandas as pd

input_file = './시뮬레이션_초단기예보조회.json'
df = pd.read_json(input_file)
print(df)
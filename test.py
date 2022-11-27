import requests
import pandas as pd
from sklearn.model_selection import train_test_split

url = 'http://127.0.0.1:1234/invocations'

headers = {'Content-type': 'application/json'}
data = pd.read_csv("win-quality.csv", sep=";")
train, test = train_test_split(data)
# test_x = test.drop(["quality"], axis=1)
test_x = pd.DataFrame(test).to_json(orient='split')
print(test_x)
resp = requests.post(
    url,
    headers=headers,
    data = test_x
    )

print(resp.content)
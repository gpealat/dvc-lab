import pandas as pd
import dvc.api

path = "data/wine_original.csv"
repo = "C:\\Users\\GuillaumePealat\\DSTI\\data_versioning"

data_url = dvc.api.get_url(
    path=path,
    repo=repo,
    rev="v4"
)

data = pd.read_csv(data_url, sep=";")

print(data)

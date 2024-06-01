
import pandas as pd
import requests
from sqlalchemy import create_engine


class Pipeline:
    def __init__(self, url):
        self.url = url
        self.data = None
        path = 'sqlite:///data//co2_data.sqlite'
        self.engine = create_engine(path, echo=False)

    def get_data(self):
        downloaded = requests.get(self.url)

        if downloaded.status_code == 200:
            with open('file.csv', 'wb') as file:
                file.write(downloaded.content)
            
            df = pd.read_csv("file.csv")
            self.data = df

        else:
            print(f"Download failed!")

    def transform(self):
        self.data = self.data[self.data["country"]=="Europe"]
        self.data = self.data[self.data["co2"].notna()][["year", "population", "co2", "co2_growth_prct"]]
        self.data.population = self.data.population.bfill()

    def save(self):
        self.data.to_sql("co2_data.csv", self.engine, index=False, if_exists='replace')

    def run_pipeline(self):
        self.get_data()
        self.transform()
        self.save()



if __name__ == '__main__':
    pipe = Pipeline("https://github.com/owid/co2-data/raw/master/owid-co2-data.csv")
    pipe.run_pipeline()

import pandas as pd
import requests
from sqlalchemy import create_engine


class Pipeline:
    def __init__(self):
        self.data = None
        self.engine = create_engine('sqlite:///../data/co2_data.db')

    def get_data(self):
        downloaded = requests.get("https://github.com/owid/co2-data/raw/master/owid-co2-data.csv")

        if downloaded.status_code == 200:
            with open('file.csv', 'wb') as file:
                file.write(downloaded.content)
            
            df = pd.read_csv("file.csv")
            self.data = df

        else:
            print(f"Download failed!")

    def get_data1(self):
        url = "https://opendata.dwd.de/climate_environment/CDC/observations_global/CLIMAT/monthly/qc/mean_sea_level_pressure/historical/01001_195101_202112.txt"
        df = pd.read_csv(url, sep=";")
        df = df.bfill()
        self.data2 = df
        self.data2.to_sql("year temperature", self.engine, index=False, if_exists='replace')
        

    def transform(self):
        self.data = self.data[self.data["country"]=="Europe"]
        self.data = self.data[self.data["co2"].notna()][["year", "population", "co2","temperature_change_from_co2", "co2_growth_prct"]]
        self.data.population = self.data.population.bfill()
        self.data.temperature_change_from_co2 = self.data.temperature_change_from_co2.bfill()

    def save(self):
        self.data.to_sql("co2_data", self.engine, index=False, if_exists='replace')

    def run_pipeline(self):
        self.get_data()
        self.get_data1()
        self.transform()
        self.save()



if __name__ == '__main__':
    pipe = Pipeline()
    pipe.run_pipeline()

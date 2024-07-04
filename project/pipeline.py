import pandas as pd
import requests
from sqlalchemy import create_engine

class Pipeline:
    def __init__(self):
        self.data = None
        self.engine = create_engine('sqlite:///../data/Output_data.db')

    def get_data(self):
        downloaded = requests.get("https://raw.githubusercontent.com/owid/co2-data/master/owid-co2-data.csv")

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
        self.data2.to_sql("Mean_Sea_Level", self.engine, index=False, if_exists='replace')

    def transform(self):
        european_countries = [
            "Albania", "Andorra", "Armenia", "Austria", "Azerbaijan", "Belarus", "Belgium", "Bosnia and Herzegovina",
            "Bulgaria", "Croatia", "Cyprus", "Czechia", "Denmark", "Estonia", "Finland", "France", "Georgia", "Germany",
            "Greece", "Hungary", "Iceland", "Ireland", "Italy", "Kazakhstan", "Kosovo", "Latvia", "Liechtenstein", "Lithuania",
            "Luxembourg", "Malta", "Moldova", "Monaco", "Montenegro", "Netherlands", "North Macedonia", "Norway", "Poland",
            "Portugal", "Romania", "Russia", "San Marino", "Serbia", "Slovakia", "Slovenia", "Spain", "Sweden", "Switzerland",
            "Turkey", "Ukraine", "United Kingdom", "Vatican City"
        ]
        self.data = self.data[self.data["country"].isin(european_countries)]
        self.data = self.data[self.data["co2"].notna()][["country", "year", "population", "co2", "temperature_change_from_co2", "co2_growth_prct"]]
        self.data.population = self.data.population.bfill()
        self.data.temperature_change_from_co2 = self.data.temperature_change_from_co2.bfill()

    def save(self):
        self.data.to_sql("CO2_data", self.engine, index=False, if_exists='replace')

    def run_pipeline(self):
        self.get_data()
        self.get_data1()
        self.transform()
        self.save()

if __name__ == '__main__':
    pipe = Pipeline()
    pipe.run_pipeline()

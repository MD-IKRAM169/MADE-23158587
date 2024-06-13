import unittest
import os
from sklearn.pipeline import Pipeline
from sqlalchemy import create_engine
import pandas as pd

class TestPipeline(unittest.TestCase):

    def setUp(self):
        self.pipeline = Pipeline()

    def test_get_data(self):
        self.pipeline.get_data()
        self.assertIsNotNone(self.pipeline.data)
        self.assertIn('co2', self.pipeline.data.columns)

    def test_get_data1(self):
        self.pipeline.get_data1()
        engine = create_engine('sqlite:///../data/Output_data.db')
        df = pd.read_sql('Mean_Sea_Level', engine)
        self.assertFalse(df.empty)

    def test_transform(self):
        self.pipeline.get_data()
        self.pipeline.transform()
        self.assertTrue('Europe' in self.pipeline.data['country'].values)
        self.assertFalse(self.pipeline.data['co2'].isnull().any())

    def test_save(self):
        self.pipeline.get_data()
        self.pipeline.transform()
        self.pipeline.save()
        engine = create_engine('sqlite:///../data/Output_data.db')
        df = pd.read_sql('CO2_data', engine)
        self.assertFalse(df.empty)

    def test_run_pipeline(self):
        self.pipeline.run_pipeline()
        engine = create_engine('sqlite:///../data/Output_data.db')
        co2_df = pd.read_sql('CO2_data', engine)
        sea_level_df = pd.read_sql('Mean_Sea_Level', engine)
        self.assertFalse(co2_df.empty)
        self.assertFalse(sea_level_df.empty)

if __name__ == '__main__':
    unittest.main()

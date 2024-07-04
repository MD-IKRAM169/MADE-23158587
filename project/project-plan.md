# Project Plan

## Title
<!-- Give your project a short title. -->
Analyzing the Correlation Between Carbon Dioxide Emissions and Mean Sea Level Pressure.

## Main Question

<!-- Think about one main question you want to answer based on the data. -->
1. What are the historical trends in carbon dioxide emissions in Europe from 1850 to 2022?

2. How has the mean sea level pressure changed globally over time?

3. How do CO2 emissions and the increasing temperature make an impact on sea level pressure?


## Description

<!-- Describe your data science project in max. 200 words. Consider writing about why and how you attempt it. -->
The main objective of this project is to study the connection between carbon dioxide emissions and Sea level mean pressure. We'll analyze two datasets: one that consists of CO2 emissions per country and another that encompasses global sea level mean pressure.

Carbon dioxide (CO2) emissions are a major contributor to global warming, and understanding their impact on atmospheric conditions is vital for predicting future climate patterns. Mean sea level pressure (MSLP) is a key indicator of atmospheric behavior and changes in weather systems. By investigating the relationship between CO2 emissions and MSLP, this study aims to provide insights into how human activities influence atmospheric dynamics, which is essential for developing effective climate mitigation 

The project will include data cleaning, combining the two datasets for country's, and looking for potential associations between emissions and Sea level metrics. We could also use visualization to show these connections and perhaps use statistical modeling to calculate the impact of emissions on sea level.

## Datasources

<!-- Describe each datasources you plan to use in a section. Use the prefic "DatasourceX" where X is the id of the datasource. -->

### Datasource1: Data on CO2 and Greenhouse Gas Emissions by Our World in Data
* Metadata URL:  https://github.com/owid/co2-data/blob/master/owid-co2-codebook.csv
* Data URL: https://raw.githubusercontent.com/owid/co2-data/master/owid-co2-data.csv
* Data Type: CSV

The data includes extensive reports of CO2 emissions for a number of countries over a period of time ranging from 1850 to 2022.The reason for selecting this dataset which is that, it provides extensive year-by-year data required for understanding historical trends of carbon emissions. Drawn from Our World in Data which is a highly regarded platform, it contains data on CO2 emissions from fossil fuels and cement production, and gas flaring which makes it a rich database for environmental and climate analysis. Nonetheless, some gaps may exist in the collection of data due to either errors in the process or because certain historical archives were not well documented. The data is used under the license Creative Commons Attribution 4.0 International (CC BY 4.0), which provides permission to use it wisely while citing the source, providing the metadata link and the source data link, and mentioning modifications if any.

## Datasources

<!-- Describe each datasources you plan to use in a section. Use the prefic "DatasourceX" where X is the id of the datasource. -->

### Datasource2: Worldwide Sea Level Pressure 
* Metadata URL: https://opendata.dwd.de/climate_environment/CDC/observations_global/CLIMAT/monthly/qc/mean_sea_level_pressure/historical/
* Data URL: https://opendata.dwd.de/climate_environment/CDC/observations_global/CLIMAT/monthly/qc/mean_sea_level_pressure/historical/01001_195101_202112.txt
* Data Type: TXT

The dataset is a time series of monthly mean sea level measurements spanning from 1951 to 2021. Each row represents a year, with columns for the sea level measurements for each month (January through December). The data is in a text format, which includes the year and the corresponding sea level values for each month. This dataset was chosen for its relevance in studying climate change, sea level rise, and their potential impacts on coastal regions. The dataset is also under the Creative Commons Attribution 4.0 International (CC BY 4.0) license like Data Source 1.

## Work Packages

<!-- List of work packages ordered sequentially, each pointing to an issue with more details. -->

[1. Extract the data from the two data sources](https://github.com/MD-IKRAM169/Project-Work-1_Md-Ikram-Tareq/issues/1)
2. Building pipeline.
3. Test data.
4. Analyze data.
5. Report on finding results.


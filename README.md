# Anlysis_accident_rate_Madrid
Is Madrid a safe place to drive?

| Requirements | Skills |
|--------------|--------|
| - `python3.10`<br> - `Pandas`<br> - `Numpy`<br> - `excel`<br> - `Jupyter`<br>  |  - `Data extracting`<br> - `Data cleaning and transformation`<br> - `Data wrangling`<br> - `API`<br> - `Data Anlysis` 

## Introduction

### Report objective
The objective of the analysis is try to identify if Madrid is a safe place to drive based on accident rate. 

I try to use the data to drive awareness and show, in numerical form, the severity of the actual situation.

### What is a drive accident
Making a bad decision behind the wheel is a decision that can affect to other people in the road. An accident
can be caused by a poor state of the road or human decisions.

In this report we analyze: General driving accidents, including those fatalities for poor road conditions and/or human decisions.

## General Analysis

### Trends by road type
1. Between 2018 and 2024, we observed a slight decrease in deaths per million inhabitants for Spain. Meanwhile, for Madrid, we observed a trend marked by a sharp decline in 2020.
2. Madrid’s figures are below the rest of Spain
3. From 2022 onward, there is a downward trend on Madrid’s roads. For Spain, figures remain stable within a range of 36 to 37.
<img src="https://github.com/rleonardg/Anlysis_accident_rate_Madrid/blob/main/assets/Spain_Madrid_General.png">
4. Interurban roads continue to prove to be much deadlier than urban roads, indicating that speed remains a key factor in fatal accidents.
<img src="https://github.com/rleonardg/Anlysis_accident_rate_Madrid/blob/main/assets/Spain_Madrid_Highways.png">
<img src="https://github.com/rleonardg/Anlysis_accident_rate_Madrid/blob/main/assets/Spain_Madrid_City_Roads.png">
5. Current values have returned to pre-pandemic levels after a slow recovery.

### Breakdown by Autonomous Communities and Municipalities - 2024
1. For 2024, the number of deaths per million inhabitants in Spain stands at 36.8.
2.  Madrid ranks first as the autonomous community with the fewest deaths per million inhabitants, with a rate of 17.83, ahead of País Vasco and comunitat Valenciana. Occupying the lowest positions are Castilla y León with a rate of 68.15, followed by Aragon and Murcia.
3. Why do communities like Madrid have fewer accidents per million inhabitants than others? Madrid has an area of 8,028 km², which implies a proportionally smaller and more concentrated road network. Therefore, it is easier to modernize using the regional budget.
<img src="https://github.com/rleonardg/Anlysis_accident_rate_Madrid/blob/main/assets/Desglose por CCAA.png">
<img src="https://github.com/rleonardg/Anlysis_accident_rate_Madrid/blob/main/assets/madrid-municipios.jpg">

## Top 3 most moortality rate by vehicle type - 2024
1. Pedestrians are the victims more deadly in a vehicle accidents, followed by bikes and other.
2. What have in common bikes and pedestrians? They are more vulnerable because they are more sentisitive to impacts.
<img src="https://github.com/rleonardg/Anlysis_accident_rate_Madrid/blob/main/assets/mortality_rate_by_vehicle_type.png">

## Resources
- [Ine](https://www.ine.es)
- [DGT](https://www.dgt.es/inicio/)

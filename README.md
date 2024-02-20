# Spreadsheet Analysis

## Data Set Details

### Original Data Set
The original data set was taken from the *[NYC Open Data](https://data.cityofnewyork.us/Environment/Air-Quality/c3uy-2p5r/about_data)*; it is a collection of air surveillance record collected from various sites of New York City. The file was originally downloaded as a CSV file.

### Raw Data

| Unique ID | Indicator ID | Name | Measure | Measure Info | Geo Type Name | Geo Join ID | Geo Place Name | Time Period | Start_Date | Data Value | Message |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
172653 | 375 | Nitrogen dioxide (NO2) | Mean | ppb | UHF34 | 203 | Bedford Stuyvesant - Crown Heights | Annual Average 2011 | 12/01/2010 | 25.3 | 
172585 | 375 | Nitrogen dioxide (NO2) | Mean | ppb | UHF34 | 203 | Bedford Stuyvesant - Crown Heights | Annual Average 2009 | 12/01/2008 | 26.93 | 
336637 | 375 | Nitrogen dioxide (NO2) | Mean | ppb | UHF34 | 204 | East New York | Annual Average 2015 | 01/01/2015 | 19.09 | 
336622 | 375 | Nitrogen dioxide (NO2) | Mean | ppb | UHF34 | 103 | Fordham - Bronx Pk | Annual Average 2015 | 01/01/2015 | 19.76 | 
172582 | 375 | Nitrogen dioxide (NO2) | Mean | ppb | UHF34 | 104 | Pelham - Throgs Neck | Annual Average 2009 | 12/01/2008 | 22.83 | 
667327 | 375 | Nitrogen dioxide (NO2) | Mean | ppb | UHF34 | 104 | Pelham - Throgs Neck | Annual Average 2020 | 01/01/2020 | 16.19 | 
172607 | 375 | Nitrogen dioxide (NO2) | Mean | ppb | UHF34 | 306308 | Chelsea-Village | Annual Average 2009 | 12/01/2008 | 38.16 | 
172675 | 375 | Nitrogen dioxide (NO2) | Mean | ppb | UHF34 | 306308 | Chelsea-Village | Annual Average 2011 | 12/01/2010 | 34.96 | 
175345 | 375 | Nitrogen dioxide (NO2) | Mean | ppb | UHF42 | 206 | Borough Park | Winter 2010-11 | 12/01/2010 | 30.1 | 
176689 | 375 | Nitrogen dioxide (NO2) | Mean | ppb | UHF42 | 206 | Borough Park | Annual Average 2013 | 12/01/2012 | 20.23 | 
176682 | 375 | Nitrogen dioxide (NO2) | Mean | ppb | UHF42 | 106 | High Bridge - Morrisania | Annual Average 2013 | 12/01/2012 | 23.73 | 
336507 | 375 | Nitrogen dioxide (NO2) | Mean | ppb | UHF42 | 106 | High Bridge - Morrisania | Winter 2014-15 | 12/01/2014 | 26 | 
740910 | 375 | Nitrogen dioxide (NO2) | Mean | ppb | UHF42 | 106 | High Bridge - Morrisania | Annual Average 2021 | 01/01/2021 | 18.04 | 
175348 | 375 | Nitrogen dioxide (NO2) | Mean | ppb | UHF42 | 209 | Bensonhurst - Bay Ridge | Winter 2010-11 | 12/01/2010 | 28.44 | 
175894 | 375 | Nitrogen dioxide (NO2) | Mean | ppb | UHF42 | 209 | Bensonhurst - Bay Ridge | Summer 2009 | 06/01/2009 | 18.95 | 
175895 | 375 | Nitrogen dioxide (NO2) | Mean | ppb | UHF42 | 210 | Coney Island - Sheepshead Bay | Summer 2009 | 06/01/2009 | 15.22 | 
175349 | 375 | Nitrogen dioxide (NO2) | Mean | ppb | UHF42 | 210 | Coney Island - Sheepshead Bay | Winter 2010-11 | 12/01/2010 | 25.7 | 
176693 | 375 | Nitrogen dioxide (NO2) | Mean | ppb | UHF42 | 210 | Coney Island - Sheepshead Bay | Annual Average 2013 | 12/01/2012 | 16.36 | 
741006 | 375 | Nitrogen dioxide (NO2) | Mean | ppb | UHF42 | 410 | Rockaways | Annual Average 2021 | 01/01/2021 | 11.41 | 

### Basic Scrubbing

First, I went over the data and saw that some columns were reduntant versions of one another. For example, _Indicator ID_ was a numerical value assigned to each unique _Name_ value. I dropped these redundant columns and left the most descriptive fields for clarity and concision. 

Then, I went over the Unique ID to check if there were any redundant rows I had to drop. The number of unique ID numbers and the number of rows matched, so I decided to drop the Unique ID column as the numbers in the field didn't provide description for the specific cases and therefore weren't relevant to analysis.

Finally, I dropped the _Message_ column as it held no data.

### Major Problems in Data

One major problem in the original data was that the table seemed to contain two different types of Air Quality Surveillance: concentrations on the air pollutant itself(such as Nitrogen Dioxide, Ozone, PM 2.5, etc.), and qualitative, categorical data describing specific situations regarding such pollutants(such as annual vehicle miles travelled, asthma emergency department visits due to PM2.5, etc.). I wanted to only look at the numerical data regarding the actual concentrations of air pollutants, so I dropped all rows containing categorical data.

### After a second look...

After I did all of the above and looking at the somewhat clean data, I found that I could drop one more column. The _Measure_ column turned out to be, for the remaining values that described the pollutant particles, the same value "Mean": therefore I dropped the entire column and edited the name of the _Data Value_ column to _Data Value(Mean)_.

I wanted to additionally drop _Measure Info_, but this turned out to be tricky as there were two units being used as measure units of the respective pollutants: for _Nitrogen Dioxide (NO2)_ and _Ozone (03)_, parts per billion(ppb), and for _Fine particles (PM 2.5)_, microgram per meter cubed(mcg/m3). I wanted to make the unit consistent, but after doing some research, I learned that the conversion factor between these two largely depended on the temperature of the atmosphere, as mcg/m3 is a unit based on the volume of air which is largely varied by the temperature(hence I assumed the season written in the _Time Period_ column). So I left this column and the units as is.

In total, these are the columns I dropped:
- Dropped _Unique ID_
- For Redundancy:
    - Pollution case description
        - Dropped _Indicator ID_
        - Kept _Name_
    - Location at which data was collected
        - Dropped _Geo Type Name_
        - Dropped _Geo Join ID_
        - Kept _Geo Place Name_
- Dropped _Message_
- Dropped _Measure_

## Analysis

### Aggregate Data
I calculated four different aggregate statistics(mean, median, mode, standard deviation) of the _Data Value_ column, which is not meaningful as the column without specific criteria is a mix of different pollutants using different units.

### Aggregate Data on Criteria
I calculated four different aggregate statistics(mean, median, mode, standard deviation) of the _Data Value_ column according to two criteria. I decided to look specifically at Nitrogen Dioxide levels in East New York. This set of statistics is more meaningful. According ot the data, the mean NO2 level of East New York is approximately 19.77ppb, the median being very close to this at 19.51ppb. The mode is 11.97ppb and the standard deviation of this data is 5.27, so it's quite spread out.

### Pivot Table

| Average of Data Value(Mean) | Fine Particles (PM2.5)(mcg/m3) | Nitrogen Dioxide (NO2)(ppb) | Ozone (O3)(ppb) |
| --- | --- | --- | --- |
| Bay Ridge and Dyker Heights (CD10) | 8.81 | 19.62 | 30.46
Bayside - Little Neck | 8.48 | 17.24 | 31.14
Bayside and Little Neck (CD11) | 8.46 | 17.60 | 31.22
Bayside Little Neck-Fresh Meadows | 8.51 | 17.98 | 31.08
Bedford Stuyvesant - Crown Heights | 9.15 | 21.73 | 30.01
Bedford Stuyvesant (CD3) | 9.24 | 22.29 | 29.53
Belmont and East Tremont (CD6) | 9.66 | 21.50 | 29.96
Bensonhurst - Bay Ridge | 8.60 | 18.87 | 31.38
Bensonhurst (CD11) | 8.55 | 19.24 | 31.82
Borough Park | 8.85 | 20.25 | 30.69
Borough Park (CD12) | 8.88 | 20.53 | 30.54
Bronx | 9.35 | 19.90 | 30.41
Brooklyn | 9.06 | 19.90 | 31.17
Brownsville (CD16) | 9.18 | 20.92 | 30.85
Bushwick (CD4) | 9.29 | 21.41 | 30.58
Canarsie - Flatlands | 8.50 | 16.75 | 33.29
Central Harlem - Morningside Heights | 9.68 | 23.97 | 28.22
Central Harlem (CD10) | 9.64 | 24.07 | 28.32
Chelsea - Clinton | 12.01 | 30.99 | 24.66
Chelsea-Village | 11.67 | 29.88 | 25.22
Clinton and Chelsea (CD4) | 11.24 | 28.75 | 25.94

I created a pivot table to look at each of the average amounts of pollutants organized by the region of the city as well; this table helps visualize and easily compare the different levels of each pollutant at specific locations.
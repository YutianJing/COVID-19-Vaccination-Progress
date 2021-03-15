# Covid-19 vaccination analysis:

##### a short report on Covid-19 vaccination data and its correlations with other factors



## Abstract

As most of the countries in the world had their respective vaccination schemes started in January, it is useful to have the up-to-date data on vaccination status and analyze with a few economic and social indicators of these countries to try to reveal the potential relationship, such that we may have a better understanding on the connections, causality, and maybe the trend of this matter. Using statistical tools including correlation, normalization and standardization, it is found that a country's vaccination status is strongly linked with its GDP and can be concluded that economic strength is a crucial factor affecting the vaccination plan of a country.

## Background

In this report, there will be 120 countries which has recorded vaccination data discussed with 4 indicators per country: GDP, GDP per capita, HDI and corruption index, based on the hypothesis that these labels all have basic positive correlation with total vaccination number and total vaccination number per hundred for a given country at the most recent recorded date.

## Data set

1. country_vaccinations.csv

   - source: https://www.kaggle.com/gpreda/covid-world-vaccination-progress

   - This dataset contains the following information:

     ```python
     Country - # this is the country for which the vaccination information is provided;
     Country ISO Code - # ISO code for the country;
     Date - # date for the data entry; for some of the dates we have only the daily vaccinations, for others, only the (cumulative) total;
     Total number of vaccinations - # this is the absolute number of total immunizations in the country;
     Total number of people vaccinated - # a person, depending on the immunization scheme, will receive one or more (typically 2) vaccines; at a certain moment, the number of vaccination might be larger than the number of people;
     Total number of people fully vaccinated - # this is the number of people that received the entire set of immunization according to the immunization scheme (typically 2); at a certain moment in time, there might be a certain number of people that received one vaccine and another number (smaller) of people that received all vaccines in the scheme;
     Daily vaccinations (raw) - # for a certain data entry, the number of vaccination for that date/country;
     Daily vaccinations - # for a certain data entry, the number of vaccination for that date/country;
     Total vaccinations per hundred - # ratio (in percent) between vaccination number and total population up to the date in the country;
     Total number of people vaccinated per hundred - # ratio (in percent) between population immunized and total population up to the date in the country;
     Total number of people fully vaccinated per hundred - # ratio (in percent) between population fully immunized and total population up to the date in the country;
     Daily vaccinations per million - # ratio (in ppm) between vaccination number and total population for the current date in the country;
     Vaccines used in the country - # total number of vaccines used in the country (up to date);
     Source name - # source of the information (national authority, international organization, local organization etc.);
     Source website - # website of the source of information;
     ```

   - In this dataset, we take only 2 columns for analysis: `Total number of vaccinations` and `Total vaccinations per hundred`. Since they are in an accumulative manner, only the most recent record (being the largest) is taken.

2. country_gdp.csv

   - source: https://data.worldbank.org/indicator/NY.GDP.MKTP.CD

   - This dataset contains the following information:

     ```python
     Country Name - # this is the country name;
     Country Code - # ISO code for the country;
     1960 - # GDP data in 1960
     ...
     2019 - # GDP data in 2019
     ```

   - In this dataset, we take only 2 columns for analysis: `Country Code` for later joins and `2019` since this is the most recent data.

3. country_gdppc.csv

   - source: https://data.worldbank.org/indicator/NY.GDP.PCAP.CD

   - This dataset contains the following information:

     ```python
     Country Name - # this is the country name;
     Country Code - # ISO code for the country;
     1960 - # GDP per capita data in 1960
     ...
     2019 - # GDP per capita data in 2019
     ```

   - In this dataset, we take only 2 columns for analysis: `Country Code` for later joins and `2019` since this is the most recent data.

4. Human Development Index (HDI).csv

   - source: http://hdr.undp.org/en/data

   - This dataset contains the following information:

     ```python
     HDI Rank - # HDI rank for the country;
     Country - # this is the country name;
     Country Code - # ISO code for the country;
     1990 - # HDI data in 1990
     ...
     2019 - # HDI data in 2019
     ```

   - In this dataset, there's no `Country Code` column for later joins, thus we only use `2019` since this is the most recent data.

5. human-development-index.csv

   - source: https://ourworldindata.org/human-development-index

   - This dataset contains the following information:

     ```python
     Entity - # this is the country name;
     Code - # ISO code for the country;
     Year - # from 1980 to 2017
     Human Development Index (UNDP) - # HDI data for the country at that year
     ```

   - In this dataset, there is ISO code column for joins but the data is only up to 2017, so we will only use the ISO code from this dataset and the 2019 data from `Human Development Index (HDI).csv`.

6. human-development-index-vs-corruption-perception-index.csv

   - source: https://ourworldindata.org/human-development-index

   - This dataset contains the following information:

     ```python
     Entity - # this is the country name;
     Code - # ISO code for the country;
     Year - # from 1800 to 2019
     Total population (Gapminder, HYDE & UN) - # population for the country
     Continent - # continent for the country
     Human Development Index (UNDP) - # HDI data for the country at that year
     Corruption Perception Index - Transparency International (2018) - # corruption index with 100 means very clean and 0 means very corrupt
     ```

   - In this dataset, we will be only using two columns: ISO code and corruption index.

## Methodology

There are many ways to show connection between two sets of data, and probably the most common approach is calculate the correlation coefficient. There will be three common method used to calculate correlation: Pearson, Kendall and Spearman. There are different conditions and data distribution characteristics that each fits better:

- Pearson's $r$:

  Used to measure the linear correlation between two variables that are normally distributed, it has a value between -1 and +1 where +1 means total positive linear correlation, 0 means no linear correlation and -1 means total negative linear correlation. The extreme values in the dataset have a big impact on Pearson's $r$, therefore it is needed to drop extremes (including NaN) and transformation on values (normalization and standardization).

- Kendall's $\tau$:

  This is used in the situation that two variables are both ordered and in intervals. Kendall's $\tau$ is non-parametric, not affected by extreme values and applies well to non-linear data. It uses less information (e.g. it does not use $\mu$ or $\sigma$ but rank) to determine the correlation between two variables. Value of 1 means a positive relationship, 0 means the two variables are independent and -1 means a negative relationship.

- Spearman's $\rho$:

  This is also a non-parametric method using rank, and has no requirement for the data to be normally distributed, not affected by extreme values and applies well to non-linear data. Spearman's $\rho$ is more sensitive to error and discrepancies than Kendall's $\tau$.

With the above correlations calculated, a p-value for each is also given. A p-value is the probability that an observed relationship could have occurred just by random chance, and in normal conditions a p-value lower than 0.05 indicates the statistical significance of the found relationship.

Lastly, to further validate the results, all the data will be normalized and standardized, then used again for the above procedures to find correlations. Using min-max normalization will transform data in numbers between 0 and 1, this is to make sure the data is compared under the same scale without bias on weights from large values. Using z-score standardization, the data will be transformed to have a mean of 0 and standard deviation of 1. Both of these linear transformations will not change the rank of data, and they are aimed to transform the original data into pure number without dimension, so that the error can be eliminated and we can then compare data with different dimensions or unit.

## Analysis

From the country vaccinations data, we can conclude that Pfizer/BioNTech, Moderna, Oxford/AstraZeneca, Sputnik V are the top 4 popular vaccine among 120 countries, over 40% of the countries have Pfizer/BioNTech as one of the vaccine type in their scheme. But based on absolute vaccination numbers, Chinese vaccine types (Sinopharm/Beijing, Sinopharm/Wuhan, Sinovac) ranked as second most injected vaccine, potentially because of its large population base. In general, US, China, UK and India are the top 4 country for total number of vaccinations, with US and China hitting 82.57M and 52.52M vaccinations, which are significantly greater than the rest of the countries.

In terms of correlations between indicators, it is found that total number of vaccinations is evidently have a strong positive linear correlation with country's GDP in 2019, shown by a Pearson's $r$ of 0.95. Even for Kendall's $\tau$ and Spearman's $\rho$, we can still observe a medium-high coefficient, this might be explained by that the more GDP a country had in 2019, the more economically developed the country is, thus it has lower possibility of issues on obtaining and distributing the vaccine. Securing, transporting, storing and distributing vaccines is a complicated pipeline and a serious challenge for any government under the pandemic situation, and it is predictable that a country with more economic growth has higher international stands and trade reputations, thus have privilege obtaining vaccines. For the same countries, they usually have mature government departments, good health care facilities and infrastructures which will undeniably give strength to the later processes in the vaccination distributing pipeline. From this result, we can predict that countries with higher total GDP will continue lead the total vaccine number rank in the future. However for total number of vaccinations per hundred, since this is effected by the correlation between a country's GDP and its population, there is a low positive correlation between a country's GDP.

For GDP per capita, HDI and corruption index, they have rather low (but positive) linear correlation with total number of vaccinations. From the observations on the correlation coefficient results, it is more likely that these 3 indicators have a medium-strong positive non-linear correlation with total number of vaccinations per hundred, since the number for Kendall's $\tau$ and Spearman's $\rho$ is a lot greater than Pearson's $r$. With a correlation number of 0.42, 0.41, 0.38 in Kendall's $\tau$ (even 30% higher in Spearman's $\rho$), we can say that after removed the population factor, a country's total number of vaccinations per hundred is positively linked with its GDP per capita, HDI and corruption index. That is, when a country is more economically developed, more socially developed and has a cleaner government, it will has a larger vaccination rate (per hundred).

## Result

In the last, we can firmly say that from the observed results, all 4 of our chosen indicator (GDP, GDP per capita, HDI and corruption index) have positive relationship with the vaccination status of a country. Even if some of them are not strong enough, we can still conclude that a country's vaccination status is largely affected and positively linked with its economical growth, human/social development and the government quality, accentuated by the total GDP which has the strongest relationship.
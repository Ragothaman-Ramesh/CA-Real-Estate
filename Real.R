install.packages("readxl")
install.packages("writexl")
library(readxl)
library(dplyr)
library(MASS)
library(ISLR)

setwd("~/Documents/Python")

county_dataset <- read_excel("real.xlsx")
names(county_dataset)
ncol(county_dataset)
numeric_dataset <- select_if(county_dataset, is.numeric)
names(numeric_dataset)
cor(numeric_dataset)
View(county_dataset)

summary(county_dataset$demand_score)
#checkdemandscore
lm.fit = lm(median_listing_price ~ supply_score+
              demand_score+nielsen_hh_rank+
              median_days_on_market, data = county_dataset)
summary(lm.fit)

plot.default(county_dataset)

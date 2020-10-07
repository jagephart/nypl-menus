library(tidyverse)

# Read in the data 
df <- read.csv("data/dfnew_labeled.csv")

# Filter to seafood dishes
df <- df %>%
  filter(seafood_yn == 1)

# Write function to sample years for a given dish
# As currently written, this funtion will only work properly if times_appeared > 2
# Add conditions such that if times_appeared == 1, only one row/year appears (either the first appearance
# or the last appearance since they should be the same) and 
# if times_appeared == 2, there is one row for the first appearance year and one for the last appearance year
# I did notice some weird instances where there were zero appearances or other inconsistencies, so these
# will need to be filtered out.

sample_years <- function(dat, dish_col = "name", times_col = "times_appeared", 
                         first_col = "first_appeared", last_col = "last_appeared"){
  n <- dat[[times_col]]
  out.df <- data.frame("name" = rep(dat[[dish_col]], n), "year" = NA)
  out.df$year[1] <- dat[[first_col]]
  out.df$year[2] <- dat[[last_col]]
  
  out.df$year[3:n] <- sample(dat[[first_col]]:dat[[last_col]], (n-2))
  
  return(out.df)
}

# This function then needs to be applied for every seafood dish to create one long df with all of the
# sampled time series data. Ultimately, we will want to resample many times to create multiple time series
# and average over them. 

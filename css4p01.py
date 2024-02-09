#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 14:18:03 2024

@author: patrickkalonde
"""

import pandas as pd

df = pd.read_csv("movie_dataset.csv")

# Question 1: Hisgested rated movies

highest_rating_index = df['Rating'].idxmax()
highest_rated_movie = df.loc[highest_rating_index]
print(highest_rated_movie)



# Question 3: Average revenue for  movies between 2015 and 2017

filtered_df = df[(df['Year'] >= 2015) & (df['Year'] <= 2017)]
average_revenue = filtered_df['Revenue (Millions)'].dropna().mean()
print(average_revenue)

# Question 4: Movies released in 2016

num_movies_2016 = df[df['Year'] == 2016].shape[0]
print("Number of movies released in 2016:", num_movies_2016)

#Question 5: Movies directed by Christopher Noran

num_movies_2016 = df[df['Director'] == 'Christopher Nolan'].shape[0]
print("Number of movies  directed by CHris:", num_movies_2016)

# Question 6: Movie with rating of atleast 8.0

num_highly_rated_movies = df[df['Rating'] >= 8.0].shape[0]
print("Number of movies with a rating of at least 8.0:", num_highly_rated_movies)

# Question 7: Median rating of Nolan's movies

nolan_movies = df[df['Director'] == 'Christopher Nolan']
median_rating_nolan_movies = nolan_movies['Rating'].median()
print("Median rating of movies directed by Christopher Nolan:", median_rating_nolan_movies)

# Question 8 - Year with the highest average rating

average_rating_by_year = df.groupby('Year')['Rating'].mean()
year_highest_average_rating = average_rating_by_year.idxmax()
print("Year with the highest average rating:", year_highest_average_rating)

# # Question 9: percentage increase

movies_2006_2016 = df[(df['Year'] >= 2006) & (df['Year'] <= 2016)]
num_movies_2006 = movies_2006_2016[movies_2006_2016['Year'] == 2006].shape[0]
num_movies_2016 = movies_2006_2016[movies_2006_2016['Year'] == 2016].shape[0]
percentage_increase = ((num_movies_2016 - num_movies_2006) / num_movies_2006) * 100
print("Percentage increase in number of movies made between 2006 and 2016:", percentage_increase)

# Question 10: Most common actor

from collections import Counter
all_actors = ','.join(df['Actors']).split(', ')
actor_counts = Counter(all_actors)
most_common_actor = actor_counts.most_common(1)[0]
print (actor_counts)

# Question 11 - Count the number of unique genres

all_genres = df['Genre'].str.split(', ')
unique_genres = set()
for genres_list in all_genres:
    unique_genres.update(genres_list)
num_unique_genres = len(unique_genres)
print("Number of unique genres in the dataset:", num_unique_genres)

# Question 12 - Correlation

correlation_duration_revenue = df['Runtime (Minutes)'].corr(df['Revenue (Millions)'])
correlation_revenue_rating = df['Revenue (Millions)'].corr(df['Rating'])
correlation_rating_duration = df['Runtime (Minutes)'].corr(df['Rating'])
correlation_rating_votes = df['Rating'].corr(df['Votes'])
correlation_year_revenue = df['Year'].corr(df['Revenue (Millions)'])

print("Correlation between Duration and Revenue:", correlation_duration_revenue)
print("Correlation between Revenue and Rating:", correlation_revenue_rating)
print("Correlation between Duration and Rating:", correlation_rating_duration)
print("Correlation between Rating and Votes:", correlation_rating_votes)
print("Correlation between Year and Revenue:", correlation_year_revenue)
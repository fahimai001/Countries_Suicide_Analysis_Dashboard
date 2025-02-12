import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt

df = pd.read_csv('suicide.csv')

df.head()

# Is the suicide rate more prominent in some age categories than others?

age_suicide_rates = df.groupby('age')['suicides/100k pop'].sum().reset_index()

fig_age_suicide = px.bar(
    age_suicide_rates, 
    x='age', 
    y='suicides/100k pop', 
    title='Suicide Rate in Different Age Categories',
    labels={'suicides/100k pop': 'Suicide Rate', 'age': 'Age Group'},
    color='age',
    text='suicides/100k pop' 
)
fig_age_suicide.update_traces(textposition='outside') 
fig_age_suicide.update_layout(
    plot_bgcolor='black', 
    paper_bgcolor='black',
    font=dict(color='white'),
    xaxis=dict(title='Age Group', tickfont=dict(color='white')),
    yaxis=dict(title='Suicide Rate per 100k Population', tickfont=dict(color='white')),
    height=600, 
    width=800
)

# Which countries have the most and the least number of suicides?

country_suicide_rates = df.groupby('country')['suicides_no'].sum().sort_values(ascending=False).head(10).reset_index()

fig_country_suicide = px.bar(
    country_suicide_rates, 
    x='country', 
    y='suicides_no', 
    title='Most Suicides in Countries',
    labels={'suicides_no': 'Total Suicides', 'country': 'Country'},
    color='country',
    text='suicides_no'
)

fig_country_suicide.update_traces(textposition='outside')
fig_country_suicide.update_layout(
    plot_bgcolor='black',
    paper_bgcolor='black',
    font=dict(color='white'),
    xaxis=dict(title='Country', tickfont=dict(color='white')),
    yaxis=dict(title='Total Suicides', tickfont=dict(color='white')),
    height=600, 
    width=800
)

# What is the effect of the population on suicide rates?

fig_population_suicide = px.scatter(
    df, 
    x='population', 
    y='suicides/100k pop', 
    title='Effect of Population on Suicide Rates',
    labels={'population': 'Population', 'suicides/100k pop': 'Suicide Rate per 100k'},
    color_discrete_sequence=['cyan']
)

fig_regression = px.scatter(
    df, 
    x='population', 
    y='suicides/100k pop', 
    trendline='ols',
    color_discrete_sequence=['red'] 
)

fig_population_suicide.add_trace(fig_regression.data[1])  

fig_population_suicide.update_layout(
    plot_bgcolor='black',   
    paper_bgcolor='black',  
    font=dict(color='white'),  
    xaxis=dict(title='Population', tickfont=dict(color='white')),
    yaxis=dict(title='Suicide Rate per 100,000', tickfont=dict(color='white')),
    height=600, 
    width=800
)

# What is the effect of the GDP of a country on suicide rates?

fig_gdp_suicide = px.scatter(
    df, 
    x=' gdp_for_year ($) ', 
    y='suicides/100k pop', 
    title='GDP per Year vs. Suicide Rate',
    labels={' gdp_for_year ($) ': 'GDP per Year', 'suicides/100k pop': 'Suicide Rate per 100k'},
    color_discrete_sequence=['lime']
)

fig_gdp_suicide.update_layout(
    plot_bgcolor='black',   
    paper_bgcolor='black',  
    font=dict(color='white'),  
    xaxis=dict(title='GDP per Year', tickfont=dict(color='white')),
    yaxis=dict(title='Suicide Rate per 100,000', tickfont=dict(color='white')),
    height=600, 
    width=800
)

# What is the trend of suicide rates across all the years?

suicide_trend = df.groupby('year')['suicides/100k pop'].mean().reset_index()

fig_suicide_trend = px.line(
    suicide_trend, 
    x='year', 
    y='suicides/100k pop', 
    title='Trend of Suicide Rates Across Years',
    labels={'year': 'Year', 'suicides/100k pop': 'Average Suicide Rate'},
    markers=True
)

fig_suicide_trend.update_traces(line=dict(color='cyan', width=2))

fig_suicide_trend.update_layout(
    plot_bgcolor='black',
    paper_bgcolor='black',
    font=dict(color='white'),
    xaxis=dict(title='Year', tickfont=dict(color='white')),
    yaxis=dict(title='Average Suicide Rate', tickfont=dict(color='white')),
    height=600,
    width=800
)

#  Is there a difference between the suicide rates of men and women?

fig_sex_suicide = px.bar(
    df.groupby('sex')['suicides/100k pop'].sum().reset_index(), 
    x='sex', 
    y='suicides/100k pop', 
    title='Comparison Between Male and Female Suicide Rate',
    labels={'sex': 'Sex', 'suicides/100k pop': 'Suicide Rate'},
    color='sex',
    color_discrete_sequence=['blue', 'pink']
)

fig_sex_suicide.update_traces(text=df.groupby('sex')['suicides/100k pop'].sum(), textposition='outside')

fig_sex_suicide.update_layout(
    plot_bgcolor='black',
    paper_bgcolor='black',
    font=dict(color='white'),
    xaxis=dict(title='Sex', tickfont=dict(color='white')),
    yaxis=dict(title='Suicide Rate', tickfont=dict(color='white')),
    height=600,
    width=800
)


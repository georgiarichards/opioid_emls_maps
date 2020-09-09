# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.6.0
#   kernelspec:
#     display_name: Python 2
#     language: python
#     name: python2
# ---

# # Global, regional & national consumption of opioids, 2015-2017
#

# Our study aims to measure variation in opioid consumption across the globe. 
#
# **Methods:**<br>
# We obtained the most up-to-date data from the <a href="https://www.incb.org/" target="_blank">International Narcotics Control Board (INCB)</a> as of Auguat 2019 (2015-17), reported in kilograms (kg). We extracted total opioid consumption for each country, state and territory (n=214) for each year. We calculated the 3-year annual mean consumption for each country and created a rate (kg per 100,000 of the population), using 2016 population data from the <a href="https://apps.who.int/gho/data/node.main.SDGPOP?lang=en" target="_blank">WHO Global Health Observatory</a>. We visualised the data and use quantiles to create the colour spectrum for the choropleth maps displayed in this Notebook.

# import libraries for handling data, analysis, and visualising/graphing the data
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# import data 
df=pd.read_csv(filepath_or_buffer="map_opioidconsum.csv")
df.head()

# to see what data is in the dataset (column names)
df.info()

# summary stats for each column 
df.describe()

# +
# visualise data 
fig1 = px.bar(df, x='Country', y='meanop_pop',
             hover_data=['Country', 'meanop_pop'],
             color='Region2',
             labels={'meanop_pop':'Annual mean consumption of opioids<br>(kg per 100,000 population)',
                    'Country': ""}
             )

fig1.update_layout(xaxis=dict(categoryorder='total descending'), 
                   xaxis_tickangle=-45,
                   font=dict(size=10),
                   yaxis=dict(showgrid=False))
fig1.show()

#improve figure by: 1) removing grid lines, 2) updating the label of the legend & 
# 3) get the descending ordering to work... 
# -

# # Maps

#converted deciles into a string so it sees it as discrete categorical data and not floats
df['decile_op_pop'] = df['decile_op_pop'].astype(str) 

df.dropna(inplace=True)

df.sort_values(by="decile_op_pop", inplace=True)
#this sorts the legend values by playing with the strings

df.head()

fig = px.choropleth(df, color="decile_op_pop",
                    locations="country_ISO",
                    hover_data=["meanop_pop"]
                   )
fig.show()

# +
data2 = [go.Choropleth(
    z = df['decile_op_pop'],
    locations = df['country_ISO'],
    text = df['Country'],
    hoverinfo = "text",
    marker_line_color='darkgray',
    marker_line_width=0.5,
    autocolorscale = False, 
    reversescale=True,
    colorscale = [[0.0, "rgb(165,0,38)"],
                [0.1111111111111111, "rgb(215,48,39)"],
                [0.2222222222222222, "rgb(244,109,67)"],
                [0.3333333333333333, "rgb(253,174,97)"],
                [0.4444444444444444, "rgb(254,224,144)"],
                [0.5555555555555556, "rgb(224,243,248)"],
                [0.6666666666666666, "rgb(171,217,233)"],
                [0.7777777777777778, "rgb(116,173,209)"],
                [0.8888888888888888, "rgb(69,117,180)"],
                [1.0, "rgb(49,54,149)"]],
    colorbar = dict(
        title="kg per 100,000<br> ",
        tickvals=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        ticktext=["0", ".0002-.003", ".004-.05", ".05-0.15", ".16-.328", ".332-.51", ".55-1.02", "1.03-1.76", "1.8-5.6", "6.2-48"],
        ticks="outside",
        thickness=20,),
)]

layout2 = go.Layout(
    geo = go.layout.Geo(
        showframe=False,
        showcoastlines=False,
        projection_type='equirectangular'),
    )

fig2 = go.Figure(data = data2, layout = layout2)

fig2.show()

# +
# same map as above but with different color 
data2 = [go.Choropleth(
    z = df['decile_op_pop'],
    locations = df['country_ISO'],
    text = df['Country'],
    hoverinfo = "text",
    marker_line_color='darkgray',
    marker_line_width=0.5,
    autocolorscale = False, 
    reversescale=False,
    colorscale = 'Reds',
    colorbar = dict(
        title="kg per 100,000<br> ",
        tickvals=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        ticktext=["0", ".0002-.003", ".004-.05", ".05-0.15", ".16-.328", ".332-.51", ".55-1.02", "1.03-1.76", "1.8-5.6", "6.2-48"],
        ticks="outside",
        thickness=20),
)]

layout2 = go.Layout(
    geo = go.layout.Geo(
        showframe=False,
        showcoastlines=False,
        projection_type='equirectangular'),
    )

fig2 = go.Figure(data = data2, layout = layout2)

fig2.show()
# -



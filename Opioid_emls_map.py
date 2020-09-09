# -*- coding: utf-8 -*-
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

# # Opioids listed on national essential medicines lists (EMLs)
#

# Our study aims to determine the value and utility of national essential medicines lists (EMLs) in promoting global access to opioids. Our objectives are: 
# 1. to compare opioids listed in the 2017 WHO Model EML with the opioids listed in the 137 national EMLs,
# 2. to assess the association between national opioid consumption and listings in EMLs, and
#
# **Methods:**<br>
# We extracted data from the <a href="https://figshare.com/articles/GlobalEssentialMedicinesDatabase_xlsx/7814246/1" target="_blank">Global Essential Medicines (GEM) database</a>; previously published in the <a href="https://www.who.int/bulletin/volumes/97/6/18-222448/en/" target="_blank">Bulletin of the World Health Organization here</a> and available as an <a href="https://global.essentialmeds.org/dashboard/countries" target="_blank">online tool here</a>. Two authors (GCR, JKA) independently searched the <a href="https://www.whocc.no/atc_ddd_index/" target="_blank">WHO’s ATC index</a> using ‘opioid’ and ‘opium’ keywords to extract chemical substance codes for opioids. Lists of opioid codes were compared, and discrepancies were discussed and agreed to form a master list of opioid codes. We used this master list of opioid codes to search for opioids in the database of EMLs. We extract all identified opioids from the database into a csv file. We calculated the total number of opioids and type of opioids listed by each of the 137 countries with an EML and made comparision to the WHO Model List of Essential Medicines. 
#
# This Notebook graphs the number of opioids listed by countries.

# import libraries for handling data, analysis, and visualising/graphing the data
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# import data 
df=pd.read_csv(filepath_or_buffer="EMLopioid_maps.csv")
df.head()

# to see what data is in the dataset (column names)
df.info()

# summary stats for each column 
df.describe()

# +
# visualise data
fig1 = px.bar(df, x='Country', y='OpioidEML',
              hover_data=['Country', 'OpioidEML'],
              color='Region2',
              labels={'OpioidEML':'Number of opioids listed in<br>national essential medicines lists',
                      'Country' : ""}
              )

fig1.update_layout(xaxis=dict(categoryorder='total descending'), 
                   xaxis_tickangle=-45,
                   font=dict(size=10),
                   yaxis=dict(showgrid=False))

fig1.show()

#improve figure by: 1) removing grid lines & 2) updating the label of the legend 
# -

# # Maps

df['quantiles'] = df['Quant9_OpioidEML'].apply(str) + "d"

df["Quant9_OpioidEML"] = df["Quant9_OpioidEML"].astype(str)

df.sort_values(by="Quant9_OpioidEML", inplace=True)

df.head()

fig2 = px.choropleth(df,
                    locations="country_ISO",
                    color="Quant9_OpioidEML",
                    hover_name="Country")
fig2.show()

# +
data2 = [go.Choropleth(
    z = df['Quant9_OpioidEML'],
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
        title="No. of opioids in EMLs<br> ",
        tickvals=[1, 2, 3, 4, 5, 6, 7, 8, 9],
        ticktext=["0-3", "4", "5", "6", "7", "8", "9", "10-11", "12-19"],
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
data2 = [go.Choropleth(
    z = df['Quant9_OpioidEML'],
    locations = df['country_ISO'],
    hovertext = df['Country'],
    colorscale ='Viridis',
    marker_line_color = 'darkgray',
    marker_line_width = 0.5,
    autocolorscale = False, 
    reversescale=False,
    colorbar=dict(
        title="No. of opioids on EML",
        tickvals=[1, 2, 3, 4, 5, 6, 7, 8, 9],
        ticktext=["0-3", "4", "5", "6", "7", "8", "9", "10-11", "12-19"],
        ticks="outside"),
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
layout2 = go.Layout(
    geo = go.layout.Geo(
        showframe=False,
        showcoastlines=False,
        projection_type='equirectangular'),
    )

fig2 = go.Figure(data = data2, layout = layout2)

z = 'Quant9_OpioidEML',
locations = 'country_ISO',
colour = "OpioidEML",
marker_line_color = 'darkgray',
marker_line_width = 0.5,
autocolorscale = False, 
reversescale=False,
colorbar=dict(
    title="No. of opioids on EML",
    tickvals=[1, 2, 3, 4, 5, 6, 7, 8, 9],
    ticktext=["0-3", "4", "5", "6", "7", "8", "9", "10-11", "12-19"],
    ticks="outside"),

layout2 = go.Layout(
    geo = go.layout.Geo(
        showframe=False,
        showcoastlines=False,
        projection_type='equirectangular'),
    )

fig2 = go.Figure(data = data2, layout = layout2)
fig2.show()

# +
data2 = [go.Choropleth(
    z = df['Quant9_OpioidEML'],
    locations = df['country_ISO'],
    hovertext = df['Country'],
    colorscale ='Reds',
    marker_line_color = 'darkgray',
    marker_line_width = 0.5,
    autocolorscale = False, 
    reversescale=False,
    colorbar=dict(
        title="No. of opioids on EML",
        tickvals=[1, 2, 3, 4, 5, 6, 7, 8, 9],
        ticktext=["0-3", "4", "5", "6", "7", "8", "9", "10-11", "12-19"],
        ticks="outside"),
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
data2 = [go.Choropleth(
    z = df['Quant9_OpioidEML'],
    locations = df['country_ISO'],
    text = df['Country'],
    hoverinfo = "text",
    marker_line_color='darkgray',
    marker_line_width=0.5,
    autocolorscale = False, 
    reversescale=False,
    colorscale = 'Reds',
    colorbar = dict(
        title="No. of opioids in EMLs<br> ",
        tickvals=[1, 2, 3, 4, 5, 6, 7, 8, 9],
        ticktext=["0-3", "4", "5", "6", "7", "8", "9", "10-11", "12-19"],
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
# -



# Import libraries
import numpy as np 
import pandas as pd 
import plotly as py
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

# Read Data
df = pd.read_csv('covid_19_data.csv')

# Rename columns
df.rename(columns={'Country/Region':'Country'}, inplace = True)
df.rename(columns={'ObservationDate':'Date'}, inplace= True)


# Manipulate Dataframe
df_countries = df.groupby(['Country', 'Date']).sum().reset_index().sort_values('Date', ascending=False)
df_countries = df_countries.drop_duplicates(subset = ['Country'])
df_countries = df_countries[df_countries['Confirmed']>0]
df.head()

# Create the Choropleth
fig = go.Figure(data=go.Choropleth(
    locations = df['Country'],
    locationmode = 'country names',
    z = df['Confirmed'],
    colorscale = 'Reds',
    autocolorscale=False,
    reversescale=True,
    marker_line_color = 'black',
    marker_line_width = 0.5,
    )
)
fig.update_layout(
    title_text = 'Confirmed Cases as of March 28, 2020',
    geo=dict(
        showframe = False,
        showcoastlines = False,
        projection_type = 'equirectangular'
    )
)

# Manipulating the original dataframe
df_countrydate = df[df['Confirmed']>0]
df_countrydate = df_countrydate.groupby(['Date','Country']).sum().reset_index()
df_countrydate = df_countrydate.drop_duplicates(subset = ['Country'])
# Creating the visualization
fig = px.choropleth(df_countrydate, 
                    locations="Country", 
                    locationmode = "country names",
                    color="Confirmed", 
                    hover_name="Country", 
                    animation_frame="Date"
                   )
fig.update_layout(
    title_text = 'Global Spread of Coronavirus',
    title_x = 0.5,
    geo=dict(
        showframe = False,
        showcoastlines = False,
    ))

fig.show()
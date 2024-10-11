import pandas as pd
import plotly.express as px

# Load the data from the CSV file
data = pd.read_csv('world_population.csv')

# Display the entire dataframe to see data of all countries
print(data)

# Create a bubble chart
fig = px.scatter(
    data, 
    x='2022 Population', 
    y='Area (km²)', 
    size=data['Density (per km²)'] * 10,  # Scale density
    color='Country', 
    hover_name='Country', 
    size_max=200,  # size of bubbles
    title='Bubble Chart of Countries by Population and Area',
    color_continuous_scale=px.colors.sequential.Viridis  # colour scale
)

# updated layout 
fig.update_layout(
    xaxis_title='Population in 2022',
    yaxis_title='Area in km²',
    legend_title='Country',
    template='plotly_white',  # white background
    font=dict(
        family="Arial, sans-serif",
        size=12,
        color="RebeccaPurple"
    )
)

# display plot
fig.show()

import pandas as pd
import plotly.express as px

# Load the data from the CSV file
data = pd.read_csv('world_population.csv')

# Display the entire dataframe to see data of all countries
print(data)

# Create a bubble chart with color by country
fig = px.scatter(
    data, 
    x='2022 Population', 
    y='Area (km²)', 
    size=data['Density (per km²)'] * 10,  # Scale the density values
    color='Country', 
    hover_name='Country', 
    size_max=200,  # Further increase the maximum size of the bubbles
    title='Bubble Chart of Countries by Population and Area',
    color_continuous_scale=px.colors.sequential.Viridis  # Use a pleasing color scale
)

# Update layout for better visibility
fig.update_layout(
    xaxis_title='Population in 2022',
    yaxis_title='Area in km²',
    legend_title='Country',
    template='plotly_white',  # Use a clean white template
    font=dict(
        family="Arial, sans-serif",
        size=12,
        color="RebeccaPurple"
    )
)

# Show the plot
fig.show()
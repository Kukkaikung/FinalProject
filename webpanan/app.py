# Import packages
from dash import Dash, html, dash_table
import pandas as pd

# Incorporate data
df = pd.read_csv('data_mange/clean02_air4thai_44t_2023-01-01_2024-02-27.csv')
df1 = pd.read_csv('predict_data/predictions_PM25.csv')
df2 = pd.read_csv('predict_data/predictions_TEMP.csv')

# Initialize the app
app = Dash(__name__)

# Define styles
table_style = {
    'margin-bottom': '20px',
    'font-family': 'Arial, sans-serif',
    'border-collapse': 'collapse',
    'width': '80%',  # Adjust the width of the tables
    'border': '1px solid #ddd',
    'text-align': 'left',
    'margin-left': 'auto',  # Center the table
    'margin-right': 'auto',  # Center the table
}

header_style = {
    'background-color': '#f2f2f2',
    'color': '#333',
    'padding': '8px',
}

cell_style = {
    'padding': '8px',
}

# App layout
app.layout = html.Div([
    html.H1(children='Air Quality Predictions', style={'text-align': 'center', 'color': 'blue'}),  # Change the title
    dash_table.DataTable(
        data=df.to_dict('records'),
        page_size=10,
        style_table=table_style,
        style_header=header_style,
        style_cell=cell_style,
    ),
    
    dash_table.DataTable(
        data=df1.to_dict('records'),
        page_size=10,
        style_table=table_style,
        style_header=header_style,
        style_cell=cell_style,
    ),
    
    dash_table.DataTable(
        data=df2.to_dict('records'),
        page_size=10,
        style_table=table_style,
        style_header=header_style,
        style_cell=cell_style,
    )
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)

# Import packages
from dash import Dash, html, dash_table
import pandas as pd

# Incorporate data
df = pd.read_csv('predict_data/predictions_PM25.csv')
df1 = pd.read_csv('predict_data/predictions_TEMP.csv')
df2 = pd.read_csv('data_mange/clean02_air4thai_44t_2023-01-01_2024-02-27.csv')

# Initialize the app
app = Dash(__name__)

# Custom styles
styles = {
    'header': {
        'backgroundColor': '#007bff',
        'color': 'white',
        'padding': '10px 0',
        'textAlign': 'center',
        'marginBottom': '20px'
    },
    'table': {
        'margin': '0 auto',
        'width': '80%',
        'textAlign': 'center',
        'border': '1px solid #007bff',  # Add border
        'borderCollapse': 'collapse',   # Collapse border spacing
    },
    'evenRow': {'backgroundColor': '#f2f2f2'},  # Alternate row color
    'oddRow': {'backgroundColor': '#ffffff'},   # Alternate row color
}

# App layout
app.layout = html.Div([
    html.Div(children='PM2.5', style=styles['header']),
    dash_table.DataTable(
        data=df.to_dict('records'),
        page_size=10,
        style_table=styles['table'],
        style_data_conditional=[
            {'if': {'row_index': 'even'}, 'backgroundColor': styles['evenRow']['backgroundColor']},
            {'if': {'row_index': 'odd'}, 'backgroundColor': styles['oddRow']['backgroundColor']}
        ]
    ),
    html.Div(children='Temperature', style=styles['header']),  # Header for second table
    dash_table.DataTable(
        data=df1.to_dict('records'),
        page_size=10,
        style_table=styles['table'],
        style_data_conditional=[
            {'if': {'row_index': 'even'}, 'backgroundColor': styles['evenRow']['backgroundColor']},
            {'if': {'row_index': 'odd'}, 'backgroundColor': styles['oddRow']['backgroundColor']}
        ]
    ),
    html.Div(children='Air Quality', style=styles['header']),  # Header for third table
    dash_table.DataTable(
        data=df2.to_dict('records'),
        page_size=10,
        style_table=styles['table'],
        style_data_conditional=[
            {'if': {'row_index': 'even'}, 'backgroundColor': styles['evenRow']['backgroundColor']},
            {'if': {'row_index': 'odd'}, 'backgroundColor': styles['oddRow']['backgroundColor']}
        ]
    )
])

# Run the app
if __name__ == '__main__':
    app.run(debug=True)

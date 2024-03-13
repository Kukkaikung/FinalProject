# Import packages
from dash import Dash, html, dash_table, dcc, callback_context
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

# Incorporate data
df = pd.read_csv('data_mange/clean03_air4thai_44t_2023-01-01_2024-02-27.csv')
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
    'max-width': '800px',  # Limit the maximum width of the tables
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

# Filter out unwanted columns
valid_columns = [col for col in df.columns if col not in ['Unnamed: 0.1', 'Unnamed: 0', 'DATETIMEDATA', 'stationID']]

# Function to create graph based on selected data
def create_graph(selected_data, filtered_df):
    fig = px.line(filtered_df, x='DATETIMEDATA', y=selected_data, title=f'{selected_data} Over Time')
    return fig

def create_histogram(selected_data, filtered_df):
    fig = px.histogram(filtered_df, x=selected_data, title=f'{selected_data} Histogram')
    return fig

# Function to create scatter plot
def create_scatter(selected_data, filtered_df):
    fig = px.scatter(filtered_df, x='DATETIMEDATA', y=selected_data, title=f'{selected_data} Scatter Plot')
    return fig

def create_predictions_graph(selected_data, filtered_df, title):
    fig = px.line(filtered_df, x='DATETIMEDATA', y='prediction_label', title=title)
    return fig

def histogram_predictions_graph(selected_data, filtered_df, title):
    fig = px.histogram(filtered_df, x='DATETIMEDATA', y='prediction_label', title=title)
    return fig

def scatter_predictions_graph(selected_data, filtered_df, title):
    fig = px.scatter(filtered_df, x='DATETIMEDATA', y='prediction_label', title=title)
    return fig

# App layout with tables, graphs, and Date Picker Range
app.layout = html.Div([
    html.H1(children='Air Quality Predictions', style={'text-align': 'center', 'color': 'blue', 'background-color': '#f2f2f2', 'padding': '10px'}),  # Change the title and add background color

    # Table for df
    dash_table.DataTable(
        id='table-df',
        data=df.to_dict('records'),
        page_size=10,
        style_table=table_style,
        style_header=header_style,
        style_cell=cell_style,
    ),
    html.Div([
        dcc.Dropdown(
            id='dropdown-graph',
            options=[{'label': column, 'value': column} for column in valid_columns],
            value='PM25',  # Default value
            style={'width': '50%', 'margin-right': '20px', 'margin-bottom': '20px'}  # Adjust width and add margin
        ),
        dcc.DatePickerRange(
            id='date-picker-range',
            start_date='2024-01-01',
            end_date='2024-02-27',
            display_format='YYYY-MM-DD',
            style={'width': '50%'}  # Adjust width
        )
    ], style={'display': 'flex', 'justify-content': 'center', 'margin-bottom': '20px'}),

    # Graphs based on selected data
    html.Div([
        dcc.Graph(id='line-graph'),
        dcc.Graph(id='histogram')
    ], style={'display': 'flex', 'flex-wrap': 'wrap', 'justify-content': 'center', 'margin-bottom': '20px'}),

    html.Div([
        dcc.Graph(id='scatter-plot')
    ], style={'display': 'flex', 'flex-wrap': 'wrap', 'justify-content': 'center', 'margin-bottom': '20px'}),

    # Table for df1
    html.Div([
        html.H2(children='Predictions PM25', style={'text-align': 'center'}),
        dash_table.DataTable(
            id='table-df1',
            data=df1.to_dict('records'),
            page_size=10,
            style_table=table_style,
            style_header=header_style,
            style_cell=cell_style,
        ),
        dcc.DatePickerRange(
            id='date-picker-range-df1',
            start_date='2024-02-28',
            end_date='2024-03-29',
            display_format='YYYY-MM-DD',
            style={'width': '25%', 'margin-right': '20px', 'margin-bottom': '20px'}  # Adjust width and add margin
        ),
    ]),
    html.Div([
        dcc.Graph(id='graph-df1'),
        dcc.Graph(id='histogram-df1')
    ], style={'display': 'flex', 'flex-wrap': 'wrap', 'justify-content': 'center', 'margin-bottom': '20px'}),

    html.Div([
        dcc.Graph(id='scatter-df1')
    ], style={'display': 'flex', 'flex-wrap': 'wrap', 'justify-content': 'center', 'margin-bottom': '20px'}),

    # Table for df2
    html.Div([
        html.H2(children='Predictions TEMP', style={'text-align': 'center'}),
        dash_table.DataTable(
            id='table-df2',
            data=df2.to_dict('records'),
            page_size=10,
            style_table=table_style,
            style_header=header_style,
            style_cell=cell_style,
        ),
        dcc.DatePickerRange(
            id='date-picker-range-df2',
            start_date='2024-02-28',
            end_date='2024-03-29',
            display_format='YYYY-MM-DD',
            style={'width': '25%', 'margin-bottom': '20px'}  # Adjust width and add margin
        ),
    ]),
    html.Div([
        dcc.Graph(id='graph-df2'),
        dcc.Graph(id='histogram-df2')
    ], style={'display': 'flex', 'flex-wrap': 'wrap', 'justify-content': 'center', 'margin-bottom': '20px'}),

    html.Div([
        dcc.Graph(id='scatter-df2')
    ], style={'display': 'flex', 'flex-wrap': 'wrap', 'justify-content': 'center', 'margin-bottom': '20px'}),

])


# Callbacks to update the graphs based on dropdown selection and Date Picker Range
@app.callback(
    Output('line-graph', 'figure'),
    Output('histogram', 'figure'),
    Output('scatter-plot', 'figure'),
    [Input('dropdown-graph', 'value'),
    Input('date-picker-range', 'start_date'),
    Input('date-picker-range', 'end_date')]
)
def update_graphs(selected_data, start_date, end_date):
    filtered_df = df[(df['DATETIMEDATA'] >= start_date) & (df['DATETIMEDATA'] <= end_date)]
    line_fig = create_graph(selected_data, filtered_df)
    histogram_fig = create_histogram(selected_data, filtered_df)
    scatter_fig = create_scatter(selected_data, filtered_df)
    return line_fig, histogram_fig, scatter_fig

# Callbacks to update the graphs for df1 and df2
@app.callback(
    Output('graph-df1', 'figure'),
    Output('histogram-df1', 'figure'),
    Output('scatter-df1', 'figure'),
    Output('graph-df2', 'figure'),
    Output('histogram-df2', 'figure'),
    Output('scatter-df2', 'figure'),
    [Input('date-picker-range-df1', 'start_date'),
     Input('date-picker-range-df1', 'end_date'),
     Input('date-picker-range-df2', 'start_date'),
     Input('date-picker-range-df2', 'end_date')]
)
def update_predictions_graphs(start_date_df1, end_date_df1, start_date_df2, end_date_df2):
    filtered_df1 = df1[(df1['DATETIMEDATA'] >= start_date_df1) & (df1['DATETIMEDATA'] <= end_date_df1)]
    filtered_df2 = df2[(df2['DATETIMEDATA'] >= start_date_df2) & (df2['DATETIMEDATA'] <= end_date_df2)]
    fig_df1 = create_predictions_graph('PM25', filtered_df1, 'Predictions PM25')
    fig_histogram_df1 = histogram_predictions_graph('PM25', filtered_df1, 'Predictions PM25')
    fig_scatter_predictions_df1 = scatter_predictions_graph('PM25', filtered_df1, 'Predictions PM25')
    fig_df2 = create_predictions_graph('TEMP', filtered_df2, 'Predictions TEMP')
    fig_histogram_df2 = histogram_predictions_graph('TEMP', filtered_df2, 'Predictions TEMP')
    fig_scatter_predictions_df2 = scatter_predictions_graph('TEMP', filtered_df2, 'Predictions TEMP')
    return fig_df1, fig_histogram_df1, fig_scatter_predictions_df1, fig_df2, fig_histogram_df2, fig_scatter_predictions_df2


# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)

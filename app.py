import dash
from dash import dash_table
from dash import dcc # dash core components
from dash import html
from dash.dependencies import Input, Output
import dash_pivottable


import pandas as pd


df = pd.read_csv('https://bit.ly/elements-periodic-table')


app = dash.Dash(__name__)
def identity(x): return x


cols = df.columns


app.layout = html.Div(children=[
    html.H2(children='Periodic Pivot Table (Cool!)'),
    dcc.Dropdown(
        id="index_dropdown",
        options=[{'label': i, 'value': i} for i in cols],
        multi=False,
        placeholder='Please select a index!'
    ),
    dcc.Dropdown(
        id="column_dropdown",
        options=[{'label': col, 'value': col} for col in cols],
        multi=False,
        placeholder='Please select a column!'
    ),
    dcc.Dropdown(
        id="value_dropdown",
        options=[{'label': val, 'value': val} for val in cols],
        multi=False,
        placeholder='Please select a value!'
    ),
    html.Div(id='output-data-upload'),
])


@app.callback(
    Output('output-data-upload', 'children'),
    [Input('index_dropdown', 'value'), 
     Input('column_dropdown', 'value'), 
     Input('value_dropdown', 'value')]
)
def update_output(index, column, value):
    if index is not None and column is not None and values is not None:
        # pt = df.pivot_table(index=index, columns=column, values=value, aggfunc=identity)
        print(index)
        print(column)
        print(value)

        rows = [list(df.iloc[[index]]) for index in range(df.shape[0])]
        rows.insert (0, df.columns) 

        return html.Div(
            dash_pivottable.PivotTable(
                data=rows,
                cols=["Element"],
                rows=[index],
                vals=[]
            )
    )


app.run_server(debug=True, host="0.0.0.0")
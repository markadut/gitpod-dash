import dash
from dash import dash_table
from dash import dcc # dash core components
from dash import html
import dash_pivottable
import pandas as pd

df = pd.read_csv('https://bit.ly/elements-periodic-table')

app = dash.Dash(__name__)

app.layout = dash_table.DataTable(
    id='table',
    columns=[{"name": i, "id": i} for i in df.columns],
    data=df.to_dict('records'),
)

app.layout = html.Div(
    dash_pivottable.PivotTable(
        data=[
            ["AtomicNumber","Element","Symbol","AtomicMass"],
            [1,"Hydrogen","H",1.007],
            [2,"Helium","He",4.002],
            [3,"Lithium","Li",6.941],
            [4,"Beryllium","Be",9.012],
        ],

        cols=["AtomicNumber"],
        rows=["Element"],
        vals=["Count"]
    )
)

app.run_server(debug=True, host="0.0.0.0")

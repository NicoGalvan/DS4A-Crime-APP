import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Connect to main app.py file
from app import app
from app import server

# Connect to your app pages
from apps import statistics, map, preditor


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div([
        dcc.Link('Statistics|', href='/apps/statistics'),
        dcc.Link('Map', href='/apps/map'),
        dcc.Link('Predictor', href='/apps/preditor'),
    ], className="row"),
    html.Div(id='page-content', children=[])
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/apps/statistics':
        return statistics.layout
    if pathname == '/apps/map':
        return map.layout
    if pathname == '/apps/preditor':
        return preditor.layout
    else:
        return "404 Page Error! Please choose a link"


if __name__ == '__main__':
    app.run_server(debug=False)
import dash
import dash_bootstrap_components as dbc

# from sklearn.preprocessing import scale
external_stylesheets = [
    'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css'
     
]



app = dash.Dash(__name__, suppress_callback_exceptions=True,
                meta_tags=[{'name':'viewport',
                            'content':'width=device-width, initial-scale=1.0'}],
                            external_stylesheets=external_stylesheets
                )

server= app.server
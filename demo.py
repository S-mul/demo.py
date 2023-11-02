import dash
from dash import dcc, html
from flask import Flask 
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Initialize the Flask server
server = Flask(__name__)

# Initialize the Dash app
app = dash.Dash(__name__, server=server ,external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.BOOTSTRAP])
#Read the files
df = pd.read_csv('count.cvs')
df1 =pd.read_csv('data.cvs')
# Build the components
Header_component = html.H1(" Traffic Anaylsis Dashboard ",style={'color':'darkcyan'})
#visual components

#component1
countfig = go.FigureWidget()

countfig.add_scatter(name= "bus", x=df["Time"],y=df["bus"],fill="tonexty")
countfig.add_scatter(name= "car", x=df["Time"],y=df["car"],fill="tonexty")

countfig.update_layout(title= "Vehicle Time Line")

# Define your app layout
app.layout = html.Div(
    [
        dbc.Row([
            Header_component
        ]
        ),
        dbc.Row(
            [dbc.Col(
                [dcc.Graph(figure = countfig)    
            ]),dbc.Col()]
        ),
        dbc.Row(
            [dbc.Col(), dbc.Col(),dbc.Col()]
        )

    ]
)

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)


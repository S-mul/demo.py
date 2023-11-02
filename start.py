from dash import Dash, html

app = Dash(__name__)

app.layout = html.Div([
    html.Div(children='Hello World')
])



app.run_server(debug=True, port=8060)

if __name__ == '__main__':
    app.run(debug=True)

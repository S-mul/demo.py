import dash
from dash import dcc, html, Input, Output

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Registration Form"),
    
    dcc.Input(id='name-input', type='text', placeholder='Full Name'),
    dcc.Input(id='email-input', type='email', placeholder='Email'),
    dcc.Input(id='password-input', type='password', placeholder='Password'),
    dcc.Input(id='confirm-password-input', type='password', placeholder='Confirm Password'),
    
    html.Button('Register', id='register-button'),
    
    html.Div(id='registration-status')
])

@app.callback(
    Output('registration-status', 'children'),
    Input('register-button', 'n_clicks'),
    State('name-input', 'value'),
    State('email-input', 'value'),
    State('password-input', 'value'),
    State('confirm-password-input', 'value')
)
def register(n_clicks, name, email, password, confirm_password):
    if n_clicks is None:
        return ''  # No registration attempt yet
    if not (name and email and password and confirm_password):
        return 'Please fill in all fields.'
    if password != confirm_password:
        return 'Passwords do not match.'
    # You can add your registration logic here
    # For simplicity, we're just displaying a success message
    return f'Registration successful for {name} with email {email}'

if __name__ == '__main__':
    app.run_server(debug=True)
 


import rimble
import dash
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc

import dash_bootstrap_components as dbc

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__,external_stylesheets=external_stylesheets)

server = app.server
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}
sidebar = html.Div(
    [
        html.H2("Dash Rimble UI Components", className="display-4"),
        html.Hr(),
        html.P(
            "Web3 UI Components for python developers", className="lead"
        ),
    ],
    style=SIDEBAR_STYLE,
)
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}
content = html.Div([
    rimble.card(html.H3('Testing card')
    ),
    rimble.box(html.H3('test'),style={'bg':'salmon'}),
    html.Div(id='output', children = rimble.qr(value='hist')),
    dcc.Input(id='input',type='text',value='test'),
    html.Div(id="metamask_button", children=rimble.metamask(id='test',value='Connect with MetaMask')),
    html.Div(id='blockie_output', children = rimble.blockie(id='blockie_test')),
    dcc.Input(id='blockie_input',type='text'),
    html.Div(id='ethaddress',children=rimble.ethaddress(address='test',textLabels=True))
], style = CONTENT_STYLE)

app.layout = html.Div([sidebar, content])


@app.callback(Output('output', 'children'), [Input('input', 'value')])
def display_output(value):
    return rimble.qr(value=value)

@app.callback(Output('blockie_output', 'children'), [Input('blockie_input', 'value')])
def display_blockie(value):
    return rimble.blockie(id='blockie_test',value=value)

if __name__ == '__main__':
    app.run_server(debug=True)

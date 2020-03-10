import rimble
import dash
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc

app = dash.Dash(__name__)

app.layout = html.Div([
    rimble.card(html.H3('Testing card')
    ),
    rimble.box(html.H3('test'),style={'bg':'salmon'}),
    html.Div(id='output', children = rimble.qr(value='hist')),
    dcc.Input(id='input',type='text',value='test'),
    html.Div(id="metamask_button", children=rimble.metamask(id='test',value='Connect with MetaMask')),
    html.Div(id='blockie_output', children = rimble.blockie(id='blockie_test')),
    dcc.Input(id='blockie_input',type='text'),
    html.Div(id='ethaddress',children=rimble.ethaddress(address='test',textLabels=True))
])


@app.callback(Output('output', 'children'), [Input('input', 'value')])
def display_output(value):
    return rimble.qr(value=value)

@app.callback(Output('blockie_output', 'children'), [Input('blockie_input', 'value')])
def display_blockie(value):
    return rimble.blockie(id='blockie_test',value=value)

if __name__ == '__main__':
    app.run_server(debug=True)

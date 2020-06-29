import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

index_page = html.Div([
    dcc.Link('Go to Page Team', href='/team'),
    html.Br(),
    dcc.Link('Go to Page Venue', href='/ven'),
    html.Br(),
    dcc.Link('Go to Page Batsman', href='/batsman'),
    html.Br(),
    dcc.Link('Go to Page Bowler', href='/bowler')
])
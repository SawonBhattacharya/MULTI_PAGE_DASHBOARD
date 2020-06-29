import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output,State
import plotly.graph_objs as go
import pandas as pd
import dash_fun as daf
import plotly.express as px
import base64

#######################################STYLES & IMAGES##########################################################
colors={'Sunrisers Hyderabad':['rgb(252, 111, 3)','black'],'Kolkata Knight Riders':['rgb(34, 19, 77)','rgb(224, 166, 7)'],'Mumbai Indians':['rgb(13, 19, 140)','rgb(22, 149, 181)'],
            'Gujarat Lions':['rgb(212, 82, 6)','rgb(9, 44, 148)'],'Rising Pune Supergiant':['rgb(71, 27, 133)','rgb(210, 38, 252)'], 'Royal Challengers Bangalore':['rgb(199, 12, 24)','black'],
            'Delhi Daredevils':['rgb(5, 20, 79)','rgb(168, 2, 7)'],'Kings XI Punjab':['rgb(227, 5, 30)','rgb(218, 195, 219)'],'Chennai Super Kings':['rgb(222, 215, 11)','rgb(222, 127, 11)'],
            'Deccan Chargers':['rgb(237, 230, 126)','rgb(18, 35, 102)'],'Kochi Tuskers Kerala':['rgb(209, 104, 23)','rgb(131, 23, 209)'],'Pune Warriors':['rgb(19, 80, 112)','rgb(38, 55, 64)'],
            'Delhi Capitals':['rgb(163, 7, 14)','rgb(25, 7, 115)'],'Rajasthan Royals':['rgb(224, 61, 107)','rgb(80, 35, 153)']}

IPL_LOGO = "assets/dashlogo.png"

#data loading
df= pd.read_excel('data/data.xlsx')
dl = pd.read_excel('data/deliveries.xlsx')

batsman_options = []
for bat in dl['batsman'].unique():
    batsman_options.append({'label':str(bat),'value':bat})

bowlers_options = []
for bowl in dl['bowler'].unique():
    bowlers_options.append({'label':str(bowl),'value':bowl})

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

"""Navbar"""
#dropdown Items

navbar = dbc.NavbarSimple(
           children=[
              dbc.NavItem(dcc.Link("INDIAN PREMIER LEAGUE DASHBOARD", href="https://www.iplt20.com/",style={'font-weight': 'bold','color':'white','padding':'10px'})),
              dbc.NavItem(dcc.Link('BATSMEN', href='/batsman',style={'font-weight': 'bold','color':'white','padding':'10px'})),
              dbc.NavItem(dcc.Link('TEAMS', href='/team',style={'font-weight': 'bold','color':'white','padding':'10px'})),
              dbc.NavItem(dcc.Link('VENUES', href='/ven',style={'font-weight': 'bold','color':'white','padding':'10px'}))
            ],
          brand="Bowler",
          brand_href="#",
          color="dark",
          dark=True,
          sticky="top",
        )

#####################################################################################
"""Body Components"""
#Cards
cardTwo = dbc.Card(
    [
        #dbc.CardImg(src="https://i.imgur.com/JnUeE7g.png", top=True),
        dbc.CardBody(
            [
                html.H4("Opponent-Wise Wickets & Favourite Batsman", className="card-title",style={"color":"rgb(250,250,250)"}),
                html.Hr(className="my-2"),
                dcc.Dropdown(id='bowler-picker',options=bowlers_options,value='SP Narine'),
                html.Hr(className="my-2"),
                html.Div(
                    dcc.Graph(id='bowling1',style={'padding':'10px','width': '70vw','align':'center'})
                ),
                html.Br(),
                html.Div(
                    dcc.Graph(id='bowling2',style={'padding':'10px','width': '70vw','align':'center'})
                )

            ]
        )     
    ],
    style={"width": "65rem","position":"center"},color="dark",
)

########################################################################################################

"""Body"""
sp=html.Br()
#rows
row = html.Div(
    [
        
        dbc.Row(html.P('')),
        dbc.Row(
            [
                dbc.Col(html.Div(cardTwo),
                width={"size": 6, "offset": 1},
                )
                
            ],
            #style={'margin': 'auto', 'width': '80vw'},
        ),
    ],style={'backgroundColor':'rgb(3, 16, 33)'}
)

#####################################################################################
foot_alert = html.Div(
    [
        dbc.Alert("Here I have considered Only the who have played in the IPL. In some cases the players have not played all the seasons like others.", color="dark"),
    ]
)
#####################################################################################
"""Layout"""

app.layout = html.Div(
    [navbar,row,foot_alert]
)

#####################################################################################




####################################################################################



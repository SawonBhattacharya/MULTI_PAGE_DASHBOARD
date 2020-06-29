import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output,State
import plotly.graph_objs as go
import pandas as pd
import dash_fun as daf
import test_ven as tv
import plotly.express as px
import base64


###############################TOKEN##############################################
mapbox_access_token='pk.eyJ1Ijoic2FuMTciLCJhIjoiY2tibWdhcG5lMGJ1ajJybWlkZThra3NqMyJ9.UHBZhrCqgqSoEmIwGclNUQ'


#######################################STYLES & IMAGES##########################################################
IPL_LOGO = "assets/dashlogo.png"

#data loading
df= pd.read_excel('data/data.xlsx')
dl = pd.read_excel('data/deliveries.xlsx')

season_options=['2008','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019']
venue_op=['Stadium Names','Average First Innings Score','Average Second Innings Score']
venue_options=[]
for v in venue_op:
    venue_options.append({'label':str(v),'value':v})
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

"""Navbar"""
navbar = dbc.NavbarSimple(
           children=[
              dbc.NavItem(dcc.Link("INDIAN PREMIER LEAGUE DASHBOARD", href="https://www.iplt20.com/",style={'font-weight': 'bold','color':'white','padding':'10px'})),
              dbc.NavItem(dcc.Link('BATSMEN', href='/batsman',style={'font-weight': 'bold','color':'white','padding':'10px'})),
              dbc.NavItem(dcc.Link('BOWLERS', href='/bowler',style={'font-weight': 'bold','color':'white','padding':'10px'})),
              dbc.NavItem(dcc.Link('TEAMS', href='/team',style={'font-weight': 'bold','color':'white','padding':'10px'}))
            ],
          brand="Venue",
          brand_href="#",
          color="dark",
          dark=True,
          sticky="top",
        )


########################INPUT JUMBTRON WITH DROPDOWN#############################################################
jumbotron = dbc.Jumbotron(
    [
        html.H1("Check Your Favourite team's Performance!", className="display-3"),
        html.P(
            "Let's see which ground is more high scoring....",
            className="lead",
        ),
        html.Hr(className="my-2"),
        #dcc.Dropdown(id='season-picker',options=season_options,value='Gujarat Lions'),
        
        
        #dcc.Markdown(id='team-caps')
        
    ]
)
#####################################################################################
cardImage = dbc.Card(
    [
        
        dbc.CardBody(
            [
                dcc.Dropdown(id='ven-picker',options=venue_options,value='Stadium Names'),
                html.Hr(className="my-2"),
                dcc.Graph(id='season',style={'padding':'10px','width': '70vw','align':'center'}),
            ]
        )     
    ],
    style={"height":"64rem","width": "64rem"},color="dark",
)

"""Body"""
#rows
row = html.Div(
        [
            dbc.Row(
            [
                
                dbc.Col(html.Div(cardImage),
                width={"size": 6, "offset": 1},
                ),
                
            ],
                #style={'margin': 'auto', 'width': '80vw'}        
            ),
        ],style={'backgroundColor':'rgb(3, 16, 33)'}
)

#####################################################################################
foot_alert = html.Div(
    [
        dbc.Alert("Here I have considered Only the Home Grounds of the teams played last season(hence record of the teams from the past like RPSG, GL, KTK, PWI, Deccan Chargers, Delhi Daredevils are not there). Also some teams have multiple homeground but I have considered only the primary one.", color="dark"),
    ]
)
#####################################################################################
"""Layout"""

app.layout = html.Div(
    [navbar,jumbotron,row,foot_alert]
)

    
#---------------------------------------------------------------

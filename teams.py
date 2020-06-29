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

team_ground={'Sunrisers Hyderabad':['Rajiv Gandhi Intl. Cricket Stadium'], 'Mumbai Indians':['Wankhede Stadium','Brabourne Stadium'], 
                'Gujarat Lions':['Saurashtra Cricket Association Stadium','Green Park'],
                'Rising Pune Supergiant':['Maharashtra Cricket Association Stadium'], 
                'Royal Challengers Bangalore':['M. Chinnaswamy Stadium'],'Kolkata Knight Riders': ['Eden Gardens'],
                 'Kings XI Punjab':['Punjab Cricket Association Stadium, Mohali',
                 'Himachal Pradesh Cricket Association Stadium','Holkar Cricket Stadium'],
                'Chennai Super Kings':['MA Chidambaram Stadium, Chepauk'], 'Rajasthan Royals': ['Sawai Mansingh Stadium'],
                'Deccan Chargers':['Rajiv Gandhi Intl. Cricket Stadium','Vidarbha Cricket Association Stadium, Jamtha',],                      'Kochi Tuskers Kerala':['Nehru Stadium','Holkar Cricket Stadium'], 
                'Pune Warriors':['Dr DY Patil Sports Academy', 'Maharashtra Cricket Association Stadium'],
                'Delhi Capitals':['Feroz Shah Kotla']
                }
team_info={'Sunrisers Hyderabad':'Kane Williamson','Kolkata Knight Riders':'Dinesh Karthik','Mumbai Indians':'Rohit Sharma',
            'Gujarat Lions':'Suresh Raina','Rising Pune Supergiant':'MS DHONI/Steve Smith', 'Royal Challengers Bangalore':'Virat Kohli',
            'Delhi Daredevils':'Virendar Sehwag/Gautam Gambhir','Kings XI Punjab':'KL RAHUL','Chennai Super Kings':'MS DHONI',
            'Deccan Chargers':'Adam Gilchrist','Kochi Tuskers Kerala':'-----','Pune Warriors':'Sourav Ganguly',
            'Delhi Capitals':'Shreyas Iyer','Rajasthan Royals':'Steve Smith'}
team_pos={'Sunrisers Hyderabad':'Sunrisers Hyderabad was the champion of 2016 IPL. Total 8 teams has participated in that season.','Kolkata Knight Riders':'Kolkata Knight Riders  became the IPL champions in 2012, by defeating Chennai Super Kings in the final. They repeated the feat in 2014, defeating Kings XI Punjab. The Knight Riders hold the record for the longest winning streak by any Indian team in T20s (14).','Mumbai Indians':'Mumbai Indians is the most successful team in league history, having won four titles.They won the trophy in 2013,2015,2017 and 2019.',
            'Gujarat Lions':'Gujarat Lions finished third in 2016 IPL season. They were the table toppers in the group stage.','Rising Pune Supergiant':'Rising Pune Supergiant was the runner up of 2017 season. Mumbai Indians defeated them by a fine margin of 1 run', 'Royal Challengers Bangalore':'Despite of playing three finals, Royal Challengers Bangalore has failed to win the trophy.They were the runners up of 2009, 2011 and 2016',
            'Delhi Daredevils':'In 2012 Virendar Sehwag led Delhi Capitals to the playoffs. They finished in the third position. They were also the table toppers in the group stage.','Kings XI Punjab':'In 2014 Kings XI Punjab was defeated by KKR and finished as Runner up.','Chennai Super Kings':'The Super Kings have lifted the IPL title thrice (in 2010, 2011 and 2018), and have the best win percentage among all teams in the IPL (61.34). They hold the records of most appearances in the IPL playoffs (nine) and in the final (seven).',
            'Deccan Chargers':'Adam Gilchrist led Deccan Chargers, defeated the Royal Challengers Bangalore in the Final by six runs to win their maiden IPL trophy and qualify for the 2009 Champions League Twenty20 (CLT20).','Kochi Tuskers Kerala':'Kochi Tuskers Kerala played only one season in 2011 and finished in the 8th position.','Pune Warriors':'They participated in three season(2011,2012,2013). In the last season they finished in the eighth position',
            'Delhi Capitals':'In 2019 Shreyas Iyer led Delhi Capitals to the playoffs. They finished in the third position.','Rajasthan Royals':'Rajasthan Royals,won the inaugural edition of the IPL under the captaincy of Shane Warne, despite being written off as a title contender by the media and fans.'}


IPL_LOGO = "assets/dashlogo.png"


#data loading
df= pd.read_excel('data/data.xlsx')
dl = pd.read_excel('data/deliveries.xlsx')

team_options = []
for team in df['team1'].unique():
    team_options.append({'label':str(team),'value':team})


app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

"""Navbar"""
navbar = dbc.NavbarSimple(
           children=[
              dbc.NavItem(dcc.Link("INDIAN PREMIER LEAGUE DASHBOARD", href="https://www.iplt20.com/",style={'font-weight': 'bold','color':'white','padding':'10px'})),
              dbc.NavItem(dcc.Link('BATSMEN', href='/batsman',style={'font-weight': 'bold','color':'white','padding':'10px'})),
              dbc.NavItem(dcc.Link('BOWLERS', href='/bowler',style={'font-weight': 'bold','color':'white','padding':'10px'})),
              dbc.NavItem(dcc.Link('VENUES', href='/ven',style={'font-weight': 'bold','color':'white','padding':'10px'}))
            ],
          brand="TEAMS",
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
            "Is your team a good away team or they only perform well in their home ground?",
            className="lead",
        ),
        html.Hr(className="my-2"),
        dcc.Dropdown(id='team-picker-home',options=team_options,value='Gujarat Lions'),
        html.Hr(className="my-2"),
        
        #dcc.Markdown(id='team-caps')
        
    ]
)
#####################################################################################
"""Body Components"""
#Cards
cardOne = dbc.Card(
    [
        #dbc.CardImg(src="https://i.imgur.com/JnUeE7g.png", top=True),
        dbc.CardBody(
            [
                html.H4("HOME RECORDS", className="card-title",style={"color":"rgb(250,250,250)"}),
                
                dcc.Graph(id='team-home'),
            ]
        )     
    ],
    style={"width": "30rem"},color="dark",
)

cardTwo = dbc.Card(
    [
        #dbc.CardImg(src="https://i.imgur.com/JnUeE7g.png", top=True),
        dbc.CardBody(
            [
                html.H4("AWAY RECORDS", className="card-title",style={"color":"rgb(250,250,250)"}),
                
                dcc.Graph(id='team-away'),
            ]
        )     
    ],
    style={"width": "30rem"},color="dark",
)

cardThree = dbc.Card(
    [
        #dbc.CardImg(src="https://i.imgur.com/JnUeE7g.png", top=True),
        dbc.CardBody(
            [
                html.H4("WIN RECORDS AGAINST EACH OPPONENT", className="card-title",style={"color":"rgb(250,250,250)"}),
                
                dcc.Graph(id='team-win'),
            ]
        )     
    ],
    style={"width": "64rem"},color="dark",
)

cardFour = dbc.Card(
    [
        #dbc.CardImg(src="https://i.imgur.com/JnUeE7g.png", top=True),
        dbc.CardBody(
            [
                html.H4("LOSS RECORDS AGAINST EACH OPPONENT", className="card-title",style={"color":"rgb(250,250,250)"}),
                
                dcc.Graph(id='team-loss'),
            ]
        )     
    ],
    style={"width": "64rem"},color="dark",
)

cardFive = dbc.Card(
    [
        #dbc.CardImg(src="https://i.imgur.com/JnUeE7g.png", top=True),
        dbc.CardBody(
            [
                html.H4("Players With Maximum No of 6s", className="card-title",style={"color":"rgb(250,250,250)"}),
                
                dcc.Graph(id='team-six'),
            ]
        )     
    ],
    style={"width": "64rem"},color="dark",
)

cardSix = dbc.Card(
    [
        #dbc.CardImg(src="https://i.imgur.com/JnUeE7g.png", top=True),
        dbc.CardBody(
            [
                html.H4("Players With Maximum No of 4s", className="card-title",style={"color":"rgb(250,250,250)"}),
                
                dcc.Graph(id='team-four'),
            ]
        )     
    ],
    style={"width": "64rem"},color="dark",
)

cardSeven = dbc.Card(
    [
        #dbc.CardImg(src="https://i.imgur.com/JnUeE7g.png", top=True),
        dbc.CardBody(
            [
                html.H4("Best Batsmen of Your Team", className="card-title",style={"color":"rgb(250,250,250)"}),
                
                dcc.Graph(id='team-bat'),
            ]
        )     
    ],
    style={"width": "64rem"},color="dark",
)

cardEight = dbc.Card(
    [
        #dbc.CardImg(src="https://i.imgur.com/JnUeE7g.png", top=True),
        dbc.CardBody(
            [
                html.H4("Best Bowlers of Your Team", className="card-title",style={"color":"rgb(250,250,250)"}),
                
                dcc.Graph(id='team-bowl'),
            ]
        )     
    ],
    style={"width": "64rem"},color="dark",
)

card_content = [
    dbc.CardHeader(dcc.Markdown(id='team-name',className="card-title",style={"color":"rgb(250,250,250)"})),
    dbc.CardBody(
        [
            dcc.Markdown(id='team-pos',className="card-text")
            
        ]
    ),
]

"""Body"""
#rows
row = html.Div(
    [
        dbc.Row(html.P('')),
        dbc.Row(dbc.Col(html.Div(dbc.Col(dbc.Card(card_content, color="dark", inverse=True)),))),
        dbc.Row(html.P('')),
        dbc.Row(
            [
                dbc.Col(html.Div(cardOne)),
                dbc.Col(html.Div(cardTwo)),
                
            ],
            style={'margin': 'auto', 'width': '80vw'},
        ),
        dbc.Row(html.P('')),
        dbc.Row(
            [
                dbc.Col(html.Div(cardThree)),
                
            ],
            style={'margin': 'auto', 'width': '80vw'}        
        ),
        dbc.Row(html.P('')),
        dbc.Row(
            [
                
                dbc.Col(html.Div(cardFour)),
                
            ],
            style={'margin': 'auto', 'width': '80vw'}        
        ),
        dbc.Row(html.P('')),
        dbc.Row(
            [
                
                dbc.Col(html.Div(cardFive)),
                
            ],
            style={'margin': 'auto', 'width': '80vw'}        
        ),
        dbc.Row(html.P('')),
        dbc.Row(
            [
                
                dbc.Col(html.Div(cardSix)),
                
            ],
            style={'margin': 'auto', 'width': '80vw'}        
        ),
        dbc.Row(html.P('')),
        dbc.Row(
            [
                
                dbc.Col(html.Div(cardSeven)),
                
            ],
            style={'margin': 'auto', 'width': '80vw'}        
        ),
        dbc.Row(html.P('')),
        dbc.Row(
            [
                
                dbc.Col(html.Div(cardEight)),
                
            ],
            style={'margin': 'auto', 'width': '80vw'}        
        ),
    ],style={'backgroundColor':'rgb(3, 16, 33)'}
)
#####################################################################################
foot_alert = html.Div(
    [
        dbc.Alert("Here I have considered the matches of 2009 and 2014 as away records because there were no particular home grounds for Teams.", color="dark"),
    ]
)
#####################################################################################

"""Layout"""

app.layout = html.Div(
    [navbar,jumbotron,row,foot_alert]
)



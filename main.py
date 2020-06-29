import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.graph_objs as go
import dash_fun as daf
import test_ven as tv
import plotly.express as px
import index
import batsman
import bowler
import venue
import teams

#print(dcc.__version__) # 0.6.0 or above is required

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

app.config.suppress_callback_exceptions = True
server=app.server
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

########################################################TEAMS###############################################################
@app.callback([Output('team-home', 'figure'),Output('team-away', 'figure'),Output('team-win', 'figure'),Output('team-loss', 'figure'),Output('team-six', 'figure'),Output('team-four', 'figure'),Output('team-bat', 'figure'),Output('team-bowl', 'figure'),Output('team-name','children'),Output('team-pos','children')],
              [Input('team-picker-home', 'value')])


def team_performance_h(selected_team):

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

    

    names=['Wins','Losses']
    home_rec=daf.team_home_performance(selected_team)
    away_rec=daf.team_away_performance(selected_team)
    
    wins=daf.win_stat(selected_team)
    losses=daf.loss_stat(selected_team)
    
    team_6s=daf.team_6s(selected_team)
    team_4s=daf.team_4s(selected_team)

    team_batting=daf.team_batting(selected_team)
    team_bowling=daf.team_bowling(selected_team)    

    fig1 = go.Figure(data=[go.Pie(labels=names,
                             values=home_rec,hole=.3)])
    fig1.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=20,
                  marker=dict(colors=colors[selected_team],line=dict(color='#000000', width=2)))
    
    fig2 = go.Figure(data=[go.Pie(labels=names,
                             values=away_rec,hole=.3)])
    fig2.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=20,
                  marker=dict(colors=colors[selected_team],line=dict(color='#000000', width=2)))

    c=0
    for s in colors[selected_team]:
        if(c==0):
            hc=s
        if(c==1):
            ac=s
        c=c+1
    fig3 = go.Figure(data=[
        go.Bar(name='Home Wins', x=wins['Team'], y=wins['Home_Wins'],marker_color=hc),
        go.Bar(name='Away Wins', x=wins['Team'], y=wins['Away_Wins'],marker_color=ac)
    ])
    # Change the bar mode
    #fig.update_traces(marker_color=colors[selected_team], marker_line_color='rgb(8,48,107)',
     #             marker_line_width=1.5, opacity=0.6)
    fig3.update_layout(barmode='group') 

    fig4 = go.Figure(data=[
        go.Bar(name='Home Losses', x=losses['Team'], y=losses['Home_Losses'],marker_color=hc),
        go.Bar(name='Away Losses', x=losses['Team'], y=losses['Away_Losses'],marker_color=ac)
    ])
    # Change the bar mode
    #fig.update_traces(marker_color=colors[selected_team], marker_line_color='rgb(8,48,107)',
     #             marker_line_width=1.5, opacity=0.6)
    fig4.update_layout(barmode='group')   

    fig5 = go.Figure()
    fig5.add_trace(go.Scatter(x=team_6s['batsman'], y=team_6s['no_of_6s'],
                    mode='lines+markers',
                    name='lines+markers',
                    #text=selected_team,
                    line=dict(color=hc, width=4),
                    text=selected_team)
                    )

    fig6= go.Figure()
    fig6.add_trace(go.Scatter(x=team_4s['batsman'], y=team_4s['no_of_4s'],
                    mode='lines+markers',
                    name='lines+markers',
                    #text=selected_team,
                    line=dict(color=ac, width=4),
                    text=selected_team)
                    )

    fig7 = px.bar(team_batting, x=team_batting['batsman'], y=team_batting['batsman_runs'],color='batsman_runs',
             #labels={'batsman_runs':'Maximum Runs scored for the team'}, 
             height=400)
    #fig7.show()

    fig8 = px.bar(team_bowling, x=team_bowling['bowlers'], y=team_bowling['wickets'],color='wickets',
             #labels={'wickets':'Maximum wickets taken for the team'}, 
             height=400)

    return (fig1,fig2,fig3,fig4,fig5,fig6,fig7,fig8,selected_team,team_pos[selected_team])

####################################################VENUE##############################################################
# Output of Graph
@app.callback(Output('season', 'figure'),
              [Input('ven-picker','value')])

def ven_score(ven_value):
    mapbox_access_token='pk.eyJ1Ijoic2FuMTciLCJhIjoiY2tibWdhcG5lMGJ1ajJybWlkZThra3NqMyJ9.UHBZhrCqgqSoEmIwGclNUQ'
    season_score=pd.DataFrame(columns=['season','Stadium','matches','first_innings_avg','second_innings_avg','Latitude','Longitude'])   

    sta=['Rajiv Gandhi Intl. Cricket Stadium','Wankhede Stadium','M. Chinnaswamy Stadium',
            'Eden Gardens','IS Bindra Stadium','MA Chidambaram Stadium, Chepauk',
            'Sawai Mansingh Stadium','Feroz Shah Kotla']
    for i in sta:
        season_score=season_score.append(tv.venue_score(i,2019))
    #print(season_score)
    if(ven_value=='Stadium Names'):
        # Create figure
        fig = go.Figure(go.Scattermapbox(
                            lon=season_score['Longitude'],
                            lat=season_score['Latitude'],
                            mode='markers',
                            marker=go.scattermapbox.Marker(
                                    size=9,
                                    color='red'
                                    ),
                            #unselected={'marker' : {'opacity':1}},
                            #selected={'marker' : {'opacity':0.5, 'size':25}},
                            text=season_score['Stadium'],
                            #labels=season_score['Stadium']
                            #hovertemplate = "%{label}: <br>Scores: %{text}"
                            hoverinfo='text'
                            
        ))

        # Return figure
        fig.update_layout(
                    width=1000,
                    height=1000,
                    #uirevision= 'foo', #preserves state of figure/map after callback activated
                    #clickmode= 'event+select',
                    hovermode='closest',
                    hoverdistance=2,
                    title=dict(text="Average Score of last season in Each Ground?",font=dict(size=25, color='rgb(32, 45, 128)')),
                    mapbox=dict(
                        accesstoken=mapbox_access_token,
                        bearing=0,
                        style='dark',
                        center=dict(
                            lat=20.5937,
                            lon=78.9629
                        ),
                        pitch=0,
                        zoom=10
                    ),
        )
        return(fig)
    if(ven_value=='Average First Innings Score'):
        # Create figure
        fig = go.Figure(go.Scattermapbox(
                            lon=season_score['Longitude'],
                            lat=season_score['Latitude'],
                            mode='markers',
                            marker=go.scattermapbox.Marker(
                                    size=9,
                                    color='red'
                                    ),
                            #unselected={'marker' : {'opacity':1}},
                            #selected={'marker' : {'opacity':0.5, 'size':25}},
                            text=season_score['first_innings_avg'],
                            #labels=season_score['Stadium']
                            #hovertemplate = "%{label}: <br>Scores: %{text}"
                            hoverinfo='text'
                            
        ))

        # Return figure
        fig.update_layout(
                    width=1000,
                    height=1000,
                    #uirevision= 'foo', #preserves state of figure/map after callback activated
                    #clickmode= 'event+select',
                    hovermode='closest',
                    hoverdistance=2,
                    title=dict(text="Average Score of last season in Each Ground?",font=dict(size=25, color='rgb(55, 24, 64)')),
                    mapbox=dict(
                        accesstoken=mapbox_access_token,
                        bearing=0,
                        style='dark',
                        center=dict(
                            lat=20.5937,
                            lon=78.9629
                        ),
                        pitch=0,
                        zoom=10
                    ),
        )
        return(fig)
    if(ven_value=='Average Second Innings Score'):
        # Create figure
        fig = go.Figure(go.Scattermapbox(
                            lon=season_score['Longitude'],
                            lat=season_score['Latitude'],
                            mode='markers',
                            marker=go.scattermapbox.Marker(
                                    size=9,
                                    color='red'
                                    ),
                            #unselected={'marker' : {'opacity':1}},
                            #selected={'marker' : {'opacity':0.5, 'size':25}},
                            text=season_score['second_innings_avg'],
                            #labels=season_score['Stadium']
                            #hovertemplate = "%{label}: <br>Scores: %{text}"
                            hoverinfo='text'
                            
        ))

        # Return figure
        fig.update_layout(
                    width=1000,
                    height=1000,
                    #uirevision= 'foo', #preserves state of figure/map after callback activated
                    #clickmode= 'event+select',
                    hovermode='closest',
                    hoverdistance=2,
                    title=dict(text="Average Score of last season in Each Ground?",font=dict(size=25, color='rgb(32, 45, 128)')),
                    mapbox=dict(
                        accesstoken=mapbox_access_token,
                        bearing=0,
                        style='dark',
                        center=dict(
                            lat=20.5937,
                            lon=78.9629
                        ),
                        pitch=0,
                        zoom=10
                    ),
        )
        return(fig)        
#---------------------------------------------------------------
#####################################batsman###############################################
@app.callback([Output('batting1', 'figure'),Output('batting2', 'figure')],
              [Input('batsman-picker', 'value')])

def batsman_performance(selected_batsman):
    batsman_seasons=daf.batsman_season(selected_batsman)
    batsman_oppo=daf.batsman_opponent(selected_batsman)
    
    fig1 = px.bar(batsman_seasons, x=batsman_seasons['season'], y=batsman_seasons['batsman_runs'],color='batsman_runs',
             #labels={'batsman_runs':'Maximum Runs scored for the team'}, 
             height=900,width=900)
    
    fig2 = px.bar(batsman_oppo, x=batsman_oppo['opponent'], y=batsman_oppo['batsman_runs'],color='opponent',
             #labels={'batsman_runs':'Maximum Runs scored for the team'}, 
             height=900,width=900)
    
    return (fig1,fig2)
#########################################BOWLERS###########################################

@app.callback([Output('bowling1', 'figure'),Output('bowling2', 'figure')],
              [Input('bowler-picker', 'value')])

def bowler_performance(selected_bowler):
    bowler_seasons=daf.bowler_opp_team(selected_bowler)
    bowler_oppo=daf.bowler_opp_batsman(selected_bowler)
    #bowler_oppo.rename(columns={'opponent':'opponent_batsman'},inplace=True)
    fig1 = px.bar(bowler_seasons, x=bowler_seasons['opponent'], y=bowler_seasons['wickets'],color='wickets',
             #labels={'batsman_runs':'Maximum Runs scored for the team'}, 
             height=900,width=900)
    
    fig2 = go.Figure()
    fig2.add_trace(go.Scatter(x=bowler_oppo['opponent'], y=bowler_oppo['wickets'],
                    mode='lines+markers',
                    name='lines+markers',
                    #text=selected_team,
                    line=dict(color="blue", width=4),
                    text=selected_bowler),
                    ),
    fig2.update_layout(
                        autosize=False,
                        width=1000,
                        height=1000,
                        margin=dict(
                            l=50,
                            r=50,
                            b=100,
                            t=100,
                            pad=4
                        ),
                        paper_bgcolor="rgb(101, 134, 140)",
                    )
                    
    return (fig1,fig2)
#######################################################################################################################
# Index Page callback
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/team':
        return teams.app.layout
    elif pathname == '/batsman':
        return batsman.app.layout
    elif pathname == '/ven':
        return venue.app.layout
    elif pathname == '/bowler':
        return bowler.app.layout
    else:
        return teams.app.layout



if __name__ == '__main__':
    app.run_server(debug=True)
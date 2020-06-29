# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import pandas as pd
import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go
import plotly.express as px


# %%
dl = pd.read_excel('data/deliveries.xlsx')
df=pd.read_excel('data/data.xlsx')
dl.head()


# %%
team_ground={'Sunrisers Hyderabad':['Rajiv Gandhi Intl. Cricket Stadium'], 'Mumbai Indians':['Wankhede Stadium','Brabourne Stadium']
, 'Gujarat Lions':['Saurashtra Cricket Association Stadium','Green Park'],'Rising Pune Supergiant':['Maharashtra Cricket Association Stadium'], 'Royal Challengers Bangalore':['M. Chinnaswamy Stadium'],'Kolkata Knight Riders': ['Eden Gardens'],
 'Delhi Daredevils':['Feroz Shah Kotla Ground'], 'Kings XI Punjab':['Punjab Cricket Association Stadium, Mohali','Himachal Pradesh Cricket Association Stadium','Holkar Cricket Stadium'],
       'Chennai Super Kings':['MA Chidambaram Stadium, Chepauk'], 'Rajasthan Royals': ['Sawai Mansingh Stadium'],
        'Deccan Chargers':['Rajiv Gandhi Intl. Cricket Stadium','Vidarbha Cricket Association Stadium, Jamtha',],
       'Kochi Tuskers Kerala':['Nehru Stadium'], 'Pune Warriors':['Dr DY Patil Sports Academy', 'Maharashtra Cricket Association Stadium','Subrata Roy Sahara Stadium'],
       'Delhi Capitals':['Feroz Shah Kotla Ground']}


# %%
colors={'Sunrisers Hyderabad':['rgb(252, 111, 3)','black'],'Kolkata Knight Riders':['rgb(34, 19, 77)','rgb(224, 166, 7)'],             'Mumbai Indians':['rgb(13, 19, 140)','rgb(22, 149, 181)'],'Gujarat Lions':['rgb(212, 82, 6)','rgb(9, 44, 148)'],              'Rising Pune Supergiant':['rgb(71, 27, 133)','rgb(210, 38, 252)'], 'Royal Challengers Bangalore':['rgb(199, 12, 24)',          'black'],'Delhi Daredevils':['rgb(5, 20, 79)','rgb(168, 2, 7)'],
          'Kings XI Punjab':['rgb(227, 5, 30)','rgb(218, 195, 219)'],
          'Chennai Super Kings':['rgb(222, 215, 11)','rgb(222, 127, 11)'],
          'Deccan Chargers':['rgb(237, 230, 126)','rgb(18, 35, 102)'],
          'Kochi Tuskers Kerala':['rgb(209, 104, 23)','rgb(131, 23, 209)'],
          'Pune Warriors':['rgb(19, 80, 112)','rgb(38, 55, 64)'],'Delhi Capitals':['rgb(163, 7, 14)','rgb(25, 7, 115)'],                 'Rajasthan Royals':['rgb(224, 61, 107)','rgb(80, 35, 153)']}


# %%
def team_home_performance(selected_team):
    #filtered_df = df[df['team1'] ==selected_team]
    h=0
    a=0
    hw=0
    aw=0
    f=0#0home 1 away

    for i,k,j,l in zip(df['team1'],df['team2'],df['venue'],df['winner']):
        f=1
        if ((i==selected_team or k==selected_team)):
            for s in team_ground[selected_team]:
                if(j==s):
                    f=0
            if(f==0):
                h=h+1
                if(l==selected_team):
                    hw=hw+1
            else:
                a=a+1
                if(l==selected_team):
                    aw=aw+1
    home_rec=[hw,h-hw]
    away_rec=[aw,a-aw]
    rec=[hw+aw,(h-hw)+(a-aw)]
    return (home_rec)
    


# %%



# %%
def team_away_performance(selected_team):
    #filtered_df = df[df['team1'] ==selected_team]
    h=0
    a=0
    hw=0
    aw=0
    f=0#0home 1 away

    for i,k,j,l in zip(df['team1'],df['team2'],df['venue'],df['winner']):
        f=1
        if ((i==selected_team or k==selected_team)):
            for s in team_ground[selected_team]:
                if(j==s):
                    f=0
            if(f==0):
                h=h+1
                if(l==selected_team):
                    hw=hw+1
            else:
                a=a+1
                if(l==selected_team):
                    aw=aw+1
    home_rec=[hw,h-hw]
    away_rec=[aw,a-aw]
    rec=[hw+aw,(h-hw)+(a-aw)]
    return (away_rec)
    


# %%
def loss_stat(selected_team):
    oponent_home=dict()
    oponent_away=dict()
    f=0 
    #oponent initialization
    teams=df['team1'].unique()
    for i in teams:
        if(i!=selected_team):
            oponent_home[i]=0
            oponent_away[i]=0
    for i,j,r,k,l in zip(df['team1'],df['team2'],df['result'],df['winner'],df['venue']):
        f=1
        if(r=='normal'):
            if(i==selected_team or j==selected_team):
                if(k!=selected_team and k!='nan'):
                    #print(k)
                    for s in team_ground[selected_team]:
                        #print(s,"-",l)
                        if(s==l):
                            f=0
                            if(f==0):  
                                #pass 
                    
                                oponent_home[k]=int(oponent_home[k])+1
                                #print(oponent_home[k],"-",k)
                    
                        if(f==1):
                            #pass
                            oponent_away[k]=int(oponent_away[k])+1
                            #print(oponent_away[k],"-",k)
    loss_home=pd.DataFrame(oponent_home.items())
    loss_home=pd.DataFrame(oponent_home.items(), columns=['Team', 'Home_Losses'])            
    
    loss_away=pd.DataFrame(oponent_away.items())
    loss_away=pd.DataFrame(oponent_away.items(), columns=['Team', 'Away_Losses'])            
    
    losses=pd.merge(loss_home,loss_away,how='inner',on='Team')
    return (losses)


# %%



# %%
def win_stat(selected_team):
    oponent_home=dict()
    oponent_away=dict()
    f=0 
    op=""
    #oponent initialization
    teams=df['team1'].unique()
    for i in teams:
        if(i!=selected_team):
            oponent_home[i]=0
            oponent_away[i]=0
    for i,j,r,k,l in zip(df['team1'],df['team2'],df['result'],df['winner'],df['venue']):
        f=1
        if(r=='normal'):
            if(i==selected_team or j==selected_team):
                if(i!=selected_team):
                    op=i
                if(j!=selected_team):
                    op=j
                if(k==selected_team):
                    for s in team_ground[selected_team]:
                        #print(s,"-",l)
                        if(s==l):
                            f=0
                        if(f==0):   
                            oponent_home[op]=int(oponent_home[op])+1
                    if(f==1):
                        oponent_away[op]=int(oponent_away[op])+1
    win_home=pd.DataFrame(oponent_home.items())
    win_home=pd.DataFrame(oponent_home.items(), columns=['Team', 'Home_Wins'])            
    
    win_away=pd.DataFrame(oponent_away.items())
    win_away=pd.DataFrame(oponent_away.items(), columns=['Team', 'Away_Wins'])            
    
    wins=pd.merge(win_home,win_away,how='inner',on='Team')
    
    return (wins)
    
    
    
    


# %%



# %%
def team_batting(selected_team):
    bn=[]
    tr=[]
    sbt=pd.DataFrame(columns=['batsman','batsman_runs'])
    batsmen = df[['id','season']].merge(dl, left_on = 'id', right_on = 'match_id', how = 'left').drop('id', axis = 1)
    season=batsmen.groupby(['batsman','batting_team'])['batsman_runs'].sum().reset_index()
    #print(season)
    for i,j,k in zip(season['batsman'],season['batting_team'],season['batsman_runs']):
        if(j==selected_team):
            bn.append(i)
            tr.append(k)
    sbt['batsman']=bn
    sbt['batsman_runs']=tr
    sbt=sbt.sort_values(by='batsman_runs',ascending=False).reset_index(drop=True)
    sbt_ret=sbt.head(10)
    return (sbt_ret)


# %%



# %%
def team_6s(selected_team):
    bn=[]
    tr=[]
    sbt=pd.DataFrame(columns=['batsman','no_of_6s'])
    
    df_sixes = dl[['batsman','batting_team','batsman_runs']][dl.batsman_runs==6].groupby(['batsman','batting_team'])['batsman_runs'].count()            .reset_index()
    
    for i,j,k in zip(df_sixes['batsman'],df_sixes['batting_team'],df_sixes['batsman_runs']):
        
        if(j==selected_team):
            bn.append(i)
            tr.append(k)
    sbt['batsman']=bn
    sbt['no_of_6s']=tr
    sbt=sbt.sort_values(by='no_of_6s',ascending=False)
    sbt_ret=sbt.head(10)
    return (sbt_ret)


# %%



# %%
def team_4s(selected_team):
    bn=[]
    tr=[]
    sbt=pd.DataFrame(columns=['batsman','no_of_4s'])
    
    df_fours = dl[['batsman','batting_team','batsman_runs']][dl.batsman_runs==4].groupby(['batsman','batting_team'])['batsman_runs'].count()            .reset_index()
    
    for i,j,k in zip(df_fours['batsman'],df_fours['batting_team'],df_fours['batsman_runs']):
        
        if(j==selected_team):
            bn.append(i)
            tr.append(k)
    sbt['batsman']=bn
    sbt['no_of_4s']=tr
    sbt=sbt.sort_values(by='no_of_4s',ascending=False)
    sbt_ret=sbt.head(10)
    return (sbt_ret)


# %%



# %%
def team_bowling(selected_team):
    bn=[]
    tr=[]
    sbt=pd.DataFrame(columns=['bowlers','wickets'])
    
    bowlers=dl.groupby('bowler').sum().reset_index()
    bowl=dl['bowler'].value_counts().reset_index()
    bowlers=bowlers.merge(bowl,left_on='bowler',right_on='index',how='left')
    bowlers=bowlers[['bowler_x','total_runs','bowler_y']]
    bowlers.rename({'bowler_x':'bowler','total_runs':'runs_given','bowler_y':'balls'},axis=1,inplace=True)
    bowlers['overs']=(bowlers['balls']//6)

    dismissal_kinds = ["bowled", "caught", "lbw", "stumped", "caught and bowled", "hit wicket"]  
    ct=dl[dl["dismissal_kind"].isin(dismissal_kinds)]
    ct=ct.groupby(['bowler','bowling_team']).size().reset_index()
    ct=ct.rename(columns={0:'wickets'}).sort_values(by='wickets')
    #print(bowlers)
    for i,j,k in zip(ct['bowler'],ct['bowling_team'],ct['wickets']):
        if(j==selected_team):
            bn.append(i)
            tr.append(k)
    sbt['bowlers']=bn
    sbt['wickets']=tr
    sbt=sbt.sort_values(by='wickets',ascending=False).reset_index(drop=True)
    sbt_ret=sbt.head(10)
    return (sbt_ret)


# %%



# %%
def venue_score(selected_venue,ssn):
    sn=[]
    mtc=[]
    avg1=[]
    avg2=[]
    std=[]
    

    batsmen = df[['id','season','venue']].merge(dl, left_on = 'id', right_on = 'match_id', how = 'left').drop('id', axis = 1)
    avgruns_each_season=df.groupby(['season','venue']).count().id.reset_index()
    avgruns_each_season.rename(columns={'id':'matches'},inplace=1)
    season=batsmen[batsmen.inning==1].groupby(['season','venue'])['total_runs'].sum().reset_index()
    avgruns_each_season['total_runs_1']=season['total_runs']
    season=batsmen[batsmen.inning==2].groupby(['season','venue'])['total_runs'].sum().reset_index()
    avgruns_each_season['total_runs_2']=season['total_runs']

    avgruns_each_season['average_runs_1st_inn']=avgruns_each_season['total_runs_1']/avgruns_each_season['matches']
    avgruns_each_season['average_runs_2nd_inn']=avgruns_each_season['total_runs_2']/avgruns_each_season['matches']

    lat=['17.4065','18.9389','12.9788','22.5646','30.6909','13.0629','26.8940','28.6379']
    lon=['78.5505','72.8258','77.5998','88.3433','76.7375','80.2792','75.8032','77.2432']
    sta=['Rajiv Gandhi Intl. Cricket Stadium','Wankhede Stadium','M. Chinnaswamy Stadium','Eden Gardens',
        'IS Bindra Stadium','MA Chidambaram Stadium, Chepauk','Sawai Mansingh Stadium','Feroz Shah Kotla']
    
    ven_info=pd.DataFrame(columns=['Stadium','Latitude','Longitude'])
    
    ven_info['Stadium']=sta
    ven_info['Latitude']=lat
    ven_info['Longitude']=lon

    for s,v,m,a1,a2 in zip(avgruns_each_season['season'],avgruns_each_season['venue'],avgruns_each_season['matches'],avgruns_each_season['average_runs_1st_inn'],avgruns_each_season['average_runs_2nd_inn']):
        #print(selected_venue)
        if(v==selected_venue):
            #print(selected_venue)
            std.append(v)
            
            sn.append(s)
            
            mtc.append(m)
            
            avg1.append(a1)
            
            avg2.append(a2)
            
            
   
    venue_avg=pd.DataFrame(columns=['season','Stadium','matches','first_innings_avg','second_innings_avg'])
    venue_avg['season']=sn
    venue_avg['Stadium']=std
    venue_avg['matches']=mtc
    venue_avg['first_innings_avg']=avg1
    venue_avg['second_innings_avg']=avg2
    
    va=pd.merge(venue_avg[venue_avg.season==ssn],ven_info[ven_info.Stadium==selected_venue],on='Stadium')
    #print(va)
    return (va)


# %%



# %%
def batsman_season(selected_batsman):
    sn=[]
    rn=[]
    sbt=pd.DataFrame(columns=['season','batsman_runs'])
    batsmen = df[['id','season']].merge(dl, left_on = 'id', right_on = 'match_id', how = 'left').drop('id', axis = 1)
    season=batsmen.groupby(['batsman','season'])['batsman_runs'].sum().reset_index()
    #print(season)
    for i,j,k in zip(season['batsman'],season['season'],season['batsman_runs']):
        if(i==selected_batsman):
            sn.append(j)
            rn.append(k)
    sbt['season']=sn
    sbt['batsman_runs']=rn
    sbt=sbt.sort_values(by='batsman_runs',ascending=False).reset_index(drop=True)
    sbt_ret=sbt
    return (sbt_ret)


# %%



# %%
def batsman_opponent(selected_batsman):
    sn=[]
    rn=[]
    sbt=pd.DataFrame(columns=['opponent','batsman_runs'])
    batsmen = df[['id','season']].merge(dl, left_on = 'id', right_on = 'match_id', how = 'left').drop('id', axis = 1)
    season=batsmen.groupby(['batsman','bowling_team'])['batsman_runs'].sum().reset_index()
    #print(season)
    for i,j,k in zip(season['batsman'],season['bowling_team'],season['batsman_runs']):
        if(i==selected_batsman):
            sn.append(j)
            rn.append(k)
    sbt['opponent']=sn
    sbt['batsman_runs']=rn
    sbt=sbt.sort_values(by='batsman_runs',ascending=False).reset_index(drop=True)
    sbt_ret=sbt
    return (sbt_ret)


# %%



# %%
def bowler_opp_team(selected_bowler):
    
    ot=[]
    wk=[]
    sbt=pd.DataFrame(columns=['opponent','wickets'])

    bowlers=dl.groupby('bowler').sum().reset_index()
    bowl=dl['bowler'].value_counts().reset_index()
    bowlers=bowlers.merge(bowl,left_on='bowler',right_on='index',how='left')
    bowlers=bowlers[['bowler_x','total_runs','bowler_y']]
    bowlers.rename({'bowler_x':'bowler','total_runs':'runs_given','bowler_y':'balls'},axis=1,inplace=True)
    bowlers['overs']=(bowlers['balls']//6)

    dismissal_kinds = ["bowled", "caught", "lbw", "stumped", "caught and bowled", "hit wicket"]  
    ct=dl[dl["dismissal_kind"].isin(dismissal_kinds)]
    ct=ct.groupby(['bowler','batting_team']).size().reset_index()
    ct=ct.rename(columns={0:'wickets'}).sort_values(by='wickets',ascending=False)
    for b,o,w in zip(ct['bowler'],ct['batting_team'],ct['wickets']):
        if(b==selected_bowler):
            ot.append(o)
            wk.append(w)
    sbt['opponent']=ot
    sbt['wickets']=wk
    sbt=sbt.sort_values(by='wickets',ascending=False).reset_index(drop=True)
    sbt_ret=sbt
    return (sbt_ret)


# %%



# %%
def bowler_opp_batsman(selected_bowler):
    
    ot=[]
    wk=[]
    sbt=pd.DataFrame(columns=['opponent','wickets'])

    bowlers=dl.groupby('bowler').sum().reset_index()
    bowl=dl['bowler'].value_counts().reset_index()
    bowlers=bowlers.merge(bowl,left_on='bowler',right_on='index',how='left')
    bowlers=bowlers[['bowler_x','total_runs','bowler_y']]
    bowlers.rename({'bowler_x':'bowler','total_runs':'runs_given','bowler_y':'balls'},axis=1,inplace=True)
    bowlers['overs']=(bowlers['balls']//6)

    dismissal_kinds = ["bowled", "caught", "lbw", "stumped", "caught and bowled", "hit wicket"]  
    ct=dl[dl["dismissal_kind"].isin(dismissal_kinds)]
    ct=ct.groupby(['bowler','batsman']).size().reset_index()
    ct=ct.rename(columns={0:'wickets'}).sort_values(by='wickets',ascending=False)
    for b,o,w in zip(ct['bowler'],ct['batsman'],ct['wickets']):
        if(b==selected_bowler):
            ot.append(o)
            wk.append(w)
    sbt['opponent']=ot
    sbt['wickets']=wk
    sbt=sbt.sort_values(by='wickets',ascending=False).reset_index(drop=True)
    sbt_ret=sbt.head(10)
    return (sbt_ret)


# %%



# %%
'''def win_stat(selected_team):
    oponent_home=dict()
    oponent_away=dict()
    f=0 
    op=""
    #oponent initialization
    teams=df['team1'].unique()
    for i in teams:
        if(i!=selected_team):
            oponent_home[i]=0
            oponent_away[i]=0
    for i,j,k,l in zip(df['team1'],df['team2'],df['winner'],df['venue']):
        f=1
        if(i==selected_team or j==selected_team):
            if(i!=selected_team):
                op=i
            if(j!=selected_team):
                op=j
            if(k==selected_team):
                for s in team_ground[selected_team]:
                    #print(s,"-",l)
                    if(s==l):
                        f=0
                if(f==0):   
                    oponent_home[op]=int(oponent_home[op])+1
                if(f==1):
                    oponent_away[op]=int(oponent_away[op])+1
    win_home=pd.DataFrame(oponent_home.items())
    win_home=pd.DataFrame(oponent_home.items(), columns=['Team', 'Home_Wins'])            
    
    win_away=pd.DataFrame(oponent_away.items())
    win_away=pd.DataFrame(oponent_away.items(), columns=['Team', 'Away_Wins'])            
    
    wins=pd.merge(win_home,win_away,how='inner',on='Team')
    
    print(wins)
    c=0
    for s in colors[selected_team]:
        if(c==0):
            hc=s
        if(c==1):
            ac=s
        c=c+1
    fig = go.Figure(data=[
        go.Bar(name='Home Wins', x=wins['Team'], y=wins['Home_Wins'],marker_color=hc),
        go.Bar(name='Away Wins', x=wins['Team'], y=wins['Away_Wins'],marker_color=ac)
    ])
    # Change the bar mode
    #fig.update_traces(marker_color=colors[selected_team], marker_line_color='rgb(8,48,107)',
     #             marker_line_width=1.5, opacity=0.6)
    #fig.update_layout(barmode='group')
    #fig.show()'''


# %%
'''
bowlers=dl.groupby('bowler').sum().reset_index()
bowl=dl['bowler'].value_counts().reset_index()
bowlers=bowlers.merge(bowl,left_on='bowler',right_on='index',how='left')
bowlers=bowlers[['bowler_x','total_runs','bowler_y']]
bowlers.rename({'bowler_x':'bowler','total_runs':'runs_given','bowler_y':'balls'},axis=1,inplace=True)
bowlers['overs']=(bowlers['balls']//6)

dismissal_kinds = ["bowled", "caught", "lbw", "stumped", "caught and bowled", "hit wicket"]  
ct=dl[dl["dismissal_kind"].isin(dismissal_kinds)]
ct=ct.groupby(['bowler','batsman']).size().reset_index()
ct=ct.rename(columns={0:'wickets'}).sort_values(by='wickets',ascending=False)
for b,o,w in zip(ct['bowler'],ct['batsman'],ct['wickets']):
    if(b=='SP Narine'):
        print(b,"\t",o,"\t",w,"\t")
'''


# %%
'''batsmen = df[['id','season']].merge(dl, left_on = 'id', right_on = 'match_id', how = 'left').drop('id', axis = 1)
season=batsmen.groupby(['batsman','season'])['batsman_runs'].sum().reset_index()
season=df.groupby(['team1','season']).count().id.reset_index()
season.rename(columns={'id':'matches'},inplace=1)
print(season.head(4))
'''


# %%
'''
df_strike_rate = dl.groupby(['batsman']).agg({'ball':'count','batsman_runs':'mean'}).sort_values(by='batsman_runs',ascending=False)
df_strike_rate.rename(columns ={'batsman_runs' : 'strike rate'}, inplace=True)
df_runs_per_match = dl.groupby(['batsman','match_id']).agg({'batsman_runs':'sum'})
df_total_runs = df_runs_per_match.groupby(['batsman']).agg({'sum' ,'mean','count'})
df_total_runs.rename(columns ={'sum' : 'batsman run','count' : 'match count','mean' :'average score'}, inplace=True)
df_total_runs.columns = df_total_runs.columns.droplevel()
df_sixes = dl[['batsman','batting_team','batsman_runs']][dl.batsman_runs==6].groupby(['batsman','batting_team']).agg({'batsman_runs':'count'})
df_four = dl[['batsman','batting_team','batsman_runs']][dl.batsman_runs==4].groupby(['batsman','batting_team']).agg({'batsman_runs':'count'})
df_batsman_stat = pd.merge(pd.merge(pd.merge(df_strike_rate,df_total_runs, left_index=True, right_index=True),
                                    df_sixes, left_index=True, right_index=True),df_four, left_index=True, right_index=True)
print(df_runs_per_match.head(10))
'''


# %%
'''
print(df_batsman_stat.columns)
df_batsman_stat.rename(columns = {'ball' : 'ball', 'strike rate':'strike_rate','batsman run' : 'batsman_run',
                                  'match count' : 'match_count','average score' : 'average_score' ,'batsman_runs_x' :'six',
                                  'batsman_runs_y':'four'},inplace=True)
df_batsman_stat['strike_rate'] = df_batsman_stat['strike_rate']*100
df_batsman_stat.sort_values(by='batsman_run',ascending=False,inplace=True)
#df_batsman_stat.sort_values(by='batsman_run',ascending=False)
#df_batsman_stat.reset_index(inplace=True)
print(df_batsman_stat.head(10))

bowlers=dl.groupby('bowler').sum().reset_index()
bowl=dl['bowler'].value_counts().reset_index()
print(bowl)
bowlers=bowlers.merge(bowl,left_on='bowler',right_on='index',how='left')
bowlers=bowlers[['bowler_x','total_runs','bowler_y']]
bowlers.rename({'bowler_x':'bowler','total_runs':'runs_given','bowler_y':'balls'},axis=1,inplace=True)
bowlers['overs']=(bowlers['balls']//6)

bowlers['economy']=(bowlers['runs_given']/bowlers['overs'])

print(bowl.columns)

'''


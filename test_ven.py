import pandas as pd
import numpy as np

dl = pd.read_excel('data/deliveries.xlsx')
df=pd.read_excel('data/data.xlsx')

def venue_score(selected_venue,ssn):
    sn=[]
    mtc=[]
    avg1=[]
    avg2=[]
    std=[]
    lati=[]
    longi=[]

    batsmen = df[['id','season','venue']].merge(dl, left_on = 'id', right_on = 'match_id', how = 'left').drop('id', axis = 1)
    avgruns_each_season=df.groupby(['season','venue']).count().id.reset_index()
    avgruns_each_season.rename(columns={'id':'matches'},inplace=1)
    season=batsmen[batsmen.inning==1].groupby(['season','venue'])['total_runs'].sum().reset_index()
    avgruns_each_season['total_runs_1']=season['total_runs']
    season=batsmen[batsmen.inning==2].groupby(['season','venue'])['total_runs'].sum().reset_index()
    avgruns_each_season['total_runs_2']=season['total_runs']

    avgruns_each_season['average_runs_1st_inn']=avgruns_each_season['total_runs_1']/avgruns_each_season['matches']
    avgruns_each_season['average_runs_2nd_inn']=avgruns_each_season['total_runs_2']/avgruns_each_season['matches']

    lat=[17.4065,18.9389,12.9788,22.5646,30.6909,13.0629,26.8940,28.6379]
    lon=[78.5505,72.8258,77.5998,88.3433,76.7375,80.2792,75.8032,77.2432]
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



    
    

    
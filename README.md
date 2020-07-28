# Multi-Page Interactive Dashboard using Dash & Plotly

## Data V⁮isulization
According to the World Economic Forum, the world produces 2.5 quintillion bytes of data every day, and 90% of all data has been created in the last two years. With so much data, it’s become increasingly difficult to manage and make sense of it all. It would be impossible for any single person to wade through data line-by-line and see distinct patterns and make observations. Data proliferation can be managed as part of the data science process, which includes data visualization.Companies who can gather and quickly act on their data will be more competitive in the marketplace because they can make informed decisions sooner than the competition. Speed is key, and data visualization aides in the understanding of vast quantities of data by applying visual representations to the data. 

## Dashboard
A data dashboard is an information management tool that visually tracks, analyzes and displays key performance indicators (KPI), metrics and key data points to monitor the health of a business, department or specific process. They are customizable to meet the specific needs of a department and company. Data is visualized on a dashboard as tables, line charts, bar charts and gauges so that users can track the health of their business against benchmarks and goals.A data dashboard is the most efficient way to track multiple data sources because it provides a central location for businesses to monitor and analyze performance. Real-time monitoring reduces the hours of analyzing and long line of communication that previously challenged businesses.

## Motivation
IPL(Indian Premier League) is currently one of the biggest leagues in the world.Every year nearly 60 matches played among 8 to 10 teams.Naturally a lot of data is generated after each season. In this project i have collected those data from kaggle and it contains ball by ball match details from 2008 to 2019. 
Dashboard will provide every possible kind of data from winning percentage to average score of each ground.

## Framework & Packages

1. Plotly
        Plotly Python is a library which helps in data visualisation in an interactive manner. But you might be wondering why do we need Plotly when we already have matplotlib which does the same thing. Plotly was created to make data more meaningful by having interactive charts and plots which could be created online as well. The fact that we could visualise data online removed a lot of hurdles which are associated with the offline usage of a library. However, Plotly can be used as both, an offline as well as online tool, thus giving us the best of both worlds.

Installation of Plotly in anaconda prompt
```bash
    pip install plotly
```

2. Dash
         Dash is an open source Python framework for building web applications, created and maintained by the people at Plotly. Dash’s web graphics are completely interactive because the framework is built on top of Ploty.js, a JavaScript library written and maintained by Ploty. This means that after importing the Dash framework into a Python file you can build a web application writing strictly in Python with no other languages necessary. 

Installation of Dash in anaconda prompt
```bash
    pip install dash
```
3. Dash Bootsrap Components
        dash-bootstrap-components is a library of Bootstrap components for Plotly Dash, that makes it easier to build consistently styled apps with complex, responsive layouts.Once installed, just link a Bootstrap stylesheet and start using the components exactly like you would use other Dash component libraries.Bootstrap components are available as native Dash components to let you easily incorporate them into your Dash apps. Each component exposes a number of props to let you control the behaviour with Dash callbacks.Dash Bootstrap Components is compatible with any Bootstrap v4 stylesheet of your choice. Learn how to customise the look of your app using the bundled themes or your own custom themes.
Installation of Dash Bootsrap Components in anaconda prompt:
```bash
        pip install dash-bootstrap-components
```

Install all the other system requirments by:
```bash 
pip install -r requirements.txt
```

After the system has been setup. Run the command: 
```bash 
python main.py
```
### Run the system
Open your browser and in the search bar type: 
<b>localhost:8050</b> be defualt dash uses this port . 
In case, this port is not available in your system, dash will try to use another port. The port number will be displayed in the command prompt.
So, type in the same port number in that case as: 
<b>localhost:<port_number></b>.

After all these steps have been completed successfully, you will be able to the multipage dashboard. Explore all the pages to understand all the functionalities of the dashboard.

### Functionalities of the IPL-Dashboard
    After successfully running the main.py file in the browser you can see the homepage of the dashboard.The home ppage mainly contains the details of each team(home away win&loss percentage, team wise win&loss percentage, top run getter and biggest hitters of each team). Other pages like Batsman contains the seasonwise batting details of all the batsmen who have participated in IPL, same goes for Bowler page. The last page is about grounds.It contains the map and each home ground is located on the map with the average scores of first inning as well as second inning.

### Fututre Scope
        I am trying to host it on a platform. Though I have tried to host it on Herokuapp due to timeout during callbacks it has failed.
### Demo Link:
    
    <a href="https://youtu.be/SlPtlaAIG24" target="_blank">Check the Demo</a>


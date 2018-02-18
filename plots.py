from plotly.offline import plot, iplot
import plotly.graph_objs as go
import plotly.figure_factory as ff
import quandl

#Graph1
x_values_1=[15, 50, 15, 20]
y_values_1=['x8', 'x7', 'x6', 'x5']
x_values_2=[-15, -50, -5, -35]
y_values_2=['x4','x3','x2','x1']

trace_1=go.Bar(x=x_values_1, y=y_values_1,name="<b>Negative</b>",
            orientation='h',
              marker=dict(
              color='rgb(255,211,155)',
              line=dict(
              color='rgb(139,115,85)',
              width=1.3)
              ),
              opacity=0.6)
trace_2=go.Bar(x=x_values_2, y=y_values_2, name="Positive",
              orientation='h',
              marker=dict(
              color='rgb(158,202,225)',
              line=dict(
              color='rgb(8,48,107)',
              width=1.3)
              ),
               opacity=0.6
              )
layout=dict(barmode='group',
           title='<b>Correlations with employees probability of churn</b>',
           yaxis=dict(
           title='Variable')
           )
data=[trace_1, trace_2]
figure_1=dict(data=data, layout=layout)


#Graph2
quandl.ApiConfig.api_key = "NjhFLGMcR7KtexSNb4yv"
data=quandl.get("FRED/GDP")
data_for_graph=data[:]
data.head()

import pandas as pd

x_values=pd.to_datetime(data_for_graph.index.values)
y_values=data_for_graph.Value
trace=go.Scatter(x=x_values, y=y_values, mode='lines', fill='tozeroy')

layout=dict(title='<b>US GDP over time</b>')

data=[trace]
figure_2=dict(data=data, layout=layout)


#Graph3
quandl.ApiConfig.api_key = "NjhFLGMcR7KtexSNb4yv"
data_1=quandl.get('WIKI/GOOGL')
data_2=quandl.get('BCHARTS/ABUCOINSUSD')

data_1.head()
data_2.head()

trace_G=go.Box(x=data_1.Open.pct_change(),
              name='<b>Google</b>')
trace_B=go.Box(x=data_2.Open.pct_change(),
              name='<b>Bitcoin</b>')
layout=dict(boxmode='group',
           title='<i>Distribution of Price Changes</i>',
          )

data=[trace_B, trace_G]

figure_3=dict(data=data, layout=layout)


#Table
quandl.ApiConfig.api_key = "NjhFLGMcR7KtexSNb4yv"
data_G=quandl.get('WIKI/GOOGL')
data_B=quandl.get('BCHARTS/ABUCOINSUSD')
data_G4=data_G[0:5]
data_B4=data_B[0:5]

header=dict(values=['Google','Bitcoin'],
           align=['left','center'],
           font=dict(color='white', size=12),
           fill=dict(color=["#119DFF"])
                            )
cells=dict(values=[data_G4.Open.pct_change().round(3)[1:5],
                 data_B4.Open.pct_change().round(3)[1:5]],
          align=['left','center'],
          fill=dict(color=['yellow','white'])
          )
                            
trace=go.Table(header=header, cells=cells)
                            
data=[trace]
layout=dict(width=500, height=300)
figure_4=dict(data=data, layout=layout)


#Graph4
df=[dict(Task="Task 1", Start='2018-01-01', Finish='2018-01-31', Resource='Idea Validation'),
   dict(Task='Task 2', Start='2018-03-01', Finish='2018-04-15', Resource='Team Formation'),
    dict(Task='Task 3', Start='2018-04-16', Finish='2018-09-30', Resource='Prototyping')
   ]
colors=['rgb(38,120,178)','rgb(253,127,40)','rgb(51,159,52)']
           
figure_5=ff.create_gantt(df, colors=colors,index_col='Resource', show_colorbar=True, title='Startup Roadmap')






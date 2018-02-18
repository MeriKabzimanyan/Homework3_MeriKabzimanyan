import dash
import dash_html_components as html 
import dash_core_components as dcc 

from plots import figure_1
from plots import figure_2
from plots import figure_3
from plots import figure_4
from plots import figure_5

app=dash.Dash()
app.css.append_css({'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'})

app.layout=html.Div([
	html.Div([
		html.H1(children='Homework 3', style={'color':'brown', 'fontFamily':"Comic Sans MS", "textAlign":'center'})]),
	html.Div([
		html.Div([
			html.P("Homework 3 assumes the development of this web application using Dash and Plotly in Python. You are required to develop 6 plots (including one table) with the given layout. Subtle differences related to styling (colors etc) are allowed, yet the general layout must be kept to perceive same information as this website does. Quandl is used as a data source for 4 plots among 6, while the other 2 are based on user provided data. Some of the Quandl based plots require minor analysis using pandas. You are encouraged to follow below mentioned steps to complete the HW:"),
			html.P(children='1.Start from first developing the 6 plots in Jupyter Notebook,'),
			html.P(children='2.Once plots are ready post them into the Dash app,'),
			html.P(children='3.Add HTML components (website heading etc.),'),
			html.P(children='4.Structure the layout of the dashboard.')],
			className='four columns'),
		html.Div([
			html.H5(children='Graph 1', style={'textAlign': 'left', 'fontWeight':'bold'}),
			html.P("The graph on the right hand side is showing correlations of different variables (call them from x1 to x8) with employee churn. Data is artificial, manually inputted by the developer. Recreate the graph. Small coloring or corelation value differences will be neglected.")],className='two columns'),
			html.Div([dcc.Graph(id="figure_1", figure=figure_1)], className='six columns')
			],className='row'),
		html.Div([
			html.Div([
				html.H5(children='Graph 2', style={'textAlign': 'left', 'fontWeight':'bold'}),
				html.P("One the right hand side we have US GDP graphed over time. The data is sourced from QUANDL API (FRED/GDP). Your task is to recreate exactly the same graph.")],className='four columns'),
				html.Div([dcc.Graph(id='figure_2', figure=figure_2)], className='seven columns')
				],className='row'),
			html.Div([
				html.Div([
					html.H5(children='Graph 3 and 4',style={'textAlign': 'left', 'fontWeight':'bold'}),
					html.P("The two graphs on this row are based on Google's stock (WIKI/GOOGL) and Bitcoin's (BCHARTS/ABUCOINSUSD) prices sourced from Quandl. First, percentage changes are calculated. Then the latter is plotted using Box plot to find the distribution and outliers. In the end the first 4 percentage changes (apart from the very first one, which is N/A) are plotted in a table. Recreate similar graphs with the same values (minor styling is neglected).")],className='three columns'),
				html.Div([dcc.Graph(id='figure_3', figure=figure_3)],className='seven columns'),
				html.Div([dcc.Graph(id='figure_4', figure=figure_4)],className='two columns')],
				className='row'),
			html.Div([
				html.Div([
					html.H5(children='Graph 5',style={'textAlign': 'left', 'fontWeight':'bold'}),
					html.P("Last graph is based on manually inputted data. It shows the Roadmap developed by an artificial startup. Task 1 is assumed to take the whole Janduary, while Task 2 is starting from March and ending in mid April. Afterwards, Task 3 begins and ends in the end of September. Recreate a similar Roadmap")],className='three columns'),
				html.Div([dcc.Graph(id='figure_5', figure=figure_5)],className='eight columns')],
				className='row')	
	])
	
if __name__=='__main__':
	app.run_server(debug=True)




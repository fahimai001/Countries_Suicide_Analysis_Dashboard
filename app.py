from dash import Dash, dcc, html

from data_analysis import (
    fig_age_suicide,
    fig_country_suicide,
    fig_population_suicide,
    fig_gdp_suicide,
    fig_suicide_trend,
    fig_sex_suicide
)

app = Dash(__name__)

app.layout = html.Div(
    style={'backgroundColor': 'black', 'color': 'white', 'padding': '20px'},
    children=[
        html.H1("Suicide Data Analysis Dashboard", style={'textAlign': 'center'}),

        html.Div(
            children=[
                html.Div(
                    children=[
                        dcc.Graph(figure=fig_age_suicide, style={'height': '300px'}),
                        html.P("Is the suicide rate more prominent in some age categories than others?", 
                               style={'textAlign': 'center', 'marginTop': '10px', 'marginBottom': '20px'})
                    ],
                    style={'width': '48%'}
                ),
                html.Div(
                    children=[
                        dcc.Graph(figure=fig_country_suicide, style={'height': '300px'}),
                        html.P("Which countries have the most and the least number of suicides?", 
                               style={'textAlign': 'center', 'marginTop': '10px', 'marginBottom': '20px'})
                    ],
                    style={'width': '48%'}
                )
            ],
            style={'display': 'flex', 'justifyContent': 'space-between', 'marginBottom': '30px'}
        ),

        html.Div(
            children=[
                html.Div(
                    children=[
                        dcc.Graph(figure=fig_population_suicide, style={'height': '300px'}),
                        html.P("What is the effect of the population on suicide rates?", 
                               style={'textAlign': 'center', 'marginTop': '10px', 'marginBottom': '20px'})
                    ],
                    style={'width': '48%'}
                ),
                html.Div(
                    children=[
                        dcc.Graph(figure=fig_gdp_suicide, style={'height': '300px'}),
                        html.P("What is the effect of the GDP of a country on suicide rates?", 
                               style={'textAlign': 'center', 'marginTop': '10px', 'marginBottom': '20px'})
                    ],
                    style={'width': '48%'}
                )
            ],
            style={'display': 'flex', 'justifyContent': 'space-between', 'marginBottom': '30px'}
        ),

        html.Div(
            children=[
                html.Div(
                    children=[
                        dcc.Graph(figure=fig_suicide_trend, style={'height': '300px'}),
                        html.P("What is the trend of suicide rates across all the years?", 
                               style={'textAlign': 'center', 'marginTop': '10px', 'marginBottom': '20px'})
                    ],
                    style={'width': '48%'}
                ),
                html.Div(
                    children=[
                        dcc.Graph(figure=fig_sex_suicide, style={'height': '300px'}),
                        html.P("Is there a difference between the suicide rates of men and women?", 
                               style={'textAlign': 'center', 'marginTop': '10px', 'marginBottom': '20px'})
                    ],
                    style={'width': '48%'}
                )
            ],
            style={'display': 'flex', 'justifyContent': 'space-between'}
        )
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
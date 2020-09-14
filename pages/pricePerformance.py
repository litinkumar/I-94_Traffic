import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from utils import Header, make_dash_table
import pandas as pd
import pathlib
import plotly.express as px

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../data").resolve()


df_current_prices = pd.read_csv(DATA_PATH.joinpath("df_current_prices.csv"))
df_hist_prices = pd.read_csv(DATA_PATH.joinpath("df_hist_prices.csv"))
df_avg_returns = pd.read_csv(DATA_PATH.joinpath("df_avg_returns.csv"))
df_after_tax = pd.read_csv(DATA_PATH.joinpath("df_after_tax.csv"))
df_recent_returns = pd.read_csv(DATA_PATH.joinpath("df_recent_returns.csv"))
df_graph = pd.read_csv(DATA_PATH.joinpath("df_graph.csv"))

df_traffic_volume = pd.read_csv(DATA_PATH.joinpath("Traffic.csv"))


def create_layout(app):
    return html.Div(
        [
            Header(app),
            # page 2
            html.Div(
                [
                    # Row 3
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H5(
                                        [
                                            "Dataset Snapshot"
                                        ],
                                        className="subtitle padded",
                                    ),
                                    html.Div(
                                        [
                                            html.Table(
                                                make_dash_table(df_traffic_volume.head()),
                                                className="tiny-header",
                                            )
                                        ],
                                        style={"overflow-x": "auto"},
                                    ),
                                ],
                                className="twelve columns",
                            )
                        ],
                        className="row ",
                    ), 

                    # Row 2
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H5("Temperature Variation over time", className="subtitle padded"),
                                    dcc.Graph(
                                        id="graph-4",
                                        figure={
                                            "data": [
                                                go.Scatter(
                                                    x=df_traffic_volume["date_time"],
                                                    y=df_traffic_volume["temp_F"],
                                                    line={"color": "#D44500"},
                                                    mode="lines",
                                                    name="Calibre Index Fund",
                                                ),
                                            ],
                                            "layout": go.Layout(
                                                autosize=True,
                                                width=700,
                                                height=400,
                                                font={"family": "Raleway", "size": 10},
                                                margin={
                                                    "r": 30,
                                                    "t": 30,
                                                    "b": 30,
                                                    "l": 30,
                                                },
                                                xaxis={
                                                    "autorange": True,
                                                    "rangeslider_visible":True,
                                                    "range": [
                                                        "2018-09-01",
                                                        "2018-09-30",
                                                    ],
                                                    "rangeselector": {
                                                        "buttons": [
                                                            {
                                                                "count": 1,
                                                                "label": "1M",
                                                                "step": "month",
                                                                "stepmode": "backward",
                                                            }, 
                                                                                                                   
                                                            {
                                                                "count": 3,
                                                                "label": "3M",
                                                                "step": "month",
                                                                "stepmode": "backward",
                                                            },
                                                            {
                                                                "count": 1,
                                                                "label": "1Y",
                                                                "step": "year",
                                                                "stepmode": "backward",
                                                            },
                                                            {
                                                                "count": 3,
                                                                "label": "3Y",
                                                                "step": "year",
                                                            },
                                                            {
                                                                "label": "All",
                                                                "step": "all",
                                                            },
                                                        ]
                                                    },
                                                    "showline": True,
                                                    "type": "date",
                                                    "zeroline": False,
                                                },
                                                yaxis={
                                                    "autorange": True,
                                                    "range": [
                                                        18.6880162434,
                                                        278.431996757,
                                                    ],
                                                    "showline": True,
                                                    "type": "linear",
                                                    "zeroline": False,
                                                },
                                            ),
                                        },
                                        config={"displayModeBar": False},
                                    ),
                                ],
                                className="twelve columns",
                            )
                        ],
                        className="row ",
                    ),               
                    # Row 2
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H5("Traffic Volume over time", className="subtitle padded"),
                                    dcc.Graph(
                                        id="graph-4",
                                        figure={
                                            "data": [
                                                go.Scatter(
                                                    x=df_traffic_volume["date_time"],
                                                    y=df_traffic_volume["traffic_volume"],
                                                    line={"color": "#D44500"},
                                                    mode="lines",
                                                    name="Calibre Index Fund",
                                                ),
                                            ],
                                            "layout": go.Layout(
                                                autosize=True,
                                                width=700,
                                                height=400,
                                                font={"family": "Raleway", "size": 10},
                                                margin={
                                                    "r": 30,
                                                    "t": 30,
                                                    "b": 30,
                                                    "l": 30,
                                                },
                                                xaxis={
                                                    "autorange": True,
                                                    "rangeslider_visible":True,
                                                    "range": [
                                                        "2018-09-01",
                                                        "2018-09-30",
                                                    ],
                                                    "rangeselector": {
                                                        "buttons": [
                                                            {
                                                                "count": 1,
                                                                "label": "1M",
                                                                "step": "month",
                                                                "stepmode": "backward",
                                                            }, 
                                                                                                                   
                                                            {
                                                                "count": 3,
                                                                "label": "3M",
                                                                "step": "month",
                                                                "stepmode": "backward",
                                                            },
                                                            {
                                                                "count": 1,
                                                                "label": "1Y",
                                                                "step": "year",
                                                                "stepmode": "backward",
                                                            },
                                                            {
                                                                "count": 3,
                                                                "label": "3Y",
                                                                "step": "year",
                                                            },
                                                            {
                                                                "label": "All",
                                                                "step": "all",
                                                            },
                                                        ]
                                                    },
                                                    "showline": True,
                                                    "type": "date",
                                                    "zeroline": False,
                                                },
                                                yaxis={
                                                    "autorange": True,
                                                    "range": [
                                                        18.6880162434,
                                                        278.431996757,
                                                    ],
                                                    "showline": True,
                                                    "type": "linear",
                                                    "zeroline": False,
                                                },
                                            ),
                                        },
                                        config={"displayModeBar": False},
                                    ),
                                ],
                                className="twelve columns",
                            )
                        ],
                        className="row ",
                    ),
                    # Row 3
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H5(
                                        [
                                            "Categorical Variable Analysis"
                                        ],
                                        className="subtitle padded",
                                    ),
                                    html.Div(
                                        [
                                            html.Div(
                                                [
                                                    dcc.Dropdown(
                                                        id="Cat_Dropdown_1",
                                                        options=[
                                                                {'label':'Weather','value':'weather_main'},
                                                                {'label':'Season','value':'Season'}

                                                        ],
                                                        value='weather_main',
                                                        multi=False,
                                                        clearable=False,
                                                        style={"width":"50%"}
                                                    ),   
                                                ],
                                            ),

                                            html.Div(
                                                [
                                                    dcc.Graph(id='Pie_Chart')
                                                ],
                                            ),

                                        ],
                                    ),
                                ],
                                className="twelve columns",
                            )
                        ],
                        className="row ",
                    ),
                ],
                className="sub_page",
            ),
        ],
        className="page",
    )


def update_graph(my_dropdown):
    df_traffic_volume_2=df_traffic_volume

    piechart=px.pie(
            data_frame=df_traffic_volume_2,
            names=my_dropdown,
            hole=0.3
            )
    return (piechart)




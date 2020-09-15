import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

from utils import Header, make_dash_table

import pandas as pd
import pathlib

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../data").resolve()


df_traffic_volume=pd.read_csv(DATA_PATH.joinpath("Traffic.csv"))
KPI=df_traffic_volume.groupby(by='Season').mean().round(2)

KPI

#Temperatur KPIs
Temp_Fall=KPI.iloc[0][6]
Temp_Spring=KPI.iloc[1][6]
Temp_Summer=KPI.iloc[2][6]
Temp_Winter=KPI.iloc[3][6]

#Rain KPIs
Rain_Fall=KPI.iloc[0][2]
Rain_Spring=KPI.iloc[1][2]
Rain_Summer=KPI.iloc[2][2]
Rain_Winter=KPI.iloc[3][2]

#CloudCoverage KPIs
Cloud_Fall=KPI.iloc[0][4]
Cloud_Spring=KPI.iloc[1][4]
Cloud_Summer=KPI.iloc[2][4]
Cloud_Winter=KPI.iloc[3][4]

#TrafficVol KPIs
Traffic_Fall=KPI.iloc[0][5]
Traffic_Spring=KPI.iloc[1][5]
Traffic_Summer=KPI.iloc[2][5]
Traffic_Winter=KPI.iloc[3][5]


def create_layout(app):
    # Page layouts
    return html.Div(
        [
            html.Div([Header(app)]),
            # page 1



            html.Div(
                [
                    # Row 3
                    html.Div(
                        [
                            html.Div(
                               [ 
                                    html.H5(["Project Summary"],className="subtitle padded"),
                                    html.Br([]),
                                    html.P(
                                        "\
                                    In this project we look at the traffic volume on I-94 understand the patterns\
                                    based on which the traffic volume changes day to day. Using the infomation\
                                    of weather attributes such as temperature, rain, cloud coverage etc. We'll\
                                    try to analyze to see if there are any patterns present in the dataset\
                                    based on which we can build an model that can predict the traffic volume\
                                    on I-94 based on the attributes that we provide.",
                                    ),
                                ],
                                className="row",
                            ),
                            ],
                        className="row",
                    ),
                    # Row 4
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.Div(
                                        [
                                            html.H4("Fall Averages"),
                                            html.H5(Temp_Fall),
                                            html.P("Average Temperature(F)"),
                                            html.H5(Rain_Fall),
                                            html.P("Average Rainfall"),
                                            html.H5(Cloud_Fall),
                                            html.P("Cloud Coverage"),
                                            html.H5(Traffic_Fall),
                                            html.P("Traffic Volume")
                                        ],
                                        className="mini_container_fall"
                                    ),
                                ],
                                className="six columns",
                            ),
                            html.Div(
                                [
                                    html.Div(
                                        [
                                            html.H4("Winter Averages"),
                                            html.H5(Temp_Winter),
                                            html.P("Average Temperature(F)"),
                                            html.H5(Rain_Winter),
                                            html.P("Average Rainfall"),
                                            html.H5(Cloud_Winter),
                                            html.P("Cloud Coverage"),
                                            html.H5(Traffic_Winter),
                                            html.P("Traffic Volume")
                                        ],
                                        className="mini_container_winter"
                                    ),                                    
                                ],
                                className="six columns",
                            ),
                        ],
                        className="row",
                        style={"margin-bottom": "35px"},
                    ),
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.Div(
                                        [
                                            html.H4("Spring Averages"),
                                            html.H5(Temp_Spring),
                                            html.P("Average Temperature(F)"),
                                            html.H5(Rain_Spring),
                                            html.P("Average Rainfall"),
                                            html.H5(Cloud_Spring),
                                            html.P("Cloud Coverage"),
                                            html.H5(Traffic_Spring),
                                            html.P("Traffic Volume")
                                        ],
                                        className="mini_container_spring"
                                    ),
                                ],
                                className="six columns",
                            ),
                            html.Div(
                                [
                                    html.Div(
                                        [
                                            html.H4("Summer Averages"),
                                            html.H5(Temp_Summer),
                                            html.P("Average Temperature(F)"),
                                            html.H5(Rain_Summer),
                                            html.P("Average Rainfall"),
                                            html.H5(Cloud_Summer),
                                            html.P("Cloud Coverage"),
                                            html.H5(Traffic_Summer),
                                            html.P("Traffic Volume")
                                        ],
                                        className="mini_container_summer"
                                    ),                                    
                                ],
                                className="six columns",
                            ),
                        ],
                        className="row",
                        style={"margin-bottom": "35px"},
                    ),

                ],
                className="sub_page",
            ),
        ],
        className="page",
    )

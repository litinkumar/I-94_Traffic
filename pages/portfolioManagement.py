import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from sklearn.ensemble import RandomForestRegressor
import joblib
import math

from utils import Header, make_dash_table
import pandas as pd
import pathlib

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../data").resolve()

df_equity_char = pd.read_csv(DATA_PATH.joinpath("df_equity_char.csv"))
df_equity_diver = pd.read_csv(DATA_PATH.joinpath("df_equity_diver.csv"))

df_traffic_volume = pd.read_csv(DATA_PATH.joinpath("Traffic.csv"))

col_names=['temp_F','rain_1h','clouds_all','month']

model=joblib.load('ModelRF.pkl')

df_feature_importances = pd.DataFrame(model.feature_importances_*100,columns=["Importance"],index=col_names)
df_feature_importances = df_feature_importances.sort_values("Importance", ascending=False)

fig_features_importance = go.Figure()
fig_features_importance.add_trace(go.Bar(x=df_feature_importances.index,
                                         y=df_feature_importances["Importance"],
                                         marker_color='rgb(212, 69, 0)')
                                 )

#fig_features_importance.update_layout(title_text='<b>Features Importance of the model<b>', title_x=0.5)
# The command below can be activated in a standard notebook to display the chart
#fig_features_importance.show()

# We record the name, min, mean and max of the three most important features
slider_1_label = df_feature_importances.index[0]
slider_1_min = math.floor(df_traffic_volume[slider_1_label].min())
slider_1_mean = round(df_traffic_volume[slider_1_label].mean())
slider_1_max = round(df_traffic_volume[slider_1_label].max())

slider_2_label = df_feature_importances.index[1]
slider_2_min = math.floor(df_traffic_volume[slider_2_label].min())
slider_2_mean = round(df_traffic_volume[slider_2_label].mean())
slider_2_max = round(df_traffic_volume[slider_2_label].max())

slider_3_label = df_feature_importances.index[2]
slider_3_min = math.floor(df_traffic_volume[slider_3_label].min())
slider_3_mean = round(df_traffic_volume[slider_3_label].mean())
slider_3_max = round(df_traffic_volume[slider_3_label].max())


def create_layout(app):
    return html.Div(
        [
            Header(app),
            # page 3
            html.Div(
                [
                    # Row 1
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H5(["Feature Importance"], className="subtitle padded"),
                                    dcc.Graph(figure=fig_features_importance),

                                ],
                                className="twelve columns",
                            )
                        ],
                        className="rows",
                    ),

                    # Row 4
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H4(children=slider_1_label),

                                    # The Dash Slider is built according to Feature #1 ranges
                                    dcc.Slider(
                                        id='X1_slider',
                                        min=slider_1_min,
                                        max=slider_1_max,
                                        step=25,
                                        value=slider_1_mean,
                                        marks={i: '{}'.format(i) for i in range(slider_1_min, slider_1_max+1,20)}
                                        ),

                                    html.H4(children=slider_2_label),
                                    dcc.Slider(
                                        id='X2_slider',
                                        min=slider_2_min,
                                        max=slider_2_max,
                                        step=25,
                                        value=slider_2_mean,
                                        marks={i: '{}'.format(i) for i in range(slider_2_min, slider_2_max+1)}
                                        ), 

                                    html.H4(children=slider_3_label),
                                    dcc.Slider(
                                        id='X3_slider',
                                        min=slider_3_min,
                                        max=slider_3_max,
                                        step=25,
                                        value=slider_3_mean,
                                        marks={i: '{}'.format(i) for i in range(slider_3_min, slider_3_max+1)}
                                        ),   


                                    html.H2(id="prediction_result"),                                                                        
                                ],
                                className=" twelve columns",
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


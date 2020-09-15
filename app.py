# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import pathlib
import plotly.express as px
import numpy as np
import joblib
import flask

server = flask.Flask(__name__)
app = dash.Dash(__name__,server=server)

from pages import (
    overview,
    EDA,
    prediction,
)

PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../I-94_Traffic/data").resolve()
df_traffic_volume = pd.read_csv(DATA_PATH.joinpath("Traffic.csv"))

app = dash.Dash(
    __name__, meta_tags=[{"name": "viewport", "content": "width=device-width"}]
)
server = app.server

model=joblib.load('ModelRF.pkl')

# Describe the layout/ UI of the app
app.layout = html.Div(
    [dcc.Location(id="url", refresh=False), html.Div(id="page-content")]
)

# Update page
@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def display_page(pathname):
    if pathname == "/Dash_Traffic_App/EDA":
        return EDA.create_layout(app)
    elif pathname == "/Dash_Traffic_App/prediction":
        return prediction.create_layout(app)
    elif pathname == "/Dash_Traffic_App/full-view":
        return (
            overview.create_layout(app),
            EDA.create_layout(app),
            prediction.create_layout(app),
        )
    else:
        return overview.create_layout(app)


app.config['suppress_callback_exceptions'] = True
app.config.suppress_callback_exceptions = True

@app.callback(
    Output(component_id='Pie_Chart', component_property='figure'),
    [Input(component_id='Cat_Dropdown_1',component_property='value')]
)

def update_graph(my_dropdown):
    df_traffic_volume_2=df_traffic_volume

    piechart=px.pie(
            data_frame=df_traffic_volume_2,
            names=my_dropdown,
            hole=0.3
            )
    return (piechart)

@app.callback(Output(component_id="prediction_result",component_property="children"),
# The values correspnding to the three sliders are obtained by calling their id and value property
              [Input("X1_slider","value"), Input("X2_slider","value"), Input("X3_slider","value")])


# The input variable are set in the same order as the callback Inputs
def update_prediction(X1, X2, X3):

    # We create a NumPy array in the form of the original features
    # ["Pressure","Viscosity","Particles_size", "Temperature","Inlet_flow", "Rotating_Speed","pH","Color_density"]
    # Except for the X1, X2 and X3, all other non-influencing parameters are set to their mean
    input_X = np.array([X1,
                       X2,
                       X3,
                       df_traffic_volume["temp_F"].mean()]).reshape(1,-1)        
    
    # Prediction is calculated based on the input_X array
    prediction = model.predict(input_X)[0]
    
    # And retuned to the Output of the callback function
    return "Prediction: {}".format(round(prediction,1))

if __name__ == "__main__":
    app.run_server(debug=True)

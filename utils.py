import dash_html_components as html
import dash_core_components as dcc


def Header(app):
    return html.Div([get_header(app)])


def get_header(app):
    header = html.Div(
        [

            html.Div(
                [
                    html.Div(
                        [html.H5("Traffic Volume Analysis")],
                        className="seven columns main-title",
                    ),
                    html.Div(
                    [
                        dcc.Link(
                            "Overview",
                            href="/Dash_Traffic_App/overview",
                            className="tab first",
                        ),
                        dcc.Link(
                            "Exploratory Data Analysis",
                            href="/Dash_Traffic_App/price-performance",
                            className="tab",
                        ),
                        dcc.Link(
                            "Prediction",
                            href="/Dash_Traffic_App/portfolio-management",
                            className="tab",
                        ),
                    ],
                    className="row all-tabs",
                )
                ],
                className="twelve columns",
                style={"padding-left": "0"},
            ),
        ],
        className="row",
    )

    return header



def make_dash_table(df):
    """ Return a dash definition of an HTML table for a Pandas dataframe """
    table = []
    for index, row in df.iterrows():
        html_row = []
        for i in range(len(row)):
            html_row.append(html.Td([row[i]]))
        table.append(html.Tr(html_row))
    return table

import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import os
import plotly.express as px


# -------------------------- PYTHON FUNCTIONS ---------------------------- #


external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

app = dash.Dash(
    __name__, external_stylesheets=external_stylesheets, assets_folder="assets"
)
server = app.server

app.config.suppress_callback_exceptions = True


# -------------------------- PROJECT DASHBOARD ---------------------------- #

df = pd.DataFrame(
    {
        "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
        "Amount": [4, 1, 2, 2, 4, 5],
        "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"],
    }
)

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

app.layout = html.Div(
    children=[
        html.H1(children="Hello Dash"),
        html.Div(
            children="""
        Dash: A web application framework for Python.
    """
        ),
        dcc.Graph(id="example-graph", figure=fig),
    ]
)


# -------------------------- MAIN ---------------------------- #


if __name__ == "__main__":
    port = os.getenv("PORT", 8000)
    app.run_server(host="0.0.0.0", port=port, debug=True, use_reloader=False)

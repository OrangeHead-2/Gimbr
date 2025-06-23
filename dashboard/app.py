import dash
from dash import dcc, html, dash_table
import plotly.express as px
import pandas as pd

# Load precomputed predictions data
PREDICTION_FILE = "models/evaluation/predictions.csv"

def load_data():
    df = pd.read_csv(PREDICTION_FILE)
    return df

app = dash.Dash(__name__)
server = app.server

df = load_data()

app.layout = html.Div([
    html.H1("Gimbr Infrastructure Failure Risk Dashboard"),
    dcc.Tabs([
        dcc.Tab(label="Map View", children=[
            dcc.Graph(
                id="risk-map",
                figure=px.scatter_mapbox(
                    df,
                    lat="latitude",
                    lon="longitude",
                    color="failure_probability",
                    hover_name="structure_id",
                    mapbox_style="carto-positron",
                    zoom=3,
                    color_continuous_scale="Reds"
                )
            )
        ]),
        dcc.Tab(label="Summary Table", children=[
            dash_table.DataTable(
                id="summary-table",
                columns=[{"name": i, "id": i} for i in df.columns],
                data=df.sort_values("failure_probability", ascending=False).to_dict("records"),
                page_size=20
            )
        ])
    ])
])

if __name__ == "__main__":
    app.run_server(debug=True, host="0.0.0.0", port=8050)
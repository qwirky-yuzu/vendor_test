# Import dash requirements
import dash
from dash import html, dcc, Input, Output, dash_table
import dash_bootstrap_components as dbc

from datetime import datetime

# ===============================#
#                               #
#         INDEX STRING          #
#                               #
# ===============================#
html_index_string = """
<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <title>{%title%}</title>
        {%favicon%}
        {%css%}
    </head>
    <body>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
        <div> </div>
    </body>
</html>
"""

# ===============================#
#                               #
#         HEADER - MAIN         #
#                               #
# ===============================#
header_main = html.Div(
    [
        # COMPANY LOGO
        html.A(
            href="http://localhost:8050/",
            children=[
                html.Img(
                    src="./assets/dsta-edit-logo-cropped.png",
                    style={"height": "8%", "width": "11%", "padding-left": "15px"},
                )
            ]
        ),

        # PROJECT NAME
        html.Div(
            [
                html.Label(
                    "Staff Appraisal Form Topic Modelling",
                    style={
                        "font-weight": "bold",
                        "font-size": "30px",
                        "color": "#0a527f",
                    },
                ),
                html.Br(),
                html.Sup("Data Updated as of: 10 Feb 2023     (Version: Proof of Concept Demo)"),
            ],
            style={"display": "inline-block", "padding-left": "15px"},
        ),
    ],
    style={"padding-top": "15px"},
    className="main-header",
)

main_tab_style = {"display": "inline-block", "width": "95%", "padding": "15px"}

selection_body = html.Div([

    html.Br(),
    # Prompt user to select type of search
    html.H3(
        "Search Mode:",
        style={
            "font-size": "30px",
            "font-weight": "bold",
            "font-family": "Sans-Serif",
            "color": "#252525",
        },
    ),

    dcc.RadioItems(
        id='search_mode',
        options=[
            {'label':'Hashtag Search', 'value':'hts'},
            {'label':'Semantic Search', 'value':'ss'}
        ],
        labelStyle={"display": "inline-block",
                    "verticalAlign": "middle"
                    },
        inputStyle={
            "margin-right": "8px",
            "margin-left": "18px"
            },
    )

],style=main_tab_style)

body_main = html.Div([
    dbc.Row([
        dbc.Col(html.Div(id='hashtag_search_mode'), width=3),
        dbc.Col(width=2),
        dbc.Col(html.Div(id='semantic_search_mode'), width=6)
    ]),
    html.Br(),
    html.H3(
        "Search Parameters:",
        style={
            "font-size": "30px",
            "font-weight": "bold",
            "font-family": "Sans-Serif",
            "color": "#252525",
        },
    ),
    html.Div([
        html.Label(
            'Programme Centre:',
            className="form-label mt-4",
            style={"font-weight": "bold",
                "padding-left": "15px",
                "color":"#0a527f",
                "font-size": "18px"}
        ),

        dcc.Dropdown(
            id='selected-pc',
            options=[
                {"label":"DMSA", "value":"dmsa"},
                {"label":"Air Systems", "value":"airsys"},
                {"label":"Naval Systems", "value":"navalsys"},
                {"label":"Land Systems", "value":"landsys"},
                {"label":"C3D", "value":"c3d"},
                {"label":"Digital Hub", "value":"digitalhub"},
            ],
            placeholder="Select PC",
            style={
                "padding-left":"18px",
                "width": "42%",
                "display": "inline-block",
                "verticalAlign": "middle",
            },
            className="select-box",
            value=61010107
        ),
    ]),
    html.Div([
        html.Label(
            'Appointment Type:',
            className="form-label mt-4",
            style={"font-weight": "bold",
                "padding-left": "15px",
                "color":"#0a527f",
                "font-size": "18px"}
        ),

        dcc.Dropdown(
            id='selected-appointment',
            options=[
                {"label":"Engineer", "value":"engineer"},
                {"label":"Senior Engineer", "value":"senior_engineer"},
                {"label":"Principal Engineer", "value":"principal_engineer"},
                {"label":"Senior Principal Engineer", "value":"senior_principal_engineer"},
                {"label":"Programme Manager", "value":"programme_manager"},
                {"label":"Senior Programme Manager", "value":"senior_programme_manager"},
            ],
            placeholder="Select appointment",
            style={
                "padding-left":"18px",
                "width": "42%",
                "display": "inline-block",
                "verticalAlign": "middle",
            },
            className="select-box",
            value=61010107
        ),

    ]),
    html.Label(
        " *Non selection of appointment will result in general search across ALL appointments",
        style={
            "font-style": "italic",
            "margin-left": "10px",
            "padding-right": "15px",
            "font-size": "10px"}
    ),
    html.Div([
        html.Label(
            'Retrieval Year Range:',
            className="form-label mt-4",
            style={"font-weight": "bold",
                    "padding-left": "15px",
                    "color":"#0a527f",
                    "font-size": "18px"}
        ),
        dcc.DatePickerRange(
            id="retrival_selected_date",
            start_date=datetime(2017,1,1),
            end_date=datetime.today(),
            display_format="Y",
            style={
                "padding-left":"18px",
                "width": "25%",
                "display": "inline-block",
                "verticalAlign": "middle",
            },
        ),
    ]),
    html.Div([
        html.Label(
            'Years In Service:',
            className="form-label mt-4",
            style={"font-weight": "bold",
                    "padding-left": "15px",
                    "color":"#0a527f",
                    "font-size": "18px"}
        ),
        html.Div([
            dbc.Row([
                dbc.Col(dbc.Input(id='yis_min', placeholder='Enter YIS min', size='sm', type="number",min=0, max=50, step=0.1), width=4),
                dbc.Col("to", width=1),
                dbc.Col(dbc.Input(id='yis_max', placeholder='Enter YIS max', size='sm', type="number",min=0, max=50, step=0.1),width=4)
            ])
        ],style={
            "padding-left": "15px",
            "display": "inline-block",
            "verticalAlign": "middle",}
        )
    ]),
    html.Div([
        html.Label(
            'Years In Appointment:',
            className="form-label mt-4",
            style={"font-weight": "bold",
                    "padding-left": "15px",
                    "color":"#0a527f",
                    "font-size": "18px"}
        ),
        html.Div([
            dbc.Row([
                dbc.Col(dbc.Input(id='yia_min', placeholder='Enter YIA min', size='sm', type="number",min=0, max=50, step=0.1), width=4),
                dbc.Col("to", width=1),
                dbc.Col(dbc.Input(id='yia_max', placeholder='Enter YIA max', size='sm', type="number",min=0, max=50, step=0.1),width=4)
            ])
        ],style={
            "padding-left": "15px",
            "display": "inline-block",
            "verticalAlign": "middle",}
        )
    ])



],style=main_tab_style)


app = dash.Dash()

@app.callback(
    Output('hashtag_search_mode', 'children'),
    [
        Input('search_mode', 'value')

    ]
)
def hashtag_search(search_mode):
    if search_mode is not None:
        disable_search = False if search_mode =='hts' else True
        c = [
            html.H3(
                "Search By Hashtags (#):",
                style={
                    "font-size": "18px",
                    "font-weight": "bold",
                    "font-family": "Sans-Serif",
                    "color": "#0a527f",
                },
            ),
            dcc.Dropdown(
                id="searched_hashtags",
                options=[
                    {'label':'Data', 'value':'data'},
                    {'label':'Data science', 'value':'data_science'},
                    {'label':'Project management', 'value':'project_management'}
                ],
                placeholder="Search hashtags",
                style={"font-size": "14px"},
                className="select-box",
                multi=True,
                disabled=disable_search
            ),
            dbc.Button("Search", id='hashtag_search_trigger', size='sm', color='success', className="me-1", disabled=disable_search),
            dbc.Row([
                    html.Div([
                        dbc.Button("#data", id='suggested_hashtag_1', size='sm', color="dark", className="me-1"),
                        dbc.Button("#data science", id='suggested_hashtag_2', size='sm', color="dark", className="me-1", style={'margin-left':'10px'}),
                        dbc.Button("# AI", id='suggested_hashtag_3', size='sm', color="dark", className="me-1", style={'margin-left':'10px'})
                    ], className='mx-auto', style={'verticalAlgin':'middle'})
            ]),
            dbc.Row([
                dbc.Col(width=1),
                html.Div([
                    dbc.Button("#project management", id='suggested_hashtag_4', size='sm', color="dark", className="me-1"),
                    dbc.Button("#procurement", id='suggested_hashtag_5', size='sm', color="dark", className="me-1", style={'margin-left':'10px'})
                ], className='mx-auto', style={'verticalAlgin':'middle'}),
            ]),
        ]
        return c

@app.callback(
    Output('semantic_search_mode', 'children'),
    [
        Input('search_mode', 'value')

    ]
)
def semantic_search(search_mode):
    if search_mode is not None:
        disable_search = False if search_mode =='ss' else True
        c = [
            html.H3(
                "Semantic Search Query:",
                style={
                    "font-size": "18px",
                    "font-weight": "bold",
                    "font-family": "Sans-Serif",
                    "color": "#0a527f",
                },
            ),
            dbc.Input(id='semantic_search_query', placeholder=f"{'Activate semantic search option...' if disable_search else 'Type something...'}", type="text", disabled=disable_search),
            dbc.Button("Search", id='semantic_search_trigger', size='sm', color='success', className="me-1", disabled=disable_search),
        ]

        return c

app.layout = html.Div([header_main,
                       selection_body,
                       body_main
                       ])

if __name__ == '__main__':
    app.run_server(host="0.0.0.0", port="8050")

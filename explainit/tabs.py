# Copyright 2022 The Explainit Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY aIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from dash import dcc
from dash import html


def build_tabs():
    """
    Generates the main application tabs.
    """
    return html.Div(
        id="tabs",
        className="tabs",
        children=[
            dcc.Tabs(
                id="app-tabs",
                value="tab1",
                className="custom-tabs",
                children=[
                    dcc.Tab(
                        id="Data-drift-tab",
                        label="Data Drift",
                        value="tab1",
                        className="custom-tab",
                        selected_className="custom-tab--selected",
                    ),
                    dcc.Tab(
                        id="Target-drift-tab",
                        label="Target Drift",
                        value="tab2",
                        className="custom-tab",
                        selected_className="custom-tab--selected",
                    ),
                    dcc.Tab(
                        id="Model-drift-tab",
                        label="Data Quality",
                        value="tab3",
                        className="custom-tab",
                        selected_className="custom-tab--selected",
                    ),
                ],
            )
        ],
    )


def data_quality_tabs():
    """
    Generates the Data quality tabs.
    """
    return html.Div(
        id="data-quality-tabs",
        className="tabs",
        children=[
            html.Hr(),
            dcc.Tabs(
                id="quality-tabs",
                value="quality-tab1",
                className="custom-tabs",
                children=[
                    dcc.Tab(
                        id="Data-summary-tab",
                        label="Data Summary",
                        value="quality-tab1",
                        className="custom-tab",
                        selected_className="custom-tab--selected",
                    ),
                    dcc.Tab(
                        id="Feature-summary-tab",
                        label="Feature Summary",
                        value="quality-tab2",
                        className="custom-tab",
                        selected_className="custom-tab--selected",
                    ),
                    dcc.Tab(
                        id="Correlation-tab",
                        label="Correlations",
                        value="quality-tab3",
                        className="custom-tab",
                        selected_className="custom-tab--selected",
                    ),
                ],
            ),
        ],
    )

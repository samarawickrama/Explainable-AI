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
from typing import Tuple

import numpy as np
import pandas as pd
from scipy.stats import norm


def proportions_diff_z_stat_ind(ref: pd.DataFrame, prod: pd.DataFrame):
    # pylint: disable=invalid-name
    n1 = len(ref)
    n2 = len(prod)

    p1 = float(sum(ref)) / n1
    p2 = float(sum(prod)) / n2
    P = float(p1 * n1 + p2 * n2) / (n1 + n2)

    return (p1 - p2) / np.sqrt(P * (1 - P) * (1.0 / n1 + 1.0 / n2))


def proportions_diff_z_test(z_stat, alternative="two-sided"):
    if alternative == "two-sided":
        return 2 * (1 - norm.cdf(np.abs(z_stat)))

    if alternative == "less":
        return norm.cdf(z_stat)

    if alternative == "greater":
        return 1 - norm.cdf(z_stat)

    raise ValueError(
        "alternative not recognized\n" "should be 'two-sided', 'less' or 'greater'"
    )


def z_stat_test(
    reference_data: pd.Series, production_data: pd.Series, threshold: float
) -> Tuple[float, bool, float]:
    #  TODO: simplify ignoring NaN values here, in chi_stat_test and data_drift_analyzer
    if (
        reference_data.nunique() == 1
        and production_data.nunique() == 1
        and reference_data.unique()[0] == production_data.unique()[0]
    ):
        p_value = 1
    else:
        keys = set(list(reference_data.unique()) + list(production_data.unique())) - {
            np.nan
        }
        ordered_keys = sorted(list(keys))
        p_value = proportions_diff_z_test(
            proportions_diff_z_stat_ind(
                reference_data.apply(
                    lambda x, key=ordered_keys[0]: 0 if x == key else 1
                ),
                production_data.apply(
                    lambda x, key=ordered_keys[0]: 0 if x == key else 1
                ),
            )
        )
    return p_value, p_value <= threshold, threshold

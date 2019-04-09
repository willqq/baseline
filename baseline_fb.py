#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:qiuzhipeng
# time:2019/4/4 14:07

import warnings
warnings.filterwarnings('ignore')

import numpy as np
import pandas as pd
from scipy import stats
import statsmodels.api as sm
import datetime
import matplotlib.pyplot as plt
from fbprophet import Prophet
from tslearn.utils import to_time_series_dataset
X = to_time_series_dataset([[1, 2, 3, 4], [1, 2, 3], [2, 5, 6, 7, 8, 9]])

from tslearn.generators import random_walks
from tslearn.preprocessing import TimeSeriesScalerMeanVariance
from tslearn import metrics

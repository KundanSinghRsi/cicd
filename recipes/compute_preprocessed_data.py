# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
home_insurance_1_distinct = dataiku.Dataset("home_insurance_1_distinct")
home_insurance_1_distinct_df = home_insurance_1_distinct.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.







preprocessed_data_df = home_insurance_1_distinct_df # For this sample code, simply copy input to output


# Write recipe outputs
preprocessed_data = dataiku.Dataset("preprocessed_data")
preprocessed_data.write_with_schema(preprocessed_data_df)

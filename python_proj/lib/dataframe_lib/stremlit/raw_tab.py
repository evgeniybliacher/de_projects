from typing import Any

import streamlit as st
import pandas as pd
from returns.result import Success,Failure
from dataframe_lib.pandas.ingest import load_dataset
from dataframe_lib.stremlit.common import dataset_info

def show_raw_tab():
    uploaded_file = st.file_uploader(
        "Select a dataset",
        type=["csv", "parquet"],
    )
    if uploaded_file is not None:
        df = load_dataset("chess","csv")
        match df:
            case Success(df):
                df = df
            case Failure(error):
                raise error
        df["empty_column"] = pd.NA
        st.session_state.had_file = True
        st.success("Dataset loaded")
        dataset_info(df)
        st.session_state.raw_df = df
    elif st.session_state.had_file:
         dataset_info(st.session_state.raw_df)
    else:
         st.session_state.had_file = False
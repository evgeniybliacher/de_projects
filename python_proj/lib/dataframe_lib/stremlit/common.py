import streamlit as st
from dataframe_lib.pandas.common import overview, get_dataframe


def overview_part (st, df: pd.DataFrame) -> st:
    st = st.header("Overview")
    data = overview(df)
    col1, col2, col3 = st.columns(3)
    col1.metric("Number of rows", data[0])
    col2.metric("Number of columns", data[1])
    col3.metric("Memory size", data[2])

def dataset_info(df: pd.DataFrame) -> Any:
        st.header("Data info")
        overview_part(st, df)
        st.dataframe(get_dataframe(df,10))
        st.session_state.raw_df = df
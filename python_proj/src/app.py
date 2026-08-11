import streamlit as st
from dataframe_lib.stremlit.raw_tab import show_raw_tab


#st.session_state.raw_df = None
if "stage" not in st.session_state:
    st.session_state.stage = "Raw"

st.session_state.had_file = False

st.set_page_config(
    page_title="Python Mid-Project",
    layout="wide",
)
stage = st.segmented_control(
    "Pipeline",
    ["Raw"],
    selection_mode="single",
    default="Raw",
    width="stretch"
)

match stage:
    case "Raw":
        show_raw_tab()
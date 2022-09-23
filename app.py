import streamlit as st
import pandas as pd
from st_aggrid import AgGrid
from st_aggrid.grid_options_builder import GridOptionsBuilder

# 데이터 읽기
@st.cache
def data_upload():
  df = pd.read_csv("포항_아파트_실거래가_현황.csv")
  return df

df = data_upload()
st.dataframe(df)
# gd = GridOptionsBuilder.from_dataframe(df)
# gd.configure_pagination(enabled=True)
# gd.configure_default_column(editable=True, groupable=True)

# sel_mode = st.radio('Selection Type', options=['single', 'multiple'])
# gd.configure_selection(selection_mode=sel_mode, use_checkbox=True)
# grid_options = gd.build()
# st.header("포항 주요아파트 실거래가 현황")
# AgGrid(df, gridOptions=grid_options) 
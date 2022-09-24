import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import json
import requests
import pandas as pd
import plotly.express as px
import streamlit as st

from streamlit_lottie import st_lottie
from app import load_lottiefile
from app import load_lottieurl


# Lottie Animation!!!
# GitHub: https://github.com/andfanilo/streamlit-Lottie
# Lottie Files: https://Lottiefiles.com/

# def load_lottiefile(filepath: str):
#     with open(filepath, 'r') as f:
#         return json.load(f)
    
# def load_lottieurl(url: str):
#     r = requests.get(url)
#     if r.status_code !=200:
#         return None
#     return r.json()

# Use Local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
        
local_css("css/style.css")


# 데이터 읽기
@st.cache
def data_upload():
  df = pd.read_csv("포항_아파트_분양권_현황.csv")
  return df

df = data_upload()

# ----- 단지 선택 -----
단지명 = st.sidebar.selectbox(
    "단지명 선택",
    options = df["단지명"].unique()
)

df_selection = df.query(
    "단지명 == @단지명"
)

# ----- 선택한 단지 엑셀로 저장 -----
df_selection.to_csv(
    "right_transaction_price.csv",
    sep = ",",
    na_rep = 'NaN',
    float_format = '%.2f',
    index = False
)

df = pd.read_csv("right_transaction_price.csv")


# ----- 전용면적 별로 정렬하기 -----
전용면적 = st.sidebar.selectbox(
    "전용면적 선택",
    options = df["전용면적"].unique()
)

df_selection = df.query(
    "전용면적 == @전용면적"
)


lottie_title = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_yg3asqro.json")

# ----- MAINPAGE -----
with st.container():
    left_column, right_column = st.columns((1,6))
    with left_column:
        st_lottie(lottie_title, width=100, height=100, key="title")
    with right_column:
        st.title("포항 주요 아파트 분양권 현황")

st.markdown(":star2: 본 사이트는 \"국토교통부 실거래가 공개시스템\"을 기초로 작성되었음을 알려드립니다.")


# ----- 최고가 최저가 보여주기 -----
low_price = df_selection["거래금액(만원)"].min()
high_price = df_selection["거래금액(만원)"].max()
danji = df["단지명"].unique()

with st.container(): 
    col1, col2 = st.columns((1,4))

    col1.markdown(" ### :house: 단지명 : ")
    col2.subheader(f"{danji}")
    
with st.container(): 
    col1, col2, col3 = st.columns((2,1,1))

    col1.markdown(" ### :high_brightness: 최고금액")
    col1.subheader(f": {high_price}만원")
    col2.empty()
    col3.markdown(" ### :low_brightness: 최저금액")
    col3.subheader(f": {low_price}만원")


# ----- 차트 그리기 -----
contract_date = df_selection["계약일"]
contract_price = df_selection["거래금액(만원)"]


fig = px.line(
    df_selection,
    x = contract_date,
    y = contract_price,
    # title = '< 거래일자 별 실거래금액 추이 >',  # 그래프 타이틀 지정
    text = contract_price,
    markers = True,
)

fig.update_layout(
    # width = 850,
    # height = 550,
    paper_bgcolor = "#0083B8",
    plot_bgcolor = "rgb(223, 100, 200)",
    xaxis=dict(showgrid=False),
    yaxis=dict(showgrid=False),
    title_font_size = 28,
    # font_color = "black",
    font_size = 14,
)

fig.update_traces(
    line=dict(width=3)
)

fig.update_xaxes(title_font_family="Arial")



# lottie_hello = load_lottiefile("malthael.json")
# st_lottie(
#     lottie_hello,
#     speed = 1,
#     reverse = False,
#     loop = True,
#     quality = "low",
#     # renderer = "svg",
#     height = 300,
#     width = 400,
#     key = None,
# )


lottie_file = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_ABViugg18Y.json")


with st.container():
    st.markdown("---")
    st.markdown("### :chart_with_upwards_trend: 거래 일자 별 실거래가 추이")
    left_column, right_column = st.columns(2)
    with left_column:
        st.plotly_chart(fig)
    with right_column:
        st.empty()
        
with st.container():
    st.markdown("---")
    st.markdown("### :file_folder: 선택한 데이터 상세")
    left_column, right_column = st.columns((1, 1))
    with left_column:
        st_lottie(lottie_file, height = 250, key = "file")
    with right_column:
        st.markdown("#")
        st.dataframe(df_selection, width = 750)
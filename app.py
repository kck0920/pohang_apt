import json

import requests
import pandas as pd
import plotly.express as px
import streamlit as st
from streamlit_lottie import st_lottie


# emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title = "포항 아파트 실거래가 현황",
                page_icon = ":chart_with_upwards_trend:",
                layout = "wide",
)

# Lottie Animation!!!
# GitHub: https://github.com/andfanilo/streamlit-Lottie
# Lottie Files: https://Lottiefiles.com/

def load_lottiefile(filepath: str):
    with open(filepath, 'r') as f:
        return json.load(f)
    
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()

# Use Local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
        
local_css("css/style.css")

# # hidden hamburger menu
# hide_menu_style = """
#         <style>
#         #MainMenu {visibility: hidden;}
#         footer {visibility: hidden;}
#         header {visibility: hidden;}        
#         </style>
#         """
# st.markdown(hide_menu_style, unsafe_allow_html=True)

# 데이터 읽기
@st.cache
def data_upload():
  df = pd.read_csv("포항_아파트_실거래가_현황.csv")
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
    "real_transaction_price.csv",
    sep = ",",
    na_rep = 'NaN',
    float_format = '%.2f',
    index = False
)

df = pd.read_csv("real_transaction_price.csv")


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
    left_column, right_column = st.columns((1,7))
    with left_column:
        st_lottie(lottie_title, width=80, height=80, key="title")
    with right_column:
        st.title("2022년 포항 주요 아파트 실거래 현황")

st.markdown(":star2: 이 사이트는 \"국토교통부 실거래가 공개시스템\"을 기초로 작성되었음을 알려드립니다.")


# ----- 최고가 최저가 보여주기 -----
low_price = df_selection["거래금액(만원)"].min()
high_price = df_selection["거래금액(만원)"].max()
danji = df["단지명"].unique()

with st.container(): 
    col1, col2, col3, col4 = st.columns([1,1,1,1])

    col1.markdown(" ### :house: 단지명")
    col1.subheader(f": {danji}")
    col2.markdown(" ### :high_brightness: 최고금액")
    col2.subheader(f": {high_price}만원")
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
    width = 850,
    height = 550,
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


lottie_coding = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_0jQBogOQOn.json")
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
        st_lottie(lottie_file, height = 400, key = "file")
    with right_column:
        st.markdown("#")
        st.dataframe(df_selection, width = 750)
        
# ----- CONTACT -----
with st.container():
    st.write("---")
    st.markdown("### :mailbox: 문의사항은 저에게...")
    st.write("##")
    
    # documention: http://formsubmit.co/ !! CHANGE EMAIL ADDRESS!!!
    contact_form = """
        <form action="https://formsubmit.co/kck0920@gmail.com" method="POST">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder ="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
        </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.write(":email: 확인하면 바로 연락드릴게요!")
        st.markdown("#")
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st_lottie(lottie_coding, height = 400, key="coding")
import streamlit as st
import pandas as pd
import plotly_express as px


# emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title = "포항 아파트 실거래가 현황",
                   page_icon = ":chart_with_upwards_trend:",
                   layout = "wide",
)

# 데이터 읽기
@st.cache
def data_upload():
  df = pd.read_csv("포항_아파트_실거래가_현황.csv")
  return df

df = data_upload()
st.dataframe(df)

# ----- 단지 선택 -----
단지명 = st.sidebar.selectbox(
    "단지명 선택",
    options = df["단지명"].unique()
)

df_selection = df.query(
    "단지명 == @단지명"
)

# ----- MAINPAGE -----
st.title(":chart_with_upwards_trend: 2022년 포항 주요 아파트 실거래 현황")
st.markdown("#")


# ----- 최고가 저저가 보여주기 -----
low_price = df_selection["거래금액(만원)"].min()
high_price = df_selection["거래금액(만원)"].max()
danji = df["단지명"].unique()

left_column, middle_column, right_column = st.columns(3)
with left_column:
    st.subheader("단지명:")
    st.subheader(f"{danji}")
with middle_column:
    st.subheader("최저금액:")
    st.subheader(f"{low_price}만원")
with right_column:
    st.subheader("최고금액:")
    st.subheader(f"{high_price}만원")

st.markdown("---")

# ----- 차트 그리기 -----
contract_date = df_selection["계약일"]
contract_price = df_selection["거래금액(만원)"]


fig = px.line(
    df_selection,
    x = contract_date,
    y = contract_price,
    title = '< 거래일자 별 실거래금액 추이 >',  # 그래프 타이틀 지정
    text = contract_price,
    markers = True,
)

fig.update_layout(
    width = 900,
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

st.plotly_chart(fig)
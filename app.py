import json

import requests
import streamlit as st
from streamlit_lottie import st_lottie


# emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title = "포항 아파트 실거래가 현황",
                page_icon = ":chart_with_upwards_trend:",
                layout = "centered",
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

lottie_title = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_yg3asqro.json")

with st.container():
    left_column, right_column = st.columns((1,6))
    with left_column:
        st_lottie(lottie_title, width=100, height=100, key="title")
    with right_column:
        st.title("포항 아파트 실거래 / 분양권 현황")
st.markdown("""
            ### :white_check_mark: 2022년 국토교통부 실거래가 공개시스템의 데이타를 기초로 작성 되었음을 알려드립니다.
            ### :clock9: 특별한 사유가 없는 한 매주 토요일에 한번씩 업데이트 할 예정입니다. 
            """)
st.markdown("""
            ### :arrow_left: 좌측 메뉴를 이용하세요.
            """)
st.markdown("""
            ### :computer: 현 사이트는 PC와 태블릿에 최적화 되어 있습니다.
            ### :mobile_phone_off: 모바일을 이용하시려면 가로로 이용하세요.
            ### :date: 최종 업데이트: 2023년 2월 11일 
            """)

load_access= load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_0jQBogOQOn.json")
st_lottie(load_access, width=700, key="access")
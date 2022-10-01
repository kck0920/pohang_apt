import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import json
from app import load_lottiefile
from app import load_lottieurl

import requests
import streamlit as st
from streamlit_lottie import st_lottie


lottie_email = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_1gekp2md.json")

# Use Local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
        
local_css("css/style.css")

# ----- CONTACT -----
with st.container():
    st.write("---")
    st.markdown("### :mailbox: 문의사항은 저에게...")
    st.write("##")
    
    # documention: http://formsubmit.co/ !! CHANGE EMAIL ADDRESS!!!
    contact_form = """
        <form action="https://formsubmit.co/kck0920@gmail.com" method="POST">
        <input type="text" name="name" placeholder="당신의 이름은?" required>
        <input type="email" name="email" placeholder ="당신의 이메일" required>
        <textarea name="message" placeholder="여기에 메지를 입력해주세요." required></textarea>
        <button type="submit">Send</button>
        </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.write(":email: 확인하면 바로 연락드릴게요!")
        st.markdown("#")
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st_lottie(lottie_email, height = 400, key="coding")
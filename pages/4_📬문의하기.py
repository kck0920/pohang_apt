import json

import requests
import streamlit as st
from streamlit_lottie import st_lottie


def load_lottiefile(filepath: str):
    with open(filepath, 'r') as f:
        return json.load(f)
    
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()

lottie_coding = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_0jQBogOQOn.json")
lottie_file = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_ABViugg18Y.json")

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
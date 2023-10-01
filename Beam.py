import streamlit as st
import numpy as np
import pandas as pd
import Radio_Style, Beam_Sidebar, Beam_Calculate, Beam_Result
from Beam_Sidebar import In

import os
os.system('cls')  # 터미널 창 청소, clear screen

### * -- Set page config
# emoji: https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/
# https://zzsza.github.io/mlops/2021/02/07/python-streamlit-dashboard/  유용한 사이트
st.set_page_config(page_title = "Beam Design (FRP vs. Rebar)", page_icon = "beam_icon.png", layout = "centered",    # centered, wide
                    initial_sidebar_state="expanded",
                    # runOnSave = True,
                    menu_items = {        #   initial_sidebar_state="auto",  # Can be "auto", "expanded", "collapsed"
                        # 'Get Help': 'https://www.extremelycoolapp.com/help',
                        # 'Report a bug': "https://www.extremelycoolapp.com/bug",
                        # 'About': "# This is a header. This is an *extremely* cool app!"
                    })
### * -- Set page config

# 메인바 윗쪽 여백 줄이기 & 텍스트, 숫자 상자 스타일,  # Adding custom style with font
css = f""" <style>
    .block-container {{
        margin-top: 20px;
        padding-top: 0px;
        max-width: {In.max_width}px !important;
    }}
    .element-container {{
            white-space: nowrap;            
            overflow-x: visible;            
            }}
    input[type="text"] {{
        padding: 6px;
        padding-left: 15px;
        background-color: {In.background_color};
        font-size: {In.font_h5};
        font-weight: bold !important;
        border: 1px solid black !important;
        border-radius: 100px;
    }}
    
    input[type="number"] {{
        padding: 5px;
        padding-left: 15px;
        # color: blue;
        background-color: {In.background_color};
        font-size: {In.font_h5};
        font-weight: bold !important;
        border: 1px solid black !important;
        border-radius: 100px;
        # width: 100%
    }}
    # input[type="number"]::-ms-clear {{
    #     display: none; /* 숫자 입력창 오른쪽에 있는 지우기(x) 버튼을 숨깁니다 */
    # }}
    [data-testid=stSidebar] {{
        background-color: whitesmoke !important;
        /* border: 3px dashed lightblue !important; */
        font-weight: bold !important;        
        padding: 5px !important;
        margin-top: -100px !important;        
        padding-bottom: 100px !important;
        height: 110% !important;
        max-width: 500px !important;  /* 사이드바의 최대 크기를 조절합니다 */
        width: 100% !important;  /* 이렇게 하면 사이드 바 폭을 고정할수 있음. */
    }}
        /* CSS to set font for everything except code blocks */
        body, h1, h2, h3, h4, h5, h6, p, blockquote {{
            font-family: 'Nanum Gothic', sans-serif; font-weight: bold !important; font-size: 16px !important;}}

        /* Font size for titles (h1 to h6) */
        h1 {{font-size: {In.font_h1} !important;}}
        h2 {{font-size: {In.font_h2} !important;}}
        h3 {{font-size: {In.font_h3} !important;}}
        h4 {{font-size: {In.font_h4} !important;}}
        h5 {{font-size: {In.font_h5} !important;}}
        h6 {{font-size: {In.font_h6} !important;}}
</style> """
st.markdown(css, unsafe_allow_html=True)

# 모든 글씨 및 라텍스 수식 진하게 설정
st.markdown('''
<style>
    .main * {
        # font-size: 26pt !important;
        font-weight: bold !important;
        # font-family: Arial !important;            
    }
    # .mjx-chtml {
    #     font-size: 36pt !important;
    # }
</style>
''', unsafe_allow_html=True)

h2 = '## ';  h3 = '### ';  h4 = '#### ';  h5 = '##### ';  h6 = '###### '
s1 = h5 + '$\quad$';  s2 = h5 + '$\qquad$';  s3 = h5 + '$\quad \qquad$'  #s12 = '$\enspace$'  공백 : \,\:\;  # ⁰¹²³⁴⁵⁶⁷⁸⁹  ₀₁₂₃₄₅₆₇₈₉

Radio_Style.radio(In.background_color, '32%')
st.sidebar.write(h2, ':blue[[Information : 입력값 📘]]')

In = Beam_Sidebar.Sidebar(h4, h5)

R = Beam_Calculate.RC(In)
F = Beam_Calculate.FRP(In)

# def ex():
#     st.session_state.Type = 'Singly Reinforced'    
# for v in st.session_state.items():
#     v
# st.button('KCI Rectangle', help = '철근콘크리트 공학(민창식, 예제 9.6~9.7) [교재에서 압축철근을 c가 아닌 a로 판단하여 오차 발생]', on_click = ex)

# In, R, F
Beam_Result.Fig(In, R, F)
[col1, col2] = st.columns([1200, 500])
with col1:
    Beam_Result.Table(In, R, F)
with col2:
    st.write('## :blue[[✤ Examples (Singly Reinforced)]]')
    st.write('#### 작성중...')
    st.button('작성중...', use_container_width = False)
    st.write('## :green[[✤ Examples (Doubly Reinforced)]]')

def set_button_style(background_color, text_color, border_color, border_width, width, height, font_size):
    button_style = f""" <style>
        .stButton > button {{
            background-color: {background_color};
            color: {text_color};
            border-color: {border_color};
            border-width: {border_width}px;
            width: {width}px;
            # height: {height}px;
            # font-size: {font_size}px;
            # text-align: right;
        }}
    </style> """
    st.markdown(button_style, unsafe_allow_html=True)

set_button_style('lightblue', 'black', 'blue', 3, 200, 50, 30)  



# Set the button color to red,
# the text color to white,
# the border color to blue and the border width to 3 pixels,
# and the width and height of the button.
# Set font size to 20 pixels and align text in center.

import streamlit as st
import streamlit.components.v1 as components

# Write some simple HTML code
html_code = """
    <div style="background-color: lightblue; padding: 10px;">
        <h1>Hello, Streamlit!</h1>
        <p>This is a simple example of inserting HTML code into a Streamlit app.</p>
    </div>
"""

# Use the 'components.html' function to insert the HTML code
components.html(html_code)

import streamlit as st
import streamlit.components.v1 as components

# Define the URL of the external webpage
url = "https://www.weather.go.kr/w/index.do"

# Use the 'components.html' function and pass in the iframe HTML code
components.html(f'<iframe src="{url}" width="100%" height="1200px" style="border:none;"></iframe>', height=1200)


from reportlab.pdfgen import canvas

c = canvas.Canvas("hello.pdf")
c.drawString(100, 750, r"$\alpha$Hello assdddddddddddddatt World")
c.save()

import pyautogui

# Capture a specific region (top-left corner of the second monitor)
screenshot = pyautogui.screenshot(region=(3840, 0, 3840, 2160))

# Save the image
screenshot.save("screenshot.png")


from PIL import Image
from mss import mss

# Create an MSS instance 
sct = mss() 

# Take a screenshot of the entire screen (or all screens)
screenshot = sct.grab(sct.monitors[2])  # Change index according to your monitor

# Convert the screenshot to an image (RGB format)
img = Image.frombytes("RGB", screenshot.size, screenshot.bgra, "raw", "BGRX")

# Save the image
img.save('screenshot2.png')






import streamlit as st
import numpy as np
import pandas as pd
import Radio_Style, Beam_Sidebar, Beam_Calculate, Beam_Result
from Beam_Sidebar import In
import Beam_Examples as ex

import os
os.system('cls')  # 터미널 창 청소, clear screen
# pip freeze > requirements.txt

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


# 스트림릿 앱의 전체 배경색을 흰색으로 설정
st.markdown(
    """
    <style>
        body {
            background-color: #ffffff;  /* 흰색 배경색으로 변경 */
        }
    </style>
    """,
    unsafe_allow_html=True
)

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

# In, R, F
Beam_Result.Fig(In, R, F)
[col1, col2] = st.columns([1200, 500])
with col1:
    Beam_Result.Table(In, R, F)
with col2:
    import plotly.graph_objects as go
    st.write('## :purple[⚖️ [Rebar 🆚 FRP]]')    
    x = ['Rebar', 'FRP']
    fig = go.Figure(data = [
        go.Bar(x = x, y = [R.Mn, F.Mn], name = 'M<sub>n</sub>', marker_color='lightskyblue', marker_line_color='black', marker_line_width=2,
            text='M<sub>n</sub>', textfont_size=20, textposition='inside'),
        go.Bar(x = x, y = [R.Md, F.Md], name = 'ϕM<sub>n</sub>', marker_color='orange', marker_line_color='black', marker_line_width=2,
            text='ϕM<sub>n</sub>', textfont_size=20, textposition='inside'),
    ])

    # Update the layout properties
    fig.update_layout(
        autosize=False,
        width=550, height=400,
        margin=dict(l=0, r=12, t=12, b=0),   # 축 외부 박스 mirror하기 위해서, 오른쪽, 위쪽 여백 12 부여함!!!
        # legend = dict(x=1.3, y=1.03, xanchor = 'right', font_size = 20, bordercolor = 'blue', borderwidth = 2),
        barmode = 'group', bargap = 0.3, bargroupgap = 0.15, showlegend=False,
    )
    
    fig.update_xaxes(showline=True, linewidth=2, linecolor='black', mirror=True)
    fig.update_yaxes(showline=True, linewidth=2, linecolor='black', mirror=True, showgrid=True, gridwidth=1, gridcolor='gray')
    fig.update_xaxes(tickfont = dict(size = 20, color = 'purple'))  # font_family = 'Arial'
    fig.update_yaxes(tickfont = dict(size = 20, color = 'black'), range=[0, 1.2*max(R.Mn, F.Mn)])
    fig.update_yaxes(title = dict(text = 'M<sub>n</sub>  or  ϕM<sub>n</sub>  [kN&#8226;m]', font_size = 20, font_color = 'green'))
    
    for i in [1, 2]:
        if i == 1: v1 = R.Mn;  v2 = F.Mn;  x = 0.85;  y = 1.06*F.Mn
        if i == 2: v1 = R.Md;  v2 = F.Md;  x = 1.22;  y = 1.08*F.Md

        value = (v2 - v1)/v1 * 100
        color = 'red' if v2 > v1 else 'blue'
        text = '⬆ 'if v2 > v1 else '⬇ '
        text = text + f'{value:,.1f}' + '%' 
        fig.add_annotation(
            x=x, y=y, text=text,
            font_color=color, font_size=20, font_family='Arial', showarrow=False,
        )

    st.plotly_chart(fig)


    st.write('## :blue[[✤ Examples (Singly Reinforced)]]')
    col = st.columns(2)
    with col[0]:
        st.button('Example 1', on_click = ex.Singly_ex1)
        st.button('Example 3', on_click = ex.Singly_ex3)        
    with col[1]:
        st.button('Example 2', on_click = ex.Singly_ex2)                
        st.button('Example 4', on_click = ex.Singly_ex4)        
    
    st.write('## :green[[✤ Examples (Doubly Reinforced)]]')
    col = st.columns(2)
    with col[0]:
        st.button('Example 5', on_click = ex.Doubly_ex1)
        st.button('Example 7', on_click = ex.Doubly_ex3)
    with col[1]:
        st.button('Example 6', on_click = ex.Doubly_ex2)
        st.button('Example 8', on_click = ex.Doubly_ex4)

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
set_button_style('lightblue', 'black', 'purple', 3, 200, 50, 30)  



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

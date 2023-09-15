import streamlit as st
import numpy as np
import pandas as pd
import style, Sidebar
from Sidebar import In

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
max_width=1800
css = f""" <style>
    .block-container {{
        margin-top: 20px;
        padding-top: 0px;
        max-width: {max_width}px !important;
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

# 왼쪽 사이드바 인쇄하지 않기 설정
st.markdown("""
<style>
@media print {
    [data-testid=stSidebar] {
        display: none;
    }
}
</style>
""", unsafe_allow_html=True)

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

style.radio(In.background_color, '32%')
st.sidebar.write(h2, ':blue[[Information : 입력값 📘]]')

In = Sidebar.Sidebar(h4, h5)



import plotly.graph_objects as go

fig = go.Figure()  # Create a blank figure
max_width = 1800  ########
height = 600

# Add a rectangle shape
fig.add_shape(
    type="rect",
    # xref='x', yref='y',
    x0=0, y0=0, x1=max_width, y1=height,
    line=dict(
        color="RoyalBlue",
        width=3,
    ),
    fillcolor='yellow'
)
fig.add_shape(
    type="circle",
    xref='x', yref='y',
    x0=100, y0=100, x1=200, y1=200,
    line=dict(
        color="RoyalBlue",
        width=2,
    ),
    fillcolor='cyan'
)

# Update the layout properties
# fig.update_layout(
#     autosize=False,
#     width=max_width,
#     height=height,
# )

fig.update_xaxes(range=[0, max_width], autorange=False, scaleanchor='y')
fig.update_yaxes(range=[0, height],  autorange=False)
# fig.update_xaxes(visible=False)
# fig.update_yaxes(visible=False)

st.plotly_chart(fig, use_container_width=True)


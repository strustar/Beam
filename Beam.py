import streamlit as st
import numpy as np
import pandas as pd
import Beam_Sidebar, Beam_Calculate, Beam_Result
from Beam_Sidebar import In
import Beam_Examples as ex

import os, sys, importlib
os.system('cls')  # 터미널 창 청소, clear screen 
sys.path.append( "D:\\Work_Python\\Common")  # 공통 스타일 변수 디렉토리 추가
import commonStyle    # print(sys.path)
importlib.reload(commonStyle) # 다른 폴더 자동 변경이 안됨? ㅠ

### * -- Set page config
st.set_page_config(page_title = "Beam Design (FRP vs. Rebar)", page_icon = "beam.png", layout = "centered",    # centered, wide
                    initial_sidebar_state="expanded",  # runOnSave = True,
                    menu_items = {
                        # 'Get Help': 'https://www.extremelycoolapp.com/help',
                        # 'Report a bug': "https://www.extremelycoolapp.com/bug",
                        # 'About': "# This is a header. This is an *extremely* cool app!"
                    })

In = Beam_Sidebar.Sidebar()
commonStyle.input_box(In)
commonStyle.watermark(In)

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

# ! 날씨 등 참조... (테스트)
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

# Define the URL of the external webpage
url = "https://www.weather.go.kr/w/index.do"

# Use the 'components.html' function and pass in the iframe HTML code
components.html(f'<iframe src="{url}" width="100%" height="1200px" style="border:none;"></iframe>', height=1200)

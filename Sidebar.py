import streamlit as st
# import re
sb = st.sidebar

class In:
    pass

In.ok = ':blue[∴ OK] (🆗✅)';  In.ng = ':red[∴ NG] (❌)'
In.space = '<div style="margin:0px">'
In.background_color = 'linen'  #'lightyellow'
In.col_span_ref = [1, 1];  In.col_span_okng = [5, 1]  # 근거, OK(NG) 등 2열 배열 간격 설정
In.font_h1 = '28px';  In.font_h2 = '24px';  In.font_h3 = '22px';  In.font_h4 = '20px';  In.font_h5 = '18px';  In.font_h6 = '15px'

color = 'green'
In.border1 = f'<hr style="border-top: 2px solid {color}; margin-top:30px; margin-bottom:30px; margin-right: -30px">'  # 1줄
In.border2 = f'<hr style="border-top: 5px double {color}; margin-top: 0px; margin-bottom:30px; margin-right: -30px">' # 2줄
border = '<hr style="border-top: 2px solid purple; margin-top:15px; margin-bottom:15px;">'

def word_wrap_style(span, txt, fs):  # 자동 줄바꿈 등    
    return st.markdown(span + f'<div style="white-space:pre-line; display:inline-block; font-size: {fs}; line-height: 1.8; text-indent: 0em">{txt}</div>', unsafe_allow_html=True)    
    # return st.markdown(span + f'<span style="white-space:pre-line; display:inline; font-size: {fs}; line-height: 2; padding-left: 0px; text-indent: 10em">{txt}</span>', unsafe_allow_html=True)    


def Sidebar(h4, h5):
    sb.write(h4, '✤ Beam Type')
    In.type = sb.radio('숨김', ('Singly Reinforced', 'Doubly Reinforced'), horizontal=True, label_visibility='collapsed')

    sb.markdown(border, unsafe_allow_html=True)   ## 빈줄 공간
    sb.write(h4, '✤ Section Dimension')
    col = sb.columns(2, gap = 'medium')
    with col[0]:
        In.b = st.number_input(h5 + r'￭ $\bm{{b_e}}$ [mm]', min_value = 10., value = 400., step = 10., format = '%.0f')
    with col[1]:
        In.h = st.number_input(h5 + r'￭ $\bm{h}$ [mm]', min_value = 10., value = 600., step = 10., format = '%.0f')

    sb.markdown(border, unsafe_allow_html=True)   ## 빈줄 공간
    sb.write(h4, '✤ Material Properties')
    col = sb.columns(2, gap = 'medium')    
    with col[0]:
        In.fck = st.number_input(h5 + r'￭ $\bm{{f_{ck}}}$ [MPa]', min_value = 10., value = 21., step = 1., format = '%.0f')
        In.fy = st.number_input(h5 + r'￭ $\bm{{f_{y}}}$ [MPa]', min_value = 10., value = 400., step = 10., format = '%.0f')
        In.ffu = st.number_input(h5 + r'￭ $\bm{{f_{fu}}}$ [MPa]', min_value = 10., value = 1440., step = 10., format = '%.0f')
        Ec = 8500*(In.fck+4)**(1/3)/1e3
    with col[1]:
        In.Ec = st.number_input(h5 + r'￭ $\bm{{E_{c}}}$ [GPa]', min_value = 10., value = Ec, step = 1., format = '%.1f')
        In.Es = st.number_input(h5 + r'￭ $\bm{{E_{s}}}$ [GPa]', min_value = 10., value = 200., step = 10., format = '%.1f')
        In.Ef = st.number_input(h5 + r'￭ $\bm{{E_{f}}}$ [GPa]', min_value = 10., value = 120., step = 10., format = '%.1f')
    
    sb.markdown(border, unsafe_allow_html=True)   ## 빈줄 공간
    sb.write(h4, '✤ Reinforcement in Tension')

    sb.markdown(border, unsafe_allow_html=True)   ## 빈줄 공간
    sb.write(h4, '✤ Reinforcement in Compression')

    return In
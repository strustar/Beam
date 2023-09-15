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
    sb.write(h4, ':green[✤ Beam Type]')
    In.type = sb.radio('숨김', ('Singly Reinforced', 'Doubly Reinforced'), horizontal=True, label_visibility='collapsed')

    sb.markdown(border, unsafe_allow_html=True)   ## 빈줄 공간
    sb.write(h4, ':green[✤ Section Dimensions]')
    col = sb.columns(2, gap = 'medium')
    with col[0]:
        In.be = st.number_input(h5 + r'￭ $\bm{{\small{{b_e}} }}$ [mm]', min_value = 10., value = 400., step = 10., format = '%.0f')
    with col[1]:
        In.height = st.number_input(h5 + r'￭ $\bm{{\small{{h}} }}$ [mm]', min_value = 10., value = 600., step = 10., format = '%.0f')

    sb.markdown(border, unsafe_allow_html=True)   ## 빈줄 공간
    sb.write(h4, ':green[✤ Material Properties]')
    col = sb.columns(2, gap = 'medium')
    with col[0]:
        In.fck = st.number_input(h5 + r'￭ $\bm{{\small{{f_{ck}}} }}$ [MPa]', min_value = 10., value = 21., step = 1., format = '%.0f')
        In.fy = st.number_input(h5 + r'￭ $\bm{{\small{{f_{y}}} }}$ [MPa]', min_value = 10., value = 400., step = 10., format = '%.0f')
        In.ffu = st.number_input(h5 + r'￭ $\bm{{\small{{f_{fu}}} }}$ [MPa]', min_value = 10., value = 1440., step = 10., format = '%.0f')
        Ec = 8500*(In.fck+4)**(1/3)/1e3
    with col[1]:
        In.Ec = st.number_input(h5 + r'￭ $\bm{{\small{{E_{c}}} }}$ [GPa]', min_value = 10., value = Ec, step = 1., format = '%.1f', disabled=True)
        In.Es = st.number_input(h5 + r'￭ $\bm{{\small{{E_{s}}} }}$ [GPa]', min_value = 10., value = 200., step = 10., format = '%.1f')
        In.Ef = st.number_input(h5 + r'￭ $\bm{{\small{{E_{f}}} }}$ [GPa]', min_value = 10., value = 120., step = 10., format = '%.1f')
    
    sb.markdown(border, unsafe_allow_html=True)   ## 빈줄 공간
    sb.write(h4, ':red[✤ Reinforcement in Tension (인장 보강)]')
    In.Layer = sb.radio('숨김', ('Single Layer', 'Double Layer'), horizontal=True, label_visibility='collapsed', captions=['','보강재의 개수 : 짝수'])
    col = sb.columns(2, gap = 'medium')
    with col[0]:
        In.depth = st.number_input(h5 + r'￭ $\bm{{\small{{ d}} }}$ (인장철근 도심) [mm]', min_value = 10., value = 520., step = 10., format = '%.0f')
    if 'Doubl' in In.Layer:
        with col[1]:
            In.dt = st.number_input(h5 +  r'￭ $\bm{{\small{{ d_t}} }}$ (최외측) [mm]', min_value = 10., value = 540., step = 10., format = '%.0f')

    col = sb.columns(2, gap = 'medium')
    with col[0]:
        In.Dia = st.number_input(h5 +  '￭ Dia. (보강재 직경) [mm]', min_value = 4., value = 25.4, step = 0.2, format = '%.1f')
    with col[1]:
        In.QTY = st.number_input(h5 +  "￭ Q'TY (보강재 개수) [EA]", min_value = 1, value = 8, step = 1, format = '%d')


    sb.markdown(border, unsafe_allow_html=True)   ## 빈줄 공간
    sb.write(h4, ':blue[✤ Reinforcement in Compression (압축 보강)]')
    col = sb.columns(2, gap = 'medium')
    with col[0]:
        In.depth1 = st.number_input(h5 + r"￭ $\bm{{\small{{ d'}} }}$ (압축철근 도심) [mm]", min_value = 10., value = 60., step = 10., format = '%.0f')

    col = sb.columns(2, gap = 'medium')
    with col[0]:
        In.Dia1 = st.number_input(h5 +  '￭ Dia. (보강재 직경) [mm]', min_value = 5., value = 25.4, step = 0.2, format = '%.1f')
    with col[1]:
        In.QTY1 = st.number_input(h5 +  "￭ Q'TY (보강재 개수) [EA]", min_value = 1, value = 2, step = 1, format = '%d')

    return In
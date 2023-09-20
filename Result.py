import streamlit as st
import plotly.graph_objects as go
import numpy as np

def shape(fig, type, x0,y0,x1,y1, color, width, fillcolor):
    fig.add_shape(
        type=type,
        x0=x0, y0=y0, x1=x1, y1=y1,
        fillcolor=fillcolor,
        line=dict(
            color=color, width=width,
        ),
    )
# W3Schools HTML Colors: https://www.w3schools.com/colors/colors_names.asp
# HTML Color Codes: https://htmlcolorcodes.com/color-names/

def Fig(In, R, F):
    fig_width = In.max_width;  fig_height = 600
    fig = go.Figure()  # Create a blank figure    

    # 그림 상자 외부 박스    
    x0 = -fig_width/2; y0 = 0; x1 = fig_width/2; y1 = fig_height    
    shape(fig, 'rect', x0,y0,x1,y1, 'RoyalBlue', 3, 'rgba(0,0,0,0)')    

    # 콘크리트 단면
    max_bh_pixel = fig_height/1.5;  max_bh = max(In.be, In.height);  bh_ratio = max_bh_pixel/max_bh
    w = In.be*bh_ratio;  h = In.height*bh_ratio;  y_b = (fig_height - h)/2   # 고정, 계속 사용
    R_c = R.c*bh_ratio;  F_c = F.c*bh_ratio
    
    x0 = -w/2;  y0 = fig_height/2 - h/2;  x1 = w/2;  y1 = fig_height/2 + h/2
    shape(fig, 'rect', x0,y0,x1,y1, 'black', 1.5, 'rgba(0,0,0,0)')  # 전체 콘크리트 박스
    
    R_lightcyan = 'rgba(204, 255, 255, 1)';  F_lightcyan = 'rgba(102, 255, 255, 1)'
    if F.c <= R.c:  c1 = F_lightcyan;  c2 = R_lightcyan;  c = F_c
    if F.c >= R.c:  c1 = R_lightcyan;  c2 = F_lightcyan;  c = R_c
    for i in range(2):
        x0 = -w/2;  y0 = y_b + h;  x1 = w/2;  y1 = y0 - c
        if i == 0:  fillcolor = c1
        if i == 1:  fillcolor = c2;  y0 = y1;  y1 = y0 - abs(R_c - F_c)        
        shape(fig, 'rect', x0,y0,x1,y1, 'black', 1, fillcolor)      # RC / FRP 압축 영역

    # fig.add_annotation(x=-500, y=100, axref='x', ayref='y', ax=-500, ay=500, arrowside='end+start', arrowwidth=2, arrowsize=3, arrowhead=2, text='<b>bold</b> <i>italic</i>', font_size=20)
    

    # Add a filled triangle
    x0 = -w/2 - 40
    y0 = y_b
    x1 = x0
    y1 = y0 + h
    fillcolor = 'black'
    color = 'black'
    width = 1.5
    txt = In.height

    arrow_size = 15;  arrow_width = arrow_size/4

    fig.add_shape(    # 치수선
        type='line',
        x0=x0, y0=y0, x1=x1, y1=y1,
        fillcolor=fillcolor,
        line=dict(
            color=color, width=width,
        ),
    )
    # fig.add_annotation(
    #     x=x0, y=(y0+y1)/2,
    #     text='ff'
    # )

    fig.add_trace(go.Scatter(
        mode='text',
        x=[x0-10], y=[(y0+y1)/2],        
        # x=[0, 100, 200],
        # y=[100, 100, 100],
        # mode="lines+markers+text",
        # name="Lines, Markers and Text",   # legend
        # text=["Text A", "Text B", "Text C"],
        text=[f'{txt:.0f}'],
        textposition="middle left",
        textfont=dict(
            family='Nanum Gothic',
            size=18,
            color="black"
        ),
    ))
    for i in [1, 2]:
        if x1 == x0:
            if y0 <= y1:  sgn = 1
            if y0 >= y1:  sgn =-1
            a0 = x0;  a1 = x0 - arrow_width;  a2 = x0 + arrow_width
            if i == 1:  b0 = y0;  b1 = y0 + sgn*arrow_size
            if i == 2:  b0 = y1;  b1 = y1 - sgn*arrow_size
            b2 = b1

        fig.add_shape(    # 치수 보조선
            type='line',
            x0=x0-arrow_size, y0=b0, x1=x0+arrow_size, y1=b0,
            fillcolor=fillcolor,
            line=dict(
                color=color, width=width,
            ),
        )        
        fig.add_shape(    # 화살표
            type="path",
            path=f"M {a0} {b0} L {a1} {b1} L {a2} {b2} Z", # M = move to, L = line to, Z = close path
            fillcolor=fillcolor,
            line=dict(
                color=color, width=width,
            ),
        )




    # Update the layout properties
    fig.update_layout(
        autosize=False,
        width=fig_width, height=fig_height,
        margin=dict(l=0, r=0, t=0, b=0),
    )

    fig.update_xaxes(range=[-fig_width/2, fig_width/2])
    fig.update_yaxes(range=[0, fig_height]) #, scaleanchor='x' #, scaleratio=1, constrain='domain'

    # fig.update_xaxes(visible=False)
    # fig.update_yaxes(visible=False)

    st.plotly_chart(fig)

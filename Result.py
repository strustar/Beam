import streamlit as st
import plotly.graph_objects as go
import numpy as np

# W3Schools HTML Colors: https://www.w3schools.com/colors/colors_names.asp
# HTML Color Codes: https://htmlcolorcodes.com/color-names/

def shape(fig, type, x0,y0,x1,y1, fillcolor, color, width):
    fig.add_shape(
        type=type,
        x0=x0, y0=y0, x1=x1, y1=y1,
        fillcolor=fillcolor,
        line=dict(color=color, width=width, ),
    )

def dimension(fig, x0,y0,length, fillcolor, color, width, txt, loc, **kargs):
    arrow_size = 12;  arrow_width = arrow_size/4  # 화살표 치수 고정 !!!

    shift = 40
    if len(kargs) > 0:
        if 'Doubl' in kargs['Layer']:
            shift = 95
        
    if 'bottom' not in loc:     # 세로 치수 (left, right)
        if 'left' in loc:  sgn = 1;   textposition = "middle left"
        if 'right' in loc: sgn = -1;  textposition = "middle right"            
        x0 = x0 - sgn*shift;  x1 = x0;  y1 = y0 + length
        tx = x0 - sgn*10;  ty = (y0 + y1)/2
        
    if 'bottom' in loc:         # 가로 치수
        y0 = y0 - shift;  y1 = y0;  x1 = x0 + length
        tx = (x0 + x1)/2;  ty = y0 + 12
        textposition = "middle center"

    fig.add_shape(    # 치수선
        type='line',
        x0=x0, y0=y0, x1=x1, y1=y1,
        fillcolor=fillcolor,
        line=dict(color=color, width=width, ),
    )

    fig.add_trace(go.Scatter(
        mode='text',            # mode="lines+markers+text",  # text=["Text A", "Text B", "Text C"],  # name="Lines, Markers and Text",   # legend
        x=[tx], y=[ty],        
        text=[f'{txt:.0f}'],
        textposition=textposition,
        textfont=dict(color=color, size=18, family='Nanum Gothic', ),
        showlegend=False,
    ))

    for i in [1, 2]:
        if 'bottom' not in loc:    # 세로 치수 (left, right)
            if y0 <= y1:  sgn = 1
            if y0 >= y1:  sgn =-1
            a0 = x0;  a1 = x0 - arrow_width;  a2 = x0 + arrow_width
            if i == 1:  b0 = y0;  b1 = y0 + sgn*arrow_size
            if i == 2:  b0 = y1;  b1 = y1 - sgn*arrow_size
            b2 = b1
            p0 = x0 - arrow_size;  p1 = x0 + arrow_size
            q0 = b0;  q1 = b0

        if 'bottom' in loc:        # 가로 치수
            if x0 <= x1:  sgn = 1
            if x0 >= x1:  sgn =-1
            b0 = y0;  b1 = y0 - arrow_width;  b2 = y0 + arrow_width
            if i == 1:  a0 = x0;  a1 = x0 + sgn*arrow_size
            if i == 2:  a0 = x1;  a1 = x1 - sgn*arrow_size
            a2 = a1
            p0 = a0;  p1 = a0
            q0 = y0 - arrow_size;  q1 = y0 + arrow_size

        fig.add_shape(    # 치수 보조선
            type='line',
            x0=p0, y0=q0, x1=p1, y1=q1,
            fillcolor=fillcolor,
            line=dict(color=color, width=width, ),
        )        
        fig.add_shape(    # 화살표
            type="path",
            path=f"M {a0} {b0} L {a1} {b1} L {a2} {b2} Z", # M = move to, L = line to, Z = close path
            fillcolor=fillcolor,
            line=dict(color=color, width=width, ),
        )


def Fig(In, R, F):
    fig_width = In.max_width;  fig_height = 600
    fig = go.Figure()  # Create a blank figure    

    # 그림 상자 외부 박스    
    x0 = -fig_width/2; y0 = 0; x1 = fig_width/2; y1 = fig_height
    shape(fig, 'rect', x0,y0,x1,y1, 'rgba(0,0,0,0)', 'RoyalBlue', 3)
    
    ## 콘크리트 단면
    max_bh_pixel = fig_height/1.5;  max_bh = max(In.be, In.height);  bh_ratio = max_bh_pixel/max_bh
    w = In.be*bh_ratio;  h = In.height*bh_ratio;  y_b = (fig_height - h)/2   # 고정, 계속 사용
    R_c = R.c*bh_ratio;  F_c = F.c*bh_ratio
    
    x0 = -w/2;  y0 = y_b;  x1 = x0 + w;  y1 = y0 + h
    shape(fig, 'rect', x0,y0,x1,y1, 'rgba(0,0,0,0)', 'black', 1.5)  # 전체 콘크리트 박스
    
    R_lightcyan = 'rgba(204, 255, 255, 1)';  F_lightcyan = 'rgba(102, 255, 255, 1)'
    if F.c <= R.c:  c1 = F_lightcyan;  c2 = R_lightcyan;  c = F_c
    if F.c >= R.c:  c1 = R_lightcyan;  c2 = F_lightcyan;  c = R_c
    for i in range(2):
        x0 = -w/2;  y0 = y_b + h;  x1 = w/2;  y1 = y0 - c
        if i == 0:  fillcolor = c1
        if i == 1:  fillcolor = c2;  y0 = y1;  y1 = y0 - abs(R_c - F_c)        
        shape(fig, 'rect', x0,y0,x1,y1, fillcolor, 'black', 1)      # RC / FRP 압축 영역
    
    x0 = -w/2;  y0 = y_b    
    dimension(fig, x0,y0,h, 'black', 'black', 1.5, In.height, 'left')  # 세로 치수        
    dimension(fig, x0,y0,w, 'black', 'black', 1.5, In.be, 'bottom')    # 가로 치수
    ## 콘크리트 단면

    ## 철근    
    for i in range(3):  # 0, 1, 2
        if (i == 1 and 'Singl' in In.Layer): continue  # 단층일때 스킵
        if (i == 2 and 'Singl' in In.type):  continue  # 단철근 일때 스킵

        x0 = w/2;  y0 = y_b
        if i == 0:
            d = In.depth*bh_ratio            
            dimension(fig, x0,y0,h-d, 'black', 'black', 1.5, In.height-In.depth, 'right')

        if i == 1:
            dt = In.dt*bh_ratio
            dimension(fig, x0,y0,h-dt, 'black', 'black', 1.5, In.height-In.dt, 'right', Layer=In.Layer)
                    
        if i == 2:
            d1 = In.depth1*bh_ratio
            y0 = y_b + h - d1
            dimension(fig, x0,y0,d1, 'black', 'black', 1.5, In.depth1, 'right')
        
        dia = In.Dia*bh_ratio*1.4  # 보강재 40% 크게 (가독성 좋게 하기 위해서)
        x0 = -w/2;  y0 = y_b + d;  x1 = x0 + dia;  y1 = y0 + dia
        shape(fig, 'circle', x0,y0,x1,y1, fillcolor, 'black', 1)
        pass
    
    ## 철근





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

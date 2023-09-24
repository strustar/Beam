import streamlit as st
import plotly.graph_objects as go
import numpy as np

# W3Schools HTML Colors: https://www.w3schools.com/colors/colors_names.asp
# HTML Color Codes: https://htmlcolorcodes.com/color-names/
font_size = 17

def shape(fig, typ, x0,y0,x1,y1, fillcolor, color, width, **kargs):
    dash = 'solid'
    if len(kargs) > 0:  dash = kargs['LineStyle']
            
    fig.add_shape(
        type=typ,
        x0=x0, y0=y0, x1=x1, y1=y1,
        fillcolor=fillcolor,
        line=dict(color=color, width=width, dash=dash, ),   # dash = solid, dot, dash, longdash, dashdot, longdashdot, '5px 10px'
    )

def annotation(fig, x,y, color, txt, locx, locy, **kargs):
    bgcolor = None;  size = 17
    if len(kargs) > 0:  bgcolor = kargs['bgcolor'];  size = kargs['size']
    fig.add_annotation(
        x=x, y=y, text=txt,
        showarrow=False,
        bgcolor=bgcolor,
        font=dict(color=color, size=size, family='Arial, Helvetica', ),
        xanchor=locx, yanchor=locy,
    )

def dimension(fig, x0,y0,length, fillcolor, color, width, txt, loc, opt):
    shift = 40;  arrow_size = 12
    if 'Doubl' in opt:  shift = 95
    if 'force' in opt:  shift = 0;  arrow_size = 18
    arrow_width = arrow_size/4  # 화살표 두께 고정 !!!
    
    if 'bottom' in loc:     # 가로 치수 (bottom)
        y0 = y0 - shift;  y1 = y0;  x1 = x0 + length
        tx = (x0 + x1)/2;  ty = y0 + 13
        locx = 'center';  locy = 'middle'
        if '1' in opt:  tx = x1;  locx = 'right'
        if '2' in opt:  tx = x1;  locx = 'left'
        if 'up' in opt:   ty = y0;  locy = 'bottom'
        if 'down' in opt: ty = y0;  locy = 'top'
        
        if 'tension' in opt and '1' in opt: tx = x0;  locx = 'right'
        if 'tension' in opt and '2' in opt: tx = x0;  locx = 'left'
    else:                   # 세로 치수 (left, right)
        if 'left' in loc:  sgn = 1;  locx = 'right';  locy = 'middle'
        if 'right' in loc: sgn =-1;  locx = 'left';   locy = 'middle'
        x0 = x0 - sgn*shift;  x1 = x0;  y1 = y0 + length
        tx = x0 - sgn*10;  ty = (y0 + y1)/2     
    
    shape(fig, 'line', x0,y0,x1,y1, fillcolor, color, width)   # 치수선
    annotation(fig, tx,ty, color, txt, locx, locy)             # 치수 문자

    for i in [1, 2]:
        if 'bottom' in loc:     # 가로 치수 (bottom)
            if x0 <= x1:  sgn = 1
            if x0 >= x1:  sgn =-1
            b0 = y0;  b1 = y0 - arrow_width;  b2 = y0 + arrow_width
            if i == 1:  a0 = x0;  a1 = x0 + sgn*arrow_size
            if i == 2:  a0 = x1;  a1 = x1 - sgn*arrow_size
            a2 = a1
            p0 = a0;  p1 = a0
            q0 = y0 - arrow_size;  q1 = y0 + arrow_size
        else:                   # 세로 치수 (left, right)
            if y0 <= y1:  sgn = 1
            if y0 >= y1:  sgn =-1
            a0 = x0;  a1 = x0 - arrow_width;  a2 = x0 + arrow_width
            if i == 1:  b0 = y0;  b1 = y0 + sgn*arrow_size
            if i == 2:  b0 = y1;  b1 = y1 - sgn*arrow_size
            b2 = b1
            p0 = x0 - arrow_size;  p1 = x0 + arrow_size
            q0 = b0;  q1 = b0

        if 'force' not in opt:  shape(fig, 'line', p0,q0,p1,q1, fillcolor, color, width)  # 치수 보조선
        if i == 2 and 'force' in opt:  continue
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
    x0 = -fig_width/2;  y0 = 0;  x1 = fig_width/2;  y1 = fig_height
    shape(fig, 'rect', x0,y0,x1,y1, 'rgba(0,0,0,0)', 'RoyalBlue', 3)
    
    ## 콘크리트 단면
    max_bh_pixel = fig_height/1.5;  max_bh = max(In.be, In.height);  bh_ratio = max_bh_pixel/max_bh
    w = In.be*bh_ratio;  h = In.height*bh_ratio;  yb = (fig_height - h)/2;  yt = yb + h   # 고정, 계속 사용
    R_c = R.c*bh_ratio;  F_c = F.c*bh_ratio
    
    x0 = -w/2;  y0 = yb;  x1 = w/2;  y1 = yt
    shape(fig, 'rect', x0,y0,x1,y1, 'rgba(0,0,0,0)', 'black', 1.5)  # 전체 콘크리트 박스
    
    R_lightcyan = 'rgba(204, 255, 255, 1)';  F_lightcyan = 'rgba(102, 255, 255, 1)'
    if F.c <= R.c:  c1 = F_lightcyan;  c2 = R_lightcyan;  c = F_c
    if F.c >= R.c:  c1 = R_lightcyan;  c2 = F_lightcyan;  c = R_c
    for i in range(1, 2+1):
        x0 = -w/2;  y0 = yt;  x1 = w/2;  y1 = y0 - c
        if i == 1:  fillcolor = c1
        if i == 2:  fillcolor = c2;  y0 = y1;  y1 = y0 - abs(R_c - F_c)        
        shape(fig, 'rect', x0,y0,x1,y1, fillcolor, 'black', 1)      # RC / FRP 압축 영역
    opt = []
    dimension(fig, -w/2,yb,h, 'black', 'black', 1.5, f'{In.height:,.0f}', 'left',   [])      # 세로 치수        
    dimension(fig, -w/2,yb,w, 'black', 'black', 1.5, f'{In.be:,.0f}',     'bottom', [])    # 가로 치수
    ## 콘크리트 단면

    ## 철근
    dia_factor = 1.2    # 보강재 20% 크게 (가독성 좋게 하기 위해서)
    for i in range(1, 2+1):
        if (i == 2 and 'Singl' in In.Type):  continue  # 단철근 일때 스킵
        
        d = In.depth*bh_ratio;  dt = In.dt*bh_ratio;  d1 = In.depth1*bh_ratio;  d_dt = abs(2*(d - dt))   # 치수
        if i == 1:  dimension(fig, w/2, yb, h-d,     'black', 'black', 1.5, f'{In.height-In.depth:,.0f}', 'right', [])
        if i == 1:  dimension(fig, w/2, yb, h-dt,    'black', 'black', 1.5, f'{In.height-In.dt:,.0f}',    'right', In.Layer)  # Double Layer
        if i == 2:  dimension(fig, w/2, yt-d1, d1, 'black', 'black', 1.5, f'{In.depth1:,.0f}',            'right', [])
        
        if i == 1:  depth = dt;  dia = In.Dia*bh_ratio*dia_factor;   qty = In.QTY;   fillcolor = 'red'
        if i == 2:  depth = d1;  dia = In.Dia1*bh_ratio*dia_factor;  qty = In.QTY1;  fillcolor = 'darkgreen'
        y0 = yt - depth - dia/2;  qty0 = qty
        if (i == 1 and 'Doubl' in In.Layer):  qty = int(np.ceil(qty/2))
        for rebar in range(1, qty+1):
            if qty == 1:  x0 = -w/2 + w/2 - dia/2
            if qty != 1:  x0 = -w/2 + w/6 - dia/2 + (rebar - 1)*4*w/6/(qty - 1)
            if (i == 1 and qty0%2 == 1  and 'Doubl' in In.Layer and rebar == qty):  dia = dia/np.sqrt(2)
            shape(fig, 'circle', x0,y0, x0 + dia, y0 + dia, fillcolor, 'black', 1.5)
            if (i == 1 and 'Doubl' in In.Layer):  shape(fig, 'circle', x0,y0+d_dt, x0 + dia, y0+d_dt + dia, fillcolor, 'black', 1.5)
                
        if i == 1:
            txt = f'<i>A<sub>s</sub> = A<sub>f</sub></i><br>{In.As:,.1f} mm²'  # HTML 엔티티(Entities)
            annotation(fig, 0,y0+d_dt+60, 'red', txt, 'center', 'middle')
        if i == 2:
            txt = f"<i>A<sub>s</sub>' = A<sub>f</sub>'</i><br>{In.As1:,.1f} mm²"   # ₀₁₂₃₄₅₆₇₈₉ ⁰¹²³⁴⁵⁶⁷⁸⁹
            annotation(fig, 0,y0-d_dt-10, 'darkgreen', txt, 'center', 'middle')
    ## 철근

    ## 변형률 (ep_cu, ep_s, ep_f),  % 1 : KDS (RC), 좌측, 2: ACI (FRP), 우측    
    max_ep_pixel = 150;  max_ep = max(R.ep_cu, R.ep_s, F.ep_cu, F.ep_f);  ep_ratio = max_ep_pixel/max_ep
    for i in range(1, 2+1):
        if i == 1:  sgn =-1;  center = R.c;  ep_cu = R.ep_cu;  ep_sf = R.ep_s;  ep_t = R.ep_t;  ep_sf1 = R.ep_s1
        if i == 2:  sgn = 1;  center = F.c;  ep_cu = F.ep_cu;  ep_sf = F.ep_f;  ep_t = F.ep_t;  ep_sf1 = F.ep_f1
        c = center*bh_ratio
        
        # Center Line (수평선)
        x0 = sgn*(w/2 + 110);  x1 = x0 + sgn*600;  y0 = yt - c;  y1 = y0
        shape(fig, 'line', x0,y0,x1,y1, fillcolor, 'black', 1., LineStyle='10px 5px')
        
        # 기준선 (수직선)
        x0 = sgn*(w/2 + 230);  x1 = x0;  y0 = yt - dt;  y1 = yt   # x0 : 고정된 값
        shape(fig, 'line', x0,y0,x1,y1, fillcolor, 'black', 1.5)
        
        # c (center) 치수
        if i == 1:  loc = 'left'
        if i == 2:  loc = 'right'
        txt = f'c = {center:.1f}'
        if i == 2 and F.rho_f < F.rho_fb:  txt = f'c<sub>b</sub> = {center:.1f}'    # FRP and Under-reinforced
        dimension(fig, x0 + sgn*4, yt - c, c, 'black', 'black', 1.5, txt, loc, [])

        # epsilon_cu
        x1 = x0 - sgn*ep_cu*ep_ratio;  y0 = y1
        shape(fig, 'line', x0,y0,x1,y1, fillcolor, 'blue', 2)                       # 수평선
        annotation(fig, (x0+x1)/2,y0, 'blue', f'{ep_cu:.4f}', 'center', 'bottom')   # 변형률 텍스트
        shape(fig, 'line', x0,yt-c,x1,y1, fillcolor, 'blue', 2)                     # 대각선 (중심과 연결선)
             
        # epsilon_sf    
        x1 = x0 + sgn*ep_t*ep_ratio;  y0 = yt - dt;  y1 = y0
        shape(fig, 'line', x0,y0,x1,y1, fillcolor, 'red', 2)                        # 수평선
        annotation(fig, (x0+x1)/2,y0, 'red', f'{ep_t:.4f}', 'center', 'top')        # 변형률 텍스트
        shape(fig, 'line', x0,yt-c,x1,y1, fillcolor, 'red', 2)                      # 대각선 (중심과 연결선)        
        if ('Doubl' in In.Layer):
            x1 = x0 + sgn*ep_sf*ep_ratio;  y0 = yt - d;  y1 = y0
            shape(fig, 'line', x0,y0,x1,y1, fillcolor, 'red', 2)                        # 수평선
            annotation(fig, (x0+x1)/2,y0, 'red', f'{ep_sf:.4f}', 'center', 'bottom')    # 변형률 텍스트

        # 압축 철근 변형률  (epsilon_sf1)
        if 'Doubl' in In.Type:
            x1 = x0 - sgn*ep_sf1*ep_ratio;  y0 = yt - d1;  y1 = y0
            shape(fig, 'line', x0,y0,x1,y1, fillcolor, 'darkgreen', 2)                        # 수평선
            annotation(fig, (x0+x1)/2,y0, 'darkgreen', f'{ep_sf1:.4f}', 'center', 'bottom')   # 변형률 텍스트


    ## 응력, 힘 Stress, Strength, C, T, Mn,  % 1 : KDS (RC), 좌측, 2: ACI (FRP), 우측
    for i in range(1, 2+1):
        if i == 1:  sgn =-1;  a = R.a;  Cc = R.Cc;  Cs = R.Cs;  Tc = R.Tc;  Ts = R.Ts;  fillcolor = R_lightcyan
        if i == 2:  sgn = 1;  a = F.a;  Cc = F.Cc;  Cs = F.Cf;  Tc = F.Tc;  Ts = F.Tf;  fillcolor = F_lightcyan
        a_ratio = a*bh_ratio
        
        # 기준선 (수직선)
        x0 = sgn*(w/2 + 520);  x1 = x0;  y0 = yt - d;  y1 = yt   # x0 : 고정된 값
        shape(fig, 'line', x0,y0,x1,y1, fillcolor, 'black', 1.5)
        
        # Compression (박스 음영)  # RC / FRP 압축 영역
        x1 = x0 + sgn*70;  y0 = yt;  y1 = yt - a_ratio
        shape(fig, 'rect', x0,y0,x1,y1, fillcolor, 'black', 1)
        
        # a (a = beta1*c) 치수
        if i == 1:  loc = 'right';  sf = 's';  Md = R.Md;  phi = R.phi;  phi_Status = R.phi_Status
        if i == 2:  loc = 'left' ;  sf = 'f';  Md = F.Md;  phi = F.phi;  phi_Status = F.phi_Status
        txt = f'a = {a:.1f}'
        if i == 2 and F.rho_f < F.rho_fb:  txt = f'a<sub>b</sub> = {a:.1f}'    # FRP and Under-reinforced
        dimension(fig, x0 + sgn*4, yt - a_ratio, a_ratio, 'black', 'black', 1.5, txt, loc, [])
        
        # Cc, Cs(or Cf) (Compression)
        if d1 <= a_ratio/2:  opt1 = 'down';  opt2 = 'up'
        if d1 >= a_ratio/2:  opt1 = 'up';    opt2 = 'down'
        txt = f'C<sub>c</sub> = {Cc:,.1f} kN'
        if i == 2 and F.rho_f < F.rho_fb:  txt = f'C<sub>c</sub> ≠ T<sub>c</sub>'    # FRP and Under-reinforced
        opt1 = 'force' + str(i) + opt1
        dimension(fig, x0, yt - a_ratio/2, sgn*100, 'blue', 'blue', 2.5, txt, 'bottom', opt1)
        if 'Doubl' in In.Type:
            opt2 = 'force' + str(i) + opt2
            dimension(fig, x0, yt - d1, sgn*100, 'darkgreen', 'darkgreen', 2.5, f'C<sub>{sf}</sub> = {Cs:,.1f} kN', 'bottom', opt2)
        
        # T = Tc + Ts(or Tf) (Tension)
        opt3 = 'force' + str(i) + 'up' + 'tension'
        dimension(fig, x0+sgn*100, yt - d, -sgn*100, 'red', 'red', 2.5, f'T = {Tc + Ts:,.1f} kN', 'bottom', opt3)

        # Md = phi Mn, phi_Status
        txt = f'ϕM<sub>n</sub> = {Md:,.1f} kN&#8226;m<br>(ϕ = {phi:.3f})'
        annotation(fig, x0 + sgn*10, yb + 0.45*h, 'black', txt, loc, 'middle')  # &#8226;(·보다 큰것)
        if 'Tension' in phi_Status:  color = 'red'
        if 'Compres' in phi_Status:  color = 'blue'
        annotation(fig, x0 + sgn*10, yb + 0.35*h, color, '('+phi_Status+')', loc, 'middle')
        
        ##  title
        x0 = sgn*fig_width/4;  y0 = 570
        if i == 1:  txt = '[ Rebar Concrete (KDS 14 : 2021) ]'
        if i == 2:  txt = '[ FRP Concrete (ACI 440.1R-15) ]'
        annotation(fig, x0, y0, 'blue', txt, 'center', 'middle', bgcolor = 'gold', size = 24)
        
    ## FRP and Under-reinforced (텍스트)
    if F.rho_f <= F.rho_fb:
        txt = """
        ※ In the case of under-reinforced section, the ACI stress block is not applicable,      
        <br>      because maximum concrete strain(0.003) may not be attained at failure.         
        <br>    Hence, an equivalent stress block would be used that approximates              
        <br>   the stress distribution in the concrete at the particular strain level reached.
        """
        annotation(fig, w/2+100, yb, 'blue', txt, 'left', 'top', bgcolor = None, size = 15)        

    

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


# ====================================================================================================
def text(fig, tx,ty, color, txt, loc, **kargs):   # 사용 안함
    textposition = "middle center"
    # if 'top' in loc:  textposition = "middle center"
    
    fig.add_trace(go.Scatter(
        mode='text',
        x=[tx], y=[ty],
        text=[txt],        
        textposition=textposition,
        textfont=dict(color=color, size=font_size, family='Arial, Helvetica', ),
        showlegend=False,
    ))
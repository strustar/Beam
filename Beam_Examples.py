import streamlit as st
from Beam_Sidebar import In

def Singly_ex1():   # Singly Example 1
    st.session_state.Type = 'Singly Reinforced'
    st.session_state.be = 300;  st.session_state.height = 600
    st.session_state.fy = 400;  st.session_state.f_fu = 1440;  st.session_state.fck = 24
    st.session_state.Es = 200;  st.session_state.Ef = 120;     st.session_state.Ec = 8500*(In.fck+4)**(1/3)/1e3

    st.session_state.Layer = 'Single Layer'
    st.session_state.depth = 540;  In.dt = In.depth  # 초기값 (Single Layer)
    st.session_state.Dia = 22.2;  st.session_state.QTY = 4

def Singly_ex2():   # Singly Example 2
    st.session_state.Type = 'Singly Reinforced'
    st.session_state.be = 300;  st.session_state.height = 600
    st.session_state.fy = 400;  st.session_state.f_fu = 600;  st.session_state.fck = 50
    st.session_state.Es = 200;  st.session_state.Ef = 50;     st.session_state.Ec = 8500*(In.fck+4)**(1/3)/1e3

    st.session_state.Layer = 'Single Layer'
    st.session_state.depth = 540;  In.dt = In.depth  # 초기값 (Single Layer)
    st.session_state.Dia = 22.2;  st.session_state.QTY = 4

def Singly_ex3():   # Singly Example 3
    st.session_state.Type = 'Singly Reinforced'
    st.session_state.be = 400;  st.session_state.height = 700
    st.session_state.fy = 400;  st.session_state.f_fu = 1440;  st.session_state.fck = 24
    st.session_state.Es = 200;  st.session_state.Ef = 120;     st.session_state.Ec = 8500*(In.fck+4)**(1/3)/1e3

    st.session_state.Layer = 'Single Layer'
    st.session_state.depth = 635;  In.dt = In.depth  # 초기값 (Single Layer)
    st.session_state.Dia = 25.4;  st.session_state.QTY = 4

def Singly_ex4():   # Singly Example 4
    st.session_state.Type = 'Singly Reinforced'
    st.session_state.be = 400;  st.session_state.height = 700
    st.session_state.fy = 400;  st.session_state.f_fu = 1440;  st.session_state.fck = 24
    st.session_state.Es = 200;  st.session_state.Ef = 120;     st.session_state.Ec = 8500*(In.fck+4)**(1/3)/1e3

    st.session_state.Layer = 'Double Layer'
    st.session_state.depth = 635.;  # st.session_state.dt 은 기본값 + 20mm
    st.session_state.Dia = 25.4;   st.session_state.QTY = 8

def Doubly_ex1():   # Doubly Example 1
    st.session_state.Type = 'Doubly Reinforced'
    st.session_state.be = 400;  st.session_state.height = 600
    st.session_state.fy = 400;  st.session_state.f_fu = 1440;  st.session_state.fck = 21
    st.session_state.Es = 200;  st.session_state.Ef = 120;     st.session_state.Ec = 8500*(In.fck+4)**(1/3)/1e3

    st.session_state.Layer = 'Double Layer'
    st.session_state.depth = 520.;  # st.session_state.dt 은 기본값 + 20mm
    st.session_state.Dia = 25.4;   st.session_state.QTY = 8
    st.session_state.depth1 = 60
    st.session_state.Dia1 = 25.4;   st.session_state.QTY1 = 2

def Doubly_ex2():   # Doubly Example 2
    st.session_state.Type = 'Doubly Reinforced'
    st.session_state.be = 400;  st.session_state.height = 600
    st.session_state.fy = 400;  st.session_state.f_fu = 1440;  st.session_state.fck = 21
    st.session_state.Es = 200;  st.session_state.Ef = 120;     st.session_state.Ec = 8500*(In.fck+4)**(1/3)/1e3

    st.session_state.Layer = 'Double Layer'
    st.session_state.depth = 520.;  # st.session_state.dt 은 기본값 + 20mm
    st.session_state.Dia = 25.4;   st.session_state.QTY = 8
    st.session_state.depth1 = 60
    st.session_state.Dia1 = 25.4;   st.session_state.QTY1 = 4

def Doubly_ex3():   # Doubly Example 3
    st.session_state.Type = 'Doubly Reinforced'
    st.session_state.be = 300;  st.session_state.height = 700
    st.session_state.fy = 400;  st.session_state.f_fu = 1440;  st.session_state.fck = 30
    st.session_state.Es = 200;  st.session_state.Ef = 120;     st.session_state.Ec = 8500*(In.fck+4)**(1/3)/1e3

    st.session_state.Layer = 'Double Layer'
    st.session_state.depth = 610.;  # st.session_state.dt 은 기본값 + 20mm
    st.session_state.Dia = 25.4;   st.session_state.QTY = 8
    st.session_state.depth1 = 65
    st.session_state.Dia1 = 25.4;   st.session_state.QTY1 = 2

def Doubly_ex4():   # Doubly Example 4
    st.session_state.Type = 'Doubly Reinforced'
    st.session_state.be = 300;  st.session_state.height = 700
    st.session_state.fy = 400;  st.session_state.f_fu = 1440;  st.session_state.fck = 30
    st.session_state.Es = 200;  st.session_state.Ef = 120;     st.session_state.Ec = 8500*(In.fck+4)**(1/3)/1e3

    st.session_state.Layer = 'Double Layer'
    st.session_state.depth = 610.;  # st.session_state.dt 은 기본값 + 20mm
    st.session_state.Dia = 25.4;   st.session_state.QTY = 8
    st.session_state.depth1 = 65
    st.session_state.Dia1 = 25.4;   st.session_state.QTY1 = 4

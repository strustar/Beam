import streamlit as st

c = 'lightblue'
aa = (
    f'font-weight: bold !important;'
    f'background-color: {c};'
    )
# 라디오 버튼 스타일 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
def radio(color, width):    
    radio_style = f""" <style>
        div.row-widget.stRadio > div[role='radiogroup'] > label input[type=radio] {{
            display: none;   /*기본 스타일 옵션 제거, 없어도 될거 같은데?? */
            font-weight: bold !important;
        }}
        div.row-widget.stRadio > div[role='radiogroup'] {{
            display: flex;
            justify-content: space-between;
            width: 100%;            
            flex-direction: row;
            font-weight: bold !important;
        }}
        div.row-widget.stRadio > div[role='radiogroup'] > label {{
            # display: inline-flex;
            # justify-content: center;
            # align-items: center;            
            font-weight: bold !important;
            padding: 2px;
            padding-left: 10px;
            padding-right: 15px;
            margin-right: 3%;
            # color: blue;
            # background-color: {color};
            # border: 1px solid blue;
            # border-radius: 100px;    
            # width: 30px;       /* 추가: 라벨의 너비를 100px로 설정 */
            # height: 100%;       /* 추가: 라벨의 높이를 50px로 설정 */
        }}
        div.row-widget.stRadio > div {{
            # display: inline-flex;
            # flex-direction: column;
            # justify-content: center;
            # align-items: center;
            font-weight: bold !important;
            font-size: 28px !important;
            padding: 5px;
            padding-left: 10px;
            padding-right: 5px;
            margin-right: 15px;
            margin-right: 3%;
            # color: blue;
            background-color: {color};            
            border: 1px solid black;
            border-radius: 100px;    
            # width: {width};       /* 추가: 라벨의 너비를 100px로 설정 */
            # width: 50%;            
            # height: 100%;       /* 추가: 라벨의 높이를 50px로 설정 */
        }}
        div.row-widget.stSelectbox > div[data-baseweb='select'] > div {{
            display: inline-flex;            
            justify-content: center;
            align-items: center;
            margin-top: -5px;
            padding: 0px;
            padding-left: 5px;
            background-color: {color};
            font-size: 18px;
            # color: blue;
            font-weight: bold;
            border: 1px solid black;
            border-radius: 100px;
            # width: 90%;
            # width: {width};
        }}
        div.row-widget.stSelectbox > div[data-baseweb='select'] > div:hover {{
            {aa}
        }}
        div.row-widget.stRadio > div[role='radiogroup'] > label:hover {{
            font-weight: bold !important;
            background-color: lightblue;    
        }}
    </style> """
    st.markdown(radio_style, unsafe_allow_html=True)
# 라디오 버튼 스타일 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
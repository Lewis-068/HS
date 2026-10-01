import streamlit as st

if 'page' not in st.session_state:
  st.session_state['page'] = 'main'
if 'email' not in st.session_state:
  st.session_state['email'] = None


def show_main_page():
  st.title("**[공지사항]** 34기 학술 자료 사이트_HS입니다.")

  tab1, tab2, tab3, tab4, tab5 = st.tabs(['수학','물리','화학','생명','지구'])

  col_left, col_right = st.columns(2)

  with tab1:
    st.link_button("수학 필기 모음_HS","https://docs.google.com/document/d/1IfHRtknxkkj1dtf5h2tnIFDs0aYaJgRB7KfH9WbWAQQ/edit?usp=sharing")
  with.tab2:
    st.link_button("물리 개념 정리_HS","https://docs.google.com/document/d/1Hq--M0r059_DK8DVi7FSDuMlbZuf3KcgYEyS9QVIAEM/edit?usp=sharing")
  with.tab3:
    st.link_button("화학 개념 정리(중단)_HS", "https://docs.google.com/document/d/1Vg_vugyvchkBi17DqHDL8o216NTWcLOQPBlHBj-R3_0/edit?usp=sharing")
  with.tab4:
    st.link_button("생명과학 정리_HS", "https://docs.google.com/document/d/1D6qrxYU7jllv5jtnFGlxYAbMLa0rDQgcxoGWZU5P-pE/edit?usp=sharing")
    st,link_button("생물의 유전 '조건 X'문제", "https://docs.google.com/document/d/1re8tg8GgR0f39a1YsslOEHRyS_RaBKt93kwJ-D1uTHM/edit?usp=sharing")
  with.tab5:
    st.link_button("지구과학 정리", "https://docs.google.com/document/d/1YOST6DnB_4Dr_jXNPWYKQ8C2EXSWMlUK6Q9_FuhP0Gk/edit?usp=sharing")




if session_state == 'main':
  show_main_page()
elif session_state == 

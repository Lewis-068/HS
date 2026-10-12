import streamlit as st

if 'page' not in st.session_state:
  st.session_state['page'] = 'main'
if 'email' not in st.session_state:
  st.session_state['email'] = None


def show_main_page():

  title, drive = st.columns([4,1])
  with title:  
    st.title("**34기 학술 자료 사이트_HS**")
  with drive:
    st.link_button("공유 드라이브","https://drive.google.com/drive/folders/0AGBBqhm2jLp4Uk9PVA?hl=ko")
  
  tab1, tab2, tab3, tab4, tab5 = st.tabs(['수학','물리','화학','생명','지구'])
  
  st.info("**[공지사항]** 34기 학술 자료 사이트입니다.")
  
  col_left, col_right = st.columns(2)

  with tab1:
    with st.container(border=True, height=170):
      st.markdown("### 수학")
      st.caption("대수, 미적분1")
      st.link_button("수학 필기 모음_HS","https://docs.google.com/document/d/1IfHRtknxkkj1dtf5h2tnIFDs0aYaJgRB7KfH9WbWAQQ/edit?usp=sharing", use_container_width=True)
  with tab2:
    with st.container(border=True, height=170):
      st.markdown("### 물리")
      st.caption("역학과 에너지")
      st.link_button("물리 개념 정리_HS","https://docs.google.com/document/d/1Hq--M0r059_DK8DVi7FSDuMlbZuf3KcgYEyS9QVIAEM/edit?usp=sharing", use_container_width=True)
  with tab3:
    with st.container(border=True, height=170):
      st.markdown("### 화학")
      st.caption("물질과 에너지")
      st.link_button("화학 개념 정리(중단)_HS", "https://docs.google.com/document/d/1Vg_vugyvchkBi17DqHDL8o216NTWcLOQPBlHBj-R3_0/edit?usp=sharing", use_container_width=True)
  with tab4:
    with st.container(border=True, height=170):
      st.markdown("### 생명")
      st.caption("통합과학1, 통합과학2, 생물의 유전")
      st.link_button("생명과학 정리_HS", "https://docs.google.com/document/d/1D6qrxYU7jllv5jtnFGlxYAbMLa0rDQgcxoGWZU5P-pE/edit?usp=sharing", use_container_width=True)
      st.link_button("생물의 유전 '조건 X'문제", "https://docs.google.com/document/d/1re8tg8GgR0f39a1YsslOEHRyS_RaBKt93kwJ-D1uTHM/edit?usp=sharing", use_container_width=True)
  with tab5:
    with st.container(border=True, height=170):
      st.markdown("### 지구")
      st.caption("행성우주 과학")
      st.link_button("지구과학 정리_HS", "https://docs.google.com/document/d/1YOST6DnB_4Dr_jXNPWYKQ8C2EXSWMlUK6Q9_FuhP0Gk/edit?usp=sharing", use_container_width=True)

  with col_left:
    st.link_button("이메일 수신 동의/미동의", "https://forms.gle/J9uYuXPvH9tFnCAY9")

  with col_right:
    st.session_state['page'] = 'suggest'

def show_suggest_page():

  st.title("**34기 학술 자료 사이트_HS**")
  form_url = "https://docs.google.com/forms/d/e/1FAIpQLScF0MI3NHn3m5OjOc2kEqYym0QDoOl_mscj1Hj4SVJkGDPjYg/viewform??embedded=true"
  st.components.v1.iframe(form_url, height=300, scrolling=True)
  
  '''
  content = st.text_area("건의 내용 작성", height=300)
    
  col1, col2 = st.columns(2)
  with col1:
    if st.button("제출하기"):
      if content.strip():
        save_suggestion_to_db(content)
        st.success("건의사항이 제출되었습니다. 감사합니다")
        st.session_state['page'] = 'main'
        st.rerun()
      else:
        st.warning("내용이 입력되지 않았습니다.")
  
  with col2:
  '''
  
  if st.button("돌아가기"):
    st.session_state['page'] = 'main'
    st.rerun()
    

if st.session_state['page'] == 'main':
    show_main_page()
if st.session_state['page'] == 'suggest':
    show_suggest_page()

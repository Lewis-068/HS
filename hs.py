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
  
  st.info("**[공지사항]** \n수학 필기 모음_HS 대수 증명 작성 중입니다. \n1반, 2반, 3반 예정된 수행평가 일정 제보해주시면 감사하겠습니다.")
  
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
    st.link_button("이메일 수신 동의/미동의", "https://docs.google.com/forms/d/e/1FAIpQLScJCCfpfFsHKUqPGoQ0PcNHRv3RysKb8nrVF4jmamunX3fHOA/viewform?usp=publish-editor")

  with col_right:
    if st.button("익명 건의함"):
      st.session_state['page'] = 'suggest'

  taba,tabb,tabc = st.tabs(['1반 수행평가','2반 수행평가','3반 수행평가'])

  with taba:
    st.write('대수 | 삼각함수 문제 만들기(11/01 1교시)')
    st.write('대수 | 50개 증명(날짜 미정)')
    st.write('전자기와 양자 | science snack project (진행중)')
    st.write('화학 반응의 세계 | 산 염기 중화 적정(16번~21번)')
    with st.expender('화학 반응의 세계 | 탄소 화합물 구조 제안서(날짜 미정)'):
      st.write('어떤 문제에 도움이 되는 탄소 화합물 구조를 만들어 제안서를 작성함. 논문 자료를 종합한 후, AI에게 '이러한 문제를 해결할 수 있는 탄소화합물을 설계해줘' 식의 프롬포트 작성. 사전 논문을 얼마나 때려박냐에 따라 정확도, 가치 달라짐')
    st.write('생물의 유전 | 질문 노트(진행중 - 4회차)')
    st.write('생물의 유전 | 모의활동을 통한 유전 원리 분석과 추론(10/29 3교시)')
    st.write('행성우주과학 | 주계열 맞추기(날짜미정)')

def show_suggest_page():

  st.title("**34기 학술 자료 사이트_HS**")
  form_url = "https://docs.google.com/forms/d/e/1FAIpQLScF0MI3NHn3m5OjOc2kEqYym0QDoOl_mscj1Hj4SVJkGDPjYg/viewform?embedded=true"
  st.components.v1.iframe(form_url, height=425, scrolling=True)
  
  
  if st.button("돌아가기"):
    st.session_state['page'] = 'main'
    st.rerun()
    

if st.session_state['page'] == 'main':
    show_main_page()
elif st.session_state['page'] == 'suggest':
    show_suggest_page()

import streamlit as st
import pandas as pd
import random

hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    [data-testid="stToolbar"] {visibility: hidden;}
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)


st.set_page_config(page_title="34기 학술 자료 사이트_HS")

if 'page' not in st.session_state:
  st.session_state['page'] = 'main'
if 'email' not in st.session_state:
  st.session_state['email'] = None
if st.session_state['page'] != 'blackjack' and 'dealer' in st.session_state:
  del st.session_state['dealer']
if st.session_state['page'] != 'blackjack' and 'player' in st.session_state:
  del st.session_state['player']
if st.session_state['page'] != 'blackjack' and 'rate' in st.session_state:
  del st.session_state['rate']



def show_main_page():

  title, drive = st.columns([4,1])
  with title:  
    st.title("**34기 학술 자료 사이트_HS**")
  with drive:
    st.link_button("공유 드라이브","https://drive.google.com/drive/folders/0AGBBqhm2jLp4Uk9PVA?hl=ko")
  
  tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(['수학','물리학','화학','생명과학','지구과학','문과 과목','임시시간표'])
  
  st.info("**[공지사항]** 34기 학술 자료 사이트입니다.")
  
  col_left, col_right1, col_right2 = st.columns([8,3,5])

  with tab1:
    with st.container(border=True, height=170):
      st.markdown("### 수학")
      math_list = ["사전 정의는 '수량 및 공간의 성질에 관하여 연구하는 학문'이다.",
                   "교육과정 중에서는 미분 이후에 적분을 배우지만, 실제로 더 먼저 탄생한 것은 적분이다."
                  ]
      math = random.choice(math_list)
      st.caption(f"캡션: {math}")
      st.link_button("수학 필기 모음_HS","https://docs.google.com/document/d/1IfHRtknxkkj1dtf5h2tnIFDs0aYaJgRB7KfH9WbWAQQ/edit?usp=sharing", use_container_width=True)
  with tab2:
    with st.container(border=True, height=170):
      st.markdown("### 물리학")
      physics_list = ["사전 정의는 '자연 현상의 보편적 법칙을 연구하는 자연 과학의 한 분야'이다.",
                   "양자역학은 태어난 지 약 100년밖에 되지 않았다."
                  ]
      physics = random.choice(physics_list)
      st.caption(f"캡션: {physics}")
      st.link_button("물리 개념 정리(종료)_HS","https://docs.google.com/document/d/1Hq--M0r059_DK8DVi7FSDuMlbZuf3KcgYEyS9QVIAEM/edit?usp=sharing", use_container_width=True)
  with tab3:
    with st.container(border=True, height=170):
      st.markdown("### 화학")
      chemistry_list = ["사전 정의는 '물질의 성질과 구조, 그 생성과 분해의 반응 및 다른 물질과의 반응을 연구하는 학문'이다.",
                   "헬륨은 1기압에서 절대영도(0K)에서마저도 얼지 않는다."
                  ]
      chemistry = random.choice(chemistry_list)
      st.caption(f"캡션: {chemistry}")    
      st.link_button("화학 개념 정리(중단)_HS", "https://docs.google.com/document/d/1Vg_vugyvchkBi17DqHDL8o216NTWcLOQPBlHBj-R3_0/edit?usp=sharing", use_container_width=True)
  with tab4:
    with st.container(border=True, height=170):
      st.markdown("### 생명과학")
      biology_list = ["사전 정의는 '생명에 관계되는 현상을 종합적으로 연구하는 과학'이다.",
                   "사람의 미토콘드리아는 AUA를 개시코돈으로 사용하기도 한다."
                  ]
      biology = random.choice(biology_list)
      st.caption(f"캡션: {biology}")  
      st.link_button("생명과학 정리_HS", "https://docs.google.com/document/d/1D6qrxYU7jllv5jtnFGlxYAbMLa0rDQgcxoGWZU5P-pE/edit?usp=sharing", use_container_width=True)
      st.link_button("생물의 유전 '조건 X'문제", "https://docs.google.com/document/d/1re8tg8GgR0f39a1YsslOEHRyS_RaBKt93kwJ-D1uTHM/edit?usp=sharing", use_container_width=True)
  with tab5:
    with st.container(border=True, height=170):
      st.markdown("### 지구과학")
      earth_list = ["사전 정의는 '지구와 그 주위의 천체를 연구하는 학문'이다.",
                   "명왕성의 소행성체 번호는 134340이다."
                  ]
      earth = random.choice(earth_list)
      st.caption(f"캡션: {earth}")
      st.link_button("지구과학 정리_HS", "https://docs.google.com/document/d/1YOST6DnB_4Dr_jXNPWYKQ8C2EXSWMlUK6Q9_FuhP0Gk/edit?usp=sharing", use_container_width=True)
  with tab6:
    st.caption("아직 자료가 없습니다.")
  with tab7:
    with st.container(border=True, height=250):
      m1, m2, ph, ch, bio, ast, kr, s1, s2, en, pe, w, x = '대수(이도환)', '미적분I(김경민)', '전자기와 양자(송오준)', '화학반응의 세계(이병일)', '생물의 유전(김가인)', '행성우주과학(양경석)', '공통국어2(손창원)', '통합사회2(이수인)', '통합사회2(성현택)', '공통영어2(한수진)', '체육2(최현호)', '자율/창체', '.'
      def subject_time(a,b,c,d,e,f,g):
        n = 0
        list = [a,b,c,d,e,f,g]
        while n < 7:
          subject = list[n]
          n += 1
          st.caption(f'{n}교시: {subject}')
      with st.container(border=False):
        st.markdown('### 11월 09일 월요일')
        a, b, c = st.columns(3)
        with a:
          with st.expander('1-1 시간표'):
            subject_time(m1, m1, en, s1, m2, bio, ph)
        with b:
          with st.expander('1-2 시간표'):
            subject_time(ast, bio, ast, ch, m1, kr, m1)
        with c:
          with st.expander('1-3 시간표'):
            subject_time(m2, ast, ch, m1, ast, en, s1)
      with st.container(border=False):
        st.markdown('### 11월 10일 화요일')
        a, b, c = st.columns(3)
        with a:
          with st.expander('1-1 시간표'):
            subject_time(m1, bio, ch, ast, ast, kr, pe)
        with b:
          with st.expander('1-2 시간표'):
            subject_time(ast, pe, m1, m2, s1, ph, en)
        with c:
          with st.expander('1-3 시간표'):
            subject_time(ch, ast, ast, pe, kr, m1, m2)
      with st.container(border=False):
        st.markdown('### 11월 11일 수요일')
        a, b, c = st.columns(3)
        with a:
          with st.expander('1-1 시간표'):
            subject_time(m2, ast, ph, ast, m1, m1, s1)
        with b:
          with st.expander('1-2 시간표'):
            subject_time(ch, en, m1, bio, m2, ast, kr)
        with c:
          with st.expander('1-3 시간표'):
            subject_time(bio, ch, kr, m1, s1, m2, s2)
      with st.container(border=False):
        st.markdown('### 11월 12일 목요일')
        a, b, c = st.columns(3)
        with a:
          with st.expander('1-1 시간표'):
            subject_time(m1, kr, bio, en, ch, m2, ast)
        with b:
          with st.expander('1-2 시간표'):
            subject_time(bio, bio, kr, m2, ph, pe, ch)
        with c:
          with st.expander('1-3 시간표'):
            subject_time(ast, ph, m2, kr, bio, m1, pe)
      with st.container(border=False):
        st.markdown('### 11월 13일 금요일')
        a, b, c = st.columns(3)
        with a:
          with st.expander('1-1 시간표'):
            subject_time(w, ch, pe, m2, w, w, x)
        with b:
          with st.expander('1-2 시간표'):
            subject_time(w, ph, ast, m1, w, w, x)
        with c:
          with st.expander('1-3 시간표'):
            subject_time(w, m1, en, bio, w, w, x)
      with st.container(border=False):
        st.markdown('### 11월 16일 월요일')
        a, b, c = st.columns(3)
        with a:
          with st.expander('1-1 시간표'):
            subject_time(s2, s2, en, s1, m2, bio, ph)
        with b:
          with st.expander('1-2 시간표'):
            subject_time(ph, bio, ph, bio, en, m2, m2)
        with c:
          with st.expander('1-3 시간표'):
            subject_time(m2, ph, bio, en, ph, en, s1)
      with st.container(border=False):
        st.markdown('### 11월 17일 화요일')
        a, b, c = st.columns(3)
        with a:
          with st.expander('1-1 시간표'):
            subject_time(ph, bio, s1, ph, m2, kr, pe)
        with b:
          with st.expander('1-2 시간표'):
            subject_time(s2, s2, kr, m2, s1, m2, bio)
        with c:
          with st.expander('1-3 시간표'):
            subject_time(kr, m2, ph, pe, bio, ph, m2)
      with st.container(border=False):
        st.markdown('### 11월 18일 수요일')
        a, b, c = st.columns(3)
        with a:
          with st.expander('1-1 시간표'):
            subject_time(ph, kr, ph, kr, en, en, w)
        with b:
          with st.expander('1-2 시간표'):
            subject_time(pe, en, en, s2, ph, s1, w)
        with c:
          with st.expander('1-3 시간표'):
            subject_time(kr, s1, kr, ph, s1, ph, w)
      with st.container(border=False):
        st.markdown('### 11월 23일 월요일')
        a, b, c = st.columns(3)
        with a:
          with st.expander('1-1 시간표'):
            subject_time(m1, s2, en, s1, m2, bio, ph)
        with b:
          with st.expander('1-2 시간표'):
            subject_time(ast, ch, ph, ch, en, m1, m2)
        with c:
          with st.expander('1-3 시간표'):
            subject_time(m2, ph, ch, m1, ast, en, s1)
      with st.container(border=False):
        st.markdown('### 11월 10일 화요일')
        a, b, c = st.columns(3)
        with a:
          with st.expander('1-1 시간표'):
            subject_time(m1, bio, ch, ast, ph, kr, pe)
        with b:
          with st.expander('1-2 시간표'):
            subject_time(ch, pe, kr, m2, s1, bio, ph)
        with c:
          with st.expander('1-3 시간표'):
            subject_time(ph, ch, ast, pe, kr, m1, m2)
      with st.container(border=False):
        st.markdown('### 11월 25일 수요일')
        a, b, c = st.columns(3)
        with a:
          with st.expander('1-1 시간표'):
            subject_time(m2, kr, ph, ast, m1, en, ch)
        with b:
          with st.expander('1-2 시간표'):
            subject_time(ch, en, m1, bio, m2, ast, kr)
        with c:
          with st.expander('1-3 시간표'):
            subject_time(bio, ch, ch, ph, ch, m2, s2)
      with st.container(border=False):
        st.markdown('### 11월 26일 목요일')
        a, b, c = st.columns(3)
        with a:
          with st.expander('1-1 시간표'):
            subject_time(ph, kr, bio, en, ch, m2, ast)
        with b:
          with st.expander('1-2 시간표'):
            subject_time(en, s1, kr, m2, ph, pe, ch)
        with c:
          with st.expander('1-3 시간표'):
            subject_time(ast, ph, m2, m1, bio, en, pe)
      with st.container(border=False):
        st.markdown('### 11월 27일 금요일')
        a, b, c = st.columns(3)
        with a:
          with st.expander('1-1 시간표'):
            subject_time(w, ch, pe, m2, w, w, x)
        with b:
          with st.expander('1-2 시간표'):
            subject_time(w, ph, ast, m1, w, w, x)
        with c:
          with st.expander('1-3 시간표'):
            subject_time(w, kr, en, ch, w, w, x)
        
  
  with col_left:
    st.link_button("이메일 수신 동의/미동의", "https://docs.google.com/forms/d/e/1FAIpQLScJCCfpfFsHKUqPGoQ0PcNHRv3RysKb8nrVF4jmamunX3fHOA/viewform?usp=publish-editor")

  with col_right1:
    if st.button("익명 건의함"):
      st.session_state['page'] = 'suggest'
  with col_right2:
    if st.button("건의 내역"):
      st.session_state['page'] = 'suggest_record'

  taba,tabb,tabc, tabd = st.tabs(['1반 수행평가','2반 수행평가','3반 수행평가', '1학년 기말고사'])

  with taba:
    with st.expander('**대수** | 증명(11/23 월요일 1교시 예상)'):
      st.caption('문항 사전 공지 예정. 30~50개 중 반 별 랜덤으로 10개를 뽑아 증명.')
    with st.expander('**미적분1** | 도함수를 이용한 실생활 다항함수 모델링 및 방정식, 부등식 문제 제작 및 해결 (11/09 ~11/11 3차시)'):
      st.caption('실생활에서 나타나는 현상을 함수로 모델링하고 분석함.  \n도함수를 이용해 그래프 개형을 그림.  \n이를 통해 방정식, 부등식을 제작하고 해결하여 결론 도달  \n필요한 데이터는 미리 출력해오며, 전자기기 사용 불가')
    with st.expander('**전자기와 양자** | science snack project (11/12~11/18 예상)'):
      st.caption('제작 세 차시, 발표 두 차시.  \n해당 주는 수업 교체로 인해 전자기와 양자 수업이 많아질 예정')
    with st.expander('**화학 반응의 세계** | 산 염기 중화 적정 보고서(~기말 이후)'):
      st.caption("보고서로 인한 변별은 거의 없음. 썼냐 안 썼냐 정도로 판단하나 고찰 파트는 생기부에 참고되므로 유의.")
    with st.expander('**화학 반응의 세계** | 탄소 화합물 구조 제안서(날짜 미정)'):
      st.caption("어떤 문제에 도움이 되는 탄소 화합물 구조를 만들어 제안서를 작성함.  \n논문 자료를 종합한 후, AI에게 '이러한 문제를 해결할 수 있는 탄소화합물을 설계해줘' 식의 프롬포트 작성.  \n사전 논문을 얼마나 때려박냐에 따라 정확도, 가치 달라짐")
    with st.expander('**생물의 유전** | 질문 노트(진행중 - 심층탐구)'):
      st.caption('심층탐구 보고서 마감: 11/23 (월)  \n1차시: 평가 안내 및 작성했던 질문노트에서 주제 찾기  \n2차시: 개별 탐구  \n3차시: 보고서 작성  \n4차시: 발표 준비  \n5~8자리: 발표 진행')
    with st.expander('**행성우주과학** | 보고서'):
      st.caption('공지된 내용이 없습니다.')
    with st.expander('**통합사회2** | 생애 주기별 금융 생활 설계'):
      st.caption('내용: 여러가지 거시적인 사건 변화들을 보고, 생애 주기에 따라 금융 생활을 설계')
    with st.expander('**공통영어2** | 말하기(11/09 월요일)'):
      st.caption('내용: 제시된 두 그림에서 다른 부분을 짝과 함께 영어로 추론.')

  with tabb:
    with st.expander('**대수** | 증명(날짜 미정)'):
      st.caption('문항 사전 공지 예정. 30~50개 중 반 별 랜덤으로 10개를 뽑아 증명.')
    with st.expander('**미적분1** | 도함수를 이용한 실생활 다항함수 모델링 및 방정식, 부등식 문제 제작 및 해결(11/09 ~11/11 3차시)'):
      st.caption('실생활에서 나타나는 현상을 함수로 모델링하고 분석함.  \n도함수를 이용해 그래프 개형을 그림.  \n이를 통해 방정식, 부등식을 제작하고 해결하여 결론 도달  \n필요한 데이터는 미리 출력해오며, 전자기기 사용 불가')
    with st.expander('**전자기와 양자** | science snack project (11/16~11/18 예상)'):
      st.caption('제작 세 차시, 발표 두 차시.  \n해당 주는 수업 교체로 인해 전자기와 양자 수업이 많아질 예정')
    with st.expander('**화학 반응의 세계** | 산 염기 중화 적정 보고서(~기말 이후)'):
      st.caption("보고서로 인한 변별은 거의 없음. 썼냐 안 썼냐 정도로 판단하나 고찰 파트는 생기부에 참고되므로 유의.")
    with st.expander('**화학 반응의 세계** | 탄소 화합물 구조 제안서(날짜 미정)'):
      st.caption("어떤 문제에 도움이 되는 탄소 화합물 구조를 만들어 제안서를 작성함.  \n논문 자료를 종합한 후, AI에게 '이러한 문제를 해결할 수 있는 탄소화합물을 설계해줘' 식의 프롬포트 작성.  \n사전 논문을 얼마나 때려박냐에 따라 정확도, 가치 달라짐")
    with st.expander('**생물의 유전** | 질문 노트(진행중 - 심층탐구)'):
      st.caption('심층탐구 보고서 마감: 11/23 (월)  \n1차시: 평가 안내 및 작성했던 질문노트에서 주제 찾기  \n2차시: 개별 탐구  \n3차시: 보고서 작성  \n4차시: 발표 준비  \n5~8자리: 발표 진행')
    with st.expander('**행성우주과학** | 보고서'):
      st.caption('공지된 내용이 없습니다.')
    with st.expander('**통합사회2** | 생애 주기별 금융 생활 설계'):
      st.caption('내용: 여러가지 거시적인 사건 변화들을 보고, 생애 주기에 따라 금융 생활을 설계')
    with st.expander('**공통영어2** | 말하기(11/09 월요일)'):
      st.caption('내용: 제시된 두 그림에서 다른 부분을 짝과 함께 영어로 추론.')

  with tabc:
    with st.expander('**대수** | 증명(날짜 미정)'):
      st.caption('문항 사전 공지 예정. 30~50개 중 반 별 랜덤으로 10개를 뽑아 증명.')
    with st.expander('**미적분1** | 도함수를 이용한 실생활 다항함수 모델링 및 방정식, 부등식 문제 제작 및 해결(11/09 ~11/11 3차시)'):
      st.caption('실생활에서 나타나는 현상을 함수로 모델링하고 분석함.  \n도함수를 이용해 그래프 개형을 그림.  \n이를 통해 방정식, 부등식을 제작하고 해결하여 결론 도달  \n필요한 데이터는 미리 출력해오며, 전자기기 사용 불가')
    with st.expander('**전자기와 양자** | science snack project (11/16~11/18 예상)'):
      st.caption('제작 세 차시, 발표 두 차시.  \n해당 주는 수업 교체로 인해 전자기와 양자 수업이 많아질 예정')
    with st.expander('**화학 반응의 세계** | 산 염기 중화 적정 보고서(~기말 이후)'):
      st.caption("보고서로 인한 변별은 거의 없음. 썼냐 안 썼냐 정도로 판단하나 고찰 파트는 생기부에 참고되므로 유의.")
    with st.expander('**화학 반응의 세계** | 탄소 화합물 구조 제안서(날짜 미정)'):
      st.caption("어떤 문제에 도움이 되는 탄소 화합물 구조를 만들어 제안서를 작성함.  \n논문 자료를 종합한 후, AI에게 '이러한 문제를 해결할 수 있는 탄소화합물을 설계해줘' 식의 프롬포트 작성.  \n사전 논문을 얼마나 때려박냐에 따라 정확도, 가치 달라짐")
    with st.expander('**생물의 유전** | 질문 노트(진행중 - 심층탐구)'):
      st.caption('심층탐구 보고서 마감: 11/23 (월)  \n1차시: 평가 안내 및 작성했던 질문노트에서 주제 찾기  \n2차시: 개별 탐구  \n3차시: 보고서 작성  \n4차시: 발표 준비  \n5~8자리: 발표 진행')
    with st.expander('**행성우주과학** | 보고서'):
      st.caption('공지된 내용이 없습니다.')
    with st.expander('**통합사회2** | 생애 주기별 금융 생활 설계'):
      st.caption('내용: 여러가지 거시적인 사건 변화들을 보고, 생애 주기에 따라 금융 생활을 설계')
    with st.expander('**공통영어2** | 말하기(11/09 월요일)'):
      st.caption('내용: 제시된 두 그림에서 다른 부분을 짝과 함께 영어로 추론.')

  with tabd:
    with st.expander('**대수** | 11. 사인 법칙과 코사인 법칙 ~ 16. 수학적 귀납법 + 학습지'):
      st.caption("삼각함수의 활용 학습지 끝자락에 있던 '삼각함수의 미분'과 arcsin은 미포함")
    with st.expander('**미적분1** | 3. 함수의 미분 ~ 13. 속도 - 거리와 적분 + 학습지'):
      st.caption("정확히는 미분 전체 ~ 적분 전체 + 학습지")
    with st.expander('**전자기와 양자** | Chapter 34 빛의 본질과 광선 광학의 원리 ~ Chapter 42 핵물리학'):
      st.caption("단, Chapter 38 상대성이론은 제외")
    with st.expander('**화학 반응의 세계** | 11. 산화 환원 ~ 15. 유기화학3'):
      st.caption("-")
    with st.expander('**생물의 유전** | 연습문제 + 중간고사 범위 일부 + 원핵생물의 전사 조절 ~ 3. 생명공학기술'):
      st.caption("일단 중간 고사 이후 범위부터 공부하다가, 나중에 알려주는 범위 받기.")
    with st.expander('**행성우주과학** | 별의 질량 ~ 우주의 거대 구조'):
      st.caption("-")
    with st.expander('**공통국어2** | 교과서 3단원 ~ 5단원'):
      st.caption("-")
    with st.expander('**통합사회2** | III 시장경제와 지속가능발전 3. 금융 자산과 금융 관리 ~ V. 미래와 지속가능한 삶'):
      st.caption("-")
    with st.expander('**공통영어2** | 2025학년도 10월 고1 영어 모의고사 + 2026학년도 10월 고1 영어 모의고사 + 수업 프린트'):
      st.caption("지문 범위는 11/02 ~ 11/06 중으로 배부.")

  
  text, _, button = st.columns([2, 7, 2])
  with text:
    code = st.text_input("secret code: ")
    if st.button("코드 확인"):
      if code == "34studyLewis":
        st.session_state['page'] = 'developer'
        st.rerun()
      elif code.lower() == "tmi":
        tmi_list = [
          "개발자 tmi: 개발자의 mbti는 INTP이다.",
          "개발자 tmi: 개발자의 최애 밴드는 실리카겔이고, 앨범 중 'POWER ANDRE 99'을 가장 많이 듣는다.",
          "개발자 tmi: 개발자가 과학을 좋아하게 된 계기는 초등학교 5학년 때 읽은 '내일은 실험왕'이다.",
          "개발자 tmi: 개발자는 입학 전 타자가 250타였으나, 수업 중 필기로 인해 현재 400타까지 상승하였다.",
          "개발자 tmi: 개발자의 고향은 구미이다.",
          "개발자 tmi: 개발자는 10월 27일에 올라온 건의를 10월 31일에야 읽는 실수를 저지르고 곧바로 개발자 공간을 제작하였다.",
          "개발자 tmi: 개발자의 롤 주챔은 아펠리오스이다.",
          "개발자 tmi: 개발자의 고양이 이름은 '루이(Louis)'이고, 강아지 이름은 '봄이'이다.",
          "개발자 tmi: 개발자의 중학교 시절 꿈은 작가였고, 아직도 가끔 글을 쓴다.",
          "개발자 tmi: 개발자는 이 학교에서 지금까지 서서 수업을 들은 시간이 앉아서 들은 시간보다 많을 것으로 추정된다."
          "개발자 tmi: 개발자는 공통수학과 화학1만 선행학습한 채 과고에 입학하였다. 지금도 예습은 미적분1만 하는 편이다.",
          "개발자 tmi: 개발자는 물리학자가 꿈임에도 불구하고, 최고 등수 12등으로 아직까지 1등급을 달성하지 못하였다.",
          "개발자 tmi: 개발자 tmi은 주로 자습시간에(...) 작성된다.",
          "개발자 tmi: 개발자는 해당 사이트를 다른 기수 영역까지 확장할 생각이 있다.",
          "개발자 tmi: 개발자는 중학교 시절 늦잠으로 10시에 등교해본 적이 있다."
        ]
        tmi = random.choice(tmi_list)
        st.toast(tmi)
      elif code.lower() == "blackjack":
        st.session_state['page'] = 'blackjack'
      elif code == "":
        st.toast("코드를 입력해주세요.")
      else:
        st.toast("코드가 올바르지 않습니다.")
  with button:
    st.button("새로고침")

def show_suggest_page():

  st.title("**34기 학술 자료 사이트_HS**")
  form_url = "https://docs.google.com/forms/d/e/1FAIpQLScF0MI3NHn3m5OjOc2kEqYym0QDoOl_mscj1Hj4SVJkGDPjYg/viewform?embedded=true"
  st.components.v1.iframe(form_url, height=425, scrolling=True)
  
  
  if st.button("돌아가기"):
    st.session_state['page'] = 'main'
    st.rerun()

def show_suggest_record_page():
  st.title("**34기 학술 자료 사이트_HS**")
  tabr, tabrr = st.tabs(['미완료 건의 내역', '검토중인 건의'])
  with tabr:
    st.write("미완료된 건의가 없습니다.")
    st.caption("모든 건의가 해결되었거나, 아직 검토되지 않았을 수 있습니다!")
  with tabrr:
    st.write("검토중인 건의가 없습니다.")
    st.caption("모든 건의가 검토되었거나, 아직 확인되지 않았을 수 있습니다!")

  ehfdkrkrl, tofhrhcla = st.columns(2)
  with ehfdkrkrl:
    if st.button("돌아가기"):
      st.session_state['page'] = 'main'
      st.rerun()
  with tofhrhcla:
    st.button("새로고침")
    
def show_developer_space_page():
  @st.fragment(run_every="30s")
  def show_sheets():
  
    st.write("익명 건의함") 

    url = "https://docs.google.com/spreadsheets/d/10Am-n7ydEK83sTMaaFWuY4b87KICdL9jqZvJwXbItvE/export?format=csv&gid=335439914"
    df = pd.read_csv(url)
    st.dataframe(df, 
                 use_container_width=True,
                 hide_index=True,
                 column_config={
                   "건의 내용 작성": st.column_config.TextColumn("건의 내용 작성", width="large")
                 }
                )

    st.write("이메일 수신 동의")
  
    url = "https://docs.google.com/spreadsheets/d/1noxPR0LvBGnHJ3Ka-MQbWoh5bVIx4D8mKLSLOjuKc2E/export?format=csv&gid=1596480109"
    df = pd.read_csv(url)
    st.dataframe(df.iloc[:, 1:], 
                 use_container_width=True,
                 hide_index=True,
                 column_config={
                   "아메일 주소": st.column_config.TextColumn("이메일 주소", width="large")
                 }
                )
  show_sheets()

  eh, to = st.columns(2)
  with to:
    st.button("새로고침")
  with eh:
    if st.button("돌아가기"):
      st.session_state['page'] = 'main'
      st.rerun()

def show_blackjack():
  st.title("이스터에그: 블랙잭")
  st.write("가진 카드의 합이 21을 넘지 않으면서 딜러보다 21에 더 가까이 만들면 승리하는 게임입니다.")
  st.caption("개발자가 코딩하기 귀찮은 관계로 간소화된 룰을 적용합니다.")
  st.caption("코딩의 편의를 위해 항상 A 카드는 맨 뒤에 배치됩니다.")
  with st.expander("룰 설명"):
    st.write("1. 플레이어와 딜러가 각각 카드를 두 장씩 받습니다(Dealing). 이때, 딜러의 두번째 카드는 비공개합니다.")
    st.write("2. 플레이어는 자신의 카드를 보고 카드를 더 받을 지(Hit), 차례를 마칠 지(Stay) 결정합니다.")
    st.caption("이때, A는 1또는 11 중 플레이어에게 유리한 수로, K Q J는 10으로 적용합니다.")
    st.caption("만일 플레이어의 첫 패가 A와 10(10, K, Q, J)일 경우 곧바로 21이 되어 승리하며, 이 패를 '블랙잭'이라고 합니다.")
    st.caption("블랙잭으로 승리할 경우 최종 승률 계산에서 1.5회 승리로 간주합니다.")
    st.caption("현재 숫자가 21을 넘지(Bust)않는 이상, 원하는 만큼 카드를 더 받을 수 있습니다.")
    st.write("3.차례가 끝나고 카드의 수를 합산한 결과, 21을 넘을 경우 딜러의 패에 관계없이 반드시 패배합니다.")
    st.write("4.차례가 끝난 후 21을 넘지 않았다면 딜러가 카드를 받으며, 이때 딜러가 버스트하거나 플레이어의 총합이 딜러의 총합보다 21에 더 가까우면 플레이어가 승리합니다.")
    st.caption("딜러는 16 이하에서 무조건 히트, 17 이상에서 스테이합니다.")
    st.caption("버스트되지 않는 한, 딜러의 A 카드는 11로 계산합니다.")
    st.write("5. 서렌더(Surrender)는 플레이어가 딜링 단계일 때만 가능합니다.")
    st.caption("서렌더는 최종 승률 계산에서 0.5회 패배로 간주합니다.")
  deck =  ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
  if 'dealer' not in st.session_state:
    st.session_state['dealer'] = {'card':[], 'sum':0, 'state':None}
  if 'player' not in st.session_state:
    st.session_state['player'] = {'card':[], 'sum':0, 'state':None}
  if 'rate' not in st.session_state:
    st.session_state['rate'] = {'match':0, 'win':0, 'blackjack':0, 'push':0, 'lose':0, 'surrender':0}
  def sumcard(subject):
    st.session_state[subject]['sum'] = 0
    st.session_state[subject]['card'].sort(key=lambda x: x == 'A')
    A_count = st.session_state[subject]['card'].count('A')
    for card in st.session_state[subject]['card']:
      if card == 'K' or card == 'Q' or card == 'J':
        st.session_state[subject]['sum'] += 10
      elif isinstance(card, int):
        st.session_state[subject]['sum'] += card
      elif card == 'A':
        if st.session_state[subject]['sum'] <= (11 - A_count):
          st.session_state[subject]['sum'] += 11
        elif st.session_state[subject]['sum'] > (11 - A_count):
          st.session_state[subject]['sum'] += 1
        A_count -= 1
  def judgement():
    if st.session_state['player']['sum'] > 21:
      st.session_state['player']['state'] = '버스트(패배)'
      st.session_state['dealer']['state'] = '승리'
      st.session_state['rate']['lose'] +=1
      st.session_state['rate']['match'] +=1
    elif st.session_state['dealer']['sum'] > 21:
      st.session_state['dealer']['state'] = '버스트(패배)'
      st.session_state['player']['state'] = '승리'
      st.session_state['rate']['win'] +=1
      st.session_state['rate']['match'] +=1
    elif st.session_state['player']['sum'] > st.session_state['dealer']['sum']:
      st.session_state['dealer']['state'] = '패배'
      st.session_state['player']['state'] = '승리'
      st.session_state['rate']['win'] +=1
      st.session_state['rate']['match'] +=1
    elif st.session_state['player']['sum'] < st.session_state['dealer']['sum']:
      st.session_state['dealer']['state'] = '승리'
      st.session_state['player']['state'] = '패배'
      st.session_state['rate']['lose'] +=1
      st.session_state['rate']['match'] +=1
    elif st.session_state['player']['sum'] == st.session_state['dealer']['sum']:
      st.session_state['dealer']['state'] = '무승부'
      st.session_state['player']['state'] = '무승부'
      st.session_state['rate']['push'] +=1
      st.session_state['rate']['match'] +=1
  
  with st.container(border=True):
    st.markdown('### 딜러')
    st.caption(f'상태: {st.session_state['dealer']['state']}')
    st.write(f"현재 패: {st.session_state['dealer']['card']}")
  with st.container(border=True):
    st.markdown('### 플레이어')
    st.caption(f'상태: {st.session_state['player']['state']}')
    st.write(f"현재 패: {st.session_state['player']['card']}")
    if st.session_state['dealer']['state'] == None:
      if st.button('딜링', use_container_width=True):
        st.session_state['dealer']['state'] = '딜링'
        st.session_state['player']['state'] = '딜링' 
        st.session_state['dealer']['card'].append(random.choice(deck))
        st.session_state['dealer']['card'].append('?')
        st.session_state['player']['card'].append(random.choice(deck))
        st.session_state['player']['card'].append(random.choice(deck))
        sumcard('player')
        if st.session_state['player']['sum'] == 21:
          st.session_state['player']['state'] = '블랙잭!'
          st.session_state['dealer']['state'] = '패배'
          st.session_state['rate']['win'] +=1
          st.session_state['rate']['blackjack'] +=1
          st.session_state['rate']['match'] +=1
        st.rerun()
    if st.session_state['dealer']['state'] == '딜링' and st.session_state['player']['state'] != '스테이':
      hit, stay = st.columns(2)
      with hit:
        if st.button('히트', use_container_width=True):
          st.session_state['player']['state'] = '히트'
          st.session_state['player']['card'].append(random.choice(deck))
          sumcard('player')
          if st.session_state['player']['sum'] > 21:
            st.session_state['player']['state'] = '버스트(패배)'
            st.session_state['dealer']['state'] = '승리'
            st.session_state['rate']['lose'] += 1
            st.session_state['rate']['match'] += 1
            st.rerun()
          else:
            st.rerun()
      with stay:
        if st.button('스테이', use_container_width=True):
          st.session_state['player']['state'] = '스테이'
          st.rerun()
    if st.session_state['player']['state'] == '스테이':
        st.session_state['dealer']['state'] = '히트'
        st.session_state['dealer']['card'].remove('?')
        st.session_state['dealer']['card'].append(random.choice(deck))
        sumcard('dealer')
        if st.session_state['dealer']['sum'] == 21:
            st.session_state['dealer']['state'] = '블랙잭!'
            st.session_state['player']['state'] = '패배'
            st.session_state['rate']['lose'] +=1
            st.session_state['rate']['match'] +=1
        else:
          while st.session_state['dealer']['sum'] < 17:
            st.session_state['dealer']['card'].append(random.choice(deck))
            sumcard('dealer')
          judgement()
        st.rerun()
    

  rerun, clear = st.columns(2)
  with rerun:
    if st.button("돌아가기"):
        st.session_state['page'] = 'main'
        st.rerun()
  with clear:
    if st.session_state['player']['state'] == '승리' or st.session_state['player']['state'] == '패배' or st.session_state['dealer']['state'] == '승리' or st.session_state['dealer']['state'] == '패배' or st.session_state['player']['state'] == None or st.session_state['dealer']['state'] == None or st.session_state['player']['state'] == '무승부' or st.session_state['dealer']['state'] == '무승부':
      if st.button("게임 초기화"):
        st.session_state['dealer'] = {'card':[], 'sum':0, 'state':None}
        st.session_state['player'] = {'card':[], 'sum':0, 'state':None}
        st.rerun()
    elif st.session_state['player']['state'] == '딜링':
      if st.button("서렌더"):
        st.session_state['dealer'] = {'card':[], 'sum':0, 'state':None}
        st.session_state['player'] = {'card':[], 'sum':0, 'state':None}
        st.session_state['rate']['lose'] +=1
        st.session_state['rate']['surrender'] +=1
        st.session_state['rate']['match'] +=1
        st.rerun()
  win = st.session_state['rate']['win']
  blackjack = st.session_state['rate']['blackjack']
  push = st.session_state['rate']['push']
  lose = st.session_state['rate']['lose']
  surrender = st.session_state['rate']['surrender']
  match = st.session_state['rate']['match']
  match2 = (win - blackjack) + 1.5 * blackjack + push + (lose - surrender) + 0.5 * surrender
  if match2 == 0:
    rate = 0
  else:
    rate = (((win - blackjack) + 1.5 * blackjack + push/2) / match2) * 100
  st.write(f"현재 승률:{rate: .2f}% ({match}전 {win}승 {push}무 {lose}패) // 블랙잭: {blackjack}회, 서렌더: {surrender}회")
  st.caption("이 페이지를 나가면 승률이 초기화됩니다.")
      
if st.session_state['page'] == 'main':
    show_main_page()
elif st.session_state['page'] == 'suggest':
    show_suggest_page()
elif st.session_state['page'] == 'suggest_record':
    show_suggest_record_page()
elif st.session_state['page'] == 'developer':
    show_developer_space_page()
elif st.session_state['page'] == 'blackjack':
    show_blackjack()

import streamlit as st

# 1. 페이지 기본 설정 (타이틀과 아이콘만 깔끔하게 설정)
st.set_page_config(page_title="Music Mate", page_icon="🎧")

st.title("🎧 Music Mate 찾기")
st.subheader("지금 끌리는 음악 장르를 골라보세요!")
st.caption("최소 1개 이상 선택하면 나와 취향이 맞는 메이트를 추천해 드려요.")

# 2. 제공할 음악 장르 리스트
genres = ['인디 밴드', '힙합/랩', '시티팝', '재즈', 'K-POP', 'R&B', '클래식', '로파이(Lo-Fi)']

# 유저가 다중 선택할 수 있는 셀렉트 박스
selected_genres = st.multiselect("나의 선호 장르 선택:", genres)

# 3. 가상의 매칭 유저 데이터
dummy_mates = [
    {'name': '음악덕후99', 'match_rate': '95%', 'genres': '시티팝, 로파이', 'song': 'Plastic Love'},
    {'name': '재즈가좋아', 'match_rate': '88%', 'genres': '재즈, R&B', 'song': 'Fly Me To The Moon'},
    {'name': '비트메이커', 'match_rate': '82%', 'genres': '힙합/랩, R&B', 'song': 'Bad Guy'},
]

st.write("---")

# 4. 매칭 시작 버튼
if st.button("나와 닮은 음악 메이트 찾기"):
    if not selected_genres:
        st.warning("⚠️ 최소 하나의 장르를 선택해 주세요!")
    else:
        st.success("🎵 당신과 취향이 통하는 메이트를 찾았습니다!")
        
        # 매칭된 유저들을 리스트 형태로 출력
        for mate in dummy_mates:
            col1, col2 = st.columns([1, 3])
            with col1:
                # 일치율을 멋진 숫자로 표시
                st.metric(label="일치율", value=mate['match_rate'])
            with col2:
                st.markdown(f"### 👤 {mate['name']}")
                st.write(f"**선호 장르:** {mate['genres']}")
                st.write(f"**🎧 지금 듣는 곡:** {mate['song']}")
            
            # 간단한 안내 메시지 분기 (버튼 클릭 처리)
            # 각 버튼이 고유한 ID를 갖도록 key를 지정해 줍니다.
            if st.button(f"💬 {mate['name']}님과 채팅 시작하기", key=f"chat_{mate['name']}"):
                st.info(f"{mate['name']}님과의 대화방을 개설하는 중입니다...")
                
            st.write("---")

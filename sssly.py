import streamlit as st

# 1. 페이지 기본 설정 및 다크 테마 감성 입히기
st.set_page_config(page_title="Music Mate", page_icon="🎧", layout="centered")

# 간단한 스타일 커스텀 (CSS)
st.markdown("""
    <style>
    .main { background-color: #121212; color: white; }
    .stButton>button { background-color: #BB86FC; color: white; width: 100%; border-radius: 10px; }
    </style>
    """, unsafe_allow_index=True)

st.title("🎧 Music Mate 찾기")
st.subheader("지금 끌리는 음악 장르를 골라보세요!")
st.caption("최소 1개 이상 선택하면 나와 취향이 맞는 메이트를 추천해 드려요.")

# 2. 제공할 음악 장르 리스트
genres = ['인디 밴드', '힙합/랩', '시티팝', '재즈', 'K-POP', 'R&B', '클래식', '로파이(Lo-Fi)']

# 유저가 다중 선택할 수 있는 셀렉트 박스
selected_genres = st.multiselect("나의 선호 장르 선택:", genres)

# 3. 가상의 매칭 유저 데이터 (데이터베이스 역할)
dummy_mates = [
    {'name': '음악덕후99', 'match_rate': '95%', 'genres': '시티팝, 로파이', 'song': 'Plastic Love'},
    {'name': '재즈가좋아', 'match_rate': '88%', 'genres': '재즈, R&B', 'song': 'Fly Me To The Moon'},
    {'name': '비트메이커', 'match_rate': '82%', 'genres': '힙합/랩, R&B', 'song': 'Bad Guy'},
]

st.write("---")

# 4. 매칭 버튼 및 결과 출력
if st.button("나와 닮은 음악 메이트 찾기"):
    if not selected_genres:
        st.warning("⚠️ 최소 하나의 장르를 선택해 주세요!")
    else:
        st.success("🎵 당신과 취향이 통하는 메이트를 찾았습니다!")
        
        # 매칭된 유저들을 카드 형태로 출력
        for mate in dummy_mates:
            with st.container():
                col1, col2 = st.columns([1, 4])
                with col1:
                    # 매칭률 표시
                    st.metric(label="일치율", value=mate['match_rate'])
                with col2:
                    st.markdown(f"### 👤 {mate['name']}")
                    st.text(f"선호 장르: {mate['genres']}")
                    st.text(f"🎧 지금 듣는 곡: {mate['song']}")
                
                # 대화하기 버튼
                if st.button(f"{mate['name']}님과 채팅하기", key=mate['name']):
                    st.info(f"💬 {mate['name']}님과의 채팅방으로 연결을 시도합니다...")
                st.write("---")

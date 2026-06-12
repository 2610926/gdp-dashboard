import streamlit as st
import time

# 1. 앱 제목 설정
st.title("🎮 게임 시간 알리미")

# 알림을 줄 시간 리스트
notice = [30, 15, 0]

# 2. 사용자 입력 받기 (st.number_input 사용)
# min_value=0을 주어 음수 입력 방지, step=1로 1분 단위 조절
game_time = st.number_input("게임시간입력 (분):", min_value=0, value=35, step=1)

# 3. '실행' 버튼 생성
if st.button("타이머 시작"):
    st.write("---")
    st.subheader("진행 결과")
    
    # 결과를 보여줄 빈 공간(placeholder) 생성
    result_area = st.empty()
    
    # 입력받은 시간을 current_time 변수에 할당하여 카운트다운 진행
    current_time = game_time
    
    while current_time >= 0:
        if current_time in notice:
            # st.info()를 사용해 알림 메시지를 깔끔하게 표시
            st.info(f"⏳ {current_time}분 남았습니다")
            
            # 시간이 0이 되면 컴퓨터 종료 메시지 출력
            if current_time == 0:
                st.error("🛑 컴퓨터가 종료됩니다")
        
        # 시간 감소 (들여쓰기를 if문 밖으로 빼서 정상적으로 카운트다운 되도록 수정)
        current_time -= 1
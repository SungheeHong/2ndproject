import streamlit as st
import pandas as pd

# 제목
st.title("📈 주식 데이터 시각화")

# 샘플 데이터
data = {
    "종목명": ["삼성전자", "LG화학", "카카오"],
    "현재가": [75000, 820000, 64000],
    "변동률": [0.5, -1.2, 2.3]
}

# 오류 발생 지점 수정 완료
price_df = pd.DataFrame(data)

# 표 출력
st.subheader("📊 주식 가격 데이터")
st.dataframe(price_df)

# 차트 출력
st.subheader("📉 가격 변동률 차트")
st.bar_chart(price_df.set_index("종목명")["변동률"])

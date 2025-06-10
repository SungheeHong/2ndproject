import streamlit as st
import yfinance as yf
import pandas as pd
import datetime
import matplotlib.pyplot as plt

st.title("🌎 글로벌 시총 TOP 10 기업 - 최근 3년 주가 변화")

# 기업 리스트
companies = {
    "Apple": "AAPL",
    "Microsoft": "MSFT",
    "Saudi Aramco": "2222.SR",
    "Alphabet (Google)": "GOOGL",
    "Amazon": "AMZN",
    "NVIDIA": "NVDA",
    "Berkshire Hathaway": "BRK-B",
    "Meta": "META",
    "TSMC": "TSM",
    "Tesla": "TSLA"
}

# 날짜 설정
end_date = datetime.date.today()
start_date = end_date - datetime.timedelta(days=3*365)

# 데이터 다운로드
st.write("데이터 불러오는 중...")
data = {}
for name, ticker in companies.items():
    df = yf.download(ticker, start=start_date, end=end_date)
    data[name] = df["Close"]

# 데이터프레임 결합
price_df = pd.DataFrame(data)

# 그래프
st.subheader("📈 주가 변화 그래프 (종가 기준)")
st.line_chart(price_df)

# 선택한 기업만 보고 싶을 때
st.subheader("🔍 선택한 기업 보기")
selected = st.multiselect("기업을 선택하세요", list(companies.keys()), default=["Apple", "Microsoft"])
if selected:
    st.line_chart(price_df[selected])

import streamlit as st
import folium
from streamlit_folium import st_folium

# 평균 기온이 가장 높은 5개 도시 데이터
hot_cities = [
    {
        "name": "쿠웨이트시티",
        "country": "쿠웨이트",
        "location": (29.3759, 47.9774),
        "avg_temp": 32.1, # 최근 10년간 연평균(°C)
        "description": (
            "쿠웨이트시티는 중동 지역의 대표적인 고온 도시로, 여름철에는 일 최고기온이 50°C를 넘나들기도 합니다. "
            "최근 10년간 연평균 기온은 약 32°C로, 지구에서 가장 더운 도시 중 하나로 꼽힙니다. "
            "현대적인 도시 풍경과 고대 이슬람 문화의 조화가 인상적이며, 대표 관광지로 쿠웨이트 타워, 대모스크, "
            "해변 산책로 등이 있습니다. 한여름에는 외출 시 자외선 차단과 수분 섭취에 각별한 주의가 필요합니다."
        )
    },
    {
        "name": "바스라",
        "country": "이라크",
        "location": (30.5085, 47.7804),
        "avg_temp": 31.8,
        "description": (
            "이라크 남부의 항구 도시 바스라는 최근 10년간 31.8°C의 높은 연평균 기온을 기록하고 있습니다. "
            "여름은 극도로 덥고 건조하며, 일교차도 큽니다. 바스라는 유프라테스와 티그리스 강 하구에 위치해 있어 "
            "고대 문명의 흔적과 현대 산업도시의 모습을 동시에 볼 수 있습니다. 방문 시에는 강변 산책, 시장 탐방, "
            "지역 전통 요리 체험 등을 추천하지만, 혹서기에는 실내 관광을 권장합니다."
        )
    },
    {
        "name": "도하",
        "country": "카타르",
        "location": (25.2854, 51.5310),
        "avg_temp": 31.4,
        "description": (
            "카타르의 수도 도하는 아라비아 반도의 중심에 위치하여, 최근 10년간 평균 31.4°C의 고온을 보이고 있습니다. "
            "도하는 현대적인 건축물과 전통 시장이 어우러져 있으며, 이슬람 미술관, 수크 와키프, 인공섬 더 펄 등을 "
            "둘러볼 수 있습니다. 여름철은 매우 덥고 습도가 높으며, 실내 관광과 야간 활동이 활발합니다."
        )
    },
    {
        "name": "리야드",
        "country": "사우디아라비아",
        "location": (24.7136, 46.6753),
        "avg_temp": 30.6,
        "description": (
            "사우디아라비아의 수도 리야드는 최근 10년간 연평균 30.6°C로 매우 높은 기온을 기록하고 있습니다. "
            "도시 곳곳에 초현대적 건축물과 대형 쇼핑몰, 고대 유적지가 공존합니다. 대표 명소로는 킹덤 센터, "
            "마스마크 요새, 국립박물관 등이 있습니다. 건기와 혹서기가 뚜렷하므로 방문 시 계절에 따른 준비가 필요합니다."
        )
    },
    {
        "name": "피닉스",
        "country": "미국 애리조나주",
        "location": (33.4484, -112.0740),
        "avg_temp": 29.9,
        "description": (
            "피닉스는 미국 대도시 중 최상위 수준의 평균 기온을 자랑하며, 최근 10년간 약 29.9°C의 연평균 기온을 기록했습니다. "
            "사막성 기후로, 여름 낮 최고기온이 45°C를 넘기도 합니다. 피닉스 주변에는 사구와 선인장이 펼쳐진 소노란 사막, "
            "뮤지엄, 리조트, 야외 액티비티 등이 많아 자연과 레저를 동시에 즐길 수 있습니다. 자외선 차단, 충분한 음료 섭취 등 "
            "건강 관리가 매우 중요합니다."
        )
    }
]

city_names = [f"{city['name']} ({city['country']})" for city in hot_cities]

st.title("지구에서 가장 뜨거운 도시 가이드 🌞")
st.markdown(
    """
    최근 10년간(2015~2024) 평균 기온이 가장 높은 도시 5곳을 선정했습니다.
    도시를 선택하면 상세 정보와 위치를 확인할 수 있습니다.
    """
)

# 도시 선택
selected_city_name = st.selectbox("도시를 선택하세요:", city_names)
selected_city = next(city for city in hot_cities if f"{city['name']} ({city['country']})" == selected_city_name)

# 폴리움 지도 생성 및 마커 표시
city_map = folium.Map(location=selected_city["location"], zoom_start=8, tiles="cartodbpositron")
for city in hot_cities:
    color = "red" if city["name"] == selected_city["name"] else "gray"
    icon = "fire" if city["name"] == selected_city["name"] else "info-sign"
    folium.Marker(
        location=city["location"],
        tooltip=f"{city['name']} ({city['country']})",
        icon=folium.Icon(color=color, icon=icon)
    ).add_to(city_map)

st.subheader("🗺️ 도시 위치 지도")
st_folium(city_map, width=700, height=450)

st.subheader("🌡️ 도시 상세 정보")
st.markdown(f"### {selected_city['name']} ({selected_city['country']})")
st.markdown(f"**최근 10년간 연평균 기온:** {selected_city['avg_temp']}°C")
st.write(selected_city["description"])


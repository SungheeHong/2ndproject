import streamlit as st
import folium
from streamlit_folium import st_folium

# 관광지 데이터 정의
tourist_spots = [
    {
        "name": "사그라다 파밀리아",
        "city": "바르셀로나",
        "location": (41.4036, 2.1744),
        "description": (
            "안토니 가우디의 대표작인 사그라다 파밀리아는 스페인을 대표하는 성당 중 하나로, "
            "1882년부터 건축이 시작되어 현재도 공사가 진행 중입니다. 독특한 건축미와 화려한 스테인드글라스, "
            "상징적인 첨탑들이 조화를 이루며, 유네스코 세계문화유산으로 등재되어 있습니다. "
            "성당 내부에 들어서면 빛의 향연과 자연에서 영감을 받은 독창적인 디자인에 감탄하게 됩니다."
        )
    },
    {
        "name": "알람브라 궁전",
        "city": "그라나다",
        "location": (37.1760, -3.5881),
        "description": (
            "알람브라 궁전은 이슬람 문화와 스페인 고유의 예술이 융합된 걸작으로, "
            "그라나다 언덕 위에 우아하게 자리잡고 있습니다. 대리석 기둥, 섬세한 무늬의 타일, "
            "정교한 정원과 분수는 방문객들에게 중세 안달루시아의 정취를 선사합니다. "
            "특히 나스리드 궁, 콤레스 궁전, 사자정원은 알람브라의 백미로 손꼽힙니다."
        )
    },
    {
        "name": "프라도 미술관",
        "city": "마드리드",
        "location": (40.4138, -3.6921),
        "description": (
            "프라도 미술관은 스페인에서 가장 유명한 미술관으로, 유럽 미술의 진수를 감상할 수 있는 곳입니다. "
            "벨라스케스, 고야, 엘 그레코 등 스페인 거장들의 작품은 물론, 루벤스, 티치아노, 히에로니무스 보스 등의 "
            "유럽 대가들의 명작도 전시되어 있습니다. 미술 애호가라면 꼭 방문해야 할 필수 코스입니다."
        )
    },
    {
        "name": "세비야 대성당 & 히랄다 탑",
        "city": "세비야",
        "location": (37.3861, -5.9926),
        "description": (
            "세비야 대성당은 세계에서 세 번째로 큰 기독교 성당으로, 15세기 고딕 양식의 웅장함을 자랑합니다. "
            "히랄다 탑은 원래 이슬람 사원의 첨탑이었으나, 이후 대성당의 종탑으로 사용되고 있습니다. "
            "탑 정상에 오르면 세비야 시내 전경을 한눈에 바라볼 수 있어 많은 이들이 방문합니다."
        )
    },
    {
        "name": "파르크 구엘",
        "city": "바르셀로나",
        "location": (41.4145, 2.1527),
        "description": (
            "파르크 구엘은 안토니 가우디가 설계한 독창적인 공원으로, 파스텔톤 모자이크와 곡선미가 돋보이는 곳입니다. "
            "동화 속에 온 듯한 분위기와 바르셀로나 시내를 내려다볼 수 있는 멋진 전망 덕분에 "
            "가족과 연인 모두에게 인기 있는 명소입니다."
        )
    }
]

# 관광지 이름 리스트 생성
spot_names = [spot["name"] for spot in tourist_spots]

st.title("스페인 주요 관광지 친절 가이드 🇪🇸")
st.markdown(
    """
    스페인은 세계적으로 유명한 관광지와 유구한 역사를 자랑하는 나라입니다.  
    아래에서 원하는 관광지를 선택하면, 해당 지역의 위치와 상세 정보를 확인할 수 있습니다!
    """
)

# 관광지 선택 위젯
selected_name = st.selectbox("관광지를 선택하세요:", spot_names)

# 선택된 관광지 정보 추출
selected_spot = next(spot for spot in tourist_spots if spot["name"] == selected_name)

# 지도 생성 및 마커 표시
m = folium.Map(location=selected_spot["location"], zoom_start=13, tiles='cartodbpositron')

# 모든 관광지 마커 추가 (선택지 강조)
for spot in tourist_spots:
    if spot["name"] == selected_name:
        folium.Marker(
            location=spot["location"],
            tooltip=spot["name"],
            icon=folium.Icon(color="blue", icon="star")
        ).add_to(m)
    else:
        folium.Marker(
            location=spot["location"],
            tooltip=spot["name"],
            icon=folium.Icon(color="gray", icon="info-sign")
        ).add_to(m)

st.subheader("🗺️ 관광지 지도")
st_folium(m, width=700, height=500)

st.subheader("🌟 관광지 상세 정보")
st.markdown(f"### {selected_spot['name']} ({selected_spot['city']})")
st.write(selected_spot["description"])

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# 기본 파라미터 설정
H0 = 70  # 허블 상수 (km/s/Mpc)
Omega_m = 0.3  # 물질 밀도
Omega_lambda = 0.7  # 암흑 에너지 밀도

st.title("표준 우주모형 기반 우주 팽창 속도 그래프")

# 사용자가 조정할 수 있는 슬라이더
H0 = st.slider("허블 상수 H₀ (km/s/Mpc)", 50, 90, 70)
Omega_m = st.slider("물질 밀도 파라미터 Ωₘ", 0.0, 1.0, 0.3)
Omega_lambda = st.slider("암흑 에너지 밀도 파라미터 Ω_Λ", 0.0, 1.0, 0.7)

# 적색편이 z 범위 설정
z = np.linspace(0, 5, 500)

# 허블 파라미터 계산 함수
def Hubble(z, H0, Omega_m, Omega_lambda):
    return H0 * np.sqrt(Omega_m * (1 + z) ** 3 + Omega_lambda)

H = Hubble(z, H0, Omega_m, Omega_lambda)

# 그래프 그리기
fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(z, H, label="H(z)")
ax.set_xlabel("적색편이 (z)")
ax.set_ylabel("허블 파라미터 H(z) (km/s/Mpc)")
ax.set_title("적색편이에 따른 우주 팽창 속도 (표준 우주모형)")
ax.legend()
ax.grid(True)

st.pyplot(fig)


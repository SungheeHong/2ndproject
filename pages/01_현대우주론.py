import streamlit as st
import numpy as np
import plotly.graph_objects as go

# 기본 파라미터
H0 = 70  # 허블 상수 (km/s/Mpc)
Omega_m = 0.3
Omega_lambda = 0.7

st.title("우주 팽창 속도와 크기의 3차원 시각화 (ΛCDM 모형, numpy 버전)")

# 파라미터 슬라이더
H0 = st.slider("허블 상수 H₀ (km/s/Mpc)", 50, 90, 70)
Omega_m = st.slider("물질 밀도 파라미터 Ωₘ", 0.0, 1.0, 0.3)
Omega_lambda = st.slider("암흑 에너지 밀도 파라미터 Ω_Λ", 0.0, 1.0, 0.7)

# z, a, H(z) 계산
z = np.linspace(0, 5, 200)
a = 1 / (1 + z)

def Hubble(z, H0, Omega_m, Omega_lambda):
    return H0 * np.sqrt(Omega_m * (1 + z) ** 3 + Omega_lambda)

H = Hubble(z, H0, Omega_m, Omega_lambda)

# 우주 나이(lookback time) 근사적 계산 (numpy 만 사용)
# H0 단위를 1/Gyr로 변환
H0_SI = H0 * 1000 / (3.086e22)  # s^-1
H0_inv_Gyr = 1 / H0_SI / (3.154e16 * 1e9)  # Gyr

Ez = np.sqrt(Omega_m * (1 + z) ** 3 + Omega_lambda)
integrand = 1 / ((1 + z) * Ez)
dz = np.gradient(z)
lookback = np.cumsum(integrand * dz) * H0_inv_Gyr
t_age = lookback[-1] - lookback  # 현재에서 볼 때, t=0이 빅뱅

# 3D 그래프 생성
fig = go.Figure(data=[go.Scatter3d(
    x=t_age,
    y=a,
    z=H,
    mode='lines',
    line=dict(color=H, colorscale='Viridis', width=4),
    hovertemplate='나이: %{x:.2f} Gyr<br>a: %{y:.3f}<br>H(z): %{z:.1f} km/s/Mpc'
)])
fig.update_layout(
    scene=dict(
        xaxis_title='우주 나이 (Gyr, 과거→현재)',
        yaxis_title='스케일 팩터 a',
        zaxis_title='허블 파라미터 H(z) (km/s/Mpc)'
    ),
    margin=dict(l=0, r=0, b=0, t=40),
    title="우주 팽창 속도와 크기의 3차원 라인 그래프"
)

st.plotly_chart(fig, use_container_width=True)

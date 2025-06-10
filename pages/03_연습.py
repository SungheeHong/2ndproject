import streamlit as st
import numpy as np
import plotly.graph_objects as go

st.title("입체 곡면으로 보는 우주의 크기 변화 (ΛCDM)")

# 파라미터 범위 설정
H0 = 70  # 허블 상수 (고정)
Omega_lambda = 0.7  # 암흑 에너지 밀도 (고정)
z = np.linspace(0, 5, 100)  # 적색편이
Omega_m_values = np.linspace(0.1, 0.5, 60)  # 다양한 물질 밀도

Z, OMEGA = np.meshgrid(z, Omega_m_values)

# 코메폴리적 거리 계산 함수
def comoving_distance(z, Omega_m, Omega_lambda, H0=70):
    # 각 파라미터별로 shape 맞추기
    z = np.atleast_2d(z)
    Omega_m = np.atleast_2d(Omega_m)
    Ez = np.sqrt(Omega_m.T * (1 + z)**3 + Omega_lambda)
    dz = np.gradient(z, axis=1)
    integrand = 1 / Ez
    # 사다리꼴 적분 근사 (누적합)
    comoving = np.cumsum(integrand * dz, axis=1) * (3e5 / H0)  # 단위: Mpc
    return comoving

# 실제 곡면 계산
COMOVING = comoving_distance(z, Omega_m_values, Omega_lambda)

# 곡면 플롯
fig = go.Figure(data=[go.Surface(
    x=Z,
    y=OMEGA,
    z=COMOVING,
    colorscale='Viridis',
    cmin=COMOVING.min(),
    cmax=COMOVING.max(),
    colorbar=dict(title="코메폴리적 거리 (Mpc)")
)])
fig.update_layout(
    scene=dict(
        xaxis_title='적색편이 z',
        yaxis_title='물질 밀도 Ωₘ',
        zaxis_title='코메폴리적 거리 (Mpc)'
    ),
    margin=dict(l=0, r=0, b=0, t=40),
    title="우주의 크기 변화 3차원 곡면 (Surface) 그래프"
)

st.plotly_chart(fig, use_container_width=True)

# Generated from: The Klinkenberg Effect.ipynb
# Converted at: 2026-03-23T15:11:51.246Z
# Next step (optional): refactor into modules & generate tests with RunCell
# Quick start: pip install runcell

import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

st.title("The Klinkenberg Effect")

# User inputs (replace input())
k = st.number_input("Enter the initial guess of absolute permeability (md):", value=1.0)
pmean = st.number_input("Enter the mean pressure (psi):", value=100.0)
kgas = st.number_input("Enter the gas permeability (md):", value=1.0)

if st.button("Calculate"):

    # Iteration
    while abs(6.9*(k**0.64) + pmean*k - pmean*kgas) > 0.0001:
        k = k - (6.9*(k**0.64) + pmean*k - pmean*kgas) / (4.416*(k**(-0.36)) + pmean)

    st.success(f"Absolute permeability ≈ {k:.5f} md")

    # Plot data
    x = [0, 1/pmean]
    y = [k, kgas]

    coefficients = np.polyfit(x, y, 1)
    polynomial = np.poly1d(coefficients)

    x_axis = np.linspace(0, 0.2, 100)
    y_axis = polynomial(x_axis)

    fig, ax = plt.subplots()
    ax.plot(x_axis, y_axis, label="Fitted Line")
    ax.plot(x, y, 'o', label="Data Points")

    ax.set_xlabel("1 / Mean Pressure (psi⁻¹)")
    ax.set_ylabel("Measured Gas Permeability (md)")
    ax.set_title("The Klinkenberg Effect")
    ax.grid(True)
    ax.legend()

    # Show plot in Streamlit
    st.pyplot(fig)

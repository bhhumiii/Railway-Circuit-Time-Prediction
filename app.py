import streamlit as st
import pandas as pd
import plotly.express as px


import os

print(os.path.getsize("feature_importance.png"))
print(os.path.getsize("actual_vs_predicted.png"))
print(os.path.getsize("residual_plot_new.png"))

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="Railway Freight Analytics",
    page_icon="🚆",
    layout="wide"
)

# -----------------------------
# CUSTOM CSS
# -----------------------------
st.markdown("""
<style>
.main {
    padding-top: 1rem;
}
h1 {
    color: #1f4e79;
}
h2 {
    color: #2e75b6;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# SIDEBAR
# -----------------------------
st.sidebar.title("🚆 Railway Analytics")

page = st.sidebar.radio(
    "Navigation",
    [
        "Overview",
        "Model Comparison",
        "Feature Analysis",
        "Prediction Results",
        "Insights"
    ]
)

# -----------------------------
# OVERVIEW PAGE
# -----------------------------
if page == "Overview":

    st.title("🚆 Railway Freight Circuit Time Prediction")

    st.markdown("---")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Records", "223,793")
    col2.metric("Features", "208+")
    col3.metric("Best R²", "0.8808")
    col4.metric("Best Model", "XGBoost")

    st.markdown("---")

    st.header("📌 Project Summary")

    st.info("""
    This project predicts Railway Freight Rake Circuit Time
    using Machine Learning techniques.

    Target Variable:
    Circuit Time (Hours)

    Best Model:
    XGBoost
    """)

    st.markdown("---")

    st.header("📊 Dataset Information")

    st.write("Total Records : 223,793")
    st.write("Original Features : 94")
    st.write("Engineered Features : 208+")
    st.write("Target Variable : Circuit Time (Hours)")

# -----------------------------
# MODEL COMPARISON PAGE
# -----------------------------
elif page == "Model Comparison":

    st.title("📈 Model Comparison")

    results = pd.DataFrame({
        "Model": [
            "RF Basic",
            "RF Enhanced",
            "LightGBM",
            "XGBoost"
        ],
        "R² Score": [
            0.8580,
            0.8735,
            0.8773,
            0.8808
        ],
        "MAE": [
            18.62,
            16.19,
            16.37,
            15.67
        ],
        "RMSE": [
            34.83,
            32.87,
            32.37,
            31.91
        ]
    })

    st.dataframe(results, use_container_width=True)

    st.markdown("---")

    fig = px.bar(
        results,
        x="Model",
        y="R² Score",
        text="R² Score",
        title="Model Performance Comparison"
    )

    st.plotly_chart(fig, use_container_width=True)

# -----------------------------
# FEATURE ANALYSIS PAGE
# -----------------------------
elif page == "Feature Analysis":

    st.title("⭐ Feature Analysis")

    st.image(
        "feature_importance.png",
        caption="Top Important Features"
    )
    st.header("Correlation Analysis")

    st.image(
        "correlation_heatmap.png",
        caption="Correlation Heatmap of Key Numerical Features",
        use_container_width=True
    )


    st.markdown("---")

    top_features = pd.DataFrame({
        "Feature":[
            "GRUPCMDT_RMC",
            "RAKECMDT_RMC",
            "GRUPTYPE_BOX",
            "LDNG_ULDG_HOR",
            "GRUPTYPE_SHRA",
            "RAKETYPE_BRN",
            "GRUPCMDT_SLPR",
            "GRUPCMDT_CONT",
            "GRUPTYPE_JUMB",
            "GRUPTYPE_BOST"
        ],
        "Importance":[
            0.111,
            0.083,
            0.064,
            0.060,
            0.052,
            0.038,
            0.031,
            0.029,
            0.022,
            0.020
        ]
    })

    st.subheader("Top Features Table")

    st.dataframe(top_features, use_container_width=True)

# -----------------------------
# PREDICTION RESULTS PAGE
# -----------------------------
elif page == "Prediction Results":

    st.title("📉 Prediction Results")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Actual vs Predicted")
        st.image("actual_vs_predicted.png")

    with col2:
        st.subheader("Residual Analysis")
        st.image("residual_plot_new.png")

# -----------------------------
# INSIGHTS PAGE
# -----------------------------
elif page == "Insights":

    st.title("🔍 Key Insights & Conclusion")

    with st.expander("Top Finding"):
        st.write("""
        Commodity type has a significant impact on
        railway rake circuit time.
        """)

    with st.expander("Most Important Feature"):
        st.write("""
        GRUPCMDT_RMC and RAKECMDT_RMC
        were the most influential features.
        """)

    with st.expander("Operational Insight"):
        st.write("""
        Loading-to-unloading travel duration
        is one of the strongest predictors.
        """)

    with st.expander("Model Performance"):
        st.write("""
        XGBoost outperformed all other models.

        R² = 0.8808
        MAE = 15.67 Hours
        RMSE = 31.91 Hours
        """)

    with st.expander("Business Impact"):
        st.write("""
        The model can help railway planners
        estimate circuit time and improve
        rake utilization.
        """)

    with st.expander("Future Scope"):
        st.write("""
        Future work may include:

        • Real-time train movement data

        • Weather information

        • Live railway operational dashboards

        • Deep Learning based prediction
        """)

    st.markdown("---")

    st.success("""
    Conclusion:

    XGBoost achieved the best performance
    among all tested models.

    R² Score : 0.8808

    MAE : 15.67 Hours

    RMSE : 31.91 Hours

    The model effectively predicts
    railway freight circuit time and
    turnaround performance.
    """)

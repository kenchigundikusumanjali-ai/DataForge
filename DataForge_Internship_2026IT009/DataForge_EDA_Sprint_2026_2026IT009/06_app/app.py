import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("DataForge EDA App")

uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("Dataset Shape")
    st.write(df.shape)

    st.subheader("Column Names")
    st.write(df.columns.tolist())

    st.subheader("Data Types")
    st.write(df.dtypes)

    st.subheader("Missing Values")
    st.write(df.isna().sum())

    st.subheader("Numeric Summary")
    st.write(df.describe())

    numeric_cols = df.select_dtypes(include="number").columns

    if len(numeric_cols) > 0:
        fig, ax = plt.subplots()
        df[numeric_cols[0]].hist(ax=ax)
        ax.set_title(f"Histogram of {numeric_cols[0]}")
        st.pyplot(fig)

        if len(numeric_cols) > 1:
            fig2, ax2 = plt.subplots()
            ax2.scatter(df[numeric_cols[0]], df[numeric_cols[1]])
            ax2.set_xlabel(numeric_cols[0])
            ax2.set_ylabel(numeric_cols[1])
            st.pyplot(fig2)
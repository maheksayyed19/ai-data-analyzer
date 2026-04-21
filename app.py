import streamlit as st
import plotly.express as px 
from analyzer import analyze_csv
from ai_insights import get_ai_insights
import plotly.express as px
import pandas as pd

st.set_page_config(page_title = "AI Data Analyzer", layout = "wide")

st.title("📊AI Data Analysis Tool")

file = st.file_uploader("Upload CSV file", type=["csv"])

if file:
    try:
        df, summary = analyze_csv(file)

        st.success("File uploaded successfully ✅")

        # 🔥 AI INSIGHTS FIRST
        st.subheader("🤖 AI Insights")

        st.info("Click below to generate AI insights from your data")

        if st.button("Generate AI Insights"):
            with st.spinner("Analyzing your data..."):
                insights = get_ai_insights(summary)
                st.success("Insights generated ✅")
                st.write(insights)

        # 📈 Visualization
        st.subheader("📈 Visualization")

        column = st.selectbox("Select column", df.columns)

        # 🔥 Smart visualization
        if pd.api.types.is_numeric_dtype(df[column]):

            # Remove ID-like columns automatically
            if "id" in column.lower() or "number" in column.lower():
                st.warning("This looks like an ID column. Try another column for better insights 👇")
            else:
                fig = px.histogram(
                    df,
                    x=column,
                    nbins=30,
                    color=column,  # ✅ this works
                )

        elif df[column].nunique() < 20:
            # Categorical column → bar chart
            fig = px.bar(
                df[column].value_counts().reset_index(),
                x="index",
                y=column,
                color="index",
                title=f"{column} Distribution",
            )

        else:
            st.info("Too many unique values for meaningful visualization.")

        # Show chart only if fig exists
        if 'fig' in locals():
            st.plotly_chart(fig, use_container_width=True)


        # 📊 Dataset Info
        show_data = st.toggle("Show Dataset Info")

        if show_data:
            st.json(summary)

    except Exception as e:
        st.error(f"Error: {e}")
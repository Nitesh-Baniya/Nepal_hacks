import streamlit as st
import plotly.express as px
import altair as alt
import pandas as pd
from collections import Counter

def normalize_response(value):
    val = value.strip('*').strip().lower()
    if val == 'satisfied':
        return 'Satisfied'
    elif val == 'not satisfied':
        return 'Not Satisfied'
    elif val == 'missing':
        return 'Missing'
    else:
        return 'Unknown'

def render_charts(consise_report_group, parse_report_func):
    bar_data = []

    for i, report in enumerate(consise_report_group):
        name = report["name"]
        consise_report = report["report"]
        dict_report = parse_report_func(consise_report)

        # Normalize and count statuses
        status_list = [normalize_response(d['Status']) for d in dict_report]
        counts = Counter(status_list)

        # Store counts for bar chart
        bar_data.append({
            "Framework": name,
            "Missing": counts.get("Missing", 0),
            "Not Satisfied": counts.get("Not Satisfied", 0),
            "Satisfied": counts.get("Satisfied", 0),
        })



    # ---- Stacked Bar Chart ----
    df_bar = pd.DataFrame(bar_data)
    df_long = df_bar.melt(id_vars="Framework", var_name="Status", value_name="Count")

    st.markdown("### 📊 Summary Bar Chart", unsafe_allow_html=True)
    chart = (
        alt.Chart(df_long)
        .mark_bar(size=80)
        .encode(
            x=alt.X("Framework:N", title="Framework"),
            y=alt.Y("Count:Q", title="Count"),
            color=alt.Color("Status:N",
                            scale=alt.Scale(
                                domain=["Missing", "Not Satisfied", "Satisfied"],
                                range=["#ff7f0e", "#dc3545", "#28a745"]
                            ),
                            title="Status"),
            tooltip=["Framework", "Status", "Count"]
        )
        .properties(width=700, height=350)
        .configure_axis(labelAngle=0)
    )

    st.altair_chart(chart, use_container_width=True)

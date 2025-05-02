import streamlit as st
import zipfile
import pandas as pd
import pytesseract
import plotly.express as px
import os
import time
# import re
from collections import Counter
from pathlib import Path
# from textwrap import dedent
# from main_pipeline import run_rag_pipeline
from results import (ccpa, cis, gdpr, hipaa, hitrust, iso, nist_80053, nist_csf, pci_dss, scf )
from utils.bar_graph import (normalize_response, render_charts)

from utils import (clear_folder, text_2_pdf)
from parsers.parse_report import parse_report

# from summarizer.summary import get_summaries
from summarizer import summary

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe' 



# --- UI CONFIG ---
st.set_page_config(page_title="Compliance Gap Detector", layout="wide")

# --- Custom CSS ---
st.markdown("""
    <style>
        html, body, [class*="css"] {
            font-size: 24px !important;
        }

        h1{
            font-size = 4em !important;    
        }
        
        h2, h3, h4, h5, h6 {
            font-size: 2em !important;
        }

        .stTextInput > div > div > input {
            font-size: 18px !important;
        }

        .stSelectbox > div > div > div > div {
            font-size: 18px !important;
        }

        .stDataFrame div {
            font-size: 18px !important;
        }
    </style>
""", unsafe_allow_html=True)


# --- Title & Description ---
st.markdown("""
        <h1 style='text-align: center; color: #00CFFD; font-size: 72px !important;'>Compliance Mate Dashboard</h1>
        <p style='text-align: center; color: #EDEDED;'>Select frameworks and upload your policy documents to identify gaps.</p>
    """, 
    unsafe_allow_html=True)


# --- Framework Selection ---
st.markdown("""
    <h2 style="text-align: center; font-size: 32px; color: #FFFFFF;">
        Select Compliance Framework(s):
    </h2>
""", unsafe_allow_html=True)


available_frameworks = [
    "ISO", "NIST_800_53", "HIPAA", "GDPR", "CCPA",
    "PCI_DSS", "CIS", "HITRUST", "NIST_CSF", "SCF"
]


# Initialize session state for checkboxes
if "select_all" not in st.session_state:
    st.session_state.select_all = False

for fw in available_frameworks:
    if fw not in st.session_state:
        st.session_state[fw] = False

# Select All checkbox
def toggle_all():
    for fw in available_frameworks:
        st.session_state[fw] = st.session_state.select_all

st.checkbox("Select All Frameworks", key="select_all", on_change=toggle_all)


col1, col2, col3 = st.columns(3)
selected_frameworks = []

for i, fw in enumerate(available_frameworks):
    if i % 3 == 0:
        if col1.checkbox(fw, key=fw): selected_frameworks.append(fw)
    elif i % 3 == 1:
        if col2.checkbox(fw, key=fw): selected_frameworks.append(fw)
    else:
        if col3.checkbox(fw, key=fw): selected_frameworks.append(fw)


# Show selected
if selected_frameworks:
    st.markdown("""
        <h3 style='text-align: center;'>✅ Selected Frameworks</h3>
    """, unsafe_allow_html=True)
    st.markdown(
        "<div style='text-align: center;'>"
        + " ".join([
            f"<span style='background-color:#00CFFD;color:black;padding:4px 10px;border-radius:20px;margin:4px;display:inline-block;font-weight:bold;'>{fw}</span>"
            for fw in selected_frameworks
        ])
        + "</div>",
        unsafe_allow_html=True
    )

# Clear all the previously uploaded policies
clear_folder.clear_previous_files("data/policies")

# --- ZIP File Upload ---
st.markdown("### Upload Your ZIP File")

uploaded_file = st.file_uploader(
    "Upload ZIP File Containing Policy Documents (.zip)", 
    type="zip"
)

if uploaded_file is not None:
    st.info("Uploading and extracting ZIP file...")
    progress = st.progress(0)
    output_dir = Path("./data/policies")
    output_dir.mkdir(parents=True, exist_ok=True)

    zip_path = output_dir / "temp_upload.zip"
    with open(zip_path, "wb") as f:
        f.write(uploaded_file.read())
        progress.progress(30)

    try:
        with zipfile.ZipFile(zip_path, "r") as zip_ref:
            zip_ref.extractall(output_dir)
            time.sleep(1)
            progress.progress(80)
        zip_path.unlink()
        time.sleep(1)
        progress.progress(100)
        st.success("✅ ZIP uploaded and extracted successfully.")
    except zipfile.BadZipFile:
        st.error("❌ Uploaded file is not a valid ZIP archive.")
        st.stop()
else:
    st.markdown("<p style='color: gray;'>Only ZIP files are allowed. Upload a compressed archive of your policy PDFs.</p>", unsafe_allow_html=True)


# Less attractive
# if uploaded_file is not None:
    # st.info("Uploading and extracting ZIP file...")
    # progress = st.progress(0)
#     output_dir = Path("./data/policies")
#     output_dir.mkdir(parents=True, exist_ok=True)

#     zip_path = output_dir / "temp_upload.zip"
#     with open(zip_path, "wb") as f:
#         f.write(uploaded_file.read())

#     try:
#         # Unzip the file
#         with zipfile.ZipFile(zip_path, "r") as zip_ref:
#             zip_ref.extractall(output_dir)
#         zip_path.unlink()
#         st.success("ZIP uploaded and extracted successfully.")
#     except zipfile.BadZipFile:
#         st.error("Uploaded file is not a valid ZIP archive.")
#         st.stop()

# --- Retrieving reports from results.py ---
framework_reports = {
    "CCPA": ccpa,
    "CIS": cis,
    "GDPR": gdpr,
    "HIPAA": hipaa,
    "HITRUST": hitrust,
    "ISO": iso,
    "NIST_800_53": nist_80053,
    "NIST_CSF": nist_csf,
    "PCI_DSS": pci_dss,
    "SCF": scf,
}

time.sleep(60)
# Show summaries after processing:
# --- Upload Summaries ---

# Get the list of policy files in data/policies (assuming they are .pdf files)
policy_files = set(os.path.splitext(file)[0] for file in os.listdir('data/policies') if file.endswith('.pdf'))

# Get the list of summary files in summarizer/summaries (assuming they are .txt files)
summary_files = summary.get_txt_files()

# Filter summary files to only include those whose names (without extension) match policy files
filtered_files = [file for file in summary_files if os.path.splitext(file)[0] in policy_files]

if not filtered_files:
    st.warning("No summary files found for the available policy files.")
else:
    st.markdown("### 📝 View Policy Summary Files")
    
    col1, col2 = st.columns([1, 3])
    with col1:
        st.markdown("<div style='font-size:20px; padding-top: 8px;'>📄 Choose a file:</div>", unsafe_allow_html=True)
    with col2:
        selected_file = st.selectbox("", filtered_files, key="summary_file_selector")

    if selected_file:
        content = summary.read_file_content(selected_file)
        st.subheader(f"Content of {selected_file}")
        st.text_area("File Content", content, height=300)
        
        # Prepare the corresponding PDF filename
        pdf_filename = os.path.splitext(selected_file)[0] + ".pdf"
        
        # # Create PDF from the summary content
        # pdf_output = text_2_pdf.create_pdf_from_text(content, pdf_filename)

        # # Provide a download button for the PDF
        # st.download_button(
        #     label="Download PDF of Summary",
        #     data=pdf_output,
        #     file_name=f"{selected_file}.pdf",
        #     mime="application/pdf"
        # )
        
        
        
# --- Display Results ---
if uploaded_file and selected_frameworks:
    print(selected_frameworks)
    #USE THE CODE THAT TAKES LIST OF FRAMEWORK NAMES AND OUTPUTS CONSISE REPORT HERE
    #consise_report=main_code(selected_frameworks)

        # Prepare and render all charts (summary or comparison level)
    consise_report_group = [
        {"name": framework, "report": framework_reports.get(framework, "")}
        for framework in selected_frameworks
    ]
    render_charts(consise_report_group, parse_report)
    
        
    if uploaded_file and selected_frameworks:
        # Dropdown to select one framework for chart + table view
        col1, col2 = st.columns([1, 3])

        with col1:
            st.markdown("<div style='font-size:30px; padding-top: 17px;'>🔎 Choose a framework:</div>", unsafe_allow_html=True)

        with col2:
            selected_fw = st.selectbox("", selected_frameworks, key="framework_selector")

        # Parse and process the selected framework report
        consise_report = framework_reports.get(selected_fw, "")
        dict_report = parse_report(consise_report)
        Status_list = [d['Status'] for d in dict_report]
        output_list = [normalize_response(val) for val in Status_list]
        counts = Counter(output_list)

        # Create pie chart
        labels = list(counts.keys())
        values = list(counts.values())
        fig = px.pie(
            names=labels,
            values=values,
            title=f"Response Distribution for {selected_fw}",
            color=labels,
            color_discrete_map={
                'Satisfied Requirements': 'green',
                'Not Satisfied Requirements': 'orange',
                'Missing Requirements': 'gray',
                'Unknown': 'blue'
            }
        )
        st.plotly_chart(fig, key=f"plotly_chart_{selected_fw}")

        # Table
        data = [
            (dic["Requirement"], dic["Status"], dic["Reason"], dic["Target Policy"])
            for dic in dict_report
        ]
        df = pd.DataFrame(data, columns=["Requirement", "Status", "Reason", "Target Policy"])
        st.markdown(f"### Compliance Gap Results for {selected_fw}")
        st.dataframe(df, use_container_width=True)


    
elif not uploaded_file:
    st.info("Please upload a ZIP file.")
elif not selected_frameworks:
    st.warning("Please select at least one compliance framework.")


import streamlit as st
import pandas as pd
st.markdown("""
<style>

.stApp {
    background-color: #0E1117;
    color: white;
}

h1, h2, h3 {
    color: #00FFD1;
}

.stButton>button {
    background-color: #00FFD1;
    color: black;
    border-radius: 10px;
    font-weight: bold;
}

.stTextInput>div>div>input {
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)
from database.db import create_table, insert_history, get_history
from automation.form_filler import fill_google_form
from utils.document_extractor import (
    extract_text_from_pdf,
    extract_fields_from_text
)
st.set_page_config(
    page_title="AutoEntry AI",
    page_icon="🤖",
    layout="wide"
)
create_table()
st.sidebar.title("🤖 AutoEntry AI")

page = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Submission History",
        "Reports",
        "Settings"
    ]
)
if page == "Dashboard":
    st.markdown("""
# 🚀 AutoEntry AI

### Intelligent Workflow Automation System

Automate repetitive data entry tasks using AI-powered smart field matching and browser automation.
""")
    st.subheader("📄 Document Intelligence Upload")
    document_file = st.file_uploader(
        "Upload PDF document for extraction",
        type=["pdf"],
        key="document_upload"
    )
    if document_file:
        extracted_text = extract_text_from_pdf(document_file)
        extracted_data = extract_fields_from_text(extracted_text)
        st.success("Document data extracted successfully!")
        st.json(extracted_data)
        doc_df = pd.DataFrame([extracted_data])
        st.subheader("📋 Extracted Data Preview")
        st.dataframe(doc_df, use_container_width=True)
        st.subheader("🔗 Google Form URL For PDF Automation")
        pdf_form_url = st.text_input(
            "Paste Google Form URL for extracted PDF data",
            key="pdf_form_url"
        )
        if pdf_form_url:
            if st.button("🚀 Auto Fill Form From PDF"):
                try:
                    fill_google_form(
                    pdf_form_url,
                    extracted_data
                    )
                    st.success(
                        "PDF data submitted successfully!"
                )
                except Exception as e:
                    st.exception(e)
    uploaded_file = st.file_uploader("Upload CSV or Excel File", type=["csv", "xlsx"])
    if uploaded_file:
        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)
        st.success("File uploaded successfully!")
        st.subheader("📄 Data Preview")
        st.dataframe(df, use_container_width=True)
        st.divider()
        st.subheader("🔗 Google Form URL")
        form_url = st.text_input("Paste your Google Form link here")
        if form_url:st.success("Google Form URL added successfully!")
        st.subheader("✅ Review Before Submission")
        max_records = st.number_input(
            "How many records do you want to submit?",
            min_value=1,
            max_value=len(df),
            value=1
        )
        confirm_submit = st.checkbox(
            "I confirm that I have permission to submit this form and want to start automation."
        )
    if st.button("🚀 Auto Fill Google Form"):
            success_count = 0
            failed_count = 0
            total_records = len(df)
            progress_bar = st.progress(0)
            status_box = st.empty()
            result_data = []
            for index, row in df.head(max_records).iterrows():
                row_data = row.to_dict()
                try:
                    status_box.info(f"Submitting row {index + 1} of {total_records}...")
                    filled_fields = fill_google_form(form_url, row_data)
                    success_count += 1
                    result_data.append({
                    "Row": index + 1,
                    "Data": row_data,
                    "Status": "Success",
                    "Message": f"Submitted successfully | Fields filled: {len(filled_fields)}"
                    })
                    insert_history(
                        index + 1,
                        row_data,
                        "Success",
                        f"Submitted successfully | Fields filled: {len(filled_fields)}"
                    )   
                except Exception as e:
                    failed_count += 1
                    result_data.append({
                        "Row": index + 1,
                        "Data": row_data,
                        "Status": "Failed",
                        "Message": str(e)
                    })
                    insert_history(
                    index + 1,
                    row_data,
                    "Failed",
                    str(e)
                    )
                progress_bar.progress((index + 1) / total_records)
            status_box.success("Submission process completed!")
            st.subheader("📊 Submission Summary")
            col1, col2, col3 = st.columns(3)
            col1.metric("Total Records", total_records)
            col2.metric("Successful", success_count)
            col3.metric("Failed", failed_count)
            st.subheader("📋 Submission Result Table")
            result_df = pd.DataFrame(result_data)
            st.dataframe(result_df, use_container_width=True)
            csv_report = result_df.to_csv(index=False).encode("utf-8")
            st.download_button(
                label="⬇️ Download Submission Report",
                data=csv_report,
                file_name="submission_report.csv",
                mime="text/csv"
            )
            st.divider()
    st.subheader("📜 Permanent Submission History")
    history = get_history()
    if history:
        history_df = pd.DataFrame(
            history,
            columns=[
                "ID",
                "Row Number",
                "Record Data",
                "Status",
                "Message",
                "Submitted At"
            ]
        )
        st.dataframe(history_df, use_container_width=True)
    else:
        st.info("No saved history yet.")
if page == "Submission History":

    st.title("📜 Submission History")

    history = get_history()

    if history:

        history_df = pd.DataFrame(
            history,
            columns=[
                "ID",
                "Row Number",
                "Record Data",
                "Status",
                "Message",
                "Submitted At"
            ]
        )

        st.dataframe(history_df, use_container_width=True)

    else:

        st.info("No submission history available.")
if page == "Reports":

    st.title("📊 Analytics Dashboard")

    history = get_history()

    if history:

        history_df = pd.DataFrame(
            history,
            columns=[
                "ID",
                "Row Number",
                "Record Data",
                "Status",
                "Message",
                "Submitted At"
            ]
        )

        total = len(history_df)

        success = len(
            history_df[history_df["Status"] == "Success"]
        )

        failed = len(
            history_df[history_df["Status"] == "Failed"]
        )

        col1, col2, col3 = st.columns(3)

        col1.metric("Total Submissions", total)

        col2.metric("Successful", success)

        col3.metric("Failed", failed)

    else:

        st.info("No analytics available yet.")
        if page == "Settings":
            st.title("⚙️ Settings")
            st.info("More settings coming soon.")
            headless_mode = st.checkbox(
            "Run browser in headless mode",
             value=False
           )
    auto_close = st.checkbox(
        "Auto close browser after submission",
        value=True
    )
    st.success("Settings saved successfully!")       
    st.divider()
    st.caption(
    "Built with Python, Streamlit, Playwright, SQLite and AI-powered automation."
)  
if page == "Settings":

    st.title("⚙️ Settings")

    st.info("Configure automation behavior here.")

    headless_mode = st.checkbox(
        "Run browser in headless mode",
        value=False
    )

    auto_close = st.checkbox(
        "Auto close browser after submission",
        value=True
    )

    delay_time = st.slider(
        "Delay between submissions in seconds",
        min_value=1,
        max_value=10,
        value=3
    )

    st.success("Settings loaded successfully!")      
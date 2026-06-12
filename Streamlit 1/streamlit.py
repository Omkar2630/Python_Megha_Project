import streamlit as st
import pandas as pd

from modules.excel_reader import ExcelReader
from modules.bcm_validator import BCMValidator
from modules.chart_generator import ChartGenerator
from modules.report_generator import ReportGenerator
from modules.pdf_converter import PDFConverter

st.set_page_config(page_title="BCM Test Automation", layout="wide")

st.title("📊 BCM Test Case Execution Dashboard")

# Upload Excel file
uploaded_file = st.file_uploader("Upload Test Case Excel File", type=["xlsx"])

if uploaded_file:

    # Read Excel
    df = ExcelReader.read_excel(uploaded_file)

    if df is None:
        st.error("❌ Excel loading failed.")
    else:
        st.success("✅ Excel loaded successfully")

        actual_results = []
        remarks_list = []

        # Progress bar
        progress = st.progress(0)
        total_rows = len(df)

        # Execute validation
        for i, (_, row) in enumerate(df.iterrows()):
            actual_result, remarks = BCMValidator.validate(row)
            actual_results.append(actual_result)
            remarks_list.append(remarks)

            progress.progress((i + 1) / total_rows)

        df["Actual_Result"] = actual_results
        df["Remarks"] = remarks_list

        # Compare results
        df["Status"] = df.apply(
            lambda row:
            "Pass"
            if str(row["Expected_Result"]).strip() ==
               str(row["Actual_Result"]).strip()
            else "Fail",
            axis=1
        )

        # Metrics
        total_tc = len(df)
        pass_count = len(df[df["Status"] == "Pass"])
        fail_count = len(df[df["Status"] == "Fail"])

        # Display Metrics
        col1, col2, col3 = st.columns(3)
        col1.metric("Total Test Cases", total_tc)
        col2.metric("Passed ✅", pass_count)
        col3.metric("Failed ❌", fail_count)

        st.divider()

        # Show Data
        st.subheader("📋 Execution Results")
        st.dataframe(df, use_container_width=True)

        # Generate chart
        ChartGenerator.generate(
            pass_count=pass_count,
            fail_count=fail_count,
            output_file="reports/pie_chart.png"
        )

        st.subheader("📈 Test Summary Chart")
        st.image("reports/pie_chart.png")

        # Report Generation Buttons
        st.divider()
        st.subheader("📄 Generate Reports")

        if st.button("Generate Word Report"):
            ReportGenerator.create_report(
                df=df,
                pass_count=pass_count,
                fail_count=fail_count,
                chart_path="reports/pie_chart.png",
                output_docx="reports/BCM_Report.docx"
            )
            st.success("✅ Word Report Generated!")

        if st.button("Generate PDF Report"):
            PDFConverter.convert_to_pdf(
                docx_file="reports/BCM_Report.docx",
                pdf_file="reports/BCM_Report.pdf"
            )
            st.success("✅ PDF Report Generated!")

        # Download Buttons
        with open("reports/BCM_Report.docx", "rb") as f:
            st.download_button(
                "⬇ Download Word Report",
                f,
                file_name="BCM_Report.docx"
            )

        with open("reports/BCM_Report.pdf", "rb") as f:
            st.download_button(
                "⬇ Download PDF Report",
                f,
                file_name="BCM_Report.pdf"
            )

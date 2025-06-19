import streamlit as st
from PyPDF2 import PdfMerger
from io import BytesIO

def merge_pdfs(uploaded_files):
    merger = PdfMerger()
    for uploaded_file in uploaded_files:
        merger.append(uploaded_file)
    output_pdf = BytesIO()
    merger.write(output_pdf)
    merger.close()
    output_pdf.seek(0)
    return output_pdf

st.title("PDFマージアプリ")
st.write("複数のPDFファイルをアップロードして、1つのPDFにマージします。")

uploaded_files = st.file_uploader(
    "PDFファイルを選択（複数可）", type=["pdf"], accept_multiple_files=True
)

if uploaded_files:
    if st.button("マージ実行"):
        try:
            merged_pdf = merge_pdfs(uploaded_files)
            st.success("PDFのマージに成功しました。")
            st.download_button(
                label="📥 マージ済みPDFをダウンロード",
                data=merged_pdf,
                file_name="merged_output.pdf",
                mime="application/pdf"
            )
        except Exception as e:
            st.error(f"エラーが発生しました: {str(e)}")

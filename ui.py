import streamlit as st
from utils.ats_parser import extract_keywords
from utils.resume_builder import generate_resume
from utils.resume_formatter import save_resume_docx, save_resume_pdf

st.set_page_config(page_title="AI Resume Generator", layout="centered")

st.title("📄 AI Resume & Cover Letter Generator (ATS-Friendly)")

# ---- Inputs ----
job_desc = st.text_area("Paste Job Description")
skills = st.text_input("Enter Your Skills (comma-separated)")

# ---- Resume Generation ----
if st.button("Generate Resume"):
    if job_desc.strip() and skills.strip():
        # Extract keywords
        keywords = extract_keywords(job_desc)

        # Generate Resume Text
        resume_text = generate_resume(job_desc, skills)

        # Display on screen
        st.subheader("Generated Resume Preview:")
        st.text(resume_text)

        # Save Files
        docx_file = save_resume_docx(resume_text)
        pdf_file = save_resume_pdf(resume_text)

        # Download Buttons
        with open(docx_file, "rb") as f:
            st.download_button("⬇️ Download DOCX", f, file_name="resume.docx")

        with open(pdf_file, "rb") as f:
            st.download_button("⬇️ Download PDF", f, file_name="resume.pdf")

    else:
        st.warning("⚠️ Please enter both Job Description and Skills.")

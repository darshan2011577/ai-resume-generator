import streamlit as st
from utils.ats_parser import extract_keywords
from utils.resume_builder import generate_resume
from utils.resume_formatter import save_resume_docx, save_resume_pdf
from utils.cover_letter import generate_cover_letter

st.set_page_config(page_title="AI Resume Generator", layout="centered")

st.title("📄 AI Resume & Cover Letter Generator (ATS-Friendly)")

# ---- Inputs ----
job_desc = st.text_area("Paste Job Description")
skills = st.text_input("Enter Your Skills (comma-separated)")
name = st.text_input("Enter Your Name", value="Candidate")

# ---- Resume Generation ----
if st.button("Generate Resume"):
    if job_desc.strip() and skills.strip():
        # Extract keywords
        keywords = extract_keywords(job_desc)

        # Generate Resume Text
        resume_text = generate_resume(job_desc, skills, name=name, email=f"{name.lower()}@example.com")

        # Display on screen
        st.subheader("Generated Resume Preview:")
        st.text(resume_text)

        # Save Files
        docx_file = save_resume_docx(resume_text, "resume.docx")
        pdf_file = save_resume_pdf(resume_text, "resume.pdf")

        # Download Buttons
        with open(docx_file, "rb") as f:
            st.download_button("⬇️ Download Resume (DOCX)", f, file_name="resume.docx")

        with open(pdf_file, "rb") as f:
            st.download_button("⬇️ Download Resume (PDF)", f, file_name="resume.pdf")

    else:
        st.warning("⚠️ Please enter both Job Description and Skills.")

# ---- Cover Letter Generation ----
if st.button("Generate Cover Letter"):
    if job_desc.strip() and skills.strip():
        cover_letter = generate_cover_letter(job_desc, skills, name)

        st.subheader("Generated Cover Letter Preview:")
        st.text(cover_letter)

        # Save as DOCX
        docx_file = save_resume_docx(cover_letter, "cover_letter.docx")
        pdf_file = save_resume_pdf(cover_letter, "cover_letter.pdf")

        with open(docx_file, "rb") as f:
            st.download_button("⬇️ Download Cover Letter (DOCX)", f, file_name="cover_letter.docx")

        with open(pdf_file, "rb") as f:
            st.download_button("⬇️ Download Cover Letter (PDF)", f, file_name="cover_letter.pdf")

    else:
        st.warning("⚠️ Please enter both Job Description and Skills.")

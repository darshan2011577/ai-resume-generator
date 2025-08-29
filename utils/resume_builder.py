def generate_resume(job_desc, skills, name="Candidate", email="candidate@email.com"):
    """
    Generate a more detailed resume structure with sections.
    """

    # Dynamically set max_length depending on input size
    input_len = len(job_desc.split())
    max_len = min(120, int(input_len * 1.2))  # expand slightly but not too long
    min_len = min(60, int(input_len * 0.8))   # at least 80% of input length

    # If job_desc is very short, fallback to plain text
    if input_len < 30:
        jd_summary = job_desc
    else:
        summary = summarizer(job_desc, max_length=max_len, min_length=min_len, do_sample=False)
        jd_summary = summary[0]['summary_text']

    resume_text = f"""
    ================================
              RESUME
    ================================

    Name: {name}
    Email: {email}

    ----------------
    Skills
    ----------------
    {skills}

    ----------------
    Profile Summary
    ----------------
    {jd_summary}

    ----------------
    Education
    ----------------
    - B.Tech in Artificial Intelligence & Data Science, 2025 (Example)

    ----------------
    Experience
    ----------------
    - Worked on data-driven projects related to {', '.join(skills.split(','))}.
    - Applied statistical and machine learning models for problem solving.

    ----------------
    Projects
    ----------------
    - Resume & Cover Letter Generator using AI (Final Year Project)

    ----------------
    References
    ----------------
    Available on request.
    """

    return resume_text.strip()

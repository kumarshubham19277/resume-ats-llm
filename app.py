import streamlit as st

from resume_parser import extract_resume
from rag_pipeline import chunk_text
from embedding import generate_embeddings, get_resume_embedding
from ats_scoring import calculate_similarity
from suggestions import generate_suggestions


st.set_page_config(page_title="AI Resume ATS Checker", page_icon="📄")
st.title("📄 AI Resume ATS Checker")

jd = st.text_area("Paste Job Description", height=200)
resume_file = st.file_uploader("Upload Resume (.pdf or .docx)", type=["pdf", "docx"])


if st.button("Analyze Resume", type="primary"):

    if resume_file is None or jd.strip() == "":
        st.warning("Please upload a resume AND paste a job description.")

    else:
        with st.spinner("Analyzing your resume..."):

            # Extract resume text
            resume_text = extract_resume(resume_file)

            if not resume_text.strip():
                st.error("Could not extract text from the resume. Please check the file.")
                st.stop()

            # Chunk resume
            chunks = chunk_text(resume_text)

            # Combine resume chunks + JD for TF-IDF vectorization
            all_text = chunks + [jd]

            # Generate TF-IDF embeddings
            embeddings = generate_embeddings(all_text)

            # Average all chunk embeddings for a better resume representation
            # Last embedding is the JD
            resume_embedding = get_resume_embedding(embeddings, num_chunks=len(chunks))
            jd_embedding = embeddings[-1]

            # Calculate TF-IDF cosine similarity score
            tfidf_score = calculate_similarity(resume_embedding, jd_embedding)

            st.subheader(f"📊 TF-IDF ATS Match Score: {tfidf_score}%")
            st.progress(int(tfidf_score))

            # Generate AI-powered suggestions via OpenAI
            st.subheader("🤖 AI Suggestions")
            suggestions = generate_suggestions(resume_text, jd)

            if suggestions:
                st.markdown(suggestions)
            else:
                st.info("Could not generate AI suggestions. Check your OPENAI_API_KEY.")
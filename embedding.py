import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer


def generate_embeddings(text_list):
    """
    Generate TF-IDF embeddings for a list of text strings.
    Returns a 2D numpy array: shape (num_texts, num_features).
    """
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(text_list)
    return vectors.toarray()


def get_resume_embedding(embeddings, num_chunks):
    """
    Average all resume chunk embeddings into a single vector.
    This gives a much better representation than just using the first chunk.

    Args:
        embeddings: Full embeddings array (chunks + JD).
        num_chunks: Number of resume chunks (not including JD).

    Returns:
        A single averaged embedding vector for the resume.
    """
    resume_embeddings = embeddings[:num_chunks]
    return np.mean(resume_embeddings, axis=0)
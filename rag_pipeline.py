def chunk_text(text, chunk_size=300):
    """
    Split text into chunks of approximately chunk_size words.

    Args:
        text: Input text string.
        chunk_size: Number of words per chunk.

    Returns:
        List of text chunk strings. Returns [""] if text is empty.
    """
    if not text or not text.strip():
        return [""]

    words = text.split()
    chunks = []

    for i in range(0, len(words), chunk_size):
        chunk = " ".join(words[i:i + chunk_size])
        chunks.append(chunk)

    return chunks
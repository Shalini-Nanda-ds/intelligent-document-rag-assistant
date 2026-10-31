
import streamlit as st

from src.rag_pipeline import answer_question
from src.utils.logger import get_logger

logger = get_logger(__name__)

st.set_page_config(
    page_title="Intelligent Document RAG Assistant",
    page_icon="📄",
    layout="centered",
)

st.title("📄 Intelligent Document RAG Assistant")

st.write(
    "Ask questions about the company leave policy. "
    "Answers are generated using the information in the PDF."
)

question = st.text_input(
    "Enter your question",
    placeholder="How many maternity leave weeks are allowed?",
)

if st.button("Get Answer", type="primary"):
    if not question.strip():
        st.warning("Please enter a question.")
    else:
        try:
            with st.spinner("Reading document and generating answer..."):
                logger.info("User submitted a question")
                answer = answer_question(question)

            st.subheader("Answer")
            st.success(answer)

        except Exception:
            logger.exception("Failed to answer user question")
            st.error(
                "Sorry, an error occurred while generating the answer. "
                "Please check logs/app.log."
            )

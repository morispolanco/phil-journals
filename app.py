import streamlit as st
from docx import Document
import re

# Configuración inicial de la página
st.set_page_config(page_title="Philosophy Manuscript Review Assistant", page_icon="📚")

# Título y descripción
st.title("Philosophy Manuscript Review Assistant")
st.write("""
Welcome to the Philosophy Manuscript Review Assistant! This tool helps authors determine if their manuscript meets the guidelines of top philosophy journals. 
Upload your manuscript, select the target journal, and receive personalized feedback.
""")

# Menú en la barra lateral para seleccionar la revista
st.sidebar.header("Select a Journal")
journal = st.sidebar.selectbox(
    "Choose the journal you are targeting:",
    [
        "Mind",
        "The Philosophical Review",
        "Journal of Philosophy",
        "Philosophy and Phenomenological Research",
        "Nous",
        "Ethics",
        "Philosophical Studies",
        "Synthese",
        "The Journal of Ethics",
        "Philosophy & Public Affairs"
    ]
)

# Cargar archivo Word
uploaded_file = st.file_uploader("Upload your manuscript (Word file)", type=["docx"])
if uploaded_file:
    st.success("File uploaded successfully!")
    document = Document(uploaded_file)
    
    # Extraer texto del manuscrito
    manuscript_text = "\n".join([para.text for para in document.paragraphs])
    st.subheader("Manuscript Preview")
    st.text_area("Manuscript Content", manuscript_text, height=300)
    
    # Verificar formato básico
    def check_format(text):
        word_count = len(re.findall(r'\w+', text))
        pages_estimate = word_count / 250  # Estimación: 250 palabras por página
        return {
            "word_count": word_count,
            "pages_estimate": pages_estimate
        }
    
    format_info = check_format(manuscript_text)
    
    # Feedback general
    st.subheader("General Feedback")
    st.write(f"- Estimated word count: **{format_info['word_count']}**")
    st.write(f"- Estimated page count: **{format_info['pages_estimate']:.1f} pages**")
    
    # Evaluar según la revista seleccionada
    if st.button("Evaluate Manuscript"):
        st.subheader(f"Evaluation for {journal}")
        
        if journal == "Mind":
            st.write(
                "- **Focus and Scope**: Your manuscript should address topics in analytic philosophy, including metaphysics, epistemology, philosophy of mind, and logic.\n"
                "- **Abstract**: Should be ≤ 250 words. Ensure it clearly outlines the problem, methods, and contributions.\n"
                f"- **Length**: Maximum 10,000 words. Your manuscript is estimated to be **{format_info['pages_estimate']:.1f} pages**."
            )
            if format_info['pages_estimate'] > 40:  # 10,000 palabras ≈ 40 páginas
                st.warning("Your manuscript exceeds the recommended length. Consider condensing content.")
        
        elif journal == "The Philosophical Review":
            st.write(
                "- **Focus and Scope**: Your manuscript should explore fundamental philosophical questions with clarity and rigor.\n"
                "- **Abstract**: Should be ≤ 200 words. Ensure it highlights the significance of your research.\n"
                f"- **Length**: Maximum 12,000 words. Your manuscript is estimated to be **{format_info['pages_estimate']:.1f} pages**."
            )
            if format_info['pages_estimate'] > 48:  # 12,000 palabras ≈ 48 páginas
                st.warning("Your manuscript exceeds the recommended length. Consider revising.")
        
        elif journal == "Journal of Philosophy":
            st.write(
                "- **Focus and Scope**: Your manuscript should contribute to debates in core areas of philosophy, such as ethics, metaphysics, or epistemology.\n"
                "- **Abstract**: Should be ≤ 150 words. Ensure it is concise and captures the essence of your argument.\n"
                f"- **Length**: Maximum 9,000 words. Your manuscript is estimated to be **{format_info['pages_estimate']:.1f} pages**."
            )
            if format_info['pages_estimate'] > 36:  # 9,000 palabras ≈ 36 páginas
                st.warning("Your manuscript exceeds the recommended length. Consider editing for brevity.")
        
        elif journal == "Philosophy and Phenomenological Research":
            st.write(
                "- **Focus and Scope**: Your manuscript should engage with phenomenology, existentialism, or related areas of analytic philosophy.\n"
                "- **Abstract**: Should be ≤ 200 words. Ensure it defines the research problem and its importance.\n"
                f"- **Length**: Maximum 10,000 words. Your manuscript is estimated to be **{format_info['pages_estimate']:.1f} pages**."
            )
            if format_info['pages_estimate'] > 40:  # 10,000 palabras ≈ 40 páginas
                st.warning("Your manuscript exceeds the recommended length. Consider revising.")
        
        elif journal == "Nous":
            st.write(
                "- **Focus and Scope**: Your manuscript should address topics in metaphysics, epistemology, philosophy of language, or philosophy of mind.\n"
                "- **Abstract**: Should be ≤ 150 words. Ensure it is clear and highlights the key contributions of your research.\n"
                f"- **Length**: Maximum 10,000 words. Your manuscript is estimated to be **{format_info['pages_estimate']:.1f} pages**."
            )
            if format_info['pages_estimate'] > 40:  # 10,000 palabras ≈ 40 páginas
                st.warning("Your manuscript exceeds the recommended length. Consider reducing content.")
        
        elif journal == "Ethics":
            st.write(
                "- **Focus and Scope**: Your manuscript should explore ethical theory, applied ethics, or moral philosophy.\n"
                "- **Abstract**: Should be ≤ 200 words. Ensure it clearly states the research problem and its significance.\n"
                f"- **Length**: Maximum 10,000 words. Your manuscript is estimated to be **{format_info['pages_estimate']:.1f} pages**."
            )
            if format_info['pages_estimate'] > 40:  # 10,000 palabras ≈ 40 páginas
                st.warning("Your manuscript exceeds the recommended length. Consider revising.")
        
        elif journal == "Philosophical Studies":
            st.write(
                "- **Focus and Scope**: Your manuscript should address topics in analytic philosophy, including metaphysics, epistemology, and philosophy of mind.\n"
                "- **Abstract**: Should be ≤ 150 words. Ensure it is concise and highlights the key contributions of your research.\n"
                f"- **Length**: Maximum 9,000 words. Your manuscript is estimated to be **{format_info['pages_estimate']:.1f} pages**."
            )
            if format_info['pages_estimate'] > 36:  # 9,000 palabras ≈ 36 páginas
                st.warning("Your manuscript exceeds the recommended length. Consider editing for brevity.")
        
        elif journal == "Synthese":
            st.write(
                "- **Focus and Scope**: Your manuscript should explore interdisciplinary topics in philosophy, including philosophy of science, epistemology, and logic.\n"
                "- **Abstract**: Should be ≤ 250 words. Ensure it clearly outlines the problem, methods, and contributions.\n"
                f"- **Length**: Maximum 12,000 words. Your manuscript is estimated to be **{format_info['pages_estimate']:.1f} pages**."
            )
            if format_info['pages_estimate'] > 48:  # 12,000 palabras ≈ 48 páginas
                st.warning("Your manuscript exceeds the recommended length. Consider condensing content.")
        
        elif journal == "The Journal of Ethics":
            st.write(
                "- **Focus and Scope**: Your manuscript should address ethical theory, normative ethics, or applied ethics.\n"
                "- **Abstract**: Should be ≤ 200 words. Ensure it is concise and captures the essence of your argument.\n"
                f"- **Length**: Maximum 10,000 words. Your manuscript is estimated to be **{format_info['pages_estimate']:.1f} pages**."
            )
            if format_info['pages_estimate'] > 40:  # 10,000 palabras ≈ 40 páginas
                st.warning("Your manuscript exceeds the recommended length. Consider revising.")
        
        elif journal == "Philosophy & Public Affairs":
            st.write(
                "- **Focus and Scope**: Your manuscript should explore the intersection of philosophy and public policy, including political philosophy and applied ethics.\n"
                "- **Abstract**: Should be ≤ 150 words. Ensure it clearly states the research problem and its significance.\n"
                f"- **Length**: Maximum 10,000 words. Your manuscript is estimated to be **{format_info['pages_estimate']:.1f} pages**."
            )
            if format_info['pages_estimate'] > 40:  # 10,000 palabras ≈ 40 páginas
                st.warning("Your manuscript exceeds the recommended length. Consider reducing content.")
        
        # Feedback adicional
        st.subheader("Additional Suggestions")
        st.write("""
- **Abstract**: Ensure it is clear, concise, and highlights the key contributions of your research.
- **Keywords**: Include 3–5 relevant keywords that reflect the core themes of your manuscript.
- **Formatting**: Use Times New Roman, size 12, double-spaced, with 1-inch margins.
- **References**: Follow the journal's specific citation style (e.g., Chicago or APA).
        """)

# Recursos adicionales
st.sidebar.header("Additional Resources")
st.sidebar.write("""
For more details, visit the official websites of the respective journals:
- [Mind](https://academic.oup.com/mind)
- [The Philosophical Review](https://read.dukeupress.edu/the-philosophical-review)
- [Journal of Philosophy](https://www.journalofphilosophy.org)
- [Philosophy and Phenomenological Research](https://onlinelibrary.wiley.com/journal/19331592)
- [Nous](https://onlinelibrary.wiley.com/journal/14680068)
- [Ethics](https://www.journals.uchicago.edu/toc/ethics/current)
- [Philosophical Studies](https://www.springer.com/journal/11098)
- [Synthese](https://www.springer.com/journal/11229)
- [The Journal of Ethics](https://www.springer.com/journal/10892)
- [Philosophy & Public Affairs](https://onlinelibrary.wiley.com/journal/10884246)
""")

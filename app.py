import streamlit as st
import spacy

# Load trained NER model
model_path = "trained_ner_model/model-best"  # Path to the best trained model
nlp = spacy.load(model_path)

st.title("Named Entity Recognition (NER) Agent")

# User input
user_input = st.text_area("Enter text for entity extraction:")

def highlight_entities(text, entities):
    for entity, label in entities:
        text = text.replace(entity, f'<mark class="{label}">{entity}</mark>')
    return text

if st.button("Analyze"):
    if user_input:
        doc = nlp(user_input)
        entities = [(ent.text, ent.label_) for ent in doc.ents]
        if entities:
            st.write("### Extracted Entities:")
            for entity, label in entities:
                st.write(f"- **{entity}** ({label})")
            
            # Highlight entities in the text
            highlighted_text = highlight_entities(user_input, entities)
            st.markdown(f'<div>{highlighted_text}</div>', unsafe_allow_html=True)
            
            # Legend
            st.write("### Legend:")
            labels = set(label for _, label in entities)
            for label in labels:
                st.markdown(f'<span class="{label}">{label}</span>', unsafe_allow_html=True)
        else:
            st.write("No named entities found.")

# CSS for highlighting
st.markdown("""
    <style>
    .PERSON { background-color: #ffcccc; }
    .ORG { background-color: #ccffcc; }
    .GPE { background-color: #ccccff; }
    .DATE { background-color: #ffffcc; }
    </style>
    """, unsafe_allow_html=True)
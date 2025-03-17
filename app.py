import streamlit as st
import streamlit.components.v1 as components
import spacy
from spacy import displacy
import pandas as pd

# Load trained NER model once
@st.cache_resource
def load_model():
    model_path = "trained_ner_model/model-best"  # Path to the best trained model
    return spacy.load(model_path)

nlp = load_model()

st.title("Named Entity Recognition (NER) Agent")

# User input
user_input = st.text_area("Enter text for entity extraction:")

def filter_entities(doc):
    return [ent for ent in doc.ents if ent.label_ in {"PERSON", "DATE", "ORG", "GPE", "EVENT"}]

if st.button("Analyze"):
    if user_input:
        doc = nlp(user_input)
        filtered_entities = filter_entities(doc)
        if filtered_entities:
            st.write("### Extracted Entities:")
            # Display filtered entities in a table
            entities = [(ent.text, ent.label_) for ent in filtered_entities]
            df = pd.DataFrame(entities, columns=["Entity", "Label"])
            st.table(df)
            
            # Highlight entities in the text using displacy
            html = displacy.render(doc, style="ent", jupyter=False, options={"ents": ["PERSON", "DATE", "ORG", "GPE", "EVENT"]})
            st.markdown(html, unsafe_allow_html=True)
        else:
            st.write("No entities found in the text.")
    else:
        st.write("Please enter some text to analyze.")
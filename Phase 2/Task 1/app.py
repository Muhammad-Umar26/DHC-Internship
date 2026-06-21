from pathlib import Path

import streamlit as st

st.set_page_config(page_title="News Classifier", page_icon="📰")
st.title("📰 News Topic Classifier")
st.write("Enter a news headline:")

MODEL_DIR = Path(__file__).resolve().parent / "saved_model"

@st.cache_resource
def load_model():
    from transformers import AutoModelForSequenceClassification, AutoTokenizer, pipeline

    tokenizer = AutoTokenizer.from_pretrained(MODEL_DIR, local_files_only=True)
    model = AutoModelForSequenceClassification.from_pretrained(MODEL_DIR, local_files_only=True)
    return pipeline("text-classification", model=model, tokenizer=tokenizer)

st.info("The model loads on the first classification request.")

user_input = st.text_area("Headline:", height=100)
category_map = {"LABEL_0": "🌍 World", "LABEL_1": "🏃 Sports", "LABEL_2": "💼 Business", "LABEL_3": "🔬 Sci/Tech"}

if st.button("Classify"):
    if user_input:
        with st.spinner("Analyzing..."):
            try:
                classifier = load_model()
                result = classifier(user_input)[0]
                st.success(f"**Category:** {category_map.get(result['label'], result['label'])}")
                st.metric("Confidence", f"{result['score']:.2%}")
            except Exception as e:
                st.error(f"❌ Prediction failed: {e}")
    else:
        st.warning("Please enter a headline.")
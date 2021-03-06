import streamlit as st
import spacy
# import spacy_streamlit
# from annotated_text import annotated_text


@st.cache(show_spinner=False, allow_output_mutation=True, suppress_st_warning=True)
def load_model():
    model = spacy.load("./models/en/")
    return model

def check_for_deps(sent):
  off_limits = ['csubj', 'csubjpass', 'relcl', 'advcl', 'mark']
  for i in sent:
    if i.dep_ in off_limits:
      return "NOT paratactic (sorry)" 
  return "PARATACTIC!! Nicely done." 

# def process_text(doc, selected_entities, anonymize=False):
#     tokens = []
#     for token in doc:
#         if (token.ent_type_ == "PERSON") & ("PER" in selected_entities):
#             tokens.append((token.text, "Person", "#faa"))
#         elif (token.ent_type_ in ["GPE", "LOC"]) & ("LOC" in selected_entities):
#             tokens.append((token.text, "Location", "#fda"))
#         elif (token.ent_type_ == "ORG") & ("ORG" in selected_entities):
#             tokens.append((token.text, "Organization", "#afa"))
#         else:
#             tokens.append(" " + token.text + " ")

#     if anonymize:
#         anonmized_tokens = []
#         for token in tokens:
#             if type(token) == tuple:
#                 anonmized_tokens.append(("X" * len(token[0]), token[1], token[2]))
#             else:
#                 anonmized_tokens.append(token)
#         return anonmized_tokens

#     return tokens


model = load_model()

# selected_language = st.sidebar.selectbox("Select a language", options=["en", "fr"])
# selected_entities = st.sidebar.multiselect(
#     "Select the entities you want to detect",
#     options=["LOC", "PER", "ORG"],
#     default=["LOC", "PER", "ORG"],
# )
# selected_model = models[selected_language]

text_input = st.text_area("Type a text to check for parataxis")

uploaded_file = st.file_uploader("or Upload a file", type=["doc", "docx", "pdf", "txt"])
if uploaded_file is not None:
    text_input = uploaded_file.getvalue()
    text_input = text_input.decode("utf-8")

# anonymize = st.checkbox("Anonymize")
# doc = selected_model(text_input)
# tokens = process_text(doc, selected_entities)

# annotated_text(*tokens)

# if anonymize:
#     st.markdown("**Anonymized text**")
#     st.markdown("---")
#     anonymized_tokens = process_text(doc, selected_entities, anonymize=anonymize)
#     annotated_text(*anonymized_tokens)

parataxis = st.checkbox("Check for parataxis")
doc = model(text_input)
msg = check_for_deps(doc)

if parataxis:
    st.markdown("**Parataxis test**")
    st.markdown("---")
    st.write(msg)

st.markdown("---")
# spacy_streamlit.visualize(selected_model, doc)
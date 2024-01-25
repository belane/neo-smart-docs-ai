import os
import openai
import streamlit as st
import streamlit.components.v1 as components
from llama_index import ServiceContext, StorageContext, load_index_from_storage

openai_api_key = os.environ.get("OPENAI_API_KEY")


# Loads Index from local storage
@st.cache_resource(show_spinner=False)
def load_indexes():
    openai.api_key = openai_api_key
    storage_context = StorageContext.from_defaults(persist_dir="./storage")
    index = load_index_from_storage(storage_context)
    return index


# Configure Page
page_icon = "https://neo.org/favicon.ico"
st.set_page_config(page_title="Neo Smart Docs", page_icon=page_icon)

# Custom CSS
with open("assets/css/style.css", "r") as f:
    css_text = f.read()
custom_css = f"<style>{css_text}</style>"
st.markdown(custom_css, unsafe_allow_html=True)
st.markdown(
    """
    <div class="red4secBrand">
        <a href="https://red4sec.com" target="_blank">
            <div><p>Developed with ❤️ by Red4Sec</p></div>
        </a>
    </div>
    """,
    unsafe_allow_html=True,
)

# Headings
l, center, r = st.columns(3)
with center:
    st.image("https://docs.neo.org/img/logo.svg", width=250)
l, center, r = st.columns([2, 5, 2])
with center:
    st.title("Neo Smart Docs", anchor=False)

# Query form
index = load_indexes()
col1, col2 = st.columns([6, 2])
with col1:
    query = st.text_input(
        "Question",
        key="question",
        label_visibility="hidden",
        placeholder="Ask any question about Neo blockchain",
    )
with col2:
    st.write("#")
    button = st.button("Search")

# Response
if query.strip() or (button and query.strip()):
    with st.spinner("Searching ..."):
        try:
            query_engine = index.as_query_engine(
                service_context=ServiceContext.from_defaults(num_output=512),
                similarity_top_k=4,
            )
            response = query_engine.query(query)
            st.caption("Response")
            st.info(response.response)

            st.caption("References")
            references = "- " + "\n- ".join(
                set([ref["file_path"] for ref in response.extra_info.values()])
            )
            st.markdown(references)
        except:
            st.error("Search error, please try again later.")

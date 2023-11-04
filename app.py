import streamlit as st


# Configure Page
page_icon = 'https://neo.org/favicon.ico'
st.set_page_config(page_title='Neo Smart Docs', page_icon=page_icon)

# Custom CSS
with open('assets/css/style.css', 'r') as f:
    css_text = f.read()
custom_css = f'<style>{css_text}</style>'
st.markdown(custom_css, unsafe_allow_html=True)
st.markdown('''
    <div class="red4secBrand">
        <a href="https://red4sec.com" target="_blank">
            <div><p>Developed with ❤️ by Red4Sec</p></div>
        </a>
    </div>
    ''', unsafe_allow_html=True)

# Headings
l, center, r = st.columns(3)
with center:
    st.image('https://docs.neo.org/img/logo.svg', width=250)
st.write(' ', anchor=False)

# Info
st.subheader('Neo APAC Hackathon is over🎉🎉🎉 Congratulations to all participants!!', anchor=False)
st.subheader('*Hop on your Neo rocket! The Neo Smart Docs project has been an intergalactic voyage of enlightenment. The mission is complete, but the star chart is available on [GitHub](https://github.com/belane/neo-smart-docs-ai).* 🚀🌠✨', anchor=False)

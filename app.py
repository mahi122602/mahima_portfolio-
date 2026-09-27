"""Mahima Thakar — Future Intelligence. Run: streamlit run app.py"""
import streamlit as st
import streamlit.components.v1 as components
from render import build_page

st.set_page_config(page_title='Mahima Thakar | Data Science & AI', page_icon='✦', layout='wide', initial_sidebar_state='collapsed')
# Keep the component's own responsive page as the only scrolling surface.
# Streamlit is pinned because these wrapper selectors depend on its markup.
st.html('''<style>
[data-testid="stHeader"], [data-testid="stToolbar"] {display:none!important}
[data-testid="stMainBlockContainer"] {padding:0!important;max-width:none!important}
[data-testid="stVerticalBlock"] {gap:0!important}
iframe[title="st.iframe"],iframe[title="streamlit.components.v1.html"] {
 height:100dvh!important;width:100%!important;border:0!important;display:block;
}
[data-testid="stMain"] {overflow:hidden!important}
.stApp {background:#eaf0f5}
</style>''')
components.html(build_page(), height=900, scrolling=True)

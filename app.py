import streamlit as st


#-----Page setup -----
about_page = st.Page(
    page ="pages/about_me.py",
    title ="About Me",
    icon =":material/account_circle:",
    default = True, # This is the first page that loads
)

sales_dashboard = st.Page(
    page ="pages/sales_dashboard.py",
    title ="Sales Dashboard",
    icon =":material/bar_chart:",
)

chatbot = st.Page(
    page = "pages/chatbot.py",
    title = "Chat Bot",
    icon = ":material/smart_toy:",
)

page_navigation = st.navigation(
    {
        "Info": [about_page],
        "Projects": [sales_dashboard, chatbot]
    }
)

st.logo("assets/Logo.png")
st.sidebar.text("Made With Love by Akindele Adebayo")

page_navigation.run()

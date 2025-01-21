import requests
import streamlit as st

# from streamlit_option_menu import option_menu

class __login__:
    def __init__(self):
        self.main()

    # def nav_sidebar(self):
    #     main_page_sidebar = st.sidebar.empty()
    #     with main_page_sidebar:
    #         selected_option = option_menu(
    #             menu_title = 'Login_Page',
    #             menu_icon = 'list-columns-reverse',
    #             icons = ['box-arrow-in-right', 'person-plus', 'x-circle','arrow-counterclockwise'],
    #             options = ['Login', 'Create Account', 'Forgot Password?', 'Reset Password'],
    #             styles = {
    #                 "container": {"padding": "5px"},
    #                 "nav-link": {"font-size": "14px", "text-align": "left", "margin":"0px"}} )
        
    def login_form(self):
        with st.form("login_form"):
            username = st.text_input("Username",placeholder="Enter Username", label_visibility="collapsed")
            password = st.text_input("Password",placeholder="Password", type="password", label_visibility="collapsed")
            submitted = st.form_submit_button("Login In", use_container_width=True)

            if submitted:
                # Flask 앱으로 로그인 요청 보내기
                response = requests.post("http://localhost:5000/login", data={"username": username, "password": password})

                if response.ok and response.json().get('success'):
                    st.session_state['logged_in'] = True
                    st.success("Logged in successfully!")
                    st.rerun() 
                else:
                    st.error("Login failed. Please check your credentials.")
    
    def main(self):
        st.markdown("<h1 style='text-align: center; color: #6495ED;'>Welcome</h1>", unsafe_allow_html=True)
        # self.nav_sidebar()

        col1, col2, col3 = st.columns([3.75, 2.5, 3.75])
        with col1:
            st.empty()

        with col2:
            st.markdown("<h4 style='text-align: center; color: black;'>Login Your Account</h4>", unsafe_allow_html=True)
            co1, co2, co3 = st.columns([4,1,5])
            with co1: st.empty()
            with co2: st.empty()
            with co3: st.empty()

            self.login_form()

        with col3:
            st.empty()

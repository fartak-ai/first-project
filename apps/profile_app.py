import time
import os
from typing import Dict
import streamlit as st
from hydralit import HydraHeadApp


# from .utils import check_usr_pass
# from .utils import load_lottieurl
# from .utils import check_valid_name
# from .utils import check_valid_email
# from .utils import check_unique_email
# from .utils import check_unique_usr
# from .utils import register_new_usr
# from .utils import check_email_exists
# from .utils import generate_random_passwd
# from .utils import send_passwd_in_email
# from .utils import change_passwd
# from .utils import check_current_passwd
# from .utils import create_connection
# from .utils import create_table
# from .utils import show_user_info

MENU_LAYOUT = [1,1,1,7,2]   

class ProfileApp(HydraHeadApp):
    
    def __init__(self, app, title = '', **kwargs):
        
        self.app = app
        self.__dict__.update(kwargs)
        self.title = title
 

    def run(self) -> None:

        # st.markdown("<h1 style='text-align: center;'>Profile</h1>", unsafe_allow_html=True)
        
        # st.title("User Profile Page")

        user_access_level, username = self.app.check_access()

        c1, c2, c3, c4, c5, c6, c7, c8 = st.columns([2, 2, 2, 2, 2, 2, 2, 2])
        pretty_btn = """
        <style>
        div[class="row-widget stButton"] > button {
            width: 100%;
        }
        </style>
        <br><br>
        """
        c6.markdown(pretty_btn, unsafe_allow_html=True)
        c7.markdown(pretty_btn, unsafe_allow_html=True)
        c8.markdown(pretty_btn, unsafe_allow_html=True)

                

        if user_access_level == 1:

            try:

                if c6.button('Supports'):
                    pass

                if c7.button('Create Account'):
                    # s = SignUp(self.app)
                    st.write('SignUp')

                if c8.button('Login'):
                    # p = LogIn(self.app)
                    st.write('LogIn')

                st.write('###')

                _,_,col_logo, col_text,_ = st.columns(MENU_LAYOUT)
                col_logo.image(os.path.join(".","resources","profile.png"),width=200,)

                st.markdown('<br><br>', unsafe_allow_html=True)

                c1,c2,c3, = st.columns([2,6,2])
                profile_form = c2.form(key="profile_form")

                c11, c22 = profile_form.columns([2, 2])

                c11.write(f'name:  ',)
                c22.write(f'last name:  ')

                c11.write('###')
                c22.write('###')

                c11.write(f'userName:  ')
                c22.write(f'age:  ')

                c11.write('###')
                c22.write('###')

                c11.write(f'Email:  ')
                c22.write(f'phone name:')

                c11.write('###')
                c22.write('###')

                profile_form.form_submit_button('')

            except:
                st.warning('please ...')


            

        if user_access_level > 1:

            try:
                
                if c6.button('Setting'):
                    pass

                if c7.button('Supports'):
                    pass

                if c8.button('Logout'):
                    pass
                
                # if col_header_text.button(''):
                #     self.do_redirect("https://hotstepper.readthedocs.io/index.html")

                # st.write('###')
                # st.write('###')
                st.write('###')

                _,_,col_logo, col_text,_ = st.columns(MENU_LAYOUT)
                col_logo.image(os.path.join(".","resources","profile.png"),width=200,)

                st.markdown('<br><br>', unsafe_allow_html=True)

                c1,c2,c3, = st.columns([2,6,2])
                profile_form = c2.form(key="profile_form")

                c11, c22 = profile_form.columns([2, 2])

                c11.write(f'name:  ',)
                c22.write(f'last name:  ')

                c11.write('###')
                c22.write('###')

                c11.write(f'userName:  ')
                c22.write(f'age:  ')

                c11.write('###')
                c22.write('###')

                c11.write(f'Email:  ')
                c22.write(f'phone name:')

                c11.write('###')
                c22.write('###')

                profile_form.form_submit_button('Edit Profile', )

                _,_,col_logo, col_text, col_btn = st.columns(MENU_LAYOUT)
                # if col_text.button('Solar Mach ➡️'):
                #     self.do_redirect('Solar Mach')
                # col_logo.button('Broken Tooth',)
                # col_text.button('restored Tooth')

                col_text.write('###')
                col_text.write('###')
                col_text.write('###')
                col_text.write('###')
                col_text.write('###')

                col_header_logo_left_far, col_header_logo_left,col_header_text,col_header_logo_right,col_header_logo_right_far = st.columns([1,2,2,2,1])
                col_header_logo_left.button('Broken Tooth')
                col_header_text.button('repairing tooth')
                col_header_logo_right.button('restored Tooth')


            
            except Exception as e:
                st.image(os.path.join(".","resources","failure.png"),width=100,)
                st.error('An error has occurred, someone will be punished for your inconvenience, we humbly request you try again.')
                st.error('Error details: {}'.format(e))

            

    def edit_profile(self):
        user_access_level, username = self.app.check_access()
        st.write(user_access_level)
        st.write(username)

        st.success("Profile updated successfully!")





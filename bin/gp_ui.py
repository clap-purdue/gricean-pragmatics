#!/usr/bin/python
from __future__ import annotations
import os

# from typing import Text, Dict, Optional
# from tempfile import TemporaryDirectory
import pandas as pd
import time


# Streamlit imports
import streamlit as st
import streamlit.components.v1 as components
from streamlit_option_menu import option_menu

# 1=sidebar menu, 2=horizontal menu, 3=horizontal menu w/ custom menu
EXAMPLE_NO = 1

def ui():
    components.html(
        """
                <div style="background-color:#475e5f;padding:10px;">
                <h2 style="color:white;text-align:center;font-size:30px">Gricean Pragmatics</h2>
                </div>
                """
    )
   
    def streamlit_menu(example=1):
        if example == 1:
            # 1. as sidebar menu
            with st.sidebar:
                selected = option_menu(
                    menu_title="Main Menu",  # required
                    options=["Naturalness", "SSM", "PRC"],  # required
                    menu_icon="cast",  # optional
                    default_index=0,  # optional
                )
            return selected

        if example == 2:
            # 2. horizontal menu w/o custom style
            selected = option_menu(
                menu_title=None,  # required
                options=["Naturalness", "SSM", "PRC"],  # required
                #icons=["house", "book", "envelope"],  # optional
                menu_icon="cast",  # optional
                default_index=0,  # optional
                orientation="horizontal",
            )
            return selected

        if example == 3:
            # 2. horizontal menu with custom style
            selected = option_menu(
                menu_title=None,  # required
                options=["Naturalness", "SSM", "PRC"],  # required
                #icons=["house", "book", "envelope"],  # optional
                menu_icon="cast",  # optional
                default_index=0,  # optional
                orientation="horizontal",
                styles={
                    "container": {"padding": "0!important", "background-color": "#fafafa"},
                    "icon": {"color": "orange", "font-size": "25px"},
                    "nav-link": {
                        "font-size": "25px",
                        "text-align": "left",
                        "margin": "0px",
                        "--hover-color": "#eee",
                    },
                    "nav-link-selected": {"background-color": "green"},
                },
            )
            return selected


    selected = streamlit_menu(example=EXAMPLE_NO)

    if selected == "Naturalness":
        st.title(f"You have selected {selected}")
    if selected == "SSM":
        st.title(f"You have selected {selected}")
    if selected == "PRC":
        st.title(f"You have selected {selected}")




if __name__ == "__main__":
    ui()
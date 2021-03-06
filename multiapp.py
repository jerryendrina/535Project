#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 05:55:59 2021

@author: jeremiasendrinajr
"""


import streamlit as st


#write a multi app object-oriented-program
class MultiApp:
    
    def __init__(self):
        self.apps = []
        
        
    #a function to create a page
    def add_app(self, title, func):
        
        self.apps.append({
            "title": title,
            "function": func
        })

    #a function to create a sidebar in the main page
    def run(self):
        app = st.sidebar.radio(
            'Click the page to display:',
            self.apps,
            format_func=lambda app: app['title'])

        app['function']()
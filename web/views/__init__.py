# coding: utf-8
#
from concurrent.futures import ThreadPoolExecutor
from .base import BaseRequestHandler
from .login import OpenIdLoginHandler, SimpleLoginHandler


class LogoutHandler(BaseRequestHandler):
    def get(self):
        self.clear_all_cookies()
        self.redirect("/login")


class MainHandler(BaseRequestHandler):
    def get(self):
        self.redirect("/devices")
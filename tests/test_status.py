import os
import unittest
import urlparse

import requests

BASE_URL = os.environ.get('BASE_URL') or 'http://pay.dev'
EXAMPLE_URL = BASE_URL
UI_URL = BASE_URL + ':8000'
SERVICE_URL = UI_URL + '/api/'


class TestStatuses(unittest.TestCase):

    def test_service_status(self):
        res = requests.get(SERVICE_URL)
        res.raise_for_status()

    def test_ui_status(self):
        res = requests.get(UI_URL)
        res.raise_for_status()


class TestRedirect(unittest.TestCase):

    def redirect(self, lang):
        res = requests.get(
            UI_URL, headers={'Accept-Language': lang}, allow_redirects=False)
        assert res.status_code == 302
        return urlparse.urlparse(res.headers['Location']).path

    def test_dbg(self):
        assert '/dbg/index.html' == self.redirect('dbg')

    def test_en(self):
        assert '/en/index.html' == self.redirect('en')

    def test_dbg_en(self):
        assert '/dbg/index.html' == self.redirect('dbg;q=0.7,en;q=0.3')

    def test_fr(self):
        assert '/en/index.html' == self.redirect('fr')

    def contents(self, lang):
        res = requests.get(UI_URL, headers={'Accept-Language': lang})
        assert res.status_code == 200
        return res.content.strip()

    def test_en_contents(self):
        assert 'An en page.' == self.contents('en')

    def test_dbg_contents(self):
        assert 'A dbg page.' == self.contents('dbg')

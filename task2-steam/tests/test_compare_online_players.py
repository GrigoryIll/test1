from base.test_base import TestBase
from pages.main_page import MainPage
from pages.about_page import AboutPage


class TestPlayersOnline(TestBase):

    def test_compare_online_players(self):
        self.main_page.click_about_button()
        online_players = self.about_page.get_online_players()
        players_now = self.about_page.get_players_now()
        assert online_players > players_now, "Игроков онлайн меньше чем играющих"
        self.about_page.click_store_button()

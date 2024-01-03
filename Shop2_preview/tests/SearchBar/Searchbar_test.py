import pytest
from pages.SearchBarFlow import SearchbarScripts

@pytest.mark.usefixtures("setup")

class Test:
    def test_Searchbar_denied(self):
        SearchbarElements = SearchbarScripts(self.driver)
        SearchbarElements.open_page()
        SearchbarElements.click_on_SearchbarInput_and_find_denied_result()
        assert SearchbarElements.is_NothingFound_displayed()
    def test_Searchbar_postive(self):
        SearchbarElements = SearchbarScripts(self.driver)
        SearchbarElements.open_page()
        SearchbarElements.click_on_SearchbarInputand_find_positive_result()
        assert SearchbarElements.is_SearchResults_displayed()
    def test_Searchbar_EmptySearch(self):
        SearchbarElements = SearchbarScripts(self.driver)
        SearchbarElements.open_page()
        SearchbarElements.click_on_Searchbar_Icon()





from .base import FunctionalTest



class MyListsTest(FunctionalTest):

    def test_logged_in_users_lists_are_saved_as_my_lists(self):
        # Edith é uma usuária logada
        self.create_pre_authenticated_session('edith@example.com')

        # Edith acessa a página inicial e começa uma lista
        self.browser.get(self.live_server_url)
        self.add_list_item('Reticulate splines')
        self.add_list_item('Immanentize eschaton')
        first_list_url = self.browser.current_url

        # Ela percebe o link para "my lists" pela primeira vez
        self.browser.find_element_by_link_text('My lists').click()

        # Ela percebe que sua lista está lá, nomeada de acordo com

        # o primeiro item da lista
        self.wait_for(
            lambda: self.browser.find_element_by_link_text('Reticulate splines')
        )
        self.browser.find_element_by_link_text('Reticulate splines').click()
        self.wait_for(
            lambda: self.assertEqual(self.browser.current_url, first_list_url)
        )

        # Ela decide iniciar outra lista, somente para conferir
        self.browser.get(self.live_server_url)
        self.add_list_item('Click cows')
        second_list_url = self.browser.current_url

        # Em "my lists", sua nova lista aparece
        self.browser.find_element_by_link_text('My lists').click()
        self.wait_for(
            lambda: self.browser.find_element_by_link_text('Click cows')
        )
        self.browser.find_element_by_link_text('Click cows').click()
        self.wait_for(
            lambda: self.assertEqual(self.browser.current_url, second_list_url)
        )

        # Ela faz logout A opção "my lists" desaparece
        self.browser.find_element_by_link_text('Log out').click()
        self.wait_for(lambda: self.assertEqual(
            self.browser.find_elements_by_link_text('My lists'),
            []
        ))

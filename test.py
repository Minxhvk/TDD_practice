
import unittest
from Menu import Menu
from MenuRepository import MenuRepository


class test_menu(unittest.TestCase):

    #  Set Test Data
    def setUp(self):
        self.menu = Menu("라면", 3000, 3)
        self.menu_1 = Menu("계란라면", 3000, 3)

        MenuRepository.save(self.menu)
        MenuRepository.save(self.menu_1)

    # Clear MenuRepository
    def tearDown(self):
        MenuRepository.menu_list.clear()

    # create Test
    def test_create_menu(self) -> None:
        menu = self.menu
        menu_1 = self.menu_1

        self.assertEqual(menu.get_name(), "라면")
        self.assertEqual(menu.get_price(), 3000)
        self.assertEqual(menu.get_amount(), 3)

        self.assertFalse(menu == menu_1)

    # Menu Save Test
    def test_save_menu(self) -> None:

        saved_menu = MenuRepository.get_menu_by_name(self.menu.get_name())
        save_menu_1 = MenuRepository.get_menu_by_name(self.menu_1.get_name())

        self.assertTrue(self.menu == saved_menu)
        self.assertFalse(self.menu == save_menu_1)

    # Menu IDX Test
    def test_menu_idx(self) -> None:

        menu_idx = MenuRepository.get_idx(self.menu)
        menu_1_idx = MenuRepository.get_idx(self.menu_1)

        self.assertEqual(0, menu_idx)
        self.assertEqual(1, menu_1_idx)

    # Edit Menu Name Test
    def test_edit_menu_name(self) -> None:

        MenuRepository.edit_menu_name(self.menu, "김치라면")

        edited_menu = MenuRepository.get_menu_by_name("김치라면")

        self.assertFalse(self.menu == edited_menu)

        self.assertTrue(
            Menu("김치라면", self.menu.get_price(),
                 self.menu.get_amount()) == edited_menu
        )

        with self.assertRaises(AttributeError):
            MenuRepository.get_menu_by_name("라면")

    # Edit Menu Price Test
    def test_edit_menu_price(self) -> None:

        MenuRepository.edit_menu_price(self.menu, 1000)

        edited_menu = MenuRepository.get_menu_by_name(self.menu.get_name())

        self.assertEqual(edited_menu.get_price(), 1000)
        self.assertFalse(self.menu == edited_menu)

    # Edit Menu Amount Test
    def test_edit_menu_amount(self) -> None:

        MenuRepository.edit_menu_amount(self.menu, 10)

        edited_menu = MenuRepository.get_menu_by_name(self.menu.get_name())

        self.assertEqual(edited_menu.get_amount(), 10)
        self.assertFalse(self.menu == edited_menu)

    def test_del_menu(self) -> None:

        MenuRepository.del_menu(self.menu)

        with self.assertRaises(AttributeError):
            MenuRepository.get_menu_by_name(self.menu.get_name())

        with self.assertRaises(AttributeError):
            MenuRepository.get_idx(self.menu)

    def test_get_list(self) -> None:

        menu_list = MenuRepository.get_menu_list()

        self.assertTrue(len(menu_list) == 2)
        self.assertTrue(self.menu in menu_list)
        self.assertTrue(self.menu_1 in menu_list)


if __name__ == '__main__':
    unittest.main()

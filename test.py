
import unittest
from Menu import Menu
from MenuRepository import MenuRepository


class test_menu(unittest.TestCase):

    #  Set Test Data
    def setUp(self):
        self.menu = Menu("라면", 3000, 3)
        self.menu_1 = Menu("계란라면", 3000, 3)

    # Clear MenuRepository
    def tearDown(self):
        MenuRepository.menu_list.clear()

    # create Test
    def test_create_menu(self) -> None:

        self.assertEqual(self.menu.get_name(), "라면")
        self.assertEqual(self.menu.get_price(), 3000)
        self.assertEqual(self.menu.get_amount(), 3)

        self.assertFalse(self.menu.equals(self.menu_1))

    # Menu Save Test
    def test_save_menu(self) -> None:

        MenuRepository.save(self.menu)
        MenuRepository.save(self.menu_1)

        saved_menu = MenuRepository.get_menu_by_name(self.menu.get_name())
        save_menu_1 = MenuRepository.get_menu_by_name(self.menu_1.get_name())

        self.assertTrue(self.menu.equals(saved_menu))
        self.assertFalse(self.menu.equals(save_menu_1))

    # Menu IDX Test
    def test_menu_idx(self) -> None:

        MenuRepository.save(self.menu)
        MenuRepository.save(self.menu_1)

        menu_idx = MenuRepository.get_idx(self.menu)
        menu_1_idx = MenuRepository.get_idx(self.menu_1)

        self.assertEqual(0, menu_idx)
        self.assertEqual(1, menu_1_idx)

    # Edit Menu Name Test
    def test_edit_menu_name(self) -> None:

        MenuRepository.save(self.menu)

        MenuRepository.edit_menu_name(self.menu, "김치라면")

        edited_menu = MenuRepository.get_menu_by_name("김치라면")

        self.assertFalse(self.menu.equals(edited_menu))
        self.assertTrue(Menu("김치라면", self.menu.get_price(),
                        self.menu.get_amount()).equals(edited_menu))

        with self.assertRaises(AttributeError):
            MenuRepository.get_menu_by_name("라면")

    # Edit Menu Price Test
    def test_edit_menu_price(self) -> None:

        menu_name = self.menu.get_name()

        MenuRepository.save(self.menu)

        MenuRepository.edit_menu_price(self.menu, 1000)

        edited_menu = MenuRepository.get_menu_by_name(menu_name)

        self.assertEqual(edited_menu.get_price(), 1000)
        self.assertFalse(self.menu.equals(edited_menu))

    # Edit Menu Amount Test
    def test_edit_menu_amount(self) -> None:

        menu_name = self.menu.get_name()

        MenuRepository.save(self.menu)

        MenuRepository.edit_menu_amount(self.menu, 10)

        edited_menu = MenuRepository.get_menu_by_name(menu_name)

        self.assertEqual(edited_menu.get_amount(), 10)
        self.assertFalse(self.menu.equals(edited_menu))

    def test_del_menu(self) -> None:

        MenuRepository.save(self.menu)

        MenuRepository.del_menu(self.menu)

        with self.assertRaises(AttributeError):
            MenuRepository.get_menu_by_name(self.menu.get_name())
            MenuRepository.get_idx(self.menu)


if __name__ == '__main__':
    unittest.main()

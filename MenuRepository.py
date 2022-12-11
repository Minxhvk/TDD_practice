

from Menu import Menu


class MenuRepository:
    menu_list = []

    @staticmethod
    def save(menu) -> None:
        MenuRepository.menu_list.append(menu)

    @staticmethod
    def get_menu_by_name(name) -> Menu:
        for i in MenuRepository.menu_list:
            if i.get_name() == name:
                return i

        raise AttributeError

    @staticmethod
    def get_idx(menu) -> int:
        for idx, i in enumerate(MenuRepository.menu_list):
            if i == menu:
                return idx

        raise AttributeError

    @staticmethod
    def edit_menu_name(want_change_menu, new_name) -> None:

        origin_idx = MenuRepository.get_idx(want_change_menu)
        change_menu = Menu(new_name, want_change_menu.get_price(),
                           want_change_menu.get_amount())

        MenuRepository.edit_menu_list(origin_idx, change_menu)

    @staticmethod
    def edit_menu_price(want_change_menu, new_price) -> None:

        origin_idx = MenuRepository.get_idx(want_change_menu)
        change_menu = Menu(want_change_menu.get_name(),
                           new_price, want_change_menu.get_amount())

        MenuRepository.edit_menu_list(origin_idx, change_menu)

    @staticmethod
    def edit_menu_amount(want_change_menu, new_amount) -> None:

        origin_idx = MenuRepository.get_idx(want_change_menu)
        change_menu = Menu(want_change_menu.get_name(),
                           want_change_menu.get_price(), new_amount)

        MenuRepository.edit_menu_list(origin_idx, change_menu)

    @staticmethod
    def del_menu(menu) -> None:
        MenuRepository.menu_list.remove(menu)

    @staticmethod
    def get_menu_list() -> list:
        return MenuRepository.menu_list

    @staticmethod
    def edit_menu_list(idx, menu) -> None:
        MenuRepository.menu_list[idx] = menu

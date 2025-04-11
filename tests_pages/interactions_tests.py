import time

import allure

from pages.interactions_page import SortablePage, SelectablePage, ResizablePage, DroppablePage, DragabblePage

@allure.suite("Interactions")
class TestInteractions:

    @allure.feature("Sortable Page")
    class TestSortablePage:

        @allure.title("Check changed sortable list and grid")
        def test_sortable(self, driver):
            sortable_page = SortablePage(driver, "https://demoqa.com/sortable")
            sortable_page.open()
            list_before, list_after = sortable_page.change_list_order()
            grid_before, grid_after = sortable_page.change_grid_order()
            assert list_before != list_after, "the order of the list has not been changed"
            assert grid_before != grid_after, "the order of the grid has not been changed"

    @allure.feature("Selectable Page")
    class TestSelectablePage:

        @allure.title("Check changed selectable list and grid")
        def test_selectable(self, driver):
            selectable_page = SelectablePage(driver, "https://demoqa.com/selectable")
            selectable_page.open()
            item_list = selectable_page.select_list_item()
            grid_list = selectable_page.select_grid_item()
            assert len(item_list) > 0, "No elements were selected"
            assert len(grid_list) > 0, "No elements were selected"

    @allure.feature("Resizable Page")
    class TestResizablePage:

        @allure.title("Check changed resizable boxes")
        def test_resizable(self, driver):
            resizable_page = ResizablePage(driver, "https://demoqa.com/resizable")
            resizable_page.open()
            max_box, min_box = resizable_page.check_size_resizable_box()
            max_resize, min_resize = resizable_page.check_size_resizable()
            assert ('500px', '300px') == max_box, "maximum size not equal '500px', '300px'"
            assert ('150px', '150px') == min_box, "minimum size not equal '150px', '150px'"
            assert max_resize != min_resize, "resizable has not been changed"

    @allure.feature("Droppable Page")
    class TestDroppable:

        @allure.title("Check simple droppable")
        def test_simple_droppable(self, driver):
            droppable_page = DroppablePage(driver, "https://demoqa.com/droppable")
            droppable_page.open()
            text = droppable_page.drop_simple()
            assert text == "Dropped!", "the element has not been dropped"

        @allure.title("Check accept droppable")
        def test_accept_droppable(self, driver):
            droppable_page = DroppablePage(driver, "https://demoqa.com/droppable")
            droppable_page.open()
            not_acceptable, acceptable = droppable_page.drop_accept()
            assert not_acceptable == "here Dropped!", "the element has been accepted"
            assert acceptable == "Dropped!", "the element has not been accepted"

        @allure.title("Check prevent propogation droppable")
        def test_revent_propogation_droppable(self, driver):
            droppable_page = DroppablePage(driver, "https://demoqa.com/droppable")
            droppable_page.open()
            not_greedy, not_greedy_inner, greedy, greedy_inner = droppable_page.drop_prevent_propogation()
            assert not_greedy == "Dropped!", "the element text has not been changed"
            assert not_greedy_inner == "Dropped!", "the element text has not been changed"
            assert greedy == "Outer droppable", "the element text has been changed"
            assert greedy_inner == "Dropped!", "the element text has not been changed"

        @allure.title("Check revert draggable droppable")
        def test_revert_draggable_droppable(self, driver):
            droppable_page = DroppablePage(driver, "https://demoqa.com/droppable")
            droppable_page.open()
            after_move, after_revert = droppable_page.drop_revert_draggable("will")
            not_after_move, not_after_revert = droppable_page.drop_revert_draggable("not_will")
            assert after_move != after_revert, "the element has not reverted"
            assert not_after_move == not_after_revert, "the element has reverted"

    @allure.feature("Draggable Page")
    class TestDragabble:

        def test_simple_dragabble(self, driver):
            dragabble_page = DragabblePage(driver, "https://demoqa.com/dragabble")
            dragabble_page.open()
            before, after = dragabble_page.simple_drag_box()
            assert before != after, "the position of the box has not been changed"

        @allure.title("Check simple draggable")
        def test_axis_restricted_dragabble(self, driver):
            dragabble_page = DragabblePage(driver, "https://demoqa.com/dragabble")
            dragabble_page.open()
            top_x, left_x = dragabble_page.axis_restricted_x()
            top_y, left_y = dragabble_page.axis_restricted_y()
            assert (top_x[0][0] == top_x[1][0] and
                    int(top_x[1][0]) == 0),"box position has not changed or there has been a shift in the y-axis"
            assert (left_x[0][0] != left_x[1][0]
                    and int(left_x[1][0]) !=0), "box position has not changed or there has been a shift in the y-axis"
            assert (top_y[0][0] != top_y[1][0]
                    and int(top_y[1][0]) != 0), "box position has not changed or there has been a shift in the x-axis"
            assert (left_y[0][0] == left_y[1][0]
                    and int(left_y[1][0]) == 0), "box position has not changed or there has been a shift in the x-axis"

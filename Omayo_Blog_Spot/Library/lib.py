from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.expected_conditions import visibility_of_element_located, element_to_be_clickable
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class Base:

    def __init__(self,driver,ActionChains):
     self.driver=driver
     self.actions=ActionChains(self.driver)


    def actionchanins_click(self,locator):
        element=self.search_for_an_element(locator)
        self.actions.click(element).perform()

    def actionchanins_double_click(self, locator):
        element=self.search_for_an_element(locator)
        self.actions.double_click(element).perform()

    def actionchanins_right_click(self, locator):
        self.search_for_an_element(locator)
        self.actions.context_click().perform()

    def hovering(self, locator):
        element=self.search_for_an_element(locator)
        self.actions.move_to_element(element)

    def actions_drag_and_drop(self, locator,locator2):
        source_element=self.search_for_an_element(locator)
        target_element=self.search_for_an_element(locator2)
        self.actions.drag_and_drop(source_element,target_element)

    def search_for_an_element(self,locator):
        element=self.driver.find_element(*locator)
        return element

    def click_on_an_element(self,locator):
        element=self.search_for_an_element(locator)
        element.click()

    def clear_a_text(self,locator):
        element=self.search_for_an_element(locator)
        element.clear()

    def send_text(self,locator,text):
        element=self.search_for_an_element(locator)
        element.send_keys(text)

    def Submit(self,locator):
        element=self.search_for_an_element(locator)
        element.submit()

    def accept_an_alert(self):
        alert=self.driver.switch_to.alert
        alert.accept()

    def dismiss_an_alert(self):
        alert = self.driver.switch_to.alert
        alert.dismiss()

    def sendtext_to_an_alert(self,text):
        alert = self.driver.switch_to.alert
        alert.send_keys(text)

    def switch_window(self):
        self.driver.find_element("id","link1").click()
        parent_window = self.driver.current_window_handle
        handles = self.driver.window_handles

        for handle in handles:
                self.driver.switch_to.new_window(handle)

        self.driver.switch_to.window(parent_window)

    def switch_to_frame(self):
        self.driver.switch_to.frame(self.driver.find_element("id","navbar-iframe"))

    def switch_to_default_frame(self):
        self.driver.switch_to.default_content()

    def switch_to_parent_frame(self):
        self.driver.switch_to.parent()

    def wait_for_visiability(self,locator,timeout):
        wait=WebDriverWait(self.driver,timeout)
        condition=visibility_of_element_located(locator)
        element=wait.until(condition)
        element.click()

    def wait_for_element_clickable(self, locator, timeout):
        wait = WebDriverWait(self.driver, timeout)
        condition =element_to_be_clickable(locator)
        element = wait.until(condition)
        element.click()

    def Back(self):
        self.driver.back()

    def select_an_option(self,locator1,locator2):
        select_class=self.search_for_an_element(locator1)
        s1=Select(select_class)
        element=self.search_for_an_element(locator2)
        s1.select_by_visible_text(element.text)

    def deselect_an_option(self,locator1):
        select_class = self.search_for_an_element(locator1)
        s1 = Select(select_class)
        s1.deselect_all()



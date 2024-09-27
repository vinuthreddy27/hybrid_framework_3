from time import sleep

from Omayo_Blog_Spot.Library.lib import Base
from Omayo_Blog_Spot.utilities.locatorsHub import omayo_blogspot_loctors


class Omayo(Base):

    def omayo(self,text,file,text2,text3,query,lastname,text1,file2):

        self.send_text(omayo_blogspot_loctors.text_area,text2)

        self.switch_to_frame()

        self.send_text(omayo_blogspot_loctors.query,query)

        self.click_on_an_element(omayo_blogspot_loctors.search_icon)

        self.switch_to_default_frame()

        self.select_an_option(omayo_blogspot_loctors.select_class,omayo_blogspot_loctors.option)

        self.select_an_option(omayo_blogspot_loctors.select_class,omayo_blogspot_loctors.option1)

        self.select_an_option(omayo_blogspot_loctors.select_class,omayo_blogspot_loctors.option2)

        self.select_an_option(omayo_blogspot_loctors.select_class,omayo_blogspot_loctors.option3)

        self.deselect_an_option(omayo_blogspot_loctors.select_class)

        self.send_text(omayo_blogspot_loctors.text_area,text2)

        self.clear_a_text(omayo_blogspot_loctors.text_area2)

        self.send_text(omayo_blogspot_loctors.text_area2,text3)

        self.clear_a_text(omayo_blogspot_loctors.textbox)

        self.send_text(omayo_blogspot_loctors.textbox,text)

        self.click_on_an_element(omayo_blogspot_loctors.submit_btn)

        self.click_on_an_element(omayo_blogspot_loctors.login_btn)

        self.click_on_an_element(omayo_blogspot_loctors.register_btn)

        self.click_on_an_element(omayo_blogspot_loctors.alert)
        self.accept_an_alert()

        self.send_text(omayo_blogspot_loctors.upload_file,file)

        self.click_on_an_element(omayo_blogspot_loctors.checkbox)

        self.click_on_an_element(omayo_blogspot_loctors.checkbox2)

        self.click_on_an_element(omayo_blogspot_loctors.checkbox3)

        self.click_on_an_element(omayo_blogspot_loctors.checkbox4)

        self.click_on_an_element(omayo_blogspot_loctors.checkbox5)

        self.click_on_an_element(omayo_blogspot_loctors.checkbox6)

        self.click_on_an_element(omayo_blogspot_loctors.male_radiobtn)

        self.click_on_an_element(omayo_blogspot_loctors.female_radiobtn)

        self.click_on_an_element(omayo_blogspot_loctors.radio_btn1)

        self.click_on_an_element(omayo_blogspot_loctors.radio_btn2)

        self.click_on_an_element(omayo_blogspot_loctors.radio_btn3)

        # self.click_on_an_element(omayo_blogspot_loctors.dropdown_btn)
        #
        # self.wait_for_visiability(omayo_blogspot_loctors.facebook_link,5)
        #
        # self.click_on_an_element(omayo_blogspot_loctors.check_this_locator)
        #
        # self.Back()
        #
        # self.wait_for_element_clickable(omayo_blogspot_loctors.checkbox7,11)
        #
        self.click_on_an_element(omayo_blogspot_loctors.link4)
        #
        # self.send_text(omayo_blogspot_loctors.ln,lastname)
        #
        # self.send_text(omayo_blogspot_loctors.hidden,text1)

        self.click_on_an_element(omayo_blogspot_loctors.bike)

        self.click_on_an_element(omayo_blogspot_loctors.boat)

        self.click_on_an_element(omayo_blogspot_loctors.car)

        self.click_on_an_element(omayo_blogspot_loctors.car)

        self.click_on_an_element(omayo_blogspot_loctors.male)

        self.click_on_an_element(omayo_blogspot_loctors.female)

        self.send_text(omayo_blogspot_loctors.file,file2)

        self.select_an_option(omayo_blogspot_loctors.select_locator,omayo_blogspot_loctors.option_locator)

        self.select_an_option(omayo_blogspot_loctors.select_locator, omayo_blogspot_loctors.option_locator1)

        self.select_an_option(omayo_blogspot_loctors.select_locator, omayo_blogspot_loctors.option_locator2)

        self.select_an_option(omayo_blogspot_loctors.select_locator, omayo_blogspot_loctors.option_locator3)

        self.select_an_option(omayo_blogspot_loctors.select_locator, omayo_blogspot_loctors.option_locator4)

        self.select_an_option(omayo_blogspot_loctors.select_locator, omayo_blogspot_loctors.option_locator5)

        self.select_an_option(omayo_blogspot_loctors.class_select,omayo_blogspot_loctors.select_option1)
        self.click_on_an_element(omayo_blogspot_loctors.arrow_btn)

        self.select_an_option(omayo_blogspot_loctors.class_select, omayo_blogspot_loctors.select_option2)
        self.click_on_an_element(omayo_blogspot_loctors.arrow_btn)

        self.select_an_option(omayo_blogspot_loctors.class_select, omayo_blogspot_loctors.select_option3)
        self.click_on_an_element(omayo_blogspot_loctors.arrow_btn)

        self.select_an_option(omayo_blogspot_loctors.class_select, omayo_blogspot_loctors.select_option4)
        self.click_on_an_element(omayo_blogspot_loctors.arrow_btn)

        self.select_an_option(omayo_blogspot_loctors.class_select, omayo_blogspot_loctors.select_option5)
        self.click_on_an_element(omayo_blogspot_loctors.arrow_btn)

        self.select_an_option(omayo_blogspot_loctors.class_select, omayo_blogspot_loctors.select_option6)
        self.click_on_an_element(omayo_blogspot_loctors.arrow_btn)

        self.select_an_option(omayo_blogspot_loctors.class_select, omayo_blogspot_loctors.select_option7)
        self.click_on_an_element(omayo_blogspot_loctors.arrow_btn)

        self.select_an_option(omayo_blogspot_loctors.class_select, omayo_blogspot_loctors.select_option8)
        self.click_on_an_element(omayo_blogspot_loctors.arrow_btn)

        self.select_an_option(omayo_blogspot_loctors.class_select, omayo_blogspot_loctors.select_option9)
        self.click_on_an_element(omayo_blogspot_loctors.arrow_btn)
        self.select_an_option(omayo_blogspot_loctors.class_select, omayo_blogspot_loctors.select_option10)

        self.click_on_an_element(omayo_blogspot_loctors.arrow_btn)
        self.select_an_option(omayo_blogspot_loctors.class_select, omayo_blogspot_loctors.select_option11)

        self.click_on_an_element(omayo_blogspot_loctors.arrow_btn)

        self.click_on_an_element(omayo_blogspot_loctors.t_alert)
        self.accept_an_alert()
        sleep(1)

        self.click_on_an_element(omayo_blogspot_loctors.t1_alert)
        sleep(1)
        self.dismiss_an_alert()

        self.click_on_an_element(omayo_blogspot_loctors.t2_alert)
        sleep(1)
        self.accept_an_alert()

        self.select_an_option(omayo_blogspot_loctors.class_select2, omayo_blogspot_loctors.select_option1)
        self.click_on_an_element(omayo_blogspot_loctors.arrow_btn2)

        self.select_an_option(omayo_blogspot_loctors.class_select2, omayo_blogspot_loctors.select_option2)
        self.click_on_an_element(omayo_blogspot_loctors.arrow_btn2)

        self.select_an_option(omayo_blogspot_loctors.class_select2, omayo_blogspot_loctors.select_option3)
        self.click_on_an_element(omayo_blogspot_loctors.arrow_btn2)

        self.select_an_option(omayo_blogspot_loctors.class_select2, omayo_blogspot_loctors.select_option4)
        self.click_on_an_element(omayo_blogspot_loctors.arrow_btn2)

        self.select_an_option(omayo_blogspot_loctors.class_select2, omayo_blogspot_loctors.select_option5)
        self.click_on_an_element(omayo_blogspot_loctors.arrow_btn2)

        self.select_an_option(omayo_blogspot_loctors.class_select2, omayo_blogspot_loctors.select_option6)
        self.click_on_an_element(omayo_blogspot_loctors.arrow_btn2)

        self.select_an_option(omayo_blogspot_loctors.class_select2, omayo_blogspot_loctors.select_option7)
        self.click_on_an_element(omayo_blogspot_loctors.arrow_btn2)

        self.select_an_option(omayo_blogspot_loctors.class_select2, omayo_blogspot_loctors.select_option8)
        self.click_on_an_element(omayo_blogspot_loctors.arrow_btn2)

        self.select_an_option(omayo_blogspot_loctors.class_select2, omayo_blogspot_loctors.select_option9)
        self.click_on_an_element(omayo_blogspot_loctors.arrow_btn2)

        self.select_an_option(omayo_blogspot_loctors.class_select2, omayo_blogspot_loctors.select_option10)
        self.click_on_an_element(omayo_blogspot_loctors.arrow_btn2)

        self.select_an_option(omayo_blogspot_loctors.class_select2, omayo_blogspot_loctors.select_option11)
        self.click_on_an_element(omayo_blogspot_loctors.arrow_btn2)

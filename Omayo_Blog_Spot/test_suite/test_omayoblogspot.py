from selenium.webdriver import ActionChains

from Omayo_Blog_Spot.POM.blogspot_page import Omayo
from Omayo_Blog_Spot.utilities.locatorsHub import omayo_blogspot_loctors


def test_Obs(driver):
    bs_page=Omayo(driver,ActionChains)
    bs_page.omayo("vinuth",
                  "C:/Users/swath/Downloads",
                  "hey hii vinuth good morning.....",
                  "i............",
                  "Instagram",
                  "reddy",
                  "jyothi",
                  "C:/Users/swath/OneDrive/Pictures/Saved Pictures/PRO1.png")


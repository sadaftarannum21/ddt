import os
import time
from pathlib import Path

import pandas as pd
import requests as rq
from selenium.webdriver import Firefox
from selenium.webdriver import FirefoxOptions
from selenium.webdriver import FirefoxProfile
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class ScraperUberFares:
    """
    ScrapperUberFares is an entity that scrapes data.
    There are two types of scraping, static and dynamic.
    For static, we can use the self._request(url) method.
    This involves capturing the number of pages.
    Then filtering the data. Lastly saving it.
    For dynamic, we can use the self._se_browser(url) method.
    This invokes the selenium framework and preloads the javascript.
    Then filter the data. Lastly save it.
    """

    def __init__(self, url: str):
        self._url = url
        # self._se_browser(url)  # use with selenium for scraping dynamic web pages
        # self._request(url)   # use with requests for scraping static web pages

    @property
    def url(self):
        return self._url

    @property
    def display(self):
        """Return an integer, total number of pages."""
        # TODO: scrape.py - capture the total number of pages available
        return ""

    @property
    def count(self):
        """Return an integer, total number of pages that are accessible."""
        # TODO: scrape.py - capture the total number of pages accessible
        return self.display

    def _get_page(self):
        """Method to scrape the data from a page."""
        # TODO: scrape.py - get page that we will use to scrape the data
        return ""

    def _get_results(self):
        """Build a DataFrame with the results."""
        # TODO: scrape.py - render the data onto a variable
        results = self._get_page()
        return ""

    def _clean_results(self):
        """Clean the DataFrame with results."""
        # TODO: scrape.py - clean the data we want from the csv file that was loaded into memory
        return ""

    @staticmethod
    def _request(url: str):
        """Get data from a static page"""
        r = rq.get(url)
        print(r.text)
        return r.status_code, r.content

    def _se_browser(self, ur):
        """When csv data isn't predefined in a file
            , check to see if it's available for download
            , then stash it in a folder
            , otherwise Selenium browser gets instantiated
            , loads a page with desired dataset
            , dynamically loads the content
            , scrape and filters the data
            , then put into a csv"""
        profile = self._se_profile()
        options = self._se_options(profile)
        driver = Firefox(options)
        self._se_initiator(driver)
        # driver.get(url=self._url)
        # if self._se_capture_csv() is None:
        #     print('csv data does not exist')
        # self._se_dl_btn_content(driver)
        # self._se_dl_btn_filter(driver)
        # self._se_dynamic_content(driver)
        # self._se_dynamic_filter(driver)
        # functionality: `driver.quit()` is used to terminate the entire browser session and all of its process
        # effect: terminates all windows and tabs then release all WebDriver system resources
        # use case: use this when we are done with the entire script and want to clean up
        driver.quit()

    @staticmethod
    def _se_profile():
        pref_folder_location = 2  # 0 desktop 1 download 2 custom
        pref_folder_list = "browser.download.folderList"
        pref_dl_dir_flag = "browser.download.useDownloadDir"
        pref_dl_dir = "browser.download.dir"
        pref_ui_dialog_flag = "browser.download.manager.showWhenStarting"
        firefox_profile_path = f'{os.getenv("USERPROFILE")}' + r'\AppData\Roaming\Mozilla\Firefox\Profiles'
        firefox_download_path = f'{os.path.abspath(os.curdir)}' + r'\stash\virtual\se\dl'

        firefox_profile = FirefoxProfile(firefox_profile_path)
        firefox_profile.set_preference(pref_folder_list, pref_folder_location)
        firefox_profile.set_preference(pref_dl_dir, firefox_download_path)
        firefox_profile.set_preference(pref_dl_dir_flag, True)
        firefox_profile.set_preference(pref_ui_dialog_flag, False)
        firefox_profile.set_preference("browser.helperApps.neverAsk.saveToDisk"
                                       , "application/csv, text/csv")
        return firefox_profile

    @staticmethod
    def _se_options(profile):
        opts = FirefoxOptions()
        opts.add_argument("--headless")
        opts.capabilities["browserVersion"] = "128.0.2"
        opts.profile = profile
        return opts

    @staticmethod
    def _se_initiator(driver):
        driver.implicitly_wait(3.0)

    @staticmethod
    def _se_capture_csv():
        df = None
        root = os.path.abspath(os.curdir)
        path = f'{root}' + r'\data\artifact - rideshare-uber\archive.csv'
        if Path(path).exists():
            try:
                df = pd.read_csv(path)
                # for col_i, col in df.items():
                #     for row_j, row in col.items():
                #         print(f'df[{col_i}][{row_j}]:{row}')
            except ValueError as exception:
                print(f'exception: {exception}')
        return df

    @staticmethod
    def _se_dl_btn_content(driver):
        _css_selector_dl_btn = ".hUcBki"
        _wait_dynamic_load = 0.5
        _wait_driver_timeout = 1.5
        _wait_se_short_load = 1.0
        _wait_se_long_load = 3.0
        dl_btn = WebDriverWait(driver, _wait_driver_timeout).until(
            expected_conditions.presence_of_element_located((By.CSS_SELECTOR, _css_selector_dl_btn))
        )
        if dl_btn:
            print("Button Found ")
            dl_btn.click()
            time.sleep(_wait_se_short_load)
            _token_xpath_email_btn = ('//*[@id="site-content"]/div[2]/div/div/div[1]/form/div/'
                                      'div/div[1]/button[2]')
            email_btn = driver.find_element(By.XPATH, _token_xpath_email_btn)
            if email_btn:
                email_btn.click()
                time.sleep(_wait_se_short_load)
                id_u = '//*[@id=":r0:"]'
                username_box = WebDriverWait(driver, _wait_driver_timeout).until(
                    expected_conditions.presence_of_element_located((By.XPATH, id_u)))
                id_p = '//*[@id=":r1:"]'
                password_box = WebDriverWait(driver, _wait_driver_timeout).until(
                    expected_conditions.presence_of_element_located((By.XPATH, id_p)))
                if username_box and password_box:
                    username_box.send_keys('USERNAME')
                    password_box.send_keys('PASSWORD')
                    _css_selector_singin_btn = ".cimwuy"
                    signin_btn = driver.find_element(By.CSS_SELECTOR, _css_selector_singin_btn)
                    signin_btn.click()
                    time.sleep(_wait_se_long_load)
                    _dl_btn = WebDriverWait(driver, _wait_driver_timeout).until(
                        expected_conditions.presence_of_element_located((By.CSS_SELECTOR, _css_selector_dl_btn))
                    )
                    _dl_btn.click()
                    time.sleep(_wait_se_short_load)
        else:
            print("Button Error")
        return

    @staticmethod
    def _se_dl_btn_filter(driver):
        # TODO: scrape.py - filter the data we want from the csv file
        return

    @staticmethod
    def _se_dynamic_content(driver):
        _js_update_scroller = "arguments[0].scrollTop = arguments[0].scrollHeight;"
        _js_return_scroller_top = "return arguments[0].scrollTop;"
        _js_return_scroller_height = "return arguments[0].scrollHeight;"
        _css_selector_scroller = ".gpTZlZ"
        _wait_dynamic_load = 1.0
        _wait_driver_timeout = 10.0
        scroller = WebDriverWait(driver, _wait_driver_timeout).until(
            expected_conditions.presence_of_element_located((By.CSS_SELECTOR, _css_selector_scroller))
        )
        while True:
            driver.execute_script(_js_update_scroller, scroller)
            time.sleep(_wait_dynamic_load)
            current_scroll_position = driver.execute_script(_js_return_scroller_top, scroller)
            scroll_height = driver.execute_script(_js_return_scroller_height, scroller)
            if current_scroll_position == scroll_height:
                break

    @staticmethod
    def _se_dynamic_filter(driver):
        _token_render_xpath = ('//*[@id="site-content"]/div[2]/div/div[2]/div/div[5]/'
                               'div[2]/div/div/div[1]/div/div[3]')
        try:
            dataset = driver.find_elements(By.XPATH, _token_render_xpath)
            if dataset:
                for row in dataset:
                    print(f'"{row.text}\n"')
            else:
                print("div element not found.")
        finally:
            # functionality: `driver.close()` is used to close the current browser window or tab
            # effect: closes current browser window or tab but leaves WebDriver process running
            # use case: use this when we want to close a specific window or tab but keep the current
            #  session running, perhaps to interact with other windows or perform additional actions
            driver.close()

    def get_bypass_decoy_data(self):
        # we stashed the data locally and want to avoid downloading *again* lets load data into memory
        return self._se_capture_csv()

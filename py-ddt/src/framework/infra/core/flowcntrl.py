import src as s
import src.data.models.platforms.datasource.scrape as scraper
from src.data.models.features.engineering.UserLogInFE import UserLogInFE
from src.data.models.features.engineering.UserRetentionFE import UserRetentionFE
from src.data.models.features.engineering.UserSignUpFE import UserSignUpFE
from src.data.models.platforms.datasource.mobile import Mobile
from src.data.models.platforms.datasource.statistics import Statistics
from src.framework.api.postgresql import PostgreSqlApi
from src.framework.api.scikit import ScikitApi
from src.framework.api.roboflow import RoboFlowApi
from src.framework.api.tableau import TableauApi
from src.framework.api.twilio.sendgrid import SendGridApi
from src.framework.infra.core.sandbox import SandBox
# noinspection PyPep8Naming
from src.framework.infra.tools.definitions import Definitions as token


class FlowCntrl:
    """
    FlowCntrl is an entity that...
    TODO: documentation for FlowCntrl.py
    """

    def __init__(self):
        print(r'FlowCntrl.py')

    modes = {
        0: 'DEBUG - Experimental',
        1: 'D1 - Marketing',
        2: 'D2 - Application',
        3: 'D3 - Demographics',
        4: 'F1 - User Login',
        5: 'F2 - User Signup',
        6: 'F3 - User Retention',
        7: 'PY - Operations for Python',
        8: 'ML - Operations for Machine Learning',
        9: 'SQL - Operations for SQL',
        10: 'EDA - Operations for Exploratory Data Analysis',
        11: 'REPORT - Operations for Report',
        -1: 'EXIT'
    }

    def fire_mode(self):
        for key, value in self.modes.items():
            print(f'"{key}:" "{value}"')
        while True:
            try:
                mode = int(input("Enter the mode:"))
                if mode in self.modes:
                    selected = self.modes[mode]
                    if mode == -1:
                        print("Exiting the program.")
                        break
                    elif mode == 0:
                        print(f'Using "{selected}"')
                        self.print_src_subfolders()
                    elif mode == 1:
                        print(f'Using "{selected}"')
                        self.fire_scraper_link()
                    elif mode == 2:
                        print(f'Using "{selected}"')
                        self.fire_application_link()
                    elif mode == 3:
                        print(f'Using "{selected}"')
                        self.fire_demographics_link()
                    elif mode == 4:
                        print(f'Using "{selected}"')
                        self.fire_f1_link()
                    elif mode == 5:
                        print(f'Using "{selected}"')
                        self.fire_f2_link()
                    elif mode == 6:
                        print(f'Using "{selected}"')
                        self.fire_f3_link()
                    elif mode == 7:
                        print(f'Using "{selected}"')
                        self.fire_audit_py_mode()
                    elif mode == 8:
                        print(f'Using "{selected}"')
                        self.fire_ml_mode()
                    elif mode == 9:
                        print(f'Using "{selected}"')
                        self.fire_sql_mode()
                    elif mode == 10:
                        print(f'Using "{selected}"')
                        self.fire_eda_mode()
                    elif mode == 11:
                        print(f'Using "{selected}"')
                        self.fire_report_mode()
                    else:
                        print(f'Unsupported: "{selected}"')
                else:
                    print("Invalid mode. Enter a Valid mode.")
            except ValueError:
                print("Invalid input. Enter a valid input.")

    def print_src_subfolders(self):
        print('fire_experimental_link()')
        s.print_src_subfolders()

    def fire_scraper_link(self):
        print('fire_scraper_link()')
        print(token.UBER_FARES_ENDPOINT)
        temp = scraper.ScraperUberFares(url=token.UBER_FARES_ENDPOINT)
        df = temp.get_bypass_decoy_data()
        if df is None:
            print("DataFrame could not be loaded.")
        else:
            print("DataFrame loaded successfully.")
        return

    def fire_application_link(self):
        print('fire_application_link()')
        Mobile()

    def fire_demographics_link(self):
        print('fire_demographics_link()')
        Statistics()

    def fire_f1_link(self):
        print('fire_f1_link()')
        UserLogInFE()

    def fire_f2_link(self):
        print('fire_f2_link()')
        UserSignUpFE()

    def fire_f3_link(self):
        print('fire_f3_link()')
        UserRetentionFE()

    def fire_audit_py_mode(self):
        print('fire_audit_py_mode()')
        SandBox()

    def fire_ml_mode(self):
        print('fire_ml_mode()')
        RoboFlowApi().caller()
        ScikitApi().caller()

    def fire_sql_mode(self):
        print('fire_sql_mode()')
        pgsql_api = PostgreSqlApi()
        pgsql_api.fire_mode()

    def fire_eda_mode(self):
        print('fire_eda_mode()')
        TableauApi()

    def fire_report_mode(self):
        print('fire_report_mode()')
        SendGridApi()


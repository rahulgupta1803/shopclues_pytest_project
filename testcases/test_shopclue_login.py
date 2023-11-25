import time

from objectpages.shopclue_page import Shopclue_login
from utilities import xlutils
from utilities.shopclue_login_logger import LogGenerator


class Test_Shopclue_login():
    log = LogGenerator.loggen()
    fpath = "D:\\credence\\shopclues_pytest_project\\testcases\\Testdata\\shopclue_login.xlsx"

    def test_shopclue_login_001(self,setup):
        self.driver = setup
        self.log.info("Open browser")
        self.slp = Shopclue_login(self.driver)
        self.row = xlutils.RowCount(self.fpath,"Sheet1")
        exp_result_list = []
        for r in range (2,self.row+1):
            self.email = xlutils.ReadData(self.fpath,"Sheet1", r, 2)
            self.password = xlutils.ReadData(self.fpath,"Sheet1",r,3)
            self.exp_result = xlutils.ReadData(self.fpath,"Sheet1",r,4)
            time.sleep(3)
            self.slp.SignIN()
            self.log.info("Click on login")
            time.sleep(3)
            self.slp.Pop_Button()
            self.log.info("Click on disabled")
            time.sleep(3)
            self.slp.Facebook()
            self.log.info("Click on facebook")
            time.sleep(3)
            self.slp.Entry_Email(self.email)
            self.log.info(f"Enter email: {self.email}")
            self.slp.Entry_Password(self.password)
            self.log.info(f"Enter password: {self.password}")
            self.slp.Login_Button()
            self.log.info("click on login button")
            time.sleep(5)
            print(self.slp.Login_Status())
            if  self.slp.Login_Status()==True:
                if self.exp_result=="pass":
                    self.log.info("case is passed")
                    exp_result_list.append("pass")
                    time.sleep(2)
                    self.driver.save_screenshot(f".\\screenshots\\{self.email}_{self.password}.PNG")
                    xlutils.WriteData(self.fpath,"Sheet1",r,5,"pass")
                    time.sleep(5)
                    self.slp.Signout()

                    time.sleep(3)
                elif self.exp_result=="fail":
                    exp_result_list.append("fail")
                    self.log.info("Case is failed")
                    self.driver.save_screenshot(f".\\screenshots\\{self.email}_{self.password}.PNG")
                    xlutils.WriteData(self.fpath,"Sheet1",r,5,"fail")
                    time.sleep(3)
                    self.slp.Signout()
                    time.sleep(3)
            elif self.slp.Login_Status()==False:
                if self.exp_result=="pass":
                    exp_result_list.append('fail')
                    self.log.info("Case is failed")
                    self.driver.save_screenshot(f".\\screenshots\\{self.email}_{self.password}.PNG")
                    xlutils.WriteData(self.fpath,"Sheet1",r,5,"fail")
                    time.sleep(3)
                    self.driver.get("https://www.shopclues.com/")
                    time.sleep(3)
                elif self.exp_result=='fail':
                    exp_result_list.append("pass")
                    self.log.info("Case is passed")
                    self.driver.save_screenshot(f".\\screenshots\\{self.email}_{self.password}.PNG")
                    xlutils.WriteData(self.fpath,"Sheet1",r,5,"pass")
                    time.sleep(3)
                    self.driver.get("https://www.shopclues.com/")
                    time.sleep(3)
        print(exp_result_list)
        if "fail" not in exp_result_list:
            self.log.info("data derive testing is passed")
            assert True
        else:
            self.log.info("data derive testing is failed")
            assert False




#/html[1]/body[1]/div[3]/aside[2]/div[2]/div[1]/div[1]/form[1]/div[1]/div[3]/div[1]/input[1]

from splinter import Browser
import time
import unittest
#from selenium import selenium
import os
 
class TestSequenceFunctions(unittest.TestCase):       
    def setUp(self):
        self.url = 'http://www.tripsta.ie/'        
        self.browser = Browser('phantomjs')
        #self.address = os.environ['recipient']
        self.location = 'SOF'
        self.destination = ['BER', 'LON', 'ROM', 'PAR', 'MAD', 'VIE']
        self.departure = [13, 20, 27]
        self.returns = ['08/06/2014', '15/06/2014', '22/06/2014', '29/06/2014'] 
        self.max_price = 120
        self.sms_url = 'http://my.globul.bg'
        self.user = '******'
        self.passwd = '******'
        self.number = '******' 
                    
    def tearDown(self):
        self.browser.quit()
        
    def get_time(self):
        return time.time()

    def make_screenshot(self):
        self.browser.driver.save_screenshot('screen_%s.png' % int(time.time()*1000) )

    def test_send_email(self):
        #self.skipTest('Still error appear')
        start = self.get_time()   
        browser = self.browser
        
        browser.visit(self.url)
        self.make_screenshot()
        
        browser.find_by_name('dep').type(self.location)
        self.make_screenshot()

        for dest in self.destination:  
            for dep in self.departure:
                browser.find_by_id('arr').fill(dest)
                self.make_screenshot()        
                    
                browser.find_by_id('obDate').fill(str(dep)+'/06/2014')
                self.make_screenshot()     

                browser.find_by_id('ibDate').fill(str(dep+2)+'/06/2014')
                self.make_screenshot()

                browser.find_by_css('button.btn-primary').click()
                self.make_screenshot()  

                time.sleep(10)
                self.make_screenshot() 

                price = browser.find_by_css('span.amount').first.text[1:]
                price = float(price)
                
                var = browser.is_element_present_by_css('span.discount')
                if var:
                    discount = browser.find_by_css('span.discount').first.text[18:]
                    discount = float(discount)
                    if price>discount:
                        price = discount
                                    
                if price<=self.max_price:     
                    time_departure = browser.find_by_css('td.depart span.cursor_default').first.text
                    time_arrival = browser.find_by_css('td.arrive span.cursor_default').first.text
                    self.make_screenshot() 
                    
                    time_return = browser.find_by_css('div.inbound td.depart span.cursor_default').first.text
                    time_return_arrive = browser.find_by_css('div.inbound td.arrive span.cursor_default').first.text
                    
                    message = '%s departure %s at %s arrive %s \n Return %s at %s arrive %s \n Price: %s' %(dest, str(dep)+'/06/2014', time_departure, time_arrival, str(dep+2)+'/06/2014', time_return, time_return_arrive ,price)
                    print message
                                                           
                    browser.visit(self.sms_url)
                    self.make_screenshot()
                        
                    browser.find_by_css('li.first a').click()
                    self.make_screenshot()
                        
                    time.sleep(5)
                    self.make_screenshot() 

                    browser.find_by_id('n_1_2').fill(self.user)
                    self.make_screenshot()
                        
                    browser.find_by_id('n_2').type(self.passwd)
                    self.make_screenshot()

                    browser.find_by_name('image').click()
                    self.make_screenshot()
                        
                    time.sleep(5)
                    self.make_screenshot() 
                                
                    browser.find_by_css('body div.wrapper div.extra div ul:nth-child(4) li:nth-child(2) a').click()
                    self.make_screenshot()
                        
                    time.sleep(5)
                    self.make_screenshot() 
                        
                    browser.find_by_id('receiverPhoneNum').type(self.number)
                    self.make_screenshot()	

                    browser.find_by_id('txtareaMessage').type(message)
                    self.make_screenshot()	
                        
                    browser.choose('reply2Inbox', 'true')
                    self.make_screenshot()

                    browser.find_by_name('btnSendSMS').click()
                    self.make_screenshot()
                    
                    browser.find_by_css('li.first a').click()
                    self.make_screenshot()  

                    browser.visit(self.url)
                    self.make_screenshot()
                    
                    browser.find_by_name('dep').type(self.location)
                    self.make_screenshot()                    
        
if __name__ == '__main__':
    unittest.main()
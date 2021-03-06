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
        self.destination = ['ROM', 'VIE', 'LON', 'PAR', 'MAD', 'BER']
        self.departure = [13, 20, 27]
        self.returns = ['08/06/2014', '15/06/2014', '22/06/2014', '29/06/2014'] 
        self.max_price = 200
        self.mail_url = 'http://m.abv.bg'
        self.user = 'nullman'
        self.passwd = '123'
        self.address = 'lilikazakova@gmail.com' 
        #os.environ['recipient']
        self.subject = 'Cheapiest flight to Vienna'
        self.message = []
            
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
                browser.find_by_name('arr').fill(dest)
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
                    #self.send_price_email( self.get_price_details(browser, price) )   
                    
    #def get_price_details(self, browser, price):
                    time_departure = browser.find_by_css('td.depart span.cursor_default').first.text
                    time_arrival = browser.find_by_css('td.arrive span.cursor_default').first.text
                    self.make_screenshot() 
                    #browser.find_by_id('form-flights-result-0')
                    time_return = browser.find_by_css('div.inbound td.depart span.cursor_default').first.text
                    time_return_arrive = browser.find_by_css('div.inbound td.arrive span.cursor_default').first.text
                
                    message_flight = 'Flight from %s to %s : \n Departure on %s at %s. Arrive at %s. \n Return flight: \n Departure on %s at %s. Arrive at %s. \n Lowest price: %s EUR. \n \n' %(self.location, dest, str(dep)+'/06/2014', time_departure, time_arrival, str(dep+2)+'/06/2014', time_return, time_return_arrive, price)
                    print message_flight
                    
                    self.message.insert(0, message_flight)
                            
    #def send_price_email(self, message):
        browser = self.browser        
                                
        browser.visit(self.mail_url)
        self.make_screenshot()

        browser.find_by_name('username').type(self.user)
        self.make_screenshot()
                
        time.sleep(5)
        self.make_screenshot()         

        browser.find_by_name('password').type(self.passwd)
        self.make_screenshot()

        browser.find_by_css('input.submit').click()
        self.make_screenshot()
                        
        browser.find_by_css('a.write').click()
        self.make_screenshot()
                
        browser.find_by_name('TO').type(self.address)
        self.make_screenshot()	

        browser.find_by_name('SUBJECT').type(self.subject)
        self.make_screenshot()	

        browser.find_by_name('BODY').type(self.message)
        self.make_screenshot()	

        browser.find_by_name('SENDMESSAGE_SEND').click()
        self.make_screenshot()	
        
if __name__ == '__main__':
    unittest.main()
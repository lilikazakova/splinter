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
        self.destination = 'VIE'
        self.departure = '06/06/2014'
        self.returns = '08/06/2014'
        self.max_price = 130
        self.mail_url = 'http://m.abv.bg'
        self.user = 'nullman'
        self.passwd = '123'
        self.address = 'lilikazakova@gmail.com' 
        #os.environ['recipient']
        self.subject = 'Cheapiest flight to Vienna'
            
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
        
        browser.find_by_name('arr').type(self.destination)
        self.make_screenshot()        
		
        browser.find_by_id('obDate').fill(self.departure)
        self.make_screenshot()     

        browser.find_by_id('ibDate').fill(self.returns)
        self.make_screenshot()

        #browser.check('extendedDates')
        #self.make_screenshot()   

        browser.find_by_css('button.btn-primary').click()
        self.make_screenshot()  

        time.sleep(10)
        self.make_screenshot() 

        price = browser.find_by_css('span.amount').first.text[1:]
        self.make_screenshot() 
                
        time_departure = browser.find_by_css('td.depart span.cursor_default').first.text
        time_arrival = browser.find_by_css('td.arrive span.cursor_default').first.text
                
        message = 'Flight from %s  to %s  Departure on %s at %s Arrive at %s Lowest price %s' %(self.location, self.destination, self.departure, time_departure, time_arrival, price)
        
        browser.find_by_id('form-flights-result-0')
        #print self.message
        
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

        browser.find_by_name('BODY').type(message)
        self.make_screenshot()	

        browser.find_by_name('SENDMESSAGE_SEND').click()
        self.make_screenshot()		
        
if __name__ == '__main__':
    unittest.main()
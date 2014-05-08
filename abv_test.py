from splinter import Browser
import time
import unittest
#from selenium import selenium
import os
 
class TestSequenceFunctions(unittest.TestCase):       
    def setUp(self):
        self.url = 'http://m.abv.bg'
        self.user = 'nullman'
        self.passwd = '123'
        self.browser = Browser('phantomjs')
        self.address = os.environ['recipient']
        self.subject = 'hello'
        self.message = 'Hello!'
    
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

        browser.find_by_name('username').type(self.user)
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
		
        self.assertTrue( browser.is_element_present_by_css('p.pl5 strong.c1') )
        #print "Time taken: %10.3f" % (get_time() - start)
        #browser.quit()            

if __name__ == '__main__':
    unittest.main()
   

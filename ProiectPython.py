"""
Bibliografie:
https://selenium-python.readthedocs.io/
https://dev.to/tonetheman/using-selenium-to-login-to-a-website-10o4
https://rzvnvilceanu.medium.com/build-an-instagram-bot-to-check-your-unfollowers-part-i-8b7c3fbfcc4
Materialele de curs puse la dispozitie

"""
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class Instagram_bot(unittest.TestCase):

    #initializarea testului
    def setUp(self):
        #selectarea driverului browser-ului chrome
        self.driver = webdriver.Chrome()

    #functia care verifica logarea pe cont
    def test_login_instagram(self):
        utilizator ='bogdan.v17'
        parola ='Parolapentrucont'

        driver = self.driver

        #se configureaza adresa url a paginii care trebuie accesata
        driver.get("http://www.instagram.com/")
        self.assertIn("Instagram", driver.title)
        time.sleep(2)

        #se apasa optiunea "accept all" din fereastra de cookies
        driver.find_element_by_xpath("/html/body/div[2]/div/div/button[1]").click()
        time.sleep(2)

        #se identifica, se introduc username-ul si parola in campurile specifice
        elem = driver.find_element_by_name("username")
        elem.send_keys(utilizator)
        elem = driver.find_element_by_name("password")
        elem.send_keys(parola)
        time.sleep(1)

        #se apasa butonul de login
        driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button').click()
        time.sleep(3)

        #se apasa butonul "not now" din fereastra de salvare a parolei
        driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()
        time.sleep(3)

        #se apasa butonul "not now" din fereastra de pornire a notificarilor
        driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()
        time.sleep(3)

        #se verifica daca logarea s-a realizat cu succes
        assert '' == driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[1]').text
        time.sleep(5)


    #functia care da like la prima poza din feed
    def test_like_poza(self):
        driver = self.driver
        self.test_login_instagram()
        time.sleep(2)

        #se apasa tasta "sageata jos" pentru a naviga in pagina
        scroll_down = driver.find_element_by_xpath('/html/body')
        scroll_down.send_keys(Keys.PAGE_DOWN)
        time.sleep(2)

        #se apasa butonul de like la prima postare din feed
        driver.find_element_by_class_name('fr66n').click()
        time.sleep(5)

    #functia care afiseaza numarul de urmaritori al contului
    def test_numar_urmaritori(self):
        driver = self.driver
        self.test_like_poza()
        time.sleep(3)

        # se apasa tasta "sageata sus" pentru a naviga in pagina
        scroll_up = driver.find_element_by_xpath('/html/body')
        scroll_up.send_keys(Keys.PAGE_UP)
        time.sleep(3)

        #accesare iconita pozei de profil
        driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[5]').click()
        time.sleep(3)

        #selectarea optiunii "profile"
        driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div[2]/div[2]/a[1]/div').click()
        time.sleep(3)

        #extrage textul de la numarul de urmaritori
        followers=driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]').text
        print('This account has: ', followers)
        time.sleep(5)


    #eliberare de resurse din test
    def tearDown(self):
        self.driver.close()

#apelarea functiilor in functia main
if __name__ == "__main__":
    Instagram_bot.test_login_instagram()
    Instagram_bot.test_like_poza()
    Instagram_bot.test_numar_urmaritori()

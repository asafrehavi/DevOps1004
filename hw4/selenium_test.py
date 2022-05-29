from selenium import webdriver


def q4():
    my_driver = webdriver.Chrome(executable_path="C:\install\chromedriver_win32\chromedriver.exe")
    my_driver.get("https://www.ycombinator.com/")
    assert my_driver.title == "Y Combinator"


def q5():
    my_driver = webdriver.Chrome(executable_path="C:\install\chromedriver_win32\chromedriver.exe")
    my_driver.get("https://hub.docker.com/")
    assert my_driver.title == "Docker Hub Container Image Library | App Containerization"

q5()


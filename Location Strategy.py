
from selenium.webdriver import Chrome

driver = Chrome()
driver.get("http://automationpractice.com/index.php");

dress_N_title = driver.find_element_by_xpath("//*/ul/li[6]/div/div[2]/h5/a");
dress_N_title.click();

#selecting the dress size(L) and color(White), and add to shopping card

driver.get("http://automationpractice.com/index.php?id_product=6&controller=product")

size = driver.find_element_by_xpath("/html/body/div/div[2]/div/div[3]/div/div/div/div[4]/form/div/div[2]/div/fieldset[1]/div");
size.click();
changesizetoL = driver.find_element_by_css_selector("#group_1 > option:nth-child(3)");
changesizetoL.click();
changecolor = driver.find_element_by_id("color_8")
changecolor.click();
submit = driver.find_element_by_name("Submit");
submit.click();



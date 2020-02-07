from Modules import *

login(url,usr,pas)

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, 'order')))
time.sleep(2)

number_of_scholarships = driver.find_element_by_xpath('//h1[@class="section-title hidden-xs ng-binding"]')
number_of_scholarships = number_of_scholarships.text
number_of_scholarships = number_of_scholarships.split()
num_of_scholarships = int(number_of_scholarships[1])
print('Total number of scholarships'+str(number_of_scholarships))

scroll_Down_to_Browse_More()
scrap_forsa_data()
while (len(Links) < num_of_scholarships):
    scroll_Down_to_Browse_More()
    scrap_forsa_data()

title_sch = list(set(accounts_name))
Link_sch = list(set(Links))

save_close(title_sch,Link_sch)

print("Process completed")
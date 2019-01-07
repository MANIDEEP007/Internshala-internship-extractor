#This is used for Educational Purpose. Don't misuse it
#Paduchuri Manideep
import csv
import time
import datetime
import sys
import os
import webbrowser
from selenium import webdriver
file_obj = open("Sample.html","w")
start = "<table>\n"
code = '''
\t<tr style ='border: 1px solid black'>\n
\t\t<th style = "colspan:2">Title</th>\n
\t\t<th style = "colspan:2">Company</th>\n
\t\t<th style = "colspan:2">Duration</th>\n
\t\t<th style = "colspan:2">Posted Date</th>\n
\t\t<th style = "colspan:2">Stipend</th>\n
\t\t<th style = "colspan:2">Link</th>\n
</tr>\n
'''
file_obj.write(start + code)
def writer(list_bulder):
	starter = "\t<tr style ='border: 1px solid black'>\n"
	start_td = "\t\t<td style = 'colspan:2;border: 1px solid black;padding-right:15px;'>\n"
	end_td = "\t\t</td>\n"
	code = ""
	for i in range(len(list_builder)-1):
		code += start_td + list_builder[i] +end_td
	code += start_td + "<a  target = '_blank'href = '"+list_builder[-1]+"'>"+"Apply Now</a>"+ end_td	
	ender = "\t</tr>\n"	
	file_obj.write(starter+code+ender)
driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
driver.maximize_window()
static_url = "https://internshala.com/internships/work-from-home-jobs/page-"
driver.get("https://internshala.com/internships/work-from-home-jobs/page-1")
yesterday = datetime.datetime.today() - datetime.timedelta(days = 1)
today = datetime.datetime.today()
time.sleep(2)
try:
	driver.find_element_by_css_selector("#no_thanks").click()
except:
	pass
for i in driver.find_elements_by_css_selector("#internship_list_container .individual_internship"):
	title = i.find_element_by_css_selector("h4").text
	company = i.find_element_by_css_selector(".link_display_like_text").text
	dur_stp_str= []	
	list_builder = []
	link = i.find_element_by_css_selector(".button_container a").get_attribute("href")
	flag = 0
	for j in i.find_elements_by_css_selector(".individual_internship_details table tbody tr td"):
		if flag == 0:
			flag = flag + 1
			continue
		if len(dur_stp_str) == 2:
			dat_mon = j.text.split("'")
			date_str = dat_mon[0]+" 20"+dat_mon[1]
			format_str = "%d %b %Y"
			date_obj = datetime.datetime.strptime(date_str,format_str)
		flag = flag + 1
		dur_stp_str.append(j.text)
	list_builder = [title,company,dur_stp_str[0],dur_stp_str[1],dur_stp_str[2],link]
	if date_obj == today:
		writer(list_builder)
	
counter = 2
while(1):
	driver.get(static_url+str(counter))
	for i in driver.find_elements_by_css_selector("#internship_list_container .individual_internship"):
		title = i.find_element_by_css_selector("h4").text
		company = i.find_element_by_css_selector(".link_display_like_text").text
		dur_stp_str= []	
		list_builder = []
		link = i.find_element_by_css_selector(".button_container a").get_attribute("href")
		flag = 0
		for j in i.find_elements_by_css_selector(".individual_internship_details table tbody tr td"):
			if flag == 0:
				flag = flag + 1
				continue
			if len(dur_stp_str) == 2:
				dat_mon = j.text.split("'")
				date_str = dat_mon[0]+" 20"+dat_mon[1]
				format_str = "%d %b %Y"
				date_obj = datetime.datetime.strptime(date_str,format_str)
				if(date_obj <= yesterday):
					webbrowser.open('file://' + os.path.realpath("Sample.html"))
					driver.close()
					sys.exit()
			flag = flag + 1
			dur_stp_str.append(j.text)
		list_builder = [title,company,dur_stp_str[0],dur_stp_str[1],dur_stp_str[2],link]
		writer(list_builder)
	counter += 1
end = "</table>"
file_obj.write(end)

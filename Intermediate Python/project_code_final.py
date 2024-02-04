#webdriver used to navigate web pages
from selenium import webdriver
#time library used for waiting during code execution
import time
import pandas as pd
from matplotlib import pyplot as plt
from IPython import get_ipython
get_ipython().run_line_magic('matplotlib', 'inline')
import requests
import json
import numpy as np

#menu function - show options for user
def menu():
    print('\nOPTIONS:\n')
    print('1. Data Science Job Search')
    print('2. Data Science Jobs Salary Information (2020-2022)')
    print('0. Quit')
    return int(input('Please, enter your option: '))

#main function - runs depending on user's choice until quit
def main():
    pd.set_option('display.max_rows', 20)
    pd.set_option('display.max_columns', 10)
    pd.set_option('display.width', 1000)
    choice = menu()
    #reading csv file 1 into dataframe
    sal_info1 = pd.read_csv('ds_salaries_workfile.csv')
    #reading csv file 2 into dataframe
    sal_info2 = pd.read_csv('Data Science Jobs Salaries1_workfile.csv')
    #merging two csv dataframes into one
    sal_info = pd.concat([sal_info1, sal_info2], axis=0)
    #creating lists to add new columns
    exp_level_list = list()
    comp_size_list = list()
    #changing non-numerical experience level into numerical, to calculate correlation
    for i in sal_info['experience_level']:
        if i == 'EN':
            j = 1
        elif i == 'MI':
            j = 2
        elif i == 'SE':
            j = 3
        exp_level_list.append(j)
    #adding new column into dataframe
    sal_info['exp_level_number'] = exp_level_list
    
    #changing non-numerical company size into numerical, to calculate correlation
    for m in sal_info['company_size']:
        if m == 'S':
            n = 1
        elif m == 'M':
            n = 2
        elif m == 'L':
            n = 3
        comp_size_list.append(n)
    #adding new column into dataframe
    sal_info['comp_size_number'] = comp_size_list
    
    #code for option 1
    if choice == 1:
        jobrole = input('Enter Job Role: ')

        #split each word
        jobr = jobrole.split(' ')
        url1 = jobr[0]
        for i in range(1,len(jobr)):
            url1 += '%20'+jobr[i]
        #fit the splitted input into the url
        url = 'https://www.linkedin.com/jobs/search/?currentJobId=3303619863&geoId=103644278&keywords='+\
            url1+'&location=United%20States&refresh=true'
            
        #get the webdriver directory
        wd = webdriver.Chrome('chromedriver.exe')
        #wd.get navigate particular URL(website) and wait till page load
        wd.get(url)

        i = 2
        #set the maximum output to 400 jobs, where one page displayed 25 jobs
        while i <= int(400/25)+1: 
            #execute_script method to call the JavaScript API 
            #scroll down the opened window with window.scrollTo method
            #scrollHeight will give the height of the entire body of the page
            wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            i = i + 1
            try:
                #when reached the bottom of the page, find the "See more jobs" button and click it
                #find_element_by_xpath returned the first element with the XPath syntax matching the location 
                wd.find_element_by_xpath('/html/body/main/div/section/button').click()
                #suspends execution for the 5 seconds (wait for the page to display the new jobs)
                time.sleep(5)
            except:
                pass
                time.sleep(5)

        #find the jobs from the class name      
        job_lists = wd.find_element_by_class_name('jobs-search__results-list')
        #create a list based on the elements tag argument
        jobs = job_lists.find_elements_by_tag_name('li')
        print('Number of current jobs available:',len(jobs))

        #creta empty lists for each data
        job_title = []
        company= []
        date_posted = []
        link = []
        #loop the data through the lists of elements and add to coresponding lists
        for job in jobs: 
         #first element with the matching CSS selector will be returned
         job_title0 = job.find_element_by_css_selector('h3').get_attribute('innerText')
         #add the extracted data into the list made before
         job_title.append(job_title0)
         company0 = job.find_element_by_css_selector('h4').get_attribute('innerText')
         company.append(company0)
         date_posted0 = job.find_element_by_css_selector('div>div>time').get_attribute('datetime')
         date_posted.append(date_posted0)
         link0 = job.find_element_by_css_selector('a').get_attribute('href')
         link.append(link0)
         
        #store the data into a dataframe using pd.DataFrame
        job_data = pd.DataFrame({
        'Date Posted': date_posted,
        'Company': company,
        'Title': job_title,
        'Link' : link
        })

        #import the dataframe into an excel file in user's computer
        job_data.to_excel('LinkedIn Job Data USA 2022.xlsx', index = False)
    #code for option 2
    elif choice == 2:
        #asking for interested job title
        job_title = input('Please enter a job title: ')
        #see if we have salary data for that job title
        found_jt = sal_info[sal_info['job_title'].str.contains(job_title)]
        #creating variable for description for that job title
        desc_sal = round(found_jt[['experience_level', 'salary_in_usd']].groupby(by = 'experience_level').describe())
        #creating variable for year by year description for that job title
        desc_sal_yby = round(found_jt[['work_year', 'experience_level', 'salary_in_usd']].groupby(by = ['work_year', 'experience_level']).describe())
        #if we have salary data on job title
        if len(found_jt) > 0:
            #show salary information
            print('\nSalary information for ' + job_title + ' (2020-2022, in USD):\n' + str(desc_sal))
            print('\nYear-by-year salary information for ' + job_title + ' (in USD):\n' + str(desc_sal_yby))
            #show correlation
            corr_exp_sal = round(found_jt['salary_in_usd'].corr(found_jt['exp_level_number']),2)
            print('\nCorrelation between experience level and salary is:', corr_exp_sal)
            corr_size_sal = round(found_jt['salary_in_usd'].corr(found_jt['comp_size_number']),2)
            print('\nCorrelation between company size and salary is:', corr_size_sal)
        #if we don't have salary data on job title
        else:
            print('Sorry, we do not have any salary information for this job title.')
   
    #code for option 0
    elif choice == 0:
        print('\nThank you. Good luck on your job search!')
        return
    main()

if __name__ == '__main__':
    main()    
    
    
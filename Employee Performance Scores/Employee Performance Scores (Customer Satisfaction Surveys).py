#THIS PROGRAM DISPLAYS A TABLE CONTAINING EMPLOYEE NAMES AND AVG CUSTOMER SATISFACTION SURVEY SCORES FOR EACH EMPLOYEE
 #BASED ON RECORDS FROM A .CSV FILE. IT ALSO DISPLAYS THE NAME OF THE INDIVIDUAL WITH THE HIGHEST AVG. LASTLY, THE PROGRAM
  #ALLOWS THE USER TO CONDUCT FILTERED SEARCHES WITHIN THE DATA RECORDS BY ENTERING AN EMPLOYEE NAME, AND THE PROGRAM DISPLAYS THE
   #EMPLOYEE'S OVERALL PERFORMANCE RATING (BASED ON AVG SURVEY SCORES) AND LISTS THEIR RESPECTIVE SCORE FOR EACH SURVEY ON RECORD.

def calc_avg():
    """ Accesses customer satisfaction survey data from table and calculates performance avgs,
    displays records as a table, and identifies the employee with highest satisfaction survey average."""

    survey_scores = open('survey_scores.csv', 'r')
    high_avg = 0
    high_avg_name = ''

    print('Employee Name', '\t', 'Avg. Score')
    print('_____________', '\t', '__________', '\n')
    #EXTRACTS NAME AND SCORES FROM FILE, AND CALCULATES AVG SCORE FOR EACH EMP.
    for aLine in survey_scores:
        values = aLine.split(',')
        emp_name = values[0]
        score1 = int(values[1])
        score2 = int(values[2])
        score3 = int(values[3])
        calc_ = float((score1 + score2 + score3) / 3)
        #PRINTS EMP NAME AND AVG SCORE IN A TABLE; FORMATS FLOAT TO 2 DECIMAL PLACES, AND ADJUST SPACING OF COLUMNS.
        print('{:18} {:}'.format(emp_name, "%.2f" % calc_))
        #IDENTIFIES THE EMPLOYEE WITH THE HIGHEST AVG SCORE.
        if calc_ > high_avg:
            high_avg = calc_
            high_avg_name = emp_name
    #PRINTS THE NAME AND AVG OF THE EMPLOYEE IDENTIFIED AS HAVING THE HIGHEST AVG SCORE.
    print('\n' + 'The employee with the highest customer satisfaction survey average is:', high_avg_name, '(', "%.2f" % high_avg, ').', '\n')

    survey_scores.close()

def searchable_by_user():
    '''Allows the user to conduct filtered searches within the data records by entering an employee's name.
    The function returns the employee's performance evaluation rating (based on a avg score) and
    also displays the employee's individual survey scores from the csv data file'''

    survey_scores = open('survey_scores.csv', 'r')
    user_search = input( "Enter an employee's name to find out their performance evaluation rating and individual survey scores:").title()
    name_in_search = False
    
    for aLine in survey_scores:
        values1 = aLine.split(',')
        emp_name1 = values1[0]
        scoreone = int(values1[1])
        scoretwo = int(values1[2])
        scorethree = int(values1[3])
        calc_1 = float((scoreone + scoretwo + scorethree) / 3)
        #USING THE CALCULATED AVG SCORE OF EACH EMPLOYEE, IDENTIFIES WHAT PERFORMANCE RATING THEY FALL UNDER (NEEDS IMP,CONTRIBUTOR,
        # VALUED CONT, AND KEY CONT).
        if user_search == emp_name1:
            if calc_1 >= 90:
                perf_rating = 'Key Contributor (Average Score > 90%)'
            elif calc_1 < 90 and calc_1 >= 80:
                perf_rating = 'Valued Contibutor (Average Score between 80% to 89.99%)'
            elif calc_1 < 80 and calc_1 >= 70:
                perf_rating = 'Contibutor (Average Score between 70% to 79.99%)'
            elif calc_1 < 70:
                perf_rating = 'Needs Improvement (Average Score less than 70%)'
            #PRINTS THE RESULTS REQUESTED BY USER, SHOWING RATING AND INDIVIDUAL SATISFACTION SURVEY SCORES ON RECORD (.CSV FILE).
            search_results_r = 'The customer satisfaction performance evalution for ' + emp_name1 + ' is rated as: ' + perf_rating
            search_results_ind = emp_name1 + "'s individual satisfaction survey scores are: " + str(scoreone)+ ', ' + str(scoretwo) + ', ' + str(scorethree)
            name_in_search = True
        #ADDS SEARCHABILITY OPTIMIZATION, ALLOWING USERS TO ENTER A PARTIAL NAME OF THE DESIRED EMPLOYEE, AND THE
        # PROGRAM WILL STILL IDENTIFY THE RECORD AND DISPLAY THE CORRESPONDING RATING AND SCORES. EX- FOR THE NAME 'EMILIANO' USER CAN
        #  TYPE 'EMI' AND STILL GET THE DESIRED RESULTS.
        elif user_search[:] in emp_name1[:]:
            if calc_1 >= 90:
                perf_rating = 'Key Contributor (Average Score > 90%)'
            elif calc_1 < 90 and calc_1 >= 80:
                perf_rating = 'Valued Contibutor (Average Score between 80% to 89.99%)'
            elif calc_1 < 80 and calc_1 >= 70:
                perf_rating = 'Contibutor (Average Score between 70% to 79.99%)'
            elif calc_1 < 70:
                perf_rating = 'Needs Improvement (Average Score less than 70%)'

            search_results_r = 'The customer satisfaction performance evalution for ' + emp_name1 + ' is rated as: ' + perf_rating
            search_results_ind = emp_name1 + "'s individual satisfaction survey scores are: " + str(scoreone)+ ', ' + str(scoretwo) + ', ' + str(scorethree)
            name_in_search = True
    #RELAUNCHES THE FUNCTION AND PROMPTS THE USER TO RE-ENTER VALID NAME IF THE RECEIVED INPUT DOES NOT MATCH NAMES ON RECORD.
    if name_in_search == False:
        print('The employee name you entered does not match our records. Please try again.')
        searchable_by_user()
    #DISPLAYS DESIRED RESULTS BASED ON SEARCH INPUT
    print(search_results_r)
    print(search_results_ind)
    
    survey_scores.close()

def main():
    '''Creates a function called main to be used to execute all main program functions'''
    
    calc_avg()
    
    print('_____________________________________________________________','\n')
    
    searchable_by_user()

main()

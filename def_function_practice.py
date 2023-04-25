## def function practice

### Sum function
def sum_function(n1, n2):
    result = n1 +n2
    print("The sum of {} and {} is ".format(n1,n2), result)
    
sum_function(4,12)

### subtract function
def subtract_function(n1, n2):
    result = n1 - n2
    print("The subtraction of {} from {} is ".format(n2,n1), result)
    
subtract_function(4,12)

### difference function
def diff_function(n1, n2):
    result = n1 - n2
    print("The difference between {} from {} is ".format(n1,n2), abs(result))
    
diff_function(4,12)

### division function
def div_function(n1,n2):
    n1 = float(n1)
    n2 = float(n2)
    result = float(n1/n2)
    print("The  division of {} by {} is ".format(n1,n2), round(result,3))
    
div_function(4,12)

### Find average marks, Highest marks and lowest marks
### Note: This function takes list as input
def student_report(marks):
    top_marks = max(marks)
    low_marks = min(marks)
    avg_marks = sum(marks)/len(marks)
    print("Average score is",avg_marks)
    print("Maximum marks obtained in a subject is",top_marks)
    print("Lowest marks obtained in a subject is",low_marks)
    
student_report([35,50,70,80,95,86])

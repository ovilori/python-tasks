#this is a module with two functions that can be called in another program.
# this function selects all numeric values, even those values that are strings, and return them as a list.
#the values must be converted to numbers and included in the returned list.
#the returned list must be sorted.
#the function handles the possibility that the user input isn't formatted properly as a list and returns an empty list.

def process_numbers(user_list):
    new_list = []
    #checks if the user_list is not formatted correctly as a list and returns an empty list. 
    if isinstance(user_list,list) == False:
        return(new_list)

    for value in user_list:
        if isinstance(value,int) == True: #checks if the values is an integer
            new_list.append(value) #adds the value to the new list.
        elif isinstance(value,str) == True: #checks if the value is a string.
            if value.isnumeric(): #checks if the type is numeric.
                convert_value = int(value) #converts it to a number.
                new_list.append(convert_value) #then adds it to the list.
    new_list.sort()
    return new_list

#this function selects all string values that aren't numeric and return them as a list.
#the returned list must be sorted.
#the function handles the possibility that the user input isn't formatted properly as a list and returns an empty list.

def process_names(user_list):
    new_list = []
    #checks if the user_list is not formatted correctly as a list and returns an empty list.
    if isinstance(user_list,list) == False:
        return(new_list)


    for value in user_list:
        #if isinstance(value,int) == False:
        if isinstance(value,str): #checks for string values in the list
            if value.isnumeric() == False: #ensures numeric data types are not added to the new list.
                new_list.append(value) #adds only string values to the new list
        #Alternatively:
        #if isinstance(value,str): #checks for string values in the list.
            #new_list.append(value) #adds the string value to the new list.
            #for value in new_list: 
                #if value.isnumeric(): #checks for numeric data types in the list
                    #new_list.remove(value) #removes the value from the new list.
    new_list.sort()
    return new_list
def mean(value):
    print("Function started")
    if type(value) == dict:
        the_mean = sum(value.values())/len(value)
    else:
        the_mean = sum(value)/len(value)
    return the_mean

the_list = [11.4,12,4.4]
the_input = {"Marry":1.3,"Larry":2.5,"Laurie":4.5}
print(mean(the_input))
print(mean(the_list))
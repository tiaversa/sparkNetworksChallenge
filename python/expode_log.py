# figure it out how to turn a date into a number
def str_to_numb(date):
    date = date.split('T')[0].split('-')
    date = int("".join(date))
    return date

# figure it out how to turn a number to a YYYY_MM format
def yymm_format(date):
    YY = str(date)[:4]
    MM = str(date)[4:6]
    return f'{YY}-{MM}'

#create the while loop
def month_loop(start_date, end_date, amount):
    date_test = str_to_numb(start_date)
    end_date = str_to_numb(end_date)
    amount = float(amount)
    subslog = {}
    while (date_test < end_date):
        key = yymm_format(date_test)
        subslog[key] = amount
        if (key[5:7]== '12'):
            date_test += 8900
        else:
            date_test += 100
    # create the if for the leftover
    if (date_test>end_date):
        part_amount = round(((amount *(date_test-end_date))/30),2)
        key = yymm_format(date_test)
        subslog[key] = part_amount
    #return the dictionary
    return subslog


# figure it out how to get the start and end date
def add_log(jsonRespSub):
    for user in jsonRespSub:
        for each_sub in user['subscription']:
            user_subscription = each_sub
            #discover how to return it all to json
            user_subscription['log'] = month_loop(user_subscription['startDate'], user_subscription['endDate'], user_subscription['amount'])
    return jsonRespSub



def datetime_to_float(moment):
    ''' Converts the given datetime to a float (only for the time, the date is discarded).

    :param moment: the datetime for which we want the time in a float format.
    :return: the time in float format, e.g, a datetime with as time 08:30 will be 
    converted to 8,5. 
    '''
    moment_time = moment.time()
    moment_float = moment_time.hour + moment.minute / 60
    return moment_float
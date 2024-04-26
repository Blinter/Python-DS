def weekday_name(day_of_week):
    """Return name of weekday.
    
        >>> weekday_name(1)
        'Sunday'
        
        >>> weekday_name(7)
        'Saturday'
        
    For days not between 1 and 7, return None
    
        >>> weekday_name(9)
        >>> weekday_name(0)
    """
    return [
        'Sunday', #0 - 1 + day_of_week(1-7)
        'Monday', #1 - 1 + day_of_week(1-7)
        'Tuesday', #2 - 1 + day_of_week(1-7)
        'Wednesday', #3  - 1 + day_of_week(1-7)
        'Thursday', #4 - 1 + day_of_week(1-7)
        'Friday', #5 - 1 + day_of_week(1-7)
        'Saturday' #6 - 1 + day_of_week(1-7)
        ][day_of_week - 1] if 1 <= day_of_week <= 7 else None
class Task:
    """Represents the description, date and time of your task
    Attributes:
        _description (str): description of the task 
        _date (str): due date of the task, format: MM/DD/YYYY
        _time (str): time the task is due, format: HH:MM
    """
    
    def __init__(self, desc, date, time):
        #assigning parameters to the attributes
        self._description = desc
        self._date = date
        self._time = time
    
    @property
    def description(self):
        #returns the task’s description string
        return self._description
    
    @property
    def date(self):
        return str(self._date)

    def __str__(self):
        #returns a string used to display the task’s information to the user in the format: description – Due: date at time
        return f"{self._description} – Due: {self._date} at {self._time}"

    def __repr__(self):
        #returns a string used to write the task’s information to the file in the format: task,date,time
        return f"{self._description},{self._date},{self._time}"

    def __lt__(self, other):
        #returns true if the self task is less than the other task
        date = self._date.split("/") #spliting the date into a list
        date_other = other._date.split("/")
        
        time = self._time.split(":") #spliting time into a list
        time_other = other._time.split(":")
        
        month_self = int(date[0]) #setting month, day, and year to its own variable
        day_self = int(date[1])
        year_self = int(date[2])
        
        month_other = int(date_other[0])
        day_other = int(date_other[1])
        year_other = int(date_other[2])
        
        hour_self = int(time[0]) #setting hour and time to its own variable
        minute_self = int(time[1])
        
        hour_other = int(time_other[0])
        minute_other = int(time_other[1])
        
        if year_self != year_other: #compares year, month, day, hour, minute and then description
            return year_self < year_other
        elif month_self != month_other:
            return month_self < month_other
        elif day_self != day_other:
            return day_self < day_other
        elif hour_self != hour_other:
            return hour_self < hour_other
        elif minute_self != minute_other:
            return minute_self < minute_other
        else:
            return self._description < other._description
        


class ModelNthUserChurn:
    """
    ModelNthUserChurn is an entity that holds the setter/mutators and getters/accessors for the fields:
    - users lost during period (int)
    - users at start of period (int)
    - percent of all users (int)
    This model will trigger events using the observer observable pattern with notifications when:
    - Δε psql db (rider_id , rider_timestamp)
    - Δζ rf api (user_attentive , user_distracted)
    """

    def __init__(self):
        self._users_lost_during_period = None
        self._users_at_start_of_period = None
        self._percent_of_all_users = None
        # print(r'DEBUG:ModelNthUserChurn.py,ModelNthUserChurn __init__')

    """ users who have stopped using the service or product within the specified time period. """

    @property
    def users_lost_during_period(self) -> int:
        """Getter for the 'users_lost_during_period' attribute."""
        return self._users_lost_during_period

    @users_lost_during_period.setter
    def users_lost_during_period(self, value):
        """Setter for the 'users_lost_during_period' attribute."""
        if isinstance(value, (int, float)) and value is not None:
            self._users_lost_during_period = value
        else:
            raise ValueError(f"users_lost_during_period must be an int or float, but got: {value}.")

    """ users at the beginning of the period you are analyzing. """

    @property
    def users_at_start_of_period(self) -> int:
        """Getter for the 'users_at_start_of_period' attribute."""
        return self._users_at_start_of_period

    @users_at_start_of_period.setter
    def users_at_start_of_period(self, value):
        """Setter for the 'users_at_start_of_period' attribute."""
        if isinstance(value, (int, float)) and value is not None:
            self._users_at_start_of_period = value
        else:
            raise ValueError(f"users_at_start_of_period must be an int or float, but got: {value}.")

    """ percentage of all possible users as a population """
    @property
    def percent_of_all_users(self) -> int:
        """Getter for the 'percent_of_all_users' attribute."""
        return self._percent_of_all_users

    @percent_of_all_users.setter
    def percent_of_all_users(self, value):
        """Setter for the 'percent_of_all_users' attribute."""
        if isinstance(value, (int, float)) and value is not None:
            self._percent_of_all_users = value
        else:
            raise ValueError(f"percent_of_all_users must be an int or float, but got: {value}.")

    """ churn rate returned as a percentage """
    def churn_rate(self) -> float:
        return (self.users_lost_during_period/self.users_at_start_of_period) * self.percent_of_all_users

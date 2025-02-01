

class ModelMthValueUser:
    """
    ModelMthValueUser is an entity that holds the setter/mutators and getters/accessors for the fields:
    - number of customers (int)
    - number of purchases (int)
    - number of unique customers (int)
    - sum of customer lifespans (int)
    - total number of purchases (int)
    - total revenue (int)
    This model will trigger events using the observer observable pattern with notifications when:
    - Δε psql db (rider_id , rider_timestamp)
    - Δζ rf api (user_attentive , user_distracted)
    Insight; not comprehensive list of formulas for high value user,
    - CLV: Customer Lifetime Value
    - RFM: Recency, Frequency, Monetary
    - NPS: Net Promoter Score
    - CSAT: Customer Satisfaction Score
    - ARPU: Average Revenue Per User
    - LTV: Lifetime Value (another term for CLV)
    - CAC: Customer Acquisition Cost (often used in conjunction with CLV to assess value)
    - ROI: Return on Investment (sometimes used to evaluate the profitability of high-value users)
    """

    def __init__(self):
        self._number_of_purchases = None
        self._total_revenue = None
        self._total_number_of_purchases = None
        self._number_of_unique_customers = None
        self._sum_of_customer_lifespans = None
        self._number_of_customers = None
        # print(r'DEBUG:ModelMthValueUser.py,ModelMthValueUser __init__')

    @property
    def number_of_purchases(self) -> int:
        """Getter for the 'number_of_purchases' attribute."""
        return self._number_of_purchases

    @number_of_purchases.setter
    def number_of_purchases(self, value):
        """Setter for the 'number_of_purchases' attribute."""
        if isinstance(value, int) and value is not None:
            self._number_of_purchases = value
        else:
            raise ValueError("number_of_purchases must be a an int type, but got: {value}.")

    @property
    def total_revenue(self) -> int:
        """Getter for the 'total_revenue' attribute."""
        return self._total_revenue

    @total_revenue.setter
    def total_revenue(self, value):
        """Setter for the 'total_revenue' attribute."""
        if isinstance(value, int) and value is not None:
            self._total_revenue = value
        else:
            raise ValueError("total_revenue must be a an int type, but got: {value}.")

    """ This is the average amount of money a customer spends per purchase for rides. """
    def average_purchase_value(self) -> float:
        return self.total_revenue/self.number_of_purchases

    @property
    def total_number_of_purchases(self) -> int:
        """Getter for the 'total_number_of_purchases' attribute."""
        return self._total_number_of_purchases

    @total_number_of_purchases.setter
    def total_number_of_purchases(self, value):
        """Setter for the 'total_number_of_purchases' attribute."""
        if isinstance(value, int) and value is not None:
            self._total_number_of_purchases = value
        else:
            raise ValueError("total_number_of_purchases must be a an int type, but got: {value}.")

    @property
    def number_of_unique_customers(self) -> int:
        """Getter for the 'number_of_unique_customers' attribute."""
        return self._number_of_unique_customers

    @number_of_unique_customers.setter
    def number_of_unique_customers(self, value):
        """Setter for the 'number_of_unique_customers' attribute."""
        if isinstance(value, int) and value is not None:
            self._number_of_unique_customers = value
        else:
            raise ValueError("number_of_unique_customers must be a an int type, but got: {value}.")

    """ This is the average number of purchases for rides a customer makes within a given time period. """
    def average_purchase_frequency(self) -> float:
        return self.total_number_of_purchases/self.number_of_unique_customers

    @property
    def sum_of_customer_lifespans(self) -> int:
        """Getter for the 'sum_of_customer_lifespans' attribute."""
        return self._sum_of_customer_lifespans

    @sum_of_customer_lifespans.setter
    def sum_of_customer_lifespans(self, value):
        """Setter for the 'sum_of_customer_lifespans' attribute."""
        if isinstance(value, int) and value is not None:
            self._sum_of_customer_lifespans = value
        else:
            raise ValueError("sum_of_customer_lifespans must be a an int type, but got: {value}.")

    @property
    def number_of_customers(self) -> int:
        """Getter for the 'number_of_customers' attribute."""
        return self._number_of_customers

    @number_of_customers.setter
    def number_of_customers(self, value):
        """Setter for the 'number_of_customers' attribute."""
        if isinstance(value, int) and value is not None:
            self._number_of_customers = value
        else:
            raise ValueError("number_of_customers must be a an int type, but got: {value}.")

    """ This is the average duration a customer continues to make purchases for rides. """
    def customer_lifespan(self) -> float:
        return self.sum_of_customer_lifespans/self.number_of_customers

    """ Calculating High-Value Users for the RiderShare Application, CVL to HVU """
    def customer_lifetime_value(self) -> float:
        return self.average_purchase_value() * self.average_purchase_frequency() * self.customer_lifespan()

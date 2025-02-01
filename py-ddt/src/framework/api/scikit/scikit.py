import os


class ScikitApi:
    """
    ScikitApi is an entity that will take in data from this client,
    (1) artifact - rideshare-uber, filtered, that tells us...
        when a user was pickedup and droppedoff which calcualtes timeofride
    (2) dumps - rideshare-mocked, filtered, that tells us...
        when a user rides, using rider_id and rider_timestamp
        , we can 'fake' and compare to (1) passenger id and passenger count
    (3) roboflowed - rideshare-visioned, filtered, that tells us...
        when a user was attentive or distracted or unknown
    * GOAL * we are after M:'high-value-user' and N:'user-churn'
    using the data from these three sources we will calculate them. inspiration...
    μ : high value user
    ν : user churn
    α : customer lifetime value
    β : customer acquisition cost
    γ : retention rate
    remember to write about the models being spoofed which makes them biased and
    mention about the probability of these events actually ocuring in a practical environment.
    TODO: documentation for ScikitApi.py
    """
    def __init__(self):
        print(r'DEBUG:scikitapi.py,SciKitApi __init__')

    @staticmethod
    def caller():
        print(os.getenv("API_KEY_SCIKIT"))

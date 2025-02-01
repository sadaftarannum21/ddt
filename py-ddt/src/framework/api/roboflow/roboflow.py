import os


class RoboFlowApi:
    """
    RoboFlowApi is an entity that will take data in the form of pictures that were captured during the
    ride with the permission of the user, we will upload this package to the cloud platform
    , and learn from the resource using computer vision to detect user engagement,
    , for now it will be enough to have three type of events,
     (1) user looking within a 45* angle, means user was looking towards the driver, attentive
     (2) user looking past a 45* angle, means user was looking towards the sides, distracted
     (3) user fits into an undefined state, out of the camera, obfuscate this result, unknown.
    we want to get a file back from roboflow that tells us confidence whether the user was
    in the state of attentive, distracted, or unknown.
    TODO: documentation for RoboFlowApi.py
    """
    def __init__(self):
        print(r'DEBUG:roboflow.py,RoboFlowApi __init__')

    @staticmethod
    def caller():
        print(os.getenv("API_KEY_ROBOFLOW"))

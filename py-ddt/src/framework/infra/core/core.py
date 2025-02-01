from src.framework.infra.core.flowcntrl import FlowCntrl
from src.framework.infra.core.sandbox import SandBox


class Core:
    """
    Core is an entity that manages the control unit logic for unique modes
     and handles dependency injection that aligns to unified data flow.
    TODO: documentation for Core.py
    """

    def __init__(self):
        print(r'DEBUG:core.py,Core __init__')
        # FlowCntrl().fire_mode()
        # FlowCntrl().fire_sql_mode()
        # FlowCntrl().fire_ml_mode()
        SandBox()

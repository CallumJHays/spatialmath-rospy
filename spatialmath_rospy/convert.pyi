from typing import Any, Union, overload

from spatialmath import SE3, Quaternion, UnitQuaternion

from std_msgs.msg import Header
from geometry_msgs.msg import Pose, PoseStamped, Twist


class SE3Stamped(SE3):
    def __init__(self, header: Header, *args, **kwargs) -> None: ...

@overload
def convert(obj: Pose) -> SE3: ...

@overload
def convert(obj: SE3) -> Pose: ...

@overload
def convert(obj: PoseStamped) -> SE3Stamped: ...

@overload
def convert(obj: SE3Stamped) -> PoseStamped: ...

@overload
def convert(obj: PoseStamped) -> SE3: ...

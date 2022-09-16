
from typing import Any, Union, overload

from spatialmath import SE3, Quaternion, UnitQuaternion

from std_msgs.msg import Header
from geometry_msgs.msg import Pose, PoseStamped, Twist


class SE3Stamped(SE3):
    def __init__(self, header: Header, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)



def convert(obj):
    if isinstance(obj, SE3):
        return Pose(
            position=obj.t,
            orientation=Quaternion(obj.R)
        )

    elif isinstance(obj, SE3Stamped):
        return PoseStamped(
            header=obj.header,
            pose=convert(obj)
        )

    elif isinstance(obj, Pose):
        return SE3(obj.position, UnitQuaternion(obj.orientation))

    elif isinstance(obj, PoseStamped):
        return SE3Stamped(obj.header, convert(obj.pose))

    elif isinstance(obj, Twist):
        return SE3(obj.linear, UnitQuaternion(obj.angular))

    else:
        raise TypeError(f"Cannot convert unsupported type {type(obj)} for object {repr(obj)}")

from typing import Optional, Union, overload
from typing_extensions import Literal

from std_msgs.msg import Header
import geometry_msgs.msg as gm
import spatialmath as sm
import spatialmath.base as smb

__all__ = ["to_ros", "to_spatialmath"]

@overload
def to_ros(
    obj: Union[sm.SE3, sm.SO3],
    header: None = None,
    *,
    as_tf: Literal[False] = False
) -> gm.Pose:
    ...


@overload
def to_ros(
    obj: Union[sm.SE3, sm.SO3],
    header: Header,
    *,
    as_tf: Literal[False] = False
) -> gm.PoseStamped:
    ...


@overload
def to_ros(
    obj: Union[sm.SE3, sm.SO3, sm.UnitQuaternion],
    header: None = None,
    *,
    as_tf: Literal[True]
) -> gm.Transform:
    ...


@overload
def to_ros(
    obj: Union[sm.SE3, sm.SO3, sm.UnitQuaternion],
    header: Header,
    *,
    as_tf: Literal[True]
) -> gm.TransformStamped:
    ...

@overload
def to_ros(
    obj: sm.UnitQuaternion,
    header: None = None,
    *,
    as_tf: Literal[False] = False
) -> gm.Quaternion:
    ...

@overload
def to_ros(
    obj: sm.UnitQuaternion,
    header: Header,
    *,
    as_tf: Literal[False] = False
) -> gm.QuaternionStamped:
    ...

def to_ros(
    obj: Union[sm.SE3, sm.SO3, sm.UnitQuaternion],
    header: Optional[Header] = None,
    *,
    as_tf: bool = False
) -> Union[
    gm.Pose, gm.PoseStamped,
    gm.Quaternion, gm.QuaternionStamped,
    gm.Transform, gm.TransformStamped
]:
    """
    Convert a supported spatialmath object to an equivalent ROS message.

    :param obj:
        The spatialmath object to convert.
        Can be an :class:`sm.SE3`, :class:`sm.SO3` or a :class:`sm.UnitQuaternion`
    :param header: (default: None)
        Optional ros msg :class:`Header`.
        If provided, the `*Stamped` equivalent message will be output.
    :param as_tf: (default: False)
        Whether to return the result as a :class:`gm.Transform` instead of a :class:`gm.Pose` or :class:`gm.Quaternion`.
    :return:
        The resulting ROS message.

    The following conversions are supported:

    - :class:`sm.SE3` or :class:`sm.SO3` -> :class:`gm.Pose` or :class:`gm.PoseStamped`
    - :class:`sm.SE3`, :class:`sm.SO3` or :class:`sm.UnitQuaternion` -> :class:`gm.Transform` or :class:`gm.TransformStamped`.
    - :class:`sm.UnitQuaternion` -> :class:`gm.Quaternion` or :class:`gm.QuaternionStamped`

    """

    # construct the appropriate geometric output object
    res = gm.Transform(
        translation=gm.Vector3(0, 0, 0) if not isinstance(obj, sm.SE3) else gm.Vector3(*obj.t),
        rotation=gm.Quaternion(*smb.r2q(obj.R, order="xyzs"))
    ) if as_tf else gm.Quaternion(
        *obj.v, obj.s
    ) if isinstance(obj, sm.UnitQuaternion) else gm.Pose(
        position=gm.Point(0, 0, 0) if not isinstance(obj, sm.SE3) else gm.Point(*obj.t),
        orientation=gm.Quaternion(*smb.r2q(obj.R, order="xyzs"))
    )
    
    # if a header was specified, wrap the result in the corresponding stamped message
    if header is not None:
        res = gm.TransformStamped(
            header=header,
            transform=res
        ) if as_tf else gm.QuaternionStamped(
            header=header,
            quaternion=res
        ) if isinstance(obj, sm.UnitQuaternion) else gm.PoseStamped(
            header=header,
            pose=res
        )
    
    return res


@overload
def to_spatialmath(obj: Union[gm.Pose, gm.Transform]) -> sm.SE3:
    ...
    
@overload
def to_spatialmath(obj: gm.Quaternion) -> sm.UnitQuaternion:
    ...

def to_spatialmath(
    obj: Union[gm.Pose, gm.Transform, gm.Quaternion]
) -> Union[sm.SE3, sm.UnitQuaternion]:
    """Convert a supported ROS message to an equivalent spatialmath object.

    :param obj:
        The ROS message to convert.
        Can be a :class:`gm.Pose`, :class:`gm.Transform` or :class:`gm.Quaternion`.
    :return:
        The resulting spatialmath object.

    The following conversions are supported:

    - :class:`gm.Pose` or :class:`gm.PoseStamped` -> :class:`sm.SE3`
    - :class:`gm.Quaternion` or :class:`gm.QuaternionStamped` -> :class:`sm.UnitQuaternion`
    - :class:`gm.Transform` or :class:`gm.TransformStamped` -> :class:`sm.SE3`
    """    
    
    if isinstance(obj, gm.Quaternion):
        return sm.UnitQuaternion(obj.w, [obj.x, obj.y, obj.z])
    
    def raise_err():
        raise ValueError(f"Unable to convert {type(obj)} to SE3")

    pos, rot = \
        (obj.position, obj.orientation) if isinstance(obj, gm.Pose) else \
        (obj.translation, obj.rotation) if isinstance(obj, gm.Transform) else \
        raise_err()

    return sm.SE3.Rt(
        R=smb.q2r([rot.x, rot.y, rot.z, rot.w], order="xyzs"),
        t=[pos.x, pos.y, pos.z]
    )

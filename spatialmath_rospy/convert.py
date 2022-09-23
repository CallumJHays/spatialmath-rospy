
from typing import TYPE_CHECKING, Optional, Union, overload
from typing_extensions import Literal

import spatialmath as sm
import spatialmath.base as smb

if TYPE_CHECKING:
    from std_msgs.msg import Header
    import geometry_msgs.msg as gm

__all__ = ["to_ros", "to_spatialmath"]

@overload
def to_ros(
    obj: Union[sm.SE3, sm.SO3],
    header: None = None,
    *,
    as_tf: Literal[False] = False
) -> 'gm.Pose':
    ...


@overload
def to_ros(
    obj: Union[sm.SE3, sm.SO3],
    header: 'Header',
    *,
    as_tf: Literal[False] = False
) -> 'gm.PoseStamped':
    ...


@overload
def to_ros(
    obj: Union[sm.SE3, sm.SO3, sm.UnitQuaternion],
    header: None = None,
    *,
    as_tf: Literal[True]
) -> 'gm.Transform':
    ...


@overload
def to_ros(
    obj: Union[sm.SE3, sm.SO3, sm.UnitQuaternion],
    header: 'Header',
    *,
    as_tf: Literal[True]
) -> 'gm.TransformStamped':
    ...

@overload
def to_ros(
    obj: sm.UnitQuaternion,
    header: None = None,
    *,
    as_tf: Literal[False] = False
) -> 'gm.Quaternion':
    ...

@overload
def to_ros(
    obj: sm.UnitQuaternion,
    header: 'Header',
    *,
    as_tf: Literal[False] = False
) -> 'gm.QuaternionStamped':
    ...

def to_ros(
    obj: Union[sm.SE3, sm.SO3, sm.UnitQuaternion],
    header: Optional['Header'] = None,
    *,
    as_tf: bool = False
) -> Union[
    'gm.Pose', 'gm.PoseStamped',
    'gm.Quaternion', 'gm.QuaternionStamped',
    'gm.Transform', 'gm.TransformStamped'
]:
    """
    Convert a supported spatialmath object to an equivalent ROS message.
    The following conversions are supported:

    - :class:`SE3` | :class:`SO3` -> :class:`Pose` | :class:`PoseStamped`
    - :class:`SE3` | :class:`SO3` | :class:`UnitQuaternion` -> :class:`Transform` | :class:`TransformStamped`.
    - :class:`UnitQuaternion` -> :class:`Quaternion` | :class:`QuaternionStamped`

    Args:
        obj: The spatialmath object to convert.
            Can be an :class:`SE3`, :class:`SO3` or a :class:`UnitQuaternion`
        header: Optional ros msg :class:`Header`.
            If provided, the `*Stamped` equivalent message will be output.
        as_tf: Whether to return the result as a :class:`Transform`,
            instead of a :class:`Pose` or :class:`Quaternion`.
    
    Returns:
        The resulting ROS message.
        
    Raises:
        AssertionError: If obj's type is not supported.
    """
    import geometry_msgs.msg as gm

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
def to_spatialmath(obj: Union['gm.Pose', 'gm.Transform']) -> sm.SE3:
    ...
    
@overload
def to_spatialmath(obj: 'gm.Quaternion') -> sm.UnitQuaternion:
    ...

def to_spatialmath(
    obj: Union['gm.Pose', 'gm.Transform', 'gm.Quaternion']
) -> Union[sm.SE3, sm.UnitQuaternion]:
    """
    Convert a supported ROS message to an equivalent spatialmath object.
    The following conversions are supported:

    - :class:`gm.Pose` -> :class:`sm.SE3`
    - :class:`gm.Quaternion` -> :class:`sm.UnitQuaternion`
    - :class:`gm.Transform` -> :class:`sm.SE3`

    Args:
        obj: The ROS message to convert.
            Can be a :class:`gm.Pose`, :class:`gm.Transform` or :class:`gm.Quaternion`.
    
    Returns:
        The resulting spatialmath object. (:class:`sm.SE3` or :class:`sm.UnitQuaternion`)

    Raises:
        AssertionError: If obj's type is not supported.
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

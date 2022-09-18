
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
def to_spatialmath(obj: Union[gm.Pose, gm.PoseStamped, gm.Transform, gm.TransformStamped]) -> sm.SE3:
    ...
    
@overload
def to_spatialmath(obj: Union[gm.Quaternion, gm.QuaternionStamped]) -> sm.UnitQuaternion:
    ...

def to_spatialmath(
    obj: Union[
        gm.Pose, gm.PoseStamped,
        gm.Quaternion, gm.QuaternionStamped,
        gm.Transform, gm.TransformStamped
    ]
) -> Union[sm.SE3, sm.UnitQuaternion]:

    raw = \
        obj.pose if isinstance(obj, gm.PoseStamped) else \
        obj.transform if isinstance(obj, gm.TransformStamped) else \
        obj.quaternion if isinstance(obj, gm.QuaternionStamped) else \
        obj
    
    if isinstance(raw, gm.Quaternion):
        return sm.UnitQuaternion(raw.w, [raw.x, raw.y, raw.z])
    
    def raise_err():
        raise ValueError(f"Unable to convert {type(obj)} to SE3")

    pos, rot = \
        (raw.position, raw.orientation) if isinstance(raw, gm.Pose) else \
        (raw.translation, raw.rotation) if isinstance(raw, gm.Transform) else \
        raise_err()

    return sm.SE3.Rt(
        R=smb.q2r([rot.x, rot.y, rot.z, rot.w], order="xyzs"),
        t=[pos.x, pos.y, pos.z]
    )

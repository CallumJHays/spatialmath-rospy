
from typing import Type, Union, Optional, overload, Literal
from typing_extensions import Self
import spatialmath as sm
import spatialmath.base as smb

from std_msgs.msg import Header
import geometry_msgs.msg as gm

from spatialmath_rospy import to_ros, to_spatialmath


class ROSCompatMixin:

    @overload
    def to_ros(
        self: Union[sm.SE3, sm.SO3],
        header: None = None,
        *,
        as_tf: Literal[False] = False
    ) -> gm.Pose:
        ...


    @overload
    def to_ros(
        self: Union[sm.SE3, sm.SO3],
        header: Header,
        *,
        as_tf: Literal[False] = False
    ) -> gm.PoseStamped:
        ...


    @overload
    def to_ros(
        self: Union[sm.SE3, sm.SO3, sm.UnitQuaternion],
        header: None = None,
        *,
        as_tf: Literal[True]
    ) -> gm.Transform:
        ...


    @overload
    def to_ros(
        self: Union[sm.SE3, sm.SO3, sm.UnitQuaternion],
        header: Header,
        *,
        as_tf: Literal[True]
    ) -> gm.TransformStamped:
        ...
        

    @overload
    def to_ros(
        self: sm.UnitQuaternion,
        header: None = None,
        *,
        as_tf: Literal[True]
    ) -> gm.Quaternion:
        ...

    @overload
    def to_ros(
        self: sm.UnitQuaternion,
        header: Header,
        *,
        as_tf: Literal[False]
    ) -> gm.QuaternionStamped:
        ...

    def to_ros(
        self,
        header: Optional[Header] = None,
        *,
        as_tf: bool = False
    ) -> Union[
        gm.Pose, gm.PoseStamped,
        gm.Quaternion, gm.QuaternionStamped,
        gm.Transform, gm.TransformStamped
    ]:
        assert isinstance(self, (sm.SE3, sm.SO3, sm.UnitQuaternion)), \
            f"ROSCompatMixin not compatible with type {self}"
        return to_ros(self, header, as_tf=as_tf) # type: ignore
    
    
    @classmethod
    @overload
    def from_ros(cls: Type[sm.SE3], obj: Union[gm.Pose, gm.PoseStamped, gm.Transform, gm.TransformStamped]) -> 'SE3':
        ...
        
    @classmethod
    @overload
    def from_ros(cls: Type[sm.SO3], obj: Union[gm.Quaternion, gm.QuaternionStamped]) -> 'SO3':
        ...

    @classmethod
    @overload
    def from_ros(cls: Type[sm.UnitQuaternion], obj: Union[gm.Quaternion, gm.QuaternionStamped]) -> 'UnitQuaternion':
        ...

    @classmethod
    def from_ros(
        cls,
        obj: Union[
            gm.Pose, gm.PoseStamped,
            gm.Quaternion, gm.QuaternionStamped,
            gm.Transform, gm.TransformStamped
        ]
    ):
        se3 = to_spatialmath(obj)

        if issubclass(cls, sm.SE3):
            return se3
        
        elif issubclass(cls, sm.SO3):
            return SO3(se3.R)

        else:
            assert issubclass(cls, sm.UnitQuaternion), \
                f"ROSCompatMixin not compatible with type {cls}"
            return UnitQuaternion(smb.r2q(se3.R))

class SE3(sm.SE3, ROSCompatMixin):
    pass

class SO3(sm.SO3, ROSCompatMixin):
    pass

class UnitQuaternion(sm.UnitQuaternion, ROSCompatMixin):
    pass
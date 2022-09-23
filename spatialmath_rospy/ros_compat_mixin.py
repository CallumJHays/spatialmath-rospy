
from typing import Type, Union, Optional, overload, TYPE_CHECKING
from typing_extensions import Literal, Self
import spatialmath as sm
import spatialmath.base as smb


from spatialmath_rospy import to_ros, to_spatialmath

if TYPE_CHECKING:
    from std_msgs.msg import Header
    import geometry_msgs.msg as gm

class ROSCompatMixin:
    """
    Mixin class for supported spatialmath-python classes
    adding the from_ros and to_ros conversion methods.

    Expected only to work with :class:`sm.SE3`, :class:`sm.SO3` and :class:`sm.UnitQuaternion`.
    """

    @overload
    def to_ros(
        self: Union[sm.SE3, sm.SO3],
        header: None = None,
        *,
        as_tf: Literal[False] = False
    ) -> 'gm.Pose':
        ...


    @overload
    def to_ros(
        self: Union[sm.SE3, sm.SO3],
        header: Header,
        *,
        as_tf: Literal[False] = False
    ) -> 'gm.PoseStamped':
        ...


    @overload
    def to_ros(
        self: Union[sm.SE3, sm.SO3, sm.UnitQuaternion],
        header: None = None,
        *,
        as_tf: Literal[True]
    ) -> 'gm.Transform':
        ...


    @overload
    def to_ros(
        self: Union[sm.SE3, sm.SO3, sm.UnitQuaternion],
        header: Header,
        *,
        as_tf: Literal[True]
    ) -> 'gm.TransformStamped':
        ...
        

    @overload
    def to_ros(
        self: sm.UnitQuaternion,
        header: None = None,
        *,
        as_tf: Literal[True]
    ) -> 'gm.Quaternion':
        ...

    @overload
    def to_ros(
        self: sm.UnitQuaternion,
        header: Header,
        *,
        as_tf: Literal[False]
    ) -> 'gm.QuaternionStamped':
        ...

    def to_ros(
        self,
        header: Optional[Header] = None,
        *,
        as_tf: bool = False
    ) -> Union[
        'gm.Pose', 'gm.PoseStamped',
        'gm.Quaternion', 'gm.QuaternionStamped',
        'gm.Transform', 'gm.TransformStamped'
    ]:
        """
        Return an equivalent ROS message to this object.
        The following conversions are supported:

        - :class:`SE3` | :class:`SO3` -> :class:`Pose` | :class:`PoseStamped`
        - :class:`SE3` | :class:`SO3` | :class:`UnitQuaternion` -> :class:`Transform` | :class:`TransformStamped`.
        - :class:`UnitQuaternion` -> :class:`Quaternion` | :class:`QuaternionStamped`

        Args:
            header: Optional ros msg :class:`Header`.
                If provided, the `*Stamped` equivalent message will be output.
            as_tf: Whether to return the result as a :class:`Transform`,
                instead of a :class:`Pose` or :class:`Quaternion`.
        
        Returns:
            The resulting ROS message.
            
        Raises:
            AssertionError: If this object is not a supported type.
        """
        assert isinstance(self, (sm.SE3, sm.SO3, sm.UnitQuaternion)), \
            f"ROSCompatMixin not compatible with type {self}"
        return to_ros(self, header, as_tf=as_tf) # type: ignore
    

    @classmethod
    def from_ros(cls, obj: Union['gm.Pose', 'gm.Transform', 'gm.Quaternion']) -> Self:
        """
        Produce an instance of the class from a supported ROS message.

        The following conversions are supported:

        - :class:`Pose` -> :class:`SE3`
        - :class:`Quaternion` -> :class:`UnitQuaternion`
        - :class:`Transform` -> :class:`SE3`

        Args:
            obj: The ROS message to convert.
                (:class:`Pose` | :class:`Transform` | :class:`Quaternion`).
        
        Returns:
            An instance of this subclass.
        
        Raises:
            AssertionError: If this class type is not supported.

        """
        
        se3 = to_spatialmath(obj)

        if issubclass(cls, sm.SE3):
            return se3 # type: ignore
        
        elif issubclass(cls, sm.SO3):
            return SO3(se3.R)

        else:
            assert issubclass(cls, sm.UnitQuaternion), \
                f"ROSCompatMixin not compatible with type {cls}"
            return UnitQuaternion(smb.r2q(se3.R))

class SE3(sm.SE3, ROSCompatMixin):
    "Spatialmath SE3 class with ROS compatibility"

class SO3(sm.SO3, ROSCompatMixin):
    "Spatialmath SO3 class with ROS compatibility"

class UnitQuaternion(sm.UnitQuaternion, ROSCompatMixin):
    "Spatialmath UnitQuaternion class with ROS compatibility"
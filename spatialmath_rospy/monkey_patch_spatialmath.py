"""
Offers a monkey_patch_spatialmath function to patch the spatialmath library,
upgrading it with a mixin class that adds ROS functionality.
"""

import spatialmath as sm
from spatialmath_rospy.ros_compat_mixin import ROSCompatMixin

def monkey_patch_spatialmath():
    "Monkey-patch the spatialmath library, adding ROSCompatMixin to the base classes of SE3, SO3 and UnitQuaternion"
    sm.SE3.__bases__ += (ROSCompatMixin,)
    sm.SO3.__bases__ += (ROSCompatMixin,)
    sm.UnitQuaternion.__bases__ += (ROSCompatMixin,)

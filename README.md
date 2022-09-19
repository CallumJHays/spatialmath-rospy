# spatialmath-rospy

<!-- TODO: set up all the services needed for these badges -->
<!-- <p align="center">
  <a href="https://github.com/CallumJHays/spatialmath-rospy/actions?query=workflow%3ACI">
    <img src="https://img.shields.io/github/workflow/status/CallumJHays/spatialmath-rospy/CI/main?label=CI&logo=github&style=flat-square" alt="CI Status" >
  </a>
  <a href="https://mathpad.readthedocs.io">
    <img src="https://img.shields.io/readthedocs/mathpad.svg?logo=read-the-docs&logoColor=fff&style=flat-square" alt="Documentation Status">
  </a>
  <a href="https://codecov.io/gh/CallumJHays/spatialmath-rospy">
    <img src="https://img.shields.io/codecov/c/github/CallumJHays/spatialmath-rospy.svg?logo=codecov&logoColor=fff&style=flat-square" alt="Test coverage percentage">
  </a>
</p>
<p align="center">
  <a href="https://pypi.org/project/spatialmath-rospy/">
    <img src="https://img.shields.io/pypi/v/spatialmath-rospy.svg?logo=python&logoColor=fff&style=flat-square" alt="PyPI Version">
  </a>
  <img src="https://img.shields.io/pypi/pyversions/spatialmath-rospy.svg?style=flat-square&logo=python&amp;logoColor=fff" alt="Supported Python versions">
  <img src="https://img.shields.io/pypi/l/spatialmath-rospy.svg?style=flat-square" alt="License">
</p> -->

Spatial Math for ROS.
Intergration library between [`rospy`](http://wiki.ros.org/rospy) and [`spatialmath-python`](https://pypi.org/project/spatialmath-python/).

Currently this lib just contains conversion functionality.

Expected to work in any ROS version, but tested only on ROS1 Noetic due to difficulties with the CI config.

# QuickStart

```bash
pip install spatialmath-rospy
```

## Using Extended Classes
[Recommended]

```python
# So far only SE3, SO3 and UniQuaternion are supported
from spatialmath_rospy import SE3, SO3, UnitQuaternion

pose_msg = SE3(1, 2, 3).to_ros()
print(pose_msg)
"""
position: 
  x: 1.0
  y: 2.0
  z: 3.0
orientation: 
  x: 0.0
  y: 0.0
  z: 0.0
  w: 1.0
"""

print(SE3.from_ros(pose_msg))
"""
  1         0         0         1         
  0         1         0         2         
  0         0         1         3         
  0         0         0         1
"""
```


## Using Conversion Functions

For those who prefer a functional style or don't want to use the extended classes

```python
import spatialmath as sm
from spatialmath_rospy import to_spatialmath, to_ros

pose_msg = to_ros(sm.SE3(1, 2, 3))
se3: sm.SE3 = to_spatialmath(pose_msg)
```

## [Link: Using Monkey-Patch](#using-monkey-patch)


## Support for `Transform` msgs

The `to_ros()` function returns a `Pose` msg by default.

A `Transform` msg can be returned instead with `to_ros(as_tf=True)`.

```python
from spatialmath_rospy import SE3

tf_msg = SE3(1, 2, 3).to_ros(as_tf=True)
print(tf_msg)
"""
translation: 
  x: 1.0
  y: 2.0
  z: 3.0
rotation: 
  x: 0.0
  y: 0.0
  z: 0.0
  w: 1.0
"""
```

## Support for `Quaternion` msgs

`Quaternion` msgs convert to `UnitQuaternion` objects and vice versa:

```python
from spatialmath_rospy import UnitQuaternion

quat_msg = UnitQuaternion(1, [0, 0, 0]).to_ros()
print(quat_msg)
print(UnitQuaternion.from_ros(quat_msg))
```

`UnitQuaternion` can also be converted to a `Transform` msg with `to_ros(as_tf=True)`:

```python
from spatialmath_rospy import UnitQuaternion, SE3

quat = UnitQuaternion(1, [0, 0, 0])

tf_msg = quat.to_ros(as_tf=True)
print(tf_msg)
"""
translation: 
  x: 0
  y: 0
  z: 0
rotation: 
  x: 0.0
  y: 0.0
  z: 0.0
  w: 1.0
"""
```

This `Transform` will have always zero translation.

## Stamped messages

Just pass a `std_msgs.msg.Header` in to `to_ros()` to construct stamped objects:

```python
from std_msgs.msg import Header
from spatialmath_rospy import SE3

pose_stamped_msg = SE3(1, 2, 3).to_ros(
  Header(frame_id="world")
)
print(pose_stamped_msg)
"""
header: 
  seq: 0
  stamp: 
    secs: 0
    nsecs:         0
  frame_id: "world"
pose: 
  position: 
    x: 1.0
    y: 2.0
    z: 3.0
  orientation: 
    x: 0.0
    y: 0.0
    z: 0.0
    w: 1.0
"""
```

This works for all supported ros msg types:
- `Pose` / `PoseStamped`
- `Transform` / `TransformStamped`
- `Quaternion` / `QuaternionStamped`

## Using monkey-patch
[not recommended]

You may prefer to use this option if wanting to add the `.from_ros()` and `.to_ros()` methods to the original `SE3`, `SO3` and `UnitQuaternion` classes via a monkey-patch. This may be useful for integrating legacy code. Not recommended as static type analysis tools like PyLance will not work.

```python
import spatialmath as sm
from spatialmath_rospy import monkey_patch_spatialmath

# Invoke this at any point before calling conversion functions
monkey_patch_spatialmath()

pose_msg = sm.SE3(1, 2, 3).to_ros()
```
<!-- Check out more examples in the [Examples directory](examples/) -->

<!-- ## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)): -->

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

<!-- This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome! -->

## Credits

This package was created with
[Cookiecutter](https://github.com/audreyr/cookiecutter) and the
[browniebroke/cookiecutter-pypackage](https://github.com/browniebroke/cookiecutter-pypackage)
project template.

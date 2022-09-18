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

Expected to work in any ROS version.
Tested on ROS1 Melodic and Noetic, as well as ROS2 Foxy, Galactic and Humble.

# QuickStart

```bash
pip install spatialmath-rospy
```

## Using extended classes
[recommended]

```python
from spatialmath_rospy import SE3

pose_msg = SE3(1, 2, 3).to_ros()
print(pose_msg)
print(SE3.from_ros(pose_msg))
```


## Using helper functions

```python
import spatialmath as sm
from spatialmath_rospy import from_ros, to_ros

pose_msg = to_ros(sm.SE3(1, 2, 3))
print(pose_msg)
print(from_ros(pose_msg))
```


## `Transform` msgs

The `to_ros()` function returns a `Pose` msg by default.

A `Transform` msg can be returned instead with `to_ros(as_tf=True)`.

```python
from spatialmath_rospy import SE3

tf_msg = SE3(1, 2, 3).to_ros(as_tf=True)
print(tf_msg)
print(from_ros(tf_msg))
```

## `Quaternion` msgs

`Quaternion` msgs convert to `UnitQuaternion` objects and vice versa.

```python
from spatialmath_rospy import UnitQuaternion

quat_msg = UnitQuaternion(1, [0, 0, 0]).to_ros()
print(quat_msg)
print(from_ros(quat_msg))
```

`UnitQuaternion` can also be converted to a `Transform` msg with `to_ros(as_tf=True)`.

This `Transform` will have zero translation.

```python
from spatialmath_rospy import UnitQuaternion

quat = UnitQuaternion(1, [0, 0, 0])

tf_msg = quat.to_ros(as_tf=True)
print(tf_msg)

se3 = from_ros(tf_msg)
print(se3)
```

## Stamped messages
Just pass a `std_msgs.msg.Header` in to `to_ros()` to construct stamped objects:

```python
from std_msgs.msg import Header
from spatialmath_rospy import SE3

pose_stamped_msg = SE3(1, 2, 3).to_ros(
  Header(frame_id="world")
)
print(pose_stamped_msg)
```

This works for all supported ros msg types:
- `Pose` / `PoseStamped`
- `Transform` / `TransformStamped`
- `Quaternion` / `QuaternionStamped`

## Using monkey-patch
[not recommended]

You may prefer to use this option if wanting to add the `from_ros()` and `to_ros()` methods to the original `SE3`, `SO3` and `UnitQuaternion` classes via a monkey-patch. This may be useful for integrating legacy code. Not recommended as static type analysis will not work.

```python
import spatialmath as sm
from spatialmath_rospy import monkey_patch_spatialmath

# Invoke this at any point before calling conversion functions
monkey_patch_spatialmath()

pose_msg = sm.SE3(1, 2, 3).to_ros()
print(pose_msg)
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

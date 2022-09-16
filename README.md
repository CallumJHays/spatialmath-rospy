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

Interface library between [`rospy`](http://wiki.ros.org/rospy) and [`spatialmath-python`](https://pypi.org/project/spatialmath-python/).

## QuickStart

```bash
pip install spatialmath-rospy
```

Conversions:

```python
from geometry_msgs.msg import PoseStamped
import spatialmath.base as smb
import spatialmath_rospy as sm_rospy

pose_msg: PoseStamped = sm_rospy.convert()

```

Check out more examples in the [Examples directory](./examples/)

## Installation

Install via pip:

`pip install mathpad`

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

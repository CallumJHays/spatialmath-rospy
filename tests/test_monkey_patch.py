"Tests generated with the help of github copilot (not very DRY)"

import numpy as np

from std_msgs.msg import Header
import geometry_msgs.msg as gm

from spatialmath import SE3, SO3, UnitQuaternion

import spatialmath_rospy
spatialmath_rospy.monkey_patch_spatialmath()


def test_se3_to_pose():
    se3 = SE3() # identity
    pose = se3.to_ros() # type: ignore

    assert isinstance(pose, gm.Pose)
    assert pose.position.x == 0
    assert pose.position.y == 0
    assert pose.position.z == 0
    assert pose.orientation.x == 0
    assert pose.orientation.y == 0
    assert pose.orientation.z == 0
    assert pose.orientation.w == 1

    se3_recreated = SE3.from_ros(pose) # type: ignore
    assert np.allclose(se3.t, se3_recreated.t)
    assert np.allclose(se3.R, se3_recreated.R)

def test_se3_to_pose_stamped():
    se3 = SE3() # identity
    header = Header()
    pose = se3.to_ros(header) # type: ignore

    assert isinstance(pose, gm.PoseStamped)
    assert pose.header is header
    assert pose.pose.position.x == 0
    assert pose.pose.position.y == 0
    assert pose.pose.position.z == 0
    assert pose.pose.orientation.x == 0
    assert pose.pose.orientation.y == 0
    assert pose.pose.orientation.z == 0
    assert pose.pose.orientation.w == 1

    se3_recreated = SE3.from_ros(pose) # type: ignore
    assert np.allclose(se3.t, se3_recreated.t)
    assert np.allclose(se3.R, se3_recreated.R)

def test_se3_to_transform():
    se3 = SE3() # identity
    transform = se3.to_ros(as_tf=True) # type: ignore

    assert isinstance(transform, gm.Transform)
    assert transform.translation.x == 0
    assert transform.translation.y == 0
    assert transform.translation.z == 0
    assert transform.rotation.x == 0
    assert transform.rotation.y == 0
    assert transform.rotation.z == 0
    assert transform.rotation.w == 1

    se3_recreated = SE3.from_ros(transform) # type: ignore
    assert np.allclose(se3.t, se3_recreated.t)
    assert np.allclose(se3.R, se3_recreated.R)

def test_se3_to_transform_stamped():
    se3 = SE3() # identity
    header = Header()
    transform = se3.to_ros(header, as_tf=True) # type: ignore

    assert isinstance(transform, gm.TransformStamped)
    assert transform.header is header
    assert transform.transform.translation.x == 0
    assert transform.transform.translation.y == 0
    assert transform.transform.translation.z == 0
    assert transform.transform.rotation.x == 0
    assert transform.transform.rotation.y == 0
    assert transform.transform.rotation.z == 0
    assert transform.transform.rotation.w == 1

    se3_recreated = SE3.from_ros(transform) # type: ignore
    assert np.allclose(se3.t, se3_recreated.t)
    assert np.allclose(se3.R, se3_recreated.R)

def test_so3_to_transform():
    so3 = SO3() # identity
    transform = so3.to_ros(as_tf=True) # type: ignore

    assert isinstance(transform, gm.Transform)
    assert transform.translation.x == 0
    assert transform.translation.y == 0
    assert transform.translation.z == 0
    assert transform.rotation.x == 0
    assert transform.rotation.y == 0
    assert transform.rotation.z == 0
    assert transform.rotation.w == 1

    se3_recreated = SE3.from_ros(transform) # type: ignore
    assert np.allclose(so3.R, se3_recreated.R)

def test_so3_to_transform_stamped():
    so3 = SO3() # identity
    header = Header()
    transform = so3.to_ros(header, as_tf=True) # type: ignore

    assert isinstance(transform, gm.TransformStamped)
    assert transform.header is header
    assert transform.transform.translation.x == 0
    assert transform.transform.translation.y == 0
    assert transform.transform.translation.z == 0
    assert transform.transform.rotation.x == 0
    assert transform.transform.rotation.y == 0
    assert transform.transform.rotation.z == 0
    assert transform.transform.rotation.w == 1

    se3_recreated = SE3.from_ros(transform) # type: ignore
    assert np.allclose(so3.R, se3_recreated.R)

def test_se3_to_pose_with_translation():
    se3 = SE3(1, 2, 3)
    pose = se3.to_ros() # type: ignore

    assert isinstance(pose, gm.Pose)
    assert pose.position.x == 1
    assert pose.position.y == 2
    assert pose.position.z == 3
    assert pose.orientation.x == 0
    assert pose.orientation.y == 0
    assert pose.orientation.z == 0
    assert pose.orientation.w == 1

    se3_recreated = SE3.from_ros(pose) # type: ignore
    assert np.allclose(se3.t, se3_recreated.t)
    assert np.allclose(se3.R, se3_recreated.R)

def test_se3_to_pose_stamped_with_translation():
    se3 = SE3(1, 2, 3)
    header = Header()
    pose = se3.to_ros(header) # type: ignore

    assert isinstance(pose, gm.PoseStamped)
    assert pose.header is header
    assert pose.pose.position.x == 1
    assert pose.pose.position.y == 2
    assert pose.pose.position.z == 3
    assert pose.pose.orientation.x == 0
    assert pose.pose.orientation.y == 0
    assert pose.pose.orientation.z == 0
    assert pose.pose.orientation.w == 1

    se3_recreated = SE3.from_ros(pose) # type: ignore
    assert np.allclose(se3.t, se3_recreated.t)
    assert np.allclose(se3.R, se3_recreated.R)

def test_se3_to_transform_with_translation():
    se3 = SE3(1, 2, 3)
    transform = se3.to_ros(as_tf=True) # type: ignore

    assert isinstance(transform, gm.Transform)
    assert transform.translation.x == 1
    assert transform.translation.y == 2
    assert transform.translation.z == 3
    assert transform.rotation.x == 0
    assert transform.rotation.y == 0
    assert transform.rotation.z == 0
    assert transform.rotation.w == 1

    se3_recreated = SE3.from_ros(transform) # type: ignore
    assert np.allclose(se3.t, se3_recreated.t)
    assert np.allclose(se3.R, se3_recreated.R)

def test_se3_to_transform_stamped_with_translation():
    se3 = SE3(1, 2, 3)
    header = Header()
    transform = se3.to_ros(header, as_tf=True) # type: ignore

    assert isinstance(transform, gm.TransformStamped)
    assert transform.header is header
    assert transform.transform.translation.x == 1
    assert transform.transform.translation.y == 2
    assert transform.transform.translation.z == 3
    assert transform.transform.rotation.x == 0
    assert transform.transform.rotation.y == 0
    assert transform.transform.rotation.z == 0
    assert transform.transform.rotation.w == 1

    se3_recreated = SE3.from_ros(transform) # type: ignore
    assert np.allclose(se3.t, se3_recreated.t)
    assert np.allclose(se3.R, se3_recreated.R)

def test_se3_to_pose_with_rotation():
    se3 = SE3.Rx(0.1) #* SE3.Ry(0.2) * SE3.Rz(0.3)
    quat = UnitQuaternion(se3.R)
    pose = se3.to_ros() # type: ignore

    assert isinstance(pose, gm.Pose)
    assert pose.position.x == 0
    assert pose.position.y == 0
    assert pose.position.z == 0

    ori = pose.orientation
    assert np.allclose(
        quat.v,
        np.array([ori.x, ori.y, ori.z])
    )
    assert np.allclose(quat.s, ori.w)

    se3_recreated = SE3.from_ros(pose) # type: ignore
    assert np.allclose(se3.t, se3_recreated.t)
    assert np.allclose(se3.R, se3_recreated.R)

def test_se3_to_pose_stamped_with_rotation():
    se3 = SE3.Rx(0.1) * SE3.Ry(0.2) * SE3.Rz(0.3)
    quat = UnitQuaternion(se3.R)
    header = Header()
    pose = se3.to_ros(header)

    assert isinstance(pose, gm.PoseStamped)
    assert pose.header is header
    assert pose.pose.position.x == 0
    assert pose.pose.position.y == 0
    assert pose.pose.position.z == 0

    ori = pose.pose.orientation
    assert np.allclose(
        quat.v,
        np.array([ori.x, ori.y, ori.z])
    )
    assert np.allclose(quat.s, ori.w)

    se3_recreated = SE3.from_ros(pose) # type: ignore
    assert np.allclose(se3.t, se3_recreated.t)
    assert np.allclose(se3.R, se3_recreated.R)

def test_se3_to_transform_with_rotation():
    se3 = SE3.Rx(0.1) * SE3.Ry(0.2) * SE3.Rz(0.3)
    quat = UnitQuaternion(se3.R)
    transform = se3.to_ros(as_tf=True)

    assert isinstance(transform, gm.Transform)
    assert transform.translation.x == 0
    assert transform.translation.y == 0
    assert transform.translation.z == 0

    ori = transform.rotation
    assert np.allclose(
        quat.v,
        np.array([ori.x, ori.y, ori.z])
    )
    assert np.allclose(quat.s, ori.w)

    se3_recreated = SE3.from_ros(transform) # type: ignore
    assert np.allclose(se3.t, se3_recreated.t)
    assert np.allclose(se3.R, se3_recreated.R)

def test_se3_to_transform_stamped_with_rotation():
    se3 = SE3.Rx(0.1) * SE3.Ry(0.2) * SE3.Rz(0.3)
    quat = UnitQuaternion(se3.R)
    header = Header()
    transform = se3.to_ros(header, as_tf=True)

    assert isinstance(transform, gm.TransformStamped)
    assert transform.header is header
    assert transform.transform.translation.x == 0
    assert transform.transform.translation.y == 0
    assert transform.transform.translation.z == 0

    ori = transform.transform.rotation
    assert np.allclose(
        quat.v,
        np.array([ori.x, ori.y, ori.z])
    )
    assert np.allclose(quat.s, ori.w)

    se3_recreated = SE3.from_ros(transform) # type: ignore
    assert np.allclose(se3.t, se3_recreated.t)
    assert np.allclose(se3.R, se3_recreated.R)

def test_se3_to_pose_with_translation_and_rotation():
    se3 = SE3(1, 2, 3) * SE3.Rx(0.1) * SE3.Ry(0.2) * SE3.Rz(0.3)
    quat = UnitQuaternion(se3.R)
    pose = se3.to_ros()
    assert isinstance(pose, gm.Pose)
    assert pose.position.x == 1
    assert pose.position.y == 2
    assert pose.position.z == 3

    ori = pose.orientation
    assert np.allclose(
        quat.v,
        np.array([ori.x, ori.y, ori.z])
    )
    assert np.allclose(quat.s, ori.w)

    se3_recreated = SE3.from_ros(pose) # type: ignore
    assert np.allclose(se3.t, se3_recreated.t)
    assert np.allclose(se3.R, se3_recreated.R)

def test_se3_to_pose_stamped_with_translation_and_rotation():
    se3: SE3 = SE3(1, 2, 3) * SE3.Rx(0.1) * SE3.Ry(0.2) * SE3.Rz(0.3)
    quat = UnitQuaternion(se3.R)
    header = Header()
    pose = se3.to_ros(header) # type: ignore

    assert isinstance(pose, gm.PoseStamped)
    assert pose.header is header
    assert pose.pose.position.x == 1
    assert pose.pose.position.y == 2
    assert pose.pose.position.z == 3

    ori = pose.pose.orientation
    assert np.allclose(
        quat.v,
        np.array([ori.x, ori.y, ori.z])
    )
    assert np.allclose(quat.s, ori.w)

    se3_recreated = SE3.from_ros(pose) # type: ignore
    assert np.allclose(se3.t, se3_recreated.t)
    assert np.allclose(se3.R, se3_recreated.R)

def test_se3_to_transform_with_translation_and_rotation():
    se3: SE3 = SE3(1, 2, 3) * SE3.Rx(0.1) * SE3.Ry(0.2) * SE3.Rz(0.3)
    quat = UnitQuaternion(se3.R)
    transform = se3.to_ros(as_tf=True) # type: ignore

    assert isinstance(transform, gm.Transform)
    assert transform.translation.x == 1
    assert transform.translation.y == 2
    assert transform.translation.z == 3

    ori = transform.rotation
    assert np.allclose(
        quat.v,
        np.array([ori.x, ori.y, ori.z])
    )
    assert np.allclose(quat.s, ori.w)

    se3_recreated = SE3.from_ros(transform) # type: ignore
    assert np.allclose(se3.t, se3_recreated.t)
    assert np.allclose(se3.R, se3_recreated.R)

def test_se3_to_transform_stamped_with_translation_and_rotation():
    se3: SE3 = SE3(1, 2, 3) * SE3.Rx(0.1) * SE3.Ry(0.2) * SE3.Rz(0.3)
    quat = UnitQuaternion(se3.R)
    header = Header()
    transform = se3.to_ros(header, as_tf=True) # type: ignore

    assert isinstance(transform, gm.TransformStamped)
    assert transform.header is header
    assert transform.transform.translation.x == 1
    assert transform.transform.translation.y == 2
    assert transform.transform.translation.z == 3

    ori = transform.transform.rotation
    assert np.allclose(
        quat.v,
        np.array([ori.x, ori.y, ori.z])
    )
    assert np.allclose(quat.s, ori.w)

    se3_recreated = SE3.from_ros(transform) # type: ignore
    assert np.allclose(se3.t, se3_recreated.t)
    assert np.allclose(se3.R, se3_recreated.R)

def test_so3_to_pose():
    so3: SO3 = SO3.Rx(0.1) * SO3.Ry(0.2) * SO3.Rz(0.3)
    quat = UnitQuaternion(so3)
    pose = so3.to_ros() # type: ignore
    assert isinstance(pose, gm.Pose)
    assert pose.position.x == 0
    assert pose.position.y == 0
    assert pose.position.z == 0

    ori = pose.orientation
    assert np.allclose(
        quat.v,
        np.array([ori.x, ori.y, ori.z])
    )
    assert np.allclose(quat.s, ori.w)

    se3_recreated = SE3.from_ros(pose) # type: ignore
    assert np.allclose(so3.R, se3_recreated.R)

def test_so3_to_pose_stamped():
    so3 = SO3.Rx(0.1) * SO3.Ry(0.2) * SO3.Rz(0.3)
    quat = UnitQuaternion(so3)
    header = Header()
    pose = so3.to_ros(header)

    assert isinstance(pose, gm.PoseStamped)
    assert pose.header is header
    assert pose.pose.position.x == 0
    assert pose.pose.position.y == 0
    assert pose.pose.position.z == 0

    ori = pose.pose.orientation
    assert np.allclose(
        quat.v,
        np.array([ori.x, ori.y, ori.z])
    )
    assert np.allclose(quat.s, ori.w)

    se3_recreated = SE3.from_ros(pose) # type: ignore
    assert np.allclose(so3.R, se3_recreated.R)

"Tests generated with the help of github copilot (not very DRY)"

import spatialmath_rospy as sm_rospy
import numpy as np

from std_msgs.msg import Header
import spatialmath as sm
import geometry_msgs.msg as gm

def test_se3_to_pose():
    se3 = sm.SE3() # identity
    pose = sm_rospy.to_ros(se3)

    assert isinstance(pose, gm.Pose)
    assert pose.position.x == 0
    assert pose.position.y == 0
    assert pose.position.z == 0
    assert pose.orientation.x == 0
    assert pose.orientation.y == 0
    assert pose.orientation.z == 0
    assert pose.orientation.w == 1

    se3_recreated = sm_rospy.to_spatialmath(pose)
    assert np.allclose(se3.t, se3_recreated.t)
    assert np.allclose(se3.R, se3_recreated.R)

def test_se3_to_pose_stamped():
    se3 = sm.SE3() # identity
    header = Header()
    pose = sm_rospy.to_ros(se3, header)

    assert isinstance(pose, gm.PoseStamped)
    assert pose.header is header
    assert pose.pose.position.x == 0
    assert pose.pose.position.y == 0
    assert pose.pose.position.z == 0
    assert pose.pose.orientation.x == 0
    assert pose.pose.orientation.y == 0
    assert pose.pose.orientation.z == 0
    assert pose.pose.orientation.w == 1

    se3_recreated = sm_rospy.to_spatialmath(pose)
    assert np.allclose(se3.t, se3_recreated.t)
    assert np.allclose(se3.R, se3_recreated.R)

def test_se3_to_transform():
    se3 = sm.SE3() # identity
    transform = sm_rospy.to_ros(se3, as_tf=True)

    assert isinstance(transform, gm.Transform)
    assert transform.translation.x == 0
    assert transform.translation.y == 0
    assert transform.translation.z == 0
    assert transform.rotation.x == 0
    assert transform.rotation.y == 0
    assert transform.rotation.z == 0
    assert transform.rotation.w == 1

    se3_recreated = sm_rospy.to_spatialmath(transform)
    assert np.allclose(se3.t, se3_recreated.t)
    assert np.allclose(se3.R, se3_recreated.R)

def test_se3_to_transform_stamped():
    se3 = sm.SE3() # identity
    header = Header()
    transform = sm_rospy.to_ros(se3, header, as_tf=True)

    assert isinstance(transform, gm.TransformStamped)
    assert transform.header is header
    assert transform.transform.translation.x == 0
    assert transform.transform.translation.y == 0
    assert transform.transform.translation.z == 0
    assert transform.transform.rotation.x == 0
    assert transform.transform.rotation.y == 0
    assert transform.transform.rotation.z == 0
    assert transform.transform.rotation.w == 1

    se3_recreated = sm_rospy.to_spatialmath(transform)
    assert np.allclose(se3.t, se3_recreated.t)
    assert np.allclose(se3.R, se3_recreated.R)

def test_so3_to_transform():
    so3 = sm.SO3() # identity
    transform = sm_rospy.to_ros(so3, as_tf=True)

    assert isinstance(transform, gm.Transform)
    assert transform.translation.x == 0
    assert transform.translation.y == 0
    assert transform.translation.z == 0
    assert transform.rotation.x == 0
    assert transform.rotation.y == 0
    assert transform.rotation.z == 0
    assert transform.rotation.w == 1

    se3_recreated = sm_rospy.to_spatialmath(transform)
    assert np.allclose(so3.R, se3_recreated.R)

def test_so3_to_transform_stamped():
    so3 = sm.SO3() # identity
    header = Header()
    transform = sm_rospy.to_ros(so3, header, as_tf=True)

    assert isinstance(transform, gm.TransformStamped)
    assert transform.header is header
    assert transform.transform.translation.x == 0
    assert transform.transform.translation.y == 0
    assert transform.transform.translation.z == 0
    assert transform.transform.rotation.x == 0
    assert transform.transform.rotation.y == 0
    assert transform.transform.rotation.z == 0
    assert transform.transform.rotation.w == 1

    se3_recreated = sm_rospy.to_spatialmath(transform)
    assert np.allclose(so3.R, se3_recreated.R)

def test_se3_to_pose_with_translation():
    se3 = sm.SE3(1, 2, 3)
    pose = sm_rospy.to_ros(se3)

    assert isinstance(pose, gm.Pose)
    assert pose.position.x == 1
    assert pose.position.y == 2
    assert pose.position.z == 3
    assert pose.orientation.x == 0
    assert pose.orientation.y == 0
    assert pose.orientation.z == 0
    assert pose.orientation.w == 1

    se3_recreated = sm_rospy.to_spatialmath(pose)
    assert np.allclose(se3.t, se3_recreated.t)
    assert np.allclose(se3.R, se3_recreated.R)

def test_se3_to_pose_stamped_with_translation():
    se3 = sm.SE3(1, 2, 3)
    header = Header()
    pose = sm_rospy.to_ros(se3, header)

    assert isinstance(pose, gm.PoseStamped)
    assert pose.header is header
    assert pose.pose.position.x == 1
    assert pose.pose.position.y == 2
    assert pose.pose.position.z == 3
    assert pose.pose.orientation.x == 0
    assert pose.pose.orientation.y == 0
    assert pose.pose.orientation.z == 0
    assert pose.pose.orientation.w == 1

    se3_recreated = sm_rospy.to_spatialmath(pose)
    assert np.allclose(se3.t, se3_recreated.t)
    assert np.allclose(se3.R, se3_recreated.R)

def test_se3_to_transform_with_translation():
    se3 = sm.SE3(1, 2, 3)
    transform = sm_rospy.to_ros(se3, as_tf=True)

    assert isinstance(transform, gm.Transform)
    assert transform.translation.x == 1
    assert transform.translation.y == 2
    assert transform.translation.z == 3
    assert transform.rotation.x == 0
    assert transform.rotation.y == 0
    assert transform.rotation.z == 0
    assert transform.rotation.w == 1

    se3_recreated = sm_rospy.to_spatialmath(transform)
    assert np.allclose(se3.t, se3_recreated.t)
    assert np.allclose(se3.R, se3_recreated.R)

def test_se3_to_transform_stamped_with_translation():
    se3 = sm.SE3(1, 2, 3)
    header = Header()
    transform = sm_rospy.to_ros(se3, header, as_tf=True)

    assert isinstance(transform, gm.TransformStamped)
    assert transform.header is header
    assert transform.transform.translation.x == 1
    assert transform.transform.translation.y == 2
    assert transform.transform.translation.z == 3
    assert transform.transform.rotation.x == 0
    assert transform.transform.rotation.y == 0
    assert transform.transform.rotation.z == 0
    assert transform.transform.rotation.w == 1

    se3_recreated = sm_rospy.to_spatialmath(transform)
    assert np.allclose(se3.t, se3_recreated.t)
    assert np.allclose(se3.R, se3_recreated.R)

def test_se3_to_pose_with_rotation():
    se3 = sm.SE3.Rx(0.1) #* sm.SE3.Ry(0.2) * sm.SE3.Rz(0.3)
    quat = sm.UnitQuaternion(se3.R)
    pose = sm_rospy.to_ros(se3)

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

    se3_recreated = sm_rospy.to_spatialmath(pose)
    assert np.allclose(se3.t, se3_recreated.t)
    assert np.allclose(se3.R, se3_recreated.R)

def test_se3_to_pose_stamped_with_rotation():
    se3 = sm.SE3.Rx(0.1) * sm.SE3.Ry(0.2) * sm.SE3.Rz(0.3)
    quat = sm.UnitQuaternion(se3.R)
    header = Header()
    pose = sm_rospy.to_ros(se3, header)

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

    se3_recreated = sm_rospy.to_spatialmath(pose)
    assert np.allclose(se3.t, se3_recreated.t)
    assert np.allclose(se3.R, se3_recreated.R)

def test_se3_to_transform_with_rotation():
    se3 = sm.SE3.Rx(0.1) * sm.SE3.Ry(0.2) * sm.SE3.Rz(0.3)
    quat = sm.UnitQuaternion(se3.R)
    transform = sm_rospy.to_ros(se3, as_tf=True)

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

    se3_recreated = sm_rospy.to_spatialmath(transform)
    assert np.allclose(se3.t, se3_recreated.t)
    assert np.allclose(se3.R, se3_recreated.R)

def test_se3_to_transform_stamped_with_rotation():
    se3 = sm.SE3.Rx(0.1) * sm.SE3.Ry(0.2) * sm.SE3.Rz(0.3)
    quat = sm.UnitQuaternion(se3.R)
    header = Header()
    transform = sm_rospy.to_ros(se3, header, as_tf=True)

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

    se3_recreated = sm_rospy.to_spatialmath(transform)
    assert np.allclose(se3.t, se3_recreated.t)
    assert np.allclose(se3.R, se3_recreated.R)

def test_se3_to_pose_with_translation_and_rotation():
    se3 = sm.SE3(1, 2, 3) * sm.SE3.Rx(0.1) * sm.SE3.Ry(0.2) * sm.SE3.Rz(0.3)
    quat = sm.UnitQuaternion(se3.R)
    pose = sm_rospy.to_ros(se3)

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

    se3_recreated = sm_rospy.to_spatialmath(pose)
    assert np.allclose(se3.t, se3_recreated.t)
    assert np.allclose(se3.R, se3_recreated.R)

def test_se3_to_pose_stamped_with_translation_and_rotation():
    se3 = sm.SE3(1, 2, 3) * sm.SE3.Rx(0.1) * sm.SE3.Ry(0.2) * sm.SE3.Rz(0.3)
    quat = sm.UnitQuaternion(se3.R)
    header = Header()
    pose = sm_rospy.to_ros(se3, header)

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

    se3_recreated = sm_rospy.to_spatialmath(pose)
    assert np.allclose(se3.t, se3_recreated.t)
    assert np.allclose(se3.R, se3_recreated.R)

def test_se3_to_transform_with_translation_and_rotation():
    se3 = sm.SE3(1, 2, 3) * sm.SE3.Rx(0.1) * sm.SE3.Ry(0.2) * sm.SE3.Rz(0.3)
    quat = sm.UnitQuaternion(se3.R)
    transform = sm_rospy.to_ros(se3, as_tf=True)

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

    se3_recreated = sm_rospy.to_spatialmath(transform)
    assert np.allclose(se3.t, se3_recreated.t)
    assert np.allclose(se3.R, se3_recreated.R)

def test_se3_to_transform_stamped_with_translation_and_rotation():
    se3 = sm.SE3(1, 2, 3) * sm.SE3.Rx(0.1) * sm.SE3.Ry(0.2) * sm.SE3.Rz(0.3)
    quat = sm.UnitQuaternion(se3.R)
    header = Header()
    transform = sm_rospy.to_ros(se3, header, as_tf=True)

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

    se3_recreated = sm_rospy.to_spatialmath(transform)
    assert np.allclose(se3.t, se3_recreated.t)
    assert np.allclose(se3.R, se3_recreated.R)

def test_so3_to_pose():
    so3 = sm.SO3.Rx(0.1) * sm.SO3.Ry(0.2) * sm.SO3.Rz(0.3)
    quat = sm.UnitQuaternion(so3)
    pose = sm_rospy.to_ros(so3)

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

    se3_recreated = sm_rospy.to_spatialmath(pose)
    assert np.allclose(so3.R, se3_recreated.R)

def test_so3_to_pose_stamped():
    so3 = sm.SO3.Rx(0.1) * sm.SO3.Ry(0.2) * sm.SO3.Rz(0.3)
    quat = sm.UnitQuaternion(so3)
    header = Header()
    pose = sm_rospy.to_ros(so3, header)

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

    se3_recreated = sm_rospy.to_spatialmath(pose)
    assert np.allclose(so3.R, se3_recreated.R)

def test_unitquat_to_quaternion():
    so3 = sm.SO3.Rx(0.1) * sm.SO3.Ry(0.2) * sm.SO3.Rz(0.3)
    quat = sm.UnitQuaternion(so3)
    quat_ros = sm_rospy.to_ros(quat)

    assert isinstance(quat_ros, gm.Quaternion)
    assert np.allclose(quat.v, np.array([quat_ros.x, quat_ros.y, quat_ros.z]))
    assert np.allclose(quat.s, quat_ros.w)

def test_unitquat_to_quaternion_stamped():
    so3 = sm.SO3.Rx(0.1) * sm.SO3.Ry(0.2) * sm.SO3.Rz(0.3)
    quat = sm.UnitQuaternion(so3)
    header = Header()
    quat_ros = sm_rospy.to_ros(quat, header)

    assert isinstance(quat_ros, gm.QuaternionStamped)
    assert quat_ros.header is header
    assert np.allclose(quat.v, np.array([quat_ros.quaternion.x, quat_ros.quaternion.y, quat_ros.quaternion.z]))
    assert np.allclose(quat.s, quat_ros.quaternion.w)

def test_unitquat_to_transform():
    so3 = sm.SO3.Rx(0.1) * sm.SO3.Ry(0.2) * sm.SO3.Rz(0.3)
    quat = sm.UnitQuaternion(so3)
    transform = sm_rospy.to_ros(quat, as_tf=True)

    assert isinstance(transform, gm.Transform)
    assert transform.translation.x == 0
    assert transform.translation.y == 0
    assert transform.translation.z == 0

    ori = transform.rotation
    assert np.allclose(quat.v, np.array([ori.x, ori.y, ori.z]))
    assert np.allclose(quat.s, ori.w)

def test_unitquat_to_transform_stamped():
    so3 = sm.SO3.Rx(0.1) * sm.SO3.Ry(0.2) * sm.SO3.Rz(0.3)
    quat = sm.UnitQuaternion(so3)
    header = Header()
    transform = sm_rospy.to_ros(quat, header, as_tf=True)

    assert isinstance(transform, gm.TransformStamped)
    assert transform.header is header
    assert transform.transform.translation.x == 0
    assert transform.transform.translation.y == 0
    assert transform.transform.translation.z == 0

    ori = transform.transform.rotation
    assert np.allclose(quat.v, np.array([ori.x, ori.y, ori.z]))
    assert np.allclose(quat.s, ori.w)

def test_quaternion_to_unitquat():
    so3 = sm.SO3.Rx(0.1) * sm.SO3.Ry(0.2) * sm.SO3.Rz(0.3)
    quat = sm.UnitQuaternion(so3)
    quat_ros = sm_rospy.to_ros(quat)
    quat_recreated = sm_rospy.to_spatialmath(quat_ros)

    assert np.allclose(quat.v, quat_recreated.v)
    assert np.allclose(quat.s, quat_recreated.s)

def test_quaternion_stamped_to_unitquat():
    so3 = sm.SO3.Rx(0.1) * sm.SO3.Ry(0.2) * sm.SO3.Rz(0.3)
    quat = sm.UnitQuaternion(so3)
    header = Header()
    quat_ros = sm_rospy.to_ros(quat, header)
    quat_recreated = sm_rospy.to_spatialmath(quat_ros)

    assert np.allclose(quat.v, quat_recreated.v)
    assert np.allclose(quat.s, quat_recreated.s)
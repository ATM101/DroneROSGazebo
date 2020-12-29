# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from mavros_msgs/State.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import std_msgs.msg

class State(genpy.Message):
  _md5sum = "65cd0a9fff993b062b91e354554ec7e9"
  _type = "mavros_msgs/State"
  _has_header = True  # flag to mark the presence of a Header object
  _full_text = """# Current autopilot state
#
# Known modes listed here:
# http://wiki.ros.org/mavros/CustomModes
#
# For system_status values
# see https://mavlink.io/en/messages/common.html#MAV_STATE
#

std_msgs/Header header
bool connected
bool armed
bool guided
bool manual_input
string mode
uint8 system_status

string MODE_APM_PLANE_MANUAL = MANUAL
string MODE_APM_PLANE_CIRCLE = CIRCLE
string MODE_APM_PLANE_STABILIZE = STABILIZE
string MODE_APM_PLANE_TRAINING = TRAINING
string MODE_APM_PLANE_ACRO = ACRO
string MODE_APM_PLANE_FBWA = FBWA
string MODE_APM_PLANE_FBWB = FBWB
string MODE_APM_PLANE_CRUISE = CRUISE
string MODE_APM_PLANE_AUTOTUNE = AUTOTUNE
string MODE_APM_PLANE_AUTO = AUTO
string MODE_APM_PLANE_RTL = RTL
string MODE_APM_PLANE_LOITER = LOITER
string MODE_APM_PLANE_LAND = LAND
string MODE_APM_PLANE_GUIDED = GUIDED
string MODE_APM_PLANE_INITIALISING = INITIALISING
string MODE_APM_PLANE_QSTABILIZE = QSTABILIZE
string MODE_APM_PLANE_QHOVER = QHOVER
string MODE_APM_PLANE_QLOITER = QLOITER
string MODE_APM_PLANE_QLAND = QLAND
string MODE_APM_PLANE_QRTL = QRTL

string MODE_APM_COPTER_STABILIZE = STABILIZE
string MODE_APM_COPTER_ACRO = ACRO
string MODE_APM_COPTER_ALT_HOLD = ALT_HOLD
string MODE_APM_COPTER_AUTO = AUTO
string MODE_APM_COPTER_GUIDED = GUIDED
string MODE_APM_COPTER_LOITER = LOITER
string MODE_APM_COPTER_RTL = RTL
string MODE_APM_COPTER_CIRCLE = CIRCLE
string MODE_APM_COPTER_POSITION = POSITION
string MODE_APM_COPTER_LAND = LAND
string MODE_APM_COPTER_OF_LOITER = OF_LOITER
string MODE_APM_COPTER_DRIFT = DRIFT
string MODE_APM_COPTER_SPORT = SPORT
string MODE_APM_COPTER_FLIP = FLIP
string MODE_APM_COPTER_AUTOTUNE = AUTOTUNE
string MODE_APM_COPTER_POSHOLD = POSHOLD
string MODE_APM_COPTER_BRAKE = BRAKE
string MODE_APM_COPTER_THROW = THROW
string MODE_APM_COPTER_AVOID_ADSB = AVOID_ADSB
string MODE_APM_COPTER_GUIDED_NOGPS = GUIDED_NOGPS

string MODE_APM_ROVER_MANUAL = MANUAL
string MODE_APM_ROVER_LEARNING = LEARNING
string MODE_APM_ROVER_STEERING = STEERING
string MODE_APM_ROVER_HOLD = HOLD
string MODE_APM_ROVER_AUTO = AUTO
string MODE_APM_ROVER_RTL = RTL
string MODE_APM_ROVER_GUIDED = GUIDED
string MODE_APM_ROVER_INITIALISING = INITIALISING

string MODE_PX4_MANUAL = MANUAL
string MODE_PX4_ACRO = ACRO
string MODE_PX4_ALTITUDE = ALTCTL
string MODE_PX4_POSITION = POSCTL
string MODE_PX4_OFFBOARD = OFFBOARD
string MODE_PX4_STABILIZED = STABILIZED
string MODE_PX4_RATTITUDE = RATTITUDE
string MODE_PX4_MISSION = AUTO.MISSION
string MODE_PX4_LOITER = AUTO.LOITER
string MODE_PX4_RTL = AUTO.RTL
string MODE_PX4_LAND = AUTO.LAND
string MODE_PX4_RTGS = AUTO.RTGS
string MODE_PX4_READY = AUTO.READY
string MODE_PX4_TAKEOFF = AUTO.TAKEOFF

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
string frame_id
"""
  # Pseudo-constants
  MODE_APM_PLANE_MANUAL = 'MANUAL'
  MODE_APM_PLANE_CIRCLE = 'CIRCLE'
  MODE_APM_PLANE_STABILIZE = 'STABILIZE'
  MODE_APM_PLANE_TRAINING = 'TRAINING'
  MODE_APM_PLANE_ACRO = 'ACRO'
  MODE_APM_PLANE_FBWA = 'FBWA'
  MODE_APM_PLANE_FBWB = 'FBWB'
  MODE_APM_PLANE_CRUISE = 'CRUISE'
  MODE_APM_PLANE_AUTOTUNE = 'AUTOTUNE'
  MODE_APM_PLANE_AUTO = 'AUTO'
  MODE_APM_PLANE_RTL = 'RTL'
  MODE_APM_PLANE_LOITER = 'LOITER'
  MODE_APM_PLANE_LAND = 'LAND'
  MODE_APM_PLANE_GUIDED = 'GUIDED'
  MODE_APM_PLANE_INITIALISING = 'INITIALISING'
  MODE_APM_PLANE_QSTABILIZE = 'QSTABILIZE'
  MODE_APM_PLANE_QHOVER = 'QHOVER'
  MODE_APM_PLANE_QLOITER = 'QLOITER'
  MODE_APM_PLANE_QLAND = 'QLAND'
  MODE_APM_PLANE_QRTL = 'QRTL'
  MODE_APM_COPTER_STABILIZE = 'STABILIZE'
  MODE_APM_COPTER_ACRO = 'ACRO'
  MODE_APM_COPTER_ALT_HOLD = 'ALT_HOLD'
  MODE_APM_COPTER_AUTO = 'AUTO'
  MODE_APM_COPTER_GUIDED = 'GUIDED'
  MODE_APM_COPTER_LOITER = 'LOITER'
  MODE_APM_COPTER_RTL = 'RTL'
  MODE_APM_COPTER_CIRCLE = 'CIRCLE'
  MODE_APM_COPTER_POSITION = 'POSITION'
  MODE_APM_COPTER_LAND = 'LAND'
  MODE_APM_COPTER_OF_LOITER = 'OF_LOITER'
  MODE_APM_COPTER_DRIFT = 'DRIFT'
  MODE_APM_COPTER_SPORT = 'SPORT'
  MODE_APM_COPTER_FLIP = 'FLIP'
  MODE_APM_COPTER_AUTOTUNE = 'AUTOTUNE'
  MODE_APM_COPTER_POSHOLD = 'POSHOLD'
  MODE_APM_COPTER_BRAKE = 'BRAKE'
  MODE_APM_COPTER_THROW = 'THROW'
  MODE_APM_COPTER_AVOID_ADSB = 'AVOID_ADSB'
  MODE_APM_COPTER_GUIDED_NOGPS = 'GUIDED_NOGPS'
  MODE_APM_ROVER_MANUAL = 'MANUAL'
  MODE_APM_ROVER_LEARNING = 'LEARNING'
  MODE_APM_ROVER_STEERING = 'STEERING'
  MODE_APM_ROVER_HOLD = 'HOLD'
  MODE_APM_ROVER_AUTO = 'AUTO'
  MODE_APM_ROVER_RTL = 'RTL'
  MODE_APM_ROVER_GUIDED = 'GUIDED'
  MODE_APM_ROVER_INITIALISING = 'INITIALISING'
  MODE_PX4_MANUAL = 'MANUAL'
  MODE_PX4_ACRO = 'ACRO'
  MODE_PX4_ALTITUDE = 'ALTCTL'
  MODE_PX4_POSITION = 'POSCTL'
  MODE_PX4_OFFBOARD = 'OFFBOARD'
  MODE_PX4_STABILIZED = 'STABILIZED'
  MODE_PX4_RATTITUDE = 'RATTITUDE'
  MODE_PX4_MISSION = 'AUTO.MISSION'
  MODE_PX4_LOITER = 'AUTO.LOITER'
  MODE_PX4_RTL = 'AUTO.RTL'
  MODE_PX4_LAND = 'AUTO.LAND'
  MODE_PX4_RTGS = 'AUTO.RTGS'
  MODE_PX4_READY = 'AUTO.READY'
  MODE_PX4_TAKEOFF = 'AUTO.TAKEOFF'

  __slots__ = ['header','connected','armed','guided','manual_input','mode','system_status']
  _slot_types = ['std_msgs/Header','bool','bool','bool','bool','string','uint8']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,connected,armed,guided,manual_input,mode,system_status

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(State, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.connected is None:
        self.connected = False
      if self.armed is None:
        self.armed = False
      if self.guided is None:
        self.guided = False
      if self.manual_input is None:
        self.manual_input = False
      if self.mode is None:
        self.mode = ''
      if self.system_status is None:
        self.system_status = 0
    else:
      self.header = std_msgs.msg.Header()
      self.connected = False
      self.armed = False
      self.guided = False
      self.manual_input = False
      self.mode = ''
      self.system_status = 0

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_4B().pack(_x.connected, _x.armed, _x.guided, _x.manual_input))
      _x = self.mode
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.system_status
      buff.write(_get_struct_B().pack(_x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 4
      (_x.connected, _x.armed, _x.guided, _x.manual_input,) = _get_struct_4B().unpack(str[start:end])
      self.connected = bool(self.connected)
      self.armed = bool(self.armed)
      self.guided = bool(self.guided)
      self.manual_input = bool(self.manual_input)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.mode = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.mode = str[start:end]
      start = end
      end += 1
      (self.system_status,) = _get_struct_B().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_4B().pack(_x.connected, _x.armed, _x.guided, _x.manual_input))
      _x = self.mode
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.system_status
      buff.write(_get_struct_B().pack(_x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 4
      (_x.connected, _x.armed, _x.guided, _x.manual_input,) = _get_struct_4B().unpack(str[start:end])
      self.connected = bool(self.connected)
      self.armed = bool(self.armed)
      self.guided = bool(self.guided)
      self.manual_input = bool(self.manual_input)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.mode = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.mode = str[start:end]
      start = end
      end += 1
      (self.system_status,) = _get_struct_B().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_3I = None
def _get_struct_3I():
    global _struct_3I
    if _struct_3I is None:
        _struct_3I = struct.Struct("<3I")
    return _struct_3I
_struct_4B = None
def _get_struct_4B():
    global _struct_4B
    if _struct_4B is None:
        _struct_4B = struct.Struct("<4B")
    return _struct_4B
_struct_B = None
def _get_struct_B():
    global _struct_B
    if _struct_B is None:
        _struct_B = struct.Struct("<B")
    return _struct_B

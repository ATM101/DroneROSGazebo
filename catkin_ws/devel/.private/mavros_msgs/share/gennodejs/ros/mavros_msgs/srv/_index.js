
"use strict";

let FileRemove = require('./FileRemove.js')
let ParamPush = require('./ParamPush.js')
let FileRename = require('./FileRename.js')
let CommandTriggerInterval = require('./CommandTriggerInterval.js')
let LogRequestData = require('./LogRequestData.js')
let WaypointClear = require('./WaypointClear.js')
let CommandLong = require('./CommandLong.js')
let WaypointPush = require('./WaypointPush.js')
let WaypointPull = require('./WaypointPull.js')
let CommandBool = require('./CommandBool.js')
let StreamRate = require('./StreamRate.js')
let SetMode = require('./SetMode.js')
let ParamPull = require('./ParamPull.js')
let MessageInterval = require('./MessageInterval.js')
let CommandTOL = require('./CommandTOL.js')
let FileRead = require('./FileRead.js')
let FileClose = require('./FileClose.js')
let CommandTriggerControl = require('./CommandTriggerControl.js')
let ParamGet = require('./ParamGet.js')
let VehicleInfoGet = require('./VehicleInfoGet.js')
let WaypointSetCurrent = require('./WaypointSetCurrent.js')
let LogRequestList = require('./LogRequestList.js')
let FileList = require('./FileList.js')
let FileChecksum = require('./FileChecksum.js')
let FileMakeDir = require('./FileMakeDir.js')
let CommandVtolTransition = require('./CommandVtolTransition.js')
let MountConfigure = require('./MountConfigure.js')
let CommandHome = require('./CommandHome.js')
let FileOpen = require('./FileOpen.js')
let FileTruncate = require('./FileTruncate.js')
let SetMavFrame = require('./SetMavFrame.js')
let LogRequestEnd = require('./LogRequestEnd.js')
let CommandInt = require('./CommandInt.js')
let FileWrite = require('./FileWrite.js')
let FileRemoveDir = require('./FileRemoveDir.js')
let ParamSet = require('./ParamSet.js')

module.exports = {
  FileRemove: FileRemove,
  ParamPush: ParamPush,
  FileRename: FileRename,
  CommandTriggerInterval: CommandTriggerInterval,
  LogRequestData: LogRequestData,
  WaypointClear: WaypointClear,
  CommandLong: CommandLong,
  WaypointPush: WaypointPush,
  WaypointPull: WaypointPull,
  CommandBool: CommandBool,
  StreamRate: StreamRate,
  SetMode: SetMode,
  ParamPull: ParamPull,
  MessageInterval: MessageInterval,
  CommandTOL: CommandTOL,
  FileRead: FileRead,
  FileClose: FileClose,
  CommandTriggerControl: CommandTriggerControl,
  ParamGet: ParamGet,
  VehicleInfoGet: VehicleInfoGet,
  WaypointSetCurrent: WaypointSetCurrent,
  LogRequestList: LogRequestList,
  FileList: FileList,
  FileChecksum: FileChecksum,
  FileMakeDir: FileMakeDir,
  CommandVtolTransition: CommandVtolTransition,
  MountConfigure: MountConfigure,
  CommandHome: CommandHome,
  FileOpen: FileOpen,
  FileTruncate: FileTruncate,
  SetMavFrame: SetMavFrame,
  LogRequestEnd: LogRequestEnd,
  CommandInt: CommandInt,
  FileWrite: FileWrite,
  FileRemoveDir: FileRemoveDir,
  ParamSet: ParamSet,
};

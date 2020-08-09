
# PythonQt.QtCore

The automatic documentation of this module fails, so we’re including the contents of the `help` function instead. 

```
NAME
    PythonQt.QtCore

FILE
    (built-in)

CLASSES
    PythonQt.PythonQtInstanceWrapper(__builtin__.object)
        QAbstractAnimation
        QAbstractItemModel
        QAbstractListModel
        QAbstractProxyModel
        QAbstractState
        QAbstractTransition
        QAnimationGroup
        QApplicationStateChangeEvent
        QBasicMutex
        QBasicTimer
        QBitArray
        QBuffer
        QByteArray
        QByteArrayMatcher
        QChildEvent
        QCollator
        QCollatorSortKey
        QCommandLineOption
        QCommandLineParser
        QCoreApplication
        QCryptographicHash
        QDataStream
        QDate
        QDateTime
        QDeferredDeleteEvent
        QDir
        QDirIterator
        QDynamicPropertyChangeEvent
        QEasingCurve
        QElapsedTimer
        QEvent
        QEventLoop
        QEventTransition
        QFactoryInterface
        QFile
        QFileDevice
        QFileInfo
        QFileSelector
        QFileSystemWatcher
        QFinalState
        QHistoryState
        QIODevice
        QIdentityProxyModel
        QJsonArray
        QJsonDocument
        QJsonObject
        QJsonParseError
        QJsonValue
        QLibrary
        QLibraryInfo
        QLine
        QLineF
        QLocale
        QLockFile
        QMarginsF
        QMessageAuthenticationCode
        QMessageLogContext
        QMessageLogger
        QMetaClassInfo
        QMetaEnum
        QMetaMethod
        QMetaObject
        QMetaProperty
        QMetaType
        QMimeData
        QMimeDatabase
        QMimeType
        QModelIndex
        QMutex
        QParallelAnimationGroup
        QPauseAnimation
        QPersistentModelIndex
        QPoint
        QPointF
        QProcess
        QProcessEnvironment
        QPropertyAnimation
        QReadWriteLock
        QRect
        QRectF
        QRegExp
        QRegularExpression
        QRegularExpressionMatch
        QRegularExpressionMatchIterator
        QResource
        QRunnable
        QSaveFile
        QSemaphore
        QSequentialAnimationGroup
        QSettings
        QSharedMemory
        QSignalBlocker
        QSignalMapper
        QSignalTransition
        QSize
        QSizeF
        QSocketNotifier
        QStandardPaths
        QState
        QStateMachine
        QStorageInfo
        QStringMatcher
        QSysInfo
        QSystemSemaphore
        QTemporaryDir
        QTemporaryFile
        QTextBoundaryFinder
        QTextCodec
        QTextDecoder
        QTextEncoder
        QTextStream
        QThreadPool
        QTime
        QTimeLine
        QTimeZone
        QTimer
        QTimerEvent
        QTranslator
        QUrl
        QUrlQuery
        QUuid
        QVariantAnimation
        QWaitCondition
        QXmlStreamEntityResolver
        Qt
    __builtin__.object
        Property
        Slot
        QtCore.Signal
    
    class Property(__builtin__.object)
     |  Property(type, fget=None, fset=None, freset=None, fdel=None, doc=None,
     |  designable=True, scriptable=True, stored=True, user=False,
     |  constant=False, final=False, notify=None) -> Property
     |  
     |  Methods defined here:
     |  
     |  __call__(...)
     |      x.__call__(...) <==> x(...)
     |  
     |  __init__(...)
     |      x.__init__(...) initializes x; see help(type(x)) for signature
     |  
     |  getter(...)
     |      Sets the fget function.
     |  
     |  read(...)
     |      Sets the fget function.
     |  
     |  setter(...)
     |      Sets the fset function.
     |  
     |  write(...)
     |      Sets the fset function.
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  __new__ = <built-in method __new__ of type object>
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
    
    class QAbstractAnimation(PythonQt.PythonQtInstanceWrapper)
     |  Method resolution order:
     |      QAbstractAnimation
     |      PythonQt.PythonQtInstanceWrapper
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  __init__(...)
     |      x.__init__(...) initializes x; see help(type(x)) for signature
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  Backward = 1
     |  
     |  DeleteWhenStopped = 1
     |  
     |  DeletionPolicy = <class 'PythonQt.QtCore.DeletionPolicy'>
     |  
     |  
     |  Direction = <class 'PythonQt.QtCore.Direction'>
     |  
     |  
     |  Forward = 0
     |  
     |  KeepWhenStopped = 0
     |  
     |  Paused = 1
     |  
     |  Running = 2
     |  
     |  State = <class 'PythonQt.QtCore.State'>
     |  
     |  
     |  Stopped = 0
     |  
     |  blockSignals = <unbound qt slot blockSignals of QAbstractAnimation typ...
     |      X.blockSignals(a, b) -> bool
     |  
     |  childEvent = <unbound qt slot py_q_childEvent of QAbstractAnimation ty...
     |      X.childEvent(a, b)
     |  
     |  children = <unbound qt slot children of QAbstractAnimation type>
     |      X.children(a) -> tuple
     |  
     |  className = <built-in method className of PythonQt.PythonQtClassWrappe...
     |      Return the classname of the object
     |  
     |  connect = <unbound qt slot connect of QAbstractAnimation type>
     |      X.connect(a, b, c, d, e) -> bool
     |  
     |  currentLoop = None
     |  
     |  currentLoopChanged = <unbound qt signal currentLoopChanged of QAbstrac...
     |  
     |  
     |  currentLoopTime = <unbound qt slot currentLoopTime of QAbstractAnimati...
     |      X.currentLoopTime(a) -> int
     |  
     |  currentTime = None
     |  
     |  customEvent = <unbound qt slot py_q_customEvent of QAbstractAnimation ...
     |      X.customEvent(a, b)
     |  
     |  delete = <built-in method delete of PythonQt.PythonQtClassWrapper obje...
     |      Deletes the given C++ object
     |  
     |  deleteLater = <unbound qt slot deleteLater of QAbstractAnimation type>
     |      X.deleteLater()
     |  
     |  destroyed = <unbound qt signal destroyed of QAbstractAnimation type>
     |  
     |  
     |  direction = None
     |  
     |  directionChanged = <unbound qt signal directionChanged of QAbstractAni...
     |  
     |  
     |  disconnect = <unbound qt slot disconnect of QAbstractAnimation type>
     |      X.disconnect(a, b, c, d) -> bool
     |  
     |  dumpObjectInfo = <unbound qt slot dumpObjectInfo of QAbstractAnimation...
     |      X.dumpObjectInfo(a)
     |  
     |  dumpObjectTree = <unbound qt slot dumpObjectTree of QAbstractAnimation...
     |      X.dumpObjectTree(a)
     |  
     |  duration = None
     |  
     |  dynamicPropertyNames = <unbound qt slot dynamicPropertyNames of QAbstr...
     |      X.dynamicPropertyNames(a)
     |  
     |  event = <unbound qt slot py_q_event of QAbstractAnimation type>
     |      X.event(a, b) -> bool
     |  
     |  eventFilter = <unbound qt slot py_q_eventFilter of QAbstractAnimation ...
     |      X.eventFilter(a, b, c) -> bool
     |  
     |  findChild = <unbound qt slot findChild of QAbstractAnimation type>
     |      X.findChild(a, b, c) -> PythonQt.private.QObject
     |  
     |  findChildren = <unbound qt slot findChildren of QAbstractAnimation typ...
     |      X.findChildren(a, b, c) -> tuple
     |  
     |  finished = <unbound qt signal finished of QAbstractAnimation type>
     |  
     |  
     |  group = <unbound qt slot group of QAbstractAnimation type>
     |      X.group(a) -> PythonQt.QtCore.QAnimationGroup
     |  
     |  help = <built-in method help of PythonQt.PythonQtClassWrapper object>
     |      Shows the help of available methods for this class
     |  
     |  inherits = <built-in method inherits of PythonQt.PythonQtClassWrapper ...
     |      Returns if the class inherits or is of given type name
     |  
     |  installEventFilter = <unbound qt slot installEventFilter of QAbstractA...
     |      X.installEventFilter(a, b)
     |  
     |  isSignalConnected = <unbound qt slot isSignalConnected of QAbstractAni...
     |      X.isSignalConnected(a, b) -> bool
     |  
     |  isWidgetType = <unbound qt slot isWidgetType of QAbstractAnimation typ...
     |      X.isWidgetType(a) -> bool
     |  
     |  isWindowType = <unbound qt slot isWindowType of QAbstractAnimation typ...
     |      X.isWindowType(a) -> bool
     |  
     |  killTimer = <unbound qt slot killTimer of QAbstractAnimation type>
     |      X.killTimer(a, b)
     |  
     |  loopCount = None
     |  
     |  metaObject = <unbound qt slot metaObject of QAbstractAnimation type>
     |      X.metaObject(a) -> PythonQt.QtCore.QMetaObject
     |  
     |  moveToThread = <unbound qt slot moveToThread of QAbstractAnimation typ...
     |      X.moveToThread(a, b)
     |  
     |  objectName = None
     |  
     |  objectNameChanged = <unbound qt signal objectNameChanged of QAbstractA...
     |  
     |  
     |  parent = <unbound qt slot parent of QAbstractAnimation type>
     |      X.parent(a) -> PythonQt.private.QObject
     |  
     |  pause = <unbound qt slot pause of QAbstractAnimation type>
     |      X.pause()
     |  
     |  property = <unbound qt slot property of QAbstractAnimation type>
     |      X.property(a, b) -> object
     |  
     |  removeEventFilter = <unbound qt slot removeEventFilter of QAbstractAni...
     |      X.removeEventFilter(a, b)
     |  
     |  resume = <unbound qt slot resume of QAbstractAnimation type>
     |      X.resume()
     |  
     |  sender = <unbound qt slot sender of QAbstractAnimation type>
     |      X.sender(a) -> PythonQt.private.QObject
     |  
     |  senderSignalIndex = <unbound qt slot senderSignalIndex of QAbstractAni...
     |      X.senderSignalIndex(a) -> int
     |  
     |  setCurrentTime = <unbound qt slot setCurrentTime of QAbstractAnimation...
     |      X.setCurrentTime(a)
     |  
     |  setDirection = <unbound qt slot setDirection of QAbstractAnimation typ...
     |      X.setDirection(a, b)
     |  
     |  setLoopCount = <unbound qt slot setLoopCount of QAbstractAnimation typ...
     |      X.setLoopCount(a, b)
     |  
     |  setObjectName = <unbound qt slot setObjectName of QAbstractAnimation t...
     |      X.setObjectName(a, b)
     |  
     |  setParent = <unbound qt slot setParent of QAbstractAnimation type>
     |      X.setParent(a, b)
     |  
     |  setPaused = <unbound qt slot setPaused of QAbstractAnimation type>
     |      X.setPaused(a)
     |  
     |  setProperty = <unbound qt slot setProperty of QAbstractAnimation type>
     |      X.setProperty(a, b, c) -> bool
     |  
     |  signalsBlocked = <unbound qt slot signalsBlocked of QAbstractAnimation...
     |      X.signalsBlocked(a) -> bool
     |  
     |  start = <unbound qt slot start of QAbstractAnimation type>
     |      X.start(a)
     |  
     |  startTimer = <unbound qt slot startTimer of QAbstractAnimation type>
     |      X.startTimer(a, b, c) -> int
     |  
     |  state = None
     |  
     |  stateChanged = <unbound qt signal stateChanged of QAbstractAnimation t...
     |  
     |  
     |  stop = <unbound qt slot stop of QAbstractAnimation type>
     |      X.stop()
     |  
     |  thread = <unbound qt slot thread of QAbstractAnimation type>
     |      X.thread(a)
     |  
     |  timerEvent = <unbound qt slot py_q_timerEvent of QAbstractAnimation ty...
     |      X.timerEvent(a, b)
     |  
     |  totalDuration = <unbound qt slot totalDuration of QAbstractAnimation t...
     |      X.totalDuration(a) -> int
     |  
     |  tr = <unbound qt slot tr of QAbstractAnimation type>
     |      X.tr(a, b, c, d) -> str
     |  
     |  updateCurrentTime = <unbound qt slot py_q_updateCurrentTime of QAbstra...
     |      X.updateCurrentTime(a, b)
     |  
     |  updateDirection = <unbound qt slot py_q_updateDirection of QAbstractAn...
     |      X.updateDirection(a, b)
     |  
     |  updateState = <unbound qt slot py_q_updateState of QAbstractAnimation ...
     |      X.updateState(a, b, c)
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __delattr__(...)
     |      x.__delattr__('name') <==> del x.name
     |  
     |  __eq__(...)
     |      x.__eq__(y) <==> x==y
     |  
     |  __ge__(...)
     |      x.__ge__(y) <==> x>=y
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __gt__(...)
     |      x.__gt__(y) <==> x>y
     |  
     |  __hash__(...)
     |      x.__hash__() <==> hash(x)
     |  
     |  __le__(...)
     |      x.__le__(y) <==> x<=y
     |  
     |  __lt__(...)
     |      x.__lt__(y) <==> x<y
     |  
     |  __ne__(...)
     |      x.__ne__(y) <==> x!=y
     |  
     |  __nonzero__(...)
     |      x.__nonzero__() <==> x != 0
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __setattr__(...)
     |      x.__setattr__('name', value) <==> x.name = value
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __new__ = <built-in method __new__ of PythonQt.PythonQtClassWrapper ob...
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
    
    class QAbstractItemModel(PythonQt.PythonQtInstanceWrapper)
     |  Method resolution order:
     |      QAbstractItemModel
     |      PythonQt.PythonQtInstanceWrapper
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  __init__(...)
     |      x.__init__(...) initializes x; see help(type(x)) for signature
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  HorizontalSortHint = 2
     |  
     |  LayoutChangeHint = <class 'PythonQt.QtCore.LayoutChangeHint'>
     |  
     |  
     |  NoLayoutChangeHint = 0
     |  
     |  VerticalSortHint = 1
     |  
     |  beginInsertColumns = <unbound qt slot beginInsertColumns of QAbstractI...
     |      X.beginInsertColumns(a, b, c, d)
     |  
     |  beginInsertRows = <unbound qt slot beginInsertRows of QAbstractItemMod...
     |      X.beginInsertRows(a, b, c, d)
     |  
     |  beginMoveColumns = <unbound qt slot beginMoveColumns of QAbstractItemM...
     |      X.beginMoveColumns(a, b, c, d, e, f) -> bool
     |  
     |  beginMoveRows = <unbound qt slot beginMoveRows of QAbstractItemModel t...
     |      X.beginMoveRows(a, b, c, d, e, f) -> bool
     |  
     |  beginRemoveColumns = <unbound qt slot beginRemoveColumns of QAbstractI...
     |      X.beginRemoveColumns(a, b, c, d)
     |  
     |  beginRemoveRows = <unbound qt slot beginRemoveRows of QAbstractItemMod...
     |      X.beginRemoveRows(a, b, c, d)
     |  
     |  beginResetModel = <unbound qt slot beginResetModel of QAbstractItemMod...
     |      X.beginResetModel(a)
     |  
     |  blockSignals = <unbound qt slot blockSignals of QAbstractItemModel typ...
     |      X.blockSignals(a, b) -> bool
     |  
     |  buddy = <unbound qt slot py_q_buddy of QAbstractItemModel type>
     |      X.buddy(a, b) -> PythonQt.QtCore.QModelIndex
     |  
     |  canDropMimeData = <unbound qt slot py_q_canDropMimeData of QAbstractIt...
     |      X.canDropMimeData(a, b, c, d, e, f) -> bool
     |  
     |  canFetchMore = <unbound qt slot py_q_canFetchMore of QAbstractItemMode...
     |      X.canFetchMore(a, b) -> bool
     |  
     |  changePersistentIndex = <unbound qt slot changePersistentIndex of QAbs...
     |      X.changePersistentIndex(a, b, c)
     |  
     |  changePersistentIndexList = <unbound qt slot changePersistentIndexList...
     |      X.changePersistentIndexList(a, b, c)
     |  
     |  childEvent = <unbound qt slot py_q_childEvent of QAbstractItemModel ty...
     |      X.childEvent(a, b)
     |  
     |  children = <unbound qt slot children of QAbstractItemModel type>
     |      X.children(a) -> tuple
     |  
     |  className = <built-in method className of PythonQt.PythonQtClassWrappe...
     |      Return the classname of the object
     |  
     |  columnCount = <unbound qt slot py_q_columnCount of QAbstractItemModel ...
     |      X.columnCount(a, b) -> int
     |  
     |  columnsAboutToBeInserted = <unbound qt signal columnsAboutToBeInserted...
     |  
     |  
     |  columnsAboutToBeMoved = <unbound qt signal columnsAboutToBeMoved of QA...
     |  
     |  
     |  columnsAboutToBeRemoved = <unbound qt signal columnsAboutToBeRemoved o...
     |  
     |  
     |  columnsInserted = <unbound qt signal columnsInserted of QAbstractItemM...
     |  
     |  
     |  columnsMoved = <unbound qt signal columnsMoved of QAbstractItemModel t...
     |  
     |  
     |  columnsRemoved = <unbound qt signal columnsRemoved of QAbstractItemMod...
     |  
     |  
     |  connect = <unbound qt slot connect of QAbstractItemModel type>
     |      X.connect(a, b, c, d, e) -> bool
     |  
     |  createIndex = <unbound qt slot createIndex of QAbstractItemModel type>
     |      X.createIndex(a, b, c, d) -> PythonQt.QtCore.QModelIndex
     |  
     |  customEvent = <unbound qt slot py_q_customEvent of QAbstractItemModel ...
     |      X.customEvent(a, b)
     |  
     |  data = <unbound qt slot py_q_data of QAbstractItemModel type>
     |      X.data(a, b, c) -> object
     |  
     |  dataChanged = <unbound qt signal dataChanged of QAbstractItemModel typ...
     |  
     |  
     |  decodeData = <unbound qt slot decodeData of QAbstractItemModel type>
     |      X.decodeData(a, b, c, d, e) -> bool
     |  
     |  delete = <built-in method delete of PythonQt.PythonQtClassWrapper obje...
     |      Deletes the given C++ object
     |  
     |  deleteLater = <unbound qt slot deleteLater of QAbstractItemModel type>
     |      X.deleteLater()
     |  
     |  destroyed = <unbound qt signal destroyed of QAbstractItemModel type>
     |  
     |  
     |  disconnect = <unbound qt slot disconnect of QAbstractItemModel type>
     |      X.disconnect(a, b, c, d) -> bool
     |  
     |  dropMimeData = <unbound qt slot py_q_dropMimeData of QAbstractItemMode...
     |      X.dropMimeData(a, b, c, d, e, f) -> bool
     |  
     |  dumpObjectInfo = <unbound qt slot dumpObjectInfo of QAbstractItemModel...
     |      X.dumpObjectInfo(a)
     |  
     |  dumpObjectTree = <unbound qt slot dumpObjectTree of QAbstractItemModel...
     |      X.dumpObjectTree(a)
     |  
     |  dynamicPropertyNames = <unbound qt slot dynamicPropertyNames of QAbstr...
     |      X.dynamicPropertyNames(a)
     |  
     |  encodeData = <unbound qt slot encodeData of QAbstractItemModel type>
     |      X.encodeData(a, b, c)
     |  
     |  endInsertColumns = <unbound qt slot endInsertColumns of QAbstractItemM...
     |      X.endInsertColumns(a)
     |  
     |  endInsertRows = <unbound qt slot endInsertRows of QAbstractItemModel t...
     |      X.endInsertRows(a)
     |  
     |  endMoveColumns = <unbound qt slot endMoveColumns of QAbstractItemModel...
     |      X.endMoveColumns(a)
     |  
     |  endMoveRows = <unbound qt slot endMoveRows of QAbstractItemModel type>
     |      X.endMoveRows(a)
     |  
     |  endRemoveColumns = <unbound qt slot endRemoveColumns of QAbstractItemM...
     |      X.endRemoveColumns(a)
     |  
     |  endRemoveRows = <unbound qt slot endRemoveRows of QAbstractItemModel t...
     |      X.endRemoveRows(a)
     |  
     |  endResetModel = <unbound qt slot endResetModel of QAbstractItemModel t...
     |      X.endResetModel(a)
     |  
     |  event = <unbound qt slot py_q_event of QAbstractItemModel type>
     |      X.event(a, b) -> bool
     |  
     |  eventFilter = <unbound qt slot py_q_eventFilter of QAbstractItemModel ...
     |      X.eventFilter(a, b, c) -> bool
     |  
     |  fetchMore = <unbound qt slot py_q_fetchMore of QAbstractItemModel type...
     |      X.fetchMore(a, b)
     |  
     |  findChild = <unbound qt slot findChild of QAbstractItemModel type>
     |      X.findChild(a, b, c) -> PythonQt.private.QObject
     |  
     |  findChildren = <unbound qt slot findChildren of QAbstractItemModel typ...
     |      X.findChildren(a, b, c) -> tuple
     |  
     |  flags = <unbound qt slot py_q_flags of QAbstractItemModel type>
     |      X.flags(a, b)
     |  
     |  hasChildren = <unbound qt slot py_q_hasChildren of QAbstractItemModel ...
     |      X.hasChildren(a, b) -> bool
     |  
     |  hasIndex = <unbound qt slot hasIndex of QAbstractItemModel type>
     |      X.hasIndex(a, b, c, d) -> bool
     |  
     |  headerData = <unbound qt slot py_q_headerData of QAbstractItemModel ty...
     |      X.headerData(a, b, c, d) -> object
     |  
     |  headerDataChanged = <unbound qt signal headerDataChanged of QAbstractI...
     |  
     |  
     |  help = <built-in method help of PythonQt.PythonQtClassWrapper object>
     |      Shows the help of available methods for this class
     |  
     |  index = <unbound qt slot py_q_index of QAbstractItemModel type>
     |      X.index(a, b, c, d) -> PythonQt.QtCore.QModelIndex
     |  
     |  inherits = <built-in method inherits of PythonQt.PythonQtClassWrapper ...
     |      Returns if the class inherits or is of given type name
     |  
     |  insertColumn = <unbound qt slot insertColumn of QAbstractItemModel typ...
     |      X.insertColumn(a, b, c) -> bool
     |  
     |  insertColumns = <unbound qt slot py_q_insertColumns of QAbstractItemMo...
     |      X.insertColumns(a, b, c, d) -> bool
     |  
     |  insertRow = <unbound qt slot insertRow of QAbstractItemModel type>
     |      X.insertRow(a, b, c) -> bool
     |  
     |  insertRows = <unbound qt slot py_q_insertRows of QAbstractItemModel ty...
     |      X.insertRows(a, b, c, d) -> bool
     |  
     |  installEventFilter = <unbound qt slot installEventFilter of QAbstractI...
     |      X.installEventFilter(a, b)
     |  
     |  isSignalConnected = <unbound qt slot isSignalConnected of QAbstractIte...
     |      X.isSignalConnected(a, b) -> bool
     |  
     |  isWidgetType = <unbound qt slot isWidgetType of QAbstractItemModel typ...
     |      X.isWidgetType(a) -> bool
     |  
     |  isWindowType = <unbound qt slot isWindowType of QAbstractItemModel typ...
     |      X.isWindowType(a) -> bool
     |  
     |  itemData = <unbound qt slot py_q_itemData of QAbstractItemModel type>
     |      X.itemData(a, b) -> dict
     |  
     |  killTimer = <unbound qt slot killTimer of QAbstractItemModel type>
     |      X.killTimer(a, b)
     |  
     |  layoutAboutToBeChanged = <unbound qt signal layoutAboutToBeChanged of ...
     |  
     |  
     |  layoutChanged = <unbound qt signal layoutChanged of QAbstractItemModel...
     |  
     |  
     |  match = <unbound qt slot py_q_match of QAbstractItemModel type>
     |      X.match(a, b, c, d, e, f) -> tuple
     |  
     |  metaObject = <unbound qt slot metaObject of QAbstractItemModel type>
     |      X.metaObject(a) -> PythonQt.QtCore.QMetaObject
     |  
     |  mimeData = <unbound qt slot py_q_mimeData of QAbstractItemModel type>
     |      X.mimeData(a, b) -> PythonQt.QtCore.QMimeData
     |  
     |  mimeTypes = <unbound qt slot py_q_mimeTypes of QAbstractItemModel type...
     |      X.mimeTypes(a) -> tuple
     |  
     |  modelAboutToBeReset = <unbound qt signal modelAboutToBeReset of QAbstr...
     |  
     |  
     |  modelReset = <unbound qt signal modelReset of QAbstractItemModel type>
     |  
     |  
     |  moveColumn = <unbound qt slot moveColumn of QAbstractItemModel type>
     |      X.moveColumn(a, b, c, d, e) -> bool
     |  
     |  moveColumns = <unbound qt slot py_q_moveColumns of QAbstractItemModel ...
     |      X.moveColumns(a, b, c, d, e, f) -> bool
     |  
     |  moveRow = <unbound qt slot moveRow of QAbstractItemModel type>
     |      X.moveRow(a, b, c, d, e) -> bool
     |  
     |  moveRows = <unbound qt slot py_q_moveRows of QAbstractItemModel type>
     |      X.moveRows(a, b, c, d, e, f) -> bool
     |  
     |  moveToThread = <unbound qt slot moveToThread of QAbstractItemModel typ...
     |      X.moveToThread(a, b)
     |  
     |  objectName = None
     |  
     |  objectNameChanged = <unbound qt signal objectNameChanged of QAbstractI...
     |  
     |  
     |  parent = <unbound qt slot py_q_parent of QAbstractItemModel type>
     |      X.parent(a, b) -> PythonQt.QtCore.QModelIndex
     |  
     |  persistentIndexList = <unbound qt slot persistentIndexList of QAbstrac...
     |      X.persistentIndexList(a) -> tuple
     |  
     |  property = <unbound qt slot property of QAbstractItemModel type>
     |      X.property(a, b) -> object
     |  
     |  removeColumn = <unbound qt slot removeColumn of QAbstractItemModel typ...
     |      X.removeColumn(a, b, c) -> bool
     |  
     |  removeColumns = <unbound qt slot py_q_removeColumns of QAbstractItemMo...
     |      X.removeColumns(a, b, c, d) -> bool
     |  
     |  removeEventFilter = <unbound qt slot removeEventFilter of QAbstractIte...
     |      X.removeEventFilter(a, b)
     |  
     |  removeRow = <unbound qt slot removeRow of QAbstractItemModel type>
     |      X.removeRow(a, b, c) -> bool
     |  
     |  removeRows = <unbound qt slot py_q_removeRows of QAbstractItemModel ty...
     |      X.removeRows(a, b, c, d) -> bool
     |  
     |  revert = <unbound qt slot py_q_revert of QAbstractItemModel type>
     |      X.revert(a)
     |  
     |  roleNames = <unbound qt slot py_q_roleNames of QAbstractItemModel type...
     |      X.roleNames(a) -> dict
     |  
     |  rowCount = <unbound qt slot py_q_rowCount of QAbstractItemModel type>
     |      X.rowCount(a, b) -> int
     |  
     |  rowsAboutToBeInserted = <unbound qt signal rowsAboutToBeInserted of QA...
     |  
     |  
     |  rowsAboutToBeMoved = <unbound qt signal rowsAboutToBeMoved of QAbstrac...
     |  
     |  
     |  rowsAboutToBeRemoved = <unbound qt signal rowsAboutToBeRemoved of QAbs...
     |  
     |  
     |  rowsInserted = <unbound qt signal rowsInserted of QAbstractItemModel t...
     |  
     |  
     |  rowsMoved = <unbound qt signal rowsMoved of QAbstractItemModel type>
     |  
     |  
     |  rowsRemoved = <unbound qt signal rowsRemoved of QAbstractItemModel typ...
     |  
     |  
     |  sender = <unbound qt slot sender of QAbstractItemModel type>
     |      X.sender(a) -> PythonQt.private.QObject
     |  
     |  senderSignalIndex = <unbound qt slot senderSignalIndex of QAbstractIte...
     |      X.senderSignalIndex(a) -> int
     |  
     |  setData = <unbound qt slot py_q_setData of QAbstractItemModel type>
     |      X.setData(a, b, c, d) -> bool
     |  
     |  setHeaderData = <unbound qt slot py_q_setHeaderData of QAbstractItemMo...
     |      X.setHeaderData(a, b, c, d, e) -> bool
     |  
     |  setItemData = <unbound qt slot py_q_setItemData of QAbstractItemModel ...
     |      X.setItemData(a, b, c) -> bool
     |  
     |  setObjectName = <unbound qt slot setObjectName of QAbstractItemModel t...
     |      X.setObjectName(a, b)
     |  
     |  setParent = <unbound qt slot setParent of QAbstractItemModel type>
     |      X.setParent(a, b)
     |  
     |  setProperty = <unbound qt slot setProperty of QAbstractItemModel type>
     |      X.setProperty(a, b, c) -> bool
     |  
     |  sibling = <unbound qt slot py_q_sibling of QAbstractItemModel type>
     |      X.sibling(a, b, c, d) -> PythonQt.QtCore.QModelIndex
     |  
     |  signalsBlocked = <unbound qt slot signalsBlocked of QAbstractItemModel...
     |      X.signalsBlocked(a) -> bool
     |  
     |  sort = <unbound qt slot py_q_sort of QAbstractItemModel type>
     |      X.sort(a, b, c)
     |  
     |  span = <unbound qt slot py_q_span of QAbstractItemModel type>
     |      X.span(a, b) -> PythonQt.QtCore.QSize
     |  
     |  startTimer = <unbound qt slot startTimer of QAbstractItemModel type>
     |      X.startTimer(a, b, c) -> int
     |  
     |  submit = <unbound qt slot py_q_submit of QAbstractItemModel type>
     |      X.submit(a) -> bool
     |  
     |  supportedDragActions = <unbound qt slot py_q_supportedDragActions of Q...
     |      X.supportedDragActions(a)
     |  
     |  supportedDropActions = <unbound qt slot py_q_supportedDropActions of Q...
     |      X.supportedDropActions(a)
     |  
     |  thread = <unbound qt slot thread of QAbstractItemModel type>
     |      X.thread(a)
     |  
     |  timerEvent = <unbound qt slot py_q_timerEvent of QAbstractItemModel ty...
     |      X.timerEvent(a, b)
     |  
     |  tr = <unbound qt slot tr of QAbstractItemModel type>
     |      X.tr(a, b, c, d) -> str
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __delattr__(...)
     |      x.__delattr__('name') <==> del x.name
     |  
     |  __eq__(...)
     |      x.__eq__(y) <==> x==y
     |  
     |  __ge__(...)
     |      x.__ge__(y) <==> x>=y
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __gt__(...)
     |      x.__gt__(y) <==> x>y
     |  
     |  __hash__(...)
     |      x.__hash__() <==> hash(x)
     |  
     |  __le__(...)
     |      x.__le__(y) <==> x<=y
     |  
     |  __lt__(...)
     |      x.__lt__(y) <==> x<y
     |  
     |  __ne__(...)
     |      x.__ne__(y) <==> x!=y
     |  
     |  __nonzero__(...)
     |      x.__nonzero__() <==> x != 0
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __setattr__(...)
     |      x.__setattr__('name', value) <==> x.name = value
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __new__ = <built-in method __new__ of PythonQt.PythonQtClassWrapper ob...
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
    
    class QAbstractListModel(PythonQt.PythonQtInstanceWrapper)
     |  Method resolution order:
     |      QAbstractListModel
     |      PythonQt.PythonQtInstanceWrapper
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  __init__(...)
     |      x.__init__(...) initializes x; see help(type(x)) for signature
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  HorizontalSortHint = 2
     |  
     |  LayoutChangeHint = <class 'PythonQt.QtCore.LayoutChangeHint'>
     |  
     |  
     |  NoLayoutChangeHint = 0
     |  
     |  VerticalSortHint = 1
     |  
     |  beginInsertColumns = <unbound qt slot beginInsertColumns of QAbstractL...
     |      X.beginInsertColumns(a, b, c, d)
     |  
     |  beginInsertRows = <unbound qt slot beginInsertRows of QAbstractListMod...
     |      X.beginInsertRows(a, b, c, d)
     |  
     |  beginMoveColumns = <unbound qt slot beginMoveColumns of QAbstractListM...
     |      X.beginMoveColumns(a, b, c, d, e, f) -> bool
     |  
     |  beginMoveRows = <unbound qt slot beginMoveRows of QAbstractListModel t...
     |      X.beginMoveRows(a, b, c, d, e, f) -> bool
     |  
     |  beginRemoveColumns = <unbound qt slot beginRemoveColumns of QAbstractL...
     |      X.beginRemoveColumns(a, b, c, d)
     |  
     |  beginRemoveRows = <unbound qt slot beginRemoveRows of QAbstractListMod...
     |      X.beginRemoveRows(a, b, c, d)
     |  
     |  beginResetModel = <unbound qt slot beginResetModel of QAbstractListMod...
     |      X.beginResetModel(a)
     |  
     |  blockSignals = <unbound qt slot blockSignals of QAbstractListModel typ...
     |      X.blockSignals(a, b) -> bool
     |  
     |  buddy = <unbound qt slot py_q_buddy of QAbstractListModel type>
     |      X.buddy(a, b) -> PythonQt.QtCore.QModelIndex
     |  
     |  canDropMimeData = <unbound qt slot py_q_canDropMimeData of QAbstractLi...
     |      X.canDropMimeData(a, b, c, d, e, f) -> bool
     |  
     |  canFetchMore = <unbound qt slot py_q_canFetchMore of QAbstractListMode...
     |      X.canFetchMore(a, b) -> bool
     |  
     |  changePersistentIndex = <unbound qt slot changePersistentIndex of QAbs...
     |      X.changePersistentIndex(a, b, c)
     |  
     |  changePersistentIndexList = <unbound qt slot changePersistentIndexList...
     |      X.changePersistentIndexList(a, b, c)
     |  
     |  childEvent = <unbound qt slot py_q_childEvent of QAbstractListModel ty...
     |      X.childEvent(a, b)
     |  
     |  children = <unbound qt slot children of QAbstractListModel type>
     |      X.children(a) -> tuple
     |  
     |  className = <built-in method className of PythonQt.PythonQtClassWrappe...
     |      Return the classname of the object
     |  
     |  columnCount = <unbound qt slot py_q_columnCount of QAbstractListModel ...
     |      X.columnCount(a, b) -> int
     |  
     |  columnsAboutToBeInserted = <unbound qt signal columnsAboutToBeInserted...
     |  
     |  
     |  columnsAboutToBeMoved = <unbound qt signal columnsAboutToBeMoved of QA...
     |  
     |  
     |  columnsAboutToBeRemoved = <unbound qt signal columnsAboutToBeRemoved o...
     |  
     |  
     |  columnsInserted = <unbound qt signal columnsInserted of QAbstractListM...
     |  
     |  
     |  columnsMoved = <unbound qt signal columnsMoved of QAbstractListModel t...
     |  
     |  
     |  columnsRemoved = <unbound qt signal columnsRemoved of QAbstractListMod...
     |  
     |  
     |  connect = <unbound qt slot connect of QAbstractListModel type>
     |      X.connect(a, b, c, d, e) -> bool
     |  
     |  createIndex = <unbound qt slot createIndex of QAbstractListModel type>
     |      X.createIndex(a, b, c, d) -> PythonQt.QtCore.QModelIndex
     |  
     |  customEvent = <unbound qt slot py_q_customEvent of QAbstractListModel ...
     |      X.customEvent(a, b)
     |  
     |  data = <unbound qt slot py_q_data of QAbstractListModel type>
     |      X.data(a, b, c) -> object
     |  
     |  dataChanged = <unbound qt signal dataChanged of QAbstractListModel typ...
     |  
     |  
     |  decodeData = <unbound qt slot decodeData of QAbstractListModel type>
     |      X.decodeData(a, b, c, d, e) -> bool
     |  
     |  delete = <built-in method delete of PythonQt.PythonQtClassWrapper obje...
     |      Deletes the given C++ object
     |  
     |  deleteLater = <unbound qt slot deleteLater of QAbstractListModel type>
     |      X.deleteLater()
     |  
     |  destroyed = <unbound qt signal destroyed of QAbstractListModel type>
     |  
     |  
     |  disconnect = <unbound qt slot disconnect of QAbstractListModel type>
     |      X.disconnect(a, b, c, d) -> bool
     |  
     |  dropMimeData = <unbound qt slot py_q_dropMimeData of QAbstractListMode...
     |      X.dropMimeData(a, b, c, d, e, f) -> bool
     |  
     |  dumpObjectInfo = <unbound qt slot dumpObjectInfo of QAbstractListModel...
     |      X.dumpObjectInfo(a)
     |  
     |  dumpObjectTree = <unbound qt slot dumpObjectTree of QAbstractListModel...
     |      X.dumpObjectTree(a)
     |  
     |  dynamicPropertyNames = <unbound qt slot dynamicPropertyNames of QAbstr...
     |      X.dynamicPropertyNames(a)
     |  
     |  encodeData = <unbound qt slot encodeData of QAbstractListModel type>
     |      X.encodeData(a, b, c)
     |  
     |  endInsertColumns = <unbound qt slot endInsertColumns of QAbstractListM...
     |      X.endInsertColumns(a)
     |  
     |  endInsertRows = <unbound qt slot endInsertRows of QAbstractListModel t...
     |      X.endInsertRows(a)
     |  
     |  endMoveColumns = <unbound qt slot endMoveColumns of QAbstractListModel...
     |      X.endMoveColumns(a)
     |  
     |  endMoveRows = <unbound qt slot endMoveRows of QAbstractListModel type>
     |      X.endMoveRows(a)
     |  
     |  endRemoveColumns = <unbound qt slot endRemoveColumns of QAbstractListM...
     |      X.endRemoveColumns(a)
     |  
     |  endRemoveRows = <unbound qt slot endRemoveRows of QAbstractListModel t...
     |      X.endRemoveRows(a)
     |  
     |  endResetModel = <unbound qt slot endResetModel of QAbstractListModel t...
     |      X.endResetModel(a)
     |  
     |  event = <unbound qt slot py_q_event of QAbstractListModel type>
     |      X.event(a, b) -> bool
     |  
     |  eventFilter = <unbound qt slot py_q_eventFilter of QAbstractListModel ...
     |      X.eventFilter(a, b, c) -> bool
     |  
     |  fetchMore = <unbound qt slot py_q_fetchMore of QAbstractListModel type...
     |      X.fetchMore(a, b)
     |  
     |  findChild = <unbound qt slot findChild of QAbstractListModel type>
     |      X.findChild(a, b, c) -> PythonQt.private.QObject
     |  
     |  findChildren = <unbound qt slot findChildren of QAbstractListModel typ...
     |      X.findChildren(a, b, c) -> tuple
     |  
     |  flags = <unbound qt slot py_q_flags of QAbstractListModel type>
     |      X.flags(a, b)
     |  
     |  hasChildren = <unbound qt slot py_q_hasChildren of QAbstractListModel ...
     |      X.hasChildren(a, b) -> bool
     |  
     |  hasIndex = <unbound qt slot hasIndex of QAbstractListModel type>
     |      X.hasIndex(a, b, c, d) -> bool
     |  
     |  headerData = <unbound qt slot py_q_headerData of QAbstractListModel ty...
     |      X.headerData(a, b, c, d) -> object
     |  
     |  headerDataChanged = <unbound qt signal headerDataChanged of QAbstractL...
     |  
     |  
     |  help = <built-in method help of PythonQt.PythonQtClassWrapper object>
     |      Shows the help of available methods for this class
     |  
     |  index = <unbound qt slot py_q_index of QAbstractListModel type>
     |      X.index(a, b, c, d) -> PythonQt.QtCore.QModelIndex
     |  
     |  inherits = <built-in method inherits of PythonQt.PythonQtClassWrapper ...
     |      Returns if the class inherits or is of given type name
     |  
     |  insertColumn = <unbound qt slot insertColumn of QAbstractListModel typ...
     |      X.insertColumn(a, b, c) -> bool
     |  
     |  insertColumns = <unbound qt slot py_q_insertColumns of QAbstractListMo...
     |      X.insertColumns(a, b, c, d) -> bool
     |  
     |  insertRow = <unbound qt slot insertRow of QAbstractListModel type>
     |      X.insertRow(a, b, c) -> bool
     |  
     |  insertRows = <unbound qt slot py_q_insertRows of QAbstractListModel ty...
     |      X.insertRows(a, b, c, d) -> bool
     |  
     |  installEventFilter = <unbound qt slot installEventFilter of QAbstractL...
     |      X.installEventFilter(a, b)
     |  
     |  isSignalConnected = <unbound qt slot isSignalConnected of QAbstractLis...
     |      X.isSignalConnected(a, b) -> bool
     |  
     |  isWidgetType = <unbound qt slot isWidgetType of QAbstractListModel typ...
     |      X.isWidgetType(a) -> bool
     |  
     |  isWindowType = <unbound qt slot isWindowType of QAbstractListModel typ...
     |      X.isWindowType(a) -> bool
     |  
     |  itemData = <unbound qt slot py_q_itemData of QAbstractListModel type>
     |      X.itemData(a, b) -> dict
     |  
     |  killTimer = <unbound qt slot killTimer of QAbstractListModel type>
     |      X.killTimer(a, b)
     |  
     |  layoutAboutToBeChanged = <unbound qt signal layoutAboutToBeChanged of ...
     |  
     |  
     |  layoutChanged = <unbound qt signal layoutChanged of QAbstractListModel...
     |  
     |  
     |  match = <unbound qt slot py_q_match of QAbstractListModel type>
     |      X.match(a, b, c, d, e, f) -> tuple
     |  
     |  metaObject = <unbound qt slot metaObject of QAbstractListModel type>
     |      X.metaObject(a) -> PythonQt.QtCore.QMetaObject
     |  
     |  mimeData = <unbound qt slot py_q_mimeData of QAbstractListModel type>
     |      X.mimeData(a, b) -> PythonQt.QtCore.QMimeData
     |  
     |  mimeTypes = <unbound qt slot py_q_mimeTypes of QAbstractListModel type...
     |      X.mimeTypes(a) -> tuple
     |  
     |  modelAboutToBeReset = <unbound qt signal modelAboutToBeReset of QAbstr...
     |  
     |  
     |  modelReset = <unbound qt signal modelReset of QAbstractListModel type>
     |  
     |  
     |  moveColumn = <unbound qt slot moveColumn of QAbstractListModel type>
     |      X.moveColumn(a, b, c, d, e) -> bool
     |  
     |  moveColumns = <unbound qt slot py_q_moveColumns of QAbstractListModel ...
     |      X.moveColumns(a, b, c, d, e, f) -> bool
     |  
     |  moveRow = <unbound qt slot moveRow of QAbstractListModel type>
     |      X.moveRow(a, b, c, d, e) -> bool
     |  
     |  moveRows = <unbound qt slot py_q_moveRows of QAbstractListModel type>
     |      X.moveRows(a, b, c, d, e, f) -> bool
     |  
     |  moveToThread = <unbound qt slot moveToThread of QAbstractListModel typ...
     |      X.moveToThread(a, b)
     |  
     |  objectName = None
     |  
     |  objectNameChanged = <unbound qt signal objectNameChanged of QAbstractL...
     |  
     |  
     |  parent = <unbound qt slot py_q_parent of QAbstractListModel type>
     |      X.parent(a, b) -> PythonQt.QtCore.QModelIndex
     |  
     |  persistentIndexList = <unbound qt slot persistentIndexList of QAbstrac...
     |      X.persistentIndexList(a) -> tuple
     |  
     |  property = <unbound qt slot property of QAbstractListModel type>
     |      X.property(a, b) -> object
     |  
     |  removeColumn = <unbound qt slot removeColumn of QAbstractListModel typ...
     |      X.removeColumn(a, b, c) -> bool
     |  
     |  removeColumns = <unbound qt slot py_q_removeColumns of QAbstractListMo...
     |      X.removeColumns(a, b, c, d) -> bool
     |  
     |  removeEventFilter = <unbound qt slot removeEventFilter of QAbstractLis...
     |      X.removeEventFilter(a, b)
     |  
     |  removeRow = <unbound qt slot removeRow of QAbstractListModel type>
     |      X.removeRow(a, b, c) -> bool
     |  
     |  removeRows = <unbound qt slot py_q_removeRows of QAbstractListModel ty...
     |      X.removeRows(a, b, c, d) -> bool
     |  
     |  revert = <unbound qt slot py_q_revert of QAbstractListModel type>
     |      X.revert(a)
     |  
     |  roleNames = <unbound qt slot py_q_roleNames of QAbstractListModel type...
     |      X.roleNames(a) -> dict
     |  
     |  rowCount = <unbound qt slot py_q_rowCount of QAbstractListModel type>
     |      X.rowCount(a, b) -> int
     |  
     |  rowsAboutToBeInserted = <unbound qt signal rowsAboutToBeInserted of QA...
     |  
     |  
     |  rowsAboutToBeMoved = <unbound qt signal rowsAboutToBeMoved of QAbstrac...
     |  
     |  
     |  rowsAboutToBeRemoved = <unbound qt signal rowsAboutToBeRemoved of QAbs...
     |  
     |  
     |  rowsInserted = <unbound qt signal rowsInserted of QAbstractListModel t...
     |  
     |  
     |  rowsMoved = <unbound qt signal rowsMoved of QAbstractListModel type>
     |  
     |  
     |  rowsRemoved = <unbound qt signal rowsRemoved of QAbstractListModel typ...
     |  
     |  
     |  sender = <unbound qt slot sender of QAbstractListModel type>
     |      X.sender(a) -> PythonQt.private.QObject
     |  
     |  senderSignalIndex = <unbound qt slot senderSignalIndex of QAbstractLis...
     |      X.senderSignalIndex(a) -> int
     |  
     |  setData = <unbound qt slot py_q_setData of QAbstractListModel type>
     |      X.setData(a, b, c, d) -> bool
     |  
     |  setHeaderData = <unbound qt slot py_q_setHeaderData of QAbstractListMo...
     |      X.setHeaderData(a, b, c, d, e) -> bool
     |  
     |  setItemData = <unbound qt slot py_q_setItemData of QAbstractListModel ...
     |      X.setItemData(a, b, c) -> bool
     |  
     |  setObjectName = <unbound qt slot setObjectName of QAbstractListModel t...
     |      X.setObjectName(a, b)
     |  
     |  setParent = <unbound qt slot setParent of QAbstractListModel type>
     |      X.setParent(a, b)
     |  
     |  setProperty = <unbound qt slot setProperty of QAbstractListModel type>
     |      X.setProperty(a, b, c) -> bool
     |  
     |  sibling = <unbound qt slot py_q_sibling of QAbstractListModel type>
     |      X.sibling(a, b, c, d) -> PythonQt.QtCore.QModelIndex
     |  
     |  signalsBlocked = <unbound qt slot signalsBlocked of QAbstractListModel...
     |      X.signalsBlocked(a) -> bool
     |  
     |  sort = <unbound qt slot py_q_sort of QAbstractListModel type>
     |      X.sort(a, b, c)
     |  
     |  span = <unbound qt slot py_q_span of QAbstractListModel type>
     |      X.span(a, b) -> PythonQt.QtCore.QSize
     |  
     |  startTimer = <unbound qt slot startTimer of QAbstractListModel type>
     |      X.startTimer(a, b, c) -> int
     |  
     |  submit = <unbound qt slot py_q_submit of QAbstractListModel type>
     |      X.submit(a) -> bool
     |  
     |  supportedDragActions = <unbound qt slot py_q_supportedDragActions of Q...
     |      X.supportedDragActions(a)
     |  
     |  supportedDropActions = <unbound qt slot py_q_supportedDropActions of Q...
     |      X.supportedDropActions(a)
     |  
     |  thread = <unbound qt slot thread of QAbstractListModel type>
     |      X.thread(a)
     |  
     |  timerEvent = <unbound qt slot py_q_timerEvent of QAbstractListModel ty...
     |      X.timerEvent(a, b)
     |  
     |  tr = <unbound qt slot tr of QAbstractListModel type>
     |      X.tr(a, b, c, d) -> str
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __delattr__(...)
     |      x.__delattr__('name') <==> del x.name
     |  
     |  __eq__(...)
     |      x.__eq__(y) <==> x==y
     |  
     |  __ge__(...)
     |      x.__ge__(y) <==> x>=y
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __gt__(...)
     |      x.__gt__(y) <==> x>y
     |  
     |  __hash__(...)
     |      x.__hash__() <==> hash(x)
     |  
     |  __le__(...)
     |      x.__le__(y) <==> x<=y
     |  
     |  __lt__(...)
     |      x.__lt__(y) <==> x<y
     |  
     |  __ne__(...)
     |      x.__ne__(y) <==> x!=y
     |  
     |  __nonzero__(...)
     |      x.__nonzero__() <==> x != 0
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __setattr__(...)
     |      x.__setattr__('name', value) <==> x.name = value
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __new__ = <built-in method __new__ of PythonQt.PythonQtClassWrapper ob...
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
    
    class QAbstractProxyModel(PythonQt.PythonQtInstanceWrapper)
     |  Method resolution order:
     |      QAbstractProxyModel
     |      PythonQt.PythonQtInstanceWrapper
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  __init__(...)
     |      x.__init__(...) initializes x; see help(type(x)) for signature
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  HorizontalSortHint = 2
     |  
     |  LayoutChangeHint = <class 'PythonQt.QtCore.LayoutChangeHint'>
     |  
     |  
     |  NoLayoutChangeHint = 0
     |  
     |  VerticalSortHint = 1
     |  
     |  beginInsertColumns = <unbound qt slot beginInsertColumns of QAbstractP...
     |      X.beginInsertColumns(a, b, c, d)
     |  
     |  beginInsertRows = <unbound qt slot beginInsertRows of QAbstractProxyMo...
     |      X.beginInsertRows(a, b, c, d)
     |  
     |  beginMoveColumns = <unbound qt slot beginMoveColumns of QAbstractProxy...
     |      X.beginMoveColumns(a, b, c, d, e, f) -> bool
     |  
     |  beginMoveRows = <unbound qt slot beginMoveRows of QAbstractProxyModel ...
     |      X.beginMoveRows(a, b, c, d, e, f) -> bool
     |  
     |  beginRemoveColumns = <unbound qt slot beginRemoveColumns of QAbstractP...
     |      X.beginRemoveColumns(a, b, c, d)
     |  
     |  beginRemoveRows = <unbound qt slot beginRemoveRows of QAbstractProxyMo...
     |      X.beginRemoveRows(a, b, c, d)
     |  
     |  beginResetModel = <unbound qt slot beginResetModel of QAbstractProxyMo...
     |      X.beginResetModel(a)
     |  
     |  blockSignals = <unbound qt slot blockSignals of QAbstractProxyModel ty...
     |      X.blockSignals(a, b) -> bool
     |  
     |  buddy = <unbound qt slot py_q_buddy of QAbstractProxyModel type>
     |      X.buddy(a, b) -> PythonQt.QtCore.QModelIndex
     |  
     |  canDropMimeData = <unbound qt slot py_q_canDropMimeData of QAbstractPr...
     |      X.canDropMimeData(a, b, c, d, e, f) -> bool
     |  
     |  canFetchMore = <unbound qt slot py_q_canFetchMore of QAbstractProxyMod...
     |      X.canFetchMore(a, b) -> bool
     |  
     |  changePersistentIndex = <unbound qt slot changePersistentIndex of QAbs...
     |      X.changePersistentIndex(a, b, c)
     |  
     |  changePersistentIndexList = <unbound qt slot changePersistentIndexList...
     |      X.changePersistentIndexList(a, b, c)
     |  
     |  childEvent = <unbound qt slot py_q_childEvent of QAbstractProxyModel t...
     |      X.childEvent(a, b)
     |  
     |  children = <unbound qt slot children of QAbstractProxyModel type>
     |      X.children(a) -> tuple
     |  
     |  className = <built-in method className of PythonQt.PythonQtClassWrappe...
     |      Return the classname of the object
     |  
     |  columnCount = <unbound qt slot py_q_columnCount of QAbstractProxyModel...
     |      X.columnCount(a, b) -> int
     |  
     |  columnsAboutToBeInserted = <unbound qt signal columnsAboutToBeInserted...
     |  
     |  
     |  columnsAboutToBeMoved = <unbound qt signal columnsAboutToBeMoved of QA...
     |  
     |  
     |  columnsAboutToBeRemoved = <unbound qt signal columnsAboutToBeRemoved o...
     |  
     |  
     |  columnsInserted = <unbound qt signal columnsInserted of QAbstractProxy...
     |  
     |  
     |  columnsMoved = <unbound qt signal columnsMoved of QAbstractProxyModel ...
     |  
     |  
     |  columnsRemoved = <unbound qt signal columnsRemoved of QAbstractProxyMo...
     |  
     |  
     |  connect = <unbound qt slot connect of QAbstractProxyModel type>
     |      X.connect(a, b, c, d, e) -> bool
     |  
     |  createIndex = <unbound qt slot createIndex of QAbstractProxyModel type...
     |      X.createIndex(a, b, c, d) -> PythonQt.QtCore.QModelIndex
     |  
     |  customEvent = <unbound qt slot py_q_customEvent of QAbstractProxyModel...
     |      X.customEvent(a, b)
     |  
     |  data = <unbound qt slot py_q_data of QAbstractProxyModel type>
     |      X.data(a, b, c) -> object
     |  
     |  dataChanged = <unbound qt signal dataChanged of QAbstractProxyModel ty...
     |  
     |  
     |  decodeData = <unbound qt slot decodeData of QAbstractProxyModel type>
     |      X.decodeData(a, b, c, d, e) -> bool
     |  
     |  delete = <built-in method delete of PythonQt.PythonQtClassWrapper obje...
     |      Deletes the given C++ object
     |  
     |  deleteLater = <unbound qt slot deleteLater of QAbstractProxyModel type...
     |      X.deleteLater()
     |  
     |  destroyed = <unbound qt signal destroyed of QAbstractProxyModel type>
     |  
     |  
     |  disconnect = <unbound qt slot disconnect of QAbstractProxyModel type>
     |      X.disconnect(a, b, c, d) -> bool
     |  
     |  dropMimeData = <unbound qt slot py_q_dropMimeData of QAbstractProxyMod...
     |      X.dropMimeData(a, b, c, d, e, f) -> bool
     |  
     |  dumpObjectInfo = <unbound qt slot dumpObjectInfo of QAbstractProxyMode...
     |      X.dumpObjectInfo(a)
     |  
     |  dumpObjectTree = <unbound qt slot dumpObjectTree of QAbstractProxyMode...
     |      X.dumpObjectTree(a)
     |  
     |  dynamicPropertyNames = <unbound qt slot dynamicPropertyNames of QAbstr...
     |      X.dynamicPropertyNames(a)
     |  
     |  encodeData = <unbound qt slot encodeData of QAbstractProxyModel type>
     |      X.encodeData(a, b, c)
     |  
     |  endInsertColumns = <unbound qt slot endInsertColumns of QAbstractProxy...
     |      X.endInsertColumns(a)
     |  
     |  endInsertRows = <unbound qt slot endInsertRows of QAbstractProxyModel ...
     |      X.endInsertRows(a)
     |  
     |  endMoveColumns = <unbound qt slot endMoveColumns of QAbstractProxyMode...
     |      X.endMoveColumns(a)
     |  
     |  endMoveRows = <unbound qt slot endMoveRows of QAbstractProxyModel type...
     |      X.endMoveRows(a)
     |  
     |  endRemoveColumns = <unbound qt slot endRemoveColumns of QAbstractProxy...
     |      X.endRemoveColumns(a)
     |  
     |  endRemoveRows = <unbound qt slot endRemoveRows of QAbstractProxyModel ...
     |      X.endRemoveRows(a)
     |  
     |  endResetModel = <unbound qt slot endResetModel of QAbstractProxyModel ...
     |      X.endResetModel(a)
     |  
     |  event = <unbound qt slot py_q_event of QAbstractProxyModel type>
     |      X.event(a, b) -> bool
     |  
     |  eventFilter = <unbound qt slot py_q_eventFilter of QAbstractProxyModel...
     |      X.eventFilter(a, b, c) -> bool
     |  
     |  fetchMore = <unbound qt slot py_q_fetchMore of QAbstractProxyModel typ...
     |      X.fetchMore(a, b)
     |  
     |  findChild = <unbound qt slot findChild of QAbstractProxyModel type>
     |      X.findChild(a, b, c) -> PythonQt.private.QObject
     |  
     |  findChildren = <unbound qt slot findChildren of QAbstractProxyModel ty...
     |      X.findChildren(a, b, c) -> tuple
     |  
     |  flags = <unbound qt slot py_q_flags of QAbstractProxyModel type>
     |      X.flags(a, b)
     |  
     |  hasChildren = <unbound qt slot py_q_hasChildren of QAbstractProxyModel...
     |      X.hasChildren(a, b) -> bool
     |  
     |  hasIndex = <unbound qt slot hasIndex of QAbstractProxyModel type>
     |      X.hasIndex(a, b, c, d) -> bool
     |  
     |  headerData = <unbound qt slot py_q_headerData of QAbstractProxyModel t...
     |      X.headerData(a, b, c, d) -> object
     |  
     |  headerDataChanged = <unbound qt signal headerDataChanged of QAbstractP...
     |  
     |  
     |  help = <built-in method help of PythonQt.PythonQtClassWrapper object>
     |      Shows the help of available methods for this class
     |  
     |  index = <unbound qt slot py_q_index of QAbstractProxyModel type>
     |      X.index(a, b, c, d) -> PythonQt.QtCore.QModelIndex
     |  
     |  inherits = <built-in method inherits of PythonQt.PythonQtClassWrapper ...
     |      Returns if the class inherits or is of given type name
     |  
     |  insertColumn = <unbound qt slot insertColumn of QAbstractProxyModel ty...
     |      X.insertColumn(a, b, c) -> bool
     |  
     |  insertColumns = <unbound qt slot py_q_insertColumns of QAbstractProxyM...
     |      X.insertColumns(a, b, c, d) -> bool
     |  
     |  insertRow = <unbound qt slot insertRow of QAbstractProxyModel type>
     |      X.insertRow(a, b, c) -> bool
     |  
     |  insertRows = <unbound qt slot py_q_insertRows of QAbstractProxyModel t...
     |      X.insertRows(a, b, c, d) -> bool
     |  
     |  installEventFilter = <unbound qt slot installEventFilter of QAbstractP...
     |      X.installEventFilter(a, b)
     |  
     |  isSignalConnected = <unbound qt slot isSignalConnected of QAbstractPro...
     |      X.isSignalConnected(a, b) -> bool
     |  
     |  isWidgetType = <unbound qt slot isWidgetType of QAbstractProxyModel ty...
     |      X.isWidgetType(a) -> bool
     |  
     |  isWindowType = <unbound qt slot isWindowType of QAbstractProxyModel ty...
     |      X.isWindowType(a) -> bool
     |  
     |  itemData = <unbound qt slot py_q_itemData of QAbstractProxyModel type>
     |      X.itemData(a, b) -> dict
     |  
     |  killTimer = <unbound qt slot killTimer of QAbstractProxyModel type>
     |      X.killTimer(a, b)
     |  
     |  layoutAboutToBeChanged = <unbound qt signal layoutAboutToBeChanged of ...
     |  
     |  
     |  layoutChanged = <unbound qt signal layoutChanged of QAbstractProxyMode...
     |  
     |  
     |  mapFromSource = <unbound qt slot py_q_mapFromSource of QAbstractProxyM...
     |      X.mapFromSource(a, b) -> PythonQt.QtCore.QModelIndex
     |  
     |  mapSelectionFromSource = <unbound qt slot py_q_mapSelectionFromSource ...
     |      X.mapSelectionFromSource(a, b) -> PythonQt.QtGui.QItemSelection
     |  
     |  mapSelectionToSource = <unbound qt slot py_q_mapSelectionToSource of Q...
     |      X.mapSelectionToSource(a, b) -> PythonQt.QtGui.QItemSelection
     |  
     |  mapToSource = <unbound qt slot py_q_mapToSource of QAbstractProxyModel...
     |      X.mapToSource(a, b) -> PythonQt.QtCore.QModelIndex
     |  
     |  match = <unbound qt slot py_q_match of QAbstractProxyModel type>
     |      X.match(a, b, c, d, e, f) -> tuple
     |  
     |  metaObject = <unbound qt slot metaObject of QAbstractProxyModel type>
     |      X.metaObject(a) -> PythonQt.QtCore.QMetaObject
     |  
     |  mimeData = <unbound qt slot py_q_mimeData of QAbstractProxyModel type>
     |      X.mimeData(a, b) -> PythonQt.QtCore.QMimeData
     |  
     |  mimeTypes = <unbound qt slot py_q_mimeTypes of QAbstractProxyModel typ...
     |      X.mimeTypes(a) -> tuple
     |  
     |  modelAboutToBeReset = <unbound qt signal modelAboutToBeReset of QAbstr...
     |  
     |  
     |  modelReset = <unbound qt signal modelReset of QAbstractProxyModel type...
     |  
     |  
     |  moveColumn = <unbound qt slot moveColumn of QAbstractProxyModel type>
     |      X.moveColumn(a, b, c, d, e) -> bool
     |  
     |  moveColumns = <unbound qt slot py_q_moveColumns of QAbstractProxyModel...
     |      X.moveColumns(a, b, c, d, e, f) -> bool
     |  
     |  moveRow = <unbound qt slot moveRow of QAbstractProxyModel type>
     |      X.moveRow(a, b, c, d, e) -> bool
     |  
     |  moveRows = <unbound qt slot py_q_moveRows of QAbstractProxyModel type>
     |      X.moveRows(a, b, c, d, e, f) -> bool
     |  
     |  moveToThread = <unbound qt slot moveToThread of QAbstractProxyModel ty...
     |      X.moveToThread(a, b)
     |  
     |  objectName = None
     |  
     |  objectNameChanged = <unbound qt signal objectNameChanged of QAbstractP...
     |  
     |  
     |  parent = <unbound qt slot py_q_parent of QAbstractProxyModel type>
     |      X.parent(a, b) -> PythonQt.QtCore.QModelIndex
     |  
     |  persistentIndexList = <unbound qt slot persistentIndexList of QAbstrac...
     |      X.persistentIndexList(a) -> tuple
     |  
     |  property = <unbound qt slot property of QAbstractProxyModel type>
     |      X.property(a, b) -> object
     |  
     |  removeColumn = <unbound qt slot removeColumn of QAbstractProxyModel ty...
     |      X.removeColumn(a, b, c) -> bool
     |  
     |  removeColumns = <unbound qt slot py_q_removeColumns of QAbstractProxyM...
     |      X.removeColumns(a, b, c, d) -> bool
     |  
     |  removeEventFilter = <unbound qt slot removeEventFilter of QAbstractPro...
     |      X.removeEventFilter(a, b)
     |  
     |  removeRow = <unbound qt slot removeRow of QAbstractProxyModel type>
     |      X.removeRow(a, b, c) -> bool
     |  
     |  removeRows = <unbound qt slot py_q_removeRows of QAbstractProxyModel t...
     |      X.removeRows(a, b, c, d) -> bool
     |  
     |  revert = <unbound qt slot py_q_revert of QAbstractProxyModel type>
     |      X.revert(a)
     |  
     |  roleNames = <unbound qt slot py_q_roleNames of QAbstractProxyModel typ...
     |      X.roleNames(a) -> dict
     |  
     |  rowCount = <unbound qt slot py_q_rowCount of QAbstractProxyModel type>
     |      X.rowCount(a, b) -> int
     |  
     |  rowsAboutToBeInserted = <unbound qt signal rowsAboutToBeInserted of QA...
     |  
     |  
     |  rowsAboutToBeMoved = <unbound qt signal rowsAboutToBeMoved of QAbstrac...
     |  
     |  
     |  rowsAboutToBeRemoved = <unbound qt signal rowsAboutToBeRemoved of QAbs...
     |  
     |  
     |  rowsInserted = <unbound qt signal rowsInserted of QAbstractProxyModel ...
     |  
     |  
     |  rowsMoved = <unbound qt signal rowsMoved of QAbstractProxyModel type>
     |  
     |  
     |  rowsRemoved = <unbound qt signal rowsRemoved of QAbstractProxyModel ty...
     |  
     |  
     |  sender = <unbound qt slot sender of QAbstractProxyModel type>
     |      X.sender(a) -> PythonQt.private.QObject
     |  
     |  senderSignalIndex = <unbound qt slot senderSignalIndex of QAbstractPro...
     |      X.senderSignalIndex(a) -> int
     |  
     |  setData = <unbound qt slot py_q_setData of QAbstractProxyModel type>
     |      X.setData(a, b, c, d) -> bool
     |  
     |  setHeaderData = <unbound qt slot py_q_setHeaderData of QAbstractProxyM...
     |      X.setHeaderData(a, b, c, d, e) -> bool
     |  
     |  setItemData = <unbound qt slot py_q_setItemData of QAbstractProxyModel...
     |      X.setItemData(a, b, c) -> bool
     |  
     |  setObjectName = <unbound qt slot setObjectName of QAbstractProxyModel ...
     |      X.setObjectName(a, b)
     |  
     |  setParent = <unbound qt slot setParent of QAbstractProxyModel type>
     |      X.setParent(a, b)
     |  
     |  setProperty = <unbound qt slot setProperty of QAbstractProxyModel type...
     |      X.setProperty(a, b, c) -> bool
     |  
     |  setSourceModel = <unbound qt slot py_q_setSourceModel of QAbstractProx...
     |      X.setSourceModel(a, b)
     |  
     |  sibling = <unbound qt slot py_q_sibling of QAbstractProxyModel type>
     |      X.sibling(a, b, c, d) -> PythonQt.QtCore.QModelIndex
     |  
     |  signalsBlocked = <unbound qt slot signalsBlocked of QAbstractProxyMode...
     |      X.signalsBlocked(a) -> bool
     |  
     |  sort = <unbound qt slot py_q_sort of QAbstractProxyModel type>
     |      X.sort(a, b, c)
     |  
     |  sourceModel = QAbstractItemModel (QAbstractItemModel at: 0x0)
     |  
     |  sourceModelChanged = <unbound qt signal sourceModelChanged of QAbstrac...
     |  
     |  
     |  span = <unbound qt slot py_q_span of QAbstractProxyModel type>
     |      X.span(a, b) -> PythonQt.QtCore.QSize
     |  
     |  startTimer = <unbound qt slot startTimer of QAbstractProxyModel type>
     |      X.startTimer(a, b, c) -> int
     |  
     |  submit = <unbound qt slot py_q_submit of QAbstractProxyModel type>
     |      X.submit(a) -> bool
     |  
     |  supportedDragActions = <unbound qt slot py_q_supportedDragActions of Q...
     |      X.supportedDragActions(a)
     |  
     |  supportedDropActions = <unbound qt slot py_q_supportedDropActions of Q...
     |      X.supportedDropActions(a)
     |  
     |  thread = <unbound qt slot thread of QAbstractProxyModel type>
     |      X.thread(a)
     |  
     |  timerEvent = <unbound qt slot py_q_timerEvent of QAbstractProxyModel t...
     |      X.timerEvent(a, b)
     |  
     |  tr = <unbound qt slot tr of QAbstractProxyModel type>
     |      X.tr(a, b, c, d) -> str
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __delattr__(...)
     |      x.__delattr__('name') <==> del x.name
     |  
     |  __eq__(...)
     |      x.__eq__(y) <==> x==y
     |  
     |  __ge__(...)
     |      x.__ge__(y) <==> x>=y
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __gt__(...)
     |      x.__gt__(y) <==> x>y
     |  
     |  __hash__(...)
     |      x.__hash__() <==> hash(x)
     |  
     |  __le__(...)
     |      x.__le__(y) <==> x<=y
     |  
     |  __lt__(...)
     |      x.__lt__(y) <==> x<y
     |  
     |  __ne__(...)
     |      x.__ne__(y) <==> x!=y
     |  
     |  __nonzero__(...)
     |      x.__nonzero__() <==> x != 0
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __setattr__(...)
     |      x.__setattr__('name', value) <==> x.name = value
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __new__ = <built-in method __new__ of PythonQt.PythonQtClassWrapper ob...
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
    
    class QAbstractState(PythonQt.PythonQtInstanceWrapper)
     |  Method resolution order:
     |      QAbstractState
     |      PythonQt.PythonQtInstanceWrapper
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  __init__(...)
     |      x.__init__(...) initializes x; see help(type(x)) for signature
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  active = None
     |  
     |  activeChanged = <unbound qt signal activeChanged of QAbstractState typ...
     |  
     |  
     |  blockSignals = <unbound qt slot blockSignals of QAbstractState type>
     |      X.blockSignals(a, b) -> bool
     |  
     |  childEvent = <unbound qt slot py_q_childEvent of QAbstractState type>
     |      X.childEvent(a, b)
     |  
     |  children = <unbound qt slot children of QAbstractState type>
     |      X.children(a) -> tuple
     |  
     |  className = <built-in method className of PythonQt.PythonQtClassWrappe...
     |      Return the classname of the object
     |  
     |  connect = <unbound qt slot connect of QAbstractState type>
     |      X.connect(a, b, c, d, e) -> bool
     |  
     |  customEvent = <unbound qt slot py_q_customEvent of QAbstractState type...
     |      X.customEvent(a, b)
     |  
     |  delete = <built-in method delete of PythonQt.PythonQtClassWrapper obje...
     |      Deletes the given C++ object
     |  
     |  deleteLater = <unbound qt slot deleteLater of QAbstractState type>
     |      X.deleteLater()
     |  
     |  destroyed = <unbound qt signal destroyed of QAbstractState type>
     |  
     |  
     |  disconnect = <unbound qt slot disconnect of QAbstractState type>
     |      X.disconnect(a, b, c, d) -> bool
     |  
     |  dumpObjectInfo = <unbound qt slot dumpObjectInfo of QAbstractState typ...
     |      X.dumpObjectInfo(a)
     |  
     |  dumpObjectTree = <unbound qt slot dumpObjectTree of QAbstractState typ...
     |      X.dumpObjectTree(a)
     |  
     |  dynamicPropertyNames = <unbound qt slot dynamicPropertyNames of QAbstr...
     |      X.dynamicPropertyNames(a)
     |  
     |  entered = <unbound qt signal entered of QAbstractState type>
     |  
     |  
     |  event = <unbound qt slot py_q_event of QAbstractState type>
     |      X.event(a, b) -> bool
     |  
     |  eventFilter = <unbound qt slot py_q_eventFilter of QAbstractState type...
     |      X.eventFilter(a, b, c) -> bool
     |  
     |  exited = <unbound qt signal exited of QAbstractState type>
     |  
     |  
     |  findChild = <unbound qt slot findChild of QAbstractState type>
     |      X.findChild(a, b, c) -> PythonQt.private.QObject
     |  
     |  findChildren = <unbound qt slot findChildren of QAbstractState type>
     |      X.findChildren(a, b, c) -> tuple
     |  
     |  help = <built-in method help of PythonQt.PythonQtClassWrapper object>
     |      Shows the help of available methods for this class
     |  
     |  inherits = <built-in method inherits of PythonQt.PythonQtClassWrapper ...
     |      Returns if the class inherits or is of given type name
     |  
     |  installEventFilter = <unbound qt slot installEventFilter of QAbstractS...
     |      X.installEventFilter(a, b)
     |  
     |  isSignalConnected = <unbound qt slot isSignalConnected of QAbstractSta...
     |      X.isSignalConnected(a, b) -> bool
     |  
     |  isWidgetType = <unbound qt slot isWidgetType of QAbstractState type>
     |      X.isWidgetType(a) -> bool
     |  
     |  isWindowType = <unbound qt slot isWindowType of QAbstractState type>
     |      X.isWindowType(a) -> bool
     |  
     |  killTimer = <unbound qt slot killTimer of QAbstractState type>
     |      X.killTimer(a, b)
     |  
     |  machine = <unbound qt slot machine of QAbstractState type>
     |      X.machine(a) -> PythonQt.QtCore.QStateMachine
     |  
     |  metaObject = <unbound qt slot metaObject of QAbstractState type>
     |      X.metaObject(a) -> PythonQt.QtCore.QMetaObject
     |  
     |  moveToThread = <unbound qt slot moveToThread of QAbstractState type>
     |      X.moveToThread(a, b)
     |  
     |  objectName = None
     |  
     |  objectNameChanged = <unbound qt signal objectNameChanged of QAbstractS...
     |  
     |  
     |  onEntry = <unbound qt slot py_q_onEntry of QAbstractState type>
     |      X.onEntry(a, b)
     |  
     |  onExit = <unbound qt slot py_q_onExit of QAbstractState type>
     |      X.onExit(a, b)
     |  
     |  parent = <unbound qt slot parent of QAbstractState type>
     |      X.parent(a) -> PythonQt.private.QObject
     |  
     |  parentState = <unbound qt slot parentState of QAbstractState type>
     |      X.parentState(a) -> PythonQt.QtCore.QState
     |  
     |  property = <unbound qt slot property of QAbstractState type>
     |      X.property(a, b) -> object
     |  
     |  removeEventFilter = <unbound qt slot removeEventFilter of QAbstractSta...
     |      X.removeEventFilter(a, b)
     |  
     |  sender = <unbound qt slot sender of QAbstractState type>
     |      X.sender(a) -> PythonQt.private.QObject
     |  
     |  senderSignalIndex = <unbound qt slot senderSignalIndex of QAbstractSta...
     |      X.senderSignalIndex(a) -> int
     |  
     |  setObjectName = <unbound qt slot setObjectName of QAbstractState type>
     |      X.setObjectName(a, b)
     |  
     |  setParent = <unbound qt slot setParent of QAbstractState type>
     |      X.setParent(a, b)
     |  
     |  setProperty = <unbound qt slot setProperty of QAbstractState type>
     |      X.setProperty(a, b, c) -> bool
     |  
     |  signalsBlocked = <unbound qt slot signalsBlocked of QAbstractState typ...
     |      X.signalsBlocked(a) -> bool
     |  
     |  startTimer = <unbound qt slot startTimer of QAbstractState type>
     |      X.startTimer(a, b, c) -> int
     |  
     |  thread = <unbound qt slot thread of QAbstractState type>
     |      X.thread(a)
     |  
     |  timerEvent = <unbound qt slot py_q_timerEvent of QAbstractState type>
     |      X.timerEvent(a, b)
     |  
     |  tr = <unbound qt slot tr of QAbstractState type>
     |      X.tr(a, b, c, d) -> str
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __delattr__(...)
     |      x.__delattr__('name') <==> del x.name
     |  
     |  __eq__(...)
     |      x.__eq__(y) <==> x==y
     |  
     |  __ge__(...)
     |      x.__ge__(y) <==> x>=y
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __gt__(...)
     |      x.__gt__(y) <==> x>y
     |  
     |  __hash__(...)
     |      x.__hash__() <==> hash(x)
     |  
     |  __le__(...)
     |      x.__le__(y) <==> x<=y
     |  
     |  __lt__(...)
     |      x.__lt__(y) <==> x<y
     |  
     |  __ne__(...)
     |      x.__ne__(y) <==> x!=y
     |  
     |  __nonzero__(...)
     |      x.__nonzero__() <==> x != 0
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __setattr__(...)
     |      x.__setattr__('name', value) <==> x.name = value
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __new__ = <built-in method __new__ of PythonQt.PythonQtClassWrapper ob...
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
    
    class QAbstractTransition(PythonQt.PythonQtInstanceWrapper)
     |  Method resolution order:
     |      QAbstractTransition
     |      PythonQt.PythonQtInstanceWrapper
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  __init__(...)
     |      x.__init__(...) initializes x; see help(type(x)) for signature
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  ExternalTransition = 0
     |  
     |  InternalTransition = 1
     |  
     |  TransitionType = <class 'PythonQt.QtCore.TransitionType'>
     |  
     |  
     |  addAnimation = <unbound qt slot addAnimation of QAbstractTransition ty...
     |      X.addAnimation(a, b)
     |  
     |  animations = <unbound qt slot animations of QAbstractTransition type>
     |      X.animations(a) -> tuple
     |  
     |  blockSignals = <unbound qt slot blockSignals of QAbstractTransition ty...
     |      X.blockSignals(a, b) -> bool
     |  
     |  childEvent = <unbound qt slot py_q_childEvent of QAbstractTransition t...
     |      X.childEvent(a, b)
     |  
     |  children = <unbound qt slot children of QAbstractTransition type>
     |      X.children(a) -> tuple
     |  
     |  className = <built-in method className of PythonQt.PythonQtClassWrappe...
     |      Return the classname of the object
     |  
     |  connect = <unbound qt slot connect of QAbstractTransition type>
     |      X.connect(a, b, c, d, e) -> bool
     |  
     |  customEvent = <unbound qt slot py_q_customEvent of QAbstractTransition...
     |      X.customEvent(a, b)
     |  
     |  delete = <built-in method delete of PythonQt.PythonQtClassWrapper obje...
     |      Deletes the given C++ object
     |  
     |  deleteLater = <unbound qt slot deleteLater of QAbstractTransition type...
     |      X.deleteLater()
     |  
     |  destroyed = <unbound qt signal destroyed of QAbstractTransition type>
     |  
     |  
     |  disconnect = <unbound qt slot disconnect of QAbstractTransition type>
     |      X.disconnect(a, b, c, d) -> bool
     |  
     |  dumpObjectInfo = <unbound qt slot dumpObjectInfo of QAbstractTransitio...
     |      X.dumpObjectInfo(a)
     |  
     |  dumpObjectTree = <unbound qt slot dumpObjectTree of QAbstractTransitio...
     |      X.dumpObjectTree(a)
     |  
     |  dynamicPropertyNames = <unbound qt slot dynamicPropertyNames of QAbstr...
     |      X.dynamicPropertyNames(a)
     |  
     |  event = <unbound qt slot py_q_event of QAbstractTransition type>
     |      X.event(a, b) -> bool
     |  
     |  eventFilter = <unbound qt slot py_q_eventFilter of QAbstractTransition...
     |      X.eventFilter(a, b, c) -> bool
     |  
     |  eventTest = <unbound qt slot py_q_eventTest of QAbstractTransition typ...
     |      X.eventTest(a, b) -> bool
     |  
     |  findChild = <unbound qt slot findChild of QAbstractTransition type>
     |      X.findChild(a, b, c) -> PythonQt.private.QObject
     |  
     |  findChildren = <unbound qt slot findChildren of QAbstractTransition ty...
     |      X.findChildren(a, b, c) -> tuple
     |  
     |  help = <built-in method help of PythonQt.PythonQtClassWrapper object>
     |      Shows the help of available methods for this class
     |  
     |  inherits = <built-in method inherits of PythonQt.PythonQtClassWrapper ...
     |      Returns if the class inherits or is of given type name
     |  
     |  installEventFilter = <unbound qt slot installEventFilter of QAbstractT...
     |      X.installEventFilter(a, b)
     |  
     |  isSignalConnected = <unbound qt slot isSignalConnected of QAbstractTra...
     |      X.isSignalConnected(a, b) -> bool
     |  
     |  isWidgetType = <unbound qt slot isWidgetType of QAbstractTransition ty...
     |      X.isWidgetType(a) -> bool
     |  
     |  isWindowType = <unbound qt slot isWindowType of QAbstractTransition ty...
     |      X.isWindowType(a) -> bool
     |  
     |  killTimer = <unbound qt slot killTimer of QAbstractTransition type>
     |      X.killTimer(a, b)
     |  
     |  machine = <unbound qt slot machine of QAbstractTransition type>
     |      X.machine(a) -> PythonQt.QtCore.QStateMachine
     |  
     |  metaObject = <unbound qt slot metaObject of QAbstractTransition type>
     |      X.metaObject(a) -> PythonQt.QtCore.QMetaObject
     |  
     |  moveToThread = <unbound qt slot moveToThread of QAbstractTransition ty...
     |      X.moveToThread(a, b)
     |  
     |  objectName = None
     |  
     |  objectNameChanged = <unbound qt signal objectNameChanged of QAbstractT...
     |  
     |  
     |  onTransition = <unbound qt slot py_q_onTransition of QAbstractTransiti...
     |      X.onTransition(a, b)
     |  
     |  parent = <unbound qt slot parent of QAbstractTransition type>
     |      X.parent(a) -> PythonQt.private.QObject
     |  
     |  property = <unbound qt slot property of QAbstractTransition type>
     |      X.property(a, b) -> object
     |  
     |  removeAnimation = <unbound qt slot removeAnimation of QAbstractTransit...
     |      X.removeAnimation(a, b)
     |  
     |  removeEventFilter = <unbound qt slot removeEventFilter of QAbstractTra...
     |      X.removeEventFilter(a, b)
     |  
     |  sender = <unbound qt slot sender of QAbstractTransition type>
     |      X.sender(a) -> PythonQt.private.QObject
     |  
     |  senderSignalIndex = <unbound qt slot senderSignalIndex of QAbstractTra...
     |      X.senderSignalIndex(a) -> int
     |  
     |  setObjectName = <unbound qt slot setObjectName of QAbstractTransition ...
     |      X.setObjectName(a, b)
     |  
     |  setParent = <unbound qt slot setParent of QAbstractTransition type>
     |      X.setParent(a, b)
     |  
     |  setProperty = <unbound qt slot setProperty of QAbstractTransition type...
     |      X.setProperty(a, b, c) -> bool
     |  
     |  setTargetState = <unbound qt slot setTargetState of QAbstractTransitio...
     |      X.setTargetState(a, b)
     |  
     |  setTargetStates = <unbound qt slot setTargetStates of QAbstractTransit...
     |      X.setTargetStates(a, b)
     |  
     |  setTransitionType = <unbound qt slot setTransitionType of QAbstractTra...
     |      X.setTransitionType(a, b)
     |  
     |  signalsBlocked = <unbound qt slot signalsBlocked of QAbstractTransitio...
     |      X.signalsBlocked(a) -> bool
     |  
     |  sourceState = QState (QState at: 0x0)
     |  
     |  startTimer = <unbound qt slot startTimer of QAbstractTransition type>
     |      X.startTimer(a, b, c) -> int
     |  
     |  targetState = QAbstractState (QAbstractState at: 0x0)
     |  
     |  targetStateChanged = <unbound qt signal targetStateChanged of QAbstrac...
     |  
     |  
     |  targetStates = None
     |  
     |  targetStatesChanged = <unbound qt signal targetStatesChanged of QAbstr...
     |  
     |  
     |  thread = <unbound qt slot thread of QAbstractTransition type>
     |      X.thread(a)
     |  
     |  timerEvent = <unbound qt slot py_q_timerEvent of QAbstractTransition t...
     |      X.timerEvent(a, b)
     |  
     |  tr = <unbound qt slot tr of QAbstractTransition type>
     |      X.tr(a, b, c, d) -> str
     |  
     |  transitionType = None
     |  
     |  triggered = <unbound qt signal triggered of QAbstractTransition type>
     |  
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __delattr__(...)
     |      x.__delattr__('name') <==> del x.name
     |  
     |  __eq__(...)
     |      x.__eq__(y) <==> x==y
     |  
     |  __ge__(...)
     |      x.__ge__(y) <==> x>=y
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __gt__(...)
     |      x.__gt__(y) <==> x>y
     |  
     |  __hash__(...)
     |      x.__hash__() <==> hash(x)
     |  
     |  __le__(...)
     |      x.__le__(y) <==> x<=y
     |  
     |  __lt__(...)
     |      x.__lt__(y) <==> x<y
     |  
     |  __ne__(...)
     |      x.__ne__(y) <==> x!=y
     |  
     |  __nonzero__(...)
     |      x.__nonzero__() <==> x != 0
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __setattr__(...)
     |      x.__setattr__('name', value) <==> x.name = value
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __new__ = <built-in method __new__ of PythonQt.PythonQtClassWrapper ob...
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
    
    class QAnimationGroup(PythonQt.PythonQtInstanceWrapper)
     |  Method resolution order:
     |      QAnimationGroup
     |      PythonQt.PythonQtInstanceWrapper
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  __init__(...)
     |      x.__init__(...) initializes x; see help(type(x)) for signature
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  Backward = 1
     |  
     |  DeleteWhenStopped = 1
     |  
     |  DeletionPolicy = <class 'PythonQt.QtCore.DeletionPolicy'>
     |  
     |  
     |  Direction = <class 'PythonQt.QtCore.Direction'>
     |  
     |  
     |  Forward = 0
     |  
     |  KeepWhenStopped = 0
     |  
     |  Paused = 1
     |  
     |  Running = 2
     |  
     |  State = <class 'PythonQt.QtCore.State'>
     |  
     |  
     |  Stopped = 0
     |  
     |  addAnimation = <unbound qt slot addAnimation of QAnimationGroup type>
     |      X.addAnimation(a, b)
     |  
     |  animationAt = <unbound qt slot animationAt of QAnimationGroup type>
     |      X.animationAt(a, b) -> PythonQt.QtCore.QAbstractAnimation
     |  
     |  animationCount = <unbound qt slot animationCount of QAnimationGroup ty...
     |      X.animationCount(a) -> int
     |  
     |  blockSignals = <unbound qt slot blockSignals of QAnimationGroup type>
     |      X.blockSignals(a, b) -> bool
     |  
     |  childEvent = <unbound qt slot py_q_childEvent of QAnimationGroup type>
     |      X.childEvent(a, b)
     |  
     |  children = <unbound qt slot children of QAnimationGroup type>
     |      X.children(a) -> tuple
     |  
     |  className = <built-in method className of PythonQt.PythonQtClassWrappe...
     |      Return the classname of the object
     |  
     |  clear = <unbound qt slot clear of QAnimationGroup type>
     |      X.clear(a)
     |  
     |  connect = <unbound qt slot connect of QAnimationGroup type>
     |      X.connect(a, b, c, d, e) -> bool
     |  
     |  currentLoop = None
     |  
     |  currentLoopChanged = <unbound qt signal currentLoopChanged of QAnimati...
     |  
     |  
     |  currentLoopTime = <unbound qt slot currentLoopTime of QAnimationGroup ...
     |      X.currentLoopTime(a) -> int
     |  
     |  currentTime = None
     |  
     |  customEvent = <unbound qt slot py_q_customEvent of QAnimationGroup typ...
     |      X.customEvent(a, b)
     |  
     |  delete = <built-in method delete of PythonQt.PythonQtClassWrapper obje...
     |      Deletes the given C++ object
     |  
     |  deleteLater = <unbound qt slot deleteLater of QAnimationGroup type>
     |      X.deleteLater()
     |  
     |  destroyed = <unbound qt signal destroyed of QAnimationGroup type>
     |  
     |  
     |  direction = None
     |  
     |  directionChanged = <unbound qt signal directionChanged of QAnimationGr...
     |  
     |  
     |  disconnect = <unbound qt slot disconnect of QAnimationGroup type>
     |      X.disconnect(a, b, c, d) -> bool
     |  
     |  dumpObjectInfo = <unbound qt slot dumpObjectInfo of QAnimationGroup ty...
     |      X.dumpObjectInfo(a)
     |  
     |  dumpObjectTree = <unbound qt slot dumpObjectTree of QAnimationGroup ty...
     |      X.dumpObjectTree(a)
     |  
     |  duration = None
     |  
     |  dynamicPropertyNames = <unbound qt slot dynamicPropertyNames of QAnima...
     |      X.dynamicPropertyNames(a)
     |  
     |  event = <unbound qt slot py_q_event of QAnimationGroup type>
     |      X.event(a, b) -> bool
     |  
     |  eventFilter = <unbound qt slot py_q_eventFilter of QAnimationGroup typ...
     |      X.eventFilter(a, b, c) -> bool
     |  
     |  findChild = <unbound qt slot findChild of QAnimationGroup type>
     |      X.findChild(a, b, c) -> PythonQt.private.QObject
     |  
     |  findChildren = <unbound qt slot findChildren of QAnimationGroup type>
     |      X.findChildren(a, b, c) -> tuple
     |  
     |  finished = <unbound qt signal finished of QAnimationGroup type>
     |  
     |  
     |  group = <unbound qt slot group of QAnimationGroup type>
     |      X.group(a) -> PythonQt.QtCore.QAnimationGroup
     |  
     |  help = <built-in method help of PythonQt.PythonQtClassWrapper object>
     |      Shows the help of available methods for this class
     |  
     |  indexOfAnimation = <unbound qt slot indexOfAnimation of QAnimationGrou...
     |      X.indexOfAnimation(a, b) -> int
     |  
     |  inherits = <built-in method inherits of PythonQt.PythonQtClassWrapper ...
     |      Returns if the class inherits or is of given type name
     |  
     |  insertAnimation = <unbound qt slot insertAnimation of QAnimationGroup ...
     |      X.insertAnimation(a, b, c)
     |  
     |  installEventFilter = <unbound qt slot installEventFilter of QAnimation...
     |      X.installEventFilter(a, b)
     |  
     |  isSignalConnected = <unbound qt slot isSignalConnected of QAnimationGr...
     |      X.isSignalConnected(a, b) -> bool
     |  
     |  isWidgetType = <unbound qt slot isWidgetType of QAnimationGroup type>
     |      X.isWidgetType(a) -> bool
     |  
     |  isWindowType = <unbound qt slot isWindowType of QAnimationGroup type>
     |      X.isWindowType(a) -> bool
     |  
     |  killTimer = <unbound qt slot killTimer of QAnimationGroup type>
     |      X.killTimer(a, b)
     |  
     |  loopCount = None
     |  
     |  metaObject = <unbound qt slot metaObject of QAnimationGroup type>
     |      X.metaObject(a) -> PythonQt.QtCore.QMetaObject
     |  
     |  moveToThread = <unbound qt slot moveToThread of QAnimationGroup type>
     |      X.moveToThread(a, b)
     |  
     |  objectName = None
     |  
     |  objectNameChanged = <unbound qt signal objectNameChanged of QAnimation...
     |  
     |  
     |  parent = <unbound qt slot parent of QAnimationGroup type>
     |      X.parent(a) -> PythonQt.private.QObject
     |  
     |  pause = <unbound qt slot pause of QAnimationGroup type>
     |      X.pause()
     |  
     |  property = <unbound qt slot property of QAnimationGroup type>
     |      X.property(a, b) -> object
     |  
     |  removeAnimation = <unbound qt slot removeAnimation of QAnimationGroup ...
     |      X.removeAnimation(a, b)
     |  
     |  removeEventFilter = <unbound qt slot removeEventFilter of QAnimationGr...
     |      X.removeEventFilter(a, b)
     |  
     |  resume = <unbound qt slot resume of QAnimationGroup type>
     |      X.resume()
     |  
     |  sender = <unbound qt slot sender of QAnimationGroup type>
     |      X.sender(a) -> PythonQt.private.QObject
     |  
     |  senderSignalIndex = <unbound qt slot senderSignalIndex of QAnimationGr...
     |      X.senderSignalIndex(a) -> int
     |  
     |  setCurrentTime = <unbound qt slot setCurrentTime of QAnimationGroup ty...
     |      X.setCurrentTime(a)
     |  
     |  setDirection = <unbound qt slot setDirection of QAnimationGroup type>
     |      X.setDirection(a, b)
     |  
     |  setLoopCount = <unbound qt slot setLoopCount of QAnimationGroup type>
     |      X.setLoopCount(a, b)
     |  
     |  setObjectName = <unbound qt slot setObjectName of QAnimationGroup type...
     |      X.setObjectName(a, b)
     |  
     |  setParent = <unbound qt slot setParent of QAnimationGroup type>
     |      X.setParent(a, b)
     |  
     |  setPaused = <unbound qt slot setPaused of QAnimationGroup type>
     |      X.setPaused(a)
     |  
     |  setProperty = <unbound qt slot setProperty of QAnimationGroup type>
     |      X.setProperty(a, b, c) -> bool
     |  
     |  signalsBlocked = <unbound qt slot signalsBlocked of QAnimationGroup ty...
     |      X.signalsBlocked(a) -> bool
     |  
     |  start = <unbound qt slot start of QAnimationGroup type>
     |      X.start(a)
     |  
     |  startTimer = <unbound qt slot startTimer of QAnimationGroup type>
     |      X.startTimer(a, b, c) -> int
     |  
     |  state = None
     |  
     |  stateChanged = <unbound qt signal stateChanged of QAnimationGroup type...
     |  
     |  
     |  stop = <unbound qt slot stop of QAnimationGroup type>
     |      X.stop()
     |  
     |  takeAnimation = <unbound qt slot takeAnimation of QAnimationGroup type...
     |      X.takeAnimation(a, b) -> PythonQt.QtCore.QAbstractAnimation
     |  
     |  thread = <unbound qt slot thread of QAnimationGroup type>
     |      X.thread(a)
     |  
     |  timerEvent = <unbound qt slot py_q_timerEvent of QAnimationGroup type>
     |      X.timerEvent(a, b)
     |  
     |  totalDuration = <unbound qt slot totalDuration of QAnimationGroup type...
     |      X.totalDuration(a) -> int
     |  
     |  tr = <unbound qt slot tr of QAnimationGroup type>
     |      X.tr(a, b, c, d) -> str
     |  
     |  updateCurrentTime = <unbound qt slot py_q_updateCurrentTime of QAnimat...
     |      X.updateCurrentTime(a, b)
     |  
     |  updateDirection = <unbound qt slot py_q_updateDirection of QAnimationG...
     |      X.updateDirection(a, b)
     |  
     |  updateState = <unbound qt slot py_q_updateState of QAnimationGroup typ...
     |      X.updateState(a, b, c)
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __delattr__(...)
     |      x.__delattr__('name') <==> del x.name
     |  
     |  __eq__(...)
     |      x.__eq__(y) <==> x==y
     |  
     |  __ge__(...)
     |      x.__ge__(y) <==> x>=y
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __gt__(...)
     |      x.__gt__(y) <==> x>y
     |  
     |  __hash__(...)
     |      x.__hash__() <==> hash(x)
     |  
     |  __le__(...)
     |      x.__le__(y) <==> x<=y
     |  
     |  __lt__(...)
     |      x.__lt__(y) <==> x<y
     |  
     |  __ne__(...)
     |      x.__ne__(y) <==> x!=y
     |  
     |  __nonzero__(...)
     |      x.__nonzero__() <==> x != 0
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __setattr__(...)
     |      x.__setattr__('name', value) <==> x.name = value
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __new__ = <built-in method __new__ of PythonQt.PythonQtClassWrapper ob...
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
    
    class QApplicationStateChangeEvent(PythonQt.PythonQtInstanceWrapper)
     |  Method resolution order:
     |      QApplicationStateChangeEvent
     |      PythonQt.PythonQtInstanceWrapper
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  __init__(...)
     |      x.__init__(...) initializes x; see help(type(x)) for signature
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  AcceptDropsChange = 152
     |  
     |  ActionAdded = 114
     |  
     |  ActionChanged = 113
     |  
     |  ActionRemoved = 115
     |  
     |  ActivateControl = 80
     |  
     |  ActivationChange = 99
     |  
     |  ApplicationActivate = 121
     |  
     |  ApplicationActivated = 121
     |  
     |  ApplicationDeactivate = 122
     |  
     |  ApplicationDeactivated = 122
     |  
     |  ApplicationFontChange = 36
     |  
     |  ApplicationLayoutDirectionChange = 37
     |  
     |  ApplicationPaletteChange = 38
     |  
     |  ApplicationStateChange = 214
     |  
     |  ApplicationWindowIconChange = 35
     |  
     |  ChildAdded = 68
     |  
     |  ChildPolished = 69
     |  
     |  ChildRemoved = 71
     |  
     |  Clipboard = 40
     |  
     |  Close = 19
     |  
     |  CloseSoftwareInputPanel = 200
     |  
     |  ContentsRectChange = 178
     |  
     |  ContextMenu = 82
     |  
     |  Create = 15
     |  
     |  CursorChange = 183
     |  
     |  DeactivateControl = 81
     |  
     |  DeferredDelete = 52
     |  
     |  Destroy = 16
     |  
     |  DragEnter = 60
     |  
     |  DragLeave = 62
     |  
     |  DragMove = 61
     |  
     |  DragResponse = 64
     |  
     |  Drop = 63
     |  
     |  DynamicPropertyChange = 170
     |  
     |  EmbeddingControl = 79
     |  
     |  EnabledChange = 98
     |  
     |  Enter = 10
     |  
     |  EnterWhatsThisMode = 124
     |  
     |  Expose = 206
     |  
     |  FileOpen = 116
     |  
     |  FocusAboutToChange = 23
     |  
     |  FocusIn = 8
     |  
     |  FocusOut = 9
     |  
     |  FontChange = 97
     |  
     |  FutureCallOut = 180
     |  
     |  Gesture = 198
     |  
     |  GestureOverride = 202
     |  
     |  GrabKeyboard = 188
     |  
     |  GrabMouse = 186
     |  
     |  GraphicsSceneContextMenu = 159
     |  
     |  GraphicsSceneDragEnter = 164
     |  
     |  GraphicsSceneDragLeave = 166
     |  
     |  GraphicsSceneDragMove = 165
     |  
     |  GraphicsSceneDrop = 167
     |  
     |  GraphicsSceneHelp = 163
     |  
     |  GraphicsSceneHoverEnter = 160
     |  
     |  GraphicsSceneHoverLeave = 162
     |  
     |  GraphicsSceneHoverMove = 161
     |  
     |  GraphicsSceneMouseDoubleClick = 158
     |  
     |  GraphicsSceneMouseMove = 155
     |  
     |  GraphicsSceneMousePress = 156
     |  
     |  GraphicsSceneMouseRelease = 157
     |  
     |  GraphicsSceneMove = 182
     |  
     |  GraphicsSceneResize = 181
     |  
     |  GraphicsSceneWheel = 168
     |  
     |  HelpRequest = 95
     |  
     |  Hide = 18
     |  
     |  HideToParent = 27
     |  
     |  HoverEnter = 127
     |  
     |  HoverLeave = 128
     |  
     |  HoverMove = 129
     |  
     |  IconDrag = 96
     |  
     |  IconTextChange = 101
     |  
     |  InputMethod = 83
     |  
     |  InputMethodQuery = 207
     |  
     |  KeyPress = 6
     |  
     |  KeyRelease = 7
     |  
     |  KeyboardLayoutChange = 169
     |  
     |  LanguageChange = 89
     |  
     |  LayoutDirectionChange = 90
     |  
     |  LayoutRequest = 76
     |  
     |  Leave = 11
     |  
     |  LeaveWhatsThisMode = 125
     |  
     |  LocaleChange = 88
     |  
     |  MacGLClearDrawable = 191
     |  
     |  MacGLWindowChange = 179
     |  
     |  MacSizeChange = 177
     |  
     |  MaxUser = 65535
     |  
     |  MetaCall = 43
     |  
     |  ModifiedChange = 102
     |  
     |  MouseButtonDblClick = 4
     |  
     |  MouseButtonPress = 2
     |  
     |  MouseButtonRelease = 3
     |  
     |  MouseMove = 5
     |  
     |  MouseTrackingChange = 109
     |  
     |  Move = 13
     |  
     |  NativeGesture = 197
     |  
     |  NetworkReplyUpdated = 185
     |  
     |  NonClientAreaMouseButtonDblClick = 176
     |  
     |  NonClientAreaMouseButtonPress = 174
     |  
     |  NonClientAreaMouseButtonRelease = 175
     |  
     |  NonClientAreaMouseMove = 173
     |  
     |  None = 0
     |  
     |  OkRequest = 94
     |  
     |  OrientationChange = 208
     |  
     |  Paint = 12
     |  
     |  PaletteChange = 39
     |  
     |  ParentAboutToChange = 131
     |  
     |  ParentChange = 21
     |  
     |  PlatformPanel = 212
     |  
     |  PlatformSurface = 217
     |  
     |  Polish = 75
     |  
     |  PolishRequest = 74
     |  
     |  QueryWhatsThis = 123
     |  
     |  Quit = 20
     |  
     |  ReadOnlyChange = 106
     |  
     |  RequestSoftwareInputPanel = 199
     |  
     |  Resize = 14
     |  
     |  ScreenChangeInternal = 216
     |  
     |  Scroll = 205
     |  
     |  ScrollPrepare = 204
     |  
     |  Shortcut = 117
     |  
     |  ShortcutOverride = 51
     |  
     |  Show = 17
     |  
     |  ShowToParent = 26
     |  
     |  ShowWindowRequest = 73
     |  
     |  SockAct = 50
     |  
     |  SockClose = 211
     |  
     |  Speech = 42
     |  
     |  StateMachineSignal = 192
     |  
     |  StateMachineWrapped = 193
     |  
     |  StatusTip = 112
     |  
     |  Style = 91
     |  
     |  StyleAnimationUpdate = 213
     |  
     |  StyleChange = 100
     |  
     |  TabletEnterProximity = 171
     |  
     |  TabletLeaveProximity = 172
     |  
     |  TabletMove = 87
     |  
     |  TabletPress = 92
     |  
     |  TabletRelease = 93
     |  
     |  ThemeChange = 210
     |  
     |  ThreadChange = 22
     |  
     |  Timer = 1
     |  
     |  ToolBarChange = 120
     |  
     |  ToolTip = 110
     |  
     |  ToolTipChange = 184
     |  
     |  TouchBegin = 194
     |  
     |  TouchCancel = 209
     |  
     |  TouchEnd = 196
     |  
     |  TouchUpdate = 195
     |  
     |  Type = <class 'PythonQt.QtCore.Type'>
     |  
     |  
     |  UngrabKeyboard = 189
     |  
     |  UngrabMouse = 187
     |  
     |  UpdateLater = 78
     |  
     |  UpdateRequest = 77
     |  
     |  User = 1000
     |  
     |  WhatsThis = 111
     |  
     |  WhatsThisClicked = 118
     |  
     |  Wheel = 31
     |  
     |  WinEventAct = 132
     |  
     |  WinIdChange = 203
     |  
     |  WindowActivate = 24
     |  
     |  WindowBlocked = 103
     |  
     |  WindowChangeInternal = 215
     |  
     |  WindowDeactivate = 25
     |  
     |  WindowIconChange = 34
     |  
     |  WindowStateChange = 105
     |  
     |  WindowTitleChange = 33
     |  
     |  WindowUnblocked = 104
     |  
     |  ZOrderChange = 126
     |  
     |  ZeroTimerEvent = 154
     |  
     |  accept = <unbound qt slot accept of QApplicationStateChangeEvent type>
     |      X.accept(a)
     |  
     |  applicationState = <unbound qt slot applicationState of QApplicationSt...
     |      X.applicationState(a)
     |  
     |  className = <built-in method className of PythonQt.PythonQtClassWrappe...
     |      Return the classname of the object
     |  
     |  delete = <built-in method delete of PythonQt.PythonQtClassWrapper obje...
     |      Deletes the given C++ object
     |  
     |  help = <built-in method help of PythonQt.PythonQtClassWrapper object>
     |      Shows the help of available methods for this class
     |  
     |  ignore = <unbound qt slot ignore of QApplicationStateChangeEvent type>
     |      X.ignore(a)
     |  
     |  inherits = <built-in method inherits of PythonQt.PythonQtClassWrapper ...
     |      Returns if the class inherits or is of given type name
     |  
     |  isAccepted = <unbound qt slot isAccepted of QApplicationStateChangeEve...
     |      X.isAccepted(a) -> bool
     |  
     |  operator_assign = <unbound qt slot operator_assign of QApplicationStat...
     |      X.operator_assign(a, b) -> PythonQt.QtCore.QEvent
     |  
     |  registerEventType = <unbound qt slot static_QEvent_registerEventType o...
     |      X.registerEventType(a) -> int
     |  
     |  setAccepted = <unbound qt slot setAccepted of QApplicationStateChangeE...
     |      X.setAccepted(a, b)
     |  
     |  spontaneous = <unbound qt slot spontaneous of QApplicationStateChangeE...
     |      X.spontaneous(a) -> bool
     |  
     |  type = <unbound qt slot type of QApplicationStateChangeEvent type>
     |      X.type(a)
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __delattr__(...)
     |      x.__delattr__('name') <==> del x.name
     |  
     |  __eq__(...)
     |      x.__eq__(y) <==> x==y
     |  
     |  __ge__(...)
     |      x.__ge__(y) <==> x>=y
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __gt__(...)
     |      x.__gt__(y) <==> x>y
     |  
     |  __hash__(...)
     |      x.__hash__() <==> hash(x)
     |  
     |  __le__(...)
     |      x.__le__(y) <==> x<=y
     |  
     |  __lt__(...)
     |      x.__lt__(y) <==> x<y
     |  
     |  __ne__(...)
     |      x.__ne__(y) <==> x!=y
     |  
     |  __nonzero__(...)
     |      x.__nonzero__() <==> x != 0
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __setattr__(...)
     |      x.__setattr__('name', value) <==> x.name = value
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __new__ = <built-in method __new__ of PythonQt.PythonQtClassWrapper ob...
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
    
    class QBasicMutex(PythonQt.PythonQtInstanceWrapper)
     |  Method resolution order:
     |      QBasicMutex
     |      PythonQt.PythonQtInstanceWrapper
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  __init__(...)
     |      x.__init__(...) initializes x; see help(type(x)) for signature
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  className = <built-in method className of PythonQt.PythonQtClassWrappe...
     |      Return the classname of the object
     |  
     |  delete = <built-in method delete of PythonQt.PythonQtClassWrapper obje...
     |      Deletes the given C++ object
     |  
     |  help = <built-in method help of PythonQt.PythonQtClassWrapper object>
     |      Shows the help of available methods for this class
     |  
     |  inherits = <built-in method inherits of PythonQt.PythonQtClassWrapper ...
     |      Returns if the class inherits or is of given type name
     |  
     |  isRecursive = <unbound qt slot isRecursive of QBasicMutex type>
     |      X.isRecursive(a) -> bool
     |  
     |  lock = <unbound qt slot lock of QBasicMutex type>
     |      X.lock(a)
     |  
     |  tryLock = <unbound qt slot tryLock of QBasicMutex type>
     |      X.tryLock(a) -> bool
     |  
     |  unlock = <unbound qt slot unlock of QBasicMutex type>
     |      X.unlock(a)
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __delattr__(...)
     |      x.__delattr__('name') <==> del x.name
     |  
     |  __eq__(...)
     |      x.__eq__(y) <==> x==y
     |  
     |  __ge__(...)
     |      x.__ge__(y) <==> x>=y
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __gt__(...)
     |      x.__gt__(y) <==> x>y
     |  
     |  __hash__(...)
     |      x.__hash__() <==> hash(x)
     |  
     |  __le__(...)
     |      x.__le__(y) <==> x<=y
     |  
     |  __lt__(...)
     |      x.__lt__(y) <==> x<y
     |  
     |  __ne__(...)
     |      x.__ne__(y) <==> x!=y
     |  
     |  __nonzero__(...)
     |      x.__nonzero__() <==> x != 0
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __setattr__(...)
     |      x.__setattr__('name', value) <==> x.name = value
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __new__ = <built-in method __new__ of PythonQt.PythonQtClassWrapper ob...
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
    
    class QBasicTimer(PythonQt.PythonQtInstanceWrapper)
     |  Method resolution order:
     |      QBasicTimer
     |      PythonQt.PythonQtInstanceWrapper
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  __init__(...)
     |      x.__init__(...) initializes x; see help(type(x)) for signature
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  className = <built-in method className of PythonQt.PythonQtClassWrappe...
     |      Return the classname of the object
     |  
     |  delete = <built-in method delete of PythonQt.PythonQtClassWrapper obje...
     |      Deletes the given C++ object
     |  
     |  help = <built-in method help of PythonQt.PythonQtClassWrapper object>
     |      Shows the help of available methods for this class
     |  
     |  inherits = <built-in method inherits of PythonQt.PythonQtClassWrapper ...
     |      Returns if the class inherits or is of given type name
     |  
     |  isActive = <unbound qt slot isActive of QBasicTimer type>
     |      X.isActive(a) -> bool
     |  
     |  start = <unbound qt slot start of QBasicTimer type>
     |      X.start(a, b, c, d)
     |  
     |  stop = <unbound qt slot stop of QBasicTimer type>
     |      X.stop(a)
     |  
     |  timerId = <unbound qt slot timerId of QBasicTimer type>
     |      X.timerId(a) -> int
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __delattr__(...)
     |      x.__delattr__('name') <==> del x.name
     |  
     |  __eq__(...)
     |      x.__eq__(y) <==> x==y
     |  
     |  __ge__(...)
     |      x.__ge__(y) <==> x>=y
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __gt__(...)
     |      x.__gt__(y) <==> x>y
     |  
     |  __hash__(...)
     |      x.__hash__() <==> hash(x)
     |  
     |  __le__(...)
     |      x.__le__(y) <==> x<=y
     |  
     |  __lt__(...)
     |      x.__lt__(y) <==> x<y
     |  
     |  __ne__(...)
     |      x.__ne__(y) <==> x!=y
     |  
     |  __nonzero__(...)
     |      x.__nonzero__() <==> x != 0
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __setattr__(...)
     |      x.__setattr__('name', value) <==> x.name = value
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __new__ = <built-in method __new__ of PythonQt.PythonQtClassWrapper ob...
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
    
    class QBitArray(PythonQt.PythonQtInstanceWrapper)
     |  Method resolution order:
     |      QBitArray
     |      PythonQt.PythonQtInstanceWrapper
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  __and__(...)
     |      x.__and__(y) <==> x&y
     |  
     |  __eq__(...)
     |      x.__eq__(y) <==> x==y
     |  
     |  __iand__(...)
     |      x.__iand__(y) <==> x&=y
     |  
     |  __init__(...)
     |      x.__init__(...) initializes x; see help(type(x)) for signature
     |  
     |  __invert__(...)
     |      x.__invert__() <==> ~x
     |  
     |  __ior__(...)
     |      x.__ior__(y) <==> x|=y
     |  
     |  __ixor__(...)
     |      x.__ixor__(y) <==> x^=y
     |  
     |  __ne__(...)
     |      x.__ne__(y) <==> x!=y
     |  
     |  __nonzero__(...)
     |      x.__nonzero__() <==> x != 0
     |  
     |  __or__(...)
     |      x.__or__(y) <==> x|y
     |  
     |  __rand__(...)
     |      x.__rand__(y) <==> y&x
     |  
     |  __ror__(...)
     |      x.__ror__(y) <==> y|x
     |  
     |  __rxor__(...)
     |      x.__rxor__(y) <==> y^x
     |  
     |  __xor__(...)
     |      x.__xor__(y) <==> x^y
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  at = <unbound qt slot at of QBitArray type>
     |      X.at(a, b) -> bool
     |  
     |  className = <built-in method className of PythonQt.PythonQtClassWrappe...
     |      Return the classname of the object
     |  
     |  clear = <unbound qt slot clear of QBitArray type>
     |      X.clear(a)
     |  
     |  clearBit = <unbound qt slot clearBit of QBitArray type>
     |      X.clearBit(a, b)
     |  
     |  count = <unbound qt slot count of QBitArray type>
     |      X.count(a, b) -> int
     |  
     |  delete = <built-in method delete of PythonQt.PythonQtClassWrapper obje...
     |      Deletes the given C++ object
     |  
     |  fill = <unbound qt slot fill of QBitArray type>
     |      X.fill(a, b, c, d)
     |  
     |  help = <built-in method help of PythonQt.PythonQtClassWrapper object>
     |      Shows the help of available methods for this class
     |  
     |  inherits = <built-in method inherits of PythonQt.PythonQtClassWrapper ...
     |      Returns if the class inherits or is of given type name
     |  
     |  isEmpty = <unbound qt slot isEmpty of QBitArray type>
     |      X.isEmpty(a) -> bool
     |  
     |  isNull = <unbound qt slot isNull of QBitArray type>
     |      X.isNull(a) -> bool
     |  
     |  operator_assign = <unbound qt slot operator_assign of QBitArray type>
     |      X.operator_assign(a, b) -> PythonQt.QtCore.QBitArray
     |  
     |  readFrom = <unbound qt slot readFrom of QBitArray type>
     |      X.readFrom(a, b)
     |  
     |  resize = <unbound qt slot resize of QBitArray type>
     |      X.resize(a, b)
     |  
     |  setBit = <unbound qt slot setBit of QBitArray type>
     |      X.setBit(a, b, c)
     |  
     |  size = <unbound qt slot size of QBitArray type>
     |      X.size(a) -> int
     |  
     |  swap = <unbound qt slot swap of QBitArray type>
     |      X.swap(a, b)
     |  
     |  testBit = <unbound qt slot testBit of QBitArray type>
     |      X.testBit(a, b) -> bool
     |  
     |  toggleBit = <unbound qt slot toggleBit of QBitArray type>
     |      X.toggleBit(a, b) -> bool
     |  
     |  truncate = <unbound qt slot truncate of QBitArray type>
     |      X.truncate(a, b)
     |  
     |  writeTo = <unbound qt slot writeTo of QBitArray type>
     |      X.writeTo(a, b)
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __delattr__(...)
     |      x.__delattr__('name') <==> del x.name
     |  
     |  __ge__(...)
     |      x.__ge__(y) <==> x>=y
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __gt__(...)
     |      x.__gt__(y) <==> x>y
     |  
     |  __hash__(...)
     |      x.__hash__() <==> hash(x)
     |  
     |  __le__(...)
     |      x.__le__(y) <==> x<=y
     |  
     |  __lt__(...)
     |      x.__lt__(y) <==> x<y
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __setattr__(...)
     |      x.__setattr__('name', value) <==> x.name = value
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __new__ = <built-in method __new__ of PythonQt.PythonQtClassWrapper ob...
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
    
    class QBuffer(PythonQt.PythonQtInstanceWrapper)
     |  Method resolution order:
     |      QBuffer
     |      PythonQt.PythonQtInstanceWrapper
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  __init__(...)
     |      x.__init__(...) initializes x; see help(type(x)) for signature
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  Append = 4
     |  
     |  NotOpen = 0
     |  
     |  OpenMode = <class 'PythonQt.QtCore.OpenMode'>
     |  
     |  
     |  OpenModeFlag = <class 'PythonQt.QtCore.OpenModeFlag'>
     |  
     |  
     |  ReadOnly = 1
     |  
     |  ReadWrite = 3
     |  
     |  Text = 16
     |  
     |  Truncate = 8
     |  
     |  Unbuffered = 32
     |  
     |  WriteOnly = 2
     |  
     |  aboutToClose = <unbound qt signal aboutToClose of QBuffer type>
     |  
     |  
     |  atEnd = <unbound qt slot py_q_atEnd of QBuffer type>
     |      X.atEnd(a) -> bool
     |  
     |  blockSignals = <unbound qt slot blockSignals of QBuffer type>
     |      X.blockSignals(a, b) -> bool
     |  
     |  buffer = <unbound qt slot buffer of QBuffer type>
     |      X.buffer(a) -> PythonQt.QtCore.QByteArray
     |  
     |  bytesAvailable = <unbound qt slot py_q_bytesAvailable of QBuffer type>
     |      X.bytesAvailable(a) -> int
     |  
     |  bytesToWrite = <unbound qt slot py_q_bytesToWrite of QBuffer type>
     |      X.bytesToWrite(a) -> int
     |  
     |  bytesWritten = <unbound qt signal bytesWritten of QBuffer type>
     |  
     |  
     |  canReadLine = <unbound qt slot py_q_canReadLine of QBuffer type>
     |      X.canReadLine(a) -> bool
     |  
     |  channelBytesWritten = <unbound qt signal channelBytesWritten of QBuffe...
     |  
     |  
     |  channelReadyRead = <unbound qt signal channelReadyRead of QBuffer type...
     |  
     |  
     |  childEvent = <unbound qt slot py_q_childEvent of QBuffer type>
     |      X.childEvent(a, b)
     |  
     |  children = <unbound qt slot children of QBuffer type>
     |      X.children(a) -> tuple
     |  
     |  className = <built-in method className of PythonQt.PythonQtClassWrappe...
     |      Return the classname of the object
     |  
     |  close = <unbound qt slot py_q_close of QBuffer type>
     |      X.close(a)
     |  
     |  connect = <unbound qt slot connect of QBuffer type>
     |      X.connect(a, b, c, d, e) -> bool
     |  
     |  connectNotify = <unbound qt slot connectNotify of QBuffer type>
     |      X.connectNotify(a, b)
     |  
     |  customEvent = <unbound qt slot py_q_customEvent of QBuffer type>
     |      X.customEvent(a, b)
     |  
     |  data = <unbound qt slot data of QBuffer type>
     |      X.data(a) -> PythonQt.QtCore.QByteArray
     |  
     |  delete = <built-in method delete of PythonQt.PythonQtClassWrapper obje...
     |      Deletes the given C++ object
     |  
     |  deleteLater = <unbound qt slot deleteLater of QBuffer type>
     |      X.deleteLater()
     |  
     |  destroyed = <unbound qt signal destroyed of QBuffer type>
     |  
     |  
     |  disconnect = <unbound qt slot disconnect of QBuffer type>
     |      X.disconnect(a, b, c, d) -> bool
     |  
     |  disconnectNotify = <unbound qt slot disconnectNotify of QBuffer type>
     |      X.disconnectNotify(a, b)
     |  
     |  dumpObjectInfo = <unbound qt slot dumpObjectInfo of QBuffer type>
     |      X.dumpObjectInfo(a)
     |  
     |  dumpObjectTree = <unbound qt slot dumpObjectTree of QBuffer type>
     |      X.dumpObjectTree(a)
     |  
     |  dynamicPropertyNames = <unbound qt slot dynamicPropertyNames of QBuffe...
     |      X.dynamicPropertyNames(a)
     |  
     |  errorString = <unbound qt slot errorString of QBuffer type>
     |      X.errorString(a) -> str
     |  
     |  event = <unbound qt slot py_q_event of QBuffer type>
     |      X.event(a, b) -> bool
     |  
     |  eventFilter = <unbound qt slot py_q_eventFilter of QBuffer type>
     |      X.eventFilter(a, b, c) -> bool
     |  
     |  findChild = <unbound qt slot findChild of QBuffer type>
     |      X.findChild(a, b, c) -> PythonQt.private.QObject
     |  
     |  findChildren = <unbound qt slot findChildren of QBuffer type>
     |      X.findChildren(a, b, c) -> tuple
     |  
     |  getChar = <unbound qt slot getChar of QBuffer type>
     |      X.getChar(a, b) -> bool
     |  
     |  help = <built-in method help of PythonQt.PythonQtClassWrapper object>
     |      Shows the help of available methods for this class
     |  
     |  inherits = <built-in method inherits of PythonQt.PythonQtClassWrapper ...
     |      Returns if the class inherits or is of given type name
     |  
     |  installEventFilter = <unbound qt slot installEventFilter of QBuffer ty...
     |      X.installEventFilter(a, b)
     |  
     |  isOpen = <unbound qt slot isOpen of QBuffer type>
     |      X.isOpen(a) -> bool
     |  
     |  isReadable = <unbound qt slot isReadable of QBuffer type>
     |      X.isReadable(a) -> bool
     |  
     |  isSequential = <unbound qt slot py_q_isSequential of QBuffer type>
     |      X.isSequential(a) -> bool
     |  
     |  isSignalConnected = <unbound qt slot isSignalConnected of QBuffer type...
     |      X.isSignalConnected(a, b) -> bool
     |  
     |  isTextModeEnabled = <unbound qt slot isTextModeEnabled of QBuffer type...
     |      X.isTextModeEnabled(a) -> bool
     |  
     |  isWidgetType = <unbound qt slot isWidgetType of QBuffer type>
     |      X.isWidgetType(a) -> bool
     |  
     |  isWindowType = <unbound qt slot isWindowType of QBuffer type>
     |      X.isWindowType(a) -> bool
     |  
     |  isWritable = <unbound qt slot isWritable of QBuffer type>
     |      X.isWritable(a) -> bool
     |  
     |  killTimer = <unbound qt slot killTimer of QBuffer type>
     |      X.killTimer(a, b)
     |  
     |  metaObject = <unbound qt slot metaObject of QBuffer type>
     |      X.metaObject(a) -> PythonQt.QtCore.QMetaObject
     |  
     |  moveToThread = <unbound qt slot moveToThread of QBuffer type>
     |      X.moveToThread(a, b)
     |  
     |  objectName = None
     |  
     |  objectNameChanged = <unbound qt signal objectNameChanged of QBuffer ty...
     |  
     |  
     |  open = <unbound qt slot py_q_open of QBuffer type>
     |      X.open(a, b) -> bool
     |  
     |  openMode = <unbound qt slot openMode of QBuffer type>
     |      X.openMode(a)
     |  
     |  parent = <unbound qt slot parent of QBuffer type>
     |      X.parent(a) -> PythonQt.private.QObject
     |  
     |  peek = <unbound qt slot peek of QBuffer type>
     |      X.peek(a, b) -> PythonQt.QtCore.QByteArray
     |  
     |  pos = <unbound qt slot py_q_pos of QBuffer type>
     |      X.pos(a) -> int
     |  
     |  property = <unbound qt slot property of QBuffer type>
     |      X.property(a, b) -> object
     |  
     |  putChar = <unbound qt slot putChar of QBuffer type>
     |      X.putChar(a, b) -> bool
     |  
     |  read = <unbound qt slot read of QBuffer type>
     |      X.read(a, b) -> PythonQt.QtCore.QByteArray
     |  
     |  readAll = <unbound qt slot readAll of QBuffer type>
     |      X.readAll(a) -> PythonQt.QtCore.QByteArray
     |  
     |  readChannelFinished = <unbound qt signal readChannelFinished of QBuffe...
     |  
     |  
     |  readData = <unbound qt slot py_q_readData of QBuffer type>
     |      X.readData(a, b, c) -> int
     |  
     |  readLine = <unbound qt slot readLine of QBuffer type>
     |      X.readLine(a, b) -> PythonQt.QtCore.QByteArray
     |  
     |  readLineData = <unbound qt slot py_q_readLineData of QBuffer type>
     |      X.readLineData(a, b, c) -> int
     |  
     |  readyRead = <unbound qt signal readyRead of QBuffer type>
     |  
     |  
     |  removeEventFilter = <unbound qt slot removeEventFilter of QBuffer type...
     |      X.removeEventFilter(a, b)
     |  
     |  reset = <unbound qt slot py_q_reset of QBuffer type>
     |      X.reset(a) -> bool
     |  
     |  seek = <unbound qt slot py_q_seek of QBuffer type>
     |      X.seek(a, b) -> bool
     |  
     |  sender = <unbound qt slot sender of QBuffer type>
     |      X.sender(a) -> PythonQt.private.QObject
     |  
     |  senderSignalIndex = <unbound qt slot senderSignalIndex of QBuffer type...
     |      X.senderSignalIndex(a) -> int
     |  
     |  setBuffer = <unbound qt slot setBuffer of QBuffer type>
     |      X.setBuffer(a, b)
     |  
     |  setData = <unbound qt slot setData of QBuffer type>
     |      X.setData(a, b)
     |  
     |  setErrorString = <unbound qt slot setErrorString of QBuffer type>
     |      X.setErrorString(a, b)
     |  
     |  setObjectName = <unbound qt slot setObjectName of QBuffer type>
     |      X.setObjectName(a, b)
     |  
     |  setOpenMode = <unbound qt slot setOpenMode of QBuffer type>
     |      X.setOpenMode(a, b)
     |  
     |  setParent = <unbound qt slot setParent of QBuffer type>
     |      X.setParent(a, b)
     |  
     |  setProperty = <unbound qt slot setProperty of QBuffer type>
     |      X.setProperty(a, b, c) -> bool
     |  
     |  setTextModeEnabled = <unbound qt slot setTextModeEnabled of QBuffer ty...
     |      X.setTextModeEnabled(a, b)
     |  
     |  signalsBlocked = <unbound qt slot signalsBlocked of QBuffer type>
     |      X.signalsBlocked(a) -> bool
     |  
     |  size = <unbound qt slot py_q_size of QBuffer type>
     |      X.size(a) -> int
     |  
     |  startTimer = <unbound qt slot startTimer of QBuffer type>
     |      X.startTimer(a, b, c) -> int
     |  
     |  thread = <unbound qt slot thread of QBuffer type>
     |      X.thread(a)
     |  
     |  timerEvent = <unbound qt slot py_q_timerEvent of QBuffer type>
     |      X.timerEvent(a, b)
     |  
     |  tr = <unbound qt slot tr of QBuffer type>
     |      X.tr(a, b, c, d) -> str
     |  
     |  ungetChar = <unbound qt slot ungetChar of QBuffer type>
     |      X.ungetChar(a, b)
     |  
     |  waitForBytesWritten = <unbound qt slot py_q_waitForBytesWritten of QBu...
     |      X.waitForBytesWritten(a, b) -> bool
     |  
     |  waitForReadyRead = <unbound qt slot py_q_waitForReadyRead of QBuffer t...
     |      X.waitForReadyRead(a, b) -> bool
     |  
     |  write = <unbound qt slot write of QBuffer type>
     |      X.write(a, b) -> int
     |  
     |  writeData = <unbound qt slot py_q_writeData of QBuffer type>
     |      X.writeData(a, b, c) -> int
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __delattr__(...)
     |      x.__delattr__('name') <==> del x.name
     |  
     |  __eq__(...)
     |      x.__eq__(y) <==> x==y
     |  
     |  __ge__(...)
     |      x.__ge__(y) <==> x>=y
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __gt__(...)
     |      x.__gt__(y) <==> x>y
     |  
     |  __hash__(...)
     |      x.__hash__() <==> hash(x)
     |  
     |  __le__(...)
     |      x.__le__(y) <==> x<=y
     |  
     |  __lt__(...)
     |      x.__lt__(y) <==> x<y
     |  
     |  __ne__(...)
     |      x.__ne__(y) <==> x!=y
     |  
     |  __nonzero__(...)
     |      x.__nonzero__() <==> x != 0
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __setattr__(...)
     |      x.__setattr__('name', value) <==> x.name = value
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __new__ = <built-in method __new__ of PythonQt.PythonQtClassWrapper ob...
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
    
    class QByteArray(PythonQt.PythonQtInstanceWrapper)
     |  Method resolution order:
     |      QByteArray
     |      PythonQt.PythonQtInstanceWrapper
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  __add__(...)
     |      x.__add__(y) <==> x+y
     |  
     |  __eq__(...)
     |      x.__eq__(y) <==> x==y
     |  
     |  __ge__(...)
     |      x.__ge__(y) <==> x>=y
     |  
     |  __gt__(...)
     |      x.__gt__(y) <==> x>y
     |  
     |  __iadd__(...)
     |      x.__iadd__(y) <==> x+=y
     |  
     |  __init__(...)
     |      x.__init__(...) initializes x; see help(type(x)) for signature
     |  
     |  __le__(...)
     |      x.__le__(y) <==> x<=y
     |  
     |  __lt__(...)
     |      x.__lt__(y) <==> x<y
     |  
     |  __nonzero__(...)
     |      x.__nonzero__() <==> x != 0
     |  
     |  __radd__(...)
     |      x.__radd__(y) <==> y+x
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  Base64Encoding = 0
     |  
     |  Base64Option = <class 'PythonQt.QtCore.Base64Option'>
     |  
     |  
     |  Base64Options = <class 'PythonQt.QtCore.Base64Options'>
     |  
     |  
     |  Base64UrlEncoding = 1
     |  
     |  KeepTrailingEquals = 0
     |  
     |  OmitTrailingEquals = 2
     |  
     |  append = <unbound qt slot append of QByteArray type>
     |      X.append(a, b, c) -> PythonQt.QtCore.QByteArray
     |  
     |  at = <unbound qt slot at of QByteArray type>
     |      X.at(a, b) -> int
     |  
     |  capacity = <unbound qt slot capacity of QByteArray type>
     |      X.capacity(a) -> int
     |  
     |  cbegin = <unbound qt slot cbegin of QByteArray type>
     |      X.cbegin(a) -> int
     |  
     |  cend = <unbound qt slot cend of QByteArray type>
     |      X.cend(a) -> int
     |  
     |  chop = <unbound qt slot chop of QByteArray type>
     |      X.chop(a, b)
     |  
     |  className = <built-in method className of PythonQt.PythonQtClassWrappe...
     |      Return the classname of the object
     |  
     |  clear = <unbound qt slot clear of QByteArray type>
     |      X.clear(a)
     |  
     |  contains = <unbound qt slot contains of QByteArray type>
     |      X.contains(a, b) -> bool
     |  
     |  count = <unbound qt slot count of QByteArray type>
     |      X.count(a, b) -> int
     |  
     |  data = <unbound qt slot data of QByteArray type>
     |      X.data(a)
     |  
     |  delete = <built-in method delete of PythonQt.PythonQtClassWrapper obje...
     |      Deletes the given C++ object
     |  
     |  endsWith = <unbound qt slot endsWith of QByteArray type>
     |      X.endsWith(a, b) -> bool
     |  
     |  fill = <unbound qt slot fill of QByteArray type>
     |      X.fill(a, b, c) -> PythonQt.QtCore.QByteArray
     |  
     |  fromBase64 = <unbound qt slot static_QByteArray_fromBase64 of QByteArr...
     |      X.fromBase64(a, b) -> PythonQt.QtCore.QByteArray
     |  
     |  fromHex = <unbound qt slot static_QByteArray_fromHex of QByteArray typ...
     |      X.fromHex(a) -> PythonQt.QtCore.QByteArray
     |  
     |  fromPercentEncoding = <unbound qt slot static_QByteArray_fromPercentEn...
     |      X.fromPercentEncoding(a, b) -> PythonQt.QtCore.QByteArray
     |  
     |  help = <built-in method help of PythonQt.PythonQtClassWrapper object>
     |      Shows the help of available methods for this class
     |  
     |  indexOf = <unbound qt slot indexOf of QByteArray type>
     |      X.indexOf(a, b, c) -> int
     |  
     |  inherits = <built-in method inherits of PythonQt.PythonQtClassWrapper ...
     |      Returns if the class inherits or is of given type name
     |  
     |  insert = <unbound qt slot insert of QByteArray type>
     |      X.insert(a, b, c, d) -> PythonQt.QtCore.QByteArray
     |  
     |  isEmpty = <unbound qt slot isEmpty of QByteArray type>
     |      X.isEmpty(a) -> bool
     |  
     |  isNull = <unbound qt slot isNull of QByteArray type>
     |      X.isNull(a) -> bool
     |  
     |  isSharedWith = <unbound qt slot isSharedWith of QByteArray type>
     |      X.isSharedWith(a, b) -> bool
     |  
     |  lastIndexOf = <unbound qt slot lastIndexOf of QByteArray type>
     |      X.lastIndexOf(a, b, c) -> int
     |  
     |  left = <unbound qt slot left of QByteArray type>
     |      X.left(a, b) -> PythonQt.QtCore.QByteArray
     |  
     |  leftJustified = <unbound qt slot leftJustified of QByteArray type>
     |      X.leftJustified(a, b, c, d) -> PythonQt.QtCore.QByteArray
     |  
     |  length = <unbound qt slot length of QByteArray type>
     |      X.length(a) -> int
     |  
     |  mid = <unbound qt slot mid of QByteArray type>
     |      X.mid(a, b, c) -> PythonQt.QtCore.QByteArray
     |  
     |  number = <unbound qt slot static_QByteArray_number of QByteArray type>
     |      X.number(a, b, c) -> PythonQt.QtCore.QByteArray
     |  
     |  operator_assign = <unbound qt slot operator_assign of QByteArray type>
     |      X.operator_assign(a, b) -> PythonQt.QtCore.QByteArray
     |  
     |  prepend = <unbound qt slot prepend of QByteArray type>
     |      X.prepend(a, b, c) -> PythonQt.QtCore.QByteArray
     |  
     |  push_back = <unbound qt slot push_back of QByteArray type>
     |      X.push_back(a, b)
     |  
     |  push_front = <unbound qt slot push_front of QByteArray type>
     |      X.push_front(a, b)
     |  
     |  readFrom = <unbound qt slot readFrom of QByteArray type>
     |      X.readFrom(a, b)
     |  
     |  remove = <unbound qt slot remove of QByteArray type>
     |      X.remove(a, b, c) -> PythonQt.QtCore.QByteArray
     |  
     |  repeated = <unbound qt slot repeated of QByteArray type>
     |      X.repeated(a, b) -> PythonQt.QtCore.QByteArray
     |  
     |  replace = <unbound qt slot replace of QByteArray type>
     |      X.replace(a, b, c, d, e) -> PythonQt.QtCore.QByteArray
     |  
     |  reserve = <unbound qt slot reserve of QByteArray type>
     |      X.reserve(a, b)
     |  
     |  resize = <unbound qt slot resize of QByteArray type>
     |      X.resize(a, b)
     |  
     |  right = <unbound qt slot right of QByteArray type>
     |      X.right(a, b) -> PythonQt.QtCore.QByteArray
     |  
     |  rightJustified = <unbound qt slot rightJustified of QByteArray type>
     |      X.rightJustified(a, b, c, d) -> PythonQt.QtCore.QByteArray
     |  
     |  setNum = <unbound qt slot setNum of QByteArray type>
     |      X.setNum(a, b, c, d) -> PythonQt.QtCore.QByteArray
     |  
     |  setRawData = <unbound qt slot setRawData of QByteArray type>
     |      X.setRawData(a, b, c) -> PythonQt.QtCore.QByteArray
     |  
     |  simplified = <unbound qt slot simplified of QByteArray type>
     |      X.simplified(a) -> PythonQt.QtCore.QByteArray
     |  
     |  size = <unbound qt slot size of QByteArray type>
     |      X.size(a) -> int
     |  
     |  split = <unbound qt slot split of QByteArray type>
     |      X.split(a, b)
     |  
     |  squeeze = <unbound qt slot squeeze of QByteArray type>
     |      X.squeeze(a)
     |  
     |  startsWith = <unbound qt slot startsWith of QByteArray type>
     |      X.startsWith(a, b) -> bool
     |  
     |  swap = <unbound qt slot swap of QByteArray type>
     |      X.swap(a, b)
     |  
     |  toBase64 = <unbound qt slot toBase64 of QByteArray type>
     |      X.toBase64(a, b) -> PythonQt.QtCore.QByteArray
     |  
     |  toDouble = <unbound qt slot toDouble of QByteArray type>
     |      X.toDouble(a, b) -> float
     |  
     |  toFloat = <unbound qt slot toFloat of QByteArray type>
     |      X.toFloat(a, b) -> float
     |  
     |  toHex = <unbound qt slot toHex of QByteArray type>
     |      X.toHex(a) -> PythonQt.QtCore.QByteArray
     |  
     |  toInt = <unbound qt slot toInt of QByteArray type>
     |      X.toInt(a, b, c) -> int
     |  
     |  toLower = <unbound qt slot toLower of QByteArray type>
     |      X.toLower(a) -> PythonQt.QtCore.QByteArray
     |  
     |  toPercentEncoding = <unbound qt slot toPercentEncoding of QByteArray t...
     |      X.toPercentEncoding(a, b, c, d) -> PythonQt.QtCore.QByteArray
     |  
     |  toUShort = <unbound qt slot toUShort of QByteArray type>
     |      X.toUShort(a, b, c) -> int
     |  
     |  toUpper = <unbound qt slot toUpper of QByteArray type>
     |      X.toUpper(a) -> PythonQt.QtCore.QByteArray
     |  
     |  trimmed = <unbound qt slot trimmed of QByteArray type>
     |      X.trimmed(a) -> PythonQt.QtCore.QByteArray
     |  
     |  truncate = <unbound qt slot truncate of QByteArray type>
     |      X.truncate(a, b)
     |  
     |  writeTo = <unbound qt slot writeTo of QByteArray type>
     |      X.writeTo(a, b)
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __delattr__(...)
     |      x.__delattr__('name') <==> del x.name
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __hash__(...)
     |      x.__hash__() <==> hash(x)
     |  
     |  __ne__(...)
     |      x.__ne__(y) <==> x!=y
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __setattr__(...)
     |      x.__setattr__('name', value) <==> x.name = value
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __new__ = <built-in method __new__ of PythonQt.PythonQtClassWrapper ob...
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
    
    class QByteArrayMatcher(PythonQt.PythonQtInstanceWrapper)
     |  Method resolution order:
     |      QByteArrayMatcher
     |      PythonQt.PythonQtInstanceWrapper
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  __init__(...)
     |      x.__init__(...) initializes x; see help(type(x)) for signature
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  className = <built-in method className of PythonQt.PythonQtClassWrappe...
     |      Return the classname of the object
     |  
     |  delete = <built-in method delete of PythonQt.PythonQtClassWrapper obje...
     |      Deletes the given C++ object
     |  
     |  help = <built-in method help of PythonQt.PythonQtClassWrapper object>
     |      Shows the help of available methods for this class
     |  
     |  indexIn = <unbound qt slot indexIn of QByteArrayMatcher type>
     |      X.indexIn(a, b, c, d) -> int
     |  
     |  inherits = <built-in method inherits of PythonQt.PythonQtClassWrapper ...
     |      Returns if the class inherits or is of given type name
     |  
     |  pattern = <unbound qt slot pattern of QByteArrayMatcher type>
     |      X.pattern(a) -> PythonQt.QtCore.QByteArray
     |  
     |  setPattern = <unbound qt slot setPattern of QByteArrayMatcher type>
     |      X.setPattern(a, b)
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __delattr__(...)
     |      x.__delattr__('name') <==> del x.name
     |  
     |  __eq__(...)
     |      x.__eq__(y) <==> x==y
     |  
     |  __ge__(...)
     |      x.__ge__(y) <==> x>=y
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __gt__(...)
     |      x.__gt__(y) <==> x>y
     |  
     |  __hash__(...)
     |      x.__hash__() <==> hash(x)
     |  
     |  __le__(...)
     |      x.__le__(y) <==> x<=y
     |  
     |  __lt__(...)
     |      x.__lt__(y) <==> x<y
     |  
     |  __ne__(...)
     |      x.__ne__(y) <==> x!=y
     |  
     |  __nonzero__(...)
     |      x.__nonzero__() <==> x != 0
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __setattr__(...)
     |      x.__setattr__('name', value) <==> x.name = value
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __new__ = <built-in method __new__ of PythonQt.PythonQtClassWrapper ob...
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
    
    class QChildEvent(PythonQt.PythonQtInstanceWrapper)
     |  Method resolution order:
     |      QChildEvent
     |      PythonQt.PythonQtInstanceWrapper
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  __init__(...)
     |      x.__init__(...) initializes x; see help(type(x)) for signature
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  AcceptDropsChange = 152
     |  
     |  ActionAdded = 114
     |  
     |  ActionChanged = 113
     |  
     |  ActionRemoved = 115
     |  
     |  ActivateControl = 80
     |  
     |  ActivationChange = 99
     |  
     |  ApplicationActivate = 121
     |  
     |  ApplicationActivated = 121
     |  
     |  ApplicationDeactivate = 122
     |  
     |  ApplicationDeactivated = 122
     |  
     |  ApplicationFontChange = 36
     |  
     |  ApplicationLayoutDirectionChange = 37
     |  
     |  ApplicationPaletteChange = 38
     |  
     |  ApplicationStateChange = 214
     |  
     |  ApplicationWindowIconChange = 35
     |  
     |  ChildAdded = 68
     |  
     |  ChildPolished = 69
     |  
     |  ChildRemoved = 71
     |  
     |  Clipboard = 40
     |  
     |  Close = 19
     |  
     |  CloseSoftwareInputPanel = 200
     |  
     |  ContentsRectChange = 178
     |  
     |  ContextMenu = 82
     |  
     |  Create = 15
     |  
     |  CursorChange = 183
     |  
     |  DeactivateControl = 81
     |  
     |  DeferredDelete = 52
     |  
     |  Destroy = 16
     |  
     |  DragEnter = 60
     |  
     |  DragLeave = 62
     |  
     |  DragMove = 61
     |  
     |  DragResponse = 64
     |  
     |  Drop = 63
     |  
     |  DynamicPropertyChange = 170
     |  
     |  EmbeddingControl = 79
     |  
     |  EnabledChange = 98
     |  
     |  Enter = 10
     |  
     |  EnterWhatsThisMode = 124
     |  
     |  Expose = 206
     |  
     |  FileOpen = 116
     |  
     |  FocusAboutToChange = 23
     |  
     |  FocusIn = 8
     |  
     |  FocusOut = 9
     |  
     |  FontChange = 97
     |  
     |  FutureCallOut = 180
     |  
     |  Gesture = 198
     |  
     |  GestureOverride = 202
     |  
     |  GrabKeyboard = 188
     |  
     |  GrabMouse = 186
     |  
     |  GraphicsSceneContextMenu = 159
     |  
     |  GraphicsSceneDragEnter = 164
     |  
     |  GraphicsSceneDragLeave = 166
     |  
     |  GraphicsSceneDragMove = 165
     |  
     |  GraphicsSceneDrop = 167
     |  
     |  GraphicsSceneHelp = 163
     |  
     |  GraphicsSceneHoverEnter = 160
     |  
     |  GraphicsSceneHoverLeave = 162
     |  
     |  GraphicsSceneHoverMove = 161
     |  
     |  GraphicsSceneMouseDoubleClick = 158
     |  
     |  GraphicsSceneMouseMove = 155
     |  
     |  GraphicsSceneMousePress = 156
     |  
     |  GraphicsSceneMouseRelease = 157
     |  
     |  GraphicsSceneMove = 182
     |  
     |  GraphicsSceneResize = 181
     |  
     |  GraphicsSceneWheel = 168
     |  
     |  HelpRequest = 95
     |  
     |  Hide = 18
     |  
     |  HideToParent = 27
     |  
     |  HoverEnter = 127
     |  
     |  HoverLeave = 128
     |  
     |  HoverMove = 129
     |  
     |  IconDrag = 96
     |  
     |  IconTextChange = 101
     |  
     |  InputMethod = 83
     |  
     |  InputMethodQuery = 207
     |  
     |  KeyPress = 6
     |  
     |  KeyRelease = 7
     |  
     |  KeyboardLayoutChange = 169
     |  
     |  LanguageChange = 89
     |  
     |  LayoutDirectionChange = 90
     |  
     |  LayoutRequest = 76
     |  
     |  Leave = 11
     |  
     |  LeaveWhatsThisMode = 125
     |  
     |  LocaleChange = 88
     |  
     |  MacGLClearDrawable = 191
     |  
     |  MacGLWindowChange = 179
     |  
     |  MacSizeChange = 177
     |  
     |  MaxUser = 65535
     |  
     |  MetaCall = 43
     |  
     |  ModifiedChange = 102
     |  
     |  MouseButtonDblClick = 4
     |  
     |  MouseButtonPress = 2
     |  
     |  MouseButtonRelease = 3
     |  
     |  MouseMove = 5
     |  
     |  MouseTrackingChange = 109
     |  
     |  Move = 13
     |  
     |  NativeGesture = 197
     |  
     |  NetworkReplyUpdated = 185
     |  
     |  NonClientAreaMouseButtonDblClick = 176
     |  
     |  NonClientAreaMouseButtonPress = 174
     |  
     |  NonClientAreaMouseButtonRelease = 175
     |  
     |  NonClientAreaMouseMove = 173
     |  
     |  None = 0
     |  
     |  OkRequest = 94
     |  
     |  OrientationChange = 208
     |  
     |  Paint = 12
     |  
     |  PaletteChange = 39
     |  
     |  ParentAboutToChange = 131
     |  
     |  ParentChange = 21
     |  
     |  PlatformPanel = 212
     |  
     |  PlatformSurface = 217
     |  
     |  Polish = 75
     |  
     |  PolishRequest = 74
     |  
     |  QueryWhatsThis = 123
     |  
     |  Quit = 20
     |  
     |  ReadOnlyChange = 106
     |  
     |  RequestSoftwareInputPanel = 199
     |  
     |  Resize = 14
     |  
     |  ScreenChangeInternal = 216
     |  
     |  Scroll = 205
     |  
     |  ScrollPrepare = 204
     |  
     |  Shortcut = 117
     |  
     |  ShortcutOverride = 51
     |  
     |  Show = 17
     |  
     |  ShowToParent = 26
     |  
     |  ShowWindowRequest = 73
     |  
     |  SockAct = 50
     |  
     |  SockClose = 211
     |  
     |  Speech = 42
     |  
     |  StateMachineSignal = 192
     |  
     |  StateMachineWrapped = 193
     |  
     |  StatusTip = 112
     |  
     |  Style = 91
     |  
     |  StyleAnimationUpdate = 213
     |  
     |  StyleChange = 100
     |  
     |  TabletEnterProximity = 171
     |  
     |  TabletLeaveProximity = 172
     |  
     |  TabletMove = 87
     |  
     |  TabletPress = 92
     |  
     |  TabletRelease = 93
     |  
     |  ThemeChange = 210
     |  
     |  ThreadChange = 22
     |  
     |  Timer = 1
     |  
     |  ToolBarChange = 120
     |  
     |  ToolTip = 110
     |  
     |  ToolTipChange = 184
     |  
     |  TouchBegin = 194
     |  
     |  TouchCancel = 209
     |  
     |  TouchEnd = 196
     |  
     |  TouchUpdate = 195
     |  
     |  Type = <class 'PythonQt.QtCore.Type'>
     |  
     |  
     |  UngrabKeyboard = 189
     |  
     |  UngrabMouse = 187
     |  
     |  UpdateLater = 78
     |  
     |  UpdateRequest = 77
     |  
     |  User = 1000
     |  
     |  WhatsThis = 111
     |  
     |  WhatsThisClicked = 118
     |  
     |  Wheel = 31
     |  
     |  WinEventAct = 132
     |  
     |  WinIdChange = 203
     |  
     |  WindowActivate = 24
     |  
     |  WindowBlocked = 103
     |  
     |  WindowChangeInternal = 215
     |  
     |  WindowDeactivate = 25
     |  
     |  WindowIconChange = 34
     |  
     |  WindowStateChange = 105
     |  
     |  WindowTitleChange = 33
     |  
     |  WindowUnblocked = 104
     |  
     |  ZOrderChange = 126
     |  
     |  ZeroTimerEvent = 154
     |  
     |  accept = <unbound qt slot accept of QChildEvent type>
     |      X.accept(a)
     |  
     |  added = <unbound qt slot added of QChildEvent type>
     |      X.added(a) -> bool
     |  
     |  child = <unbound qt slot child of QChildEvent type>
     |      X.child(a) -> PythonQt.private.QObject
     |  
     |  className = <built-in method className of PythonQt.PythonQtClassWrappe...
     |      Return the classname of the object
     |  
     |  delete = <built-in method delete of PythonQt.PythonQtClassWrapper obje...
     |      Deletes the given C++ object
     |  
     |  help = <built-in method help of PythonQt.PythonQtClassWrapper object>
     |      Shows the help of available methods for this class
     |  
     |  ignore = <unbound qt slot ignore of QChildEvent type>
     |      X.ignore(a)
     |  
     |  inherits = <built-in method inherits of PythonQt.PythonQtClassWrapper ...
     |      Returns if the class inherits or is of given type name
     |  
     |  isAccepted = <unbound qt slot isAccepted of QChildEvent type>
     |      X.isAccepted(a) -> bool
     |  
     |  operator_assign = <unbound qt slot operator_assign of QChildEvent type...
     |      X.operator_assign(a, b) -> PythonQt.QtCore.QEvent
     |  
     |  polished = <unbound qt slot polished of QChildEvent type>
     |      X.polished(a) -> bool
     |  
     |  registerEventType = <unbound qt slot static_QEvent_registerEventType o...
     |      X.registerEventType(a) -> int
     |  
     |  removed = <unbound qt slot removed of QChildEvent type>
     |      X.removed(a) -> bool
     |  
     |  setAccepted = <unbound qt slot setAccepted of QChildEvent type>
     |      X.setAccepted(a, b)
     |  
     |  spontaneous = <unbound qt slot spontaneous of QChildEvent type>
     |      X.spontaneous(a) -> bool
     |  
     |  type = <unbound qt slot type of QChildEvent type>
     |      X.type(a)
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __delattr__(...)
     |      x.__delattr__('name') <==> del x.name
     |  
     |  __eq__(...)
     |      x.__eq__(y) <==> x==y
     |  
     |  __ge__(...)
     |      x.__ge__(y) <==> x>=y
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __gt__(...)
     |      x.__gt__(y) <==> x>y
     |  
     |  __hash__(...)
     |      x.__hash__() <==> hash(x)
     |  
     |  __le__(...)
     |      x.__le__(y) <==> x<=y
     |  
     |  __lt__(...)
     |      x.__lt__(y) <==> x<y
     |  
     |  __ne__(...)
     |      x.__ne__(y) <==> x!=y
     |  
     |  __nonzero__(...)
     |      x.__nonzero__() <==> x != 0
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __setattr__(...)
     |      x.__setattr__('name', value) <==> x.name = value
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __new__ = <built-in method __new__ of PythonQt.PythonQtClassWrapper ob...
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
    
    class QCollator(PythonQt.PythonQtInstanceWrapper)
     |  Method resolution order:
     |      QCollator
     |      PythonQt.PythonQtInstanceWrapper
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  __init__(...)
     |      x.__init__(...) initializes x; see help(type(x)) for signature
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  caseSensitivity = <unbound qt slot caseSensitivity of QCollator type>
     |      X.caseSensitivity(a)
     |  
     |  className = <built-in method className of PythonQt.PythonQtClassWrappe...
     |      Return the classname of the object
     |  
     |  compare = <unbound qt slot compare of QCollator type>
     |      X.compare(a, b, c, d, e) -> int
     |  
     |  delete = <built-in method delete of PythonQt.PythonQtClassWrapper obje...
     |      Deletes the given C++ object
     |  
     |  help = <built-in method help of PythonQt.PythonQtClassWrapper object>
     |      Shows the help of available methods for this class
     |  
     |  ignorePunctuation = <unbound qt slot ignorePunctuation of QCollator ty...
     |      X.ignorePunctuation(a) -> bool
     |  
     |  inherits = <built-in method inherits of PythonQt.PythonQtClassWrapper ...
     |      Returns if the class inherits or is of given type name
     |  
     |  locale = <unbound qt slot locale of QCollator type>
     |      X.locale(a) -> PythonQt.QtCore.QLocale
     |  
     |  numericMode = <unbound qt slot numericMode of QCollator type>
     |      X.numericMode(a) -> bool
     |  
     |  operator_assign = <unbound qt slot operator_assign of QCollator type>
     |      X.operator_assign(a, b) -> PythonQt.QtCore.QCollator
     |  
     |  operator_cast_ = <unbound qt slot operator_cast_ of QCollator type>
     |      X.operator_cast_(a, b, c) -> bool
     |  
     |  setCaseSensitivity = <unbound qt slot setCaseSensitivity of QCollator ...
     |      X.setCaseSensitivity(a, b)
     |  
     |  setIgnorePunctuation = <unbound qt slot setIgnorePunctuation of QColla...
     |      X.setIgnorePunctuation(a, b)
     |  
     |  setLocale = <unbound qt slot setLocale of QCollator type>
     |      X.setLocale(a, b)
     |  
     |  setNumericMode = <unbound qt slot setNumericMode of QCollator type>
     |      X.setNumericMode(a, b)
     |  
     |  sortKey = <unbound qt slot sortKey of QCollator type>
     |      X.sortKey(a, b) -> PythonQt.QtCore.QCollatorSortKey
     |  
     |  swap = <unbound qt slot swap of QCollator type>
     |      X.swap(a, b)
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __delattr__(...)
     |      x.__delattr__('name') <==> del x.name
     |  
     |  __eq__(...)
     |      x.__eq__(y) <==> x==y
     |  
     |  __ge__(...)
     |      x.__ge__(y) <==> x>=y
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __gt__(...)
     |      x.__gt__(y) <==> x>y
     |  
     |  __hash__(...)
     |      x.__hash__() <==> hash(x)
     |  
     |  __le__(...)
     |      x.__le__(y) <==> x<=y
     |  
     |  __lt__(...)
     |      x.__lt__(y) <==> x<y
     |  
     |  __ne__(...)
     |      x.__ne__(y) <==> x!=y
     |  
     |  __nonzero__(...)
     |      x.__nonzero__() <==> x != 0
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __setattr__(...)
     |      x.__setattr__('name', value) <==> x.name = value
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __new__ = <built-in method __new__ of PythonQt.PythonQtClassWrapper ob...
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
    
    class QCollatorSortKey(PythonQt.PythonQtInstanceWrapper)
     |  Method resolution order:
     |      QCollatorSortKey
     |      PythonQt.PythonQtInstanceWrapper
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  __init__(...)
     |      x.__init__(...) initializes x; see help(type(x)) for signature
     |  
     |  __lt__(...)
     |      x.__lt__(y) <==> x<y
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  className = <built-in method className of PythonQt.PythonQtClassWrappe...
     |      Return the classname of the object
     |  
     |  compare = <unbound qt slot compare of QCollatorSortKey type>
     |      X.compare(a, b) -> int
     |  
     |  delete = <built-in method delete of PythonQt.PythonQtClassWrapper obje...
     |      Deletes the given C++ object
     |  
     |  help = <built-in method help of PythonQt.PythonQtClassWrapper object>
     |      Shows the help of available methods for this class
     |  
     |  inherits = <built-in method inherits of PythonQt.PythonQtClassWrapper ...
     |      Returns if the class inherits or is of given type name
     |  
     |  operator_assign = <unbound qt slot operator_assign of QCollatorSortKey...
     |      X.operator_assign(a, b) -> PythonQt.QtCore.QCollatorSortKey
     |  
     |  swap = <unbound qt slot swap of QCollatorSortKey type>
     |      X.swap(a, b)
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __delattr__(...)
     |      x.__delattr__('name') <==> del x.name
     |  
     |  __eq__(...)
     |      x.__eq__(y) <==> x==y
     |  
     |  __ge__(...)
     |      x.__ge__(y) <==> x>=y
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __gt__(...)
     |      x.__gt__(y) <==> x>y
     |  
     |  __hash__(...)
     |      x.__hash__() <==> hash(x)
     |  
     |  __le__(...)
     |      x.__le__(y) <==> x<=y
     |  
     |  __ne__(...)
     |      x.__ne__(y) <==> x!=y
     |  
     |  __nonzero__(...)
     |      x.__nonzero__() <==> x != 0
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __setattr__(...)
     |      x.__setattr__('name', value) <==> x.name = value
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __new__ = <built-in method __new__ of PythonQt.PythonQtClassWrapper ob...
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
    
    class QCommandLineOption(PythonQt.PythonQtInstanceWrapper)
     |  Method resolution order:
     |      QCommandLineOption
     |      PythonQt.PythonQtInstanceWrapper
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  __init__(...)
     |      x.__init__(...) initializes x; see help(type(x)) for signature
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  className = <built-in method className of PythonQt.PythonQtClassWrappe...
     |      Return the classname of the object
     |  
     |  defaultValues = <unbound qt slot defaultValues of QCommandLineOption t...
     |      X.defaultValues(a) -> tuple
     |  
     |  delete = <built-in method delete of PythonQt.PythonQtClassWrapper obje...
     |      Deletes the given C++ object
     |  
     |  description = <unbound qt slot description of QCommandLineOption type>
     |      X.description(a) -> str
     |  
     |  help = <built-in method help of PythonQt.PythonQtClassWrapper object>
     |      Shows the help of available methods for this class
     |  
     |  inherits = <built-in method inherits of PythonQt.PythonQtClassWrapper ...
     |      Returns if the class inherits or is of given type name
     |  
     |  isHidden = <unbound qt slot isHidden of QCommandLineOption type>
     |      X.isHidden(a) -> bool
     |  
     |  names = <unbound qt slot names of QCommandLineOption type>
     |      X.names(a) -> tuple
     |  
     |  operator_assign = <unbound qt slot operator_assign of QCommandLineOpti...
     |      X.operator_assign(a, b) -> PythonQt.QtCore.QCommandLineOption
     |  
     |  setDefaultValue = <unbound qt slot setDefaultValue of QCommandLineOpti...
     |      X.setDefaultValue(a, b)
     |  
     |  setDefaultValues = <unbound qt slot setDefaultValues of QCommandLineOp...
     |      X.setDefaultValues(a, b)
     |  
     |  setDescription = <unbound qt slot setDescription of QCommandLineOption...
     |      X.setDescription(a, b)
     |  
     |  setHidden = <unbound qt slot setHidden of QCommandLineOption type>
     |      X.setHidden(a, b)
     |  
     |  setValueName = <unbound qt slot setValueName of QCommandLineOption typ...
     |      X.setValueName(a, b)
     |  
     |  swap = <unbound qt slot swap of QCommandLineOption type>
     |      X.swap(a, b)
     |  
     |  valueName = <unbound qt slot valueName of QCommandLineOption type>
     |      X.valueName(a) -> str
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __delattr__(...)
     |      x.__delattr__('name') <==> del x.name
     |  
     |  __eq__(...)
     |      x.__eq__(y) <==> x==y
     |  
     |  __ge__(...)
     |      x.__ge__(y) <==> x>=y
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __gt__(...)
     |      x.__gt__(y) <==> x>y
     |  
     |  __hash__(...)
     |      x.__hash__() <==> hash(x)
     |  
     |  __le__(...)
     |      x.__le__(y) <==> x<=y
     |  
     |  __lt__(...)
     |      x.__lt__(y) <==> x<y
     |  
     |  __ne__(...)
     |      x.__ne__(y) <==> x!=y
     |  
     |  __nonzero__(...)
     |      x.__nonzero__() <==> x != 0
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __setattr__(...)
     |      x.__setattr__('name', value) <==> x.name = value
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __new__ = <built-in method __new__ of PythonQt.PythonQtClassWrapper ob...
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
    
    class QCommandLineParser(PythonQt.PythonQtInstanceWrapper)
     |  Method resolution order:
     |      QCommandLineParser
     |      PythonQt.PythonQtInstanceWrapper
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  __init__(...)
     |      x.__init__(...) initializes x; see help(type(x)) for signature
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  OptionsAfterPositionalArgumentsMode = <class 'PythonQt.QtCore.OptionsA...
     |  
     |  
     |  ParseAsCompactedShortOptions = 0
     |  
     |  ParseAsLongOptions = 1
     |  
     |  ParseAsOptions = 0
     |  
     |  ParseAsPositionalArguments = 1
     |  
     |  SingleDashWordOptionMode = <class 'PythonQt.QtCore.SingleDashWordOptio...
     |  
     |  
     |  addHelpOption = <unbound qt slot addHelpOption of QCommandLineParser t...
     |      X.addHelpOption(a) -> PythonQt.QtCore.QCommandLineOption
     |  
     |  addOption = <unbound qt slot addOption of QCommandLineParser type>
     |      X.addOption(a, b) -> bool
     |  
     |  addOptions = <unbound qt slot addOptions of QCommandLineParser type>
     |      X.addOptions(a, b) -> bool
     |  
     |  addPositionalArgument = <unbound qt slot addPositionalArgument of QCom...
     |      X.addPositionalArgument(a, b, c, d)
     |  
     |  addVersionOption = <unbound qt slot addVersionOption of QCommandLinePa...
     |      X.addVersionOption(a) -> PythonQt.QtCore.QCommandLineOption
     |  
     |  applicationDescription = <unbound qt slot applicationDescription of QC...
     |      X.applicationDescription(a) -> str
     |  
     |  className = <built-in method className of PythonQt.PythonQtClassWrappe...
     |      Return the classname of the object
     |  
     |  clearPositionalArguments = <unbound qt slot clearPositionalArguments o...
     |      X.clearPositionalArguments(a)
     |  
     |  delete = <built-in method delete of PythonQt.PythonQtClassWrapper obje...
     |      Deletes the given C++ object
     |  
     |  errorText = <unbound qt slot errorText of QCommandLineParser type>
     |      X.errorText(a) -> str
     |  
     |  help = <built-in method help of PythonQt.PythonQtClassWrapper object>
     |      Shows the help of available methods for this class
     |  
     |  helpText = <unbound qt slot helpText of QCommandLineParser type>
     |      X.helpText(a) -> str
     |  
     |  inherits = <built-in method inherits of PythonQt.PythonQtClassWrapper ...
     |      Returns if the class inherits or is of given type name
     |  
     |  isSet = <unbound qt slot isSet of QCommandLineParser type>
     |      X.isSet(a, b) -> bool
     |  
     |  optionNames = <unbound qt slot optionNames of QCommandLineParser type>
     |      X.optionNames(a) -> tuple
     |  
     |  parse = <unbound qt slot parse of QCommandLineParser type>
     |      X.parse(a, b) -> bool
     |  
     |  positionalArguments = <unbound qt slot positionalArguments of QCommand...
     |      X.positionalArguments(a) -> tuple
     |  
     |  process = <unbound qt slot process of QCommandLineParser type>
     |      X.process(a, b)
     |  
     |  setApplicationDescription = <unbound qt slot setApplicationDescription...
     |      X.setApplicationDescription(a, b)
     |  
     |  setOptionsAfterPositionalArgumentsMode = <unbound qt slot setOptionsAf...
     |      X.setOptionsAfterPositionalArgumentsMode(a, b)
     |  
     |  setSingleDashWordOptionMode = <unbound qt slot setSingleDashWordOption...
     |      X.setSingleDashWordOptionMode(a, b)
     |  
     |  showHelp = <unbound qt slot showHelp of QCommandLineParser type>
     |      X.showHelp(a, b)
     |  
     |  showVersion = <unbound qt slot showVersion of QCommandLineParser type>
     |      X.showVersion(a)
     |  
     |  tr = <unbound qt slot static_QCommandLineParser_tr of QCommandLinePars...
     |      X.tr(a, b, c) -> str
     |  
     |  trUtf8 = <unbound qt slot static_QCommandLineParser_trUtf8 of QCommand...
     |      X.trUtf8(a, b, c) -> str
     |  
     |  unknownOptionNames = <unbound qt slot unknownOptionNames of QCommandLi...
     |      X.unknownOptionNames(a) -> tuple
     |  
     |  value = <unbound qt slot value of QCommandLineParser type>
     |      X.value(a, b) -> str
     |  
     |  values = <unbound qt slot values of QCommandLineParser type>
     |      X.values(a, b) -> tuple
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __delattr__(...)
     |      x.__delattr__('name') <==> del x.name
     |  
     |  __eq__(...)
     |      x.__eq__(y) <==> x==y
     |  
     |  __ge__(...)
     |      x.__ge__(y) <==> x>=y
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __gt__(...)
     |      x.__gt__(y) <==> x>y
     |  
     |  __hash__(...)
     |      x.__hash__() <==> hash(x)
     |  
     |  __le__(...)
     |      x.__le__(y) <==> x<=y
     |  
     |  __lt__(...)
     |      x.__lt__(y) <==> x<y
     |  
     |  __ne__(...)
     |      x.__ne__(y) <==> x!=y
     |  
     |  __nonzero__(...)
     |      x.__nonzero__() <==> x != 0
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __setattr__(...)
     |      x.__setattr__('name', value) <==> x.name = value
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __new__ = <built-in method __new__ of PythonQt.PythonQtClassWrapper ob...
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
    
    class QCoreApplication(PythonQt.PythonQtInstanceWrapper)
     |  Method resolution order:
     |      QCoreApplication
     |      PythonQt.PythonQtInstanceWrapper
     |      __builtin__.object
     |  
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  ApplicationFlags = 329992
     |  
     |  aboutToQuit = <unbound qt signal aboutToQuit of QCoreApplication type>
     |  
     |  
     |  addLibraryPath = <unbound qt slot static_QCoreApplication_addLibraryPa...
     |      X.addLibraryPath(a)
     |  
     |  applicationDirPath = <unbound qt slot static_QCoreApplication_applicat...
     |      X.applicationDirPath() -> str
     |  
     |  applicationFilePath = <unbound qt slot static_QCoreApplication_applica...
     |      X.applicationFilePath() -> str
     |  
     |  applicationName = None
     |  
     |  applicationNameChanged = <unbound qt signal applicationNameChanged of ...
     |  
     |  
     |  applicationPid = <unbound qt slot static_QCoreApplication_applicationP...
     |      X.applicationPid() -> int
     |  
     |  applicationVersion = None
     |  
     |  applicationVersionChanged = <unbound qt signal applicationVersionChang...
     |  
     |  
     |  blockSignals = <unbound qt slot blockSignals of QCoreApplication type>
     |      X.blockSignals(a, b) -> bool
     |  
     |  childEvent = <unbound qt slot py_q_childEvent of QCoreApplication type...
     |      X.childEvent(a, b)
     |  
     |  children = <unbound qt slot children of QCoreApplication type>
     |      X.children(a) -> tuple
     |  
     |  className = <built-in method className of PythonQt.PythonQtClassWrappe...
     |      Return the classname of the object
     |  
     |  closingDown = <unbound qt slot static_QCoreApplication_closingDown of ...
     |      X.closingDown() -> bool
     |  
     |  connect = <unbound qt slot connect of QCoreApplication type>
     |      X.connect(a, b, c, d, e) -> bool
     |  
     |  customEvent = <unbound qt slot py_q_customEvent of QCoreApplication ty...
     |      X.customEvent(a, b)
     |  
     |  delete = <built-in method delete of PythonQt.PythonQtClassWrapper obje...
     |      Deletes the given C++ object
     |  
     |  deleteLater = <unbound qt slot deleteLater of QCoreApplication type>
     |      X.deleteLater()
     |  
     |  destroyed = <unbound qt signal destroyed of QCoreApplication type>
     |  
     |  
     |  disconnect = <unbound qt slot disconnect of QCoreApplication type>
     |      X.disconnect(a, b, c, d) -> bool
     |  
     |  dumpObjectInfo = <unbound qt slot dumpObjectInfo of QCoreApplication t...
     |      X.dumpObjectInfo(a)
     |  
     |  dumpObjectTree = <unbound qt slot dumpObjectTree of QCoreApplication t...
     |      X.dumpObjectTree(a)
     |  
     |  dynamicPropertyNames = <unbound qt slot dynamicPropertyNames of QCoreA...
     |      X.dynamicPropertyNames(a)
     |  
     |  enum_1 = <class 'PythonQt.QtCore.enum_1'>
     |  
     |  
     |  event = <unbound qt slot py_q_event of QCoreApplication type>
     |      X.event(a, b) -> bool
     |  
     |  eventDispatcher = <unbound qt slot static_QCoreApplication_eventDispat...
     |      X.eventDispatcher()
     |  
     |  eventFilter = <unbound qt slot py_q_eventFilter of QCoreApplication ty...
     |      X.eventFilter(a, b, c) -> bool
     |  
     |  exec = <unbound qt slot static_QCoreApplication_exec of QCoreApplicati...
     |      X.exec() -> int
     |  
     |  exit = <unbound qt slot static_QCoreApplication_exit of QCoreApplicati...
     |      X.exit(a)
     |  
     |  findChild = <unbound qt slot findChild of QCoreApplication type>
     |      X.findChild(a, b, c) -> PythonQt.private.QObject
     |  
     |  findChildren = <unbound qt slot findChildren of QCoreApplication type>
     |      X.findChildren(a, b, c) -> tuple
     |  
     |  flush = <unbound qt slot static_QCoreApplication_flush of QCoreApplica...
     |      X.flush()
     |  
     |  hasPendingEvents = <unbound qt slot static_QCoreApplication_hasPending...
     |      X.hasPendingEvents() -> bool
     |  
     |  help = <built-in method help of PythonQt.PythonQtClassWrapper object>
     |      Shows the help of available methods for this class
     |  
     |  inherits = <built-in method inherits of PythonQt.PythonQtClassWrapper ...
     |      Returns if the class inherits or is of given type name
     |  
     |  installEventFilter = <unbound qt slot installEventFilter of QCoreAppli...
     |      X.installEventFilter(a, b)
     |  
     |  installTranslator = <unbound qt slot static_QCoreApplication_installTr...
     |      X.installTranslator(a) -> bool
     |  
     |  instance = <unbound qt slot static_QCoreApplication_instance of QCoreA...
     |      X.instance() -> PythonQt.QtCore.QCoreApplication
     |  
     |  isQuitLockEnabled = <unbound qt slot static_QCoreApplication_isQuitLoc...
     |      X.isQuitLockEnabled() -> bool
     |  
     |  isSetuidAllowed = <unbound qt slot static_QCoreApplication_isSetuidAll...
     |      X.isSetuidAllowed() -> bool
     |  
     |  isSignalConnected = <unbound qt slot isSignalConnected of QCoreApplica...
     |      X.isSignalConnected(a, b) -> bool
     |  
     |  isWidgetType = <unbound qt slot isWidgetType of QCoreApplication type>
     |      X.isWidgetType(a) -> bool
     |  
     |  isWindowType = <unbound qt slot isWindowType of QCoreApplication type>
     |      X.isWindowType(a) -> bool
     |  
     |  killTimer = <unbound qt slot killTimer of QCoreApplication type>
     |      X.killTimer(a, b)
     |  
     |  libraryPaths = <unbound qt slot static_QCoreApplication_libraryPaths o...
     |      X.libraryPaths() -> tuple
     |  
     |  metaObject = <unbound qt slot metaObject of QCoreApplication type>
     |      X.metaObject(a) -> PythonQt.QtCore.QMetaObject
     |  
     |  moveToThread = <unbound qt slot moveToThread of QCoreApplication type>
     |      X.moveToThread(a, b)
     |  
     |  notify = <unbound qt slot py_q_notify of QCoreApplication type>
     |      X.notify(a, b, c) -> bool
     |  
     |  objectName = None
     |  
     |  objectNameChanged = <unbound qt signal objectNameChanged of QCoreAppli...
     |  
     |  
     |  organizationDomain = None
     |  
     |  organizationDomainChanged = <unbound qt signal organizationDomainChang...
     |  
     |  
     |  organizationName = None
     |  
     |  organizationNameChanged = <unbound qt signal organizationNameChanged o...
     |  
     |  
     |  parent = <unbound qt slot parent of QCoreApplication type>
     |      X.parent(a) -> PythonQt.private.QObject
     |  
     |  postEvent = <unbound qt slot static_QCoreApplication_postEvent of QCor...
     |      X.postEvent(a, b, c)
     |  
     |  processEvents = <unbound qt slot static_QCoreApplication_processEvents...
     |      X.processEvents(a, b)
     |  
     |  property = <unbound qt slot property of QCoreApplication type>
     |      X.property(a, b) -> object
     |  
     |  quit = <unbound qt slot quit of QCoreApplication type>
     |      X.quit()
     |  
     |  quitLockEnabled = None
     |  
     |  removeEventFilter = <unbound qt slot removeEventFilter of QCoreApplica...
     |      X.removeEventFilter(a, b)
     |  
     |  removeLibraryPath = <unbound qt slot static_QCoreApplication_removeLib...
     |      X.removeLibraryPath(a)
     |  
     |  removePostedEvents = <unbound qt slot static_QCoreApplication_removePo...
     |      X.removePostedEvents(a, b)
     |  
     |  removeTranslator = <unbound qt slot static_QCoreApplication_removeTran...
     |      X.removeTranslator(a) -> bool
     |  
     |  sendEvent = <unbound qt slot static_QCoreApplication_sendEvent of QCor...
     |      X.sendEvent(a, b) -> bool
     |  
     |  sendPostedEvents = <unbound qt slot static_QCoreApplication_sendPosted...
     |      X.sendPostedEvents(a, b)
     |  
     |  sender = <unbound qt slot sender of QCoreApplication type>
     |      X.sender(a) -> PythonQt.private.QObject
     |  
     |  senderSignalIndex = <unbound qt slot senderSignalIndex of QCoreApplica...
     |      X.senderSignalIndex(a) -> int
     |  
     |  setApplicationName = <unbound qt slot static_QCoreApplication_setAppli...
     |      X.setApplicationName(a)
     |  
     |  setApplicationVersion = <unbound qt slot static_QCoreApplication_setAp...
     |      X.setApplicationVersion(a)
     |  
     |  setAttribute = <unbound qt slot static_QCoreApplication_setAttribute o...
     |      X.setAttribute(a, b)
     |  
     |  setEventDispatcher = <unbound qt slot static_QCoreApplication_setEvent...
     |      X.setEventDispatcher(a)
     |  
     |  setLibraryPaths = <unbound qt slot static_QCoreApplication_setLibraryP...
     |      X.setLibraryPaths(a)
     |  
     |  setObjectName = <unbound qt slot setObjectName of QCoreApplication typ...
     |      X.setObjectName(a, b)
     |  
     |  setOrganizationDomain = <unbound qt slot static_QCoreApplication_setOr...
     |      X.setOrganizationDomain(a)
     |  
     |  setOrganizationName = <unbound qt slot static_QCoreApplication_setOrga...
     |      X.setOrganizationName(a)
     |  
     |  setParent = <unbound qt slot setParent of QCoreApplication type>
     |      X.setParent(a, b)
     |  
     |  setProperty = <unbound qt slot setProperty of QCoreApplication type>
     |      X.setProperty(a, b, c) -> bool
     |  
     |  setQuitLockEnabled = <unbound qt slot static_QCoreApplication_setQuitL...
     |      X.setQuitLockEnabled(a)
     |  
     |  setSetuidAllowed = <unbound qt slot static_QCoreApplication_setSetuidA...
     |      X.setSetuidAllowed(a)
     |  
     |  signalsBlocked = <unbound qt slot signalsBlocked of QCoreApplication t...
     |      X.signalsBlocked(a) -> bool
     |  
     |  startTimer = <unbound qt slot startTimer of QCoreApplication type>
     |      X.startTimer(a, b, c) -> int
     |  
     |  startingUp = <unbound qt slot static_QCoreApplication_startingUp of QC...
     |      X.startingUp() -> bool
     |  
     |  testAttribute = <unbound qt slot static_QCoreApplication_testAttribute...
     |      X.testAttribute(a) -> bool
     |  
     |  thread = <unbound qt slot thread of QCoreApplication type>
     |      X.thread(a)
     |  
     |  timerEvent = <unbound qt slot py_q_timerEvent of QCoreApplication type...
     |      X.timerEvent(a, b)
     |  
     |  tr = <unbound qt slot tr of QCoreApplication type>
     |      X.tr(a, b, c, d) -> str
     |  
     |  translate = <unbound qt slot static_QCoreApplication_translate of QCor...
     |      X.translate(a, b, c, d) -> str
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __delattr__(...)
     |      x.__delattr__('name') <==> del x.name
     |  
     |  __eq__(...)
     |      x.__eq__(y) <==> x==y
     |  
     |  __ge__(...)
     |      x.__ge__(y) <==> x>=y
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __gt__(...)
     |      x.__gt__(y) <==> x>y
     |  
     |  __hash__(...)
     |      x.__hash__() <==> hash(x)
     |  
     |  __init__(...)
     |      x.__init__(...) initializes x; see help(type(x)) for signature
     |  
     |  __le__(...)
     |      x.__le__(y) <==> x<=y
     |  
     |  __lt__(...)
     |      x.__lt__(y) <==> x<y
     |  
     |  __ne__(...)
     |      x.__ne__(y) <==> x!=y
     |  
     |  __nonzero__(...)
     |      x.__nonzero__() <==> x != 0
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __setattr__(...)
     |      x.__setattr__('name', value) <==> x.name = value
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __new__ = <built-in method __new__ of PythonQt.PythonQtClassWrapper ob...
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
    
    class QCryptographicHash(PythonQt.PythonQtInstanceWrapper)
     |  Method resolution order:
     |      QCryptographicHash
     |      PythonQt.PythonQtInstanceWrapper
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  __init__(...)
     |      x.__init__(...) initializes x; see help(type(x)) for signature
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  Algorithm = <class 'PythonQt.QtCore.Algorithm'>
     |  
     |  
     |  Md4 = 0
     |  
     |  Md5 = 1
     |  
     |  Sha1 = 2
     |  
     |  Sha224 = 3
     |  
     |  Sha256 = 4
     |  
     |  Sha384 = 5
     |  
     |  Sha3_224 = 11
     |  
     |  Sha3_256 = 12
     |  
     |  Sha3_384 = 13
     |  
     |  Sha3_512 = 14
     |  
     |  Sha512 = 6
     |  
     |  addData = <unbound qt slot addData of QCryptographicHash type>
     |      X.addData(a, b) -> bool
     |  
     |  className = <built-in method className of PythonQt.PythonQtClassWrappe...
     |      Return the classname of the object
     |  
     |  delete = <built-in method delete of PythonQt.PythonQtClassWrapper obje...
     |      Deletes the given C++ object
     |  
     |  hash = <unbound qt slot static_QCryptographicHash_hash of QCryptograph...
     |      X.hash(a, b) -> PythonQt.QtCore.QByteArray
     |  
     |  help = <built-in method help of PythonQt.PythonQtClassWrapper object>
     |      Shows the help of available methods for this class
     |  
     |  inherits = <built-in method inherits of PythonQt.PythonQtClassWrapper ...
     |      Returns if the class inherits or is of given type name
     |  
     |  reset = <unbound qt slot reset of QCryptographicHash type>
     |      X.reset(a)
     |  
     |  result = <unbound qt slot result of QCryptographicHash type>
     |      X.result(a) -> PythonQt.QtCore.QByteArray
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __delattr__(...)
     |      x.__delattr__('name') <==> del x.name
     |  
     |  __eq__(...)
     |      x.__eq__(y) <==> x==y
     |  
     |  __ge__(...)
     |      x.__ge__(y) <==> x>=y
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __gt__(...)
     |      x.__gt__(y) <==> x>y
     |  
     |  __hash__(...)
     |      x.__hash__() <==> hash(x)
     |  
     |  __le__(...)
     |      x.__le__(y) <==> x<=y
     |  
     |  __lt__(...)
     |      x.__lt__(y) <==> x<y
     |  
     |  __ne__(...)
     |      x.__ne__(y) <==> x!=y
     |  
     |  __nonzero__(...)
     |      x.__nonzero__() <==> x != 0
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __setattr__(...)
     |      x.__setattr__('name', value) <==> x.name = value
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __new__ = <built-in method __new__ of PythonQt.PythonQtClassWrapper ob...
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
    
    class QDataStream(PythonQt.PythonQtInstanceWrapper)
     |  Method resolution order:
     |      QDataStream
     |      PythonQt.PythonQtInstanceWrapper
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  __init__(...)
     |      x.__init__(...) initializes x; see help(type(x)) for signature
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  BigEndian = 0
     |  
     |  ByteOrder = <class 'PythonQt.QtCore.ByteOrder'>
     |  
     |  
     |  DoublePrecision = 1
     |  
     |  FloatingPointPrecision = <class 'PythonQt.QtCore.FloatingPointPrecisio...
     |  
     |  
     |  LittleEndian = 1
     |  
     |  Ok = 0
     |  
     |  Qt_1_0 = 1
     |  
     |  Qt_2_0 = 2
     |  
     |  Qt_2_1 = 3
     |  
     |  Qt_3_0 = 4
     |  
     |  Qt_3_1 = 5
     |  
     |  Qt_3_3 = 6
     |  
     |  Qt_4_0 = 7
     |  
     |  Qt_4_1 = 7
     |  
     |  Qt_4_2 = 8
     |  
     |  Qt_4_3 = 9
     |  
     |  Qt_4_4 = 10
     |  
     |  Qt_4_5 = 11
     |  
     |  Qt_4_6 = 12
     |  
     |  Qt_4_7 = 12
     |  
     |  Qt_4_8 = 12
     |  
     |  Qt_4_9 = 12
     |  
     |  Qt_5_0 = 13
     |  
     |  Qt_5_1 = 14
     |  
     |  Qt_5_2 = 15
     |  
     |  Qt_5_3 = 15
     |  
     |  Qt_5_4 = 16
     |  
     |  Qt_5_5 = 16
     |  
     |  Qt_5_6 = 17
     |  
     |  Qt_DefaultCompiledVersion = 17
     |  
     |  ReadCorruptData = 2
     |  
     |  ReadPastEnd = 1
     |  
     |  SinglePrecision = 0
     |  
     |  Status = <class 'PythonQt.QtCore.Status'>
     |  
     |  
     |  Version = <class 'PythonQt.QtCore.Version'>
     |  
     |  
     |  WriteFailed = 3
     |  
     |  atEnd = <unbound qt slot atEnd of QDataStream type>
     |      X.atEnd(a) -> bool
     |  
     |  byteOrder = <unbound qt slot byteOrder of QDataStream type>
     |      X.byteOrder(a)
     |  
     |  className = <built-in method className of PythonQt.PythonQtClassWrappe...
     |      Return the classname of the object
     |  
     |  delete = <built-in method delete of PythonQt.PythonQtClassWrapper obje...
     |      Deletes the given C++ object
     |  
     |  device = <unbound qt slot device of QDataStream type>
     |      X.device(a) -> PythonQt.QtCore.QIODevice
     |  
     |  floatingPointPrecision = <unbound qt slot floatingPointPrecision of QD...
     |      X.floatingPointPrecision(a)
     |  
     |  help = <built-in method help of PythonQt.PythonQtClassWrapper object>
     |      Shows the help of available methods for this class
     |  
     |  inherits = <built-in method inherits of PythonQt.PythonQtClassWrapper ...
     |      Returns if the class inherits or is of given type name
     |  
     |  readBool = <unbound qt slot readBool of QDataStream type>
     |      X.readBool(a) -> bool
     |  
     |  readDouble = <unbound qt slot readDouble of QDataStream type>
     |      X.readDouble(a) -> float
     |  
     |  readFloat = <unbound qt slot readFloat of QDataStream type>
     |      X.readFloat(a) -> float
     |  
     |  readInt16 = <unbound qt slot readInt16 of QDataStream type>
     |      X.readInt16(a) -> int
     |  
     |  readInt32 = <unbound qt slot readInt32 of QDataStream type>
     |      X.readInt32(a) -> int
     |  
     |  readInt64 = <unbound qt slot readInt64 of QDataStream type>
     |      X.readInt64(a) -> int
     |  
     |  readInt8 = <unbound qt slot readInt8 of QDataStream type>
     |      X.readInt8(a) -> int
     |  
     |  readQChar = <unbound qt slot readQChar of QDataStream type>
     |      X.readQChar(a)
     |  
     |  readQString = <unbound qt slot readQString of QDataStream type>
     |      X.readQString(a) -> str
     |  
     |  readQStringList = <unbound qt slot readQStringList of QDataStream type...
     |      X.readQStringList(a) -> tuple
     |  
     |  readQVariant = <unbound qt slot readQVariant of QDataStream type>
     |      X.readQVariant(a) -> object
     |  
     |  readRawData = <unbound qt slot readRawData of QDataStream type>
     |      X.readRawData(a, b)
     |  
     |  readString = <unbound qt slot readString of QDataStream type>
     |      X.readString(a) -> str
     |  
     |  readUInt16 = <unbound qt slot readUInt16 of QDataStream type>
     |      X.readUInt16(a) -> int
     |  
     |  readUInt32 = <unbound qt slot readUInt32 of QDataStream type>
     |      X.readUInt32(a) -> int
     |  
     |  readUInt64 = <unbound qt slot readUInt64 of QDataStream type>
     |      X.readUInt64(a) -> int
     |  
     |  readUInt8 = <unbound qt slot readUInt8 of QDataStream type>
     |      X.readUInt8(a) -> int
     |  
     |  resetStatus = <unbound qt slot resetStatus of QDataStream type>
     |      X.resetStatus(a)
     |  
     |  setByteOrder = <unbound qt slot setByteOrder of QDataStream type>
     |      X.setByteOrder(a, b)
     |  
     |  setDevice = <unbound qt slot setDevice of QDataStream type>
     |      X.setDevice(a, b)
     |  
     |  setFloatingPointPrecision = <unbound qt slot setFloatingPointPrecision...
     |      X.setFloatingPointPrecision(a, b)
     |  
     |  setStatus = <unbound qt slot setStatus of QDataStream type>
     |      X.setStatus(a, b)
     |  
     |  setVersion = <unbound qt slot setVersion of QDataStream type>
     |      X.setVersion(a, b)
     |  
     |  skipRawData = <unbound qt slot skipRawData of QDataStream type>
     |      X.skipRawData(a, b) -> int
     |  
     |  status = <unbound qt slot status of QDataStream type>
     |      X.status(a)
     |  
     |  unsetDevice = <unbound qt slot unsetDevice of QDataStream type>
     |      X.unsetDevice(a)
     |  
     |  version = <unbound qt slot version of QDataStream type>
     |      X.version(a) -> int
     |  
     |  writeBool = <unbound qt slot writeBool of QDataStream type>
     |      X.writeBool(a, b)
     |  
     |  writeDouble = <unbound qt slot writeDouble of QDataStream type>
     |      X.writeDouble(a, b)
     |  
     |  writeFloat = <unbound qt slot writeFloat of QDataStream type>
     |      X.writeFloat(a, b)
     |  
     |  writeInt16 = <unbound qt slot writeInt16 of QDataStream type>
     |      X.writeInt16(a, b)
     |  
     |  writeInt32 = <unbound qt slot writeInt32 of QDataStream type>
     |      X.writeInt32(a, b)
     |  
     |  writeInt64 = <unbound qt slot writeInt64 of QDataStream type>
     |      X.writeInt64(a, b)
     |  
     |  writeInt8 = <unbound qt slot writeInt8 of QDataStream type>
     |      X.writeInt8(a, b)
     |  
     |  writeQChar = <unbound qt slot writeQChar of QDataStream type>
     |      X.writeQChar(a, b)
     |  
     |  writeQString = <unbound qt slot writeQString of QDataStream type>
     |      X.writeQString(a, b)
     |  
     |  writeQStringList = <unbound qt slot writeQStringList of QDataStream ty...
     |      X.writeQStringList(a, b)
     |  
     |  writeQVariant = <unbound qt slot writeQVariant of QDataStream type>
     |      X.writeQVariant(a, b)
     |  
     |  writeRawData = <unbound qt slot writeRawData of QDataStream type>
     |      X.writeRawData(a, b) -> int
     |  
     |  writeString = <unbound qt slot writeString of QDataStream type>
     |      X.writeString(a, b)
     |  
     |  writeUInt16 = <unbound qt slot writeUInt16 of QDataStream type>
     |      X.writeUInt16(a, b)
     |  
     |  writeUInt32 = <unbound qt slot writeUInt32 of QDataStream type>
     |      X.writeUInt32(a, b)
     |  
     |  writeUInt64 = <unbound qt slot writeUInt64 of QDataStream type>
     |      X.writeUInt64(a, b)
     |  
     |  writeUInt8 = <unbound qt slot writeUInt8 of QDataStream type>
     |      X.writeUInt8(a, b)
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __delattr__(...)
     |      x.__delattr__('name') <==> del x.name
     |  
     |  __eq__(...)
     |      x.__eq__(y) <==> x==y
     |  
     |  __ge__(...)
     |      x.__ge__(y) <==> x>=y
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __gt__(...)
     |      x.__gt__(y) <==> x>y
     |  
     |  __hash__(...)
     |      x.__hash__() <==> hash(x)
     |  
     |  __le__(...)
     |      x.__le__(y) <==> x<=y
     |  
     |  __lt__(...)
     |      x.__lt__(y) <==> x<y
     |  
     |  __ne__(...)
     |      x.__ne__(y) <==> x!=y
     |  
     |  __nonzero__(...)
     |      x.__nonzero__() <==> x != 0
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __setattr__(...)
     |      x.__setattr__('name', value) <==> x.name = value
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __new__ = <built-in method __new__ of PythonQt.PythonQtClassWrapper ob...
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
    
    class QDate(PythonQt.PythonQtInstanceWrapper)
     |  Method resolution order:
     |      QDate
     |      PythonQt.PythonQtInstanceWrapper
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  __eq__(...)
     |      x.__eq__(y) <==> x==y
     |  
     |  __ge__(...)
     |      x.__ge__(y) <==> x>=y
     |  
     |  __gt__(...)
     |      x.__gt__(y) <==> x>y
     |  
     |  __init__(...)
     |      x.__init__(...) initializes x; see help(type(x)) for signature
     |  
     |  __le__(...)
     |      x.__le__(y) <==> x<=y
     |  
     |  __lt__(...)
     |      x.__lt__(y) <==> x<y
     |  
     |  __ne__(...)
     |      x.__ne__(y) <==> x!=y
     |  
     |  __nonzero__(...)
     |      x.__nonzero__() <==> x != 0
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  DateFormat = 0
     |  
     |  MonthNameType = <class 'PythonQt.QtCore.MonthNameType'>
     |  
     |  
     |  StandaloneFormat = 1
     |  
     |  addDays = <unbound qt slot addDays of QDate type>
     |      X.addDays(a, b) -> PythonQt.QtCore.QDate
     |  
     |  addMonths = <unbound qt slot addMonths of QDate type>
     |      X.addMonths(a, b) -> PythonQt.QtCore.QDate
     |  
     |  addYears = <unbound qt slot addYears of QDate type>
     |      X.addYears(a, b) -> PythonQt.QtCore.QDate
     |  
     |  className = <built-in method className of PythonQt.PythonQtClassWrappe...
     |      Return the classname of the object
     |  
     |  currentDate = <unbound qt slot static_QDate_currentDate of QDate type>
     |      X.currentDate() -> PythonQt.QtCore.QDate
     |  
     |  day = <unbound qt slot day of QDate type>
     |      X.day(a) -> int
     |  
     |  dayOfWeek = <unbound qt slot dayOfWeek of QDate type>
     |      X.dayOfWeek(a) -> int
     |  
     |  dayOfYear = <unbound qt slot dayOfYear of QDate type>
     |      X.dayOfYear(a) -> int
     |  
     |  daysInMonth = <unbound qt slot daysInMonth of QDate type>
     |      X.daysInMonth(a) -> int
     |  
     |  daysInYear = <unbound qt slot daysInYear of QDate type>
     |      X.daysInYear(a) -> int
     |  
     |  daysTo = <unbound qt slot daysTo of QDate type>
     |      X.daysTo(a, b) -> int
     |  
     |  delete = <built-in method delete of PythonQt.PythonQtClassWrapper obje...
     |      Deletes the given C++ object
     |  
     |  fromJulianDay = <unbound qt slot static_QDate_fromJulianDay of QDate t...
     |      X.fromJulianDay(a) -> PythonQt.QtCore.QDate
     |  
     |  fromString = <unbound qt slot static_QDate_fromString of QDate type>
     |      X.fromString(a, b) -> PythonQt.QtCore.QDate
     |  
     |  getDate = <unbound qt slot getDate of QDate type>
     |      X.getDate(a, b, c, d)
     |  
     |  help = <built-in method help of PythonQt.PythonQtClassWrapper object>
     |      Shows the help of available methods for this class
     |  
     |  inherits = <built-in method inherits of PythonQt.PythonQtClassWrapper ...
     |      Returns if the class inherits or is of given type name
     |  
     |  isLeapYear = <unbound qt slot static_QDate_isLeapYear of QDate type>
     |      X.isLeapYear(a) -> bool
     |  
     |  isNull = <unbound qt slot isNull of QDate type>
     |      X.isNull(a) -> bool
     |  
     |  isValid = <unbound qt slot isValid of QDate type>
     |      X.isValid(a, b, c) -> bool
     |  
     |  longDayName = <unbound qt slot static_QDate_longDayName of QDate type>
     |      X.longDayName(a, b) -> str
     |  
     |  longMonthName = <unbound qt slot static_QDate_longMonthName of QDate t...
     |      X.longMonthName(a, b) -> str
     |  
     |  month = <unbound qt slot month of QDate type>
     |      X.month(a) -> int
     |  
     |  readFrom = <unbound qt slot readFrom of QDate type>
     |      X.readFrom(a, b)
     |  
     |  setDate = <unbound qt slot setDate of QDate type>
     |      X.setDate(a, b, c, d) -> bool
     |  
     |  shortDayName = <unbound qt slot static_QDate_shortDayName of QDate typ...
     |      X.shortDayName(a, b) -> str
     |  
     |  shortMonthName = <unbound qt slot static_QDate_shortMonthName of QDate...
     |      X.shortMonthName(a, b) -> str
     |  
     |  toJulianDay = <unbound qt slot toJulianDay of QDate type>
     |      X.toJulianDay(a) -> int
     |  
     |  toString = <unbound qt slot toString of QDate type>
     |      X.toString(a, b) -> str
     |  
     |  weekNumber = <unbound qt slot weekNumber of QDate type>
     |      X.weekNumber(a, b) -> int
     |  
     |  writeTo = <unbound qt slot writeTo of QDate type>
     |      X.writeTo(a, b)
     |  
     |  year = <unbound qt slot year of QDate type>
     |      X.year(a) -> int
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __delattr__(...)
     |      x.__delattr__('name') <==> del x.name
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __hash__(...)
     |      x.__hash__() <==> hash(x)
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __setattr__(...)
     |      x.__setattr__('name', value) <==> x.name = value
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __new__ = <built-in method __new__ of PythonQt.PythonQtClassWrapper ob...
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
    
    class QDateTime(PythonQt.PythonQtInstanceWrapper)
     |  Method resolution order:
     |      QDateTime
     |      PythonQt.PythonQtInstanceWrapper
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  __eq__(...)
     |      x.__eq__(y) <==> x==y
     |  
     |  __ge__(...)
     |      x.__ge__(y) <==> x>=y
     |  
     |  __gt__(...)
     |      x.__gt__(y) <==> x>y
     |  
     |  __init__(...)
     |      x.__init__(...) initializes x; see help(type(x)) for signature
     |  
     |  __le__(...)
     |      x.__le__(y) <==> x<=y
     |  
     |  __lt__(...)
     |      x.__lt__(y) <==> x<y
     |  
     |  __ne__(...)
     |      x.__ne__(y) <==> x!=y
     |  
     |  __nonzero__(...)
     |      x.__nonzero__() <==> x != 0
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  addDays = <unbound qt slot addDays of QDateTime type>
     |      X.addDays(a, b) -> PythonQt.QtCore.QDateTime
     |  
     |  addMSecs = <unbound qt slot addMSecs of QDateTime type>
     |      X.addMSecs(a, b) -> PythonQt.QtCore.QDateTime
     |  
     |  addMonths = <unbound qt slot addMonths of QDateTime type>
     |      X.addMonths(a, b) -> PythonQt.QtCore.QDateTime
     |  
     |  addSecs = <unbound qt slot addSecs of QDateTime type>
     |      X.addSecs(a, b) -> PythonQt.QtCore.QDateTime
     |  
     |  addYears = <unbound qt slot addYears of QDateTime type>
     |      X.addYears(a, b) -> PythonQt.QtCore.QDateTime
     |  
     |  className = <built-in method className of PythonQt.PythonQtClassWrappe...
     |      Return the classname of the object
     |  
     |  currentDateTime = <unbound qt slot static_QDateTime_currentDateTime of...
     |      X.currentDateTime() -> PythonQt.QtCore.QDateTime
     |  
     |  currentDateTimeUtc = <unbound qt slot static_QDateTime_currentDateTime...
     |      X.currentDateTimeUtc() -> PythonQt.QtCore.QDateTime
     |  
     |  currentMSecsSinceEpoch = <unbound qt slot static_QDateTime_currentMSec...
     |      X.currentMSecsSinceEpoch() -> int
     |  
     |  date = <unbound qt slot date of QDateTime type>
     |      X.date(a) -> PythonQt.QtCore.QDate
     |  
     |  daysTo = <unbound qt slot daysTo of QDateTime type>
     |      X.daysTo(a, b) -> int
     |  
     |  delete = <built-in method delete of PythonQt.PythonQtClassWrapper obje...
     |      Deletes the given C++ object
     |  
     |  fromMSecsSinceEpoch = <unbound qt slot static_QDateTime_fromMSecsSince...
     |      X.fromMSecsSinceEpoch(a, b, c) -> PythonQt.QtCore.QDateTime
     |  
     |  fromString = <unbound qt slot static_QDateTime_fromString of QDateTime...
     |      X.fromString(a, b) -> PythonQt.QtCore.QDateTime
     |  
     |  fromTime_t = <unbound qt slot static_QDateTime_fromTime_t of QDateTime...
     |      X.fromTime_t(a, b, c) -> PythonQt.QtCore.QDateTime
     |  
     |  help = <built-in method help of PythonQt.PythonQtClassWrapper object>
     |      Shows the help of available methods for this class
     |  
     |  inherits = <built-in method inherits of PythonQt.PythonQtClassWrapper ...
     |      Returns if the class inherits or is of given type name
     |  
     |  isDaylightTime = <unbound qt slot isDaylightTime of QDateTime type>
     |      X.isDaylightTime(a) -> bool
     |  
     |  isNull = <unbound qt slot isNull of QDateTime type>
     |      X.isNull(a) -> bool
     |  
     |  isValid = <unbound qt slot isValid of QDateTime type>
     |      X.isValid(a) -> bool
     |  
     |  msecsTo = <unbound qt slot msecsTo of QDateTime type>
     |      X.msecsTo(a, b) -> int
     |  
     |  offsetFromUtc = <unbound qt slot offsetFromUtc of QDateTime type>
     |      X.offsetFromUtc(a) -> int
     |  
     |  readFrom = <unbound qt slot readFrom of QDateTime type>
     |      X.readFrom(a, b)
     |  
     |  secsTo = <unbound qt slot secsTo of QDateTime type>
     |      X.secsTo(a, b) -> int
     |  
     |  setDate = <unbound qt slot setDate of QDateTime type>
     |      X.setDate(a, b)
     |  
     |  setMSecsSinceEpoch = <unbound qt slot setMSecsSinceEpoch of QDateTime ...
     |      X.setMSecsSinceEpoch(a, b)
     |  
     |  setOffsetFromUtc = <unbound qt slot setOffsetFromUtc of QDateTime type...
     |      X.setOffsetFromUtc(a, b)
     |  
     |  setTime = <unbound qt slot setTime of QDateTime type>
     |      X.setTime(a, b)
     |  
     |  setTimeSpec = <unbound qt slot setTimeSpec of QDateTime type>
     |      X.setTimeSpec(a, b)
     |  
     |  setTimeZone = <unbound qt slot setTimeZone of QDateTime type>
     |      X.setTimeZone(a, b)
     |  
     |  setTime_t = <unbound qt slot setTime_t of QDateTime type>
     |      X.setTime_t(a, b)
     |  
     |  setUtcOffset = <unbound qt slot setUtcOffset of QDateTime type>
     |      X.setUtcOffset(a, b)
     |  
     |  swap = <unbound qt slot swap of QDateTime type>
     |      X.swap(a, b)
     |  
     |  time = <unbound qt slot time of QDateTime type>
     |      X.time(a) -> PythonQt.QtCore.QTime
     |  
     |  timeSpec = <unbound qt slot timeSpec of QDateTime type>
     |      X.timeSpec(a)
     |  
     |  timeZone = <unbound qt slot timeZone of QDateTime type>
     |      X.timeZone(a) -> PythonQt.QtCore.QTimeZone
     |  
     |  timeZoneAbbreviation = <unbound qt slot timeZoneAbbreviation of QDateT...
     |      X.timeZoneAbbreviation(a) -> str
     |  
     |  toLocalTime = <unbound qt slot toLocalTime of QDateTime type>
     |      X.toLocalTime(a) -> PythonQt.QtCore.QDateTime
     |  
     |  toMSecsSinceEpoch = <unbound qt slot toMSecsSinceEpoch of QDateTime ty...
     |      X.toMSecsSinceEpoch(a) -> int
     |  
     |  toOffsetFromUtc = <unbound qt slot toOffsetFromUtc of QDateTime type>
     |      X.toOffsetFromUtc(a, b) -> PythonQt.QtCore.QDateTime
     |  
     |  toString = <unbound qt slot toString of QDateTime type>
     |      X.toString(a, b) -> str
     |  
     |  toTimeSpec = <unbound qt slot toTimeSpec of QDateTime type>
     |      X.toTimeSpec(a, b) -> PythonQt.QtCore.QDateTime
     |  
     |  toTimeZone = <unbound qt slot toTimeZone of QDateTime type>
     |      X.toTimeZone(a, b) -> PythonQt.QtCore.QDateTime
     |  
     |  toTime_t = <unbound qt slot toTime_t of QDateTime type>
     |      X.toTime_t(a) -> int
     |  
     |  toUTC = <unbound qt slot toUTC of QDateTime type>
     |      X.toUTC(a) -> PythonQt.QtCore.QDateTime
     |  
     |  utcOffset = <unbound qt slot utcOffset of QDateTime type>
     |      X.utcOffset(a) -> int
     |  
     |  writeTo = <unbound qt slot writeTo of QDateTime type>
     |      X.writeTo(a, b)
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __delattr__(...)
     |      x.__delattr__('name') <==> del x.name
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __hash__(...)
     |      x.__hash__() <==> hash(x)
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __setattr__(...)
     |      x.__setattr__('name', value) <==> x.name = value
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __new__ = <built-in method __new__ of PythonQt.PythonQtClassWrapper ob...
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
    
    class QDeferredDeleteEvent(PythonQt.PythonQtInstanceWrapper)
     |  Method resolution order:
     |      QDeferredDeleteEvent
     |      PythonQt.PythonQtInstanceWrapper
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  __init__(...)
     |      x.__init__(...) initializes x; see help(type(x)) for signature
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  AcceptDropsChange = 152
     |  
     |  ActionAdded = 114
     |  
     |  ActionChanged = 113
     |  
     |  ActionRemoved = 115
     |  
     |  ActivateControl = 80
     |  
     |  ActivationChange = 99
     |  
     |  ApplicationActivate = 121
     |  
     |  ApplicationActivated = 121
     |  
     |  ApplicationDeactivate = 122
     |  
     |  ApplicationDeactivated = 122
     |  
     |  ApplicationFontChange = 36
     |  
     |  ApplicationLayoutDirectionChange = 37
     |  
     |  ApplicationPaletteChange = 38
     |  
     |  ApplicationStateChange = 214
     |  
     |  ApplicationWindowIconChange = 35
     |  
     |  ChildAdded = 68
     |  
     |  ChildPolished = 69
     |  
     |  ChildRemoved = 71
     |  
     |  Clipboard = 40
     |  
     |  Close = 19
     |  
     |  CloseSoftwareInputPanel = 200
     |  
     |  ContentsRectChange = 178
     |  
     |  ContextMenu = 82
     |  
     |  Create = 15
     |  
     |  CursorChange = 183
     |  
     |  DeactivateControl = 81
     |  
     |  DeferredDelete = 52
     |  
     |  Destroy = 16
     |  
     |  DragEnter = 60
     |  
     |  DragLeave = 62
     |  
     |  DragMove = 61
     |  
     |  DragResponse = 64
     |  
     |  Drop = 63
     |  
     |  DynamicPropertyChange = 170
     |  
     |  EmbeddingControl = 79
     |  
     |  EnabledChange = 98
     |  
     |  Enter = 10
     |  
     |  EnterWhatsThisMode = 124
     |  
     |  Expose = 206
     |  
     |  FileOpen = 116
     |  
     |  FocusAboutToChange = 23
     |  
     |  FocusIn = 8
     |  
     |  FocusOut = 9
     |  
     |  FontChange = 97
     |  
     |  FutureCallOut = 180
     |  
     |  Gesture = 198
     |  
     |  GestureOverride = 202
     |  
     |  GrabKeyboard = 188
     |  
     |  GrabMouse = 186
     |  
     |  GraphicsSceneContextMenu = 159
     |  
     |  GraphicsSceneDragEnter = 164
     |  
     |  GraphicsSceneDragLeave = 166
     |  
     |  GraphicsSceneDragMove = 165
     |  
     |  GraphicsSceneDrop = 167
     |  
     |  GraphicsSceneHelp = 163
     |  
     |  GraphicsSceneHoverEnter = 160
     |  
     |  GraphicsSceneHoverLeave = 162
     |  
     |  GraphicsSceneHoverMove = 161
     |  
     |  GraphicsSceneMouseDoubleClick = 158
     |  
     |  GraphicsSceneMouseMove = 155
     |  
     |  GraphicsSceneMousePress = 156
     |  
     |  GraphicsSceneMouseRelease = 157
     |  
     |  GraphicsSceneMove = 182
     |  
     |  GraphicsSceneResize = 181
     |  
     |  GraphicsSceneWheel = 168
     |  
     |  HelpRequest = 95
     |  
     |  Hide = 18
     |  
     |  HideToParent = 27
     |  
     |  HoverEnter = 127
     |  
     |  HoverLeave = 128
     |  
     |  HoverMove = 129
     |  
     |  IconDrag = 96
     |  
     |  IconTextChange = 101
     |  
     |  InputMethod = 83
     |  
     |  InputMethodQuery = 207
     |  
     |  KeyPress = 6
     |  
     |  KeyRelease = 7
     |  
     |  KeyboardLayoutChange = 169
     |  
     |  LanguageChange = 89
     |  
     |  LayoutDirectionChange = 90
     |  
     |  LayoutRequest = 76
     |  
     |  Leave = 11
     |  
     |  LeaveWhatsThisMode = 125
     |  
     |  LocaleChange = 88
     |  
     |  MacGLClearDrawable = 191
     |  
     |  MacGLWindowChange = 179
     |  
     |  MacSizeChange = 177
     |  
     |  MaxUser = 65535
     |  
     |  MetaCall = 43
     |  
     |  ModifiedChange = 102
     |  
     |  MouseButtonDblClick = 4
     |  
     |  MouseButtonPress = 2
     |  
     |  MouseButtonRelease = 3
     |  
     |  MouseMove = 5
     |  
     |  MouseTrackingChange = 109
     |  
     |  Move = 13
     |  
     |  NativeGesture = 197
     |  
     |  NetworkReplyUpdated = 185
     |  
     |  NonClientAreaMouseButtonDblClick = 176
     |  
     |  NonClientAreaMouseButtonPress = 174
     |  
     |  NonClientAreaMouseButtonRelease = 175
     |  
     |  NonClientAreaMouseMove = 173
     |  
     |  None = 0
     |  
     |  OkRequest = 94
     |  
     |  OrientationChange = 208
     |  
     |  Paint = 12
     |  
     |  PaletteChange = 39
     |  
     |  ParentAboutToChange = 131
     |  
     |  ParentChange = 21
     |  
     |  PlatformPanel = 212
     |  
     |  PlatformSurface = 217
     |  
     |  Polish = 75
     |  
     |  PolishRequest = 74
     |  
     |  QueryWhatsThis = 123
     |  
     |  Quit = 20
     |  
     |  ReadOnlyChange = 106
     |  
     |  RequestSoftwareInputPanel = 199
     |  
     |  Resize = 14
     |  
     |  ScreenChangeInternal = 216
     |  
     |  Scroll = 205
     |  
     |  ScrollPrepare = 204
     |  
     |  Shortcut = 117
     |  
     |  ShortcutOverride = 51
     |  
     |  Show = 17
     |  
     |  ShowToParent = 26
     |  
     |  ShowWindowRequest = 73
     |  
     |  SockAct = 50
     |  
     |  SockClose = 211
     |  
     |  Speech = 42
     |  
     |  StateMachineSignal = 192
     |  
     |  StateMachineWrapped = 193
     |  
     |  StatusTip = 112
     |  
     |  Style = 91
     |  
     |  StyleAnimationUpdate = 213
     |  
     |  StyleChange = 100
     |  
     |  TabletEnterProximity = 171
     |  
     |  TabletLeaveProximity = 172
     |  
     |  TabletMove = 87
     |  
     |  TabletPress = 92
     |  
     |  TabletRelease = 93
     |  
     |  ThemeChange = 210
     |  
     |  ThreadChange = 22
     |  
     |  Timer = 1
     |  
     |  ToolBarChange = 120
     |  
     |  ToolTip = 110
     |  
     |  ToolTipChange = 184
     |  
     |  TouchBegin = 194
     |  
     |  TouchCancel = 209
     |  
     |  TouchEnd = 196
     |  
     |  TouchUpdate = 195
     |  
     |  Type = <class 'PythonQt.QtCore.Type'>
     |  
     |  
     |  UngrabKeyboard = 189
     |  
     |  UngrabMouse = 187
     |  
     |  UpdateLater = 78
     |  
     |  UpdateRequest = 77
     |  
     |  User = 1000
     |  
     |  WhatsThis = 111
     |  
     |  WhatsThisClicked = 118
     |  
     |  Wheel = 31
     |  
     |  WinEventAct = 132
     |  
     |  WinIdChange = 203
     |  
     |  WindowActivate = 24
     |  
     |  WindowBlocked = 103
     |  
     |  WindowChangeInternal = 215
     |  
     |  WindowDeactivate = 25
     |  
     |  WindowIconChange = 34
     |  
     |  WindowStateChange = 105
     |  
     |  WindowTitleChange = 33
     |  
     |  WindowUnblocked = 104
     |  
     |  ZOrderChange = 126
     |  
     |  ZeroTimerEvent = 154
     |  
     |  accept = <unbound qt slot accept of QDeferredDeleteEvent type>
     |      X.accept(a)
     |  
     |  className = <built-in method className of PythonQt.PythonQtClassWrappe...
     |      Return the classname of the object
     |  
     |  delete = <built-in method delete of PythonQt.PythonQtClassWrapper obje...
     |      Deletes the given C++ object
     |  
     |  help = <built-in method help of PythonQt.PythonQtClassWrapper object>
     |      Shows the help of available methods for this class
     |  
     |  ignore = <unbound qt slot ignore of QDeferredDeleteEvent type>
     |      X.ignore(a)
     |  
     |  inherits = <built-in method inherits of PythonQt.PythonQtClassWrapper ...
     |      Returns if the class inherits or is of given type name
     |  
     |  isAccepted = <unbound qt slot isAccepted of QDeferredDeleteEvent type>
     |      X.isAccepted(a) -> bool
     |  
     |  loopLevel = <unbound qt slot loopLevel of QDeferredDeleteEvent type>
     |      X.loopLevel(a) -> int
     |  
     |  operator_assign = <unbound qt slot operator_assign of QDeferredDeleteE...
     |      X.operator_assign(a, b) -> PythonQt.QtCore.QEvent
     |  
     |  registerEventType = <unbound qt slot static_QEvent_registerEventType o...
     |      X.registerEventType(a) -> int
     |  
     |  setAccepted = <unbound qt slot setAccepted of QDeferredDeleteEvent typ...
     |      X.setAccepted(a, b)
     |  
     |  spontaneous = <unbound qt slot spontaneous of QDeferredDeleteEvent typ...
     |      X.spontaneous(a) -> bool
     |  
     |  type = <unbound qt slot type of QDeferredDeleteEvent type>
     |      X.type(a)
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __delattr__(...)
     |      x.__delattr__('name') <==> del x.name
     |  
     |  __eq__(...)
     |      x.__eq__(y) <==> x==y
     |  
     |  __ge__(...)
     |      x.__ge__(y) <==> x>=y
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __gt__(...)
     |      x.__gt__(y) <==> x>y
     |  
     |  __hash__(...)
     |      x.__hash__() <==> hash(x)
     |  
     |  __le__(...)
     |      x.__le__(y) <==> x<=y
     |  
     |  __lt__(...)
     |      x.__lt__(y) <==> x<y
     |  
     |  __ne__(...)
     |      x.__ne__(y) <==> x!=y
     |  
     |  __nonzero__(...)
     |      x.__nonzero__() <==> x != 0
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __setattr__(...)
     |      x.__setattr__('name', value) <==> x.name = value
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __new__ = <built-in method __new__ of PythonQt.PythonQtClassWrapper ob...
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
    
    class QDir(PythonQt.PythonQtInstanceWrapper)
     |  Method resolution order:
     |      QDir
     |      PythonQt.PythonQtInstanceWrapper
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  __eq__(...)
     |      x.__eq__(y) <==> x==y
     |  
     |  __init__(...)
     |      x.__init__(...) initializes x; see help(type(x)) for signature
     |  
     |  __ne__(...)
     |      x.__ne__(y) <==> x!=y
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  AccessMask = 1008
     |  
     |  AllDirs = 1024
     |  
     |  AllEntries = 7
     |  
     |  CaseSensitive = 2048
     |  
     |  Dirs = 1
     |  
     |  DirsFirst = 4
     |  
     |  DirsLast = 32
     |  
     |  Drives = 4
     |  
     |  Executable = 64
     |  
     |  Files = 2
     |  
     |  Filter = <class 'PythonQt.QtCore.Filter'>
     |  
     |  
     |  Filters = <class 'PythonQt.QtCore.Filters'>
     |  
     |  
     |  Hidden = 256
     |  
     |  IgnoreCase = 16
     |  
     |  LocaleAware = 64
     |  
     |  Modified = 128
     |  
     |  Name = 0
     |  
     |  NoDot = 8192
     |  
     |  NoDotAndDotDot = 24576
     |  
     |  NoDotDot = 16384
     |  
     |  NoFilter = -1
     |  
     |  NoSort = -1
     |  
     |  NoSymLinks = 8
     |  
     |  PermissionMask = 112
     |  
     |  Readable = 16
     |  
     |  Reversed = 8
     |  
     |  Size = 2
     |  
     |  SortByMask = 3
     |  
     |  SortFlag = <class 'PythonQt.QtCore.SortFlag'>
     |  
     |  
     |  SortFlags = <class 'PythonQt.QtCore.SortFlags'>
     |  
     |  
     |  System = 512
     |  
     |  Time = 1
     |  
     |  Type = 128
     |  
     |  TypeMask = 15
     |  
     |  Unsorted = 3
     |  
     |  Writable = 32
     |  
     |  absoluteFilePath = <unbound qt slot absoluteFilePath of QDir type>
     |      X.absoluteFilePath(a, b) -> str
     |  
     |  absolutePath = <unbound qt slot absolutePath of QDir type>
     |      X.absolutePath(a) -> str
     |  
     |  addSearchPath = <unbound qt slot static_QDir_addSearchPath of QDir typ...
     |      X.addSearchPath(a, b)
     |  
     |  canonicalPath = <unbound qt slot canonicalPath of QDir type>
     |      X.canonicalPath(a) -> str
     |  
     |  cd = <unbound qt slot cd of QDir type>
     |      X.cd(a, b) -> bool
     |  
     |  cdUp = <unbound qt slot cdUp of QDir type>
     |      X.cdUp(a) -> bool
     |  
     |  className = <built-in method className of PythonQt.PythonQtClassWrappe...
     |      Return the classname of the object
     |  
     |  cleanPath = <unbound qt slot static_QDir_cleanPath of QDir type>
     |      X.cleanPath(a) -> str
     |  
     |  count = <unbound qt slot count of QDir type>
     |      X.count(a) -> int
     |  
     |  current = <unbound qt slot static_QDir_current of QDir type>
     |      X.current() -> PythonQt.QtCore.QDir
     |  
     |  currentPath = <unbound qt slot static_QDir_currentPath of QDir type>
     |      X.currentPath() -> str
     |  
     |  delete = <built-in method delete of PythonQt.PythonQtClassWrapper obje...
     |      Deletes the given C++ object
     |  
     |  dirName = <unbound qt slot dirName of QDir type>
     |      X.dirName(a) -> str
     |  
     |  drives = <unbound qt slot static_QDir_drives of QDir type>
     |      X.drives() -> tuple
     |  
     |  entryInfoList = <unbound qt slot entryInfoList of QDir type>
     |      X.entryInfoList(a, b, c, d) -> tuple
     |  
     |  entryList = <unbound qt slot entryList of QDir type>
     |      X.entryList(a, b, c, d) -> tuple
     |  
     |  exists = <unbound qt slot exists of QDir type>
     |      X.exists(a, b) -> bool
     |  
     |  filePath = <unbound qt slot filePath of QDir type>
     |      X.filePath(a, b) -> str
     |  
     |  filter = <unbound qt slot filter of QDir type>
     |      X.filter(a)
     |  
     |  fromNativeSeparators = <unbound qt slot static_QDir_fromNativeSeparato...
     |      X.fromNativeSeparators(a) -> str
     |  
     |  help = <built-in method help of PythonQt.PythonQtClassWrapper object>
     |      Shows the help of available methods for this class
     |  
     |  home = <unbound qt slot static_QDir_home of QDir type>
     |      X.home() -> PythonQt.QtCore.QDir
     |  
     |  homePath = <unbound qt slot static_QDir_homePath of QDir type>
     |      X.homePath() -> str
     |  
     |  inherits = <built-in method inherits of PythonQt.PythonQtClassWrapper ...
     |      Returns if the class inherits or is of given type name
     |  
     |  isAbsolute = <unbound qt slot isAbsolute of QDir type>
     |      X.isAbsolute(a) -> bool
     |  
     |  isAbsolutePath = <unbound qt slot static_QDir_isAbsolutePath of QDir t...
     |      X.isAbsolutePath(a) -> bool
     |  
     |  isReadable = <unbound qt slot isReadable of QDir type>
     |      X.isReadable(a) -> bool
     |  
     |  isRelative = <unbound qt slot isRelative of QDir type>
     |      X.isRelative(a) -> bool
     |  
     |  isRelativePath = <unbound qt slot static_QDir_isRelativePath of QDir t...
     |      X.isRelativePath(a) -> bool
     |  
     |  isRoot = <unbound qt slot isRoot of QDir type>
     |      X.isRoot(a) -> bool
     |  
     |  listSeparator = <unbound qt slot static_QDir_listSeparator of QDir typ...
     |      X.listSeparator()
     |  
     |  makeAbsolute = <unbound qt slot makeAbsolute of QDir type>
     |      X.makeAbsolute(a) -> bool
     |  
     |  match = <unbound qt slot static_QDir_match of QDir type>
     |      X.match(a, b) -> bool
     |  
     |  mkdir = <unbound qt slot mkdir of QDir type>
     |      X.mkdir(a, b) -> bool
     |  
     |  mkpath = <unbound qt slot mkpath of QDir type>
     |      X.mkpath(a, b) -> bool
     |  
     |  nameFilters = <unbound qt slot nameFilters of QDir type>
     |      X.nameFilters(a) -> tuple
     |  
     |  nameFiltersFromString = <unbound qt slot static_QDir_nameFiltersFromSt...
     |      X.nameFiltersFromString(a) -> tuple
     |  
     |  operator_subscript = <unbound qt slot operator_subscript of QDir type>
     |      X.operator_subscript(a, b) -> str
     |  
     |  path = <unbound qt slot path of QDir type>
     |      X.path(a) -> str
     |  
     |  refresh = <unbound qt slot refresh of QDir type>
     |      X.refresh(a)
     |  
     |  relativeFilePath = <unbound qt slot relativeFilePath of QDir type>
     |      X.relativeFilePath(a, b) -> str
     |  
     |  remove = <unbound qt slot remove of QDir type>
     |      X.remove(a, b) -> bool
     |  
     |  removeRecursively = <unbound qt slot removeRecursively of QDir type>
     |      X.removeRecursively(a) -> bool
     |  
     |  rename = <unbound qt slot rename of QDir type>
     |      X.rename(a, b, c) -> bool
     |  
     |  rmdir = <unbound qt slot rmdir of QDir type>
     |      X.rmdir(a, b) -> bool
     |  
     |  rmpath = <unbound qt slot rmpath of QDir type>
     |      X.rmpath(a, b) -> bool
     |  
     |  root = <unbound qt slot static_QDir_root of QDir type>
     |      X.root() -> PythonQt.QtCore.QDir
     |  
     |  rootPath = <unbound qt slot static_QDir_rootPath of QDir type>
     |      X.rootPath() -> str
     |  
     |  searchPaths = <unbound qt slot static_QDir_searchPaths of QDir type>
     |      X.searchPaths(a) -> tuple
     |  
     |  separator = <unbound qt slot static_QDir_separator of QDir type>
     |      X.separator()
     |  
     |  setCurrent = <unbound qt slot static_QDir_setCurrent of QDir type>
     |      X.setCurrent(a) -> bool
     |  
     |  setFilter = <unbound qt slot setFilter of QDir type>
     |      X.setFilter(a, b)
     |  
     |  setNameFilters = <unbound qt slot setNameFilters of QDir type>
     |      X.setNameFilters(a, b)
     |  
     |  setPath = <unbound qt slot setPath of QDir type>
     |      X.setPath(a, b)
     |  
     |  setSearchPaths = <unbound qt slot static_QDir_setSearchPaths of QDir t...
     |      X.setSearchPaths(a, b)
     |  
     |  setSorting = <unbound qt slot setSorting of QDir type>
     |      X.setSorting(a, b)
     |  
     |  sorting = <unbound qt slot sorting of QDir type>
     |      X.sorting(a)
     |  
     |  swap = <unbound qt slot swap of QDir type>
     |      X.swap(a, b)
     |  
     |  temp = <unbound qt slot static_QDir_temp of QDir type>
     |      X.temp() -> PythonQt.QtCore.QDir
     |  
     |  tempPath = <unbound qt slot static_QDir_tempPath of QDir type>
     |      X.tempPath() -> str
     |  
     |  toNativeSeparators = <unbound qt slot static_QDir_toNativeSeparators o...
     |      X.toNativeSeparators(a) -> str
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __delattr__(...)
     |      x.__delattr__('name') <==> del x.name
     |  
     |  __ge__(...)
     |      x.__ge__(y) <==> x>=y
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __gt__(...)
     |      x.__gt__(y) <==> x>y
     |  
     |  __hash__(...)
     |      x.__hash__() <==> hash(x)
     |  
     |  __le__(...)
     |      x.__le__(y) <==> x<=y
     |  
     |  __lt__(...)
     |      x.__lt__(y) <==> x<y
     |  
     |  __nonzero__(...)
     |      x.__nonzero__() <==> x != 0
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __setattr__(...)
     |      x.__setattr__('name', value) <==> x.name = value
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __new__ = <built-in method __new__ of PythonQt.PythonQtClassWrapper ob...
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
    
    class QDirIterator(PythonQt.PythonQtInstanceWrapper)
     |  Method resolution order:
     |      QDirIterator
     |      PythonQt.PythonQtInstanceWrapper
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  __init__(...)
     |      x.__init__(...) initializes x; see help(type(x)) for signature
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  FollowSymlinks = 1
     |  
     |  IteratorFlag = <class 'PythonQt.QtCore.IteratorFlag'>
     |  
     |  
     |  IteratorFlags = <class 'PythonQt.QtCore.IteratorFlags'>
     |  
     |  
     |  NoIteratorFlags = 0
     |  
     |  Subdirectories = 2
     |  
     |  className = <built-in method className of PythonQt.PythonQtClassWrappe...
     |      Return the classname of the object
     |  
     |  delete = <built-in method delete of PythonQt.PythonQtClassWrapper obje...
     |      Deletes the given C++ object
     |  
     |  fileInfo = <unbound qt slot fileInfo of QDirIterator type>
     |      X.fileInfo(a) -> PythonQt.QtCore.QFileInfo
     |  
     |  fileName = <unbound qt slot fileName of QDirIterator type>
     |      X.fileName(a) -> str
     |  
     |  filePath = <unbound qt slot filePath of QDirIterator type>
     |      X.filePath(a) -> str
     |  
     |  hasNext = <unbound qt slot hasNext of QDirIterator type>
     |      X.hasNext(a) -> bool
     |  
     |  help = <built-in method help of PythonQt.PythonQtClassWrapper object>
     |      Shows the help of available methods for this class
     |  
     |  inherits = <built-in method inherits of PythonQt.PythonQtClassWrapper ...
     |      Returns if the class inherits or is of given type name
     |  
     |  next = <unbound qt slot next of QDirIterator type>
     |      X.next(a) -> str
     |  
     |  path = <unbound qt slot path of QDirIterator type>
     |      X.path(a) -> str
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __delattr__(...)
     |      x.__delattr__('name') <==> del x.name
     |  
     |  __eq__(...)
     |      x.__eq__(y) <==> x==y
     |  
     |  __ge__(...)
     |      x.__ge__(y) <==> x>=y
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __gt__(...)
     |      x.__gt__(y) <==> x>y
     |  
     |  __hash__(...)
     |      x.__hash__() <==> hash(x)
     |  
     |  __le__(...)
     |      x.__le__(y) <==> x<=y
     |  
     |  __lt__(...)
     |      x.__lt__(y) <==> x<y
     |  
     |  __ne__(...)
     |      x.__ne__(y) <==> x!=y
     |  
     |  __nonzero__(...)
     |      x.__nonzero__() <==> x != 0
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __setattr__(...)
     |      x.__setattr__('name', value) <==> x.name = value
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __new__ = <built-in method __new__ of PythonQt.PythonQtClassWrapper ob...
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
    
    class QDynamicPropertyChangeEvent(PythonQt.PythonQtInstanceWrapper)
     |  Method resolution order:
     |      QDynamicPropertyChangeEvent
     |      PythonQt.PythonQtInstanceWrapper
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  __init__(...)
     |      x.__init__(...) initializes x; see help(type(x)) for signature
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  AcceptDropsChange = 152
     |  
     |  ActionAdded = 114
     |  
     |  ActionChanged = 113
     |  
     |  ActionRemoved = 115
     |  
     |  ActivateControl = 80
     |  
     |  ActivationChange = 99
     |  
     |  ApplicationActivate = 121
     |  
     |  ApplicationActivated = 121
     |  
     |  ApplicationDeactivate = 122
     |  
     |  ApplicationDeactivated = 122
     |  
     |  ApplicationFontChange = 36
     |  
     |  ApplicationLayoutDirectionChange = 37
     |  
     |  ApplicationPaletteChange = 38
     |  
     |  ApplicationStateChange = 214
     |  
     |  ApplicationWindowIconChange = 35
     |  
     |  ChildAdded = 68
     |  
     |  ChildPolished = 69
     |  
     |  ChildRemoved = 71
     |  
     |  Clipboard = 40
     |  
     |  Close = 19
     |  
     |  CloseSoftwareInputPanel = 200
     |  
     |  ContentsRectChange = 178
     |  
     |  ContextMenu = 82
     |  
     |  Create = 15
     |  
     |  CursorChange = 183
     |  
     |  DeactivateControl = 81
     |  
     |  DeferredDelete = 52
     |  
     |  Destroy = 16
     |  
     |  DragEnter = 60
     |  
     |  DragLeave = 62
     |  
     |  DragMove = 61
     |  
     |  DragResponse = 64
     |  
     |  Drop = 63
     |  
     |  DynamicPropertyChange = 170
     |  
     |  EmbeddingControl = 79
     |  
     |  EnabledChange = 98
     |  
     |  Enter = 10
     |  
     |  EnterWhatsThisMode = 124
     |  
     |  Expose = 206
     |  
     |  FileOpen = 116
     |  
     |  FocusAboutToChange = 23
     |  
     |  FocusIn = 8
     |  
     |  FocusOut = 9
     |  
     |  FontChange = 97
     |  
     |  FutureCallOut = 180
     |  
     |  Gesture = 198
     |  
     |  GestureOverride = 202
     |  
     |  GrabKeyboard = 188
     |  
     |  GrabMouse = 186
     |  
     |  GraphicsSceneContextMenu = 159
     |  
     |  GraphicsSceneDragEnter = 164
     |  
     |  GraphicsSceneDragLeave = 166
     |  
     |  GraphicsSceneDragMove = 165
     |  
     |  GraphicsSceneDrop = 167
     |  
     |  GraphicsSceneHelp = 163
     |  
     |  GraphicsSceneHoverEnter = 160
     |  
     |  GraphicsSceneHoverLeave = 162
     |  
     |  GraphicsSceneHoverMove = 161
     |  
     |  GraphicsSceneMouseDoubleClick = 158
     |  
     |  GraphicsSceneMouseMove = 155
     |  
     |  GraphicsSceneMousePress = 156
     |  
     |  GraphicsSceneMouseRelease = 157
     |  
     |  GraphicsSceneMove = 182
     |  
     |  GraphicsSceneResize = 181
     |  
     |  GraphicsSceneWheel = 168
     |  
     |  HelpRequest = 95
     |  
     |  Hide = 18
     |  
     |  HideToParent = 27
     |  
     |  HoverEnter = 127
     |  
     |  HoverLeave = 128
     |  
     |  HoverMove = 129
     |  
     |  IconDrag = 96
     |  
     |  IconTextChange = 101
     |  
     |  InputMethod = 83
     |  
     |  InputMethodQuery = 207
     |  
     |  KeyPress = 6
     |  
     |  KeyRelease = 7
     |  
     |  KeyboardLayoutChange = 169
     |  
     |  LanguageChange = 89
     |  
     |  LayoutDirectionChange = 90
     |  
     |  LayoutRequest = 76
     |  
     |  Leave = 11
     |  
     |  LeaveWhatsThisMode = 125
     |  
     |  LocaleChange = 88
     |  
     |  MacGLClearDrawable = 191
     |  
     |  MacGLWindowChange = 179
     |  
     |  MacSizeChange = 177
     |  
     |  MaxUser = 65535
     |  
     |  MetaCall = 43
     |  
     |  ModifiedChange = 102
     |  
     |  MouseButtonDblClick = 4
     |  
     |  MouseButtonPress = 2
     |  
     |  MouseButtonRelease = 3
     |  
     |  MouseMove = 5
     |  
     |  MouseTrackingChange = 109
     |  
     |  Move = 13
     |  
     |  NativeGesture = 197
     |  
     |  NetworkReplyUpdated = 185
     |  
     |  NonClientAreaMouseButtonDblClick = 176
     |  
     |  NonClientAreaMouseButtonPress = 174
     |  
     |  NonClientAreaMouseButtonRelease = 175
     |  
     |  NonClientAreaMouseMove = 173
     |  
     |  None = 0
     |  
     |  OkRequest = 94
     |  
     |  OrientationChange = 208
     |  
     |  Paint = 12
     |  
     |  PaletteChange = 39
     |  
     |  ParentAboutToChange = 131
     |  
     |  ParentChange = 21
     |  
     |  PlatformPanel = 212
     |  
     |  PlatformSurface = 217
     |  
     |  Polish = 75
     |  
     |  PolishRequest = 74
     |  
     |  QueryWhatsThis = 123
     |  
     |  Quit = 20
     |  
     |  ReadOnlyChange = 106
     |  
     |  RequestSoftwareInputPanel = 199
     |  
     |  Resize = 14
     |  
     |  ScreenChangeInternal = 216
     |  
     |  Scroll = 205
     |  
     |  ScrollPrepare = 204
     |  
     |  Shortcut = 117
     |  
     |  ShortcutOverride = 51
     |  
     |  Show = 17
     |  
     |  ShowToParent = 26
     |  
     |  ShowWindowRequest = 73
     |  
     |  SockAct = 50
     |  
     |  SockClose = 211
     |  
     |  Speech = 42
     |  
     |  StateMachineSignal = 192
     |  
     |  StateMachineWrapped = 193
     |  
     |  StatusTip = 112
     |  
     |  Style = 91
     |  
     |  StyleAnimationUpdate = 213
     |  
     |  StyleChange = 100
     |  
     |  TabletEnterProximity = 171
     |  
     |  TabletLeaveProximity = 172
     |  
     |  TabletMove = 87
     |  
     |  TabletPress = 92
     |  
     |  TabletRelease = 93
     |  
     |  ThemeChange = 210
     |  
     |  ThreadChange = 22
     |  
     |  Timer = 1
     |  
     |  ToolBarChange = 120
     |  
     |  ToolTip = 110
     |  
     |  ToolTipChange = 184
     |  
     |  TouchBegin = 194
     |  
     |  TouchCancel = 209
     |  
     |  TouchEnd = 196
     |  
     |  TouchUpdate = 195
     |  
     |  Type = <class 'PythonQt.QtCore.Type'>
     |  
     |  
     |  UngrabKeyboard = 189
     |  
     |  UngrabMouse = 187
     |  
     |  UpdateLater = 78
     |  
     |  UpdateRequest = 77
     |  
     |  User = 1000
     |  
     |  WhatsThis = 111
     |  
     |  WhatsThisClicked = 118
     |  
     |  Wheel = 31
     |  
     |  WinEventAct = 132
     |  
     |  WinIdChange = 203
     |  
     |  WindowActivate = 24
     |  
     |  WindowBlocked = 103
     |  
     |  WindowChangeInternal = 215
     |  
     |  WindowDeactivate = 25
     |  
     |  WindowIconChange = 34
     |  
     |  WindowStateChange = 105
     |  
     |  WindowTitleChange = 33
     |  
     |  WindowUnblocked = 104
     |  
     |  ZOrderChange = 126
     |  
     |  ZeroTimerEvent = 154
     |  
     |  accept = <unbound qt slot accept of QDynamicPropertyChangeEvent type>
     |      X.accept(a)
     |  
     |  className = <built-in method className of PythonQt.PythonQtClassWrappe...
     |      Return the classname of the object
     |  
     |  delete = <built-in method delete of PythonQt.PythonQtClassWrapper obje...
     |      Deletes the given C++ object
     |  
     |  help = <built-in method help of PythonQt.PythonQtClassWrapper object>
     |      Shows the help of available methods for this class
     |  
     |  ignore = <unbound qt slot ignore of QDynamicPropertyChangeEvent type>
     |      X.ignore(a)
     |  
     |  inherits = <built-in method inherits of PythonQt.PythonQtClassWrapper ...
     |      Returns if the class inherits or is of given type name
     |  
     |  isAccepted = <unbound qt slot isAccepted of QDynamicPropertyChangeEven...
     |      X.isAccepted(a) -> bool
     |  
     |  operator_assign = <unbound qt slot operator_assign of QDynamicProperty...
     |      X.operator_assign(a, b) -> PythonQt.QtCore.QEvent
     |  
     |  propertyName = <unbound qt slot propertyName of QDynamicPropertyChange...
     |      X.propertyName(a) -> PythonQt.QtCore.QByteArray
     |  
     |  registerEventType = <unbound qt slot static_QEvent_registerEventType o...
     |      X.registerEventType(a) -> int
     |  
     |  setAccepted = <unbound qt slot setAccepted of QDynamicPropertyChangeEv...
     |      X.setAccepted(a, b)
     |  
     |  spontaneous = <unbound qt slot spontaneous of QDynamicPropertyChangeEv...
     |      X.spontaneous(a) -> bool
     |  
     |  type = <unbound qt slot type of QDynamicPropertyChangeEvent type>
     |      X.type(a)
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __delattr__(...)
     |      x.__delattr__('name') <==> del x.name
     |  
     |  __eq__(...)
     |      x.__eq__(y) <==> x==y
     |  
     |  __ge__(...)
     |      x.__ge__(y) <==> x>=y
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __gt__(...)
     |      x.__gt__(y) <==> x>y
     |  
     |  __hash__(...)
     |      x.__hash__() <==> hash(x)
     |  
     |  __le__(...)
     |      x.__le__(y) <==> x<=y
     |  
     |  __lt__(...)
     |      x.__lt__(y) <==> x<y
     |  
     |  __ne__(...)
     |      x.__ne__(y) <==> x!=y
     |  
     |  __nonzero__(...)
     |      x.__nonzero__() <==> x != 0
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __setattr__(...)
     |      x.__setattr__('name', value) <==> x.name = value
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __new__ = <built-in method __new__ of PythonQt.PythonQtClassWrapper ob...
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
    
    class QEasingCurve(PythonQt.PythonQtInstanceWrapper)
     |  Method resolution order:
     |      QEasingCurve
     |      PythonQt.PythonQtInstanceWrapper
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  __eq__(...)
     |      x.__eq__(y) <==> x==y
     |  
     |  __init__(...)
     |      x.__init__(...) initializes x; see help(type(x)) for signature
     |  
     |  __ne__(...)
     |      x.__ne__(y) <==> x!=y
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  BezierSpline = 45
     |  
     |  CosineCurve = 44
     |  
     |  Custom = 47
     |  
     |  InBack = 33
     |  
     |  InBounce = 37
     |  
     |  InCirc = 25
     |  
     |  InCubic = 5
     |  
     |  InCurve = 41
     |  
     |  InElastic = 29
     |  
     |  InExpo = 21
     |  
     |  InOutBack = 35
     |  
     |  InOutBounce = 39
     |  
     |  InOutCirc = 27
     |  
     |  InOutCubic = 7
     |  
     |  InOutElastic = 31
     |  
     |  InOutExpo = 23
     |  
     |  InOutQuad = 3
     |  
     |  InOutQuart = 11
     |  
     |  InOutQuint = 15
     |  
     |  InOutSine = 19
     |  
     |  InQuad = 1
     |  
     |  InQuart = 9
     |  
     |  InQuint = 13
     |  
     |  InSine = 17
     |  
     |  Linear = 0
     |  
     |  NCurveTypes = 48
     |  
     |  OutBack = 34
     |  
     |  OutBounce = 38
     |  
     |  OutCirc = 26
     |  
     |  OutCubic = 6
     |  
     |  OutCurve = 42
     |  
     |  OutElastic = 30
     |  
     |  OutExpo = 22
     |  
     |  OutInBack = 36
     |  
     |  OutInBounce = 40
     |  
     |  OutInCirc = 28
     |  
     |  OutInCubic = 8
     |  
     |  OutInElastic = 32
     |  
     |  OutInExpo = 24
     |  
     |  OutInQuad = 4
     |  
     |  OutInQuart = 12
     |  
     |  OutInQuint = 16
     |  
     |  OutInSine = 20
     |  
     |  OutQuad = 2
     |  
     |  OutQuart = 10
     |  
     |  OutQuint = 14
     |  
     |  OutSine = 18
     |  
     |  SineCurve = 43
     |  
     |  TCBSpline = 46
     |  
     |  Type = <class 'PythonQt.QtCore.Type'>
     |  
     |  
     |  addCubicBezierSegment = <unbound qt slot addCubicBezierSegment of QEas...
     |      X.addCubicBezierSegment(a, b, c, d)
     |  
     |  addTCBSegment = <unbound qt slot addTCBSegment of QEasingCurve type>
     |      X.addTCBSegment(a, b, c, d, e)
     |  
     |  amplitude = <unbound qt slot amplitude of QEasingCurve type>
     |      X.amplitude(a) -> float
     |  
     |  className = <built-in method className of PythonQt.PythonQtClassWrappe...
     |      Return the classname of the object
     |  
     |  delete = <built-in method delete of PythonQt.PythonQtClassWrapper obje...
     |      Deletes the given C++ object
     |  
     |  help = <built-in method help of PythonQt.PythonQtClassWrapper object>
     |      Shows the help of available methods for this class
     |  
     |  inherits = <built-in method inherits of PythonQt.PythonQtClassWrapper ...
     |      Returns if the class inherits or is of given type name
     |  
     |  operator_assign = <unbound qt slot operator_assign of QEasingCurve typ...
     |      X.operator_assign(a, b) -> PythonQt.QtCore.QEasingCurve
     |  
     |  overshoot = <unbound qt slot overshoot of QEasingCurve type>
     |      X.overshoot(a) -> float
     |  
     |  period = <unbound qt slot period of QEasingCurve type>
     |      X.period(a) -> float
     |  
     |  readFrom = <unbound qt slot readFrom of QEasingCurve type>
     |      X.readFrom(a, b)
     |  
     |  setAmplitude = <unbound qt slot setAmplitude of QEasingCurve type>
     |      X.setAmplitude(a, b)
     |  
     |  setOvershoot = <unbound qt slot setOvershoot of QEasingCurve type>
     |      X.setOvershoot(a, b)
     |  
     |  setPeriod = <unbound qt slot setPeriod of QEasingCurve type>
     |      X.setPeriod(a, b)
     |  
     |  setType = <unbound qt slot setType of QEasingCurve type>
     |      X.setType(a, b)
     |  
     |  swap = <unbound qt slot swap of QEasingCurve type>
     |      X.swap(a, b)
     |  
     |  toCubicSpline = <unbound qt slot toCubicSpline of QEasingCurve type>
     |      X.toCubicSpline(a) -> tuple
     |  
     |  type = <unbound qt slot type of QEasingCurve type>
     |      X.type(a)
     |  
     |  valueForProgress = <unbound qt slot valueForProgress of QEasingCurve t...
     |      X.valueForProgress(a, b) -> float
     |  
     |  writeTo = <unbound qt slot writeTo of QEasingCurve type>
     |      X.writeTo(a, b)
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __delattr__(...)
     |      x.__delattr__('name') <==> del x.name
     |  
     |  __ge__(...)
     |      x.__ge__(y) <==> x>=y
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __gt__(...)
     |      x.__gt__(y) <==> x>y
     |  
     |  __hash__(...)
     |      x.__hash__() <==> hash(x)
     |  
     |  __le__(...)
     |      x.__le__(y) <==> x<=y
     |  
     |  __lt__(...)
     |      x.__lt__(y) <==> x<y
     |  
     |  __nonzero__(...)
     |      x.__nonzero__() <==> x != 0
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __setattr__(...)
     |      x.__setattr__('name', value) <==> x.name = value
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __new__ = <built-in method __new__ of PythonQt.PythonQtClassWrapper ob...
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
    
    class QElapsedTimer(PythonQt.PythonQtInstanceWrapper)
     |  Method resolution order:
     |      QElapsedTimer
     |      PythonQt.PythonQtInstanceWrapper
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  __eq__(...)
     |      x.__eq__(y) <==> x==y
     |  
     |  __init__(...)
     |      x.__init__(...) initializes x; see help(type(x)) for signature
     |  
     |  __ne__(...)
     |      x.__ne__(y) <==> x!=y
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  ClockType = <class 'PythonQt.QtCore.ClockType'>
     |  
     |  
     |  MachAbsoluteTime = 3
     |  
     |  MonotonicClock = 1
     |  
     |  PerformanceCounter = 4
     |  
     |  SystemTime = 0
     |  
     |  TickCounter = 2
     |  
     |  className = <built-in method className of PythonQt.PythonQtClassWrappe...
     |      Return the classname of the object
     |  
     |  clockType = <unbound qt slot static_QElapsedTimer_clockType of QElapse...
     |      X.clockType()
     |  
     |  delete = <built-in method delete of PythonQt.PythonQtClassWrapper obje...
     |      Deletes the given C++ object
     |  
     |  elapsed = <unbound qt slot elapsed of QElapsedTimer type>
     |      X.elapsed(a) -> int
     |  
     |  hasExpired = <unbound qt slot hasExpired of QElapsedTimer type>
     |      X.hasExpired(a, b) -> bool
     |  
     |  help = <built-in method help of PythonQt.PythonQtClassWrapper object>
     |      Shows the help of available methods for this class
     |  
     |  inherits = <built-in method inherits of PythonQt.PythonQtClassWrapper ...
     |      Returns if the class inherits or is of given type name
     |  
     |  invalidate = <unbound qt slot invalidate of QElapsedTimer type>
     |      X.invalidate(a)
     |  
     |  isMonotonic = <unbound qt slot static_QElapsedTimer_isMonotonic of QEl...
     |      X.isMonotonic() -> bool
     |  
     |  isValid = <unbound qt slot isValid of QElapsedTimer type>
     |      X.isValid(a) -> bool
     |  
     |  msecsSinceReference = <unbound qt slot msecsSinceReference of QElapsed...
     |      X.msecsSinceReference(a) -> int
     |  
     |  msecsTo = <unbound qt slot msecsTo of QElapsedTimer type>
     |      X.msecsTo(a, b) -> int
     |  
     |  nsecsElapsed = <unbound qt slot nsecsElapsed of QElapsedTimer type>
     |      X.nsecsElapsed(a) -> int
     |  
     |  restart = <unbound qt slot restart of QElapsedTimer type>
     |      X.restart(a) -> int
     |  
     |  secsTo = <unbound qt slot secsTo of QElapsedTimer type>
     |      X.secsTo(a, b) -> int
     |  
     |  start = <unbound qt slot start of QElapsedTimer type>
     |      X.start(a)
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __delattr__(...)
     |      x.__delattr__('name') <==> del x.name
     |  
     |  __ge__(...)
     |      x.__ge__(y) <==> x>=y
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __gt__(...)
     |      x.__gt__(y) <==> x>y
     |  
     |  __hash__(...)
     |      x.__hash__() <==> hash(x)
     |  
     |  __le__(...)
     |      x.__le__(y) <==> x<=y
     |  
     |  __lt__(...)
     |      x.__lt__(y) <==> x<y
     |  
     |  __nonzero__(...)
     |      x.__nonzero__() <==> x != 0
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __setattr__(...)
     |      x.__setattr__('name', value) <==> x.name = value
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __new__ = <built-in method __new__ of PythonQt.PythonQtClassWrapper ob...
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
    
    class QEvent(PythonQt.PythonQtInstanceWrapper)
     |  Method resolution order:
     |      QEvent
     |      PythonQt.PythonQtInstanceWrapper
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  __init__(...)
     |      x.__init__(...) initializes x; see help(type(x)) for signature
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  AcceptDropsChange = 152
     |  
     |  ActionAdded = 114
     |  
     |  ActionChanged = 113
     |  
     |  ActionRemoved = 115
     |  
     |  ActivateControl = 80
     |  
     |  ActivationChange = 99
     |  
     |  ApplicationActivate = 121
     |  
     |  ApplicationActivated = 121
     |  
     |  ApplicationDeactivate = 122
     |  
     |  ApplicationDeactivated = 122
     |  
     |  ApplicationFontChange = 36
     |  
     |  ApplicationLayoutDirectionChange = 37
     |  
     |  ApplicationPaletteChange = 38
     |  
     |  ApplicationStateChange = 214
     |  
     |  ApplicationWindowIconChange = 35
     |  
     |  ChildAdded = 68
     |  
     |  ChildPolished = 69
     |  
     |  ChildRemoved = 71
     |  
     |  Clipboard = 40
     |  
     |  Close = 19
     |  
     |  CloseSoftwareInputPanel = 200
     |  
     |  ContentsRectChange = 178
     |  
     |  ContextMenu = 82
     |  
     |  Create = 15
     |  
     |  CursorChange = 183
     |  
     |  DeactivateControl = 81
     |  
     |  DeferredDelete = 52
     |  
     |  Destroy = 16
     |  
     |  DragEnter = 60
     |  
     |  DragLeave = 62
     |  
     |  DragMove = 61
     |  
     |  DragResponse = 64
     |  
     |  Drop = 63
     |  
     |  DynamicPropertyChange = 170
     |  
     |  EmbeddingControl = 79
     |  
     |  EnabledChange = 98
     |  
     |  Enter = 10
     |  
     |  EnterWhatsThisMode = 124
     |  
     |  Expose = 206
     |  
     |  FileOpen = 116
     |  
     |  FocusAboutToChange = 23
     |  
     |  FocusIn = 8
     |  
     |  FocusOut = 9
     |  
     |  FontChange = 97
     |  
     |  FutureCallOut = 180
     |  
     |  Gesture = 198
     |  
     |  GestureOverride = 202
     |  
     |  GrabKeyboard = 188
     |  
     |  GrabMouse = 186
     |  
     |  GraphicsSceneContextMenu = 159
     |  
     |  GraphicsSceneDragEnter = 164
     |  
     |  GraphicsSceneDragLeave = 166
     |  
     |  GraphicsSceneDragMove = 165
     |  
     |  GraphicsSceneDrop = 167
     |  
     |  GraphicsSceneHelp = 163
     |  
     |  GraphicsSceneHoverEnter = 160
     |  
     |  GraphicsSceneHoverLeave = 162
     |  
     |  GraphicsSceneHoverMove = 161
     |  
     |  GraphicsSceneMouseDoubleClick = 158
     |  
     |  GraphicsSceneMouseMove = 155
     |  
     |  GraphicsSceneMousePress = 156
     |  
     |  GraphicsSceneMouseRelease = 157
     |  
     |  GraphicsSceneMove = 182
     |  
     |  GraphicsSceneResize = 181
     |  
     |  GraphicsSceneWheel = 168
     |  
     |  HelpRequest = 95
     |  
     |  Hide = 18
     |  
     |  HideToParent = 27
     |  
     |  HoverEnter = 127
     |  
     |  HoverLeave = 128
     |  
     |  HoverMove = 129
     |  
     |  IconDrag = 96
     |  
     |  IconTextChange = 101
     |  
     |  InputMethod = 83
     |  
     |  InputMethodQuery = 207
     |  
     |  KeyPress = 6
     |  
     |  KeyRelease = 7
     |  
     |  KeyboardLayoutChange = 169
     |  
     |  LanguageChange = 89
     |  
     |  LayoutDirectionChange = 90
     |  
     |  LayoutRequest = 76
     |  
     |  Leave = 11
     |  
     |  LeaveWhatsThisMode = 125
     |  
     |  LocaleChange = 88
     |  
     |  MacGLClearDrawable = 191
     |  
     |  MacGLWindowChange = 179
     |  
     |  MacSizeChange = 177
     |  
     |  MaxUser = 65535
     |  
     |  MetaCall = 43
     |  
     |  ModifiedChange = 102
     |  
     |  MouseButtonDblClick = 4
     |  
     |  MouseButtonPress = 2
     |  
     |  MouseButtonRelease = 3
     |  
     |  MouseMove = 5
     |  
     |  MouseTrackingChange = 109
     |  
     |  Move = 13
     |  
     |  NativeGesture = 197
     |  
     |  NetworkReplyUpdated = 185
     |  
     |  NonClientAreaMouseButtonDblClick = 176
     |  
     |  NonClientAreaMouseButtonPress = 174
     |  
     |  NonClientAreaMouseButtonRelease = 175
     |  
     |  NonClientAreaMouseMove = 173
     |  
     |  None = 0
     |  
     |  OkRequest = 94
     |  
     |  OrientationChange = 208
     |  
     |  Paint = 12
     |  
     |  PaletteChange = 39
     |  
     |  ParentAboutToChange = 131
     |  
     |  ParentChange = 21
     |  
     |  PlatformPanel = 212
     |  
     |  PlatformSurface = 217
     |  
     |  Polish = 75
     |  
     |  PolishRequest = 74
     |  
     |  QueryWhatsThis = 123
     |  
     |  Quit = 20
     |  
     |  ReadOnlyChange = 106
     |  
     |  RequestSoftwareInputPanel = 199
     |  
     |  Resize = 14
     |  
     |  ScreenChangeInternal = 216
     |  
     |  Scroll = 205
     |  
     |  ScrollPrepare = 204
     |  
     |  Shortcut = 117
     |  
     |  ShortcutOverride = 51
     |  
     |  Show = 17
     |  
     |  ShowToParent = 26
     |  
     |  ShowWindowRequest = 73
     |  
     |  SockAct = 50
     |  
     |  SockClose = 211
     |  
     |  Speech = 42
     |  
     |  StateMachineSignal = 192
     |  
     |  StateMachineWrapped = 193
     |  
     |  StatusTip = 112
     |  
     |  Style = 91
     |  
     |  StyleAnimationUpdate = 213
     |  
     |  StyleChange = 100
     |  
     |  TabletEnterProximity = 171
     |  
     |  TabletLeaveProximity = 172
     |  
     |  TabletMove = 87
     |  
     |  TabletPress = 92
     |  
     |  TabletRelease = 93
     |  
     |  ThemeChange = 210
     |  
     |  ThreadChange = 22
     |  
     |  Timer = 1
     |  
     |  ToolBarChange = 120
     |  
     |  ToolTip = 110
     |  
     |  ToolTipChange = 184
     |  
     |  TouchBegin = 194
     |  
     |  TouchCancel = 209
     |  
     |  TouchEnd = 196
     |  
     |  TouchUpdate = 195
     |  
     |  Type = <class 'PythonQt.QtCore.Type'>
     |  
     |  
     |  UngrabKeyboard = 189
     |  
     |  UngrabMouse = 187
     |  
     |  UpdateLater = 78
     |  
     |  UpdateRequest = 77
     |  
     |  User = 1000
     |  
     |  WhatsThis = 111
     |  
     |  WhatsThisClicked = 118
     |  
     |  Wheel = 31
     |  
     |  WinEventAct = 132
     |  
     |  WinIdChange = 203
     |  
     |  WindowActivate = 24
     |  
     |  WindowBlocked = 103
     |  
     |  WindowChangeInternal = 215
     |  
     |  WindowDeactivate = 25
     |  
     |  WindowIconChange = 34
     |  
     |  WindowStateChange = 105
     |  
     |  WindowTitleChange = 33
     |  
     |  WindowUnblocked = 104
     |  
     |  ZOrderChange = 126
     |  
     |  ZeroTimerEvent = 154
     |  
     |  accept = <unbound qt slot accept of QEvent type>
     |      X.accept(a)
     |  
     |  className = <built-in method className of PythonQt.PythonQtClassWrappe...
     |      Return the classname of the object
     |  
     |  delete = <built-in method delete of PythonQt.PythonQtClassWrapper obje...
     |      Deletes the given C++ object
     |  
     |  help = <built-in method help of PythonQt.PythonQtClassWrapper object>
     |      Shows the help of available methods for this class
     |  
     |  ignore = <unbound qt slot ignore of QEvent type>
     |      X.ignore(a)
     |  
     |  inherits = <built-in method inherits of PythonQt.PythonQtClassWrapper ...
     |      Returns if the class inherits or is of given type name
     |  
     |  isAccepted = <unbound qt slot isAccepted of QEvent type>
     |      X.isAccepted(a) -> bool
     |  
     |  operator_assign = <unbound qt slot operator_assign of QEvent type>
     |      X.operator_assign(a, b) -> PythonQt.QtCore.QEvent
     |  
     |  registerEventType = <unbound qt slot static_QEvent_registerEventType o...
     |      X.registerEventType(a) -> int
     |  
     |  setAccepted = <unbound qt slot setAccepted of QEvent type>
     |      X.setAccepted(a, b)
     |  
     |  spontaneous = <unbound qt slot spontaneous of QEvent type>
     |      X.spontaneous(a) -> bool
     |  
     |  type = <unbound qt slot type of QEvent type>
     |      X.type(a)
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __delattr__(...)
     |      x.__delattr__('name') <==> del x.name
     |  
     |  __eq__(...)
     |      x.__eq__(y) <==> x==y
     |  
     |  __ge__(...)
     |      x.__ge__(y) <==> x>=y
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __gt__(...)
     |      x.__gt__(y) <==> x>y
     |  
     |  __hash__(...)
     |      x.__hash__() <==> hash(x)
     |  
     |  __le__(...)
     |      x.__le__(y) <==> x<=y
     |  
     |  __lt__(...)
     |      x.__lt__(y) <==> x<y
     |  
     |  __ne__(...)
     |      x.__ne__(y) <==> x!=y
     |  
     |  __nonzero__(...)
     |      x.__nonzero__() <==> x != 0
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __setattr__(...)
     |      x.__setattr__('name', value) <==> x.name = value
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __new__ = <built-in method __new__ of PythonQt.PythonQtClassWrapper ob...
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
    
    class QEventLoop(PythonQt.PythonQtInstanceWrapper)
     |  Method resolution order:
     |      QEventLoop
     |      PythonQt.PythonQtInstanceWrapper
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  __init__(...)
     |      x.__init__(...) initializes x; see help(type(x)) for signature
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  AllEvents = 0
     |  
     |  DialogExec = 64
     |  
     |  EventLoopExec = 32
     |  
     |  ExcludeSocketNotifiers = 2
     |  
     |  ExcludeUserInputEvents = 1
     |  
     |  ProcessEventsFlag = <class 'PythonQt.QtCore.ProcessEventsFlag'>
     |  
     |  
     |  ProcessEventsFlags = <class 'PythonQt.QtCore.ProcessEventsFlags'>
     |  
     |  
     |  WaitForMoreEvents = 4
     |  
     |  X11ExcludeTimers = 8
     |  
     |  blockSignals = <unbound qt slot blockSignals of QEventLoop type>
     |      X.blockSignals(a, b) -> bool
     |  
     |  childEvent = <unbound qt slot py_q_childEvent of QEventLoop type>
     |      X.childEvent(a, b)
     |  
     |  children = <unbound qt slot children of QEventLoop type>
     |      X.children(a) -> tuple
     |  
     |  className = <built-in method className of PythonQt.PythonQtClassWrappe...
     |      Return the classname of the object
     |  
     |  connect = <unbound qt slot connect of QEventLoop type>
     |      X.connect(a, b, c, d, e) -> bool
     |  
     |  customEvent = <unbound qt slot py_q_customEvent of QEventLoop type>
     |      X.customEvent(a, b)
     |  
     |  delete = <built-in method delete of PythonQt.PythonQtClassWrapper obje...
     |      Deletes the given C++ object
     |  
     |  deleteLater = <unbound qt slot deleteLater of QEventLoop type>
     |      X.deleteLater()
     |  
     |  destroyed = <unbound qt signal destroyed of QEventLoop type>
     |  
     |  
     |  disconnect = <unbound qt slot disconnect of QEventLoop type>
     |      X.disconnect(a, b, c, d) -> bool
     |  
     |  dumpObjectInfo = <unbound qt slot dumpObjectInfo of QEventLoop type>
     |      X.dumpObjectInfo(a)
     |  
     |  dumpObjectTree = <unbound qt slot dumpObjectTree of QEventLoop type>
     |      X.dumpObjectTree(a)
     |  
     |  dynamicPropertyNames = <unbound qt slot dynamicPropertyNames of QEvent...
     |      X.dynamicPropertyNames(a)
     |  
     |  event = <unbound qt slot py_q_event of QEventLoop type>
     |      X.event(a, b) -> bool
     |  
     |  eventFilter = <unbound qt slot py_q_eventFilter of QEventLoop type>
     |      X.eventFilter(a, b, c) -> bool
     |  
     |  exec = <unbound qt slot exec of QEventLoop type>
     |      X.exec(a, b) -> int
     |  
     |  exit = <unbound qt slot exit of QEventLoop type>
     |      X.exit(a, b)
     |  
     |  findChild = <unbound qt slot findChild of QEventLoop type>
     |      X.findChild(a, b, c) -> PythonQt.private.QObject
     |  
     |  findChildren = <unbound qt slot findChildren of QEventLoop type>
     |      X.findChildren(a, b, c) -> tuple
     |  
     |  help = <built-in method help of PythonQt.PythonQtClassWrapper object>
     |      Shows the help of available methods for this class
     |  
     |  inherits = <built-in method inherits of PythonQt.PythonQtClassWrapper ...
     |      Returns if the class inherits or is of given type name
     |  
     |  installEventFilter = <unbound qt slot installEventFilter of QEventLoop...
     |      X.installEventFilter(a, b)
     |  
     |  isRunning = <unbound qt slot isRunning of QEventLoop type>
     |      X.isRunning(a) -> bool
     |  
     |  isSignalConnected = <unbound qt slot isSignalConnected of QEventLoop t...
     |      X.isSignalConnected(a, b) -> bool
     |  
     |  isWidgetType = <unbound qt slot isWidgetType of QEventLoop type>
     |      X.isWidgetType(a) -> bool
     |  
     |  isWindowType = <unbound qt slot isWindowType of QEventLoop type>
     |      X.isWindowType(a) -> bool
     |  
     |  killTimer = <unbound qt slot killTimer of QEventLoop type>
     |      X.killTimer(a, b)
     |  
     |  metaObject = <unbound qt slot metaObject of QEventLoop type>
     |      X.metaObject(a) -> PythonQt.QtCore.QMetaObject
     |  
     |  moveToThread = <unbound qt slot moveToThread of QEventLoop type>
     |      X.moveToThread(a, b)
     |  
     |  objectName = None
     |  
     |  objectNameChanged = <unbound qt signal objectNameChanged of QEventLoop...
     |  
     |  
     |  parent = <unbound qt slot parent of QEventLoop type>
     |      X.parent(a) -> PythonQt.private.QObject
     |  
     |  processEvents = <unbound qt slot processEvents of QEventLoop type>
     |      X.processEvents(a, b, c) -> bool
     |  
     |  property = <unbound qt slot property of QEventLoop type>
     |      X.property(a, b) -> object
     |  
     |  quit = <unbound qt slot quit of QEventLoop type>
     |      X.quit()
     |  
     |  removeEventFilter = <unbound qt slot removeEventFilter of QEventLoop t...
     |      X.removeEventFilter(a, b)
     |  
     |  sender = <unbound qt slot sender of QEventLoop type>
     |      X.sender(a) -> PythonQt.private.QObject
     |  
     |  senderSignalIndex = <unbound qt slot senderSignalIndex of QEventLoop t...
     |      X.senderSignalIndex(a) -> int
     |  
     |  setObjectName = <unbound qt slot setObjectName of QEventLoop type>
     |      X.setObjectName(a, b)
     |  
     |  setParent = <unbound qt slot setParent of QEventLoop type>
     |      X.setParent(a, b)
     |  
     |  setProperty = <unbound qt slot setProperty of QEventLoop type>
     |      X.setProperty(a, b, c) -> bool
     |  
     |  signalsBlocked = <unbound qt slot signalsBlocked of QEventLoop type>
     |      X.signalsBlocked(a) -> bool
     |  
     |  startTimer = <unbound qt slot startTimer of QEventLoop type>
     |      X.startTimer(a, b, c) -> int
     |  
     |  thread = <unbound qt slot thread of QEventLoop type>
     |      X.thread(a)
     |  
     |  timerEvent = <unbound qt slot py_q_timerEvent of QEventLoop type>
     |      X.timerEvent(a, b)
     |  
     |  tr = <unbound qt slot tr of QEventLoop type>
     |      X.tr(a, b, c, d) -> str
     |  
     |  wakeUp = <unbound qt slot wakeUp of QEventLoop type>
     |      X.wakeUp(a)
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __delattr__(...)
     |      x.__delattr__('name') <==> del x.name
     |  
     |  __eq__(...)
     |      x.__eq__(y) <==> x==y
     |  
     |  __ge__(...)
     |      x.__ge__(y) <==> x>=y
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __gt__(...)
     |      x.__gt__(y) <==> x>y
     |  
     |  __hash__(...)
     |      x.__hash__() <==> hash(x)
     |  
     |  __le__(...)
     |      x.__le__(y) <==> x<=y
     |  
     |  __lt__(...)
     |      x.__lt__(y) <==> x<y
     |  
     |  __ne__(...)
     |      x.__ne__(y) <==> x!=y
     |  
     |  __nonzero__(...)
     |      x.__nonzero__() <==> x != 0
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __setattr__(...)
     |      x.__setattr__('name', value) <==> x.name = value
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __new__ = <built-in method __new__ of PythonQt.PythonQtClassWrapper ob...
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
    
    class QEventTransition(PythonQt.PythonQtInstanceWrapper)
     |  Method resolution order:
     |      QEventTransition
     |      PythonQt.PythonQtInstanceWrapper
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  __init__(...)
     |      x.__init__(...) initializes x; see help(type(x)) for signature
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  ExternalTransition = 0
     |  
     |  InternalTransition = 1
     |  
     |  TransitionType = <class 'PythonQt.QtCore.TransitionType'>
     |  
     |  
     |  addAnimation = <unbound qt slot addAnimation of QEventTransition type>
     |      X.addAnimation(a, b)
     |  
     |  animations = <unbound qt slot animations of QEventTransition type>
     |      X.animations(a) -> tuple
     |  
     |  blockSignals = <unbound qt slot blockSignals of QEventTransition type>
     |      X.blockSignals(a, b) -> bool
     |  
     |  childEvent = <unbound qt slot py_q_childEvent of QEventTransition type...
     |      X.childEvent(a, b)
     |  
     |  children = <unbound qt slot children of QEventTransition type>
     |      X.children(a) -> tuple
     |  
     |  className = <built-in method className of PythonQt.PythonQtClassWrappe...
     |      Return the classname of the object
     |  
     |  connect = <unbound qt slot connect of QEventTransition type>
     |      X.connect(a, b, c, d, e) -> bool
     |  
     |  customEvent = <unbound qt slot py_q_customEvent of QEventTransition ty...
     |      X.customEvent(a, b)
     |  
     |  delete = <built-in method delete of PythonQt.PythonQtClassWrapper obje...
     |      Deletes the given C++ object
     |  
     |  deleteLater = <unbound qt slot deleteLater of QEventTransition type>
     |      X.deleteLater()
     |  
     |  destroyed = <unbound qt signal destroyed of QEventTransition type>
     |  
     |  
     |  disconnect = <unbound qt slot disconnect of QEventTransition type>
     |      X.disconnect(a, b, c, d) -> bool
     |  
     |  dumpObjectInfo = <unbound qt slot dumpObjectInfo of QEventTransition t...
     |      X.dumpObjectInfo(a)
     |  
     |  dumpObjectTree = <unbound qt slot dumpObjectTree of QEventTransition t...
     |      X.dumpObjectTree(a)
     |  
     |  dynamicPropertyNames = <unbound qt slot dynamicPropertyNames of QEvent...
     |      X.dynamicPropertyNames(a)
     |  
     |  event = <unbound qt slot py_q_event of QEventTransition type>
     |      X.event(a, b) -> bool
     |  
     |  eventFilter = <unbound qt slot py_q_eventFilter of QEventTransition ty...
     |      X.eventFilter(a, b, c) -> bool
     |  
     |  eventSource = QObject (QObject at: 0x0)
     |  
     |  eventTest = <unbound qt slot py_q_eventTest of QEventTransition type>
     |      X.eventTest(a, b) -> bool
     |  
     |  eventType = None
     |  
     |  findChild = <unbound qt slot findChild of QEventTransition type>
     |      X.findChild(a, b, c) -> PythonQt.private.QObject
     |  
     |  findChildren = <unbound qt slot findChildren of QEventTransition type>
     |      X.findChildren(a, b, c) -> tuple
     |  
     |  help = <built-in method help of PythonQt.PythonQtClassWrapper object>
     |      Shows the help of available methods for this class
     |  
     |  inherits = <built-in method inherits of PythonQt.PythonQtClassWrapper ...
     |      Returns if the class inherits or is of given type name
     |  
     |  installEventFilter = <unbound qt slot installEventFilter of QEventTran...
     |      X.installEventFilter(a, b)
     |  
     |  isSignalConnected = <unbound qt slot isSignalConnected of QEventTransi...
     |      X.isSignalConnected(a, b) -> bool
     |  
     |  isWidgetType = <unbound qt slot isWidgetType of QEventTransition type>
     |      X.isWidgetType(a) -> bool
     |  
     |  isWindowType = <unbound qt slot isWindowType of QEventTransition type>
     |      X.isWindowType(a) -> bool
     |  
     |  killTimer = <unbound qt slot killTimer of QEventTransition type>
     |      X.killTimer(a, b)
     |  
     |  machine = <unbound qt slot machine of QEventTransition type>
     |      X.machine(a) -> PythonQt.QtCore.QStateMachine
     |  
     |  metaObject = <unbound qt slot metaObject of QEventTransition type>
     |      X.metaObject(a) -> PythonQt.QtCore.QMetaObject
     |  
     |  moveToThread = <unbound qt slot moveToThread of QEventTransition type>
     |      X.moveToThread(a, b)
     |  
     |  objectName = None
     |  
     |  objectNameChanged = <unbound qt signal objectNameChanged of QEventTran...
     |  
     |  
     |  onTransition = <unbound qt slot py_q_onTransition of QEventTransition ...
     |      X.onTransition(a, b)
     |  
     |  parent = <unbound qt slot parent of QEventTransition type>
     |      X.parent(a) -> PythonQt.private.QObject
     |  
     |  property = <unbound qt slot property of QEventTransition type>
     |      X.property(a, b) -> object
     |  
     |  removeAnimation = <unbound qt slot removeAnimation of QEventTransition...
     |      X.removeAnimation(a, b)
     |  
     |  removeEventFilter = <unbound qt slot removeEventFilter of QEventTransi...
     |      X.removeEventFilter(a, b)
     |  
     |  sender = <unbound qt slot sender of QEventTransition type>
     |      X.sender(a) -> PythonQt.private.QObject
     |  
     |  senderSignalIndex = <unbound qt slot senderSignalIndex of QEventTransi...
     |      X.senderSignalIndex(a) -> int
     |  
     |  setEventSource = <unbound qt slot setEventSource of QEventTransition t...
     |      X.setEventSource(a, b)
     |  
     |  setEventType = <unbound qt slot setEventType of QEventTransition type>
     |      X.setEventType(a, b)
     |  
     |  setObjectName = <unbound qt slot setObjectName of QEventTransition typ...
     |      X.setObjectName(a, b)
     |  
     |  setParent = <unbound qt slot setParent of QEventTransition type>
     |      X.setParent(a, b)
     |  
     |  setProperty = <unbound qt slot setProperty of QEventTransition type>
     |      X.setProperty(a, b, c) -> bool
     |  
     |  setTargetState = <unbound qt slot setTargetState of QEventTransition t...
     |      X.setTargetState(a, b)
     |  
     |  setTargetStates = <unbound qt slot setTargetStates of QEventTransition...
     |      X.setTargetStates(a, b)
     |  
     |  setTransitionType = <unbound qt slot setTransitionType of QEventTransi...
     |      X.setTransitionType(a, b)
     |  
     |  signalsBlocked = <unbound qt slot signalsBlocked of QEventTransition t...
     |      X.signalsBlocked(a) -> bool
     |  
     |  sourceState = QState (QState at: 0x0)
     |  
     |  startTimer = <unbound qt slot startTimer of QEventTransition type>
     |      X.startTimer(a, b, c) -> int
     |  
     |  targetState = QAbstractState (QAbstractState at: 0x0)
     |  
     |  targetStateChanged = <unbound qt signal targetStateChanged of QEventTr...
     |  
     |  
     |  targetStates = None
     |  
     |  targetStatesChanged = <unbound qt signal targetStatesChanged of QEvent...
     |  
     |  
     |  thread = <unbound qt slot thread of QEventTransition type>
     |      X.thread(a)
     |  
     |  timerEvent = <unbound qt slot py_q_timerEvent of QEventTransition type...
     |      X.timerEvent(a, b)
     |  
     |  tr = <unbound qt slot tr of QEventTransition type>
     |      X.tr(a, b, c, d) -> str
     |  
     |  transitionType = None
     |  
     |  triggered = <unbound qt signal triggered of QEventTransition type>
     |  
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __delattr__(...)
     |      x.__delattr__('name') <==> del x.name
     |  
     |  __eq__(...)
     |      x.__eq__(y) <==> x==y
     |  
     |  __ge__(...)
     |      x.__ge__(y) <==> x>=y
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __gt__(...)
     |      x.__gt__(y) <==> x>y
     |  
     |  __hash__(...)
     |      x.__hash__() <==> hash(x)
     |  
     |  __le__(...)
     |      x.__le__(y) <==> x<=y
     |  
     |  __lt__(...)
     |      x.__lt__(y) <==> x<y
     |  
     |  __ne__(...)
     |      x.__ne__(y) <==> x!=y
     |  
     |  __nonzero__(...)
     |      x.__nonzero__() <==> x != 0
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __setattr__(...)
     |      x.__setattr__('name', value) <==> x.name = value
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __new__ = <built-in method __new__ of PythonQt.PythonQtClassWrapper ob...
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
    
    class QFactoryInterface(PythonQt.PythonQtInstanceWrapper)
     |  Method resolution order:
     |      QFactoryInterface
     |      PythonQt.PythonQtInstanceWrapper
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  __init__(...)
     |      x.__init__(...) initializes x; see help(type(x)) for signature
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  className = <built-in method className of PythonQt.PythonQtClassWrappe...
     |      Return the classname of the object
     |  
     |  delete = <built-in method delete of PythonQt.PythonQtClassWrapper obje...
     |      Deletes the given C++ object
     |  
     |  help = <built-in method help of PythonQt.PythonQtClassWrapper object>
     |      Shows the help of available methods for this class
     |  
     |  inherits = <built-in method inherits of PythonQt.PythonQtClassWrapper ...
     |      Returns if the class inherits or is of given type name
     |  
     |  keys = <unbound qt slot py_q_keys of QFactoryInterface type>
     |      X.keys(a) -> tuple
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __delattr__(...)
     |      x.__delattr__('name') <==> del x.name
     |  
     |  __eq__(...)
     |      x.__eq__(y) <==> x==y
     |  
     |  __ge__(...)
     |      x.__ge__(y) <==> x>=y
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __gt__(...)
     |      x.__gt__(y) <==> x>y
     |  
     |  __hash__(...)
     |      x.__hash__() <==> hash(x)
     |  
     |  __le__(...)
     |      x.__le__(y) <==> x<=y
     |  
     |  __lt__(...)
     |      x.__lt__(y) <==> x<y
     |  
     |  __ne__(...)
     |      x.__ne__(y) <==> x!=y
     |  
     |  __nonzero__(...)
     |      x.__nonzero__() <==> x != 0
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __setattr__(...)
     |      x.__setattr__('name', value) <==> x.name = value
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __new__ = <built-in method __new__ of PythonQt.PythonQtClassWrapper ob...
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
    
    class QFile(PythonQt.PythonQtInstanceWrapper)
     |  Method resolution order:
     |      QFile
     |      PythonQt.PythonQtInstanceWrapper
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  __init__(...)
     |      x.__init__(...) initializes x; see help(type(x)) for signature
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  AbortError = 6
     |  
     |  Append = 4
     |  
     |  AutoCloseHandle = 1
     |  
     |  CopyError = 14
     |  
     |  DontCloseHandle = 0
     |  
     |  ExeGroup = 16
     |  
     |  ExeOther = 1
     |  
     |  ExeOwner = 4096
     |  
     |  ExeUser = 256
     |  
     |  FatalError = 3
     |  
     |  FileError = <class 'PythonQt.QtCore.FileError'>
     |  
     |  
     |  FileHandleFlag = <class 'PythonQt.QtCore.FileHandleFlag'>
     |  
     |  
     |  FileHandleFlags = <class 'PythonQt.QtCore.FileHandleFlags'>
     |  
     |  
     |  MapPrivateOption = 1
     |  
     |  MemoryMapFlags = <class 'PythonQt.QtCore.MemoryMapFlags'>
     |  
     |  
     |  NoError = 0
     |  
     |  NoOptions = 0
     |  
     |  NotOpen = 0
     |  
     |  OpenError = 5
     |  
     |  OpenMode = <class 'PythonQt.QtCore.OpenMode'>
     |  
     |  
     |  OpenModeFlag = <class 'PythonQt.QtCore.OpenModeFlag'>
     |  
     |  
     |  Permission = <class 'PythonQt.QtCore.Permission'>
     |  
     |  
     |  Permissions = <class 'PythonQt.QtCore.Permissions'>
     |  
     |  
     |  PermissionsError = 13
     |  
     |  PositionError = 11
     |  
     |  ReadError = 1
     |  
     |  ReadGroup = 64
     |  
     |  ReadOnly = 1
     |  
     |  ReadOther = 4
     |  
     |  ReadOwner = 16384
     |  
     |  ReadUser = 1024
     |  
     |  ReadWrite = 3
     |  
     |  RemoveError = 9
     |  
     |  RenameError = 10
     |  
     |  ResizeError = 12
     |  
     |  ResourceError = 4
     |  
     |  Text = 16
     |  
     |  TimeOutError = 7
     |  
     |  Truncate = 8
     |  
     |  Unbuffered = 32
     |  
     |  UnspecifiedError = 8
     |  
     |  WriteError = 2
     |  
     |  WriteGroup = 32
     |  
     |  WriteOnly = 2
     |  
     |  WriteOther = 2
     |  
     |  WriteOwner = 8192
     |  
     |  WriteUser = 512
     |  
     |  aboutToClose = <unbound qt signal aboutToClose of QFile type>
     |  
     |  
     |  atEnd = <unbound qt slot py_q_atEnd of QFile type>
     |      X.atEnd(a) -> bool
     |  
     |  blockSignals = <unbound qt slot blockSignals of QFile type>
     |      X.blockSignals(a, b) -> bool
     |  
     |  bytesAvailable = <unbound qt slot py_q_bytesAvailable of QFile type>
     |      X.bytesAvailable(a) -> int
     |  
     |  bytesToWrite = <unbound qt slot py_q_bytesToWrite of QFile type>
     |      X.bytesToWrite(a) -> int
     |  
     |  bytesWritten = <unbound qt signal bytesWritten of QFile type>
     |  
     |  
     |  canReadLine = <unbound qt slot py_q_canReadLine of QFile type>
     |      X.canReadLine(a) -> bool
     |  
     |  channelBytesWritten = <unbound qt signal channelBytesWritten of QFile ...
     |  
     |  
     |  channelReadyRead = <unbound qt signal channelReadyRead of QFile type>
     |  
     |  
     |  childEvent = <unbound qt slot py_q_childEvent of QFile type>
     |      X.childEvent(a, b)
     |  
     |  children = <unbound qt slot children of QFile type>
     |      X.children(a) -> tuple
     |  
     |  className = <built-in method className of PythonQt.PythonQtClassWrappe...
     |      Return the classname of the object
     |  
     |  close = <unbound qt slot py_q_close of QFile type>
     |      X.close(a)
     |  
     |  connect = <unbound qt slot connect of QFile type>
     |      X.connect(a, b, c, d, e) -> bool
     |  
     |  copy = <unbound qt slot static_QFile_copy of QFile type>
     |      X.copy(a, b) -> bool
     |  
     |  customEvent = <unbound qt slot py_q_customEvent of QFile type>
     |      X.customEvent(a, b)
     |  
     |  decodeName = <unbound qt slot static_QFile_decodeName of QFile type>
     |      X.decodeName(a) -> str
     |  
     |  delete = <built-in method delete of PythonQt.PythonQtClassWrapper obje...
     |      Deletes the given C++ object
     |  
     |  deleteLater = <unbound qt slot deleteLater of QFile type>
     |      X.deleteLater()
     |  
     |  destroyed = <unbound qt signal destroyed of QFile type>
     |  
     |  
     |  disconnect = <unbound qt slot disconnect of QFile type>
     |      X.disconnect(a, b, c, d) -> bool
     |  
     |  dumpObjectInfo = <unbound qt slot dumpObjectInfo of QFile type>
     |      X.dumpObjectInfo(a)
     |  
     |  dumpObjectTree = <unbound qt slot dumpObjectTree of QFile type>
     |      X.dumpObjectTree(a)
     |  
     |  dynamicPropertyNames = <unbound qt slot dynamicPropertyNames of QFile ...
     |      X.dynamicPropertyNames(a)
     |  
     |  encodeName = <unbound qt slot static_QFile_encodeName of QFile type>
     |      X.encodeName(a) -> PythonQt.QtCore.QByteArray
     |  
     |  error = <unbound qt slot error of QFile type>
     |      X.error(a)
     |  
     |  errorString = <unbound qt slot errorString of QFile type>
     |      X.errorString(a) -> str
     |  
     |  event = <unbound qt slot py_q_event of QFile type>
     |      X.event(a, b) -> bool
     |  
     |  eventFilter = <unbound qt slot py_q_eventFilter of QFile type>
     |      X.eventFilter(a, b, c) -> bool
     |  
     |  exists = <unbound qt slot exists of QFile type>
     |      X.exists(a) -> bool
     |  
     |  fileName = <unbound qt slot py_q_fileName of QFile type>
     |      X.fileName(a) -> str
     |  
     |  findChild = <unbound qt slot findChild of QFile type>
     |      X.findChild(a, b, c) -> PythonQt.private.QObject
     |  
     |  findChildren = <unbound qt slot findChildren of QFile type>
     |      X.findChildren(a, b, c) -> tuple
     |  
     |  flush = <unbound qt slot flush of QFile type>
     |      X.flush(a) -> bool
     |  
     |  getChar = <unbound qt slot getChar of QFile type>
     |      X.getChar(a, b) -> bool
     |  
     |  handle = <unbound qt slot handle of QFile type>
     |      X.handle(a) -> int
     |  
     |  help = <built-in method help of PythonQt.PythonQtClassWrapper object>
     |      Shows the help of available methods for this class
     |  
     |  inherits = <built-in method inherits of PythonQt.PythonQtClassWrapper ...
     |      Returns if the class inherits or is of given type name
     |  
     |  installEventFilter = <unbound qt slot installEventFilter of QFile type...
     |      X.installEventFilter(a, b)
     |  
     |  isOpen = <unbound qt slot isOpen of QFile type>
     |      X.isOpen(a) -> bool
     |  
     |  isReadable = <unbound qt slot isReadable of QFile type>
     |      X.isReadable(a) -> bool
     |  
     |  isSequential = <unbound qt slot py_q_isSequential of QFile type>
     |      X.isSequential(a) -> bool
     |  
     |  isSignalConnected = <unbound qt slot isSignalConnected of QFile type>
     |      X.isSignalConnected(a, b) -> bool
     |  
     |  isTextModeEnabled = <unbound qt slot isTextModeEnabled of QFile type>
     |      X.isTextModeEnabled(a) -> bool
     |  
     |  isWidgetType = <unbound qt slot isWidgetType of QFile type>
     |      X.isWidgetType(a) -> bool
     |  
     |  isWindowType = <unbound qt slot isWindowType of QFile type>
     |      X.isWindowType(a) -> bool
     |  
     |  isWritable = <unbound qt slot isWritable of QFile type>
     |      X.isWritable(a) -> bool
     |  
     |  killTimer = <unbound qt slot killTimer of QFile type>
     |      X.killTimer(a, b)
     |  
     |  link = <unbound qt slot link of QFile type>
     |      X.link(a, b) -> bool
     |  
     |  map = <unbound qt slot map of QFile type>
     |      X.map(a, b, c, d) -> int
     |  
     |  metaObject = <unbound qt slot metaObject of QFile type>
     |      X.metaObject(a) -> PythonQt.QtCore.QMetaObject
     |  
     |  moveToThread = <unbound qt slot moveToThread of QFile type>
     |      X.moveToThread(a, b)
     |  
     |  objectName = None
     |  
     |  objectNameChanged = <unbound qt signal objectNameChanged of QFile type...
     |  
     |  
     |  open = <unbound qt slot py_q_open of QFile type>
     |      X.open(a, b) -> bool
     |  
     |  openMode = <unbound qt slot openMode of QFile type>
     |      X.openMode(a)
     |  
     |  parent = <unbound qt slot parent of QFile type>
     |      X.parent(a) -> PythonQt.private.QObject
     |  
     |  peek = <unbound qt slot peek of QFile type>
     |      X.peek(a, b) -> PythonQt.QtCore.QByteArray
     |  
     |  permissions = <unbound qt slot py_q_permissions of QFile type>
     |      X.permissions(a)
     |  
     |  pos = <unbound qt slot py_q_pos of QFile type>
     |      X.pos(a) -> int
     |  
     |  property = <unbound qt slot property of QFile type>
     |      X.property(a, b) -> object
     |  
     |  putChar = <unbound qt slot putChar of QFile type>
     |      X.putChar(a, b) -> bool
     |  
     |  read = <unbound qt slot read of QFile type>
     |      X.read(a, b) -> PythonQt.QtCore.QByteArray
     |  
     |  readAll = <unbound qt slot readAll of QFile type>
     |      X.readAll(a) -> PythonQt.QtCore.QByteArray
     |  
     |  readChannelFinished = <unbound qt signal readChannelFinished of QFile ...
     |  
     |  
     |  readData = <unbound qt slot py_q_readData of QFile type>
     |      X.readData(a, b, c) -> int
     |  
     |  readLine = <unbound qt slot readLine of QFile type>
     |      X.readLine(a, b) -> PythonQt.QtCore.QByteArray
     |  
     |  readLineData = <unbound qt slot py_q_readLineData of QFile type>
     |      X.readLineData(a, b, c) -> int
     |  
     |  readyRead = <unbound qt signal readyRead of QFile type>
     |  
     |  
     |  remove = <unbound qt slot remove of QFile type>
     |      X.remove(a) -> bool
     |  
     |  removeEventFilter = <unbound qt slot removeEventFilter of QFile type>
     |      X.removeEventFilter(a, b)
     |  
     |  rename = <unbound qt slot rename of QFile type>
     |      X.rename(a, b) -> bool
     |  
     |  reset = <unbound qt slot py_q_reset of QFile type>
     |      X.reset(a) -> bool
     |  
     |  resize = <unbound qt slot py_q_resize of QFile type>
     |      X.resize(a, b) -> bool
     |  
     |  seek = <unbound qt slot py_q_seek of QFile type>
     |      X.seek(a, b) -> bool
     |  
     |  sender = <unbound qt slot sender of QFile type>
     |      X.sender(a) -> PythonQt.private.QObject
     |  
     |  senderSignalIndex = <unbound qt slot senderSignalIndex of QFile type>
     |      X.senderSignalIndex(a) -> int
     |  
     |  setErrorString = <unbound qt slot setErrorString of QFile type>
     |      X.setErrorString(a, b)
     |  
     |  setFileName = <unbound qt slot setFileName of QFile type>
     |      X.setFileName(a, b)
     |  
     |  setObjectName = <unbound qt slot setObjectName of QFile type>
     |      X.setObjectName(a, b)
     |  
     |  setOpenMode = <unbound qt slot setOpenMode of QFile type>
     |      X.setOpenMode(a, b)
     |  
     |  setParent = <unbound qt slot setParent of QFile type>
     |      X.setParent(a, b)
     |  
     |  setPermissions = <unbound qt slot py_q_setPermissions of QFile type>
     |      X.setPermissions(a, b) -> bool
     |  
     |  setProperty = <unbound qt slot setProperty of QFile type>
     |      X.setProperty(a, b, c) -> bool
     |  
     |  setTextModeEnabled = <unbound qt slot setTextModeEnabled of QFile type...
     |      X.setTextModeEnabled(a, b)
     |  
     |  signalsBlocked = <unbound qt slot signalsBlocked of QFile type>
     |      X.signalsBlocked(a) -> bool
     |  
     |  size = <unbound qt slot py_q_size of QFile type>
     |      X.size(a) -> int
     |  
     |  startTimer = <unbound qt slot startTimer of QFile type>
     |      X.startTimer(a, b, c) -> int
     |  
     |  symLinkTarget = <unbound qt slot symLinkTarget of QFile type>
     |      X.symLinkTarget(a) -> str
     |  
     |  thread = <unbound qt slot thread of QFile type>
     |      X.thread(a)
     |  
     |  timerEvent = <unbound qt slot py_q_timerEvent of QFile type>
     |      X.timerEvent(a, b)
     |  
     |  tr = <unbound qt slot tr of QFile type>
     |      X.tr(a, b, c, d) -> str
     |  
     |  ungetChar = <unbound qt slot ungetChar of QFile type>
     |      X.ungetChar(a, b)
     |  
     |  unmap = <unbound qt slot unmap of QFile type>
     |      X.unmap(a, b) -> bool
     |  
     |  unsetError = <unbound qt slot unsetError of QFile type>
     |      X.unsetError(a)
     |  
     |  waitForBytesWritten = <unbound qt slot py_q_waitForBytesWritten of QFi...
     |      X.waitForBytesWritten(a, b) -> bool
     |  
     |  waitForReadyRead = <unbound qt slot py_q_waitForReadyRead of QFile typ...
     |      X.waitForReadyRead(a, b) -> bool
     |  
     |  write = <unbound qt slot write of QFile type>
     |      X.write(a, b) -> int
     |  
     |  writeData = <unbound qt slot py_q_writeData of QFile type>
     |      X.writeData(a, b, c) -> int
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __delattr__(...)
     |      x.__delattr__('name') <==> del x.name
     |  
     |  __eq__(...)
     |      x.__eq__(y) <==> x==y
     |  
     |  __ge__(...)
     |      x.__ge__(y) <==> x>=y
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __gt__(...)
     |      x.__gt__(y) <==> x>y
     |  
     |  __hash__(...)
     |      x.__hash__() <==> hash(x)
     |  
     |  __le__(...)
     |      x.__le__(y) <==> x<=y
     |  
     |  __lt__(...)
     |      x.__lt__(y) <==> x<y
     |  
     |  __ne__(...)
     |      x.__ne__(y) <==> x!=y
     |  
     |  __nonzero__(...)
     |      x.__nonzero__() <==> x != 0
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __setattr__(...)
     |      x.__setattr__('name', value) <==> x.name = value
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __new__ = <built-in method __new__ of PythonQt.PythonQtClassWrapper ob...
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
    
    class QFileDevice(PythonQt.PythonQtInstanceWrapper)
     |  Method resolution order:
     |      QFileDevice
     |      PythonQt.PythonQtInstanceWrapper
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  __init__(...)
     |      x.__init__(...) initializes x; see help(type(x)) for signature
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  AbortError = 6
     |  
     |  Append = 4
     |  
     |  AutoCloseHandle = 1
     |  
     |  CopyError = 14
     |  
     |  DontCloseHandle = 0
     |  
     |  ExeGroup = 16
     |  
     |  ExeOther = 1
     |  
     |  ExeOwner = 4096
     |  
     |  ExeUser = 256
     |  
     |  FatalError = 3
     |  
     |  FileError = <class 'PythonQt.QtCore.FileError'>
     |  
     |  
     |  FileHandleFlag = <class 'PythonQt.QtCore.FileHandleFlag'>
     |  
     |  
     |  FileHandleFlags = <class 'PythonQt.QtCore.FileHandleFlags'>
     |  
     |  
     |  MapPrivateOption = 1
     |  
     |  MemoryMapFlags = <class 'PythonQt.QtCore.MemoryMapFlags'>
     |  
     |  
     |  NoError = 0
     |  
     |  NoOptions = 0
     |  
     |  NotOpen = 0
     |  
     |  OpenError = 5
     |  
     |  OpenMode = <class 'PythonQt.QtCore.OpenMode'>
     |  
     |  
     |  OpenModeFlag = <class 'PythonQt.QtCore.OpenModeFlag'>
     |  
     |  
     |  Permission = <class 'PythonQt.QtCore.Permission'>
     |  
     |  
     |  Permissions = <class 'PythonQt.QtCore.Permissions'>
     |  
     |  
     |  PermissionsError = 13
     |  
     |  PositionError = 11
     |  
     |  ReadError = 1
     |  
     |  ReadGroup = 64
     |  
     |  ReadOnly = 1
     |  
     |  ReadOther = 4
     |  
     |  ReadOwner = 16384
     |  
     |  ReadUser = 1024
     |  
     |  ReadWrite = 3
     |  
     |  RemoveError = 9
     |  
     |  RenameError = 10
     |  
     |  ResizeError = 12
     |  
     |  ResourceError = 4
     |  
     |  Text = 16
     |  
     |  TimeOutError = 7
     |  
     |  Truncate = 8
     |  
     |  Unbuffered = 32
     |  
     |  UnspecifiedError = 8
     |  
     |  WriteError = 2
     |  
     |  WriteGroup = 32
     |  
     |  WriteOnly = 2
     |  
     |  WriteOther = 2
     |  
     |  WriteOwner = 8192
     |  
     |  WriteUser = 512
     |  
     |  aboutToClose = <unbound qt signal aboutToClose of QFileDevice type>
     |  
     |  
     |  atEnd = <unbound qt slot py_q_atEnd of QFileDevice type>
     |      X.atEnd(a) -> bool
     |  
     |  blockSignals = <unbound qt slot blockSignals of QFileDevice type>
     |      X.blockSignals(a, b) -> bool
     |  
     |  bytesAvailable = <unbound qt slot py_q_bytesAvailable of QFileDevice t...
     |      X.bytesAvailable(a) -> int
     |  
     |  bytesToWrite = <unbound qt slot py_q_bytesToWrite of QFileDevice type>
     |      X.bytesToWrite(a) -> int
     |  
     |  bytesWritten = <unbound qt signal bytesWritten of QFileDevice type>
     |  
     |  
     |  canReadLine = <unbound qt slot py_q_canReadLine of QFileDevice type>
     |      X.canReadLine(a) -> bool
     |  
     |  channelBytesWritten = <unbound qt signal channelBytesWritten of QFileD...
     |  
     |  
     |  channelReadyRead = <unbound qt signal channelReadyRead of QFileDevice ...
     |  
     |  
     |  childEvent = <unbound qt slot py_q_childEvent of QFileDevice type>
     |      X.childEvent(a, b)
     |  
     |  children = <unbound qt slot children of QFileDevice type>
     |      X.children(a) -> tuple
     |  
     |  className = <built-in method className of PythonQt.PythonQtClassWrappe...
     |      Return the classname of the object
     |  
     |  close = <unbound qt slot py_q_close of QFileDevice type>
     |      X.close(a)
     |  
     |  connect = <unbound qt slot connect of QFileDevice type>
     |      X.connect(a, b, c, d, e) -> bool
     |  
     |  customEvent = <unbound qt slot py_q_customEvent of QFileDevice type>
     |      X.customEvent(a, b)
     |  
     |  delete = <built-in method delete of PythonQt.PythonQtClassWrapper obje...
     |      Deletes the given C++ object
     |  
     |  deleteLater = <unbound qt slot deleteLater of QFileDevice type>
     |      X.deleteLater()
     |  
     |  destroyed = <unbound qt signal destroyed of QFileDevice type>
     |  
     |  
     |  disconnect = <unbound qt slot disconnect of QFileDevice type>
     |      X.disconnect(a, b, c, d) -> bool
     |  
     |  dumpObjectInfo = <unbound qt slot dumpObjectInfo of QFileDevice type>
     |      X.dumpObjectInfo(a)
     |  
     |  dumpObjectTree = <unbound qt slot dumpObjectTree of QFileDevice type>
     |      X.dumpObjectTree(a)
     |  
     |  dynamicPropertyNames = <unbound qt slot dynamicPropertyNames of QFileD...
     |      X.dynamicPropertyNames(a)
     |  
     |  error = <unbound qt slot error of QFileDevice type>
     |      X.error(a)
     |  
     |  errorString = <unbound qt slot errorString of QFileDevice type>
     |      X.errorString(a) -> str
     |  
     |  event = <unbound qt slot py_q_event of QFileDevice type>
     |      X.event(a, b) -> bool
     |  
     |  eventFilter = <unbound qt slot py_q_eventFilter of QFileDevice type>
     |      X.eventFilter(a, b, c) -> bool
     |  
     |  fileName = <unbound qt slot py_q_fileName of QFileDevice type>
     |      X.fileName(a) -> str
     |  
     |  findChild = <unbound qt slot findChild of QFileDevice type>
     |      X.findChild(a, b, c) -> PythonQt.private.QObject
     |  
     |  findChildren = <unbound qt slot findChildren of QFileDevice type>
     |      X.findChildren(a, b, c) -> tuple
     |  
     |  flush = <unbound qt slot flush of QFileDevice type>
     |      X.flush(a) -> bool
     |  
     |  getChar = <unbound qt slot getChar of QFileDevice type>
     |      X.getChar(a, b) -> bool
     |  
     |  handle = <unbound qt slot handle of QFileDevice type>
     |      X.handle(a) -> int
     |  
     |  help = <built-in method help of PythonQt.PythonQtClassWrapper object>
     |      Shows the help of available methods for this class
     |  
     |  inherits = <built-in method inherits of PythonQt.PythonQtClassWrapper ...
     |      Returns if the class inherits or is of given type name
     |  
     |  installEventFilter = <unbound qt slot installEventFilter of QFileDevic...
     |      X.installEventFilter(a, b)
     |  
     |  isOpen = <unbound qt slot isOpen of QFileDevice type>
     |      X.isOpen(a) -> bool
     |  
     |  isReadable = <unbound qt slot isReadable of QFileDevice type>
     |      X.isReadable(a) -> bool
     |  
     |  isSequential = <unbound qt slot py_q_isSequential of QFileDevice type>
     |      X.isSequential(a) -> bool
     |  
     |  isSignalConnected = <unbound qt slot isSignalConnected of QFileDevice ...
     |      X.isSignalConnected(a, b) -> bool
     |  
     |  isTextModeEnabled = <unbound qt slot isTextModeEnabled of QFileDevice ...
     |      X.isTextModeEnabled(a) -> bool
     |  
     |  isWidgetType = <unbound qt slot isWidgetType of QFileDevice type>
     |      X.isWidgetType(a) -> bool
     |  
     |  isWindowType = <unbound qt slot isWindowType of QFileDevice type>
     |      X.isWindowType(a) -> bool
     |  
     |  isWritable = <unbound qt slot isWritable of QFileDevice type>
     |      X.isWritable(a) -> bool
     |  
     |  killTimer = <unbound qt slot killTimer of QFileDevice type>
     |      X.killTimer(a, b)
     |  
     |  map = <unbound qt slot map of QFileDevice type>
     |      X.map(a, b, c, d) -> int
     |  
     |  metaObject = <unbound qt slot metaObject of QFileDevice type>
     |      X.metaObject(a) -> PythonQt.QtCore.QMetaObject
     |  
     |  moveToThread = <unbound qt slot moveToThread of QFileDevice type>
     |      X.moveToThread(a, b)
     |  
     |  objectName = None
     |  
     |  objectNameChanged = <unbound qt signal objectNameChanged of QFileDevic...
     |  
     |  
     |  open = <unbound qt slot py_q_open of QFileDevice type>
     |      X.open(a, b) -> bool
     |  
     |  openMode = <unbound qt slot openMode of QFileDevice type>
     |      X.openMode(a)
     |  
     |  parent = <unbound qt slot parent of QFileDevice type>
     |      X.parent(a) -> PythonQt.private.QObject
     |  
     |  peek = <unbound qt slot peek of QFileDevice type>
     |      X.peek(a, b) -> PythonQt.QtCore.QByteArray
     |  
     |  permissions = <unbound qt slot py_q_permissions of QFileDevice type>
     |      X.permissions(a)
     |  
     |  pos = <unbound qt slot py_q_pos of QFileDevice type>
     |      X.pos(a) -> int
     |  
     |  property = <unbound qt slot property of QFileDevice type>
     |      X.property(a, b) -> object
     |  
     |  putChar = <unbound qt slot putChar of QFileDevice type>
     |      X.putChar(a, b) -> bool
     |  
     |  read = <unbound qt slot read of QFileDevice type>
     |      X.read(a, b) -> PythonQt.QtCore.QByteArray
     |  
     |  readAll = <unbound qt slot readAll of QFileDevice type>
     |      X.readAll(a) -> PythonQt.QtCore.QByteArray
     |  
     |  readChannelFinished = <unbound qt signal readChannelFinished of QFileD...
     |  
     |  
     |  readData = <unbound qt slot py_q_readData of QFileDevice type>
     |      X.readData(a, b, c) -> int
     |  
     |  readLine = <unbound qt slot readLine of QFileDevice type>
     |      X.readLine(a, b) -> PythonQt.QtCore.QByteArray
     |  
     |  readLineData = <unbound qt slot py_q_readLineData of QFileDevice type>
     |      X.readLineData(a, b, c) -> int
     |  
     |  readyRead = <unbound qt signal readyRead of QFileDevice type>
     |  
     |  
     |  removeEventFilter = <unbound qt slot removeEventFilter of QFileDevice ...
     |      X.removeEventFilter(a, b)
     |  
     |  reset = <unbound qt slot py_q_reset of QFileDevice type>
     |      X.reset(a) -> bool
     |  
     |  resize = <unbound qt slot py_q_resize of QFileDevice type>
     |      X.resize(a, b) -> bool
     |  
     |  seek = <unbound qt slot py_q_seek of QFileDevice type>
     |      X.seek(a, b) -> bool
     |  
     |  sender = <unbound qt slot sender of QFileDevice type>
     |      X.sender(a) -> PythonQt.private.QObject
     |  
     |  senderSignalIndex = <unbound qt slot senderSignalIndex of QFileDevice ...
     |      X.senderSignalIndex(a) -> int
     |  
     |  setErrorString = <unbound qt slot setErrorString of QFileDevice type>
     |      X.setErrorString(a, b)
     |  
     |  setObjectName = <unbound qt slot setObjectName of QFileDevice type>
     |      X.setObjectName(a, b)
     |  
     |  setOpenMode = <unbound qt slot setOpenMode of QFileDevice type>
     |      X.setOpenMode(a, b)
     |  
     |  setParent = <unbound qt slot setParent of QFileDevice type>
     |      X.setParent(a, b)
     |  
     |  setPermissions = <unbound qt slot py_q_setPermissions of QFileDevice t...
     |      X.setPermissions(a, b) -> bool
     |  
     |  setProperty = <unbound qt slot setProperty of QFileDevice type>
     |      X.setProperty(a, b, c) -> bool
     |  
     |  setTextModeEnabled = <unbound qt slot setTextModeEnabled of QFileDevic...
     |      X.setTextModeEnabled(a, b)
     |  
     |  signalsBlocked = <unbound qt slot signalsBlocked of QFileDevice type>
     |      X.signalsBlocked(a) -> bool
     |  
     |  size = <unbound qt slot py_q_size of QFileDevice type>
     |      X.size(a) -> int
     |  
     |  startTimer = <unbound qt slot startTimer of QFileDevice type>
     |      X.startTimer(a, b, c) -> int
     |  
     |  thread = <unbound qt slot thread of QFileDevice type>
     |      X.thread(a)
     |  
     |  timerEvent = <unbound qt slot py_q_timerEvent of QFileDevice type>
     |      X.timerEvent(a, b)
     |  
     |  tr = <unbound qt slot tr of QFileDevice type>
     |      X.tr(a, b, c, d) -> str
     |  
     |  ungetChar = <unbound qt slot ungetChar of QFileDevice type>
     |      X.ungetChar(a, b)
     |  
     |  unmap = <unbound qt slot unmap of QFileDevice type>
     |      X.unmap(a, b) -> bool
     |  
     |  unsetError = <unbound qt slot unsetError of QFileDevice type>
     |      X.unsetError(a)
     |  
     |  waitForBytesWritten = <unbound qt slot py_q_waitForBytesWritten of QFi...
     |      X.waitForBytesWritten(a, b) -> bool
     |  
     |  waitForReadyRead = <unbound qt slot py_q_waitForReadyRead of QFileDevi...
     |      X.waitForReadyRead(a, b) -> bool
     |  
     |  write = <unbound qt slot write of QFileDevice type>
     |      X.write(a, b) -> int
     |  
     |  writeData = <unbound qt slot py_q_writeData of QFileDevice type>
     |      X.writeData(a, b, c) -> int
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __delattr__(...)
     |      x.__delattr__('name') <==> del x.name
     |  
     |  __eq__(...)
     |      x.__eq__(y) <==> x==y
     |  
     |  __ge__(...)
     |      x.__ge__(y) <==> x>=y
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __gt__(...)
     |      x.__gt__(y) <==> x>y
     |  
     |  __hash__(...)
     |      x.__hash__() <==> hash(x)
     |  
     |  __le__(...)
     |      x.__le__(y) <==> x<=y
     |  
     |  __lt__(...)
     |      x.__lt__(y) <==> x<y
     |  
     |  __ne__(...)
     |      x.__ne__(y) <==> x!=y
     |  
     |  __nonzero__(...)
     |      x.__nonzero__() <==> x != 0
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __setattr__(...)
     |      x.__setattr__('name', value) <==> x.name = value
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __new__ = <built-in method __new__ of PythonQt.PythonQtClassWrapper ob...
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
    
    class QFileInfo(PythonQt.PythonQtInstanceWrapper)
     |  Method resolution order:
     |      QFileInfo
     |      PythonQt.PythonQtInstanceWrapper
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  __init__(...)
     |      x.__init__(...) initializes x; see help(type(x)) for signature
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  absoluteDir = <unbound qt slot absoluteDir of QFileInfo type>
     |      X.absoluteDir(a) -> PythonQt.QtCore.QDir
     |  
     |  absoluteFilePath = <unbound qt slot absoluteFilePath of QFileInfo type...
     |      X.absoluteFilePath(a) -> str
     |  
     |  absolutePath = <unbound qt slot absolutePath of QFileInfo type>
     |      X.absolutePath(a) -> str
     |  
     |  baseName = <unbound qt slot baseName of QFileInfo type>
     |      X.baseName(a) -> str
     |  
     |  bundleName = <unbound qt slot bundleName of QFileInfo type>
     |      X.bundleName(a) -> str
     |  
     |  caching = <unbound qt slot caching of QFileInfo type>
     |      X.caching(a) -> bool
     |  
     |  canonicalFilePath = <unbound qt slot canonicalFilePath of QFileInfo ty...
     |      X.canonicalFilePath(a) -> str
     |  
     |  canonicalPath = <unbound qt slot canonicalPath of QFileInfo type>
     |      X.canonicalPath(a) -> str
     |  
     |  className = <built-in method className of PythonQt.PythonQtClassWrappe...
     |      Return the classname of the object
     |  
     |  completeBaseName = <unbound qt slot completeBaseName of QFileInfo type...
     |      X.completeBaseName(a) -> str
     |  
     |  completeSuffix = <unbound qt slot completeSuffix of QFileInfo type>
     |      X.completeSuffix(a) -> str
     |  
     |  created = <unbound qt slot created of QFileInfo type>
     |      X.created(a) -> PythonQt.QtCore.QDateTime
     |  
     |  delete = <built-in method delete of PythonQt.PythonQtClassWrapper obje...
     |      Deletes the given C++ object
     |  
     |  dir = <unbound qt slot dir of QFileInfo type>
     |      X.dir(a) -> PythonQt.QtCore.QDir
     |  
     |  exists = <unbound qt slot exists of QFileInfo type>
     |      X.exists(a) -> bool
     |  
     |  fileName = <unbound qt slot fileName of QFileInfo type>
     |      X.fileName(a) -> str
     |  
     |  filePath = <unbound qt slot filePath of QFileInfo type>
     |      X.filePath(a) -> str
     |  
     |  group = <unbound qt slot group of QFileInfo type>
     |      X.group(a) -> str
     |  
     |  groupId = <unbound qt slot groupId of QFileInfo type>
     |      X.groupId(a) -> int
     |  
     |  help = <built-in method help of PythonQt.PythonQtClassWrapper object>
     |      Shows the help of available methods for this class
     |  
     |  inherits = <built-in method inherits of PythonQt.PythonQtClassWrapper ...
     |      Returns if the class inherits or is of given type name
     |  
     |  isAbsolute = <unbound qt slot isAbsolute of QFileInfo type>
     |      X.isAbsolute(a) -> bool
     |  
     |  isBundle = <unbound qt slot isBundle of QFileInfo type>
     |      X.isBundle(a) -> bool
     |  
     |  isDir = <unbound qt slot isDir of QFileInfo type>
     |      X.isDir(a) -> bool
     |  
     |  isExecutable = <unbound qt slot isExecutable of QFileInfo type>
     |      X.isExecutable(a) -> bool
     |  
     |  isFile = <unbound qt slot isFile of QFileInfo type>
     |      X.isFile(a) -> bool
     |  
     |  isHidden = <unbound qt slot isHidden of QFileInfo type>
     |      X.isHidden(a) -> bool
     |  
     |  isNativePath = <unbound qt slot isNativePath of QFileInfo type>
     |      X.isNativePath(a) -> bool
     |  
     |  isReadable = <unbound qt slot isReadable of QFileInfo type>
     |      X.isReadable(a) -> bool
     |  
     |  isRelative = <unbound qt slot isRelative of QFileInfo type>
     |      X.isRelative(a) -> bool
     |  
     |  isRoot = <unbound qt slot isRoot of QFileInfo type>
     |      X.isRoot(a) -> bool
     |  
     |  isSymLink = <unbound qt slot isSymLink of QFileInfo type>
     |      X.isSymLink(a) -> bool
     |  
     |  isWritable = <unbound qt slot isWritable of QFileInfo type>
     |      X.isWritable(a) -> bool
     |  
     |  lastModified = <unbound qt slot lastModified of QFileInfo type>
     |      X.lastModified(a) -> PythonQt.QtCore.QDateTime
     |  
     |  lastRead = <unbound qt slot lastRead of QFileInfo type>
     |      X.lastRead(a) -> PythonQt.QtCore.QDateTime
     |  
     |  makeAbsolute = <unbound qt slot makeAbsolute of QFileInfo type>
     |      X.makeAbsolute(a) -> bool
     |  
     |  owner = <unbound qt slot owner of QFileInfo type>
     |      X.owner(a) -> str
     |  
     |  ownerId = <unbound qt slot ownerId of QFileInfo type>
     |      X.ownerId(a) -> int
     |  
     |  path = <unbound qt slot path of QFileInfo type>
     |      X.path(a) -> str
     |  
     |  permission = <unbound qt slot permission of QFileInfo type>
     |      X.permission(a, b) -> bool
     |  
     |  permissions = <unbound qt slot permissions of QFileInfo type>
     |      X.permissions(a)
     |  
     |  refresh = <unbound qt slot refresh of QFileInfo type>
     |      X.refresh(a)
     |  
     |  setCaching = <unbound qt slot setCaching of QFileInfo type>
     |      X.setCaching(a, b)
     |  
     |  setFile = <unbound qt slot setFile of QFileInfo type>
     |      X.setFile(a, b, c)
     |  
     |  size = <unbound qt slot size of QFileInfo type>
     |      X.size(a) -> int
     |  
     |  suffix = <unbound qt slot suffix of QFileInfo type>
     |      X.suffix(a) -> str
     |  
     |  swap = <unbound qt slot swap of QFileInfo type>
     |      X.swap(a, b)
     |  
     |  symLinkTarget = <unbound qt slot symLinkTarget of QFileInfo type>
     |      X.symLinkTarget(a) -> str
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __delattr__(...)
     |      x.__delattr__('name') <==> del x.name
     |  
     |  __eq__(...)
     |      x.__eq__(y) <==> x==y
     |  
     |  __ge__(...)
     |      x.__ge__(y) <==> x>=y
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __gt__(...)
     |      x.__gt__(y) <==> x>y
     |  
     |  __hash__(...)
     |      x.__hash__() <==> hash(x)
     |  
     |  __le__(...)
     |      x.__le__(y) <==> x<=y
     |  
     |  __lt__(...)
     |      x.__lt__(y) <==> x<y
     |  
     |  __ne__(...)
     |      x.__ne__(y) <==> x!=y
     |  
     |  __nonzero__(...)
     |      x.__nonzero__() <==> x != 0
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __setattr__(...)
     |      x.__setattr__('name', value) <==> x.name = value
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __new__ = <built-in method __new__ of PythonQt.PythonQtClassWrapper ob...
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
    
    class QFileSelector(PythonQt.PythonQtInstanceWrapper)
     |  Method resolution order:
     |      QFileSelector
     |      PythonQt.PythonQtInstanceWrapper
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  __init__(...)
     |      x.__init__(...) initializes x; see help(type(x)) for signature
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  allSelectors = <unbound qt slot allSelectors of QFileSelector type>
     |      X.allSelectors(a) -> tuple
     |  
     |  blockSignals = <unbound qt slot blockSignals of QFileSelector type>
     |      X.blockSignals(a, b) -> bool
     |  
     |  childEvent = <unbound qt slot py_q_childEvent of QFileSelector type>
     |      X.childEvent(a, b)
     |  
     |  children = <unbound qt slot children of QFileSelector type>
     |      X.children(a) -> tuple
     |  
     |  className = <built-in method className of PythonQt.PythonQtClassWrappe...
     |      Return the classname of the object
     |  
     |  connect = <unbound qt slot connect of QFileSelector type>
     |      X.connect(a, b, c, d, e) -> bool
     |  
     |  customEvent = <unbound qt slot py_q_customEvent of QFileSelector type>
     |      X.customEvent(a, b)
     |  
     |  delete = <built-in method delete of PythonQt.PythonQtClassWrapper obje...
     |      Deletes the given C++ object
     |  
     |  deleteLater = <unbound qt slot deleteLater of QFileSelector type>
     |      X.deleteLater()
     |  
     |  destroyed = <unbound qt signal destroyed of QFileSelector type>
     |  
     |  
     |  disconnect = <unbound qt slot disconnect of QFileSelector type>
     |      X.disconnect(a, b, c, d) -> bool
     |  
     |  dumpObjectInfo = <unbound qt slot dumpObjectInfo of QFileSelector type...
     |      X.dumpObjectInfo(a)
     |  
     |  dumpObjectTree = <unbound qt slot dumpObjectTree of QFileSelector type...
     |      X.dumpObjectTree(a)
     |  
     |  dynamicPropertyNames = <unbound qt slot dynamicPropertyNames of QFileS...
     |      X.dynamicPropertyNames(a)
     |  
     |  event = <unbound qt slot py_q_event of QFileSelector type>
     |      X.event(a, b) -> bool
     |  
     |  eventFilter = <unbound qt slot py_q_eventFilter of QFileSelector type>
     |      X.eventFilter(a, b, c) -> bool
     |  
     |  extraSelectors = <unbound qt slot extraSelectors of QFileSelector type...
     |      X.extraSelectors(a) -> tuple
     |  
     |  findChild = <unbound qt slot findChild of QFileSelector type>
     |      X.findChild(a, b, c) -> PythonQt.private.QObject
     |  
     |  findChildren = <unbound qt slot findChildren of QFileSelector type>
     |      X.findChildren(a, b, c) -> tuple
     |  
     |  help = <built-in method help of PythonQt.PythonQtClassWrapper object>
     |      Shows the help of available methods for this class
     |  
     |  inherits = <built-in method inherits of PythonQt.PythonQtClassWrapper ...
     |      Returns if the class inherits or is of given type name
     |  
     |  installEventFilter = <unbound qt slot installEventFilter of QFileSelec...
     |      X.installEventFilter(a, b)
     |  
     |  isSignalConnected = <unbound qt slot isSignalConnected of QFileSelecto...
     |      X.isSignalConnected(a, b) -> bool
     |  
     |  isWidgetType = <unbound qt slot isWidgetType of QFileSelector type>
     |      X.isWidgetType(a) -> bool
     |  
     |  isWindowType = <unbound qt slot isWindowType of QFileSelector type>
     |      X.isWindowType(a) -> bool
     |  
     |  killTimer = <unbound qt slot killTimer of QFileSelector type>
     |      X.killTimer(a, b)
     |  
     |  metaObject = <unbound qt slot metaObject of QFileSelector type>
     |      X.metaObject(a) -> PythonQt.QtCore.QMetaObject
     |  
     |  moveToThread = <unbound qt slot moveToThread of QFileSelector type>
     |      X.moveToThread(a, b)
     |  
     |  objectName = None
     |  
     |  objectNameChanged = <unbound qt signal objectNameChanged of QFileSelec...
     |  
     |  
     |  parent = <unbound qt slot parent of QFileSelector type>
     |      X.parent(a) -> PythonQt.private.QObject
     |  
     |  property = <unbound qt slot property of QFileSelector type>
     |      X.property(a, b) -> object
     |  
     |  removeEventFilter = <unbound qt slot removeEventFilter of QFileSelecto...
     |      X.removeEventFilter(a, b)
     |  
     |  select = <unbound qt slot select of QFileSelector type>
     |      X.select(a, b) -> str
     |  
     |  sender = <unbound qt slot sender of QFileSelector type>
     |      X.sender(a) -> PythonQt.private.QObject
     |  
     |  senderSignalIndex = <unbound qt slot senderSignalIndex of QFileSelecto...
     |      X.senderSignalIndex(a) -> int
     |  
     |  setExtraSelectors = <unbound qt slot setExtraSelectors of QFileSelecto...
     |      X.setExtraSelectors(a, b)
     |  
     |  setObjectName = <unbound qt slot setObjectName of QFileSelector type>
     |      X.setObjectName(a, b)
     |  
     |  setParent = <unbound qt slot setParent of QFileSelector type>
     |      X.setParent(a, b)
     |  
     |  setProperty = <unbound qt slot setProperty of QFileSelector type>
     |      X.setProperty(a, b, c) -> bool
     |  
     |  signalsBlocked = <unbound qt slot signalsBlocked of QFileSelector type...
     |      X.signalsBlocked(a) -> bool
     |  
     |  startTimer = <unbound qt slot startTimer of QFileSelector type>
     |      X.startTimer(a, b, c) -> int
     |  
     |  thread = <unbound qt slot thread of QFileSelector type>
     |      X.thread(a)
     |  
     |  timerEvent = <unbound qt slot py_q_timerEvent of QFileSelector type>
     |      X.timerEvent(a, b)
     |  
     |  tr = <unbound qt slot tr of QFileSelector type>
     |      X.tr(a, b, c, d) -> str
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __delattr__(...)
     |      x.__delattr__('name') <==> del x.name
     |  
     |  __eq__(...)
     |      x.__eq__(y) <==> x==y
     |  
     |  __ge__(...)
     |      x.__ge__(y) <==> x>=y
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __gt__(...)
     |      x.__gt__(y) <==> x>y
     |  
     |  __hash__(...)
     |      x.__hash__() <==> hash(x)
     |  
     |  __le__(...)
     |      x.__le__(y) <==> x<=y
     |  
     |  __lt__(...)
     |      x.__lt__(y) <==> x<y
     |  
     |  __ne__(...)
     |      x.__ne__(y) <==> x!=y
     |  
     |  __nonzero__(...)
     |      x.__nonzero__() <==> x != 0
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __setattr__(...)
     |      x.__setattr__('name', value) <==> x.name = value
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __new__ = <built-in method __new__ of PythonQt.PythonQtClassWrapper ob...
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
    
    class QFileSystemWatcher(PythonQt.PythonQtInstanceWrapper)
     |  Method resolution order:
     |      QFileSystemWatcher
     |      PythonQt.PythonQtInstanceWrapper
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  __init__(...)
     |      x.__init__(...) initializes x; see help(type(x)) for signature
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  addPath = <unbound qt slot addPath of QFileSystemWatcher type>
     |      X.addPath(a, b) -> bool
     |  
     |  addPaths = <unbound qt slot addPaths of QFileSystemWatcher type>
     |      X.addPaths(a, b) -> tuple
     |  
     |  blockSignals = <unbound qt slot blockSignals of QFileSystemWatcher typ...
     |      X.blockSignals(a, b) -> bool
     |  
     |  childEvent = <unbound qt slot py_q_childEvent of QFileSystemWatcher ty...
     |      X.childEvent(a, b)
     |  
     |  children = <unbound qt slot children of QFileSystemWatcher type>
     |      X.children(a) -> tuple
     |  
     |  className = <built-in method className of PythonQt.PythonQtClassWrappe...
     |      Return the classname of the object
     |  
     |  connect = <unbound qt slot connect of QFileSystemWatcher type>
     |      X.connect(a, b, c, d, e) -> bool
     |  
     |  customEvent = <unbound qt slot py_q_customEvent of QFileSystemWatcher ...
     |      X.customEvent(a, b)
     |  
     |  delete = <built-in method delete of PythonQt.PythonQtClassWrapper obje...
     |      Deletes the given C++ object
     |  
     |  deleteLater = <unbound qt slot deleteLater of QFileSystemWatcher type>
     |      X.deleteLater()
     |  
     |  destroyed = <unbound qt signal destroyed of QFileSystemWatcher type>
     |  
     |  
     |  directories = <unbound qt slot directories of QFileSystemWatcher type>
     |      X.directories(a) -> tuple
     |  
     |  directoryChanged = <unbound qt signal directoryChanged of QFileSystemW...
     |  
     |  
     |  disconnect = <unbound qt slot disconnect of QFileSystemWatcher type>
     |      X.disconnect(a, b, c, d) -> bool
     |  
     |  dumpObjectInfo = <unbound qt slot dumpObjectInfo of QFileSystemWatcher...
     |      X.dumpObjectInfo(a)
     |  
     |  dumpObjectTree = <unbound qt slot dumpObjectTree of QFileSystemWatcher...
     |      X.dumpObjectTree(a)
     |  
     |  dynamicPropertyNames = <unbound qt slot dynamicPropertyNames of QFileS...
     |      X.dynamicPropertyNames(a)
     |  
     |  event = <unbound qt slot py_q_event of QFileSystemWatcher type>
     |      X.event(a, b) -> bool
     |  
     |  eventFilter = <unbound qt slot py_q_eventFilter of QFileSystemWatcher ...
     |      X.eventFilter(a, b, c) -> bool
     |  
     |  fileChanged = <unbound qt signal fileChanged of QFileSystemWatcher typ...
     |  
     |  
     |  files = <unbound qt slot files of QFileSystemWatcher type>
     |      X.files(a) -> tuple
     |  
     |  findChild = <unbound qt slot findChild of QFileSystemWatcher type>
     |      X.findChild(a, b, c) -> PythonQt.private.QObject
     |  
     |  findChildren = <unbound qt slot findChildren of QFileSystemWatcher typ...
     |      X.findChildren(a, b, c) -> tuple
     |  
     |  help = <built-in method help of PythonQt.PythonQtClassWrapper object>
     |      Shows the help of available methods for this class
     |  
     |  inherits = <built-in method inherits of PythonQt.PythonQtClassWrapper ...
     |      Returns if the class inherits or is of given type name
     |  
     |  installEventFilter = <unbound qt slot installEventFilter of QFileSyste...
     |      X.installEventFilter(a, b)
     |  
     |  isSignalConnected = <unbound qt slot isSignalConnected of QFileSystemW...
     |      X.isSignalConnected(a, b) -> bool
     |  
     |  isWidgetType = <unbound qt slot isWidgetType of QFileSystemWatcher typ...
     |      X.isWidgetType(a) -> bool
     |  
     |  isWindowType = <unbound qt slot isWindowType of QFileSystemWatcher typ...
     |      X.isWindowType(a) -> bool
     |  
     |  killTimer = <unbound qt slot killTimer of QFileSystemWatcher type>
     |      X.killTimer(a, b)
     |  
     |  metaObject = <unbound qt slot metaObject of QFileSystemWatcher type>
     |      X.metaObject(a) -> PythonQt.QtCore.QMetaObject
     |  
     |  moveToThread = <unbound qt slot moveToThread of QFileSystemWatcher typ...
     |      X.moveToThread(a, b)
     |  
     |  objectName = None
     |  
     |  objectNameChanged = <unbound qt signal objectNameChanged of QFileSyste...
     |  
     |  
     |  parent = <unbound qt slot parent of QFileSystemWatcher type>
     |      X.parent(a) -> PythonQt.private.QObject
     |  
     |  property = <unbound qt slot property of QFileSystemWatcher type>
     |      X.property(a, b) -> object
     |  
     |  removeEventFilter = <unbound qt slot removeEventFilter of QFileSystemW...
     |      X.removeEventFilter(a, b)
     |  
     |  removePath = <unbound qt slot removePath of QFileSystemWatcher type>
     |      X.removePath(a, b) -> bool
     |  
     |  removePaths = <unbound qt slot removePaths of QFileSystemWatcher type>
     |      X.removePaths(a, b) -> tuple
     |  
     |  sender = <unbound qt slot sender of QFileSystemWatcher type>
     |      X.sender(a) -> PythonQt.private.QObject
     |  
     |  senderSignalIndex = <unbound qt slot senderSignalIndex of QFileSystemW...
     |      X.senderSignalIndex(a) -> int
     |  
     |  setObjectName = <unbound qt slot setObjectName of QFileSystemWatcher t...
     |      X.setObjectName(a, b)
     |  
     |  setParent = <unbound qt slot setParent of QFileSystemWatcher type>
     |      X.setParent(a, b)
     |  
     |  setProperty = <unbound qt slot setProperty of QFileSystemWatcher type>
     |      X.setProperty(a, b, c) -> bool
     |  
     |  signalsBlocked = <unbound qt slot signalsBlocked of QFileSystemWatcher...
     |      X.signalsBlocked(a) -> bool
     |  
     |  startTimer = <unbound qt slot startTimer of QFileSystemWatcher type>
     |      X.startTimer(a, b, c) -> int
     |  
     |  thread = <unbound qt slot thread of QFileSystemWatcher type>
     |      X.thread(a)
     |  
     |  timerEvent = <unbound qt slot py_q_timerEvent of QFileSystemWatcher ty...
     |      X.timerEvent(a, b)
     |  
     |  tr = <unbound qt slot tr of QFileSystemWatcher type>
     |      X.tr(a, b, c, d) -> str
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __delattr__(...)
     |      x.__delattr__('name') <==> del x.name
     |  
     |  __eq__(...)
     |      x.__eq__(y) <==> x==y
     |  
     |  __ge__(...)
     |      x.__ge__(y) <==> x>=y
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __gt__(...)
     |      x.__gt__(y) <==> x>y
     |  
     |  __hash__(...)
     |      x.__hash__() <==> hash(x)
     |  
     |  __le__(...)
     |      x.__le__(y) <==> x<=y
     |  
     |  __lt__(...)
     |      x.__lt__(y) <==> x<y
     |  
     |  __ne__(...)
     |      x.__ne__(y) <==> x!=y
     |  
     |  __nonzero__(...)
     |      x.__nonzero__() <==> x != 0
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __setattr__(...)
     |      x.__setattr__('name', value) <==> x.name = value
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __new__ = <built-in method __new__ of PythonQt.PythonQtClassWrapper ob...
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
    
    class QFinalState(PythonQt.PythonQtInstanceWrapper)
     |  Method resolution order:
     |      QFinalState
     |      PythonQt.PythonQtInstanceWrapper
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  __init__(...)
     |      x.__init__(...) initializes x; see help(type(x)) for signature
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  active = None
     |  
     |  activeChanged = <unbound qt signal activeChanged of QFinalState type>
     |  
     |  
     |  blockSignals = <unbound qt slot blockSignals of QFinalState type>
     |      X.blockSignals(a, b) -> bool
     |  
     |  childEvent = <unbound qt slot py_q_childEvent of QFinalState type>
     |      X.childEvent(a, b)
     |  
     |  children = <unbound qt slot children of QFinalState type>
     |      X.children(a) -> tuple
     |  
     |  className = <built-in method className of PythonQt.PythonQtClassWrappe...
     |      Return the classname of the object
     |  
     |  connect = <unbound qt slot connect of QFinalState type>
     |      X.connect(a, b, c, d, e) -> bool
     |  
     |  customEvent = <unbound qt slot py_q_customEvent of QFinalState type>
     |      X.customEvent(a, b)
     |  
     |  delete = <built-in method delete of PythonQt.PythonQtClassWrapper obje...
     |      Deletes the given C++ object
     |  
     |  deleteLater = <unbound qt slot deleteLater of QFinalState type>
     |      X.deleteLater()
     |  
     |  destroyed = <unbound qt signal destroyed of QFinalState type>
     |  
     |  
     |  disconnect = <unbound qt slot disconnect of QFinalState type>
     |      X.disconnect(a, b, c, d) -> bool
     |  
     |  dumpObjectInfo = <unbound qt slot dumpObjectInfo of QFinalState type>
     |      X.dumpObjectInfo(a)
     |  
     |  dumpObjectTree = <unbound qt slot dumpObjectTree of QFinalState type>
     |      X.dumpObjectTree(a)
     |  
     |  dynamicPropertyNames = <unbound qt slot dynamicPropertyNames of QFinal...
     |      X.dynamicPropertyNames(a)
     |  
     |  entered = <unbound qt signal entered of QFinalState type>
     |  
     |  
     |  event = <unbound qt slot py_q_event of QFinalState type>
     |      X.event(a, b) -> bool
     |  
     |  eventFilter = <unbound qt slot py_q_eventFilter of QFinalState type>
     |      X.eventFilter(a, b, c) -> bool
     |  
     |  exited = <unbound qt signal exited of QFinalState type>
     |  
     |  
     |  findChild = <unbound qt slot findChild of QFinalState type>
     |      X.findChild(a, b, c) -> PythonQt.private.QObject
     |  
     |  findChildren = <unbound qt slot findChildren of QFinalState type>
     |      X.findChildren(a, b, c) -> tuple
     |  
     |  help = <built-in method help of PythonQt.PythonQtClassWrapper object>
     |      Shows the help of available methods for this class
     |  
     |  inherits = <built-in method inherits of PythonQt.PythonQtClassWrapper ...
     |      Returns if the class inherits or is of given type name
     |  
     |  installEventFilter = <unbound qt slot installEventFilter of QFinalStat...
     |      X.installEventFilter(a, b)
     |  
     |  isSignalConnected = <unbound qt slot isSignalConnected of QFinalState ...
     |      X.isSignalConnected(a, b) -> bool
     |  
     |  isWidgetType = <unbound qt slot isWidgetType of QFinalState type>
     |      X.isWidgetType(a) -> bool
     |  
     |  isWindowType = <unbound qt slot isWindowType of QFinalState type>
     |      X.isWindowType(a) -> bool
     |  
     |  killTimer = <unbound qt slot killTimer of QFinalState type>
     |      X.killTimer(a, b)
     |  
     |  machine = <unbound qt slot machine of QFinalState type>
     |      X.machine(a) -> PythonQt.QtCore.QStateMachine
     |  
     |  metaObject = <unbound qt slot metaObject of QFinalState type>
     |      X.metaObject(a) -> PythonQt.QtCore.QMetaObject
     |  
     |  moveToThread = <unbound qt slot moveToThread of QFinalState type>
     |      X.moveToThread(a, b)
     |  
     |  objectName = None
     |  
     |  objectNameChanged = <unbound qt signal objectNameChanged of QFinalStat...
     |  
     |  
     |  onEntry = <unbound qt slot py_q_onEntry of QFinalState type>
     |      X.onEntry(a, b)
     |  
     |  onExit = <unbound qt slot py_q_onExit of QFinalState type>
     |      X.onExit(a, b)
     |  
     |  parent = <unbound qt slot parent of QFinalState type>
     |      X.parent(a) -> PythonQt.private.QObject
     |  
     |  parentState = <unbound qt slot parentState of QFinalState type>
     |      X.parentState(a) -> PythonQt.QtCore.QState
     |  
     |  property = <unbound qt slot property of QFinalState type>
     |      X.property(a, b) -> object
     |  
     |  removeEventFilter = <unbound qt slot removeEventFilter of QFinalState ...
     |      X.removeEventFilter(a, b)
     |  
     |  sender = <unbound qt slot sender of QFinalState type>
     |      X.sender(a) -> PythonQt.private.QObject
     |  
     |  senderSignalIndex = <unbound qt slot senderSignalIndex of QFinalState ...
     |      X.senderSignalIndex(a) -> int
     |  
     |  setObjectName = <unbound qt slot setObjectName of QFinalState type>
     |      X.setObjectName(a, b)
     |  
     |  setParent = <unbound qt slot setParent of QFinalState type>
     |      X.setParent(a, b)
     |  
     |  setProperty = <unbound qt slot setProperty of QFinalState type>
     |      X.setProperty(a, b, c) -> bool
     |  
     |  signalsBlocked = <unbound qt slot signalsBlocked of QFinalState type>
     |      X.signalsBlocked(a) -> bool
     |  
     |  startTimer = <unbound qt slot startTimer of QFinalState type>
     |      X.startTimer(a, b, c) -> int
     |  
     |  thread = <unbound qt slot thread of QFinalState type>
     |      X.thread(a)
     |  
     |  timerEvent = <unbound qt slot py_q_timerEvent of QFinalState type>
     |      X.timerEvent(a, b)
     |  
     |  tr = <unbound qt slot tr of QFinalState type>
     |      X.tr(a, b, c, d) -> str
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __delattr__(...)
     |      x.__delattr__('name') <==> del x.name
     |  
     |  __eq__(...)
     |      x.__eq__(y) <==> x==y
     |  
     |  __ge__(...)
     |      x.__ge__(y) <==> x>=y
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __gt__(...)
     |      x.__gt__(y) <==> x>y
     |  
     |  __hash__(...)
     |      x.__hash__() <==> hash(x)
     |  
     |  __le__(...)
     |      x.__le__(y) <==> x<=y
     |  
     |  __lt__(...)
     |      x.__lt__(y) <==> x<y
     |  
     |  __ne__(...)
     |      x.__ne__(y) <==> x!=y
     |  
     |  __nonzero__(...)
     |      x.__nonzero__() <==> x != 0
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __setattr__(...)
     |      x.__setattr__('name', value) <==> x.name = value
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __new__ = <built-in method __new__ of PythonQt.PythonQtClassWrapper ob...
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
    
    class QHistoryState(PythonQt.PythonQtInstanceWrapper)
     |  Method resolution order:
     |      QHistoryState
     |      PythonQt.PythonQtInstanceWrapper
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  __init__(...)
     |      x.__init__(...) initializes x; see help(type(x)) for signature
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  DeepHistory = 1
     |  
     |  HistoryType = <class 'PythonQt.QtCore.HistoryType'>
     |  
     |  
     |  ShallowHistory = 0
     |  
     |  active = None
     |  
     |  activeChanged = <unbound qt signal activeChanged of QHistoryState type...
     |  
     |  
     |  blockSignals = <unbound qt slot blockSignals of QHistoryState type>
     |      X.blockSignals(a, b) -> bool
     |  
     |  childEvent = <unbound qt slot py_q_childEvent of QHistoryState type>
     |      X.childEvent(a, b)
     |  
     |  children = <unbound qt slot children of QHistoryState type>
     |      X.children(a) -> tuple
     |  
     |  className = <built-in method className of PythonQt.PythonQtClassWrappe...
     |      Return the classname of the object
     |  
     |  connect = <unbound qt slot connect of QHistoryState type>
     |      X.connect(a, b, c, d, e) -> bool
     |  
     |  customEvent = <unbound qt slot py_q_customEvent of QHistoryState type>
     |      X.customEvent(a, b)
     |  
     |  defaultState = QAbstractState (QAbstractState at: 0x0)
     |  
     |  defaultStateChanged = <unbound qt signal defaultStateChanged of QHisto...
     |  
     |  
     |  defaultTransition = QAbstractTransition (QAbstractTransition at: 0x0)
     |  
     |  defaultTransitionChanged = <unbound qt signal defaultTransitionChanged...
     |  
     |  
     |  delete = <built-in method delete of PythonQt.PythonQtClassWrapper obje...
     |      Deletes the given C++ object
     |  
     |  deleteLater = <unbound qt slot deleteLater of QHistoryState type>
     |      X.deleteLater()
     |  
     |  destroyed = <unbound qt signal destroyed of QHistoryState type>
     |  
     |  
     |  disconnect = <unbound qt slot disconnect of QHistoryState type>
     |      X.disconnect(a, b, c, d) -> bool
     |  
     |  dumpObjectInfo = <unbound qt slot dumpObjectInfo of QHistoryState type...
     |      X.dumpObjectInfo(a)
     |  
     |  dumpObjectTree = <unbound qt slot dumpObjectTree of QHistoryState type...
     |      X.dumpObjectTree(a)
     |  
     |  dynamicPropertyNames = <unbound qt slot dynamicPropertyNames of QHisto...
     |      X.dynamicPropertyNames(a)
     |  
     |  entered = <unbound qt signal entered of QHistoryState type>
     |  
     |  
     |  event = <unbound qt slot py_q_event of QHistoryState type>
     |      X.event(a, b) -> bool
     |  
     |  eventFilter = <unbound qt slot py_q_eventFilter of QHistoryState type>
     |      X.eventFilter(a, b, c) -> bool
     |  
     |  exited = <unbound qt signal exited of QHistoryState type>
     |  
     |  
     |  findChild = <unbound qt slot findChild of QHistoryState type>
     |      X.findChild(a, b, c) -> PythonQt.private.QObject
     |  
     |  findChildren = <unbound qt slot findChildren of QHistoryState type>
     |      X.findChildren(a, b, c) -> tuple
     |  
     |  help = <built-in method help of PythonQt.PythonQtClassWrapper object>
     |      Shows the help of available methods for this class
     |  
     |  historyType = None
     |  
     |  historyTypeChanged = <unbound qt signal historyTypeChanged of QHistory...
     |  
     |  
     |  inherits = <built-in method inherits of PythonQt.PythonQtClassWrapper ...
     |      Returns if the class inherits or is of given type name
     |  
     |  installEventFilter = <unbound qt slot installEventFilter of QHistorySt...
     |      X.installEventFilter(a, b)
     |  
     |  isSignalConnected = <unbound qt slot isSignalConnected of QHistoryStat...
     |      X.isSignalConnected(a, b) -> bool
     |  
     |  isWidgetType = <unbound qt slot isWidgetType of QHistoryState type>
     |      X.isWidgetType(a) -> bool
     |  
     |  isWindowType = <unbound qt slot isWindowType of QHistoryState type>
     |      X.isWindowType(a) -> bool
     |  
     |  killTimer = <unbound qt slot killTimer of QHistoryState type>
     |      X.killTimer(a, b)
     |  
     |  machine = <unbound qt slot machine of QHistoryState type>
     |      X.machine(a) -> PythonQt.QtCore.QStateMachine
     |  
     |  metaObject = <unbound qt slot metaObject of QHistoryState type>
     |      X.metaObject(a) -> PythonQt.QtCore.QMetaObject
     |  
     |  moveToThread = <unbound qt slot moveToThread of QHistoryState type>
     |      X.moveToThread(a, b)
     |  
     |  objectName = None
     |  
     |  objectNameChanged = <unbound qt signal objectNameChanged of QHistorySt...
     |  
     |  
     |  onEntry = <unbound qt slot py_q_onEntry of QHistoryState type>
     |      X.onEntry(a, b)
     |  
     |  onExit = <unbound qt slot py_q_onExit of QHistoryState type>
     |      X.onExit(a, b)
     |  
     |  parent = <unbound qt slot parent of QHistoryState type>
     |      X.parent(a) -> PythonQt.private.QObject
     |  
     |  parentState = <unbound qt slot parentState of QHistoryState type>
     |      X.parentState(a) -> PythonQt.QtCore.QState
     |  
     |  property = <unbound qt slot property of QHistoryState type>
     |      X.property(a, b) -> object
     |  
     |  removeEventFilter = <unbound qt slot removeEventFilter of QHistoryStat...
     |      X.removeEventFilter(a, b)
     |  
     |  sender = <unbound qt slot sender of QHistoryState type>
     |      X.sender(a) -> PythonQt.private.QObject
     |  
     |  senderSignalIndex = <unbound qt slot senderSignalIndex of QHistoryStat...
     |      X.senderSignalIndex(a) -> int
     |  
     |  setDefaultState = <unbound qt slot setDefaultState of QHistoryState ty...
     |      X.setDefaultState(a, b)
     |  
     |  setDefaultTransition = <unbound qt slot setDefaultTransition of QHisto...
     |      X.setDefaultTransition(a, b)
     |  
     |  setHistoryType = <unbound qt slot setHistoryType of QHistoryState type...
     |      X.setHistoryType(a, b)
     |  
     |  setObjectName = <unbound qt slot setObjectName of QHistoryState type>
     |      X.setObjectName(a, b)
     |  
     |  setParent = <unbound qt slot setParent of QHistoryState type>
     |      X.setParent(a, b)
     |  
     |  setProperty = <unbound qt slot setProperty of QHistoryState type>
     |      X.setProperty(a, b, c) -> bool
     |  
     |  signalsBlocked = <unbound qt slot signalsBlocked of QHistoryState type...
     |      X.signalsBlocked(a) -> bool
     |  
     |  startTimer = <unbound qt slot startTimer of QHistoryState type>
     |      X.startTimer(a, b, c) -> int
     |  
     |  thread = <unbound qt slot thread of QHistoryState type>
     |      X.thread(a)
     |  
     |  timerEvent = <unbound qt slot py_q_timerEvent of QHistoryState type>
     |      X.timerEvent(a, b)
     |  
     |  tr = <unbound qt slot tr of QHistoryState type>
     |      X.tr(a, b, c, d) -> str
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __delattr__(...)
     |      x.__delattr__('name') <==> del x.name
     |  
     |  __eq__(...)
     |      x.__eq__(y) <==> x==y
     |  
     |  __ge__(...)
     |      x.__ge__(y) <==> x>=y
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __gt__(...)
     |      x.__gt__(y) <==> x>y
     |  
     |  __hash__(...)
     |      x.__hash__() <==> hash(x)
     |  
     |  __le__(...)
     |      x.__le__(y) <==> x<=y
     |  
     |  __lt__(...)
     |      x.__lt__(y) <==> x<y
     |  
     |  __ne__(...)
     |      x.__ne__(y) <==> x!=y
     |  
     |  __nonzero__(...)
     |      x.__nonzero__() <==> x != 0
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __setattr__(...)
     |      x.__setattr__('name', value) <==> x.name = value
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __new__ = <built-in method __new__ of PythonQt.PythonQtClassWrapper ob...
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
    
    class QIODevice(PythonQt.PythonQtInstanceWrapper)
     |  Method resolution order:
     |      QIODevice
     |      PythonQt.PythonQtInstanceWrapper
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  __init__(...)
     |      x.__init__(...) initializes x; see help(type(x)) for signature
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  Append = 4
     |  
     |  NotOpen = 0
     |  
     |  OpenMode = <class 'PythonQt.QtCore.OpenMode'>
     |  
     |  
     |  OpenModeFlag = <class 'PythonQt.QtCore.OpenModeFlag'>
     |  
     |  
     |  ReadOnly = 1
     |  
     |  ReadWrite = 3
     |  
     |  Text = 16
     |  
     |  Truncate = 8
     |  
     |  Unbuffered = 32
     |  
     |  WriteOnly = 2
     |  
     |  aboutToClose = <unbound qt signal aboutToClose of QIODevice type>
     |  
     |  
     |  atEnd = <unbound qt slot py_q_atEnd of QIODevice type>
     |      X.atEnd(a) -> bool
     |  
     |  blockSignals = <unbound qt slot blockSignals of QIODevice type>
     |      X.blockSignals(a, b) -> bool
     |  
     |  bytesAvailable = <unbound qt slot py_q_bytesAvailable of QIODevice typ...
     |      X.bytesAvailable(a) -> int
     |  
     |  bytesToWrite = <unbound qt slot py_q_bytesToWrite of QIODevice type>
     |      X.bytesToWrite(a) -> int
     |  
     |  bytesWritten = <unbound qt signal bytesWritten of QIODevice type>
     |  
     |  
     |  canReadLine = <unbound qt slot py_q_canReadLine of QIODevice type>
     |      X.canReadLine(a) -> bool
     |  
     |  channelBytesWritten = <unbound qt signal channelBytesWritten of QIODev...
     |  
     |  
     |  channelReadyRead = <unbound qt signal channelReadyRead of QIODevice ty...
     |  
     |  
     |  childEvent = <unbound qt slot py_q_childEvent of QIODevice type>
     |      X.childEvent(a, b)
     |  
     |  children = <unbound qt slot children of QIODevice type>
     |      X.children(a) -> tuple
     |  
     |  className = <built-in method className of PythonQt.PythonQtClassWrappe...
     |      Return the classname of the object
     |  
     |  close = <unbound qt slot py_q_close of QIODevice type>
     |      X.close(a)
     |  
     |  connect = <unbound qt slot connect of QIODevice type>
     |      X.connect(a, b, c, d, e) -> bool
     |  
     |  customEvent = <unbound qt slot py_q_customEvent of QIODevice type>
     |      X.customEvent(a, b)
     |  
     |  delete = <built-in method delete of PythonQt.PythonQtClassWrapper obje...
     |      Deletes the given C++ object
     |  
     |  deleteLater = <unbound qt slot deleteLater of QIODevice type>
     |      X.deleteLater()
     |  
     |  destroyed = <unbound qt signal destroyed of QIODevice type>
     |  
     |  
     |  disconnect = <unbound qt slot disconnect of QIODevice type>
     |      X.disconnect(a, b, c, d) -> bool
     |  
     |  dumpObjectInfo = <unbound qt slot dumpObjectInfo of QIODevice type>
     |      X.dumpObjectInfo(a)
     |  
     |  dumpObjectTree = <unbound qt slot dumpObjectTree of QIODevice type>
     |      X.dumpObjectTree(a)
     |  
     |  dynamicPropertyNames = <unbound qt slot dynamicPropertyNames of QIODev...
     |      X.dynamicPropertyNames(a)
     |  
     |  errorString = <unbound qt slot errorString of QIODevice type>
     |      X.errorString(a) -> str
     |  
     |  event = <unbound qt slot py_q_event of QIODevice type>
     |      X.event(a, b) -> bool
     |  
     |  eventFilter = <unbound qt slot py_q_eventFilter of QIODevice type>
     |      X.eventFilter(a, b, c) -> bool
     |  
     |  findChild = <unbound qt slot findChild of QIODevice type>
     |      X.findChild(a, b, c) -> PythonQt.private.QObject
     |  
     |  findChildren = <unbound qt slot findChildren of QIODevice type>
     |      X.findChildren(a, b, c) -> tuple
     |  
     |  getChar = <unbound qt slot getChar of QIODevice type>
     |      X.getChar(a, b) -> bool
     |  
     |  help = <built-in method help of PythonQt.PythonQtClassWrapper object>
     |      Shows the help of available methods for this class
     |  
     |  inherits = <built-in method inherits of PythonQt.PythonQtClassWrapper ...
     |      Returns if the class inherits or is of given type name
     |  
     |  installEventFilter = <unbound qt slot installEventFilter of QIODevice ...
     |      X.installEventFilter(a, b)
     |  
     |  isOpen = <unbound qt slot isOpen of QIODevice type>
     |      X.isOpen(a) -> bool
     |  
     |  isReadable = <unbound qt slot isReadable of QIODevice type>
     |      X.isReadable(a) -> bool
     |  
     |  isSequential = <unbound qt slot py_q_isSequential of QIODevice type>
     |      X.isSequential(a) -> bool
     |  
     |  isSignalConnected = <unbound qt slot isSignalConnected of QIODevice ty...
     |      X.isSignalConnected(a, b) -> bool
     |  
     |  isTextModeEnabled = <unbound qt slot isTextModeEnabled of QIODevice ty...
     |      X.isTextModeEnabled(a) -> bool
     |  
     |  isWidgetType = <unbound qt slot isWidgetType of QIODevice type>
     |      X.isWidgetType(a) -> bool
     |  
     |  isWindowType = <unbound qt slot isWindowType of QIODevice type>
     |      X.isWindowType(a) -> bool
     |  
     |  isWritable = <unbound qt slot isWritable of QIODevice type>
     |      X.isWritable(a) -> bool
     |  
     |  killTimer = <unbound qt slot killTimer of QIODevice type>
     |      X.killTimer(a, b)
     |  
     |  metaObject = <unbound qt slot metaObject of QIODevice type>
     |      X.metaObject(a) -> PythonQt.QtCore.QMetaObject
     |  
     |  moveToThread = <unbound qt slot moveToThread of QIODevice type>
     |      X.moveToThread(a, b)
     |  
     |  objectName = None
     |  
     |  objectNameChanged = <unbound qt signal objectNameChanged of QIODevice ...
     |  
     |  
     |  open = <unbound qt slot py_q_open of QIODevice type>
     |      X.open(a, b) -> bool
     |  
     |  openMode = <unbound qt slot openMode of QIODevice type>
     |      X.openMode(a)
     |  
     |  parent = <unbound qt slot parent of QIODevice type>
     |      X.parent(a) -> PythonQt.private.QObject
     |  
     |  peek = <unbound qt slot peek of QIODevice type>
     |      X.peek(a, b) -> PythonQt.QtCore.QByteArray
     |  
     |  pos = <unbound qt slot py_q_pos of QIODevice type>
     |      X.pos(a) -> int
     |  
     |  property = <unbound qt slot property of QIODevice type>
     |      X.property(a, b) -> object
     |  
     |  putChar = <unbound qt slot putChar of QIODevice type>
     |      X.putChar(a, b) -> bool
     |  
     |  read = <unbound qt slot read of QIODevice type>
     |      X.read(a, b) -> PythonQt.QtCore.QByteArray
     |  
     |  readAll = <unbound qt slot readAll of QIODevice type>
     |      X.readAll(a) -> PythonQt.QtCore.QByteArray
     |  
     |  readChannelFinished = <unbound qt signal readChannelFinished of QIODev...
     |  
     |  
     |  readData = <unbound qt slot py_q_readData of QIODevice type>
     |      X.readData(a, b, c) -> int
     |  
     |  readLine = <unbound qt slot readLine of QIODevice type>
     |      X.readLine(a, b) -> PythonQt.QtCore.QByteArray
     |  
     |  readLineData = <unbound qt slot py_q_readLineData of QIODevice type>
     |      X.readLineData(a, b, c) -> int
     |  
     |  readyRead = <unbound qt signal readyRead of QIODevice type>
     |  
     |  
     |  removeEventFilter = <unbound qt slot removeEventFilter of QIODevice ty...
     |      X.removeEventFilter(a, b)
     |  
     |  reset = <unbound qt slot py_q_reset of QIODevice type>
     |      X.reset(a) -> bool
     |  
     |  seek = <unbound qt slot py_q_seek of QIODevice type>
     |      X.seek(a, b) -> bool
     |  
     |  sender = <unbound qt slot sender of QIODevice type>
     |      X.sender(a) -> PythonQt.private.QObject
     |  
     |  senderSignalIndex = <unbound qt slot senderSignalIndex of QIODevice ty...
     |      X.senderSignalIndex(a) -> int
     |  
     |  setErrorString = <unbound qt slot setErrorString of QIODevice type>
     |      X.setErrorString(a, b)
     |  
     |  setObjectName = <unbound qt slot setObjectName of QIODevice type>
     |      X.setObjectName(a, b)
     |  
     |  setOpenMode = <unbound qt slot setOpenMode of QIODevice type>
     |      X.setOpenMode(a, b)
     |  
     |  setParent = <unbound qt slot setParent of QIODevice type>
     |      X.setParent(a, b)
     |  
     |  setProperty = <unbound qt slot setProperty of QIODevice type>
     |      X.setProperty(a, b, c) -> bool
     |  
     |  setTextModeEnabled = <unbound qt slot setTextModeEnabled of QIODevice ...
     |      X.setTextModeEnabled(a, b)
     |  
     |  signalsBlocked = <unbound qt slot signalsBlocked of QIODevice type>
     |      X.signalsBlocked(a) -> bool
     |  
     |  size = <unbound qt slot py_q_size of QIODevice type>
     |      X.size(a) -> int
     |  
     |  startTimer = <unbound qt slot startTimer of QIODevice type>
     |      X.startTimer(a, b, c) -> int
     |  
     |  thread = <unbound qt slot thread of QIODevice type>
     |      X.thread(a)
     |  
     |  timerEvent = <unbound qt slot py_q_timerEvent of QIODevice type>
     |      X.timerEvent(a, b)
     |  
     |  tr = <unbound qt slot tr of QIODevice type>
     |      X.tr(a, b, c, d) -> str
     |  
     |  ungetChar = <unbound qt slot ungetChar of QIODevice type>
     |      X.ungetChar(a, b)
     |  
     |  waitForBytesWritten = <unbound qt slot py_q_waitForBytesWritten of QIO...
     |      X.waitForBytesWritten(a, b) -> bool
     |  
     |  waitForReadyRead = <unbound qt slot py_q_waitForReadyRead of QIODevice...
     |      X.waitForReadyRead(a, b) -> bool
     |  
     |  write = <unbound qt slot write of QIODevice type>
     |      X.write(a, b) -> int
     |  
     |  writeData = <unbound qt slot py_q_writeData of QIODevice type>
     |      X.writeData(a, b, c) -> int
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __delattr__(...)
     |      x.__delattr__('name') <==> del x.name
     |  
     |  __eq__(...)
     |      x.__eq__(y) <==> x==y
     |  
     |  __ge__(...)
     |      x.__ge__(y) <==> x>=y
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __gt__(...)
     |      x.__gt__(y) <==> x>y
     |  
     |  __hash__(...)
     |      x.__hash__() <==> hash(x)
     |  
     |  __le__(...)
     |      x.__le__(y) <==> x<=y
     |  
     |  __lt__(...)
     |      x.__lt__(y) <==> x<y
     |  
     |  __ne__(...)
     |      x.__ne__(y) <==> x!=y
     |  
     |  __nonzero__(...)
     |      x.__nonzero__() <==> x != 0
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __setattr__(...)
     |      x.__setattr__('name', value) <==> x.name = value
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __new__ = <built-in method __new__ of PythonQt.PythonQtClassWrapper ob...
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
    
    class QIdentityProxyModel(PythonQt.PythonQtInstanceWrapper)
     |  Method resolution order:
     |      QIdentityProxyModel
     |      PythonQt.PythonQtInstanceWrapper
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  __init__(...)
     |      x.__init__(...) initializes x; see help(type(x)) for signature
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  HorizontalSortHint = 2
     |  
     |  LayoutChangeHint = <class 'PythonQt.QtCore.LayoutChangeHint'>
     |  
     |  
     |  NoLayoutChangeHint = 0
     |  
     |  VerticalSortHint = 1
     |  
     |  beginInsertColumns = <unbound qt slot beginInsertColumns of QIdentityP...
     |      X.beginInsertColumns(a, b, c, d)
     |  
     |  beginInsertRows = <unbound qt slot beginInsertRows of QIdentityProxyMo...
     |      X.beginInsertRows(a, b, c, d)
     |  
     |  beginMoveColumns = <unbound qt slot beginMoveColumns of QIdentityProxy...
     |      X.beginMoveColumns(a, b, c, d, e, f) -> bool
     |  
     |  beginMoveRows = <unbound qt slot beginMoveRows of QIdentityProxyModel ...
     |      X.beginMoveRows(a, b, c, d, e, f) -> bool
     |  
     |  beginRemoveColumns = <unbound qt slot beginRemoveColumns of QIdentityP...
     |      X.beginRemoveColumns(a, b, c, d)
     |  
     |  beginRemoveRows = <unbound qt slot beginRemoveRows of QIdentityProxyMo...
     |      X.beginRemoveRows(a, b, c, d)
     |  
     |  beginResetModel = <unbound qt slot beginResetModel of QIdentityProxyMo...
     |      X.beginResetModel(a)
     |  
     |  blockSignals = <unbound qt slot blockSignals of QIdentityProxyModel ty...
     |      X.blockSignals(a, b) -> bool
     |  
     |  buddy = <unbound qt slot py_q_buddy of QIdentityProxyModel type>
     |      X.buddy(a, b) -> PythonQt.QtCore.QModelIndex
     |  
     |  canDropMimeData = <unbound qt slot py_q_canDropMimeData of QIdentityPr...
     |      X.canDropMimeData(a, b, c, d, e, f) -> bool
     |  
     |  canFetchMore = <unbound qt slot py_q_canFetchMore of QIdentityProxyMod...
     |      X.canFetchMore(a, b) -> bool
     |  
     |  changePersistentIndex = <unbound qt slot changePersistentIndex of QIde...
     |      X.changePersistentIndex(a, b, c)
     |  
     |  changePersistentIndexList = <unbound qt slot changePersistentIndexList...
     |      X.changePersistentIndexList(a, b, c)
     |  
     |  childEvent = <unbound qt slot py_q_childEvent of QIdentityProxyModel t...
     |      X.childEvent(a, b)
     |  
     |  children = <unbound qt slot children of QIdentityProxyModel type>
     |      X.children(a) -> tuple
     |  
     |  className = <built-in method className of PythonQt.PythonQtClassWrappe...
     |      Return the classname of the object
     |  
     |  columnCount = <unbound qt slot py_q_columnCount of QIdentityProxyModel...
     |      X.columnCount(a, b) -> int
     |  
     |  columnsAboutToBeInserted = <unbound qt signal columnsAboutToBeInserted...
     |  
     |  
     |  columnsAboutToBeMoved = <unbound qt signal columnsAboutToBeMoved of QI...
     |  
     |  
     |  columnsAboutToBeRemoved = <unbound qt signal columnsAboutToBeRemoved o...
     |  
     |  
     |  columnsInserted = <unbound qt signal columnsInserted of QIdentityProxy...
     |  
     |  
     |  columnsMoved = <unbound qt signal columnsMoved of QIdentityProxyModel ...
     |  
     |  
     |  columnsRemoved = <unbound qt signal columnsRemoved of QIdentityProxyMo...
     |  
     |  
     |  connect = <unbound qt slot connect of QIdentityProxyModel type>
     |      X.connect(a, b, c, d, e) -> bool
     |  
     |  createIndex = <unbound qt slot createIndex of QIdentityProxyModel type...
     |      X.createIndex(a, b, c, d) -> PythonQt.QtCore.QModelIndex
     |  
     |  customEvent = <unbound qt slot py_q_customEvent of QIdentityProxyModel...
     |      X.customEvent(a, b)
     |  
     |  data = <unbound qt slot py_q_data of QIdentityProxyModel type>
     |      X.data(a, b, c) -> object
     |  
     |  dataChanged = <unbound qt signal dataChanged of QIdentityProxyModel ty...
     |  
     |  
     |  decodeData = <unbound qt slot decodeData of QIdentityProxyModel type>
     |      X.decodeData(a, b, c, d, e) -> bool
     |  
     |  delete = <built-in method delete of PythonQt.PythonQtClassWrapper obje...
     |      Deletes the given C++ object
     |  
     |  deleteLater = <unbound qt slot deleteLater of QIdentityProxyModel type...
     |      X.deleteLater()
     |  
     |  destroyed = <unbound qt signal destroyed of QIdentityProxyModel type>
     |  
     |  
     |  disconnect = <unbound qt slot disconnect of QIdentityProxyModel type>
     |      X.disconnect(a, b, c, d) -> bool
     |  
     |  dropMimeData = <unbound qt slot py_q_dropMimeData of QIdentityProxyMod...
     |      X.dropMimeData(a, b, c, d, e, f) -> bool
     |  
     |  dumpObjectInfo = <unbound qt slot dumpObjectInfo of QIdentityProxyMode...
     |      X.dumpObjectInfo(a)
     |  
     |  dumpObjectTree = <unbound qt slot dumpObjectTree of QIdentityProxyMode...
     |      X.dumpObjectTree(a)
     |  
     |  dynamicPropertyNames = <unbound qt slot dynamicPropertyNames of QIdent...
     |      X.dynamicPropertyNames(a)
     |  
     |  encodeData = <unbound qt slot encodeData of QIdentityProxyModel type>
     |      X.encodeData(a, b, c)
     |  
     |  endInsertColumns = <unbound qt slot endInsertColumns of QIdentityProxy...
     |      X.endInsertColumns(a)
     |  
     |  endInsertRows = <unbound qt slot endInsertRows of QIdentityProxyModel ...
     |      X.endInsertRows(a)
     |  
     |  endMoveColumns = <unbound qt slot endMoveColumns of QIdentityProxyMode...
     |      X.endMoveColumns(a)
     |  
     |  endMoveRows = <unbound qt slot endMoveRows of QIdentityProxyModel type...
     |      X.endMoveRows(a)
     |  
     |  endRemoveColumns = <unbound qt slot endRemoveColumns of QIdentityProxy...
     |      X.endRemoveColumns(a)
     |  
     |  endRemoveRows = <unbound qt slot endRemoveRows of QIdentityProxyModel ...
     |      X.endRemoveRows(a)
     |  
     |  endResetModel = <unbound qt slot endResetModel of QIdentityProxyModel ...
     |      X.endResetModel(a)
     |  
     |  event = <unbound qt slot py_q_event of QIdentityProxyModel type>
     |      X.event(a, b) -> bool
     |  
     |  eventFilter = <unbound qt slot py_q_eventFilter of QIdentityProxyModel...
     |      X.eventFilter(a, b, c) -> bool
     |  
     |  fetchMore = <unbound qt slot py_q_fetchMore of QIdentityProxyModel typ...
     |      X.fetchMore(a, b)
     |  
     |  findChild = <unbound qt slot findChild of QIdentityProxyModel type>
     |      X.findChild(a, b, c) -> PythonQt.private.QObject
     |  
     |  findChildren = <unbound qt slot findChildren of QIdentityProxyModel ty...
     |      X.findChildren(a, b, c) -> tuple
     |  
     |  flags = <unbound qt slot py_q_flags of QIdentityProxyModel type>
     |      X.flags(a, b)
     |  
     |  hasChildren = <unbound qt slot py_q_hasChildren of QIdentityProxyModel...
     |      X.hasChildren(a, b) -> bool
     |  
     |  hasIndex = <unbound qt slot hasIndex of QIdentityProxyModel type>
     |      X.hasIndex(a, b, c, d) -> bool
     |  
     |  headerData = <unbound qt slot py_q_headerData of QIdentityProxyModel t...
     |      X.headerData(a, b, c, d) -> object
     |  
     |  headerDataChanged = <unbound qt signal headerDataChanged of QIdentityP...
     |  
     |  
     |  help = <built-in method help of PythonQt.PythonQtClassWrapper object>
     |      Shows the help of available methods for this class
     |  
     |  index = <unbound qt slot py_q_index of QIdentityProxyModel type>
     |      X.index(a, b, c, d) -> PythonQt.QtCore.QModelIndex
     |  
     |  inherits = <built-in method inherits of PythonQt.PythonQtClassWrapper ...
     |      Returns if the class inherits or is of given type name
     |  
     |  insertColumn = <unbound qt slot insertColumn of QIdentityProxyModel ty...
     |      X.insertColumn(a, b, c) -> bool
     |  
     |  insertColumns = <unbound qt slot py_q_insertColumns of QIdentityProxyM...
     |      X.insertColumns(a, b, c, d) -> bool
     |  
     |  insertRow = <unbound qt slot insertRow of QIdentityProxyModel type>
     |      X.insertRow(a, b, c) -> bool
     |  
     |  insertRows = <unbound qt slot py_q_insertRows of QIdentityProxyModel t...
     |      X.insertRows(a, b, c, d) -> bool
     |  
     |  installEventFilter = <unbound qt slot installEventFilter of QIdentityP...
     |      X.installEventFilter(a, b)
     |  
     |  isSignalConnected = <unbound qt slot isSignalConnected of QIdentityPro...
     |      X.isSignalConnected(a, b) -> bool
     |  
     |  isWidgetType = <unbound qt slot isWidgetType of QIdentityProxyModel ty...
     |      X.isWidgetType(a) -> bool
     |  
     |  isWindowType = <unbound qt slot isWindowType of QIdentityProxyModel ty...
     |      X.isWindowType(a) -> bool
     |  
     |  itemData = <unbound qt slot py_q_itemData of QIdentityProxyModel type>
     |      X.itemData(a, b) -> dict
     |  
     |  killTimer = <unbound qt slot killTimer of QIdentityProxyModel type>
     |      X.killTimer(a, b)
     |  
     |  layoutAboutToBeChanged = <unbound qt signal layoutAboutToBeChanged of ...
     |  
     |  
     |  layoutChanged = <unbound qt signal layoutChanged of QIdentityProxyMode...
     |  
     |  
     |  mapFromSource = <unbound qt slot py_q_mapFromSource of QIdentityProxyM...
     |      X.mapFromSource(a, b) -> PythonQt.QtCore.QModelIndex
     |  
     |  mapSelectionFromSource = <unbound qt slot py_q_mapSelectionFromSource ...
     |      X.mapSelectionFromSource(a, b) -> PythonQt.QtGui.QItemSelection
     |  
     |  mapSelectionToSource = <unbound qt slot py_q_mapSelectionToSource of Q...
     |      X.mapSelectionToSource(a, b) -> PythonQt.QtGui.QItemSelection
     |  
     |  mapToSource = <unbound qt slot py_q_mapToSource of QIdentityProxyModel...
     |      X.mapToSource(a, b) -> PythonQt.QtCore.QModelIndex
     |  
     |  match = <unbound qt slot py_q_match of QIdentityProxyModel type>
     |      X.match(a, b, c, d, e, f) -> tuple
     |  
     |  metaObject = <unbound qt slot metaObject of QIdentityProxyModel type>
     |      X.metaObject(a) -> PythonQt.QtCore.QMetaObject
     |  
     |  mimeData = <unbound qt slot py_q_mimeData of QIdentityProxyModel type>
     |      X.mimeData(a, b) -> PythonQt.QtCore.QMimeData
     |  
     |  mimeTypes = <unbound qt slot py_q_mimeTypes of QIdentityProxyModel typ...
     |      X.mimeTypes(a) -> tuple
     |  
     |  modelAboutToBeReset = <unbound qt signal modelAboutToBeReset of QIdent...
     |  
     |  
     |  modelReset = <unbound qt signal modelReset of QIdentityProxyModel type...
     |  
     |  
     |  moveColumn = <unbound qt slot moveColumn of QIdentityProxyModel type>
     |      X.moveColumn(a, b, c, d, e) -> bool
     |  
     |  moveColumns = <unbound qt slot py_q_moveColumns of QIdentityProxyModel...
     |      X.moveColumns(a, b, c, d, e, f) -> bool
     |  
     |  moveRow = <unbound qt slot moveRow of QIdentityProxyModel type>
     |      X.moveRow(a, b, c, d, e) -> bool
     |  
     |  moveRows = <unbound qt slot py_q_moveRows of QIdentityProxyModel type>
     |      X.moveRows(a, b, c, d, e, f) -> bool
     |  
     |  moveToThread = <unbound qt slot moveToThread of QIdentityProxyModel ty...
     |      X.moveToThread(a, b)
     |  
     |  objectName = None
     |  
     |  objectNameChanged = <unbound qt signal objectNameChanged of QIdentityP...
     |  
     |  
     |  parent = <unbound qt slot py_q_parent of QIdentityProxyModel type>
     |      X.parent(a, b) -> PythonQt.QtCore.QModelIndex
     |  
     |  persistentIndexList = <unbound qt slot persistentIndexList of QIdentit...
     |      X.persistentIndexList(a) -> tuple
     |  
     |  property = <unbound qt slot property of QIdentityProxyModel type>
     |      X.property(a, b) -> object
     |  
     |  removeColumn = <unbound qt slot removeColumn of QIdentityProxyModel ty...
     |      X.removeColumn(a, b, c) -> bool
     |  
     |  removeColumns = <unbound qt slot py_q_removeColumns of QIdentityProxyM...
     |      X.removeColumns(a, b, c, d) -> bool
     |  
     |  removeEventFilter = <unbound qt slot removeEventFilter of QIdentityPro...
     |      X.removeEventFilter(a, b)
     |  
     |  removeRow = <unbound qt slot removeRow of QIdentityProxyModel type>
     |      X.removeRow(a, b, c) -> bool
     |  
     |  removeRows = <unbound qt slot py_q_removeRows of QIdentityProxyModel t...
     |      X.removeRows(a, b, c, d) -> bool
     |  
     |  revert = <unbound qt slot py_q_revert of QIdentityProxyModel type>
     |      X.revert(a)
     |  
     |  roleNames = <unbound qt slot py_q_roleNames of QIdentityProxyModel typ...
     |      X.roleNames(a) -> dict
     |  
     |  rowCount = <unbound qt slot py_q_rowCount of QIdentityProxyModel type>
     |      X.rowCount(a, b) -> int
     |  
     |  rowsAboutToBeInserted = <unbound qt signal rowsAboutToBeInserted of QI...
     |  
     |  
     |  rowsAboutToBeMoved = <unbound qt signal rowsAboutToBeMoved of QIdentit...
     |  
     |  
     |  rowsAboutToBeRemoved = <unbound qt signal rowsAboutToBeRemoved of QIde...
     |  
     |  
     |  rowsInserted = <unbound qt signal rowsInserted of QIdentityProxyModel ...
     |  
     |  
     |  rowsMoved = <unbound qt signal rowsMoved of QIdentityProxyModel type>
     |  
     |  
     |  rowsRemoved = <unbound qt signal rowsRemoved of QIdentityProxyModel ty...
     |  
     |  
     |  sender = <unbound qt slot sender of QIdentityProxyModel type>
     |      X.sender(a) -> PythonQt.private.QObject
     |  
     |  senderSignalIndex = <unbound qt slot senderSignalIndex of QIdentityPro...
     |      X.senderSignalIndex(a) -> int
     |  
     |  setData = <unbound qt slot py_q_setData of QIdentityProxyModel type>
     |      X.setData(a, b, c, d) -> bool
     |  
     |  setHeaderData = <unbound qt slot py_q_setHeaderData of QIdentityProxyM...
     |      X.setHeaderData(a, b, c, d, e) -> bool
     |  
     |  setItemData = <unbound qt slot py_q_setItemData of QIdentityProxyModel...
     |      X.setItemData(a, b, c) -> bool
     |  
     |  setObjectName = <unbound qt slot setObjectName of QIdentityProxyModel ...
     |      X.setObjectName(a, b)
     |  
     |  setParent = <unbound qt slot setParent of QIdentityProxyModel type>
     |      X.setParent(a, b)
     |  
     |  setProperty = <unbound qt slot setProperty of QIdentityProxyModel type...
     |      X.setProperty(a, b, c) -> bool
     |  
     |  setSourceModel = <unbound qt slot py_q_setSourceModel of QIdentityProx...
     |      X.setSourceModel(a, b)
     |  
     |  sibling = <unbound qt slot py_q_sibling of QIdentityProxyModel type>
     |      X.sibling(a, b, c, d) -> PythonQt.QtCore.QModelIndex
     |  
     |  signalsBlocked = <unbound qt slot signalsBlocked of QIdentityProxyMode...
     |      X.signalsBlocked(a) -> bool
     |  
     |  sort = <unbound qt slot py_q_sort of QIdentityProxyModel type>
     |      X.sort(a, b, c)
     |  
     |  sourceModel = QAbstractItemModel (QAbstractItemModel at: 0x0)
     |  
     |  sourceModelChanged = <unbound qt signal sourceModelChanged of QIdentit...
     |  
     |  
     |  span = <unbound qt slot py_q_span of QIdentityProxyModel type>
     |      X.span(a, b) -> PythonQt.QtCore.QSize
     |  
     |  startTimer = <unbound qt slot startTimer of QIdentityProxyModel type>
     |      X.startTimer(a, b, c) -> int
     |  
     |  submit = <unbound qt slot py_q_submit of QIdentityProxyModel type>
     |      X.submit(a) -> bool
     |  
     |  supportedDragActions = <unbound qt slot py_q_supportedDragActions of Q...
     |      X.supportedDragActions(a)
     |  
     |  supportedDropActions = <unbound qt slot py_q_supportedDropActions of Q...
     |      X.supportedDropActions(a)
     |  
     |  thread = <unbound qt slot thread of QIdentityProxyModel type>
     |      X.thread(a)
     |  
     |  timerEvent = <unbound qt slot py_q_timerEvent of QIdentityProxyModel t...
     |      X.timerEvent(a, b)
     |  
     |  tr = <unbound qt slot tr of QIdentityProxyModel type>
     |      X.tr(a, b, c, d) -> str
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __delattr__(...)
     |      x.__delattr__('name') <==> del x.name
     |  
     |  __eq__(...)
     |      x.__eq__(y) <==> x==y
     |  
     |  __ge__(...)
     |      x.__ge__(y) <==> x>=y
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __gt__(...)
     |      x.__gt__(y) <==> x>y
     |  
     |  __hash__(...)
     |      x.__hash__() <==> hash(x)
     |  
     |  __le__(...)
     |      x.__le__(y) <==> x<=y
     |  
     |  __lt__(...)
     |      x.__lt__(y) <==> x<y
     |  
     |  __ne__(...)
     |      x.__ne__(y) <==> x!=y
     |  
     |  __nonzero__(...)
     |      x.__nonzero__() <==> x != 0
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __setattr__(...)
     |      x.__setattr__('name', value) <==> x.name = value
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __new__ = <built-in method __new__ of PythonQt.PythonQtClassWrapper ob...
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
    
    class QJsonArray(PythonQt.PythonQtInstanceWrapper)
     |  Method resolution order:
     |      QJsonArray
     |      PythonQt.PythonQtInstanceWrapper
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  __add__(...)
     |      x.__add__(y) <==> x+y
     |  
     |  __eq__(...)
     |      x.__eq__(y) <==> x==y
     |  
     |  __iadd__(...)
     |      x.__iadd__(y) <==> x+=y
     |  
     |  __init__(...)
     |      x.__init__(...) initializes x; see help(type(x)) for signature
     |  
     |  __ne__(...)
     |      x.__ne__(y) <==> x!=y
     |  
     |  __radd__(...)
     |      x.__radd__(y) <==> y+x
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  __lshift__ = <unbound qt slot __lshift__ of QJsonArray type>
     |      X.__lshift__(a, b) -> PythonQt.QtCore.QJsonArray
     |  
     |  append = <unbound qt slot append of QJsonArray type>
     |      X.append(a, b)
     |  
     |  at = <unbound qt slot at of QJsonArray type>
     |      X.at(a, b) -> PythonQt.QtCore.QJsonValue
     |  
     |  className = <built-in method className of PythonQt.PythonQtClassWrappe...
     |      Return the classname of the object
     |  
     |  contains = <unbound qt slot contains of QJsonArray type>
     |      X.contains(a, b) -> bool
     |  
     |  count = <unbound qt slot count of QJsonArray type>
     |      X.count(a) -> int
     |  
     |  delete = <built-in method delete of PythonQt.PythonQtClassWrapper obje...
     |      Deletes the given C++ object
     |  
     |  empty = <unbound qt slot empty of QJsonArray type>
     |      X.empty(a) -> bool
     |  
     |  first = <unbound qt slot first of QJsonArray type>
     |      X.first(a) -> PythonQt.QtCore.QJsonValue
     |  
     |  fromStringList = <unbound qt slot static_QJsonArray_fromStringList of ...
     |      X.fromStringList(a) -> PythonQt.QtCore.QJsonArray
     |  
     |  fromVariantList = <unbound qt slot static_QJsonArray_fromVariantList o...
     |      X.fromVariantList(a) -> PythonQt.QtCore.QJsonArray
     |  
     |  help = <built-in method help of PythonQt.PythonQtClassWrapper object>
     |      Shows the help of available methods for this class
     |  
     |  inherits = <built-in method inherits of PythonQt.PythonQtClassWrapper ...
     |      Returns if the class inherits or is of given type name
     |  
     |  insert = <unbound qt slot insert of QJsonArray type>
     |      X.insert(a, b, c)
     |  
     |  isEmpty = <unbound qt slot isEmpty of QJsonArray type>
     |      X.isEmpty(a) -> bool
     |  
     |  last = <unbound qt slot last of QJsonArray type>
     |      X.last(a) -> PythonQt.QtCore.QJsonValue
     |  
     |  operator_assign = <unbound qt slot operator_assign of QJsonArray type>
     |      X.operator_assign(a, b) -> PythonQt.QtCore.QJsonArray
     |  
     |  operator_subscript = <unbound qt slot operator_subscript of QJsonArray...
     |      X.operator_subscript(a, b) -> PythonQt.QtCore.QJsonValue
     |  
     |  pop_back = <unbound qt slot pop_back of QJsonArray type>
     |      X.pop_back(a)
     |  
     |  pop_front = <unbound qt slot pop_front of QJsonArray type>
     |      X.pop_front(a)
     |  
     |  prepend = <unbound qt slot prepend of QJsonArray type>
     |      X.prepend(a, b)
     |  
     |  push_back = <unbound qt slot push_back of QJsonArray type>
     |      X.push_back(a, b)
     |  
     |  push_front = <unbound qt slot push_front of QJsonArray type>
     |      X.push_front(a, b)
     |  
     |  removeAt = <unbound qt slot removeAt of QJsonArray type>
     |      X.removeAt(a, b)
     |  
     |  removeFirst = <unbound qt slot removeFirst of QJsonArray type>
     |      X.removeFirst(a)
     |  
     |  removeLast = <unbound qt slot removeLast of QJsonArray type>
     |      X.removeLast(a)
     |  
     |  replace = <unbound qt slot replace of QJsonArray type>
     |      X.replace(a, b, c)
     |  
     |  size = <unbound qt slot size of QJsonArray type>
     |      X.size(a) -> int
     |  
     |  takeAt = <unbound qt slot takeAt of QJsonArray type>
     |      X.takeAt(a, b) -> PythonQt.QtCore.QJsonValue
     |  
     |  toVariantList = <unbound qt slot toVariantList of QJsonArray type>
     |      X.toVariantList(a) -> tuple
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __delattr__(...)
     |      x.__delattr__('name') <==> del x.name
     |  
     |  __ge__(...)
     |      x.__ge__(y) <==> x>=y
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __gt__(...)
     |      x.__gt__(y) <==> x>y
     |  
     |  __hash__(...)
     |      x.__hash__() <==> hash(x)
     |  
     |  __le__(...)
     |      x.__le__(y) <==> x<=y
     |  
     |  __lt__(...)
     |      x.__lt__(y) <==> x<y
     |  
     |  __nonzero__(...)
     |      x.__nonzero__() <==> x != 0
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __setattr__(...)
     |      x.__setattr__('name', value) <==> x.name = value
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __new__ = <built-in method __new__ of PythonQt.PythonQtClassWrapper ob...
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
    
    class QJsonDocument(PythonQt.PythonQtInstanceWrapper)
     |  Method resolution order:
     |      QJsonDocument
     |      PythonQt.PythonQtInstanceWrapper
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  __eq__(...)
     |      x.__eq__(y) <==> x==y
     |  
     |  __init__(...)
     |      x.__init__(...) initializes x; see help(type(x)) for signature
     |  
     |  __ne__(...)
     |      x.__ne__(y) <==> x!=y
     |  
     |  __nonzero__(...)
     |      x.__nonzero__() <==> x != 0
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  BypassValidation = 1
     |  
     |  Compact = 1
     |  
     |  DataValidation = <class 'PythonQt.QtCore.DataValidation'>
     |  
     |  
     |  Indented = 0
     |  
     |  JsonFormat = <class 'PythonQt.QtCore.JsonFormat'>
     |  
     |  
     |  Validate = 0
     |  
     |  array = <unbound qt slot array of QJsonDocument type>
     |      X.array(a) -> PythonQt.QtCore.QJsonArray
     |  
     |  className = <built-in method className of PythonQt.PythonQtClassWrappe...
     |      Return the classname of the object
     |  
     |  delete = <built-in method delete of PythonQt.PythonQtClassWrapper obje...
     |      Deletes the given C++ object
     |  
     |  fromBinaryData = <unbound qt slot static_QJsonDocument_fromBinaryData ...
     |      X.fromBinaryData(a, b) -> PythonQt.QtCore.QJsonDocument
     |  
     |  fromJson = <unbound qt slot static_QJsonDocument_fromJson of QJsonDocu...
     |      X.fromJson(a, b) -> PythonQt.QtCore.QJsonDocument
     |  
     |  fromRawData = <unbound qt slot static_QJsonDocument_fromRawData of QJs...
     |      X.fromRawData(a, b, c) -> PythonQt.QtCore.QJsonDocument
     |  
     |  fromVariant = <unbound qt slot static_QJsonDocument_fromVariant of QJs...
     |      X.fromVariant(a) -> PythonQt.QtCore.QJsonDocument
     |  
     |  help = <built-in method help of PythonQt.PythonQtClassWrapper object>
     |      Shows the help of available methods for this class
     |  
     |  inherits = <built-in method inherits of PythonQt.PythonQtClassWrapper ...
     |      Returns if the class inherits or is of given type name
     |  
     |  isArray = <unbound qt slot isArray of QJsonDocument type>
     |      X.isArray(a) -> bool
     |  
     |  isEmpty = <unbound qt slot isEmpty of QJsonDocument type>
     |      X.isEmpty(a) -> bool
     |  
     |  isNull = <unbound qt slot isNull of QJsonDocument type>
     |      X.isNull(a) -> bool
     |  
     |  isObject = <unbound qt slot isObject of QJsonDocument type>
     |      X.isObject(a) -> bool
     |  
     |  object = <unbound qt slot object of QJsonDocument type>
     |      X.object(a) -> PythonQt.QtCore.QJsonObject
     |  
     |  operator_assign = <unbound qt slot operator_assign of QJsonDocument ty...
     |      X.operator_assign(a, b) -> PythonQt.QtCore.QJsonDocument
     |  
     |  rawData = <unbound qt slot rawData of QJsonDocument type>
     |      X.rawData(a, b) -> int
     |  
     |  setArray = <unbound qt slot setArray of QJsonDocument type>
     |      X.setArray(a, b)
     |  
     |  setObject = <unbound qt slot setObject of QJsonDocument type>
     |      X.setObject(a, b)
     |  
     |  toBinaryData = <unbound qt slot toBinaryData of QJsonDocument type>
     |      X.toBinaryData(a) -> PythonQt.QtCore.QByteArray
     |  
     |  toJson = <unbound qt slot toJson of QJsonDocument type>
     |      X.toJson(a, b) -> PythonQt.QtCore.QByteArray
     |  
     |  toVariant = <unbound qt slot toVariant of QJsonDocument type>
     |      X.toVariant(a) -> object
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __delattr__(...)
     |      x.__delattr__('name') <==> del x.name
     |  
     |  __ge__(...)
     |      x.__ge__(y) <==> x>=y
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __gt__(...)
     |      x.__gt__(y) <==> x>y
     |  
     |  __hash__(...)
     |      x.__hash__() <==> hash(x)
     |  
     |  __le__(...)
     |      x.__le__(y) <==> x<=y
     |  
     |  __lt__(...)
     |      x.__lt__(y) <==> x<y
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __setattr__(...)
     |      x.__setattr__('name', value) <==> x.name = value
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __new__ = <built-in method __new__ of PythonQt.PythonQtClassWrapper ob...
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
    
    class QJsonObject(PythonQt.PythonQtInstanceWrapper)
     |  Method resolution order:
     |      QJsonObject
     |      PythonQt.PythonQtInstanceWrapper
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  __eq__(...)
     |      x.__eq__(y) <==> x==y
     |  
     |  __init__(...)
     |      x.__init__(...) initializes x; see help(type(x)) for signature
     |  
     |  __ne__(...)
     |      x.__ne__(y) <==> x!=y
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  className = <built-in method className of PythonQt.PythonQtClassWrappe...
     |      Return the classname of the object
     |  
     |  contains = <unbound qt slot contains of QJsonObject type>
     |      X.contains(a, b) -> bool
     |  
     |  count = <unbound qt slot count of QJsonObject type>
     |      X.count(a) -> int
     |  
     |  delete = <built-in method delete of PythonQt.PythonQtClassWrapper obje...
     |      Deletes the given C++ object
     |  
     |  empty = <unbound qt slot empty of QJsonObject type>
     |      X.empty(a) -> bool
     |  
     |  fromVariantHash = <unbound qt slot static_QJsonObject_fromVariantHash ...
     |      X.fromVariantHash(a) -> PythonQt.QtCore.QJsonObject
     |  
     |  fromVariantMap = <unbound qt slot static_QJsonObject_fromVariantMap of...
     |      X.fromVariantMap(a) -> PythonQt.QtCore.QJsonObject
     |  
     |  help = <built-in method help of PythonQt.PythonQtClassWrapper object>
     |      Shows the help of available methods for this class
     |  
     |  inherits = <built-in method inherits of PythonQt.PythonQtClassWrapper ...
     |      Returns if the class inherits or is of given type name
     |  
     |  isEmpty = <unbound qt slot isEmpty of QJsonObject type>
     |      X.isEmpty(a) -> bool
     |  
     |  keys = <unbound qt slot keys of QJsonObject type>
     |      X.keys(a) -> tuple
     |  
     |  length = <unbound qt slot length of QJsonObject type>
     |      X.length(a) -> int
     |  
     |  operator_assign = <unbound qt slot operator_assign of QJsonObject type...
     |      X.operator_assign(a, b) -> PythonQt.QtCore.QJsonObject
     |  
     |  operator_subscript = <unbound qt slot operator_subscript of QJsonObjec...
     |      X.operator_subscript(a, b) -> PythonQt.QtCore.QJsonValue
     |  
     |  remove = <unbound qt slot remove of QJsonObject type>
     |      X.remove(a, b)
     |  
     |  size = <unbound qt slot size of QJsonObject type>
     |      X.size(a) -> int
     |  
     |  take = <unbound qt slot take of QJsonObject type>
     |      X.take(a, b) -> PythonQt.QtCore.QJsonValue
     |  
     |  toVariantHash = <unbound qt slot toVariantHash of QJsonObject type>
     |      X.toVariantHash(a) -> dict
     |  
     |  toVariantMap = <unbound qt slot toVariantMap of QJsonObject type>
     |      X.toVariantMap(a) -> dict
     |  
     |  value = <unbound qt slot value of QJsonObject type>
     |      X.value(a, b) -> PythonQt.QtCore.QJsonValue
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __delattr__(...)
     |      x.__delattr__('name') <==> del x.name
     |  
     |  __ge__(...)
     |      x.__ge__(y) <==> x>=y
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __gt__(...)
     |      x.__gt__(y) <==> x>y
     |  
     |  __hash__(...)
     |      x.__hash__() <==> hash(x)
     |  
     |  __le__(...)
     |      x.__le__(y) <==> x<=y
     |  
     |  __lt__(...)
     |      x.__lt__(y) <==> x<y
     |  
     |  __nonzero__(...)
     |      x.__nonzero__() <==> x != 0
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __setattr__(...)
     |      x.__setattr__('name', value) <==> x.name = value
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __new__ = <built-in method __new__ of PythonQt.PythonQtClassWrapper ob...
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
    
    class QJsonParseError(PythonQt.PythonQtInstanceWrapper)
     |  Method resolution order:
     |      QJsonParseError
     |      PythonQt.PythonQtInstanceWrapper
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  __init__(...)
     |      x.__init__(...) initializes x; see help(type(x)) for signature
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  DeepNesting = 12
     |  
     |  DocumentTooLarge = 13
     |  
     |  GarbageAtEnd = 14
     |  
     |  IllegalEscapeSequence = 8
     |  
     |  IllegalNumber = 7
     |  
     |  IllegalUTF8String = 9
     |  
     |  IllegalValue = 5
     |  
     |  MissingNameSeparator = 2
     |  
     |  MissingObject = 11
     |  
     |  MissingValueSeparator = 4
     |  
     |  NoError = 0
     |  
     |  ParseError = <class 'PythonQt.QtCore.ParseError'>
     |  
     |  
     |  TerminationByNumber = 6
     |  
     |  UnterminatedArray = 3
     |  
     |  UnterminatedObject = 1
     |  
     |  UnterminatedString = 10
     |  
     |  className = <built-in method className of PythonQt.PythonQtClassWrappe...
     |      Return the classname of the object
     |  
     |  delete = <built-in method delete of PythonQt.PythonQtClassWrapper obje...
     |      Deletes the given C++ object
     |  
     |  error = None
     |  
     |  errorString = <unbound qt slot errorString of QJsonParseError type>
     |      X.errorString(a) -> str
     |  
     |  help = <built-in method help of PythonQt.PythonQtClassWrapper object>
     |      Shows the help of available methods for this class
     |  
     |  inherits = <built-in method inherits of PythonQt.PythonQtClassWrapper ...
     |      Returns if the class inherits or is of given type name
     |  
     |  offset = None
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __delattr__(...)
     |      x.__delattr__('name') <==> del x.name
     |  
     |  __eq__(...)
     |      x.__eq__(y) <==> x==y
     |  
     |  __ge__(...)
     |      x.__ge__(y) <==> x>=y
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __gt__(...)
     |      x.__gt__(y) <==> x>y
     |  
     |  __hash__(...)
     |      x.__hash__() <==> hash(x)
     |  
     |  __le__(...)
     |      x.__le__(y) <==> x<=y
     |  
     |  __lt__(...)
     |      x.__lt__(y) <==> x<y
     |  
     |  __ne__(...)
     |      x.__ne__(y) <==> x!=y
     |  
     |  __nonzero__(...)
     |      x.__nonzero__() <==> x != 0
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __setattr__(...)
     |      x.__setattr__('name', value) <==> x.name = value
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __new__ = <built-in method __new__ of PythonQt.PythonQtClassWrapper ob...
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
    
    class QJsonValue(PythonQt.PythonQtInstanceWrapper)
     |  Method resolution order:
     |      QJsonValue
     |      PythonQt.PythonQtInstanceWrapper
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  __eq__(...)
     |      x.__eq__(y) <==> x==y
     |  
     |  __init__(...)
     |      x.__init__(...) initializes x; see help(type(x)) for signature
     |  
     |  __ne__(...)
     |      x.__ne__(y) <==> x!=y
     |  
     |  __nonzero__(...)
     |      x.__nonzero__() <==> x != 0
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  Array = 4
     |  
     |  Bool = 1
     |  
     |  Double = 2
     |  
     |  Null = 0
     |  
     |  Object = 5
     |  
     |  String = 3
     |  
     |  Type = <class 'PythonQt.QtCore.Type'>
     |  
     |  
     |  Undefined = 128
     |  
     |  className = <built-in method className of PythonQt.PythonQtClassWrappe...
     |      Return the classname of the object
     |  
     |  delete = <built-in method delete of PythonQt.PythonQtClassWrapper obje...
     |      Deletes the given C++ object
     |  
     |  fromVariant = <unbound qt slot static_QJsonValue_fromVariant of QJsonV...
     |      X.fromVariant(a) -> PythonQt.QtCore.QJsonValue
     |  
     |  help = <built-in method help of PythonQt.PythonQtClassWrapper object>
     |      Shows the help of available methods for this class
     |  
     |  inherits = <built-in method inherits of PythonQt.PythonQtClassWrapper ...
     |      Returns if the class inherits or is of given type name
     |  
     |  isArray = <unbound qt slot isArray of QJsonValue type>
     |      X.isArray(a) -> bool
     |  
     |  isBool = <unbound qt slot isBool of QJsonValue type>
     |      X.isBool(a) -> bool
     |  
     |  isDouble = <unbound qt slot isDouble of QJsonValue type>
     |      X.isDouble(a) -> bool
     |  
     |  isNull = <unbound qt slot isNull of QJsonValue type>
     |      X.isNull(a) -> bool
     |  
     |  isObject = <unbound qt slot isObject of QJsonValue type>
     |      X.isObject(a) -> bool
     |  
     |  isString = <unbound qt slot isString of QJsonValue type>
     |      X.isString(a) -> bool
     |  
     |  isUndefined = <unbound qt slot isUndefined of QJsonValue type>
     |      X.isUndefined(a) -> bool
     |  
     |  operator_assign = <unbound qt slot operator_assign of QJsonValue type>
     |      X.operator_assign(a, b) -> PythonQt.QtCore.QJsonValue
     |  
     |  toArray = <unbound qt slot toArray of QJsonValue type>
     |      X.toArray(a, b) -> PythonQt.QtCore.QJsonArray
     |  
     |  toBool = <unbound qt slot toBool of QJsonValue type>
     |      X.toBool(a, b) -> bool
     |  
     |  toDouble = <unbound qt slot toDouble of QJsonValue type>
     |      X.toDouble(a, b) -> float
     |  
     |  toInt = <unbound qt slot toInt of QJsonValue type>
     |      X.toInt(a, b) -> int
     |  
     |  toObject = <unbound qt slot toObject of QJsonValue type>
     |      X.toObject(a, b) -> PythonQt.QtCore.QJsonObject
     |  
     |  toString = <unbound qt slot toString of QJsonValue type>
     |      X.toString(a, b) -> str
     |  
     |  toVariant = <unbound qt slot toVariant of QJsonValue type>
     |      X.toVariant(a) -> object
     |  
     |  type = <unbound qt slot type of QJsonValue type>
     |      X.type(a)
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __delattr__(...)
     |      x.__delattr__('name') <==> del x.name
     |  
     |  __ge__(...)
     |      x.__ge__(y) <==> x>=y
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __gt__(...)
     |      x.__gt__(y) <==> x>y
     |  
     |  __hash__(...)
     |      x.__hash__() <==> hash(x)
     |  
     |  __le__(...)
     |      x.__le__(y) <==> x<=y
     |  
     |  __lt__(...)
     |      x.__lt__(y) <==> x<y
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __setattr__(...)
     |      x.__setattr__('name', value) <==> x.name = value
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __new__ = <built-in method __new__ of PythonQt.PythonQtClassWrapper ob...
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
    
    class QLibrary(PythonQt.PythonQtInstanceWrapper)
     |  Method resolution order:
     |      QLibrary
     |      PythonQt.PythonQtInstanceWrapper
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  __init__(...)
     |      x.__init__(...) initializes x; see help(type(x)) for signature
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  DeepBindHint = 16
     |  
     |  ExportExternalSymbolsHint = 2
     |  
     |  LoadArchiveMemberHint = 4
     |  
     |  LoadHint = <class 'PythonQt.QtCore.LoadHint'>
     |  
     |  
     |  LoadHints = <class 'PythonQt.QtCore.LoadHints'>
     |  
     |  
     |  PreventUnloadHint = 8
     |  
     |  ResolveAllSymbolsHint = 1
     |  
     |  blockSignals = <unbound qt slot blockSignals of QLibrary type>
     |      X.blockSignals(a, b) -> bool
     |  
     |  childEvent = <unbound qt slot py_q_childEvent of QLibrary type>
     |      X.childEvent(a, b)
     |  
     |  children = <unbound qt slot children of QLibrary type>
     |      X.children(a) -> tuple
     |  
     |  className = <built-in method className of PythonQt.PythonQtClassWrappe...
     |      Return the classname of the object
     |  
     |  connect = <unbound qt slot connect of QLibrary type>
     |      X.connect(a, b, c, d, e) -> bool
     |  
     |  customEvent = <unbound qt slot py_q_customEvent of QLibrary type>
     |      X.customEvent(a, b)
     |  
     |  delete = <built-in method delete of PythonQt.PythonQtClassWrapper obje...
     |      Deletes the given C++ object
     |  
     |  deleteLater = <unbound qt slot deleteLater of QLibrary type>
     |      X.deleteLater()
     |  
     |  destroyed = <unbound qt signal destroyed of QLibrary type>
     |  
     |  
     |  disconnect = <unbound qt slot disconnect of QLibrary type>
     |      X.disconnect(a, b, c, d) -> bool
     |  
     |  dumpObjectInfo = <unbound qt slot dumpObjectInfo of QLibrary type>
     |      X.dumpObjectInfo(a)
     |  
     |  dumpObjectTree = <unbound qt slot dumpObjectTree of QLibrary type>
     |      X.dumpObjectTree(a)
     |  
     |  dynamicPropertyNames = <unbound qt slot dynamicPropertyNames of QLibra...
     |      X.dynamicPropertyNames(a)
     |  
     |  errorString = <unbound qt slot errorString of QLibrary type>
     |      X.errorString(a) -> str
     |  
     |  event = <unbound qt slot py_q_event of QLibrary type>
     |      X.event(a, b) -> bool
     |  
     |  eventFilter = <unbound qt slot py_q_eventFilter of QLibrary type>
     |      X.eventFilter(a, b, c) -> bool
     |  
     |  fileName = None
     |  
     |  findChild = <unbound qt slot findChild of QLibrary type>
     |      X.findChild(a, b, c) -> PythonQt.private.QObject
     |  
     |  findChildren = <unbound qt slot findChildren of QLibrary type>
     |      X.findChildren(a, b, c) -> tuple
     |  
     |  help = <built-in method help of PythonQt.PythonQtClassWrapper object>
     |      Shows the help of available methods for this class
     |  
     |  inherits = <built-in method inherits of PythonQt.PythonQtClassWrapper ...
     |      Returns if the class inherits or is of given type name
     |  
     |  installEventFilter = <unbound qt slot installEventFilter of QLibrary t...
     |      X.installEventFilter(a, b)
     |  
     |  isLibrary = <unbound qt slot static_QLibrary_isLibrary of QLibrary typ...
     |      X.isLibrary(a) -> bool
     |  
     |  isLoaded = <unbound qt slot isLoaded of QLibrary type>
     |      X.isLoaded(a) -> bool
     |  
     |  isSignalConnected = <unbound qt slot isSignalConnected of QLibrary typ...
     |      X.isSignalConnected(a, b) -> bool
     |  
     |  isWidgetType = <unbound qt slot isWidgetType of QLibrary type>
     |      X.isWidgetType(a) -> bool
     |  
     |  isWindowType = <unbound qt slot isWindowType of QLibrary type>
     |      X.isWindowType(a) -> bool
     |  
     |  killTimer = <unbound qt slot killTimer of QLibrary type>
     |      X.killTimer(a, b)
     |  
     |  load = <unbound qt slot load of QLibrary type>
     |      X.load(a) -> bool
     |  
     |  loadHints = None
     |  
     |  metaObject = <unbound qt slot metaObject of QLibrary type>
     |      X.metaObject(a) -> PythonQt.QtCore.QMetaObject
     |  
     |  moveToThread = <unbound qt slot moveToThread of QLibrary type>
     |      X.moveToThread(a, b)
     |  
     |  objectName = None
     |  
     |  objectNameChanged = <unbound qt signal objectNameChanged of QLibrary t...
     |  
     |  
     |  parent = <unbound qt slot parent of QLibrary type>
     |      X.parent(a) -> PythonQt.private.QObject
     |  
     |  property = <unbound qt slot property of QLibrary type>
     |      X.property(a, b) -> object
     |  
     |  removeEventFilter = <unbound qt slot removeEventFilter of QLibrary typ...
     |      X.removeEventFilter(a, b)
     |  
     |  sender = <unbound qt slot sender of QLibrary type>
     |      X.sender(a) -> PythonQt.private.QObject
     |  
     |  senderSignalIndex = <unbound qt slot senderSignalIndex of QLibrary typ...
     |      X.senderSignalIndex(a) -> int
     |  
     |  setFileName = <unbound qt slot setFileName of QLibrary type>
     |      X.setFileName(a, b)
     |  
     |  setFileNameAndVersion = <unbound qt slot setFileNameAndVersion of QLib...
     |      X.setFileNameAndVersion(a, b, c)
     |  
     |  setLoadHints = <unbound qt slot setLoadHints of QLibrary type>
     |      X.setLoadHints(a, b)
     |  
     |  setObjectName = <unbound qt slot setObjectName of QLibrary type>
     |      X.setObjectName(a, b)
     |  
     |  setParent = <unbound qt slot setParent of QLibrary type>
     |      X.setParent(a, b)
     |  
     |  setProperty = <unbound qt slot setProperty of QLibrary type>
     |      X.setProperty(a, b, c) -> bool
     |  
     |  signalsBlocked = <unbound qt slot signalsBlocked of QLibrary type>
     |      X.signalsBlocked(a) -> bool
     |  
     |  startTimer = <unbound qt slot startTimer of QLibrary type>
     |      X.startTimer(a, b, c) -> int
     |  
     |  thread = <unbound qt slot thread of QLibrary type>
     |      X.thread(a)
     |  
     |  timerEvent = <unbound qt slot py_q_timerEvent of QLibrary type>
     |      X.timerEvent(a, b)
     |  
     |  tr = <unbound qt slot tr of QLibrary type>
     |      X.tr(a, b, c, d) -> str
     |  
     |  unload = <unbound qt slot unload of QLibrary type>
     |      X.unload(a) -> bool
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __delattr__(...)
     |      x.__delattr__('name') <==> del x.name
     |  
     |  __eq__(...)
     |      x.__eq__(y) <==> x==y
     |  
     |  __ge__(...)
     |      x.__ge__(y) <==> x>=y
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __gt__(...)
     |      x.__gt__(y) <==> x>y
     |  
     |  __hash__(...)
     |      x.__hash__() <==> hash(x)
     |  
     |  __le__(...)
     |      x.__le__(y) <==> x<=y
     |  
     |  __lt__(...)
     |      x.__lt__(y) <==> x<y
     |  
     |  __ne__(...)
     |      x.__ne__(y) <==> x!=y
     |  
     |  __nonzero__(...)
     |      x.__nonzero__() <==> x != 0
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __setattr__(...)
     |      x.__setattr__('name', value) <==> x.name = value
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __new__ = <built-in method __new__ of PythonQt.PythonQtClassWrapper ob...
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
    
    class QLibraryInfo(PythonQt.PythonQtInstanceWrapper)
     |  Method resolution order:
     |      QLibraryInfo
     |      PythonQt.PythonQtInstanceWrapper
     |      __builtin__.object
     |  
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  ArchDataPath = 9
     |  
     |  BinariesPath = 5
     |  
     |  DataPath = 10
     |  
     |  DocumentationPath = 1
     |  
     |  ExamplesPath = 12
     |  
     |  HeadersPath = 2
     |  
     |  ImportsPath = 7
     |  
     |  LibrariesPath = 3
     |  
     |  LibraryExecutablesPath = 4
     |  
     |  LibraryLocation = <class 'PythonQt.QtCore.LibraryLocation'>
     |  
     |  
     |  PluginsPath = 6
     |  
     |  PrefixPath = 0
     |  
     |  Qml2ImportsPath = 8
     |  
     |  SettingsPath = 100
     |  
     |  TestsPath = 13
     |  
     |  TranslationsPath = 11
     |  
     |  build = <unbound qt slot static_QLibraryInfo_build of QLibraryInfo typ...
     |      X.build() -> int
     |  
     |  buildDate = <unbound qt slot static_QLibraryInfo_buildDate of QLibrary...
     |      X.buildDate() -> PythonQt.QtCore.QDate
     |  
     |  className = <built-in method className of PythonQt.PythonQtClassWrappe...
     |      Return the classname of the object
     |  
     |  delete = <built-in method delete of PythonQt.PythonQtClassWrapper obje...
     |      Deletes the given C++ object
     |  
     |  help = <built-in method help of PythonQt.PythonQtClassWrapper object>
     |      Shows the help of available methods for this class
     |  
     |  inherits = <built-in method inherits of PythonQt.PythonQtClassWrapper ...
     |      Returns if the class inherits or is of given type name
     |  
     |  isDebugBuild = <unbound qt slot static_QLibraryInfo_isDebugBuild of QL...
     |      X.isDebugBuild() -> bool
     |  
     |  licensedProducts = <unbound qt slot static_QLibraryInfo_licensedProduc...
     |      X.licensedProducts() -> str
     |  
     |  licensee = <unbound qt slot static_QLibraryInfo_licensee of QLibraryIn...
     |      X.licensee() -> str
     |  
     |  location = <unbound qt slot static_QLibraryInfo_location of QLibraryIn...
     |      X.location(a) -> str
     |  
     |  platformPluginArguments = <unbound qt slot static_QLibraryInfo_platfor...
     |      X.platformPluginArguments(a) -> tuple
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __delattr__(...)
     |      x.__delattr__('name') <==> del x.name
     |  
     |  __eq__(...)
     |      x.__eq__(y) <==> x==y
     |  
     |  __ge__(...)
     |      x.__ge__(y) <==> x>=y
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __gt__(...)
     |      x.__gt__(y) <==> x>y
     |  
     |  __hash__(...)
     |      x.__hash__() <==> hash(x)
     |  
     |  __init__(...)
     |      x.__init__(...) initializes x; see help(type(x)) for signature
     |  
     |  __le__(...)
     |      x.__le__(y) <==> x<=y
     |  
     |  __lt__(...)
     |      x.__lt__(y) <==> x<y
     |  
     |  __ne__(...)
     |      x.__ne__(y) <==> x!=y
     |  
     |  __nonzero__(...)
     |      x.__nonzero__() <==> x != 0
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __setattr__(...)
     |      x.__setattr__('name', value) <==> x.name = value
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __new__ = <built-in method __new__ of PythonQt.PythonQtClassWrapper ob...
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
    
    class QLine(PythonQt.PythonQtInstanceWrapper)
     |  Method resolution order:
     |      QLine
     |      PythonQt.PythonQtInstanceWrapper
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  __eq__(...)
     |      x.__eq__(y) <==> x==y
     |  
     |  __init__(...)
     |      x.__init__(...) initializes x; see help(type(x)) for signature
     |  
     |  __mul__(...)
     |      x.__mul__(y) <==> x*y
     |  
     |  __ne__(...)
     |      x.__ne__(y) <==> x!=y
     |  
     |  __nonzero__(...)
     |      x.__nonzero__() <==> x != 0
     |  
     |  __rmul__(...)
     |      x.__rmul__(y) <==> y*x
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  className = <built-in method className of PythonQt.PythonQtClassWrappe...
     |      Return the classname of the object
     |  
     |  delete = <built-in method delete of PythonQt.PythonQtClassWrapper obje...
     |      Deletes the given C++ object
     |  
     |  dx = <unbound qt slot dx of QLine type>
     |      X.dx(a) -> int
     |  
     |  dy = <unbound qt slot dy of QLine type>
     |      X.dy(a) -> int
     |  
     |  help = <built-in method help of PythonQt.PythonQtClassWrapper object>
     |      Shows the help of available methods for this class
     |  
     |  inherits = <built-in method inherits of PythonQt.PythonQtClassWrapper ...
     |      Returns if the class inherits or is of given type name
     |  
     |  isNull = <unbound qt slot isNull of QLine type>
     |      X.isNull(a) -> bool
     |  
     |  p1 = <unbound qt slot p1 of QLine type>
     |      X.p1(a) -> PythonQt.QtCore.QPoint
     |  
     |  p2 = <unbound qt slot p2 of QLine type>
     |      X.p2(a) -> PythonQt.QtCore.QPoint
     |  
     |  readFrom = <unbound qt slot readFrom of QLine type>
     |      X.readFrom(a, b)
     |  
     |  setLine = <unbound qt slot setLine of QLine type>
     |      X.setLine(a, b, c, d, e)
     |  
     |  setP1 = <unbound qt slot setP1 of QLine type>
     |      X.setP1(a, b)
     |  
     |  setP2 = <unbound qt slot setP2 of QLine type>
     |      X.setP2(a, b)
     |  
     |  setPoints = <unbound qt slot setPoints of QLine type>
     |      X.setPoints(a, b, c)
     |  
     |  translate = <unbound qt slot translate of QLine type>
     |      X.translate(a, b, c)
     |  
     |  translated = <unbound qt slot translated of QLine type>
     |      X.translated(a, b, c) -> PythonQt.QtCore.QLine
     |  
     |  writeTo = <unbound qt slot writeTo of QLine type>
     |      X.writeTo(a, b)
     |  
     |  x1 = <unbound qt slot x1 of QLine type>
     |      X.x1(a) -> int
     |  
     |  x2 = <unbound qt slot x2 of QLine type>
     |      X.x2(a) -> int
     |  
     |  y1 = <unbound qt slot y1 of QLine type>
     |      X.y1(a) -> int
     |  
     |  y2 = <unbound qt slot y2 of QLine type>
     |      X.y2(a) -> int
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __delattr__(...)
     |      x.__delattr__('name') <==> del x.name
     |  
     |  __ge__(...)
     |      x.__ge__(y) <==> x>=y
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __gt__(...)
     |      x.__gt__(y) <==> x>y
     |  
     |  __hash__(...)
     |      x.__hash__() <==> hash(x)
     |  
     |  __le__(...)
     |      x.__le__(y) <==> x<=y
     |  
     |  __lt__(...)
     |      x.__lt__(y) <==> x<y
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __setattr__(...)
     |      x.__setattr__('name', value) <==> x.name = value
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __new__ = <built-in method __new__ of PythonQt.PythonQtClassWrapper ob...
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
    
    class QLineF(PythonQt.PythonQtInstanceWrapper)
     |  Method resolution order:
     |      QLineF
     |      PythonQt.PythonQtInstanceWrapper
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  __eq__(...)
     |      x.__eq__(y) <==> x==y
     |  
     |  __init__(...)
     |      x.__init__(...) initializes x; see help(type(x)) for signature
     |  
     |  __mul__(...)
     |      x.__mul__(y) <==> x*y
     |  
     |  __ne__(...)
     |      x.__ne__(y) <==> x!=y
     |  
     |  __nonzero__(...)
     |      x.__nonzero__() <==> x != 0
     |  
     |  __rmul__(...)
     |      x.__rmul__(y) <==> y*x
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  BoundedIntersection = 1
     |  
     |  IntersectType = <class 'PythonQt.QtCore.IntersectType'>
     |  
     |  
     |  NoIntersection = 0
     |  
     |  UnboundedIntersection = 2
     |  
     |  angle = <unbound qt slot angle of QLineF type>
     |      X.angle(a, b) -> float
     |  
     |  angleTo = <unbound qt slot angleTo of QLineF type>
     |      X.angleTo(a, b) -> float
     |  
     |  className = <built-in method className of PythonQt.PythonQtClassWrappe...
     |      Return the classname of the object
     |  
     |  delete = <built-in method delete of PythonQt.PythonQtClassWrapper obje...
     |      Deletes the given C++ object
     |  
     |  dx = <unbound qt slot dx of QLineF type>
     |      X.dx(a) -> float
     |  
     |  dy = <unbound qt slot dy of QLineF type>
     |      X.dy(a) -> float
     |  
     |  fromPolar = <unbound qt slot static_QLineF_fromPolar of QLineF type>
     |      X.fromPolar(a, b) -> PythonQt.QtCore.QLineF
     |  
     |  help = <built-in method help of PythonQt.PythonQtClassWrapper object>
     |      Shows the help of available methods for this class
     |  
     |  inherits = <built-in method inherits of PythonQt.PythonQtClassWrapper ...
     |      Returns if the class inherits or is of given type name
     |  
     |  intersect = <unbound qt slot intersect of QLineF type>
     |      X.intersect(a, b, c)
     |  
     |  isNull = <unbound qt slot isNull of QLineF type>
     |      X.isNull(a) -> bool
     |  
     |  length = <unbound qt slot length of QLineF type>
     |      X.length(a) -> float
     |  
     |  normalVector = <unbound qt slot normalVector of QLineF type>
     |      X.normalVector(a) -> PythonQt.QtCore.QLineF
     |  
     |  p1 = <unbound qt slot p1 of QLineF type>
     |      X.p1(a) -> PythonQt.QtCore.QPointF
     |  
     |  p2 = <unbound qt slot p2 of QLineF type>
     |      X.p2(a) -> PythonQt.QtCore.QPointF
     |  
     |  pointAt = <unbound qt slot pointAt of QLineF type>
     |      X.pointAt(a, b) -> PythonQt.QtCore.QPointF
     |  
     |  readFrom = <unbound qt slot readFrom of QLineF type>
     |      X.readFrom(a, b)
     |  
     |  setAngle = <unbound qt slot setAngle of QLineF type>
     |      X.setAngle(a, b)
     |  
     |  setLength = <unbound qt slot setLength of QLineF type>
     |      X.setLength(a, b)
     |  
     |  setLine = <unbound qt slot setLine of QLineF type>
     |      X.setLine(a, b, c, d, e)
     |  
     |  setP1 = <unbound qt slot setP1 of QLineF type>
     |      X.setP1(a, b)
     |  
     |  setP2 = <unbound qt slot setP2 of QLineF type>
     |      X.setP2(a, b)
     |  
     |  setPoints = <unbound qt slot setPoints of QLineF type>
     |      X.setPoints(a, b, c)
     |  
     |  toLine = <unbound qt slot toLine of QLineF type>
     |      X.toLine(a) -> PythonQt.QtCore.QLine
     |  
     |  translate = <unbound qt slot translate of QLineF type>
     |      X.translate(a, b, c)
     |  
     |  translated = <unbound qt slot translated of QLineF type>
     |      X.translated(a, b, c) -> PythonQt.QtCore.QLineF
     |  
     |  unitVector = <unbound qt slot unitVector of QLineF type>
     |      X.unitVector(a) -> PythonQt.QtCore.QLineF
     |  
     |  writeTo = <unbound qt slot writeTo of QLineF type>
     |      X.writeTo(a, b)
     |  
     |  x1 = <unbound qt slot x1 of QLineF type>
     |      X.x1(a) -> float
     |  
     |  x2 = <unbound qt slot x2 of QLineF type>
     |      X.x2(a) -> float
     |  
     |  y1 = <unbound qt slot y1 of QLineF type>
     |      X.y1(a) -> float
     |  
     |  y2 = <unbound qt slot y2 of QLineF type>
     |      X.y2(a) -> float
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __delattr__(...)
     |      x.__delattr__('name') <==> del x.name
     |  
     |  __ge__(...)
     |      x.__ge__(y) <==> x>=y
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __gt__(...)
     |      x.__gt__(y) <==> x>y
     |  
     |  __hash__(...)
     |      x.__hash__() <==> hash(x)
     |  
     |  __le__(...)
     |      x.__le__(y) <==> x<=y
     |  
     |  __lt__(...)
     |      x.__lt__(y) <==> x<y
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __setattr__(...)
     |      x.__setattr__('name', value) <==> x.name = value
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __new__ = <built-in method __new__ of PythonQt.PythonQtClassWrapper ob...
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
    
    class QLocale(PythonQt.PythonQtInstanceWrapper)
     |  Method resolution order:
     |      QLocale
     |      PythonQt.PythonQtInstanceWrapper
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  __eq__(...)
     |      x.__eq__(y) <==> x==y
     |  
     |  __init__(...)
     |      x.__init__(...) initializes x; see help(type(x)) for signature
     |  
     |  __ne__(...)
     |      x.__ne__(y) <==> x!=y
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  Abkhazian = 2
     |  
     |  Afan = 3
     |  
     |  Afar = 4
     |  
     |  Afghanistan = 1
     |  
     |  Afrikaans = 5
     |  
     |  Aghem = 237
     |  
     |  Akan = 146
     |  
     |  Akkadian = 262
     |  
     |  Akoose = 312
     |  
     |  AlandIslands = 248
     |  
     |  Albania = 2
     |  
     |  Albanian = 6
     |  
     |  Algeria = 3
     |  
     |  AlternateQuotation = 1
     |  
     |  AmericanSamoa = 4
     |  
     |  Amharic = 7
     |  
     |  AncientEgyptian = 263
     |  
     |  AncientGreek = 264
     |  
     |  AncientNorthArabian = 331
     |  
     |  Andorra = 5
     |  
     |  Angola = 6
     |  
     |  Anguilla = 7
     |  
     |  Antarctica = 8
     |  
     |  AntiguaAndBarbuda = 9
     |  
     |  AnyCountry = 0
     |  
     |  AnyLanguage = 0
     |  
     |  AnyScript = 0
     |  
     |  Arabic = 8
     |  
     |  ArabicScript = 1
     |  
     |  Aragonese = 261
     |  
     |  Aramaic = 265
     |  
     |  Argentina = 10
     |  
     |  Armenia = 11
     |  
     |  Armenian = 9
     |  
     |  ArmenianScript = 10
     |  
     |  Aruba = 12
     |  
     |  AscensionIsland = 247
     |  
     |  Assamese = 10
     |  
     |  Asturian = 256
     |  
     |  Asu = 205
     |  
     |  Atsam = 156
     |  
     |  Australia = 13
     |  
     |  Austria = 14
     |  
     |  Avaric = 216
     |  
     |  Avestan = 255
     |  
     |  AvestanScript = 36
     |  
     |  Aymara = 11
     |  
     |  Azerbaijan = 15
     |  
     |  Azerbaijani = 12
     |  
     |  Bafia = 243
     |  
     |  Bahamas = 16
     |  
     |  Bahrain = 17
     |  
     |  Balinese = 266
     |  
     |  BalineseScript = 37
     |  
     |  Bambara = 188
     |  
     |  BamumScript = 38
     |  
     |  Bamun = 267
     |  
     |  Bangladesh = 18
     |  
     |  Barbados = 19
     |  
     |  Basaa = 238
     |  
     |  Bashkir = 13
     |  
     |  Basque = 14
     |  
     |  Bassa = 336
     |  
     |  BassaVahScript = 106
     |  
     |  BatakScript = 39
     |  
     |  BatakToba = 268
     |  
     |  Belarus = 20
     |  
     |  Belarusian = 22
     |  
     |  Belgium = 21
     |  
     |  Belize = 22
     |  
     |  Bemba = 195
     |  
     |  Bena = 186
     |  
     |  Bengali = 15
     |  
     |  BengaliScript = 11
     |  
     |  Benin = 23
     |  
     |  Bermuda = 24
     |  
     |  Bhutan = 25
     |  
     |  Bhutani = 16
     |  
     |  Bihari = 17
     |  
     |  Bislama = 18
     |  
     |  Blin = 152
     |  
     |  Bodo = 215
     |  
     |  Bolivia = 26
     |  
     |  Bonaire = 255
     |  
     |  BopomofoScript = 40
     |  
     |  BosniaAndHerzegowina = 27
     |  
     |  Bosnian = 142
     |  
     |  Botswana = 28
     |  
     |  BouvetIsland = 29
     |  
     |  BrahmiScript = 41
     |  
     |  BrailleScript = 103
     |  
     |  Brazil = 30
     |  
     |  Breton = 19
     |  
     |  BritishIndianOceanTerritory = 31
     |  
     |  BritishVirginIslands = 233
     |  
     |  Brunei = 32
     |  
     |  Buginese = 269
     |  
     |  BugineseScript = 42
     |  
     |  Buhid = 270
     |  
     |  BuhidScript = 43
     |  
     |  Bulgaria = 33
     |  
     |  Bulgarian = 20
     |  
     |  BurkinaFaso = 34
     |  
     |  Burmese = 21
     |  
     |  Burundi = 35
     |  
     |  Byelorussian = 22
     |  
     |  C = 1
     |  
     |  Cambodia = 36
     |  
     |  Cambodian = 23
     |  
     |  Cameroon = 37
     |  
     |  Canada = 38
     |  
     |  CanadianAboriginalScript = 44
     |  
     |  CanaryIslands = 238
     |  
     |  CapeVerde = 39
     |  
     |  Carian = 271
     |  
     |  CarianScript = 45
     |  
     |  Catalan = 24
     |  
     |  CaucasianAlbanianScript = 105
     |  
     |  CaymanIslands = 40
     |  
     |  CentralAfricanRepublic = 41
     |  
     |  CentralKurdish = 316
     |  
     |  CentralMoroccoTamazight = 212
     |  
     |  CeutaAndMelilla = 250
     |  
     |  Chad = 42
     |  
     |  Chakma = 272
     |  
     |  ChakmaScript = 46
     |  
     |  ChamScript = 47
     |  
     |  Chamorro = 217
     |  
     |  Chechen = 218
     |  
     |  Cherokee = 190
     |  
     |  CherokeeScript = 12
     |  
     |  Chewa = 165
     |  
     |  Chiga = 211
     |  
     |  Chile = 43
     |  
     |  China = 44
     |  
     |  Chinese = 25
     |  
     |  ChristmasIsland = 45
     |  
     |  Church = 219
     |  
     |  Chuvash = 220
     |  
     |  ClassicalMandaic = 273
     |  
     |  ClippertonIsland = 241
     |  
     |  CocosIslands = 46
     |  
     |  Colognian = 201
     |  
     |  Colombia = 47
     |  
     |  Comoros = 48
     |  
     |  CongoBrazzaville = 50
     |  
     |  CongoKinshasa = 49
     |  
     |  CongoSwahili = 250
     |  
     |  CookIslands = 51
     |  
     |  Coptic = 274
     |  
     |  CopticScript = 48
     |  
     |  Cornish = 145
     |  
     |  Corsican = 26
     |  
     |  CostaRica = 52
     |  
     |  Country = <class 'PythonQt.QtCore.Country'>
     |  
     |  
     |  Cree = 221
     |  
     |  Croatia = 54
     |  
     |  Croatian = 27
     |  
     |  Cuba = 55
     |  
     |  CuneiformScript = 94
     |  
     |  CuraSao = 152
     |  
     |  CurrencyDisplayName = 2
     |  
     |  CurrencyIsoCode = 0
     |  
     |  CurrencySymbol = 1
     |  
     |  CurrencySymbolFormat = <class 'PythonQt.QtCore.CurrencySymbolFormat'>
     |  
     |  
     |  CypriotScript = 49
     |  
     |  Cyprus = 56
     |  
     |  CyrillicScript = 2
     |  
     |  Czech = 28
     |  
     |  CzechRepublic = 57
     |  
     |  Danish = 29
     |  
     |  DemocraticRepublicOfCongo = 49
     |  
     |  DemocraticRepublicOfKorea = 113
     |  
     |  Denmark = 58
     |  
     |  DeseretScript = 3
     |  
     |  DevanagariScript = 13
     |  
     |  DiegoGarcia = 249
     |  
     |  Divehi = 143
     |  
     |  Djibouti = 59
     |  
     |  Dogri = 275
     |  
     |  Dominica = 60
     |  
     |  DominicanRepublic = 61
     |  
     |  Duala = 240
     |  
     |  DuployanScript = 107
     |  
     |  Dutch = 30
     |  
     |  Dzongkha = 16
     |  
     |  EastTimor = 62
     |  
     |  EasternCham = 276
     |  
     |  EasternKayah = 277
     |  
     |  Ecuador = 63
     |  
     |  Egypt = 64
     |  
     |  EgyptianHieroglyphsScript = 50
     |  
     |  ElSalvador = 65
     |  
     |  ElbasanScript = 108
     |  
     |  Embu = 189
     |  
     |  English = 31
     |  
     |  EquatorialGuinea = 66
     |  
     |  Eritrea = 67
     |  
     |  Esperanto = 32
     |  
     |  Estonia = 68
     |  
     |  Estonian = 33
     |  
     |  Ethiopia = 69
     |  
     |  EthiopicScript = 14
     |  
     |  Etruscan = 278
     |  
     |  Ewe = 161
     |  
     |  Ewondo = 242
     |  
     |  FalklandIslands = 70
     |  
     |  FaroeIslands = 71
     |  
     |  Faroese = 34
     |  
     |  Fiji = 72
     |  
     |  Fijian = 35
     |  
     |  Filipino = 166
     |  
     |  Finland = 73
     |  
     |  Finnish = 36
     |  
     |  FormatType = <class 'PythonQt.QtCore.FormatType'>
     |  
     |  
     |  France = 74
     |  
     |  FraserScript = 51
     |  
     |  French = 37
     |  
     |  FrenchGuiana = 76
     |  
     |  FrenchPolynesia = 77
     |  
     |  FrenchSouthernTerritories = 78
     |  
     |  Frisian = 38
     |  
     |  Friulian = 159
     |  
     |  Fulah = 177
     |  
     |  Ga = 148
     |  
     |  Gabon = 79
     |  
     |  Gaelic = 39
     |  
     |  Galician = 40
     |  
     |  Gambia = 80
     |  
     |  Ganda = 194
     |  
     |  Geez = 153
     |  
     |  Georgia = 81
     |  
     |  Georgian = 41
     |  
     |  GeorgianScript = 15
     |  
     |  German = 42
     |  
     |  Germany = 82
     |  
     |  Ghana = 83
     |  
     |  Gibraltar = 84
     |  
     |  GlagoliticScript = 52
     |  
     |  Gothic = 279
     |  
     |  GothicScript = 53
     |  
     |  GranthaScript = 109
     |  
     |  Greece = 85
     |  
     |  Greek = 43
     |  
     |  GreekScript = 16
     |  
     |  Greenland = 86
     |  
     |  Greenlandic = 44
     |  
     |  Grenada = 87
     |  
     |  Guadeloupe = 88
     |  
     |  Guam = 89
     |  
     |  Guarani = 45
     |  
     |  Guatemala = 90
     |  
     |  Guernsey = 75
     |  
     |  Guinea = 91
     |  
     |  GuineaBissau = 92
     |  
     |  Gujarati = 46
     |  
     |  GujaratiScript = 17
     |  
     |  GurmukhiScript = 4
     |  
     |  Gusii = 175
     |  
     |  Guyana = 93
     |  
     |  Haiti = 94
     |  
     |  Haitian = 222
     |  
     |  HanScript = 54
     |  
     |  HangulScript = 55
     |  
     |  Hanunoo = 280
     |  
     |  HanunooScript = 56
     |  
     |  Hausa = 47
     |  
     |  Hawaiian = 163
     |  
     |  HeardAndMcDonaldIslands = 95
     |  
     |  Hebrew = 48
     |  
     |  HebrewScript = 18
     |  
     |  Herero = 223
     |  
     |  Hindi = 49
     |  
     |  HiraganaScript = 104
     |  
     |  HiriMotu = 224
     |  
     |  HmongNjua = 333
     |  
     |  Ho = 334
     |  
     |  Honduras = 96
     |  
     |  HongKong = 97
     |  
     |  Hungarian = 50
     |  
     |  Hungary = 98
     |  
     |  Iceland = 99
     |  
     |  Icelandic = 51
     |  
     |  Igbo = 149
     |  
     |  ImperialAramaicScript = 57
     |  
     |  ImperialSystem = 1
     |  
     |  ImperialUKSystem = 2
     |  
     |  ImperialUSSystem = 1
     |  
     |  InariSami = 326
     |  
     |  India = 100
     |  
     |  Indonesia = 101
     |  
     |  Indonesian = 52
     |  
     |  Ingush = 281
     |  
     |  InscriptionalPahlaviScript = 58
     |  
     |  InscriptionalParthianScript = 59
     |  
     |  Interlingua = 53
     |  
     |  Interlingue = 54
     |  
     |  Inuktitut = 55
     |  
     |  Inupiak = 56
     |  
     |  Iran = 102
     |  
     |  Iraq = 103
     |  
     |  Ireland = 104
     |  
     |  Irish = 57
     |  
     |  IsleOfMan = 251
     |  
     |  Israel = 105
     |  
     |  Italian = 58
     |  
     |  Italy = 106
     |  
     |  IvoryCoast = 53
     |  
     |  Jamaica = 107
     |  
     |  Japan = 108
     |  
     |  Japanese = 59
     |  
     |  JapaneseScript = 19
     |  
     |  Javanese = 60
     |  
     |  JavaneseScript = 60
     |  
     |  Jersey = 252
     |  
     |  Jju = 158
     |  
     |  JolaFonyi = 241
     |  
     |  Jordan = 109
     |  
     |  Kabuverdianu = 196
     |  
     |  Kabyle = 184
     |  
     |  KaithiScript = 61
     |  
     |  Kako = 258
     |  
     |  Kalenjin = 198
     |  
     |  Kamba = 150
     |  
     |  Kannada = 61
     |  
     |  KannadaScript = 21
     |  
     |  Kanuri = 225
     |  
     |  Kashmiri = 62
     |  
     |  KatakanaScript = 62
     |  
     |  KayahLiScript = 63
     |  
     |  Kazakh = 63
     |  
     |  Kazakhstan = 110
     |  
     |  Kenya = 111
     |  
     |  Kenyang = 319
     |  
     |  KharoshthiScript = 64
     |  
     |  Khmer = 23
     |  
     |  KhmerScript = 20
     |  
     |  KhojkiScript = 111
     |  
     |  KhudawadiScript = 125
     |  
     |  Kiche = 323
     |  
     |  Kikuyu = 178
     |  
     |  Kinyarwanda = 64
     |  
     |  Kirghiz = 65
     |  
     |  Kiribati = 112
     |  
     |  Komi = 226
     |  
     |  Kongo = 227
     |  
     |  Konkani = 147
     |  
     |  Korean = 66
     |  
     |  KoreanScript = 22
     |  
     |  Koro = 154
     |  
     |  Kosovo = 257
     |  
     |  KoyraChiini = 208
     |  
     |  KoyraboroSenni = 213
     |  
     |  Kpelle = 169
     |  
     |  Kurdish = 67
     |  
     |  Kurundi = 68
     |  
     |  Kuwait = 115
     |  
     |  Kwanyama = 228
     |  
     |  Kwasio = 246
     |  
     |  Kyrgyzstan = 116
     |  
     |  Lakota = 313
     |  
     |  Langi = 193
     |  
     |  Language = <class 'PythonQt.QtCore.Language'>
     |  
     |  
     |  LannaScript = 65
     |  
     |  Lao = 69
     |  
     |  LaoScript = 23
     |  
     |  Laos = 117
     |  
     |  LargeFloweryMiao = 282
     |  
     |  LastCountry = 259
     |  
     |  LastLanguage = 359
     |  
     |  LastScript = 141
     |  
     |  Latin = 70
     |  
     |  LatinAmericaAndTheCaribbean = 246
     |  
     |  LatinScript = 7
     |  
     |  Latvia = 118
     |  
     |  Latvian = 71
     |  
     |  Lebanon = 119
     |  
     |  Lepcha = 283
     |  
     |  LepchaScript = 66
     |  
     |  Lesotho = 120
     |  
     |  Lezghian = 335
     |  
     |  Liberia = 121
     |  
     |  Libya = 122
     |  
     |  Liechtenstein = 123
     |  
     |  Limbu = 284
     |  
     |  LimbuScript = 67
     |  
     |  Limburgish = 229
     |  
     |  LinearA = 332
     |  
     |  LinearAScript = 112
     |  
     |  LinearBScript = 68
     |  
     |  Lingala = 72
     |  
     |  Lisu = 285
     |  
     |  Lithuania = 124
     |  
     |  Lithuanian = 73
     |  
     |  LongFormat = 0
     |  
     |  LowGerman = 170
     |  
     |  LowerSorbian = 317
     |  
     |  Lu = 286
     |  
     |  LubaKatanga = 230
     |  
     |  LuleSami = 325
     |  
     |  Luo = 210
     |  
     |  Luxembourg = 125
     |  
     |  Luxembourgish = 231
     |  
     |  Luyia = 204
     |  
     |  Lycian = 287
     |  
     |  LycianScript = 69
     |  
     |  Lydian = 288
     |  
     |  LydianScript = 70
     |  
     |  Macau = 126
     |  
     |  Macedonia = 127
     |  
     |  Macedonian = 74
     |  
     |  Machame = 200
     |  
     |  Madagascar = 128
     |  
     |  MahajaniScript = 113
     |  
     |  Maithili = 339
     |  
     |  MakhuwaMeetto = 244
     |  
     |  Makonde = 192
     |  
     |  Malagasy = 75
     |  
     |  Malawi = 129
     |  
     |  Malay = 76
     |  
     |  Malayalam = 77
     |  
     |  MalayalamScript = 24
     |  
     |  Malaysia = 130
     |  
     |  Maldives = 131
     |  
     |  Mali = 132
     |  
     |  Malta = 133
     |  
     |  Maltese = 78
     |  
     |  MandaeanScript = 71
     |  
     |  Mandingo = 289
     |  
     |  ManichaeanMiddlePersian = 329
     |  
     |  ManichaeanScript = 114
     |  
     |  Manipuri = 290
     |  
     |  Manx = 144
     |  
     |  Maori = 79
     |  
     |  Mapuche = 315
     |  
     |  Marathi = 80
     |  
     |  MarshallIslands = 134
     |  
     |  Marshallese = 81
     |  
     |  Martinique = 135
     |  
     |  Masai = 202
     |  
     |  Mauritania = 136
     |  
     |  Mauritius = 137
     |  
     |  Mayotte = 138
     |  
     |  MeasurementSystem = <class 'PythonQt.QtCore.MeasurementSystem'>
     |  
     |  
     |  MeiteiMayekScript = 72
     |  
     |  Mende = 330
     |  
     |  MendeKikakuiScript = 115
     |  
     |  Meroitic = 291
     |  
     |  MeroiticCursiveScript = 74
     |  
     |  MeroiticScript = 73
     |  
     |  Meru = 197
     |  
     |  Meta = 259
     |  
     |  MetricSystem = 0
     |  
     |  Mexico = 139
     |  
     |  Micronesia = 140
     |  
     |  ModiScript = 116
     |  
     |  Mohawk = 320
     |  
     |  Moldavian = 95
     |  
     |  Moldova = 141
     |  
     |  Monaco = 142
     |  
     |  Mongolia = 143
     |  
     |  Mongolian = 82
     |  
     |  MongolianScript = 8
     |  
     |  Mono = 337
     |  
     |  Montenegro = 242
     |  
     |  Montserrat = 144
     |  
     |  Morisyen = 191
     |  
     |  Morocco = 145
     |  
     |  Mozambique = 146
     |  
     |  MroScript = 117
     |  
     |  Mundang = 245
     |  
     |  Myanmar = 147
     |  
     |  MyanmarScript = 25
     |  
     |  NabataeanScript = 119
     |  
     |  Nama = 199
     |  
     |  Namibia = 148
     |  
     |  NarrowFormat = 2
     |  
     |  NauruCountry = 149
     |  
     |  NauruLanguage = 83
     |  
     |  Navaho = 232
     |  
     |  Ndonga = 233
     |  
     |  Nepal = 150
     |  
     |  Nepali = 84
     |  
     |  Netherlands = 151
     |  
     |  NewCaledonia = 153
     |  
     |  NewTaiLueScript = 76
     |  
     |  NewZealand = 154
     |  
     |  Ngiemboon = 260
     |  
     |  Ngomba = 257
     |  
     |  Nicaragua = 155
     |  
     |  Niger = 156
     |  
     |  Nigeria = 157
     |  
     |  Niue = 158
     |  
     |  Nko = 321
     |  
     |  NkoScript = 75
     |  
     |  NorfolkIsland = 159
     |  
     |  NorthKorea = 113
     |  
     |  NorthNdebele = 181
     |  
     |  NorthernMarianaIslands = 160
     |  
     |  NorthernSami = 173
     |  
     |  NorthernSotho = 172
     |  
     |  NorthernThai = 292
     |  
     |  Norway = 161
     |  
     |  Norwegian = 85
     |  
     |  NorwegianBokmal = 85
     |  
     |  NorwegianNynorsk = 141
     |  
     |  Nuer = 247
     |  
     |  NumberOption = <class 'PythonQt.QtCore.NumberOption'>
     |  
     |  
     |  NumberOptions = <class 'PythonQt.QtCore.NumberOptions'>
     |  
     |  
     |  Nyanja = 165
     |  
     |  Nyankole = 185
     |  
     |  Occitan = 86
     |  
     |  OghamScript = 77
     |  
     |  Ojibwa = 234
     |  
     |  OlChikiScript = 78
     |  
     |  OldIrish = 293
     |  
     |  OldItalicScript = 79
     |  
     |  OldNorse = 294
     |  
     |  OldNorthArabianScript = 118
     |  
     |  OldPermicScript = 122
     |  
     |  OldPersian = 295
     |  
     |  OldPersianScript = 80
     |  
     |  OldSouthArabianScript = 81
     |  
     |  OldTurkish = 296
     |  
     |  Oman = 162
     |  
     |  OmitGroupSeparator = 1
     |  
     |  Oriya = 87
     |  
     |  OriyaScript = 26
     |  
     |  OrkhonScript = 82
     |  
     |  Oromo = 3
     |  
     |  OsmanyaScript = 83
     |  
     |  Ossetic = 101
     |  
     |  PahawhHmongScript = 110
     |  
     |  Pahlavi = 297
     |  
     |  Pakistan = 163
     |  
     |  Palau = 164
     |  
     |  PalestinianTerritories = 165
     |  
     |  Pali = 235
     |  
     |  PalmyreneScript = 120
     |  
     |  Panama = 166
     |  
     |  PapuaNewGuinea = 167
     |  
     |  Paraguay = 168
     |  
     |  Parthian = 298
     |  
     |  Pashto = 88
     |  
     |  PauCinHauScript = 121
     |  
     |  PeoplesRepublicOfCongo = 50
     |  
     |  Persian = 89
     |  
     |  Peru = 169
     |  
     |  PhagsPaScript = 84
     |  
     |  Philippines = 170
     |  
     |  Phoenician = 299
     |  
     |  PhoenicianScript = 85
     |  
     |  Pitcairn = 171
     |  
     |  Poland = 172
     |  
     |  Polish = 90
     |  
     |  PollardPhoneticScript = 86
     |  
     |  Portugal = 173
     |  
     |  Portuguese = 91
     |  
     |  PrakritLanguage = 300
     |  
     |  Prussian = 322
     |  
     |  PsalterPahlaviScript = 123
     |  
     |  PuertoRico = 174
     |  
     |  Punjabi = 92
     |  
     |  Qatar = 175
     |  
     |  Quechua = 93
     |  
     |  QuotationStyle = <class 'PythonQt.QtCore.QuotationStyle'>
     |  
     |  
     |  Rejang = 301
     |  
     |  RejangScript = 87
     |  
     |  RejectGroupSeparator = 2
     |  
     |  RepublicOfKorea = 114
     |  
     |  Reunion = 176
     |  
     |  RhaetoRomance = 94
     |  
     |  Romania = 177
     |  
     |  Romanian = 95
     |  
     |  Romansh = 94
     |  
     |  Rombo = 182
     |  
     |  Rundi = 68
     |  
     |  RunicScript = 88
     |  
     |  Russia = 178
     |  
     |  Russian = 96
     |  
     |  RussianFederation = 178
     |  
     |  Rwa = 209
     |  
     |  Rwanda = 179
     |  
     |  Sabaean = 302
     |  
     |  Saho = 207
     |  
     |  SaintBarthelemy = 244
     |  
     |  SaintHelena = 199
     |  
     |  SaintKittsAndNevis = 180
     |  
     |  SaintLucia = 181
     |  
     |  SaintMartin = 245
     |  
     |  SaintPierreAndMiquelon = 200
     |  
     |  SaintVincentAndTheGrenadines = 182
     |  
     |  Sakha = 248
     |  
     |  Samaritan = 303
     |  
     |  SamaritanScript = 89
     |  
     |  Samburu = 179
     |  
     |  Samoa = 183
     |  
     |  Samoan = 97
     |  
     |  SanMarino = 184
     |  
     |  Sango = 98
     |  
     |  Sangu = 249
     |  
     |  Sanskrit = 99
     |  
     |  Santali = 304
     |  
     |  SaoTomeAndPrincipe = 185
     |  
     |  Sardinian = 115
     |  
     |  SaudiArabia = 186
     |  
     |  Saurashtra = 305
     |  
     |  SaurashtraScript = 90
     |  
     |  Script = <class 'PythonQt.QtCore.Script'>
     |  
     |  
     |  Sena = 180
     |  
     |  Senegal = 187
     |  
     |  Serbia = 243
     |  
     |  Serbian = 100
     |  
     |  SerboCroatian = 100
     |  
     |  Seychelles = 188
     |  
     |  Shambala = 214
     |  
     |  SharadaScript = 91
     |  
     |  ShavianScript = 92
     |  
     |  Shona = 104
     |  
     |  ShortFormat = 1
     |  
     |  SichuanYi = 168
     |  
     |  Sidamo = 155
     |  
     |  SiddhamScript = 124
     |  
     |  SierraLeone = 189
     |  
     |  SimplifiedChineseScript = 5
     |  
     |  SimplifiedHanScript = 5
     |  
     |  Sindhi = 105
     |  
     |  Singapore = 190
     |  
     |  Sinhala = 106
     |  
     |  SinhalaScript = 32
     |  
     |  SintMaarten = 256
     |  
     |  SkoltSami = 327
     |  
     |  Slovak = 108
     |  
     |  Slovakia = 191
     |  
     |  Slovenia = 192
     |  
     |  Slovenian = 109
     |  
     |  Soga = 203
     |  
     |  SolomonIslands = 193
     |  
     |  Somali = 110
     |  
     |  Somalia = 194
     |  
     |  Sora = 306
     |  
     |  SoraSompengScript = 93
     |  
     |  SouthAfrica = 195
     |  
     |  SouthGeorgiaAndTheSouthSandwichIslands = 196
     |  
     |  SouthKorea = 114
     |  
     |  SouthNdebele = 171
     |  
     |  SouthSudan = 254
     |  
     |  SouthernSami = 324
     |  
     |  SouthernSotho = 102
     |  
     |  Spain = 197
     |  
     |  Spanish = 111
     |  
     |  SriLanka = 198
     |  
     |  StandardMoroccanTamazight = 314
     |  
     |  StandardQuotation = 0
     |  
     |  Sudan = 201
     |  
     |  Sundanese = 112
     |  
     |  SundaneseScript = 95
     |  
     |  Suriname = 202
     |  
     |  SvalbardAndJanMayenIslands = 203
     |  
     |  Swahili = 113
     |  
     |  Swati = 107
     |  
     |  Swaziland = 204
     |  
     |  Sweden = 205
     |  
     |  Swedish = 114
     |  
     |  SwissGerman = 167
     |  
     |  Switzerland = 206
     |  
     |  Sylheti = 307
     |  
     |  SylotiNagriScript = 96
     |  
     |  Syria = 207
     |  
     |  Syriac = 151
     |  
     |  SyriacScript = 33
     |  
     |  SyrianArabRepublic = 207
     |  
     |  Tachelhit = 183
     |  
     |  Tagalog = 166
     |  
     |  TagalogScript = 97
     |  
     |  Tagbanwa = 308
     |  
     |  TagbanwaScript = 98
     |  
     |  Tahitian = 127
     |  
     |  TaiDam = 309
     |  
     |  TaiLeScript = 99
     |  
     |  TaiNua = 310
     |  
     |  TaiVietScript = 100
     |  
     |  Taita = 176
     |  
     |  Taiwan = 208
     |  
     |  Tajik = 116
     |  
     |  Tajikistan = 209
     |  
     |  TakriScript = 101
     |  
     |  Tamil = 117
     |  
     |  TamilScript = 27
     |  
     |  Tanzania = 210
     |  
     |  Taroko = 174
     |  
     |  Tasawaq = 251
     |  
     |  Tatar = 118
     |  
     |  TedimChin = 338
     |  
     |  Telugu = 119
     |  
     |  TeluguScript = 28
     |  
     |  Teso = 206
     |  
     |  ThaanaScript = 29
     |  
     |  Thai = 120
     |  
     |  ThaiScript = 30
     |  
     |  Thailand = 211
     |  
     |  Tibetan = 121
     |  
     |  TibetanScript = 31
     |  
     |  TifinaghScript = 9
     |  
     |  Tigre = 157
     |  
     |  Tigrinya = 122
     |  
     |  TirhutaScript = 126
     |  
     |  Togo = 212
     |  
     |  Tokelau = 213
     |  
     |  Tonga = 214
     |  
     |  Tongan = 123
     |  
     |  TraditionalChineseScript = 6
     |  
     |  TraditionalHanScript = 6
     |  
     |  TrinidadAndTobago = 215
     |  
     |  TristanDaCunha = 253
     |  
     |  Tsonga = 124
     |  
     |  Tswana = 103
     |  
     |  Tunisia = 216
     |  
     |  Turkey = 217
     |  
     |  Turkish = 125
     |  
     |  Turkmen = 126
     |  
     |  Turkmenistan = 218
     |  
     |  TurksAndCaicosIslands = 219
     |  
     |  Tuvalu = 220
     |  
     |  Twi = 146
     |  
     |  Tyap = 164
     |  
     |  Uganda = 221
     |  
     |  Ugaritic = 311
     |  
     |  UgariticScript = 102
     |  
     |  Uighur = 128
     |  
     |  Uigur = 128
     |  
     |  Ukraine = 222
     |  
     |  Ukrainian = 129
     |  
     |  UnitedArabEmirates = 223
     |  
     |  UnitedKingdom = 224
     |  
     |  UnitedStates = 225
     |  
     |  UnitedStatesMinorOutlyingIslands = 226
     |  
     |  UnitedStatesVirginIslands = 234
     |  
     |  UpperSorbian = 318
     |  
     |  Urdu = 130
     |  
     |  Uruguay = 227
     |  
     |  Uzbek = 131
     |  
     |  Uzbekistan = 228
     |  
     |  Vai = 252
     |  
     |  VaiScript = 35
     |  
     |  Vanuatu = 229
     |  
     |  VarangKshitiScript = 127
     |  
     |  VaticanCityState = 230
     |  
     |  Venda = 160
     |  
     |  Venezuela = 231
     |  
     |  Vietnam = 232
     |  
     |  Vietnamese = 132
     |  
     |  Volapuk = 133
     |  
     |  Vunjo = 187
     |  
     |  Walamo = 162
     |  
     |  WallisAndFutunaIslands = 235
     |  
     |  Walloon = 236
     |  
     |  Walser = 253
     |  
     |  Warlpiri = 328
     |  
     |  Welsh = 134
     |  
     |  WesternFrisian = 38
     |  
     |  WesternSahara = 236
     |  
     |  Wolof = 135
     |  
     |  Xhosa = 136
     |  
     |  Yangben = 254
     |  
     |  Yemen = 237
     |  
     |  YiScript = 34
     |  
     |  Yiddish = 137
     |  
     |  Yoruba = 138
     |  
     |  Zambia = 239
     |  
     |  Zarma = 239
     |  
     |  Zhuang = 139
     |  
     |  Zimbabwe = 240
     |  
     |  Zulu = 140
     |  
     |  amText = <unbound qt slot amText of QLocale type>
     |      X.amText(a) -> str
     |  
     |  bcp47Name = <unbound qt slot bcp47Name of QLocale type>
     |      X.bcp47Name(a) -> str
     |  
     |  c = <unbound qt slot static_QLocale_c of QLocale type>
     |      X.c() -> PythonQt.QtCore.QLocale
     |  
     |  className = <built-in method className of PythonQt.PythonQtClassWrappe...
     |      Return the classname of the object
     |  
     |  countriesForLanguage = <unbound qt slot static_QLocale_countriesForLan...
     |      X.countriesForLanguage(a) -> tuple
     |  
     |  country = <unbound qt slot country of QLocale type>
     |      X.country(a)
     |  
     |  countryToString = <unbound qt slot static_QLocale_countryToString of Q...
     |      X.countryToString(a) -> str
     |  
     |  createSeparatedList = <unbound qt slot createSeparatedList of QLocale ...
     |      X.createSeparatedList(a, b) -> str
     |  
     |  currencySymbol = <unbound qt slot currencySymbol of QLocale type>
     |      X.currencySymbol(a, b) -> str
     |  
     |  dateFormat = <unbound qt slot dateFormat of QLocale type>
     |      X.dateFormat(a, b) -> str
     |  
     |  dateTimeFormat = <unbound qt slot dateTimeFormat of QLocale type>
     |      X.dateTimeFormat(a, b) -> str
     |  
     |  dayName = <unbound qt slot dayName of QLocale type>
     |      X.dayName(a, b, c) -> str
     |  
     |  decimalPoint = <unbound qt slot decimalPoint of QLocale type>
     |      X.decimalPoint(a)
     |  
     |  delete = <built-in method delete of PythonQt.PythonQtClassWrapper obje...
     |      Deletes the given C++ object
     |  
     |  exponential = <unbound qt slot exponential of QLocale type>
     |      X.exponential(a)
     |  
     |  firstDayOfWeek = <unbound qt slot firstDayOfWeek of QLocale type>
     |      X.firstDayOfWeek(a)
     |  
     |  groupSeparator = <unbound qt slot groupSeparator of QLocale type>
     |      X.groupSeparator(a)
     |  
     |  help = <built-in method help of PythonQt.PythonQtClassWrapper object>
     |      Shows the help of available methods for this class
     |  
     |  inherits = <built-in method inherits of PythonQt.PythonQtClassWrapper ...
     |      Returns if the class inherits or is of given type name
     |  
     |  language = <unbound qt slot language of QLocale type>
     |      X.language(a)
     |  
     |  languageToString = <unbound qt slot static_QLocale_languageToString of...
     |      X.languageToString(a) -> str
     |  
     |  matchingLocales = <unbound qt slot static_QLocale_matchingLocales of Q...
     |      X.matchingLocales(a, b, c) -> tuple
     |  
     |  measurementSystem = <unbound qt slot measurementSystem of QLocale type...
     |      X.measurementSystem(a)
     |  
     |  monthName = <unbound qt slot monthName of QLocale type>
     |      X.monthName(a, b, c) -> str
     |  
     |  name = <unbound qt slot name of QLocale type>
     |      X.name(a) -> str
     |  
     |  nativeCountryName = <unbound qt slot nativeCountryName of QLocale type...
     |      X.nativeCountryName(a) -> str
     |  
     |  nativeLanguageName = <unbound qt slot nativeLanguageName of QLocale ty...
     |      X.nativeLanguageName(a) -> str
     |  
     |  negativeSign = <unbound qt slot negativeSign of QLocale type>
     |      X.negativeSign(a)
     |  
     |  numberOptions = <unbound qt slot numberOptions of QLocale type>
     |      X.numberOptions(a)
     |  
     |  percent = <unbound qt slot percent of QLocale type>
     |      X.percent(a)
     |  
     |  pmText = <unbound qt slot pmText of QLocale type>
     |      X.pmText(a) -> str
     |  
     |  positiveSign = <unbound qt slot positiveSign of QLocale type>
     |      X.positiveSign(a)
     |  
     |  quoteString = <unbound qt slot quoteString of QLocale type>
     |      X.quoteString(a, b, c) -> str
     |  
     |  readFrom = <unbound qt slot readFrom of QLocale type>
     |      X.readFrom(a, b)
     |  
     |  script = <unbound qt slot script of QLocale type>
     |      X.script(a)
     |  
     |  scriptToString = <unbound qt slot static_QLocale_scriptToString of QLo...
     |      X.scriptToString(a) -> str
     |  
     |  setDefault = <unbound qt slot static_QLocale_setDefault of QLocale typ...
     |      X.setDefault(a)
     |  
     |  setNumberOptions = <unbound qt slot setNumberOptions of QLocale type>
     |      X.setNumberOptions(a, b)
     |  
     |  standaloneDayName = <unbound qt slot standaloneDayName of QLocale type...
     |      X.standaloneDayName(a, b, c) -> str
     |  
     |  standaloneMonthName = <unbound qt slot standaloneMonthName of QLocale ...
     |      X.standaloneMonthName(a, b, c) -> str
     |  
     |  system = <unbound qt slot static_QLocale_system of QLocale type>
     |      X.system() -> PythonQt.QtCore.QLocale
     |  
     |  textDirection = <unbound qt slot textDirection of QLocale type>
     |      X.textDirection(a)
     |  
     |  timeFormat = <unbound qt slot timeFormat of QLocale type>
     |      X.timeFormat(a, b) -> str
     |  
     |  toCurrencyString = <unbound qt slot toCurrencyString of QLocale type>
     |      X.toCurrencyString(a, b, c) -> str
     |  
     |  toDate = <unbound qt slot toDate of QLocale type>
     |      X.toDate(a, b, c) -> PythonQt.QtCore.QDate
     |  
     |  toDateTime = <unbound qt slot toDateTime of QLocale type>
     |      X.toDateTime(a, b, c) -> PythonQt.QtCore.QDateTime
     |  
     |  toDouble = <unbound qt slot toDouble of QLocale type>
     |      X.toDouble(a, b, c) -> float
     |  
     |  toFloat = <unbound qt slot toFloat of QLocale type>
     |      X.toFloat(a, b, c) -> float
     |  
     |  toInt = <unbound qt slot toInt of QLocale type>
     |      X.toInt(a, b, c) -> int
     |  
     |  toLongLong = <unbound qt slot toLongLong of QLocale type>
     |      X.toLongLong(a, b, c) -> int
     |  
     |  toLower = <unbound qt slot toLower of QLocale type>
     |      X.toLower(a, b) -> str
     |  
     |  toShort = <unbound qt slot toShort of QLocale type>
     |      X.toShort(a, b, c) -> int
     |  
     |  toString = <unbound qt slot toString of QLocale type>
     |      X.toString(a, b, c, d) -> str
     |  
     |  toTime = <unbound qt slot toTime of QLocale type>
     |      X.toTime(a, b, c) -> PythonQt.QtCore.QTime
     |  
     |  toUInt = <unbound qt slot toUInt of QLocale type>
     |      X.toUInt(a, b, c) -> int
     |  
     |  toULongLong = <unbound qt slot toULongLong of QLocale type>
     |      X.toULongLong(a, b, c) -> int
     |  
     |  toUShort = <unbound qt slot toUShort of QLocale type>
     |      X.toUShort(a, b, c) -> int
     |  
     |  toUpper = <unbound qt slot toUpper of QLocale type>
     |      X.toUpper(a, b) -> str
     |  
     |  uiLanguages = <unbound qt slot uiLanguages of QLocale type>
     |      X.uiLanguages(a) -> tuple
     |  
     |  weekdays = <unbound qt slot weekdays of QLocale type>
     |      X.weekdays(a) -> tuple
     |  
     |  writeTo = <unbound qt slot writeTo of QLocale type>
     |      X.writeTo(a, b)
     |  
     |  zeroDigit = <unbound qt slot zeroDigit of QLocale type>
     |      X.zeroDigit(a)
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __delattr__(...)
     |      x.__delattr__('name') <==> del x.name
     |  
     |  __ge__(...)
     |      x.__ge__(y) <==> x>=y
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __gt__(...)
     |      x.__gt__(y) <==> x>y
     |  
     |  __hash__(...)
     |      x.__hash__() <==> hash(x)
     |  
     |  __le__(...)
     |      x.__le__(y) <==> x<=y
     |  
     |  __lt__(...)
     |      x.__lt__(y) <==> x<y
     |  
     |  __nonzero__(...)
     |      x.__nonzero__() <==> x != 0
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __setattr__(...)
     |      x.__setattr__('name', value) <==> x.name = value
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __new__ = <built-in method __new__ of PythonQt.PythonQtClassWrapper ob...
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
    
    class QLockFile(PythonQt.PythonQtInstanceWrapper)
     |  Method resolution order:
     |      QLockFile
     |      PythonQt.PythonQtInstanceWrapper
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  __init__(...)
     |      x.__init__(...) initializes x; see help(type(x)) for signature
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  LockError = <class 'PythonQt.QtCore.LockError'>
     |  
     |  
     |  LockFailedError = 1
     |  
     |  NoError = 0
     |  
     |  PermissionError = 2
     |  
     |  UnknownError = 3
     |  
     |  className = <built-in method className of PythonQt.PythonQtClassWrappe...
     |      Return the classname of the object
     |  
     |  delete = <built-in method delete of PythonQt.PythonQtClassWrapper obje...
     |      Deletes the given C++ object
     |  
     |  error = <unbound qt slot error of QLockFile type>
     |      X.error(a)
     |  
     |  getLockInfo = <unbound qt slot getLockInfo of QLockFile type>
     |      X.getLockInfo(a, b, c, d) -> bool
     |  
     |  help = <built-in method help of PythonQt.PythonQtClassWrapper object>
     |      Shows the help of available methods for this class
     |  
     |  inherits = <built-in method inherits of PythonQt.PythonQtClassWrapper ...
     |      Returns if the class inherits or is of given type name
     |  
     |  isLocked = <unbound qt slot isLocked of QLockFile type>
     |      X.isLocked(a) -> bool
     |  
     |  lock = <unbound qt slot lock of QLockFile type>
     |      X.lock(a) -> bool
     |  
     |  removeStaleLockFile = <unbound qt slot removeStaleLockFile of QLockFil...
     |      X.removeStaleLockFile(a) -> bool
     |  
     |  setStaleLockTime = <unbound qt slot setStaleLockTime of QLockFile type...
     |      X.setStaleLockTime(a, b)
     |  
     |  staleLockTime = <unbound qt slot staleLockTime of QLockFile type>
     |      X.staleLockTime(a) -> int
     |  
     |  tryLock = <unbound qt slot tryLock of QLockFile type>
     |      X.tryLock(a, b) -> bool
     |  
     |  unlock = <unbound qt slot unlock of QLockFile type>
     |      X.unlock(a)
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __delattr__(...)
     |      x.__delattr__('name') <==> del x.name
     |  
     |  __eq__(...)
     |      x.__eq__(y) <==> x==y
     |  
     |  __ge__(...)
     |      x.__ge__(y) <==> x>=y
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __gt__(...)
     |      x.__gt__(y) <==> x>y
     |  
     |  __hash__(...)
     |      x.__hash__() <==> hash(x)
     |  
     |  __le__(...)
     |      x.__le__(y) <==> x<=y
     |  
     |  __lt__(...)
     |      x.__lt__(y) <==> x<y
     |  
     |  __ne__(...)
     |      x.__ne__(y) <==> x!=y
     |  
     |  __nonzero__(...)
     |      x.__nonzero__() <==> x != 0
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __setattr__(...)
     |      x.__setattr__('name', value) <==> x.name = value
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __new__ = <built-in method __new__ of PythonQt.PythonQtClassWrapper ob...
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
    
    class QMarginsF(PythonQt.PythonQtInstanceWrapper)
     |  Method resolution order:
     |      QMarginsF
     |      PythonQt.PythonQtInstanceWrapper
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  __add__(...)
     |      x.__add__(y) <==> x+y
     |  
     |  __div__(...)
     |      x.__div__(y) <==> x/y
     |  
     |  __eq__(...)
     |      x.__eq__(y) <==> x==y
     |  
     |  __iadd__(...)
     |      x.__iadd__(y) <==> x+=y
     |  
     |  __idiv__(...)
     |      x.__idiv__(y) <==> x/=y
     |  
     |  __imul__(...)
     |      x.__imul__(y) <==> x*=y
     |  
     |  __init__(...)
     |      x.__init__(...) initializes x; see help(type(x)) for signature
     |  
     |  __isub__(...)
     |      x.__isub__(y) <==> x-=y
     |  
     |  __itruediv__(...)
     |      x.__itruediv__(y) <==> x/=y
     |  
     |  __mul__(...)
     |      x.__mul__(y) <==> x*y
     |  
     |  __neg__(...)
     |      x.__neg__() <==> -x
     |  
     |  __nonzero__(...)
     |      x.__nonzero__() <==> x != 0
     |  
     |  __radd__(...)
     |      x.__radd__(y) <==> y+x
     |  
     |  __rdiv__(...)
     |      x.__rdiv__(y) <==> y/x
     |  
     |  __rmul__(...)
     |      x.__rmul__(y) <==> y*x
     |  
     |  __rsub__(...)
     |      x.__rsub__(y) <==> y-x
     |  
     |  __rtruediv__(...)
     |      x.__rtruediv__(y) <==> y/x
     |  
     |  __sub__(...)
     |      x.__sub__(y) <==> x-y
     |  
     |  __truediv__(...)
     |      x.__truediv__(y) <==> x/y
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  bottom = <unbound qt slot bottom of QMarginsF type>
     |      X.bottom(a) -> float
     |  
     |  className = <built-in method className of PythonQt.PythonQtClassWrappe...
     |      Return the classname of the object
     |  
     |  delete = <built-in method delete of PythonQt.PythonQtClassWrapper obje...
     |      Deletes the given C++ object
     |  
     |  help = <built-in method help of PythonQt.PythonQtClassWrapper object>
     |      Shows the help of available methods for this class
     |  
     |  inherits = <built-in method inherits of PythonQt.PythonQtClassWrapper ...
     |      Returns if the class inherits or is of given type name
     |  
     |  isNull = <unbound qt slot isNull of QMarginsF type>
     |      X.isNull(a) -> bool
     |  
     |  left = <unbound qt slot left of QMarginsF type>
     |      X.left(a) -> float
     |  
     |  readFrom = <unbound qt slot readFrom of QMarginsF type>
     |      X.readFrom(a, b)
     |  
     |  right = <unbound qt slot right of QMarginsF type>
     |      X.right(a) -> float
     |  
     |  setBottom = <unbound qt slot setBottom of QMarginsF type>
     |      X.setBottom(a, b)
     |  
     |  setLeft = <unbound qt slot setLeft of QMarginsF type>
     |      X.setLeft(a, b)
     |  
     |  setRight = <unbound qt slot setRight of QMarginsF type>
     |      X.setRight(a, b)
     |  
     |  setTop = <unbound qt slot setTop of QMarginsF type>
     |      X.setTop(a, b)
     |  
     |  toMargins = <unbound qt slot toMargins of QMarginsF type>
     |      X.toMargins(a) -> PythonQt.QtGui.QMargins
     |  
     |  top = <unbound qt slot top of QMarginsF type>
     |      X.top(a) -> float
     |  
     |  writeTo = <unbound qt slot writeTo of QMarginsF type>
     |      X.writeTo(a, b)
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __delattr__(...)
     |      x.__delattr__('name') <==> del x.name
     |  
     |  __ge__(...)
     |      x.__ge__(y) <==> x>=y
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __gt__(...)
     |      x.__gt__(y) <==> x>y
     |  
     |  __hash__(...)
     |      x.__hash__() <==> hash(x)
     |  
     |  __le__(...)
     |      x.__le__(y) <==> x<=y
     |  
     |  __lt__(...)
     |      x.__lt__(y) <==> x<y
     |  
     |  __ne__(...)
     |      x.__ne__(y) <==> x!=y
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __setattr__(...)
     |      x.__setattr__('name', value) <==> x.name = value
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __new__ = <built-in method __new__ of PythonQt.PythonQtClassWrapper ob...
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
    
    class QMessageAuthenticationCode(PythonQt.PythonQtInstanceWrapper)
     |  Method resolution order:
     |      QMessageAuthenticationCode
     |      PythonQt.PythonQtInstanceWrapper
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  __init__(...)
     |      x.__init__(...) initializes x; see help(type(x)) for signature
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  addData = <unbound qt slot addData of QMessageAuthenticationCode type>
     |      X.addData(a, b, c) -> bool
     |  
     |  className = <built-in method className of PythonQt.PythonQtClassWrappe...
     |      Return the classname of the object
     |  
     |  delete = <built-in method delete of PythonQt.PythonQtClassWrapper obje...
     |      Deletes the given C++ object
     |  
     |  hash = <unbound qt slot static_QMessageAuthenticationCode_hash of QMes...
     |      X.hash(a, b, c) -> PythonQt.QtCore.QByteArray
     |  
     |  help = <built-in method help of PythonQt.PythonQtClassWrapper object>
     |      Shows the help of available methods for this class
     |  
     |  inherits = <built-in method inherits of PythonQt.PythonQtClassWrapper ...
     |      Returns if the class inherits or is of given type name
     |  
     |  reset = <unbound qt slot reset of QMessageAuthenticationCode type>
     |      X.reset(a)
     |  
     |  result = <unbound qt slot result of QMessageAuthenticationCode type>
     |      X.result(a) -> PythonQt.QtCore.QByteArray
     |  
     |  setKey = <unbound qt slot setKey of QMessageAuthenticationCode type>
     |      X.setKey(a, b)
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __delattr__(...)
     |      x.__delattr__('name') <==> del x.name
     |  
     |  __eq__(...)
     |      x.__eq__(y) <==> x==y
     |  
     |  __ge__(...)
     |      x.__ge__(y) <==> x>=y
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __gt__(...)
     |      x.__gt__(y) <==> x>y
     |  
     |  __hash__(...)
     |      x.__hash__() <==> hash(x)
     |  
     |  __le__(...)
     |      x.__le__(y) <==> x<=y
     |  
     |  __lt__(...)
     |      x.__lt__(y) <==> x<y
     |  
     |  __ne__(...)
     |      x.__ne__(y) <==> x!=y
     |  
     |  __nonzero__(...)
     |      x.__nonzero__() <==> x != 0
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __setattr__(...)
     |      x.__setattr__('name', value) <==> x.name = value
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __new__ = <built-in method __new__ of PythonQt.PythonQtClassWrapper ob...
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
    
    class QMessageLogContext(PythonQt.PythonQtInstanceWrapper)
     |  Method resolution order:
     |      QMessageLogContext
     |      PythonQt.PythonQtInstanceWrapper
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  __init__(...)
     |      x.__init__(...) initializes x; see help(type(x)) for signature
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  category = None
     |  
     |  className = <built-in method className of PythonQt.PythonQtClassWrappe...
     |      Return the classname of the object
     |  
     |  delete = <built-in method delete of PythonQt.PythonQtClassWrapper obje...
     |      Deletes the given C++ object
     |  
     |  file = None
     |  
     |  function = None
     |  
     |  help = <built-in method help of PythonQt.PythonQtClassWrapper object>
     |      Shows the help of available methods for this class
     |  
     |  inherits = <built-in method inherits of PythonQt.PythonQtClassWrapper ...
     |      Returns if the class inherits or is of given type name
     |  
     |  line = None
     |  
     |  version = None
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __delattr__(...)
     |      x.__delattr__('name') <==> del x.name
     |  
     |  __eq__(...)
     |      x.__eq__(y) <==> x==y
     |  
     |  __ge__(...)
     |      x.__ge__(y) <==> x>=y
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __gt__(...)
     |      x.__gt__(y) <==> x>y
     |  
     |  __hash__(...)
     |      x.__hash__() <==> hash(x)
     |  
     |  __le__(...)
     |      x.__le__(y) <==> x<=y
     |  
     |  __lt__(...)
     |      x.__lt__(y) <==> x<y
     |  
     |  __ne__(...)
     |      x.__ne__(y) <==> x!=y
     |  
     |  __nonzero__(...)
     |      x.__nonzero__() <==> x != 0
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __setattr__(...)
     |      x.__setattr__('name', value) <==> x.name = value
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __new__ = <built-in method __new__ of PythonQt.PythonQtClassWrapper ob...
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
    
    class QMessageLogger(PythonQt.PythonQtInstanceWrapper)
     |  Method resolution order:
     |      QMessageLogger
     |      PythonQt.PythonQtInstanceWrapper
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  __init__(...)
     |      x.__init__(...) initializes x; see help(type(x)) for signature
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  className = <built-in method className of PythonQt.PythonQtClassWrappe...
     |      Return the classname of the object
     |  
     |  critical = <unbound qt slot critical of QMessageLogger type>
     |      X.critical(a, b)
     |  
     |  debug = <unbound qt slot debug of QMessageLogger type>
     |      X.debug(a, b)
     |  
     |  delete = <built-in method delete of PythonQt.PythonQtClassWrapper obje...
     |      Deletes the given C++ object
     |  
     |  fatal = <unbound qt slot fatal of QMessageLogger type>
     |      X.fatal(a, b)
     |  
     |  help = <built-in method help of PythonQt.PythonQtClassWrapper object>
     |      Shows the help of available methods for this class
     |  
     |  info = <unbound qt slot info of QMessageLogger type>
     |      X.info(a, b)
     |  
     |  inherits = <built-in method inherits of PythonQt.PythonQtClassWrapper ...
     |      Returns if the class inherits or is of given type name
     |  
     |  noDebug = <unbound qt slot noDebug of QMessageLogger type>
     |      X.noDebug(a, b)
     |  
     |  warning = <unbound qt slot warning of QMessageLogger type>
     |      X.warning(a, b)
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __delattr__(...)
     |      x.__delattr__('name') <==> del x.name
     |  
     |  __eq__(...)
     |      x.__eq__(y) <==> x==y
     |  
     |  __ge__(...)
     |      x.__ge__(y) <==> x>=y
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __gt__(...)
     |      x.__gt__(y) <==> x>y
     |  
     |  __hash__(...)
     |      x.__hash__() <==> hash(x)
     |  
     |  __le__(...)
     |      x.__le__(y) <==> x<=y
     |  
     |  __lt__(...)
     |      x.__lt__(y) <==> x<y
     |  
     |  __ne__(...)
     |      x.__ne__(y) <==> x!=y
     |  
     |  __nonzero__(...)
     |      x.__nonzero__() <==> x != 0
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __setattr__(...)
     |      x.__setattr__('name', value) <==> x.name = value
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __new__ = <built-in method __new__ of PythonQt.PythonQtClassWrapper ob...
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
    
    class QMetaClassInfo(PythonQt.PythonQtInstanceWrapper)
     |  Method resolution order:
     |      QMetaClassInfo
     |      PythonQt.PythonQtInstanceWrapper
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  __init__(...)
     |      x.__init__(...) initializes x; see help(type(x)) for signature
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  className = <built-in method className of PythonQt.PythonQtClassWrappe...
     |      Return the classname of the object
     |  
     |  delete = <built-in method delete of PythonQt.PythonQtClassWrapper obje...
     |      Deletes the given C++ object
     |  
     |  enclosingMetaObject = <unbound qt slot enclosingMetaObject of QMetaCla...
     |      X.enclosingMetaObject(a) -> PythonQt.QtCore.QMetaObject
     |  
     |  help = <built-in method help of PythonQt.PythonQtClassWrapper object>
     |      Shows the help of available methods for this class
     |  
     |  inherits = <built-in method inherits of PythonQt.PythonQtClassWrapper ...
     |      Returns if the class inherits or is of given type name
     |  
     |  name = <unbound qt slot name of QMetaClassInfo type>
     |      X.name(a) -> int
     |  
     |  value = <unbound qt slot value of QMetaClassInfo type>
     |      X.value(a) -> int
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __delattr__(...)
     |      x.__delattr__('name') <==> del x.name
     |  
     |  __eq__(...)
     |      x.__eq__(y) <==> x==y
     |  
     |  __ge__(...)
     |      x.__ge__(y) <==> x>=y
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __gt__(...)
     |      x.__gt__(y) <==> x>y
     |  
     |  __hash__(...)
     |      x.__hash__() <==> hash(x)
     |  
     |  __le__(...)
     |      x.__le__(y) <==> x<=y
     |  
     |  __lt__(...)
     |      x.__lt__(y) <==> x<y
     |  
     |  __ne__(...)
     |      x.__ne__(y) <==> x!=y
     |  
     |  __nonzero__(...)
     |      x.__nonzero__() <==> x != 0
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __setattr__(...)
     |      x.__setattr__('name', value) <==> x.name = value
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __new__ = <built-in method __new__ of PythonQt.PythonQtClassWrapper ob...
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
    
    class QMetaEnum(PythonQt.PythonQtInstanceWrapper)
     |  Method resolution order:
     |      QMetaEnum
     |      PythonQt.PythonQtInstanceWrapper
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  __init__(...)
     |      x.__init__(...) initializes x; see help(type(x)) for signature
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  className = <built-in method className of PythonQt.PythonQtClassWrappe...
     |      Return the classname of the object
     |  
     |  delete = <built-in method delete of PythonQt.PythonQtClassWrapper obje...
     |      Deletes the given C++ object
     |  
     |  enclosingMetaObject = <unbound qt slot enclosingMetaObject of QMetaEnu...
     |      X.enclosingMetaObject(a) -> PythonQt.QtCore.QMetaObject
     |  
     |  help = <built-in method help of PythonQt.PythonQtClassWrapper object>
     |      Shows the help of available methods for this class
     |  
     |  inherits = <built-in method inherits of PythonQt.PythonQtClassWrapper ...
     |      Returns if the class inherits or is of given type name
     |  
     |  isFlag = <unbound qt slot isFlag of QMetaEnum type>
     |      X.isFlag(a) -> bool
     |  
     |  isValid = <unbound qt slot isValid of QMetaEnum type>
     |      X.isValid(a) -> bool
     |  
     |  key = <unbound qt slot key of QMetaEnum type>
     |      X.key(a, b) -> int
     |  
     |  keyCount = <unbound qt slot keyCount of QMetaEnum type>
     |      X.keyCount(a) -> int
     |  
     |  keyToValue = <unbound qt slot keyToValue of QMetaEnum type>
     |      X.keyToValue(a, b, c) -> int
     |  
     |  keysToValue = <unbound qt slot keysToValue of QMetaEnum type>
     |      X.keysToValue(a, b, c) -> int
     |  
     |  name = <unbound qt slot name of QMetaEnum type>
     |      X.name(a) -> int
     |  
     |  scope = <unbound qt slot scope of QMetaEnum type>
     |      X.scope(a) -> int
     |  
     |  value = <unbound qt slot value of QMetaEnum type>
     |      X.value(a, b) -> int
     |  
     |  valueToKey = <unbound qt slot valueToKey of QMetaEnum type>
     |      X.valueToKey(a, b) -> int
     |  
     |  valueToKeys = <unbound qt slot valueToKeys of QMetaEnum type>
     |      X.valueToKeys(a, b) -> PythonQt.QtCore.QByteArray
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __delattr__(...)
     |      x.__delattr__('name') <==> del x.name
     |  
     |  __eq__(...)
     |      x.__eq__(y) <==> x==y
     |  
     |  __ge__(...)
     |      x.__ge__(y) <==> x>=y
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __gt__(...)
     |      x.__gt__(y) <==> x>y
     |  
     |  __hash__(...)
     |      x.__hash__() <==> hash(x)
     |  
     |  __le__(...)
     |      x.__le__(y) <==> x<=y
     |  
     |  __lt__(...)
     |      x.__lt__(y) <==> x<y
     |  
     |  __ne__(...)
     |      x.__ne__(y) <==> x!=y
     |  
     |  __nonzero__(...)
     |      x.__nonzero__() <==> x != 0
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __setattr__(...)
     |      x.__setattr__('name', value) <==> x.name = value
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __new__ = <built-in method __new__ of PythonQt.PythonQtClassWrapper ob...
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
    
    class QMetaMethod(PythonQt.PythonQtInstanceWrapper)
     |  Method resolution order:
     |      QMetaMethod
     |      PythonQt.PythonQtInstanceWrapper
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  __eq__(...)
     |      x.__eq__(y) <==> x==y
     |  
     |  __init__(...)
     |      x.__init__(...) initializes x; see help(type(x)) for signature
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  Access = <class 'PythonQt.QtCore.Access'>
     |  
     |  
     |  Attributes = <class 'PythonQt.QtCore.Attributes'>
     |  
     |  
     |  Cloned = 2
     |  
     |  Compatibility = 1
     |  
     |  Constructor = 3
     |  
     |  Method = 0
     |  
     |  MethodType = <class 'PythonQt.QtCore.MethodType'>
     |  
     |  
     |  Private = 0
     |  
     |  Protected = 1
     |  
     |  Public = 2
     |  
     |  Scriptable = 4
     |  
     |  Signal = 1
     |  
     |  Slot = 2
     |  
     |  access = <unbound qt slot access of QMetaMethod type>
     |      X.access(a)
     |  
     |  attributes = <unbound qt slot attributes of QMetaMethod type>
     |      X.attributes(a) -> int
     |  
     |  className = <built-in method className of PythonQt.PythonQtClassWrappe...
     |      Return the classname of the object
     |  
     |  delete = <built-in method delete of PythonQt.PythonQtClassWrapper obje...
     |      Deletes the given C++ object
     |  
     |  enclosingMetaObject = <unbound qt slot enclosingMetaObject of QMetaMet...
     |      X.enclosingMetaObject(a) -> PythonQt.QtCore.QMetaObject
     |  
     |  getParameterTypes = <unbound qt slot getParameterTypes of QMetaMethod ...
     |      X.getParameterTypes(a, b)
     |  
     |  help = <built-in method help of PythonQt.PythonQtClassWrapper object>
     |      Shows the help of available methods for this class
     |  
     |  inherits = <built-in method inherits of PythonQt.PythonQtClassWrapper ...
     |      Returns if the class inherits or is of given type name
     |  
     |  isValid = <unbound qt slot isValid of QMetaMethod type>
     |      X.isValid(a) -> bool
     |  
     |  methodIndex = <unbound qt slot methodIndex of QMetaMethod type>
     |      X.methodIndex(a) -> int
     |  
     |  methodSignature = <unbound qt slot methodSignature of QMetaMethod type...
     |      X.methodSignature(a) -> PythonQt.QtCore.QByteArray
     |  
     |  methodType = <unbound qt slot methodType of QMetaMethod type>
     |      X.methodType(a)
     |  
     |  name = <unbound qt slot name of QMetaMethod type>
     |      X.name(a) -> PythonQt.QtCore.QByteArray
     |  
     |  parameterCount = <unbound qt slot parameterCount of QMetaMethod type>
     |      X.parameterCount(a) -> int
     |  
     |  parameterNames = <unbound qt slot parameterNames of QMetaMethod type>
     |      X.parameterNames(a)
     |  
     |  parameterType = <unbound qt slot parameterType of QMetaMethod type>
     |      X.parameterType(a, b) -> int
     |  
     |  parameterTypes = <unbound qt slot parameterTypes of QMetaMethod type>
     |      X.parameterTypes(a)
     |  
     |  returnType = <unbound qt slot returnType of QMetaMethod type>
     |      X.returnType(a) -> int
     |  
     |  revision = <unbound qt slot revision of QMetaMethod type>
     |      X.revision(a) -> int
     |  
     |  tag = <unbound qt slot tag of QMetaMethod type>
     |      X.tag(a) -> int
     |  
     |  typeName = <unbound qt slot typeName of QMetaMethod type>
     |      X.typeName(a) -> int
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __delattr__(...)
     |      x.__delattr__('name') <==> del x.name
     |  
     |  __ge__(...)
     |      x.__ge__(y) <==> x>=y
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __gt__(...)
     |      x.__gt__(y) <==> x>y
     |  
     |  __hash__(...)
     |      x.__hash__() <==> hash(x)
     |  
     |  __le__(...)
     |      x.__le__(y) <==> x<=y
     |  
     |  __lt__(...)
     |      x.__lt__(y) <==> x<y
     |  
     |  __ne__(...)
     |      x.__ne__(y) <==> x!=y
     |  
     |  __nonzero__(...)
     |      x.__nonzero__() <==> x != 0
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __setattr__(...)
     |      x.__setattr__('name', value) <==> x.name = value
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __new__ = <built-in method __new__ of PythonQt.PythonQtClassWrapper ob...
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
    
    class QMetaObject(PythonQt.PythonQtInstanceWrapper)
     |  Method resolution order:
     |      QMetaObject
     |      PythonQt.PythonQtInstanceWrapper
     |      __builtin__.object
     |  
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  checkConnectArgs = <unbound qt slot static_QMetaObject_checkConnectArg...
     |      X.checkConnectArgs(a, b) -> bool
     |  
     |  classInfo = <unbound qt slot classInfo of QMetaObject type>
     |      X.classInfo(a, b) -> PythonQt.QtCore.QMetaClassInfo
     |  
     |  classInfoCount = <unbound qt slot classInfoCount of QMetaObject type>
     |      X.classInfoCount(a) -> int
     |  
     |  classInfoOffset = <unbound qt slot classInfoOffset of QMetaObject type...
     |      X.classInfoOffset(a) -> int
     |  
     |  className = <unbound qt slot className of QMetaObject type>
     |      X.className(a) -> int
     |  
     |  constructor = <unbound qt slot constructor of QMetaObject type>
     |      X.constructor(a, b) -> PythonQt.QtCore.QMetaMethod
     |  
     |  constructorCount = <unbound qt slot constructorCount of QMetaObject ty...
     |      X.constructorCount(a) -> int
     |  
     |  delete = <built-in method delete of PythonQt.PythonQtClassWrapper obje...
     |      Deletes the given C++ object
     |  
     |  enumerator = <unbound qt slot enumerator of QMetaObject type>
     |      X.enumerator(a, b) -> PythonQt.QtCore.QMetaEnum
     |  
     |  enumeratorCount = <unbound qt slot enumeratorCount of QMetaObject type...
     |      X.enumeratorCount(a) -> int
     |  
     |  enumeratorOffset = <unbound qt slot enumeratorOffset of QMetaObject ty...
     |      X.enumeratorOffset(a) -> int
     |  
     |  help = <built-in method help of PythonQt.PythonQtClassWrapper object>
     |      Shows the help of available methods for this class
     |  
     |  indexOfClassInfo = <unbound qt slot indexOfClassInfo of QMetaObject ty...
     |      X.indexOfClassInfo(a, b) -> int
     |  
     |  indexOfConstructor = <unbound qt slot indexOfConstructor of QMetaObjec...
     |      X.indexOfConstructor(a, b) -> int
     |  
     |  indexOfEnumerator = <unbound qt slot indexOfEnumerator of QMetaObject ...
     |      X.indexOfEnumerator(a, b) -> int
     |  
     |  indexOfMethod = <unbound qt slot indexOfMethod of QMetaObject type>
     |      X.indexOfMethod(a, b) -> int
     |  
     |  indexOfProperty = <unbound qt slot indexOfProperty of QMetaObject type...
     |      X.indexOfProperty(a, b) -> int
     |  
     |  indexOfSignal = <unbound qt slot indexOfSignal of QMetaObject type>
     |      X.indexOfSignal(a, b) -> int
     |  
     |  indexOfSlot = <unbound qt slot indexOfSlot of QMetaObject type>
     |      X.indexOfSlot(a, b) -> int
     |  
     |  inherits = <built-in method inherits of PythonQt.PythonQtClassWrapper ...
     |      Returns if the class inherits or is of given type name
     |  
     |  method = <unbound qt slot method of QMetaObject type>
     |      X.method(a, b) -> PythonQt.QtCore.QMetaMethod
     |  
     |  methodCount = <unbound qt slot methodCount of QMetaObject type>
     |      X.methodCount(a) -> int
     |  
     |  methodOffset = <unbound qt slot methodOffset of QMetaObject type>
     |      X.methodOffset(a) -> int
     |  
     |  normalizedSignature = <unbound qt slot static_QMetaObject_normalizedSi...
     |      X.normalizedSignature(a) -> PythonQt.QtCore.QByteArray
     |  
     |  normalizedType = <unbound qt slot static_QMetaObject_normalizedType of...
     |      X.normalizedType(a) -> PythonQt.QtCore.QByteArray
     |  
     |  property = <unbound qt slot property of QMetaObject type>
     |      X.property(a, b) -> PythonQt.QtCore.QMetaProperty
     |  
     |  propertyCount = <unbound qt slot propertyCount of QMetaObject type>
     |      X.propertyCount(a) -> int
     |  
     |  propertyOffset = <unbound qt slot propertyOffset of QMetaObject type>
     |      X.propertyOffset(a) -> int
     |  
     |  superClass = <unbound qt slot superClass of QMetaObject type>
     |      X.superClass(a) -> PythonQt.QtCore.QMetaObject
     |  
     |  userProperty = <unbound qt slot userProperty of QMetaObject type>
     |      X.userProperty(a) -> PythonQt.QtCore.QMetaProperty
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __delattr__(...)
     |      x.__delattr__('name') <==> del x.name
     |  
     |  __eq__(...)
     |      x.__eq__(y) <==> x==y
     |  
     |  __ge__(...)
     |      x.__ge__(y) <==> x>=y
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __gt__(...)
     |      x.__gt__(y) <==> x>y
     |  
     |  __hash__(...)
     |      x.__hash__() <==> hash(x)
     |  
     |  __init__(...)
     |      x.__init__(...) initializes x; see help(type(x)) for signature
     |  
     |  __le__(...)
     |      x.__le__(y) <==> x<=y
     |  
     |  __lt__(...)
     |      x.__lt__(y) <==> x<y
     |  
     |  __ne__(...)
     |      x.__ne__(y) <==> x!=y
     |  
     |  __nonzero__(...)
     |      x.__nonzero__() <==> x != 0
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __setattr__(...)
     |      x.__setattr__('name', value) <==> x.name = value
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __new__ = <built-in method __new__ of PythonQt.PythonQtClassWrapper ob...
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
    
    class QMetaProperty(PythonQt.PythonQtInstanceWrapper)
     |  Method resolution order:
     |      QMetaProperty
     |      PythonQt.PythonQtInstanceWrapper
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  __init__(...)
     |      x.__init__(...) initializes x; see help(type(x)) for signature
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  className = <built-in method className of PythonQt.PythonQtClassWrappe...
     |      Return the classname of the object
     |  
     |  delete = <built-in method delete of PythonQt.PythonQtClassWrapper obje...
     |      Deletes the given C++ object
     |  
     |  enclosingMetaObject = <unbound qt slot enclosingMetaObject of QMetaPro...
     |      X.enclosingMetaObject(a) -> PythonQt.QtCore.QMetaObject
     |  
     |  enumerator = <unbound qt slot enumerator of QMetaProperty type>
     |      X.enumerator(a) -> PythonQt.QtCore.QMetaEnum
     |  
     |  hasNotifySignal = <unbound qt slot hasNotifySignal of QMetaProperty ty...
     |      X.hasNotifySignal(a) -> bool
     |  
     |  hasStdCppSet = <unbound qt slot hasStdCppSet of QMetaProperty type>
     |      X.hasStdCppSet(a) -> bool
     |  
     |  help = <built-in method help of PythonQt.PythonQtClassWrapper object>
     |      Shows the help of available methods for this class
     |  
     |  inherits = <built-in method inherits of PythonQt.PythonQtClassWrapper ...
     |      Returns if the class inherits or is of given type name
     |  
     |  isConstant = <unbound qt slot isConstant of QMetaProperty type>
     |      X.isConstant(a) -> bool
     |  
     |  isDesignable = <unbound qt slot isDesignable of QMetaProperty type>
     |      X.isDesignable(a, b) -> bool
     |  
     |  isEditable = <unbound qt slot isEditable of QMetaProperty type>
     |      X.isEditable(a, b) -> bool
     |  
     |  isEnumType = <unbound qt slot isEnumType of QMetaProperty type>
     |      X.isEnumType(a) -> bool
     |  
     |  isFinal = <unbound qt slot isFinal of QMetaProperty type>
     |      X.isFinal(a) -> bool
     |  
     |  isFlagType = <unbound qt slot isFlagType of QMetaProperty type>
     |      X.isFlagType(a) -> bool
     |  
     |  isReadable = <unbound qt slot isReadable of QMetaProperty type>
     |      X.isReadable(a) -> bool
     |  
     |  isResettable = <unbound qt slot isResettable of QMetaProperty type>
     |      X.isResettable(a) -> bool
     |  
     |  isScriptable = <unbound qt slot isScriptable of QMetaProperty type>
     |      X.isScriptable(a, b) -> bool
     |  
     |  isStored = <unbound qt slot isStored of QMetaProperty type>
     |      X.isStored(a, b) -> bool
     |  
     |  isUser = <unbound qt slot isUser of QMetaProperty type>
     |      X.isUser(a, b) -> bool
     |  
     |  isValid = <unbound qt slot isValid of QMetaProperty type>
     |      X.isValid(a) -> bool
     |  
     |  isWritable = <unbound qt slot isWritable of QMetaProperty type>
     |      X.isWritable(a) -> bool
     |  
     |  name = <unbound qt slot name of QMetaProperty type>
     |      X.name(a) -> int
     |  
     |  notifySignal = <unbound qt slot notifySignal of QMetaProperty type>
     |      X.notifySignal(a) -> PythonQt.QtCore.QMetaMethod
     |  
     |  notifySignalIndex = <unbound qt slot notifySignalIndex of QMetaPropert...
     |      X.notifySignalIndex(a) -> int
     |  
     |  propertyIndex = <unbound qt slot propertyIndex of QMetaProperty type>
     |      X.propertyIndex(a) -> int
     |  
     |  read = <unbound qt slot read of QMetaProperty type>
     |      X.read(a, b) -> object
     |  
     |  readOnGadget = <unbound qt slot readOnGadget of QMetaProperty type>
     |      X.readOnGadget(a, b) -> object
     |  
     |  reset = <unbound qt slot reset of QMetaProperty type>
     |      X.reset(a, b) -> bool
     |  
     |  resetOnGadget = <unbound qt slot resetOnGadget of QMetaProperty type>
     |      X.resetOnGadget(a, b) -> bool
     |  
     |  revision = <unbound qt slot revision of QMetaProperty type>
     |      X.revision(a) -> int
     |  
     |  type = <unbound qt slot type of QMetaProperty type>
     |      X.type(a)
     |  
     |  typeName = <unbound qt slot typeName of QMetaProperty type>
     |      X.typeName(a) -> int
     |  
     |  userType = <unbound qt slot userType of QMetaProperty type>
     |      X.userType(a) -> int
     |  
     |  write = <unbound qt slot write of QMetaProperty type>
     |      X.write(a, b, c) -> bool
     |  
     |  writeOnGadget = <unbound qt slot writeOnGadget of QMetaProperty type>
     |      X.writeOnGadget(a, b, c) -> bool
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __delattr__(...)
     |      x.__delattr__('name') <==> del x.name
     |  
     |  __eq__(...)
     |      x.__eq__(y) <==> x==y
     |  
     |  __ge__(...)
     |      x.__ge__(y) <==> x>=y
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __gt__(...)
     |      x.__gt__(y) <==> x>y
     |  
     |  __hash__(...)
     |      x.__hash__() <==> hash(x)
     |  
     |  __le__(...)
     |      x.__le__(y) <==> x<=y
     |  
     |  __lt__(...)
     |      x.__lt__(y) <==> x<y
     |  
     |  __ne__(...)
     |      x.__ne__(y) <==> x!=y
     |  
     |  __nonzero__(...)
     |      x.__nonzero__() <==> x != 0
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __setattr__(...)
     |      x.__setattr__('name', value) <==> x.name = value
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __new__ = <built-in method __new__ of PythonQt.PythonQtClassWrapper ob...
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
    
    class QMetaType(PythonQt.PythonQtInstanceWrapper)
     |  Method resolution order:
     |      QMetaType
     |      PythonQt.PythonQtInstanceWrapper
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  __init__(...)
     |      x.__init__(...) initializes x; see help(type(x)) for signature
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  IsEnumeration = 16
     |  
     |  IsGadget = 512
     |  
     |  MovableType = 4
     |  
     |  NeedsConstruction = 1
     |  
     |  NeedsDestruction = 2
     |  
     |  PointerToQObject = 8
     |  
     |  SharedPointerToQObject = 32
     |  
     |  TrackingPointerToQObject = 128
     |  
     |  TypeFlag = <class 'PythonQt.QtCore.TypeFlag'>
     |  
     |  
     |  TypeFlags = <class 'PythonQt.QtCore.TypeFlags'>
     |  
     |  
     |  WasDeclaredAsMetaType = 256
     |  
     |  WeakPointerToQObject = 64
     |  
     |  className = <built-in method className of PythonQt.PythonQtClassWrappe...
     |      Return the classname of the object
     |  
     |  compare = <unbound qt slot static_QMetaType_compare of QMetaType type>
     |      X.compare(a, b, c, d) -> bool
     |  
     |  construct = <unbound qt slot static_QMetaType_construct of QMetaType t...
     |      X.construct(a, b, c)
     |  
     |  convert = <unbound qt slot static_QMetaType_convert of QMetaType type>
     |      X.convert(a, b, c, d) -> bool
     |  
     |  create = <unbound qt slot create of QMetaType type>
     |      X.create(a, b)
     |  
     |  delete = <built-in method delete of PythonQt.PythonQtClassWrapper obje...
     |      Deletes the given C++ object
     |  
     |  destroy = <unbound qt slot static_QMetaType_destroy of QMetaType type>
     |      X.destroy(a, b)
     |  
     |  destruct = <unbound qt slot static_QMetaType_destruct of QMetaType typ...
     |      X.destruct(a, b)
     |  
     |  equals = <unbound qt slot static_QMetaType_equals of QMetaType type>
     |      X.equals(a, b, c, d) -> bool
     |  
     |  flags = <unbound qt slot flags of QMetaType type>
     |      X.flags(a)
     |  
     |  hasRegisteredComparators = <unbound qt slot static_QMetaType_hasRegist...
     |      X.hasRegisteredComparators(a) -> bool
     |  
     |  hasRegisteredConverterFunction = <unbound qt slot static_QMetaType_has...
     |      X.hasRegisteredConverterFunction(a, b) -> bool
     |  
     |  hasRegisteredDebugStreamOperator = <unbound qt slot static_QMetaType_h...
     |      X.hasRegisteredDebugStreamOperator(a) -> bool
     |  
     |  help = <built-in method help of PythonQt.PythonQtClassWrapper object>
     |      Shows the help of available methods for this class
     |  
     |  inherits = <built-in method inherits of PythonQt.PythonQtClassWrapper ...
     |      Returns if the class inherits or is of given type name
     |  
     |  isRegistered = <unbound qt slot isRegistered of QMetaType type>
     |      X.isRegistered(a) -> bool
     |  
     |  isValid = <unbound qt slot isValid of QMetaType type>
     |      X.isValid(a) -> bool
     |  
     |  load = <unbound qt slot static_QMetaType_load of QMetaType type>
     |      X.load(a, b, c) -> bool
     |  
     |  metaObject = <unbound qt slot metaObject of QMetaType type>
     |      X.metaObject(a) -> PythonQt.QtCore.QMetaObject
     |  
     |  metaObjectForType = <unbound qt slot static_QMetaType_metaObjectForTyp...
     |      X.metaObjectForType(a) -> PythonQt.QtCore.QMetaObject
     |  
     |  registerNormalizedTypedef = <unbound qt slot static_QMetaType_register...
     |      X.registerNormalizedTypedef(a, b) -> int
     |  
     |  registerTypedef = <unbound qt slot static_QMetaType_registerTypedef of...
     |      X.registerTypedef(a, b) -> int
     |  
     |  save = <unbound qt slot static_QMetaType_save of QMetaType type>
     |      X.save(a, b, c) -> bool
     |  
     |  sizeOf = <unbound qt slot sizeOf of QMetaType type>
     |      X.sizeOf(a) -> int
     |  
     |  type = <unbound qt slot static_QMetaType_type of QMetaType type>
     |      X.type(a) -> int
     |  
     |  typeFlags = <unbound qt slot static_QMetaType_typeFlags of QMetaType t...
     |      X.typeFlags(a)
     |  
     |  typeName = <unbound qt slot static_QMetaType_typeName of QMetaType typ...
     |      X.typeName(a) -> int
     |  
     |  unregisterType = <unbound qt slot static_QMetaType_unregisterType of Q...
     |      X.unregisterType(a) -> bool
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __delattr__(...)
     |      x.__delattr__('name') <==> del x.name
     |  
     |  __eq__(...)
     |      x.__eq__(y) <==> x==y
     |  
     |  __ge__(...)
     |      x.__ge__(y) <==> x>=y
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __gt__(...)
     |      x.__gt__(y) <==> x>y
     |  
     |  __hash__(...)
     |      x.__hash__() <==> hash(x)
     |  
     |  __le__(...)
     |      x.__le__(y) <==> x<=y
     |  
     |  __lt__(...)
     |      x.__lt__(y) <==> x<y
     |  
     |  __ne__(...)
     |      x.__ne__(y) <==> x!=y
     |  
     |  __nonzero__(...)
     |      x.__nonzero__() <==> x != 0
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __setattr__(...)
     |      x.__setattr__('name', value) <==> x.name = value
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __new__ = <built-in method __new__ of PythonQt.PythonQtClassWrapper ob...
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
    
    class QMimeData(PythonQt.PythonQtInstanceWrapper)
     |  Method resolution order:
     |      QMimeData
     |      PythonQt.PythonQtInstanceWrapper
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  __init__(...)
     |      x.__init__(...) initializes x; see help(type(x)) for signature
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  blockSignals = <unbound qt slot blockSignals of QMimeData type>
     |      X.blockSignals(a, b) -> bool
     |  
     |  childEvent = <unbound qt slot py_q_childEvent of QMimeData type>
     |      X.childEvent(a, b)
     |  
     |  children = <unbound qt slot children of QMimeData type>
     |      X.children(a) -> tuple
     |  
     |  className = <built-in method className of PythonQt.PythonQtClassWrappe...
     |      Return the classname of the object
     |  
     |  clear = <unbound qt slot clear of QMimeData type>
     |      X.clear(a)
     |  
     |  colorData = <unbound qt slot colorData of QMimeData type>
     |      X.colorData(a) -> object
     |  
     |  connect = <unbound qt slot connect of QMimeData type>
     |      X.connect(a, b, c, d, e) -> bool
     |  
     |  customEvent = <unbound qt slot py_q_customEvent of QMimeData type>
     |      X.customEvent(a, b)
     |  
     |  data = <unbound qt slot data of QMimeData type>
     |      X.data(a, b) -> PythonQt.QtCore.QByteArray
     |  
     |  delete = <built-in method delete of PythonQt.PythonQtClassWrapper obje...
     |      Deletes the given C++ object
     |  
     |  deleteLater = <unbound qt slot deleteLater of QMimeData type>
     |      X.deleteLater()
     |  
     |  destroyed = <unbound qt signal destroyed of QMimeData type>
     |  
     |  
     |  disconnect = <unbound qt slot disconnect of QMimeData type>
     |      X.disconnect(a, b, c, d) -> bool
     |  
     |  dumpObjectInfo = <unbound qt slot dumpObjectInfo of QMimeData type>
     |      X.dumpObjectInfo(a)
     |  
     |  dumpObjectTree = <unbound qt slot dumpObjectTree of QMimeData type>
     |      X.dumpObjectTree(a)
     |  
     |  dynamicPropertyNames = <unbound qt slot dynamicPropertyNames of QMimeD...
     |      X.dynamicPropertyNames(a)
     |  
     |  event = <unbound qt slot py_q_event of QMimeData type>
     |      X.event(a, b) -> bool
     |  
     |  eventFilter = <unbound qt slot py_q_eventFilter of QMimeData type>
     |      X.eventFilter(a, b, c) -> bool
     |  
     |  findChild = <unbound qt slot findChild of QMimeData type>
     |      X.findChild(a, b, c) -> PythonQt.private.QObject
     |  
     |  findChildren = <unbound qt slot findChildren of QMimeData type>
     |      X.findChildren(a, b, c) -> tuple
     |  
     |  formats = <unbound qt slot py_q_formats of QMimeData type>
     |      X.formats(a) -> tuple
     |  
     |  hasColor = <unbound qt slot hasColor of QMimeData type>
     |      X.hasColor(a) -> bool
     |  
     |  hasFormat = <unbound qt slot py_q_hasFormat of QMimeData type>
     |      X.hasFormat(a, b) -> bool
     |  
     |  hasHtml = <unbound qt slot hasHtml of QMimeData type>
     |      X.hasHtml(a) -> bool
     |  
     |  hasImage = <unbound qt slot hasImage of QMimeData type>
     |      X.hasImage(a) -> bool
     |  
     |  hasText = <unbound qt slot hasText of QMimeData type>
     |      X.hasText(a) -> bool
     |  
     |  hasUrls = <unbound qt slot hasUrls of QMimeData type>
     |      X.hasUrls(a) -> bool
     |  
     |  help = <built-in method help of PythonQt.PythonQtClassWrapper object>
     |      Shows the help of available methods for this class
     |  
     |  html = <unbound qt slot html of QMimeData type>
     |      X.html(a) -> str
     |  
     |  imageData = <unbound qt slot imageData of QMimeData type>
     |      X.imageData(a) -> object
     |  
     |  inherits = <built-in method inherits of PythonQt.PythonQtClassWrapper ...
     |      Returns if the class inherits or is of given type name
     |  
     |  installEventFilter = <unbound qt slot installEventFilter of QMimeData ...
     |      X.installEventFilter(a, b)
     |  
     |  isSignalConnected = <unbound qt slot isSignalConnected of QMimeData ty...
     |      X.isSignalConnected(a, b) -> bool
     |  
     |  isWidgetType = <unbound qt slot isWidgetType of QMimeData type>
     |      X.isWidgetType(a) -> bool
     |  
     |  isWindowType = <unbound qt slot isWindowType of QMimeData type>
     |      X.isWindowType(a) -> bool
     |  
     |  killTimer = <unbound qt slot killTimer of QMimeData type>
     |      X.killTimer(a, b)
     |  
     |  metaObject = <unbound qt slot metaObject of QMimeData type>
     |      X.metaObject(a) -> PythonQt.QtCore.QMetaObject
     |  
     |  moveToThread = <unbound qt slot moveToThread of QMimeData type>
     |      X.moveToThread(a, b)
     |  
     |  objectName = None
     |  
     |  objectNameChanged = <unbound qt signal objectNameChanged of QMimeData ...
     |  
     |  
     |  parent = <unbound qt slot parent of QMimeData type>
     |      X.parent(a) -> PythonQt.private.QObject
     |  
     |  property = <unbound qt slot property of QMimeData type>
     |      X.property(a, b) -> object
     |  
     |  removeEventFilter = <unbound qt slot removeEventFilter of QMimeData ty...
     |      X.removeEventFilter(a, b)
     |  
     |  removeFormat = <unbound qt slot removeFormat of QMimeData type>
     |      X.removeFormat(a, b)
     |  
     |  retrieveData = <unbound qt slot py_q_retrieveData of QMimeData type>
     |      X.retrieveData(a, b, c) -> object
     |  
     |  sender = <unbound qt slot sender of QMimeData type>
     |      X.sender(a) -> PythonQt.private.QObject
     |  
     |  senderSignalIndex = <unbound qt slot senderSignalIndex of QMimeData ty...
     |      X.senderSignalIndex(a) -> int
     |  
     |  setColorData = <unbound qt slot setColorData of QMimeData type>
     |      X.setColorData(a, b)
     |  
     |  setData = <unbound qt slot setData of QMimeData type>
     |      X.setData(a, b, c)
     |  
     |  setHtml = <unbound qt slot setHtml of QMimeData type>
     |      X.setHtml(a, b)
     |  
     |  setImageData = <unbound qt slot setImageData of QMimeData type>
     |      X.setImageData(a, b)
     |  
     |  setObjectName = <unbound qt slot setObjectName of QMimeData type>
     |      X.setObjectName(a, b)
     |  
     |  setParent = <unbound qt slot setParent of QMimeData type>
     |      X.setParent(a, b)
     |  
     |  setProperty = <unbound qt slot setProperty of QMimeData type>
     |      X.setProperty(a, b, c) -> bool
     |  
     |  setText = <unbound qt slot setText of QMimeData type>
     |      X.setText(a, b)
     |  
     |  setUrls = <unbound qt slot setUrls of QMimeData type>
     |      X.setUrls(a, b)
     |  
     |  signalsBlocked = <unbound qt slot signalsBlocked of QMimeData type>
     |      X.signalsBlocked(a) -> bool
     |  
     |  startTimer = <unbound qt slot startTimer of QMimeData type>
     |      X.startTimer(a, b, c) -> int
     |  
     |  text = <unbound qt slot text of QMimeData type>
     |      X.text(a) -> str
     |  
     |  thread = <unbound qt slot thread of QMimeData type>
     |      X.thread(a)
     |  
     |  timerEvent = <unbound qt slot py_q_timerEvent of QMimeData type>
     |      X.timerEvent(a, b)
     |  
     |  tr = <unbound qt slot tr of QMimeData type>
     |      X.tr(a, b, c, d) -> str
     |  
     |  urls = <unbound qt slot urls of QMimeData type>
     |      X.urls(a) -> tuple
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __delattr__(...)
     |      x.__delattr__('name') <==> del x.name
     |  
     |  __eq__(...)
     |      x.__eq__(y) <==> x==y
     |  
     |  __ge__(...)
     |      x.__ge__(y) <==> x>=y
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __gt__(...)
     |      x.__gt__(y) <==> x>y
     |  
     |  __hash__(...)
     |      x.__hash__() <==> hash(x)
     |  
     |  __le__(...)
     |      x.__le__(y) <==> x<=y
     |  
     |  __lt__(...)
     |      x.__lt__(y) <==> x<y
     |  
     |  __ne__(...)
     |      x.__ne__(y) <==> x!=y
     |  
     |  __nonzero__(...)
     |      x.__nonzero__() <==> x != 0
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __setattr__(...)
     |      x.__setattr__('name', value) <==> x.name = value
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __new__ = <built-in method __new__ of PythonQt.PythonQtClassWrapper ob...
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
    
    class QMimeDatabase(PythonQt.PythonQtInstanceWrapper)
     |  Method resolution order:
     |      QMimeDatabase
     |      PythonQt.PythonQtInstanceWrapper
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  __init__(...)
     |      x.__init__(...) initializes x; see help(type(x)) for signature
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  MatchContent = 2
     |  
     |  MatchDefault = 0
     |  
     |  MatchExtension = 1
     |  
     |  MatchMode = <class 'PythonQt.QtCore.MatchMode'>
     |  
     |  
     |  allMimeTypes = <unbound qt slot allMimeTypes of QMimeDatabase type>
     |      X.allMimeTypes(a) -> tuple
     |  
     |  className = <built-in method className of PythonQt.PythonQtClassWrappe...
     |      Return the classname of the object
     |  
     |  delete = <built-in method delete of PythonQt.PythonQtClassWrapper obje...
     |      Deletes the given C++ object
     |  
     |  help = <built-in method help of PythonQt.PythonQtClassWrapper object>
     |      Shows the help of available methods for this class
     |  
     |  inherits = <built-in method inherits of PythonQt.PythonQtClassWrapper ...
     |      Returns if the class inherits or is of given type name
     |  
     |  mimeTypeForData = <unbound qt slot mimeTypeForData of QMimeDatabase ty...
     |      X.mimeTypeForData(a, b) -> PythonQt.QtCore.QMimeType
     |  
     |  mimeTypeForFile = <unbound qt slot mimeTypeForFile of QMimeDatabase ty...
     |      X.mimeTypeForFile(a, b, c) -> PythonQt.QtCore.QMimeType
     |  
     |  mimeTypeForFileNameAndData = <unbound qt slot mimeTypeForFileNameAndDa...
     |      X.mimeTypeForFileNameAndData(a, b, c) -> PythonQt.QtCore.QMimeType
     |  
     |  mimeTypeForName = <unbound qt slot mimeTypeForName of QMimeDatabase ty...
     |      X.mimeTypeForName(a, b) -> PythonQt.QtCore.QMimeType
     |  
     |  mimeTypeForUrl = <unbound qt slot mimeTypeForUrl of QMimeDatabase type...
     |      X.mimeTypeForUrl(a, b) -> PythonQt.QtCore.QMimeType
     |  
     |  mimeTypesForFileName = <unbound qt slot mimeTypesForFileName of QMimeD...
     |      X.mimeTypesForFileName(a, b) -> tuple
     |  
     |  suffixForFileName = <unbound qt slot suffixForFileName of QMimeDatabas...
     |      X.suffixForFileName(a, b) -> str
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __delattr__(...)
     |      x.__delattr__('name') <==> del x.name
     |  
     |  __eq__(...)
     |      x.__eq__(y) <==> x==y
     |  
     |  __ge__(...)
     |      x.__ge__(y) <==> x>=y
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __gt__(...)
     |      x.__gt__(y) <==> x>y
     |  
     |  __hash__(...)
     |      x.__hash__() <==> hash(x)
     |  
     |  __le__(...)
     |      x.__le__(y) <==> x<=y
     |  
     |  __lt__(...)
     |      x.__lt__(y) <==> x<y
     |  
     |  __ne__(...)
     |      x.__ne__(y) <==> x!=y
     |  
     |  __nonzero__(...)
     |      x.__nonzero__() <==> x != 0
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __setattr__(...)
     |      x.__setattr__('name', value) <==> x.name = value
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __new__ = <built-in method __new__ of PythonQt.PythonQtClassWrapper ob...
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
    
    class QMimeType(PythonQt.PythonQtInstanceWrapper)
     |  Method resolution order:
     |      QMimeType
     |      PythonQt.PythonQtInstanceWrapper
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  __eq__(...)
     |      x.__eq__(y) <==> x==y
     |  
     |  __init__(...)
     |      x.__init__(...) initializes x; see help(type(x)) for signature
     |  
     |  __ne__(...)
     |      x.__ne__(y) <==> x!=y
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  aliases = <unbound qt slot aliases of QMimeType type>
     |      X.aliases(a) -> tuple
     |  
     |  allAncestors = <unbound qt slot allAncestors of QMimeType type>
     |      X.allAncestors(a) -> tuple
     |  
     |  className = <built-in method className of PythonQt.PythonQtClassWrappe...
     |      Return the classname of the object
     |  
     |  comment = <unbound qt slot comment of QMimeType type>
     |      X.comment(a) -> str
     |  
     |  delete = <built-in method delete of PythonQt.PythonQtClassWrapper obje...
     |      Deletes the given C++ object
     |  
     |  filterString = <unbound qt slot filterString of QMimeType type>
     |      X.filterString(a) -> str
     |  
     |  genericIconName = <unbound qt slot genericIconName of QMimeType type>
     |      X.genericIconName(a) -> str
     |  
     |  globPatterns = <unbound qt slot globPatterns of QMimeType type>
     |      X.globPatterns(a) -> tuple
     |  
     |  help = <built-in method help of PythonQt.PythonQtClassWrapper object>
     |      Shows the help of available methods for this class
     |  
     |  iconName = <unbound qt slot iconName of QMimeType type>
     |      X.iconName(a) -> str
     |  
     |  inherits = <unbound qt slot inherits of QMimeType type>
     |      X.inherits(a, b) -> bool
     |  
     |  isDefault = <unbound qt slot isDefault of QMimeType type>
     |      X.isDefault(a) -> bool
     |  
     |  isValid = <unbound qt slot isValid of QMimeType type>
     |      X.isValid(a) -> bool
     |  
     |  name = <unbound qt slot name of QMimeType type>
     |      X.name(a) -> str
     |  
     |  operator_assign = <unbound qt slot operator_assign of QMimeType type>
     |      X.operator_assign(a, b) -> PythonQt.QtCore.QMimeType
     |  
     |  parentMimeTypes = <unbound qt slot parentMimeTypes of QMimeType type>
     |      X.parentMimeTypes(a) -> tuple
     |  
     |  preferredSuffix = <unbound qt slot preferredSuffix of QMimeType type>
     |      X.preferredSuffix(a) -> str
     |  
     |  suffixes = <unbound qt slot suffixes of QMimeType type>
     |      X.suffixes(a) -> tuple
     |  
     |  swap = <unbound qt slot swap of QMimeType type>
     |      X.swap(a, b)
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __delattr__(...)
     |      x.__delattr__('name') <==> del x.name
     |  
     |  __ge__(...)
     |      x.__ge__(y) <==> x>=y
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __gt__(...)
     |      x.__gt__(y) <==> x>y
     |  
     |  __hash__(...)
     |      x.__hash__() <==> hash(x)
     |  
     |  __le__(...)
     |      x.__le__(y) <==> x<=y
     |  
     |  __lt__(...)
     |      x.__lt__(y) <==> x<y
     |  
     |  __nonzero__(...)
     |      x.__nonzero__() <==> x != 0
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __setattr__(...)
     |      x.__setattr__('name', value) <==> x.name = value
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __new__ = <built-in method __new__ of PythonQt.PythonQtClassWrapper ob...
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
    
    class QModelIndex(PythonQt.PythonQtInstanceWrapper)
     |  Method resolution order:
     |      QModelIndex
     |      PythonQt.PythonQtInstanceWrapper
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  __eq__(...)
     |      x.__eq__(y) <==> x==y
     |  
     |  __init__(...)
     |      x.__init__(...) initializes x; see help(type(x)) for signature
     |  
     |  __lt__(...)
     |      x.__lt__(y) <==> x<y
     |  
     |  __ne__(...)
     |      x.__ne__(y) <==> x!=y
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  child = <unbound qt slot child of QModelIndex type>
     |      X.child(a, b, c) -> PythonQt.QtCore.QModelIndex
     |  
     |  className = <built-in method className of PythonQt.PythonQtClassWrappe...
     |      Return the classname of the object
     |  
     |  column = <unbound qt slot column of QModelIndex type>
     |      X.column(a) -> int
     |  
     |  data = <unbound qt slot data of QModelIndex type>
     |      X.data(a, b) -> object
     |  
     |  delete = <built-in method delete of PythonQt.PythonQtClassWrapper obje...
     |      Deletes the given C++ object
     |  
     |  flags = <unbound qt slot flags of QModelIndex type>
     |      X.flags(a)
     |  
     |  help = <built-in method help of PythonQt.PythonQtClassWrapper object>
     |      Shows the help of available methods for this class
     |  
     |  inherits = <built-in method inherits of PythonQt.PythonQtClassWrapper ...
     |      Returns if the class inherits or is of given type name
     |  
     |  internalId = <unbound qt slot internalId of QModelIndex type>
     |      X.internalId(a)
     |  
     |  internalPointer = <unbound qt slot internalPointer of QModelIndex type...
     |      X.internalPointer(a)
     |  
     |  isValid = <unbound qt slot isValid of QModelIndex type>
     |      X.isValid(a) -> bool
     |  
     |  model = <unbound qt slot model of QModelIndex type>
     |      X.model(a) -> PythonQt.QtCore.QAbstractItemModel
     |  
     |  parent = <unbound qt slot parent of QModelIndex type>
     |      X.parent(a) -> PythonQt.QtCore.QModelIndex
     |  
     |  row = <unbound qt slot row of QModelIndex type>
     |      X.row(a) -> int
     |  
     |  sibling = <unbound qt slot sibling of QModelIndex type>
     |      X.sibling(a, b, c) -> PythonQt.QtCore.QModelIndex
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __delattr__(...)
     |      x.__delattr__('name') <==> del x.name
     |  
     |  __ge__(...)
     |      x.__ge__(y) <==> x>=y
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __gt__(...)
     |      x.__gt__(y) <==> x>y
     |  
     |  __hash__(...)
     |      x.__hash__() <==> hash(x)
     |  
     |  __le__(...)
     |      x.__le__(y) <==> x<=y
     |  
     |  __nonzero__(...)
     |      x.__nonzero__() <==> x != 0
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __setattr__(...)
     |      x.__setattr__('name', value) <==> x.name = value
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __new__ = <built-in method __new__ of PythonQt.PythonQtClassWrapper ob...
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
    
    class QMutex(PythonQt.PythonQtInstanceWrapper)
     |  Method resolution order:
     |      QMutex
     |      PythonQt.PythonQtInstanceWrapper
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  __init__(...)
     |      x.__init__(...) initializes x; see help(type(x)) for signature
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  NonRecursive = 0
     |  
     |  RecursionMode = <class 'PythonQt.QtCore.RecursionMode'>
     |  
     |  
     |  Recursive = 1
     |  
     |  className = <built-in method className of PythonQt.PythonQtClassWrappe...
     |      Return the classname of the object
     |  
     |  delete = <built-in method delete of PythonQt.PythonQtClassWrapper obje...
     |      Deletes the given C++ object
     |  
     |  help = <built-in method help of PythonQt.PythonQtClassWrapper object>
     |      Shows the help of available methods for this class
     |  
     |  inherits = <built-in method inherits of PythonQt.PythonQtClassWrapper ...
     |      Returns if the class inherits or is of given type name
     |  
     |  isRecursive = <unbound qt slot isRecursive of QMutex type>
     |      X.isRecursive(a) -> bool
     |  
     |  lock = <unbound qt slot lock of QMutex type>
     |      X.lock(a)
     |  
     |  tryLock = <unbound qt slot tryLock of QMutex type>
     |      X.tryLock(a, b) -> bool
     |  
     |  unlock = <unbound qt slot unlock of QMutex type>
     |      X.unlock(a)
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __delattr__(...)
     |      x.__delattr__('name') <==> del x.name
     |  
     |  __eq__(...)
     |      x.__eq__(y) <==> x==y
     |  
     |  __ge__(...)
     |      x.__ge__(y) <==> x>=y
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __gt__(...)
     |      x.__gt__(y) <==> x>y
     |  
     |  __hash__(...)
     |      x.__hash__() <==> hash(x)
     |  
     |  __le__(...)
     |      x.__le__(y) <==> x<=y
     |  
     |  __lt__(...)
     |      x.__lt__(y) <==> x<y
     |  
     |  __ne__(...)
     |      x.__ne__(y) <==> x!=y
     |  
     |  __nonzero__(...)
     |      x.__nonzero__() <==> x != 0
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __setattr__(...)
     |      x.__setattr__('name', value) <==> x.name = value
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __new__ = <built-in method __new__ of PythonQt.PythonQtClassWrapper ob...
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
    
    class QParallelAnimationGroup(PythonQt.PythonQtInstanceWrapper)
     |  Method resolution order:
     |      QParallelAnimationGroup
     |      PythonQt.PythonQtInstanceWrapper
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  __init__(...)
     |      x.__init__(...) initializes x; see help(type(x)) for signature
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  Backward = 1
     |  
     |  DeleteWhenStopped = 1
     |  
     |  DeletionPolicy = <class 'PythonQt.QtCore.DeletionPolicy'>
     |  
     |  
     |  Direction = <class 'PythonQt.QtCore.Direction'>
     |  
     |  
     |  Forward = 0
     |  
     |  KeepWhenStopped = 0
     |  
     |  Paused = 1
     |  
     |  Running = 2
     |  
     |  State = <class 'PythonQt.QtCore.State'>
     |  
     |  
     |  Stopped = 0
     |  
     |  addAnimation = <unbound qt slot addAnimation of QParallelAnimationGrou...
     |      X.addAnimation(a, b)
     |  
     |  animationAt = <unbound qt slot animationAt of QParallelAnimationGroup ...
     |      X.animationAt(a, b) -> PythonQt.QtCore.QAbstractAnimation
     |  
     |  animationCount = <unbound qt slot animationCount of QParallelAnimation...
     |      X.animationCount(a) -> int
     |  
     |  blockSignals = <unbound qt slot blockSignals of QParallelAnimationGrou...
     |      X.blockSignals(a, b) -> bool
     |  
     |  childEvent = <unbound qt slot py_q_childEvent of QParallelAnimationGro...
     |      X.childEvent(a, b)
     |  
     |  children = <unbound qt slot children of QParallelAnimationGroup type>
     |      X.children(a) -> tuple
     |  
     |  className = <built-in method className of PythonQt.PythonQtClassWrappe...
     |      Return the classname of the object
     |  
     |  clear = <unbound qt slot clear of QParallelAnimationGroup type>
     |      X.clear(a)
     |  
     |  connect = <unbound qt slot connect of QParallelAnimationGroup type>
     |      X.connect(a, b, c, d, e) -> bool
     |  
     |  currentLoop = None
     |  
     |  currentLoopChanged = <unbound qt signal currentLoopChanged of QParalle...
     |  
     |  
     |  currentLoopTime = <unbound qt slot currentLoopTime of QParallelAnimati...
     |      X.currentLoopTime(a) -> int
     |  
     |  currentTime = None
     |  
     |  customEvent = <unbound qt slot py_q_customEvent of QParallelAnimationG...
     |      X.customEvent(a, b)
     |  
     |  delete = <built-in method delete of PythonQt.PythonQtClassWrapper obje...
     |      Deletes the given C++ object
     |  
     |  deleteLater = <unbound qt slot deleteLater of QParallelAnimationGroup ...
     |      X.deleteLater()
     |  
     |  destroyed = <unbound qt signal destroyed of QParallelAnimationGroup ty...
     |  
     |  
     |  direction = None
     |  
     |  directionChanged = <unbound qt signal directionChanged of QParallelAni...
     |  
     |  
     |  disconnect = <unbound qt slot disconnect of QParallelAnimationGroup ty...
     |      X.disconnect(a, b, c, d) -> bool
     |  
     |  dumpObjectInfo = <unbound qt slot dumpObjectInfo of QParallelAnimation...
     |      X.dumpObjectInfo(a)
     |  
     |  dumpObjectTree = <unbound qt slot dumpObjectTree of QParallelAnimation...
     |      X.dumpObjectTree(a)
     |  
     |  duration = None
     |  
     |  dynamicPropertyNames = <unbound qt slot dynamicPropertyNames of QParal...
     |      X.dynamicPropertyNames(a)
     |  
     |  event = <unbound qt slot py_q_event of QParallelAnimationGroup type>
     |      X.event(a, b) -> bool
     |  
     |  eventFilter = <unbound qt slot py_q_eventFilter of QParallelAnimationG...
     |      X.eventFilter(a, b, c) -> bool
     |  
     |  findChild = <unbound qt slot findChild of QParallelAnimationGroup type...
     |      X.findChild(a, b, c) -> PythonQt.private.QObject
     |  
     |  findChildren = <unbound qt slot findChildren of QParallelAnimationGrou...
     |      X.findChildren(a, b, c) -> tuple
     |  
     |  finished = <unbound qt signal finished of QParallelAnimationGroup type...
     |  
     |  
     |  group = <unbound qt slot group of QParallelAnimationGroup type>
     |      X.group(a) -> PythonQt.QtCore.QAnimationGroup
     |  
     |  help = <built-in method help of PythonQt.PythonQtClassWrapper object>
     |      Shows the help of available methods for this class
     |  
     |  indexOfAnimation = <unbound qt slot indexOfAnimation of QParallelAnima...
     |      X.indexOfAnimation(a, b) -> int
     |  
     |  inherits = <built-in method inherits of PythonQt.PythonQtClassWrapper ...
     |      Returns if the class inherits or is of given type name
     |  
     |  insertAnimation = <unbound qt slot insertAnimation of QParallelAnimati...
     |      X.insertAnimation(a, b, c)
     |  
     |  installEventFilter = <unbound qt slot installEventFilter of QParallelA...
     |      X.installEventFilter(a, b)
     |  
     |  isSignalConnected = <unbound qt slot isSignalConnected of QParallelAni...
     |      X.isSignalConnected(a, b) -> bool
     |  
     |  isWidgetType = <unbound qt slot isWidgetType of QParallelAnimationGrou...
     |      X.isWidgetType(a) -> bool
     |  
     |  isWindowType = <unbound qt slot isWindowType of QParallelAnimationGrou...
     |      X.isWindowType(a) -> bool
     |  
     |  killTimer = <unbound qt slot killTimer of QParallelAnimationGroup type...
     |      X.killTimer(a, b)
     |  
     |  loopCount = None
     |  
     |  metaObject = <unbound qt slot metaObject of QParallelAnimationGroup ty...
     |      X.metaObject(a) -> PythonQt.QtCore.QMetaObject
     |  
     |  moveToThread = <unbound qt slot moveToThread of QParallelAnimationGrou...
     |      X.moveToThread(a, b)
     |  
     |  objectName = None
     |  
     |  objectNameChanged = <unbound qt signal objectNameChanged of QParallelA...
     |  
     |  
     |  parent = <unbound qt slot parent of QParallelAnimationGroup type>
     |      X.parent(a) -> PythonQt.private.QObject
     |  
     |  pause = <unbound qt slot pause of QParallelAnimationGroup type>
     |      X.pause()
     |  
     |  property = <unbound qt slot property of QParallelAnimationGroup type>
     |      X.property(a, b) -> object
     |  
     |  removeAnimation = <unbound qt slot removeAnimation of QParallelAnimati...
     |      X.removeAnimation(a, b)
     |  
     |  removeEventFilter = <unbound qt slot removeEventFilter of QParallelAni...
     |      X.removeEventFilter(a, b)
     |  
     |  resume = <unbound qt slot resume of QParallelAnimationGroup type>
     |      X.resume()
     |  
     |  sender = <unbound qt slot sender of QParallelAnimationGroup type>
     |      X.sender(a) -> PythonQt.private.QObject
     |  
     |  senderSignalIndex = <unbound qt slot senderSignalIndex of QParallelAni...
     |      X.senderSignalIndex(a) -> int
     |  
     |  setCurrentTime = <unbound qt slot setCurrentTime of QParallelAnimation...
     |      X.setCurrentTime(a)
     |  
     |  setDirection = <unbound qt slot setDirection of QParallelAnimationGrou...
     |      X.setDirection(a, b)
     |  
     |  setLoopCount = <unbound qt slot setLoopCount of QParallelAnimationGrou...
     |      X.setLoopCount(a, b)
     |  
     |  setObjectName = <unbound qt slot setObjectName of QParallelAnimationGr...
     |      X.setObjectName(a, b)
     |  
     |  setParent = <unbound qt slot setParent of QParallelAnimationGroup type...
     |      X.setParent(a, b)
     |  
     |  setPaused = <unbound qt slot setPaused of QParallelAnimationGroup type...
     |      X.setPaused(a)
     |  
     |  setProperty = <unbound qt slot setProperty of QParallelAnimationGroup ...
     |      X.setProperty(a, b, c) -> bool
     |  
     |  signalsBlocked = <unbound qt slot signalsBlocked of QParallelAnimation...
     |      X.signalsBlocked(a) -> bool
     |  
     |  start = <unbound qt slot start of QParallelAnimationGroup type>
     |      X.start(a)
     |  
     |  startTimer = <unbound qt slot startTimer of QParallelAnimationGroup ty...
     |      X.startTimer(a, b, c) -> int
     |  
     |  state = None
     |  
     |  stateChanged = <unbound qt signal stateChanged of QParallelAnimationGr...
     |  
     |  
     |  stop = <unbound qt slot stop of QParallelAnimationGroup type>
     |      X.stop()
     |  
     |  takeAnimation = <unbound qt slot takeAnimation of QParallelAnimationGr...
     |      X.takeAnimation(a, b) -> PythonQt.QtCore.QAbstractAnimation
     |  
     |  thread = <unbound qt slot thread of QParallelAnimationGroup type>
     |      X.thread(a)
     |  
     |  timerEvent = <unbound qt slot py_q_timerEvent of QParallelAnimationGro...
     |      X.timerEvent(a, b)
     |  
     |  totalDuration = <unbound qt slot totalDuration of QParallelAnimationGr...
     |      X.totalDuration(a) -> int
     |  
     |  tr = <unbound qt slot tr of QParallelAnimationGroup type>
     |      X.tr(a, b, c, d) -> str
     |  
     |  updateCurrentTime = <unbound qt slot py_q_updateCurrentTime of QParall...
     |      X.updateCurrentTime(a, b)
     |  
     |  updateDirection = <unbound qt slot py_q_updateDirection of QParallelAn...
     |      X.updateDirection(a, b)
     |  
     |  updateState = <unbound qt slot py_q_updateState of QParallelAnimationG...
     |      X.updateState(a, b, c)
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __delattr__(...)
     |      x.__delattr__('name') <==> del x.name
     |  
     |  __eq__(...)
     |      x.__eq__(y) <==> x==y
     |  
     |  __ge__(...)
     |      x.__ge__(y) <==> x>=y
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __gt__(...)
     |      x.__gt__(y) <==> x>y
     |  
     |  __hash__(...)
     |      x.__hash__() <==> hash(x)
     |  
     |  __le__(...)
     |      x.__le__(y) <==> x<=y
     |  
     |  __lt__(...)
     |      x.__lt__(y) <==> x<y
     |  
     |  __ne__(...)
     |      x.__ne__(y) <==> x!=y
     |  
     |  __nonzero__(...)
     |      x.__nonzero__() <==> x != 0
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __setattr__(...)
     |      x.__setattr__('name', value) <==> x.name = value
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __new__ = <built-in method __new__ of PythonQt.PythonQtClassWrapper ob...
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
    
    class QPauseAnimation(PythonQt.PythonQtInstanceWrapper)
     |  Method resolution order:
     |      QPauseAnimation
     |      PythonQt.PythonQtInstanceWrapper
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  __init__(...)
     |      x.__init__(...) initializes x; see help(type(x)) for signature
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  Backward = 1
     |  
     |  DeleteWhenStopped = 1
     |  
     |  DeletionPolicy = <class 'PythonQt.QtCore.DeletionPolicy'>
     |  
     |  
     |  Direction = <class 'PythonQt.QtCore.Direction'>
     |  
     |  
     |  Forward = 0
     |  
     |  KeepWhenStopped = 0
     |  
     |  Paused = 1
     |  
     |  Running = 2
     |  
     |  State = <class 'PythonQt.QtCore.State'>
     |  
     |  
     |  Stopped = 0
     |  
     |  blockSignals = <unbound qt slot blockSignals of QPauseAnimation type>
     |      X.blockSignals(a, b) -> bool
     |  
     |  childEvent = <unbound qt slot py_q_childEvent of QPauseAnimation type>
     |      X.childEvent(a, b)
     |  
     |  children = <unbound qt slot children of QPauseAnimation type>
     |      X.children(a) -> tuple
     |  
     |  className = <built-in method className of PythonQt.PythonQtClassWrappe...
     |      Return the classname of the object
     |  
     |  connect = <unbound qt slot connect of QPauseAnimation type>
     |      X.connect(a, b, c, d, e) -> bool
     |  
     |  currentLoop = None
     |  
     |  currentLoopChanged = <unbound qt signal currentLoopChanged of QPauseAn...
     |  
     |  
     |  currentLoopTime = <unbound qt slot currentLoopTime of QPauseAnimation ...
     |      X.currentLoopTime(a) -> int
     |  
     |  currentTime = None
     |  
     |  customEvent = <unbound qt slot py_q_customEvent of QPauseAnimation typ...
     |      X.customEvent(a, b)
     |  
     |  delete = <built-in method delete of PythonQt.PythonQtClassWrapper obje...
     |      Deletes the given C++ object
     |  
     |  deleteLater = <unbound qt slot deleteLater of QPauseAnimation type>
     |      X.deleteLater()
     |  
     |  destroyed = <unbound qt signal destroyed of QPauseAnimation type>
     |  
     |  
     |  direction = None
     |  
     |  directionChanged = <unbound qt signal directionChanged of QPauseAnimat...
     |  
     |  
     |  disconnect = <unbound qt slot disconnect of QPauseAnimation type>
     |      X.disconnect(a, b, c, d) -> bool
     |  
     |  dumpObjectInfo = <unbound qt slot dumpObjectInfo of QPauseAnimation ty...
     |      X.dumpObjectInfo(a)
     |  
     |  dumpObjectTree = <unbound qt slot dumpObjectTree of QPauseAnimation ty...
     |      X.dumpObjectTree(a)
     |  
     |  duration = None
     |  
     |  dynamicPropertyNames = <unbound qt slot dynamicPropertyNames of QPause...
     |      X.dynamicPropertyNames(a)
     |  
     |  event = <unbound qt slot py_q_event of QPauseAnimation type>
     |      X.event(a, b) -> bool
     |  
     |  eventFilter = <unbound qt slot py_q_eventFilter of QPauseAnimation typ...
     |      X.eventFilter(a, b, c) -> bool
     |  
     |  findChild = <unbound qt slot findChild of QPauseAnimation type>
     |      X.findChild(a, b, c) -> PythonQt.private.QObject
     |  
     |  findChildren = <unbound qt slot findChildren of QPauseAnimation type>
     |      X.findChildren(a, b, c) -> tuple
     |  
     |  finished = <unbound qt signal finished of QPauseAnimation type>
     |  
     |  
     |  group = <unbound qt slot group of QPauseAnimation type>
     |      X.group(a) -> PythonQt.QtCore.QAnimationGroup
     |  
     |  help = <built-in method help of PythonQt.PythonQtClassWrapper object>
     |      Shows the help of available methods for this class
     |  
     |  inherits = <built-in method inherits of PythonQt.PythonQtClassWrapper ...
     |      Returns if the class inherits or is of given type name
     |  
     |  installEventFilter = <unbound qt slot installEventFilter of QPauseAnim...
     |      X.installEventFilter(a, b)
     |  
     |  isSignalConnected = <unbound qt slot isSignalConnected of QPauseAnimat...
     |      X.isSignalConnected(a, b) -> bool
     |  
     |  isWidgetType = <unbound qt slot isWidgetType of QPauseAnimation type>
     |      X.isWidgetType(a) -> bool
     |  
     |  isWindowType = <unbound qt slot isWindowType of QPauseAnimation type>
     |      X.isWindowType(a) -> bool
     |  
     |  killTimer = <unbound qt slot killTimer of QPauseAnimation type>
     |      X.killTimer(a, b)
     |  
     |  loopCount = None
     |  
     |  metaObject = <unbound qt slot metaObject of QPauseAnimation type>
     |      X.metaObject(a) -> PythonQt.QtCore.QMetaObject
     |  
     |  moveToThread = <unbound qt slot moveToThread of QPauseAnimation type>
     |      X.moveToThread(a, b)
     |  
     |  objectName = None
     |  
     |  objectNameChanged = <unbound qt signal objectNameChanged of QPauseAnim...
     |  
     |  
     |  parent = <unbound qt slot parent of QPauseAnimation type>
     |      X.parent(a) -> PythonQt.private.QObject
     |  
     |  pause = <unbound qt slot pause of QPauseAnimation type>
     |      X.pause()
     |  
     |  property = <unbound qt slot property of QPauseAnimation type>
     |      X.property(a, b) -> object
     |  
     |  removeEventFilter = <unbound qt slot removeEventFilter of QPauseAnimat...
     |      X.removeEventFilter(a, b)
     |  
     |  resume = <unbound qt slot resume of QPauseAnimation type>
     |      X.resume()
     |  
     |  sender = <unbound qt slot sender of QPauseAnimation type>
     |      X.sender(a) -> PythonQt.private.QObject
     |  
     |  senderSignalIndex = <unbound qt slot senderSignalIndex of QPauseAnimat...
     |      X.senderSignalIndex(a) -> int
     |  
     |  setCurrentTime = <unbound qt slot setCurrentTime of QPauseAnimation ty...
     |      X.setCurrentTime(a)
     |  
     |  setDirection = <unbound qt slot setDirection of QPauseAnimation type>
     |      X.setDirection(a, b)
     |  
     |  setDuration = <unbound qt slot setDuration of QPauseAnimation type>
     |      X.setDuration(a, b)
     |  
     |  setLoopCount = <unbound qt slot setLoopCount of QPauseAnimation type>
     |      X.setLoopCount(a, b)
     |  
     |  setObjectName = <unbound qt slot setObjectName of QPauseAnimation type...
     |      X.setObjectName(a, b)
     |  
     |  setParent = <unbound qt slot setParent of QPauseAnimation type>
     |      X.setParent(a, b)
     |  
     |  setPaused = <unbound qt slot setPaused of QPauseAnimation type>
     |      X.setPaused(a)
     |  
     |  setProperty = <unbound qt slot setProperty of QPauseAnimation type>
     |      X.setProperty(a, b, c) -> bool
     |  
     |  signalsBlocked = <unbound qt slot signalsBlocked of QPauseAnimation ty...
     |      X.signalsBlocked(a) -> bool
     |  
     |  start = <unbound qt slot start of QPauseAnimation type>
     |      X.start(a)
     |  
     |  startTimer = <unbound qt slot startTimer of QPauseAnimation type>
     |      X.startTimer(a, b, c) -> int
     |  
     |  state = None
     |  
     |  stateChanged = <unbound qt signal stateChanged of QPauseAnimation type...
     |  
     |  
     |  stop = <unbound qt slot stop of QPauseAnimation type>
     |      X.stop()
     |  
     |  thread = <unbound qt slot thread of QPauseAnimation type>
     |      X.thread(a)
     |  
     |  timerEvent = <unbound qt slot py_q_timerEvent of QPauseAnimation type>
     |      X.timerEvent(a, b)
     |  
     |  totalDuration = <unbound qt slot totalDuration of QPauseAnimation type...
     |      X.totalDuration(a) -> int
     |  
     |  tr = <unbound qt slot tr of QPauseAnimation type>
     |      X.tr(a, b, c, d) -> str
     |  
     |  updateCurrentTime = <unbound qt slot py_q_updateCurrentTime of QPauseA...
     |      X.updateCurrentTime(a, b)
     |  
     |  updateDirection = <unbound qt slot py_q_updateDirection of QPauseAnima...
     |      X.updateDirection(a, b)
     |  
     |  updateState = <unbound qt slot py_q_updateState of QPauseAnimation typ...
     |      X.updateState(a, b, c)
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __delattr__(...)
     |      x.__delattr__('name') <==> del x.name
     |  
     |  __eq__(...)
     |      x.__eq__(y) <==> x==y
     |  
     |  __ge__(...)
     |      x.__ge__(y) <==> x>=y
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __gt__(...)
     |      x.__gt__(y) <==> x>y
     |  
     |  __hash__(...)
     |      x.__hash__() <==> hash(x)
     |  
     |  __le__(...)
     |      x.__le__(y) <==> x<=y
     |  
     |  __lt__(...)
     |      x.__lt__(y) <==> x<y
     |  
     |  __ne__(...)
     |      x.__ne__(y) <==> x!=y
     |  
     |  __nonzero__(...)
     |      x.__nonzero__() <==> x != 0
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __setattr__(...)
     |      x.__setattr__('name', value) <==> x.name = value
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __new__ = <built-in method __new__ of PythonQt.PythonQtClassWrapper ob...
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
    
    class QPersistentModelIndex(PythonQt.PythonQtInstanceWrapper)
     |  Method resolution order:
     |      QPersistentModelIndex
     |      PythonQt.PythonQtInstanceWrapper
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  __eq__(...)
     |      x.__eq__(y) <==> x==y
     |  
     |  __init__(...)
     |      x.__init__(...) initializes x; see help(type(x)) for signature
     |  
     |  __lt__(...)
     |      x.__lt__(y) <==> x<y
     |  
     |  __ne__(...)
     |      x.__ne__(y) <==> x!=y
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  child = <unbound qt slot child of QPersistentModelIndex type>
     |      X.child(a, b, c) -> PythonQt.QtCore.QModelIndex
     |  
     |  className = <built-in method className of PythonQt.PythonQtClassWrappe...
     |      Return the classname of the object
     |  
     |  column = <unbound qt slot column of QPersistentModelIndex type>
     |      X.column(a) -> int
     |  
     |  data = <unbound qt slot data of QPersistentModelIndex type>
     |      X.data(a, b) -> object
     |  
     |  delete = <built-in method delete of PythonQt.PythonQtClassWrapper obje...
     |      Deletes the given C++ object
     |  
     |  flags = <unbound qt slot flags of QPersistentModelIndex type>
     |      X.flags(a)
     |  
     |  help = <built-in method help of PythonQt.PythonQtClassWrapper object>
     |      Shows the help of available methods for this class
     |  
     |  inherits = <built-in method inherits of PythonQt.PythonQtClassWrapper ...
     |      Returns if the class inherits or is of given type name
     |  
     |  internalId = <unbound qt slot internalId of QPersistentModelIndex type...
     |      X.internalId(a)
     |  
     |  isValid = <unbound qt slot isValid of QPersistentModelIndex type>
     |      X.isValid(a) -> bool
     |  
     |  model = <unbound qt slot model of QPersistentModelIndex type>
     |      X.model(a) -> PythonQt.QtCore.QAbstractItemModel
     |  
     |  operator_cast_QModelIndex = <unbound qt slot operator_cast_QModelIndex...
     |      X.operator_cast_QModelIndex(a) -> PythonQt.QtCore.QModelIndex
     |  
     |  parent = <unbound qt slot parent of QPersistentModelIndex type>
     |      X.parent(a) -> PythonQt.QtCore.QModelIndex
     |  
     |  row = <unbound qt slot row of QPersistentModelIndex type>
     |      X.row(a) -> int
     |  
     |  sibling = <unbound qt slot sibling of QPersistentModelIndex type>
     |      X.sibling(a, b, c) -> PythonQt.QtCore.QModelIndex
     |  
     |  swap = <unbound qt slot swap of QPersistentModelIndex type>
     |      X.swap(a, b)
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __delattr__(...)
     |      x.__delattr__('name') <==> del x.name
     |  
     |  __ge__(...)
     |      x.__ge__(y) <==> x>=y
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __gt__(...)
     |      x.__gt__(y) <==> x>y
     |  
     |  __hash__(...)
     |      x.__hash__() <==> hash(x)
     |  
     |  __le__(...)
     |      x.__le__(y) <==> x<=y
     |  
     |  __nonzero__(...)
     |      x.__nonzero__() <==> x != 0
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __setattr__(...)
     |      x.__setattr__('name', value) <==> x.name = value
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __new__ = <built-in method __new__ of PythonQt.PythonQtClassWrapper ob...
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
    
    class QPoint(PythonQt.PythonQtInstanceWrapper)
     |  Method resolution order:
     |      QPoint
     |      PythonQt.PythonQtInstanceWrapper
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  __add__(...)
     |      x.__add__(y) <==> x+y
     |  
     |  __div__(...)
     |      x.__div__(y) <==> x/y
     |  
     |  __eq__(...)
     |      x.__eq__(y) <==> x==y
     |  
     |  __iadd__(...)
     |      x.__iadd__(y) <==> x+=y
     |  
     |  __idiv__(...)
     |      x.__idiv__(y) <==> x/=y
     |  
     |  __imul__(...)
     |      x.__imul__(y) <==> x*=y
     |  
     |  __init__(...)
     |      x.__init__(...) initializes x; see help(type(x)) for signature
     |  
     |  __isub__(...)
     |      x.__isub__(y) <==> x-=y
     |  
     |  __itruediv__(...)
     |      x.__itruediv__(y) <==> x/=y
     |  
     |  __mul__(...)
     |      x.__mul__(y) <==> x*y
     |  
     |  __neg__(...)
     |      x.__neg__() <==> -x
     |  
     |  __nonzero__(...)
     |      x.__nonzero__() <==> x != 0
     |  
     |  __radd__(...)
     |      x.__radd__(y) <==> y+x
     |  
     |  __rdiv__(...)
     |      x.__rdiv__(y) <==> y/x
     |  
     |  __rmul__(...)
     |      x.__rmul__(y) <==> y*x
     |  
     |  __rsub__(...)
     |      x.__rsub__(y) <==> y-x
     |  
     |  __rtruediv__(...)
     |      x.__rtruediv__(y) <==> y/x
     |  
     |  __sub__(...)
     |      x.__sub__(y) <==> x-y
     |  
     |  __truediv__(...)
     |      x.__truediv__(y) <==> x/y
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  className = <built-in method className of PythonQt.PythonQtClassWrappe...
     |      Return the classname of the object
     |  
     |  delete = <built-in method delete of PythonQt.PythonQtClassWrapper obje...
     |      Deletes the given C++ object
     |  
     |  dotProduct = <unbound qt slot static_QPoint_dotProduct of QPoint type>
     |      X.dotProduct(a, b) -> int
     |  
     |  help = <built-in method help of PythonQt.PythonQtClassWrapper object>
     |      Shows the help of available methods for this class
     |  
     |  inherits = <built-in method inherits of PythonQt.PythonQtClassWrapper ...
     |      Returns if the class inherits or is of given type name
     |  
     |  isNull = <unbound qt slot isNull of QPoint type>
     |      X.isNull(a) -> bool
     |  
     |  manhattanLength = <unbound qt slot manhattanLength of QPoint type>
     |      X.manhattanLength(a) -> int
     |  
     |  readFrom = <unbound qt slot readFrom of QPoint type>
     |      X.readFrom(a, b)
     |  
     |  setX = <unbound qt slot setX of QPoint type>
     |      X.setX(a, b)
     |  
     |  setY = <unbound qt slot setY of QPoint type>
     |      X.setY(a, b)
     |  
     |  writeTo = <unbound qt slot writeTo of QPoint type>
     |      X.writeTo(a, b)
     |  
     |  x = <unbound qt slot x of QPoint type>
     |      X.x(a) -> int
     |  
     |  y = <unbound qt slot y of QPoint type>
     |      X.y(a) -> int
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __delattr__(...)
     |      x.__delattr__('name') <==> del x.name
     |  
     |  __ge__(...)
     |      x.__ge__(y) <==> x>=y
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __gt__(...)
     |      x.__gt__(y) <==> x>y
     |  
     |  __hash__(...)
     |      x.__hash__() <==> hash(x)
     |  
     |  __le__(...)
     |      x.__le__(y) <==> x<=y
     |  
     |  __lt__(...)
     |      x.__lt__(y) <==> x<y
     |  
     |  __ne__(...)
     |      x.__ne__(y) <==> x!=y
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __setattr__(...)
     |      x.__setattr__('name', value) <==> x.name = value
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __new__ = <built-in method __new__ of PythonQt.PythonQtClassWrapper ob...
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
    
    class QPointF(PythonQt.PythonQtInstanceWrapper)
     |  Method resolution order:
     |      QPointF
     |      PythonQt.PythonQtInstanceWrapper
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  __add__(...)
     |      x.__add__(y) <==> x+y
     |  
     |  __div__(...)
     |      x.__div__(y) <==> x/y
     |  
     |  __eq__(...)
     |      x.__eq__(y) <==> x==y
     |  
     |  __iadd__(...)
     |      x.__iadd__(y) <==> x+=y
     |  
     |  __idiv__(...)
     |      x.__idiv__(y) <==> x/=y
     |  
     |  __imul__(...)
     |      x.__imul__(y) <==> x*=y
     |  
     |  __init__(...)
     |      x.__init__(...) initializes x; see help(type(x)) for signature
     |  
     |  __isub__(...)
     |      x.__isub__(y) <==> x-=y
     |  
     |  __itruediv__(...)
     |      x.__itruediv__(y) <==> x/=y
     |  
     |  __mul__(...)
     |      x.__mul__(y) <==> x*y
     |  
     |  __neg__(...)
     |      x.__neg__() <==> -x
     |  
     |  __nonzero__(...)
     |      x.__nonzero__() <==> x != 0
     |  
     |  __radd__(...)
     |      x.__radd__(y) <==> y+x
     |  
     |  __rdiv__(...)
     |      x.__rdiv__(y) <==> y/x
     |  
     |  __rmul__(...)
     |      x.__rmul__(y) <==> y*x
     |  
     |  __rsub__(...)
     |      x.__rsub__(y) <==> y-x
     |  
     |  __rtruediv__(...)
     |      x.__rtruediv__(y) <==> y/x
     |  
     |  __sub__(...)
     |      x.__sub__(y) <==> x-y
     |  
     |  __truediv__(...)
     |      x.__truediv__(y) <==> x/y
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  className = <built-in method className of PythonQt.PythonQtClassWrappe...
     |      Return the classname of the object
     |  
     |  delete = <built-in method delete of PythonQt.PythonQtClassWrapper obje...
     |      Deletes the given C++ object
     |  
     |  dotProduct = <unbound qt slot static_QPointF_dotProduct of QPointF typ...
     |      X.dotProduct(a, b) -> float
     |  
     |  help = <built-in method help of PythonQt.PythonQtClassWrapper object>
     |      Shows the help of available methods for this class
     |  
     |  inherits = <built-in method inherits of PythonQt.PythonQtClassWrapper ...
     |      Returns if the class inherits or is of given type name
     |  
     |  isNull = <unbound qt slot isNull of QPointF type>
     |      X.isNull(a) -> bool
     |  
     |  manhattanLength = <unbound qt slot manhattanLength of QPointF type>
     |      X.manhattanLength(a) -> float
     |  
     |  readFrom = <unbound qt slot readFrom of QPointF type>
     |      X.readFrom(a, b)
     |  
     |  setX = <unbound qt slot setX of QPointF type>
     |      X.setX(a, b)
     |  
     |  setY = <unbound qt slot setY of QPointF type>
     |      X.setY(a, b)
     |  
     |  toPoint = <unbound qt slot toPoint of QPointF type>
     |      X.toPoint(a) -> PythonQt.QtCore.QPoint
     |  
     |  writeTo = <unbound qt slot writeTo of QPointF type>
     |      X.writeTo(a, b)
     |  
     |  x = <unbound qt slot x of QPointF type>
     |      X.x(a) -> float
     |  
     |  y = <unbound qt slot y of QPointF type>
     |      X.y(a) -> float
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __delattr__(...)
     |      x.__delattr__('name') <==> del x.name
     |  
     |  __ge__(...)
     |      x.__ge__(y) <==> x>=y
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __gt__(...)
     |      x.__gt__(y) <==> x>y
     |  
     |  __hash__(...)
     |      x.__hash__() <==> hash(x)
     |  
     |  __le__(...)
     |      x.__le__(y) <==> x<=y
     |  
     |  __lt__(...)
     |      x.__lt__(y) <==> x<y
     |  
     |  __ne__(...)
     |      x.__ne__(y) <==> x!=y
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __setattr__(...)
     |      x.__setattr__('name', value) <==> x.name = value
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __new__ = <built-in method __new__ of PythonQt.PythonQtClassWrapper ob...
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
    
    class QProcess(PythonQt.PythonQtInstanceWrapper)
     |  Method resolution order:
     |      QProcess
     |      PythonQt.PythonQtInstanceWrapper
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  __init__(...)
     |      x.__init__(...) initializes x; see help(type(x)) for signature
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  Append = 4
     |  
     |  CrashExit = 1
     |  
     |  Crashed = 1
     |  
     |  ExitStatus = <class 'PythonQt.QtCore.ExitStatus'>
     |  
     |  
     |  FailedToStart = 0
     |  
     |  ForwardedChannels = 2
     |  
     |  ForwardedErrorChannel = 4
     |  
     |  ForwardedInputChannel = 1
     |  
     |  ForwardedOutputChannel = 3
     |  
     |  InputChannelMode = <class 'PythonQt.QtCore.InputChannelMode'>
     |  
     |  
     |  ManagedInputChannel = 0
     |  
     |  MergedChannels = 1
     |  
     |  NormalExit = 0
     |  
     |  NotOpen = 0
     |  
     |  NotRunning = 0
     |  
     |  OpenMode = <class 'PythonQt.QtCore.OpenMode'>
     |  
     |  
     |  OpenModeFlag = <class 'PythonQt.QtCore.OpenModeFlag'>
     |  
     |  
     |  ProcessChannel = <class 'PythonQt.QtCore.ProcessChannel'>
     |  
     |  
     |  ProcessChannelMode = <class 'PythonQt.QtCore.ProcessChannelMode'>
     |  
     |  
     |  ProcessError = <class 'PythonQt.QtCore.ProcessError'>
     |  
     |  
     |  ProcessState = <class 'PythonQt.QtCore.ProcessState'>
     |  
     |  
     |  ReadError = 3
     |  
     |  ReadOnly = 1
     |  
     |  ReadWrite = 3
     |  
     |  Running = 2
     |  
     |  SeparateChannels = 0
     |  
     |  StandardError = 1
     |  
     |  StandardOutput = 0
     |  
     |  Starting = 1
     |  
     |  Text = 16
     |  
     |  Timedout = 2
     |  
     |  Truncate = 8
     |  
     |  Unbuffered = 32
     |  
     |  UnknownError = 5
     |  
     |  WriteError = 4
     |  
     |  WriteOnly = 2
     |  
     |  aboutToClose = <unbound qt signal aboutToClose of QProcess type>
     |  
     |  
     |  arguments = <unbound qt slot arguments of QProcess type>
     |      X.arguments(a) -> tuple
     |  
     |  atEnd = <unbound qt slot py_q_atEnd of QProcess type>
     |      X.atEnd(a) -> bool
     |  
     |  blockSignals = <unbound qt slot blockSignals of QProcess type>
     |      X.blockSignals(a, b) -> bool
     |  
     |  bytesAvailable = <unbound qt slot py_q_bytesAvailable of QProcess type...
     |      X.bytesAvailable(a) -> int
     |  
     |  bytesToWrite = <unbound qt slot py_q_bytesToWrite of QProcess type>
     |      X.bytesToWrite(a) -> int
     |  
     |  bytesWritten = <unbound qt signal bytesWritten of QProcess type>
     |  
     |  
     |  canReadLine = <unbound qt slot py_q_canReadLine of QProcess type>
     |      X.canReadLine(a) -> bool
     |  
     |  channelBytesWritten = <unbound qt signal channelBytesWritten of QProce...
     |  
     |  
     |  channelReadyRead = <unbound qt signal channelReadyRead of QProcess typ...
     |  
     |  
     |  childEvent = <unbound qt slot py_q_childEvent of QProcess type>
     |      X.childEvent(a, b)
     |  
     |  children = <unbound qt slot children of QProcess type>
     |      X.children(a) -> tuple
     |  
     |  className = <built-in method className of PythonQt.PythonQtClassWrappe...
     |      Return the classname of the object
     |  
     |  close = <unbound qt slot py_q_close of QProcess type>
     |      X.close(a)
     |  
     |  closeReadChannel = <unbound qt slot closeReadChannel of QProcess type>
     |      X.closeReadChannel(a, b)
     |  
     |  closeWriteChannel = <unbound qt slot closeWriteChannel of QProcess typ...
     |      X.closeWriteChannel(a)
     |  
     |  connect = <unbound qt slot connect of QProcess type>
     |      X.connect(a, b, c, d, e) -> bool
     |  
     |  customEvent = <unbound qt slot py_q_customEvent of QProcess type>
     |      X.customEvent(a, b)
     |  
     |  delete = <built-in method delete of PythonQt.PythonQtClassWrapper obje...
     |      Deletes the given C++ object
     |  
     |  deleteLater = <unbound qt slot deleteLater of QProcess type>
     |      X.deleteLater()
     |  
     |  destroyed = <unbound qt signal destroyed of QProcess type>
     |  
     |  
     |  disconnect = <unbound qt slot disconnect of QProcess type>
     |      X.disconnect(a, b, c, d) -> bool
     |  
     |  dumpObjectInfo = <unbound qt slot dumpObjectInfo of QProcess type>
     |      X.dumpObjectInfo(a)
     |  
     |  dumpObjectTree = <unbound qt slot dumpObjectTree of QProcess type>
     |      X.dumpObjectTree(a)
     |  
     |  dynamicPropertyNames = <unbound qt slot dynamicPropertyNames of QProce...
     |      X.dynamicPropertyNames(a)
     |  
     |  environment = <unbound qt slot environment of QProcess type>
     |      X.environment(a) -> tuple
     |  
     |  error = <unbound qt slot error of QProcess type>
     |      X.error(a)
     |  
     |  errorOccurred = <unbound qt signal errorOccurred of QProcess type>
     |  
     |  
     |  errorString = <unbound qt slot errorString of QProcess type>
     |      X.errorString(a) -> str
     |  
     |  event = <unbound qt slot py_q_event of QProcess type>
     |      X.event(a, b) -> bool
     |  
     |  eventFilter = <unbound qt slot py_q_eventFilter of QProcess type>
     |      X.eventFilter(a, b, c) -> bool
     |  
     |  execute = <unbound qt slot static_QProcess_execute of QProcess type>
     |      X.execute(a, b) -> int
     |  
     |  exitCode = <unbound qt slot exitCode of QProcess type>
     |      X.exitCode(a) -> int
     |  
     |  exitStatus = <unbound qt slot exitStatus of QProcess type>
     |      X.exitStatus(a)
     |  
     |  findChild = <unbound qt slot findChild of QProcess type>
     |      X.findChild(a, b, c) -> PythonQt.private.QObject
     |  
     |  findChildren = <unbound qt slot findChildren of QProcess type>
     |      X.findChildren(a, b, c) -> tuple
     |  
     |  finished = <unbound qt signal finished of QProcess type>
     |  
     |  
     |  getChar = <unbound qt slot getChar of QProcess type>
     |      X.getChar(a, b) -> bool
     |  
     |  help = <built-in method help of PythonQt.PythonQtClassWrapper object>
     |      Shows the help of available methods for this class
     |  
     |  inherits = <built-in method inherits of PythonQt.PythonQtClassWrapper ...
     |      Returns if the class inherits or is of given type name
     |  
     |  inputChannelMode = <unbound qt slot inputChannelMode of QProcess type>
     |      X.inputChannelMode(a)
     |  
     |  installEventFilter = <unbound qt slot installEventFilter of QProcess t...
     |      X.installEventFilter(a, b)
     |  
     |  isOpen = <unbound qt slot isOpen of QProcess type>
     |      X.isOpen(a) -> bool
     |  
     |  isReadable = <unbound qt slot isReadable of QProcess type>
     |      X.isReadable(a) -> bool
     |  
     |  isSequential = <unbound qt slot py_q_isSequential of QProcess type>
     |      X.isSequential(a) -> bool
     |  
     |  isSignalConnected = <unbound qt slot isSignalConnected of QProcess typ...
     |      X.isSignalConnected(a, b) -> bool
     |  
     |  isTextModeEnabled = <unbound qt slot isTextModeEnabled of QProcess typ...
     |      X.isTextModeEnabled(a) -> bool
     |  
     |  isWidgetType = <unbound qt slot isWidgetType of QProcess type>
     |      X.isWidgetType(a) -> bool
     |  
     |  isWindowType = <unbound qt slot isWindowType of QProcess type>
     |      X.isWindowType(a) -> bool
     |  
     |  isWritable = <unbound qt slot isWritable of QProcess type>
     |      X.isWritable(a) -> bool
     |  
     |  kill = <unbound qt slot kill of QProcess type>
     |      X.kill()
     |  
     |  killTimer = <unbound qt slot killTimer of QProcess type>
     |      X.killTimer(a, b)
     |  
     |  metaObject = <unbound qt slot metaObject of QProcess type>
     |      X.metaObject(a) -> PythonQt.QtCore.QMetaObject
     |  
     |  moveToThread = <unbound qt slot moveToThread of QProcess type>
     |      X.moveToThread(a, b)
     |  
     |  nullDevice = <unbound qt slot static_QProcess_nullDevice of QProcess t...
     |      X.nullDevice() -> str
     |  
     |  objectName = None
     |  
     |  objectNameChanged = <unbound qt signal objectNameChanged of QProcess t...
     |  
     |  
     |  open = <unbound qt slot py_q_open of QProcess type>
     |      X.open(a, b) -> bool
     |  
     |  openMode = <unbound qt slot openMode of QProcess type>
     |      X.openMode(a)
     |  
     |  parent = <unbound qt slot parent of QProcess type>
     |      X.parent(a) -> PythonQt.private.QObject
     |  
     |  peek = <unbound qt slot peek of QProcess type>
     |      X.peek(a, b) -> PythonQt.QtCore.QByteArray
     |  
     |  pos = <unbound qt slot py_q_pos of QProcess type>
     |      X.pos(a) -> int
     |  
     |  processChannelMode = <unbound qt slot processChannelMode of QProcess t...
     |      X.processChannelMode(a)
     |  
     |  processEnvironment = <unbound qt slot processEnvironment of QProcess t...
     |      X.processEnvironment(a) -> PythonQt.QtCore.QProcessEnvironment
     |  
     |  processId = <unbound qt slot processId of QProcess type>
     |      X.processId(a) -> int
     |  
     |  program = <unbound qt slot program of QProcess type>
     |      X.program(a) -> str
     |  
     |  property = <unbound qt slot property of QProcess type>
     |      X.property(a, b) -> object
     |  
     |  putChar = <unbound qt slot putChar of QProcess type>
     |      X.putChar(a, b) -> bool
     |  
     |  read = <unbound qt slot read of QProcess type>
     |      X.read(a, b) -> PythonQt.QtCore.QByteArray
     |  
     |  readAll = <unbound qt slot readAll of QProcess type>
     |      X.readAll(a) -> PythonQt.QtCore.QByteArray
     |  
     |  readAllStandardError = <unbound qt slot readAllStandardError of QProce...
     |      X.readAllStandardError(a) -> PythonQt.QtCore.QByteArray
     |  
     |  readAllStandardOutput = <unbound qt slot readAllStandardOutput of QPro...
     |      X.readAllStandardOutput(a) -> PythonQt.QtCore.QByteArray
     |  
     |  readChannel = <unbound qt slot readChannel of QProcess type>
     |      X.readChannel(a)
     |  
     |  readChannelFinished = <unbound qt signal readChannelFinished of QProce...
     |  
     |  
     |  readData = <unbound qt slot py_q_readData of QProcess type>
     |      X.readData(a, b, c) -> int
     |  
     |  readLine = <unbound qt slot readLine of QProcess type>
     |      X.readLine(a, b) -> PythonQt.QtCore.QByteArray
     |  
     |  readLineData = <unbound qt slot py_q_readLineData of QProcess type>
     |      X.readLineData(a, b, c) -> int
     |  
     |  readyRead = <unbound qt signal readyRead of QProcess type>
     |  
     |  
     |  readyReadStandardError = <unbound qt signal readyReadStandardError of ...
     |  
     |  
     |  readyReadStandardOutput = <unbound qt signal readyReadStandardOutput o...
     |  
     |  
     |  removeEventFilter = <unbound qt slot removeEventFilter of QProcess typ...
     |      X.removeEventFilter(a, b)
     |  
     |  reset = <unbound qt slot py_q_reset of QProcess type>
     |      X.reset(a) -> bool
     |  
     |  seek = <unbound qt slot py_q_seek of QProcess type>
     |      X.seek(a, b) -> bool
     |  
     |  sender = <unbound qt slot sender of QProcess type>
     |      X.sender(a) -> PythonQt.private.QObject
     |  
     |  senderSignalIndex = <unbound qt slot senderSignalIndex of QProcess typ...
     |      X.senderSignalIndex(a) -> int
     |  
     |  setArguments = <unbound qt slot setArguments of QProcess type>
     |      X.setArguments(a, b)
     |  
     |  setEnvironment = <unbound qt slot setEnvironment of QProcess type>
     |      X.setEnvironment(a, b)
     |  
     |  setErrorString = <unbound qt slot setErrorString of QProcess type>
     |      X.setErrorString(a, b)
     |  
     |  setInputChannelMode = <unbound qt slot setInputChannelMode of QProcess...
     |      X.setInputChannelMode(a, b)
     |  
     |  setObjectName = <unbound qt slot setObjectName of QProcess type>
     |      X.setObjectName(a, b)
     |  
     |  setOpenMode = <unbound qt slot setOpenMode of QProcess type>
     |      X.setOpenMode(a, b)
     |  
     |  setParent = <unbound qt slot setParent of QProcess type>
     |      X.setParent(a, b)
     |  
     |  setProcessChannelMode = <unbound qt slot setProcessChannelMode of QPro...
     |      X.setProcessChannelMode(a, b)
     |  
     |  setProcessEnvironment = <unbound qt slot setProcessEnvironment of QPro...
     |      X.setProcessEnvironment(a, b)
     |  
     |  setProcessState = <unbound qt slot setProcessState of QProcess type>
     |      X.setProcessState(a, b)
     |  
     |  setProgram = <unbound qt slot setProgram of QProcess type>
     |      X.setProgram(a, b)
     |  
     |  setProperty = <unbound qt slot setProperty of QProcess type>
     |      X.setProperty(a, b, c) -> bool
     |  
     |  setReadChannel = <unbound qt slot setReadChannel of QProcess type>
     |      X.setReadChannel(a, b)
     |  
     |  setStandardErrorFile = <unbound qt slot setStandardErrorFile of QProce...
     |      X.setStandardErrorFile(a, b, c)
     |  
     |  setStandardInputFile = <unbound qt slot setStandardInputFile of QProce...
     |      X.setStandardInputFile(a, b)
     |  
     |  setStandardOutputFile = <unbound qt slot setStandardOutputFile of QPro...
     |      X.setStandardOutputFile(a, b, c)
     |  
     |  setStandardOutputProcess = <unbound qt slot setStandardOutputProcess o...
     |      X.setStandardOutputProcess(a, b)
     |  
     |  setTextModeEnabled = <unbound qt slot setTextModeEnabled of QProcess t...
     |      X.setTextModeEnabled(a, b)
     |  
     |  setWorkingDirectory = <unbound qt slot setWorkingDirectory of QProcess...
     |      X.setWorkingDirectory(a, b)
     |  
     |  setupChildProcess = <unbound qt slot py_q_setupChildProcess of QProces...
     |      X.setupChildProcess(a)
     |  
     |  signalsBlocked = <unbound qt slot signalsBlocked of QProcess type>
     |      X.signalsBlocked(a) -> bool
     |  
     |  size = <unbound qt slot py_q_size of QProcess type>
     |      X.size(a) -> int
     |  
     |  start = <unbound qt slot start of QProcess type>
     |      X.start(a, b, c, d)
     |  
     |  startDetached = <unbound qt slot static_QProcess_startDetached of QPro...
     |      X.startDetached(a, b, c, d) -> bool
     |  
     |  startTimer = <unbound qt slot startTimer of QProcess type>
     |      X.startTimer(a, b, c) -> int
     |  
     |  started = <unbound qt signal started of QProcess type>
     |  
     |  
     |  state = <unbound qt slot state of QProcess type>
     |      X.state(a)
     |  
     |  stateChanged = <unbound qt signal stateChanged of QProcess type>
     |  
     |  
     |  systemEnvironment = <unbound qt slot static_QProcess_systemEnvironment...
     |      X.systemEnvironment() -> tuple
     |  
     |  terminate = <unbound qt slot terminate of QProcess type>
     |      X.terminate()
     |  
     |  thread = <unbound qt slot thread of QProcess type>
     |      X.thread(a)
     |  
     |  timerEvent = <unbound qt slot py_q_timerEvent of QProcess type>
     |      X.timerEvent(a, b)
     |  
     |  tr = <unbound qt slot tr of QProcess type>
     |      X.tr(a, b, c, d) -> str
     |  
     |  ungetChar = <unbound qt slot ungetChar of QProcess type>
     |      X.ungetChar(a, b)
     |  
     |  waitForBytesWritten = <unbound qt slot py_q_waitForBytesWritten of QPr...
     |      X.waitForBytesWritten(a, b) -> bool
     |  
     |  waitForFinished = <unbound qt slot waitForFinished of QProcess type>
     |      X.waitForFinished(a, b) -> bool
     |  
     |  waitForReadyRead = <unbound qt slot py_q_waitForReadyRead of QProcess ...
     |      X.waitForReadyRead(a, b) -> bool
     |  
     |  waitForStarted = <unbound qt slot waitForStarted of QProcess type>
     |      X.waitForStarted(a, b) -> bool
     |  
     |  workingDirectory = <unbound qt slot workingDirectory of QProcess type>
     |      X.workingDirectory(a) -> str
     |  
     |  write = <unbound qt slot write of QProcess type>
     |      X.write(a, b) -> int
     |  
     |  writeData = <unbound qt slot py_q_writeData of QProcess type>
     |      X.writeData(a, b, c) -> int
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __delattr__(...)
     |      x.__delattr__('name') <==> del x.name
     |  
     |  __eq__(...)
     |      x.__eq__(y) <==> x==y
     |  
     |  __ge__(...)
     |      x.__ge__(y) <==> x>=y
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __gt__(...)
     |      x.__gt__(y) <==> x>y
     |  
     |  __hash__(...)
     |      x.__hash__() <==> hash(x)
     |  
     |  __le__(...)
     |      x.__le__(y) <==> x<=y
     |  
     |  __lt__(...)
     |      x.__lt__(y) <==> x<y
     |  
     |  __ne__(...)
     |      x.__ne__(y) <==> x!=y
     |  
     |  __nonzero__(...)
     |      x.__nonzero__() <==> x != 0
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __setattr__(...)
     |      x.__setattr__('name', value) <==> x.name = value
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __new__ = <built-in method __new__ of PythonQt.PythonQtClassWrapper ob...
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
    
    class QProcessEnvironment(PythonQt.PythonQtInstanceWrapper)
     |  Method resolution order:
     |      QProcessEnvironment
     |      PythonQt.PythonQtInstanceWrapper
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  __eq__(...)
     |      x.__eq__(y) <==> x==y
     |  
     |  __init__(...)
     |      x.__init__(...) initializes x; see help(type(x)) for signature
     |  
     |  __ne__(...)
     |      x.__ne__(y) <==> x!=y
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  className = <built-in method className of PythonQt.PythonQtClassWrappe...
     |      Return the classname of the object
     |  
     |  clear = <unbound qt slot clear of QProcessEnvironment type>
     |      X.clear(a)
     |  
     |  contains = <unbound qt slot contains of QProcessEnvironment type>
     |      X.contains(a, b) -> bool
     |  
     |  delete = <built-in method delete of PythonQt.PythonQtClassWrapper obje...
     |      Deletes the given C++ object
     |  
     |  help = <built-in method help of PythonQt.PythonQtClassWrapper object>
     |      Shows the help of available methods for this class
     |  
     |  inherits = <built-in method inherits of PythonQt.PythonQtClassWrapper ...
     |      Returns if the class inherits or is of given type name
     |  
     |  insert = <unbound qt slot insert of QProcessEnvironment type>
     |      X.insert(a, b, c)
     |  
     |  isEmpty = <unbound qt slot isEmpty of QProcessEnvironment type>
     |      X.isEmpty(a) -> bool
     |  
     |  keys = <unbound qt slot keys of QProcessEnvironment type>
     |      X.keys(a) -> tuple
     |  
     |  operator_assign = <unbound qt slot operator_assign of QProcessEnvironm...
     |      X.operator_assign(a, b) -> PythonQt.QtCore.QProcessEnvironment
     |  
     |  remove = <unbound qt slot remove of QProcessEnvironment type>
     |      X.remove(a, b)
     |  
     |  swap = <unbound qt slot swap of QProcessEnvironment type>
     |      X.swap(a, b)
     |  
     |  systemEnvironment = <unbound qt slot static_QProcessEnvironment_system...
     |      X.systemEnvironment() -> PythonQt.QtCore.QProcessEnvironment
     |  
     |  toStringList = <unbound qt slot toStringList of QProcessEnvironment ty...
     |      X.toStringList(a) -> tuple
     |  
     |  value = <unbound qt slot value of QProcessEnvironment type>
     |      X.value(a, b, c) -> str
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __delattr__(...)
     |      x.__delattr__('name') <==> del x.name
     |  
     |  __ge__(...)
     |      x.__ge__(y) <==> x>=y
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __gt__(...)
     |      x.__gt__(y) <==> x>y
     |  
     |  __hash__(...)
     |      x.__hash__() <==> hash(x)
     |  
     |  __le__(...)
     |      x.__le__(y) <==> x<=y
     |  
     |  __lt__(...)
     |      x.__lt__(y) <==> x<y
     |  
     |  __nonzero__(...)
     |      x.__nonzero__() <==> x != 0
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __setattr__(...)
     |      x.__setattr__('name', value) <==> x.name = value
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __new__ = <built-in method __new__ of PythonQt.PythonQtClassWrapper ob...
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
    
    class QPropertyAnimation(PythonQt.PythonQtInstanceWrapper)
     |  Method resolution order:
     |      QPropertyAnimation
     |      PythonQt.PythonQtInstanceWrapper
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  __init__(...)
     |      x.__init__(...) initializes x; see help(type(x)) for signature
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  Backward = 1
     |  
     |  DeleteWhenStopped = 1
     |  
     |  DeletionPolicy = <class 'PythonQt.QtCore.DeletionPolicy'>
     |  
     |  
     |  Direction = <class 'PythonQt.QtCore.Direction'>
     |  
     |  
     |  Forward = 0
     |  
     |  KeepWhenStopped = 0
     |  
     |  Paused = 1
     |  
     |  Running = 2
     |  
     |  State = <class 'PythonQt.QtCore.State'>
     |  
     |  
     |  Stopped = 0
     |  
     |  blockSignals = <unbound qt slot blockSignals of QPropertyAnimation typ...
     |      X.blockSignals(a, b) -> bool
     |  
     |  childEvent = <unbound qt slot py_q_childEvent of QPropertyAnimation ty...
     |      X.childEvent(a, b)
     |  
     |  children = <unbound qt slot children of QPropertyAnimation type>
     |      X.children(a) -> tuple
     |  
     |  className = <built-in method className of PythonQt.PythonQtClassWrappe...
     |      Return the classname of the object
     |  
     |  connect = <unbound qt slot connect of QPropertyAnimation type>
     |      X.connect(a, b, c, d, e) -> bool
     |  
     |  currentLoop = None
     |  
     |  currentLoopChanged = <unbound qt signal currentLoopChanged of QPropert...
     |  
     |  
     |  currentLoopTime = <unbound qt slot currentLoopTime of QPropertyAnimati...
     |      X.currentLoopTime(a) -> int
     |  
     |  currentTime = None
     |  
     |  currentValue = None
     |  
     |  customEvent = <unbound qt slot py_q_customEvent of QPropertyAnimation ...
     |      X.customEvent(a, b)
     |  
     |  delete = <built-in method delete of PythonQt.PythonQtClassWrapper obje...
     |      Deletes the given C++ object
     |  
     |  deleteLater = <unbound qt slot deleteLater of QPropertyAnimation type>
     |      X.deleteLater()
     |  
     |  destroyed = <unbound qt signal destroyed of QPropertyAnimation type>
     |  
     |  
     |  direction = None
     |  
     |  directionChanged = <unbound qt signal directionChanged of QPropertyAni...
     |  
     |  
     |  disconnect = <unbound qt slot disconnect of QPropertyAnimation type>
     |      X.disconnect(a, b, c, d) -> bool
     |  
     |  dumpObjectInfo = <unbound qt slot dumpObjectInfo of QPropertyAnimation...
     |      X.dumpObjectInfo(a)
     |  
     |  dumpObjectTree = <unbound qt slot dumpObjectTree of QPropertyAnimation...
     |      X.dumpObjectTree(a)
     |  
     |  duration = None
     |  
     |  dynamicPropertyNames = <unbound qt slot dynamicPropertyNames of QPrope...
     |      X.dynamicPropertyNames(a)
     |  
     |  easingCurve = QEasingCurve (QEasingCurve at: 0x0)
     |  
     |  endValue = None
     |  
     |  event = <unbound qt slot py_q_event of QPropertyAnimation type>
     |      X.event(a, b) -> bool
     |  
     |  eventFilter = <unbound qt slot py_q_eventFilter of QPropertyAnimation ...
     |      X.eventFilter(a, b, c) -> bool
     |  
     |  findChild = <unbound qt slot findChild of QPropertyAnimation type>
     |      X.findChild(a, b, c) -> PythonQt.private.QObject
     |  
     |  findChildren = <unbound qt slot findChildren of QPropertyAnimation typ...
     |      X.findChildren(a, b, c) -> tuple
     |  
     |  finished = <unbound qt signal finished of QPropertyAnimation type>
     |  
     |  
     |  group = <unbound qt slot group of QPropertyAnimation type>
     |      X.group(a) -> PythonQt.QtCore.QAnimationGroup
     |  
     |  help = <built-in method help of PythonQt.PythonQtClassWrapper object>
     |      Shows the help of available methods for this class
     |  
     |  inherits = <built-in method inherits of PythonQt.PythonQtClassWrapper ...
     |      Returns if the class inherits or is of given type name
     |  
     |  installEventFilter = <unbound qt slot installEventFilter of QPropertyA...
     |      X.installEventFilter(a, b)
     |  
     |  interpolated = <unbound qt slot py_q_interpolated of QPropertyAnimatio...
     |      X.interpolated(a, b, c, d) -> object
     |  
     |  isSignalConnected = <unbound qt slot isSignalConnected of QPropertyAni...
     |      X.isSignalConnected(a, b) -> bool
     |  
     |  isWidgetType = <unbound qt slot isWidgetType of QPropertyAnimation typ...
     |      X.isWidgetType(a) -> bool
     |  
     |  isWindowType = <unbound qt slot isWindowType of QPropertyAnimation typ...
     |      X.isWindowType(a) -> bool
     |  
     |  keyValueAt = <unbound qt slot keyValueAt of QPropertyAnimation type>
     |      X.keyValueAt(a, b) -> object
     |  
     |  keyValues = <unbound qt slot keyValues of QPropertyAnimation type>
     |      X.keyValues(a) -> tuple
     |  
     |  killTimer = <unbound qt slot killTimer of QPropertyAnimation type>
     |      X.killTimer(a, b)
     |  
     |  loopCount = None
     |  
     |  metaObject = <unbound qt slot metaObject of QPropertyAnimation type>
     |      X.metaObject(a) -> PythonQt.QtCore.QMetaObject
     |  
     |  moveToThread = <unbound qt slot moveToThread of QPropertyAnimation typ...
     |      X.moveToThread(a, b)
     |  
     |  objectName = None
     |  
     |  objectNameChanged = <unbound qt signal objectNameChanged of QPropertyA...
     |  
     |  
     |  parent = <unbound qt slot parent of QPropertyAnimation type>
     |      X.parent(a) -> PythonQt.private.QObject
     |  
     |  pause = <unbound qt slot pause of QPropertyAnimation type>
     |      X.pause()
     |  
     |  property = <unbound qt slot property of QPropertyAnimation type>
     |      X.property(a, b) -> object
     |  
     |  propertyName = QByteArray (QByteArray at: 0x0)
     |  
     |  removeEventFilter = <unbound qt slot removeEventFilter of QPropertyAni...
     |      X.removeEventFilter(a, b)
     |  
     |  resume = <unbound qt slot resume of QPropertyAnimation type>
     |      X.resume()
     |  
     |  sender = <unbound qt slot sender of QPropertyAnimation type>
     |      X.sender(a) -> PythonQt.private.QObject
     |  
     |  senderSignalIndex = <unbound qt slot senderSignalIndex of QPropertyAni...
     |      X.senderSignalIndex(a) -> int
     |  
     |  setCurrentTime = <unbound qt slot setCurrentTime of QPropertyAnimation...
     |      X.setCurrentTime(a)
     |  
     |  setDirection = <unbound qt slot setDirection of QPropertyAnimation typ...
     |      X.setDirection(a, b)
     |  
     |  setDuration = <unbound qt slot setDuration of QPropertyAnimation type>
     |      X.setDuration(a, b)
     |  
     |  setEasingCurve = <unbound qt slot setEasingCurve of QPropertyAnimation...
     |      X.setEasingCurve(a, b)
     |  
     |  setEndValue = <unbound qt slot setEndValue of QPropertyAnimation type>
     |      X.setEndValue(a, b)
     |  
     |  setKeyValueAt = <unbound qt slot setKeyValueAt of QPropertyAnimation t...
     |      X.setKeyValueAt(a, b, c)
     |  
     |  setKeyValues = <unbound qt slot setKeyValues of QPropertyAnimation typ...
     |      X.setKeyValues(a, b)
     |  
     |  setLoopCount = <unbound qt slot setLoopCount of QPropertyAnimation typ...
     |      X.setLoopCount(a, b)
     |  
     |  setObjectName = <unbound qt slot setObjectName of QPropertyAnimation t...
     |      X.setObjectName(a, b)
     |  
     |  setParent = <unbound qt slot setParent of QPropertyAnimation type>
     |      X.setParent(a, b)
     |  
     |  setPaused = <unbound qt slot setPaused of QPropertyAnimation type>
     |      X.setPaused(a)
     |  
     |  setProperty = <unbound qt slot setProperty of QPropertyAnimation type>
     |      X.setProperty(a, b, c) -> bool
     |  
     |  setPropertyName = <unbound qt slot setPropertyName of QPropertyAnimati...
     |      X.setPropertyName(a, b)
     |  
     |  setStartValue = <unbound qt slot setStartValue of QPropertyAnimation t...
     |      X.setStartValue(a, b)
     |  
     |  setTargetObject = <unbound qt slot setTargetObject of QPropertyAnimati...
     |      X.setTargetObject(a, b)
     |  
     |  signalsBlocked = <unbound qt slot signalsBlocked of QPropertyAnimation...
     |      X.signalsBlocked(a) -> bool
     |  
     |  start = <unbound qt slot start of QPropertyAnimation type>
     |      X.start(a)
     |  
     |  startTimer = <unbound qt slot startTimer of QPropertyAnimation type>
     |      X.startTimer(a, b, c) -> int
     |  
     |  startValue = None
     |  
     |  state = None
     |  
     |  stateChanged = <unbound qt signal stateChanged of QPropertyAnimation t...
     |  
     |  
     |  stop = <unbound qt slot stop of QPropertyAnimation type>
     |      X.stop()
     |  
     |  targetObject = QObject (QObject at: 0x0)
     |  
     |  thread = <unbound qt slot thread of QPropertyAnimation type>
     |      X.thread(a)
     |  
     |  timerEvent = <unbound qt slot py_q_timerEvent of QPropertyAnimation ty...
     |      X.timerEvent(a, b)
     |  
     |  totalDuration = <unbound qt slot totalDuration of QPropertyAnimation t...
     |      X.totalDuration(a) -> int
     |  
     |  tr = <unbound qt slot tr of QPropertyAnimation type>
     |      X.tr(a, b, c, d) -> str
     |  
     |  updateCurrentTime = <unbound qt slot py_q_updateCurrentTime of QProper...
     |      X.updateCurrentTime(a, b)
     |  
     |  updateCurrentValue = <unbound qt slot py_q_updateCurrentValue of QProp...
     |      X.updateCurrentValue(a, b)
     |  
     |  updateDirection = <unbound qt slot py_q_updateDirection of QPropertyAn...
     |      X.updateDirection(a, b)
     |  
     |  updateState = <unbound qt slot py_q_updateState of QPropertyAnimation ...
     |      X.updateState(a, b, c)
     |  
     |  valueChanged = <unbound qt signal valueChanged of QPropertyAnimation t...
     |  
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __delattr__(...)
     |      x.__delattr__('name') <==> del x.name
     |  
     |  __eq__(...)
     |      x.__eq__(y) <==> x==y
     |  
     |  __ge__(...)
     |      x.__ge__(y) <==> x>=y
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __gt__(...)
     |      x.__gt__(y) <==> x>y
     |  
     |  __hash__(...)
     |      x.__hash__() <==> hash(x)
     |  
     |  __le__(...)
     |      x.__le__(y) <==> x<=y
     |  
     |  __lt__(...)
     |      x.__lt__(y) <==> x<y
     |  
     |  __ne__(...)
     |      x.__ne__(y) <==> x!=y
     |  
     |  __nonzero__(...)
     |      x.__nonzero__() <==> x != 0
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __setattr__(...)
     |      x.__setattr__('name', value) <==> x.name = value
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __new__ = <built-in method __new__ of PythonQt.PythonQtClassWrapper ob...
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
    
    class QReadWriteLock(PythonQt.PythonQtInstanceWrapper)
     |  Method resolution order:
     |      QReadWriteLock
     |      PythonQt.PythonQtInstanceWrapper
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  __init__(...)
     |      x.__init__(...) initializes x; see help(type(x)) for signature
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  NonRecursive = 0
     |  
     |  RecursionMode = <class 'PythonQt.QtCore.RecursionMode'>
     |  
     |  
     |  Recursive = 1
     |  
     |  className = <built-in method className of PythonQt.PythonQtClassWrappe...
     |      Return the classname of the object
     |  
     |  delete = <built-in method delete of PythonQt.PythonQtClassWrapper obje...
     |      Deletes the given C++ object
     |  
     |  help = <built-in method help of PythonQt.PythonQtClassWrapper object>
     |      Shows the help of available methods for this class
     |  
     |  inherits = <built-in method inherits of PythonQt.PythonQtClassWrapper ...
     |      Returns if the class inherits or is of given type name
     |  
     |  lockForRead = <unbound qt slot lockForRead of QReadWriteLock type>
     |      X.lockForRead(a)
     |  
     |  lockForWrite = <unbound qt slot lockForWrite of QReadWriteLock type>
     |      X.lockForWrite(a)
     |  
     |  tryLockForRead = <unbound qt slot tryLockForRead of QReadWriteLock typ...
     |      X.tryLockForRead(a, b) -> bool
     |  
     |  tryLockForWrite = <unbound qt slot tryLockForWrite of QReadWriteLock t...
     |      X.tryLockForWrite(a, b) -> bool
     |  
     |  unlock = <unbound qt slot unlock of QReadWriteLock type>
     |      X.unlock(a)
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __delattr__(...)
     |      x.__delattr__('name') <==> del x.name
     |  
     |  __eq__(...)
     |      x.__eq__(y) <==> x==y
     |  
     |  __ge__(...)
     |      x.__ge__(y) <==> x>=y
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __gt__(...)
     |      x.__gt__(y) <==> x>y
     |  
     |  __hash__(...)
     |      x.__hash__() <==> hash(x)
     |  
     |  __le__(...)
     |      x.__le__(y) <==> x<=y
     |  
     |  __lt__(...)
     |      x.__lt__(y) <==> x<y
     |  
     |  __ne__(...)
     |      x.__ne__(y) <==> x!=y
     |  
     |  __nonzero__(...)
     |      x.__nonzero__() <==> x != 0
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __setattr__(...)
     |      x.__setattr__('name', value) <==> x.name = value
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __new__ = <built-in method __new__ of PythonQt.PythonQtClassWrapper ob...
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
    
    class QRect(PythonQt.PythonQtInstanceWrapper)
     |  Method resolution order:
     |      QRect
     |      PythonQt.PythonQtInstanceWrapper
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  __add__(...)
     |      x.__add__(y) <==> x+y
     |  
     |  __and__(...)
     |      x.__and__(y) <==> x&y
     |  
     |  __eq__(...)
     |      x.__eq__(y) <==> x==y
     |  
     |  __iadd__(...)
     |      x.__iadd__(y) <==> x+=y
     |  
     |  __iand__(...)
     |      x.__iand__(y) <==> x&=y
     |  
     |  __init__(...)
     |      x.__init__(...) initializes x; see help(type(x)) for signature
     |  
     |  __ior__(...)
     |      x.__ior__(y) <==> x|=y
     |  
     |  __isub__(...)
     |      x.__isub__(y) <==> x-=y
     |  
     |  __neg__(...)
     |      x.__neg__() <==> -x
     |  
     |  __nonzero__(...)
     |      x.__nonzero__() <==> x != 0
     |  
     |  __or__(...)
     |      x.__or__(y) <==> x|y
     |  
     |  __radd__(...)
     |      x.__radd__(y) <==> y+x
     |  
     |  __rand__(...)
     |      x.__rand__(y) <==> y&x
     |  
     |  __ror__(...)
     |      x.__ror__(y) <==> y|x
     |  
     |  __rsub__(...)
     |      x.__rsub__(y) <==> y-x
     |  
     |  __sub__(...)
     |      x.__sub__(y) <==> x-y
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  adjust = <unbound qt slot adjust of QRect type>
     |      X.adjust(a, b, c, d, e)
     |  
     |  adjusted = <unbound qt slot adjusted of QRect type>
     |      X.adjusted(a, b, c, d, e) -> PythonQt.QtCore.QRect
     |  
     |  bottom = <unbound qt slot bottom of QRect type>
     |      X.bottom(a) -> int
     |  
     |  bottomLeft = <unbound qt slot bottomLeft of QRect type>
     |      X.bottomLeft(a) -> PythonQt.QtCore.QPoint
     |  
     |  bottomRight = <unbound qt slot bottomRight of QRect type>
     |      X.bottomRight(a) -> PythonQt.QtCore.QPoint
     |  
     |  center = <unbound qt slot center of QRect type>
     |      X.center(a) -> PythonQt.QtCore.QPoint
     |  
     |  className = <built-in method className of PythonQt.PythonQtClassWrappe...
     |      Return the classname of the object
     |  
     |  contains = <unbound qt slot contains of QRect type>
     |      X.contains(a, b, c, d) -> bool
     |  
     |  delete = <built-in method delete of PythonQt.PythonQtClassWrapper obje...
     |      Deletes the given C++ object
     |  
     |  height = <unbound qt slot height of QRect type>
     |      X.height(a) -> int
     |  
     |  help = <built-in method help of PythonQt.PythonQtClassWrapper object>
     |      Shows the help of available methods for this class
     |  
     |  inherits = <built-in method inherits of PythonQt.PythonQtClassWrapper ...
     |      Returns if the class inherits or is of given type name
     |  
     |  intersected = <unbound qt slot intersected of QRect type>
     |      X.intersected(a, b) -> PythonQt.QtCore.QRect
     |  
     |  intersects = <unbound qt slot intersects of QRect type>
     |      X.intersects(a, b) -> bool
     |  
     |  isEmpty = <unbound qt slot isEmpty of QRect type>
     |      X.isEmpty(a) -> bool
     |  
     |  isNull = <unbound qt slot isNull of QRect type>
     |      X.isNull(a) -> bool
     |  
     |  isValid = <unbound qt slot isValid of QRect type>
     |      X.isValid(a) -> bool
     |  
     |  left = <unbound qt slot left of QRect type>
     |      X.left(a) -> int
     |  
     |  marginsAdded = <unbound qt slot marginsAdded of QRect type>
     |      X.marginsAdded(a, b) -> PythonQt.QtCore.QRect
     |  
     |  marginsRemoved = <unbound qt slot marginsRemoved of QRect type>
     |      X.marginsRemoved(a, b) -> PythonQt.QtCore.QRect
     |  
     |  moveBottom = <unbound qt slot moveBottom of QRect type>
     |      X.moveBottom(a, b)
     |  
     |  moveBottomLeft = <unbound qt slot moveBottomLeft of QRect type>
     |      X.moveBottomLeft(a, b)
     |  
     |  moveBottomRight = <unbound qt slot moveBottomRight of QRect type>
     |      X.moveBottomRight(a, b)
     |  
     |  moveCenter = <unbound qt slot moveCenter of QRect type>
     |      X.moveCenter(a, b)
     |  
     |  moveLeft = <unbound qt slot moveLeft of QRect type>
     |      X.moveLeft(a, b)
     |  
     |  moveRight = <unbound qt slot moveRight of QRect type>
     |      X.moveRight(a, b)
     |  
     |  moveTo = <unbound qt slot moveTo of QRect type>
     |      X.moveTo(a, b, c)
     |  
     |  moveTop = <unbound qt slot moveTop of QRect type>
     |      X.moveTop(a, b)
     |  
     |  moveTopLeft = <unbound qt slot moveTopLeft of QRect type>
     |      X.moveTopLeft(a, b)
     |  
     |  moveTopRight = <unbound qt slot moveTopRight of QRect type>
     |      X.moveTopRight(a, b)
     |  
     |  normalized = <unbound qt slot normalized of QRect type>
     |      X.normalized(a) -> PythonQt.QtCore.QRect
     |  
     |  readFrom = <unbound qt slot readFrom of QRect type>
     |      X.readFrom(a, b)
     |  
     |  right = <unbound qt slot right of QRect type>
     |      X.right(a) -> int
     |  
     |  setBottom = <unbound qt slot setBottom of QRect type>
     |      X.setBottom(a, b)
     |  
     |  setBottomLeft = <unbound qt slot setBottomLeft of QRect type>
     |      X.setBottomLeft(a, b)
     |  
     |  setBottomRight = <unbound qt slot setBottomRight of QRect type>
     |      X.setBottomRight(a, b)
     |  
     |  setCoords = <unbound qt slot setCoords of QRect type>
     |      X.setCoords(a, b, c, d, e)
     |  
     |  setHeight = <unbound qt slot setHeight of QRect type>
     |      X.setHeight(a, b)
     |  
     |  setLeft = <unbound qt slot setLeft of QRect type>
     |      X.setLeft(a, b)
     |  
     |  setRect = <unbound qt slot setRect of QRect type>
     |      X.setRect(a, b, c, d, e)
     |  
     |  setRight = <unbound qt slot setRight of QRect type>
     |      X.setRight(a, b)
     |  
     |  setSize = <unbound qt slot setSize of QRect type>
     |      X.setSize(a, b)
     |  
     |  setTop = <unbound qt slot setTop of QRect type>
     |      X.setTop(a, b)
     |  
     |  setTopLeft = <unbound qt slot setTopLeft of QRect type>
     |      X.setTopLeft(a, b)
     |  
     |  setTopRight = <unbound qt slot setTopRight of QRect type>
     |      X.setTopRight(a, b)
     |  
     |  setWidth = <unbound qt slot setWidth of QRect type>
     |      X.setWidth(a, b)
     |  
     |  setX = <unbound qt slot setX of QRect type>
     |      X.setX(a, b)
     |  
     |  setY = <unbound qt slot setY of QRect type>
     |      X.setY(a, b)
     |  
     |  size = <unbound qt slot size of QRect type>
     |      X.size(a) -> PythonQt.QtCore.QSize
     |  
     |  top = <unbound qt slot top of QRect type>
     |      X.top(a) -> int
     |  
     |  topLeft = <unbound qt slot topLeft of QRect type>
     |      X.topLeft(a) -> PythonQt.QtCore.QPoint
     |  
     |  topRight = <unbound qt slot topRight of QRect type>
     |      X.topRight(a) -> PythonQt.QtCore.QPoint
     |  
     |  translate = <unbound qt slot translate of QRect type>
     |      X.translate(a, b, c)
     |  
     |  translated = <unbound qt slot translated of QRect type>
     |      X.translated(a, b, c) -> PythonQt.QtCore.QRect
     |  
     |  united = <unbound qt slot united of QRect type>
     |      X.united(a, b) -> PythonQt.QtCore.QRect
     |  
     |  width = <unbound qt slot width of QRect type>
     |      X.width(a) -> int
     |  
     |  writeTo = <unbound qt slot writeTo of QRect type>
     |      X.writeTo(a, b)
     |  
     |  x = <unbound qt slot x of QRect type>
     |      X.x(a) -> int
     |  
     |  y = <unbound qt slot y of QRect type>
     |      X.y(a) -> int
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __delattr__(...)
     |      x.__delattr__('name') <==> del x.name
     |  
     |  __ge__(...)
     |      x.__ge__(y) <==> x>=y
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __gt__(...)
     |      x.__gt__(y) <==> x>y
     |  
     |  __hash__(...)
     |      x.__hash__() <==> hash(x)
     |  
     |  __le__(...)
     |      x.__le__(y) <==> x<=y
     |  
     |  __lt__(...)
     |      x.__lt__(y) <==> x<y
     |  
     |  __ne__(...)
     |      x.__ne__(y) <==> x!=y
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __setattr__(...)
     |      x.__setattr__('name', value) <==> x.name = value
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __new__ = <built-in method __new__ of PythonQt.PythonQtClassWrapper ob...
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
    
    class QRectF(PythonQt.PythonQtInstanceWrapper)
     |  Method resolution order:
     |      QRectF
     |      PythonQt.PythonQtInstanceWrapper
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  __add__(...)
     |      x.__add__(y) <==> x+y
     |  
     |  __and__(...)
     |      x.__and__(y) <==> x&y
     |  
     |  __eq__(...)
     |      x.__eq__(y) <==> x==y
     |  
     |  __iadd__(...)
     |      x.__iadd__(y) <==> x+=y
     |  
     |  __iand__(...)
     |      x.__iand__(y) <==> x&=y
     |  
     |  __init__(...)
     |      x.__init__(...) initializes x; see help(type(x)) for signature
     |  
     |  __ior__(...)
     |      x.__ior__(y) <==> x|=y
     |  
     |  __isub__(...)
     |      x.__isub__(y) <==> x-=y
     |  
     |  __neg__(...)
     |      x.__neg__() <==> -x
     |  
     |  __nonzero__(...)
     |      x.__nonzero__() <==> x != 0
     |  
     |  __or__(...)
     |      x.__or__(y) <==> x|y
     |  
     |  __radd__(...)
     |      x.__radd__(y) <==> y+x
     |  
     |  __rand__(...)
     |      x.__rand__(y) <==> y&x
     |  
     |  __ror__(...)
     |      x.__ror__(y) <==> y|x
     |  
     |  __rsub__(...)
     |      x.__rsub__(y) <==> y-x
     |  
     |  __sub__(...)
     |      x.__sub__(y) <==> x-y
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  adjust = <unbound qt slot adjust of QRectF type>
     |      X.adjust(a, b, c, d, e)
     |  
     |  adjusted = <unbound qt slot adjusted of QRectF type>
     |      X.adjusted(a, b, c, d, e) -> PythonQt.QtCore.QRectF
     |  
     |  bottom = <unbound qt slot bottom of QRectF type>
     |      X.bottom(a) -> float
     |  
     |  bottomLeft = <unbound qt slot bottomLeft of QRectF type>
     |      X.bottomLeft(a) -> PythonQt.QtCore.QPointF
     |  
     |  bottomRight = <unbound qt slot bottomRight of QRectF type>
     |      X.bottomRight(a) -> PythonQt.QtCore.QPointF
     |  
     |  center = <unbound qt slot center of QRectF type>
     |      X.center(a) -> PythonQt.QtCore.QPointF
     |  
     |  className = <built-in method className of PythonQt.PythonQtClassWrappe...
     |      Return the classname of the object
     |  
     |  contains = <unbound qt slot contains of QRectF type>
     |      X.contains(a, b, c) -> bool
     |  
     |  delete = <built-in method delete of PythonQt.PythonQtClassWrapper obje...
     |      Deletes the given C++ object
     |  
     |  height = <unbound qt slot height of QRectF type>
     |      X.height(a) -> float
     |  
     |  help = <built-in method help of PythonQt.PythonQtClassWrapper object>
     |      Shows the help of available methods for this class
     |  
     |  inherits = <built-in method inherits of PythonQt.PythonQtClassWrapper ...
     |      Returns if the class inherits or is of given type name
     |  
     |  intersected = <unbound qt slot intersected of QRectF type>
     |      X.intersected(a, b) -> PythonQt.QtCore.QRectF
     |  
     |  intersects = <unbound qt slot intersects of QRectF type>
     |      X.intersects(a, b) -> bool
     |  
     |  isEmpty = <unbound qt slot isEmpty of QRectF type>
     |      X.isEmpty(a) -> bool
     |  
     |  isNull = <unbound qt slot isNull of QRectF type>
     |      X.isNull(a) -> bool
     |  
     |  isValid = <unbound qt slot isValid of QRectF type>
     |      X.isValid(a) -> bool
     |  
     |  left = <unbound qt slot left of QRectF type>
     |      X.left(a) -> float
     |  
     |  marginsAdded = <unbound qt slot marginsAdded of QRectF type>
     |      X.marginsAdded(a, b) -> PythonQt.QtCore.QRectF
     |  
     |  marginsRemoved = <unbound qt slot marginsRemoved of QRectF type>
     |      X.marginsRemoved(a, b) -> PythonQt.QtCore.QRectF
     |  
     |  moveBottom = <unbound qt slot moveBottom of QRectF type>
     |      X.moveBottom(a, b)
     |  
     |  moveBottomLeft = <unbound qt slot moveBottomLeft of QRectF type>
     |      X.moveBottomLeft(a, b)
     |  
     |  moveBottomRight = <unbound qt slot moveBottomRight of QRectF type>
     |      X.moveBottomRight(a, b)
     |  
     |  moveCenter = <unbound qt slot moveCenter of QRectF type>
     |      X.moveCenter(a, b)
     |  
     |  moveLeft = <unbound qt slot moveLeft of QRectF type>
     |      X.moveLeft(a, b)
     |  
     |  moveRight = <unbound qt slot moveRight of QRectF type>
     |      X.moveRight(a, b)
     |  
     |  moveTo = <unbound qt slot moveTo of QRectF type>
     |      X.moveTo(a, b, c)
     |  
     |  moveTop = <unbound qt slot moveTop of QRectF type>
     |      X.moveTop(a, b)
     |  
     |  moveTopLeft = <unbound qt slot moveTopLeft of QRectF type>
     |      X.moveTopLeft(a, b)
     |  
     |  moveTopRight = <unbound qt slot moveTopRight of QRectF type>
     |      X.moveTopRight(a, b)
     |  
     |  normalized = <unbound qt slot normalized of QRectF type>
     |      X.normalized(a) -> PythonQt.QtCore.QRectF
     |  
     |  readFrom = <unbound qt slot readFrom of QRectF type>
     |      X.readFrom(a, b)
     |  
     |  right = <unbound qt slot right of QRectF type>
     |      X.right(a) -> float
     |  
     |  setBottom = <unbound qt slot setBottom of QRectF type>
     |      X.setBottom(a, b)
     |  
     |  setBottomLeft = <unbound qt slot setBottomLeft of QRectF type>
     |      X.setBottomLeft(a, b)
     |  
     |  setBottomRight = <unbound qt slot setBottomRight of QRectF type>
     |      X.setBottomRight(a, b)
     |  
     |  setCoords = <unbound qt slot setCoords of QRectF type>
     |      X.setCoords(a, b, c, d, e)
     |  
     |  setHeight = <unbound qt slot setHeight of QRectF type>
     |      X.setHeight(a, b)
     |  
     |  setLeft = <unbound qt slot setLeft of QRectF type>
     |      X.setLeft(a, b)
     |  
     |  setRect = <unbound qt slot setRect of QRectF type>
     |      X.setRect(a, b, c, d, e)
     |  
     |  setRight = <unbound qt slot setRight of QRectF type>
     |      X.setRight(a, b)
     |  
     |  setSize = <unbound qt slot setSize of QRectF type>
     |      X.setSize(a, b)
     |  
     |  setTop = <unbound qt slot setTop of QRectF type>
     |      X.setTop(a, b)
     |  
     |  setTopLeft = <unbound qt slot setTopLeft of QRectF type>
     |      X.setTopLeft(a, b)
     |  
     |  setTopRight = <unbound qt slot setTopRight of QRectF type>
     |      X.setTopRight(a, b)
     |  
     |  setWidth = <unbound qt slot setWidth of QRectF type>
     |      X.setWidth(a, b)
     |  
     |  setX = <unbound qt slot setX of QRectF type>
     |      X.setX(a, b)
     |  
     |  setY = <unbound qt slot setY of QRectF type>
     |      X.setY(a, b)
     |  
     |  size = <unbound qt slot size of QRectF type>
     |      X.size(a) -> PythonQt.QtCore.QSizeF
     |  
     |  toAlignedRect = <unbound qt slot toAlignedRect of QRectF type>
     |      X.toAlignedRect(a) -> PythonQt.QtCore.QRect
     |  
     |  toRect = <unbound qt slot toRect of QRectF type>
     |      X.toRect(a) -> PythonQt.QtCore.QRect
     |  
     |  top = <unbound qt slot top of QRectF type>
     |      X.top(a) -> float
     |  
     |  topLeft = <unbound qt slot topLeft of QRectF type>
     |      X.topLeft(a) -> PythonQt.QtCore.QPointF
     |  
     |  topRight = <unbound qt slot topRight of QRectF type>
     |      X.topRight(a) -> PythonQt.QtCore.QPointF
     |  
     |  translate = <unbound qt slot translate of QRectF type>
     |      X.translate(a, b, c)
     |  
     |  translated = <unbound qt slot translated of QRectF type>
     |      X.translated(a, b, c) -> PythonQt.QtCore.QRectF
     |  
     |  united = <unbound qt slot united of QRectF type>
     |      X.united(a, b) -> PythonQt.QtCore.QRectF
     |  
     |  width = <unbound qt slot width of QRectF type>
     |      X.width(a) -> float
     |  
     |  writeTo = <unbound qt slot writeTo of QRectF type>
     |      X.writeTo(a, b)
     |  
     |  x = <unbound qt slot x of QRectF type>
     |      X.x(a) -> float
     |  
     |  y = <unbound qt slot y of QRectF type>
     |      X.y(a) -> float
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __delattr__(...)
     |      x.__delattr__('name') <==> del x.name
     |  
     |  __ge__(...)
     |      x.__ge__(y) <==> x>=y
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __gt__(...)
     |      x.__gt__(y) <==> x>y
     |  
     |  __hash__(...)
     |      x.__hash__() <==> hash(x)
     |  
     |  __le__(...)
     |      x.__le__(y) <==> x<=y
     |  
     |  __lt__(...)
     |      x.__lt__(y) <==> x<y
     |  
     |  __ne__(...)
     |      x.__ne__(y) <==> x!=y
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __setattr__(...)
     |      x.__setattr__('name', value) <==> x.name = value
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __new__ = <built-in method __new__ of PythonQt.PythonQtClassWrapper ob...
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
    
    class QRegExp(PythonQt.PythonQtInstanceWrapper)
     |  Method resolution order:
     |      QRegExp
     |      PythonQt.PythonQtInstanceWrapper
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  __eq__(...)
     |      x.__eq__(y) <==> x==y
     |  
     |  __init__(...)
     |      x.__init__(...) initializes x; see help(type(x)) for signature
     |  
     |  __ne__(...)
     |      x.__ne__(y) <==> x!=y
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  CaretAtOffset = 1
     |  
     |  CaretAtZero = 0
     |  
     |  CaretMode = <class 'PythonQt.QtCore.CaretMode'>
     |  
     |  
     |  CaretWontMatch = 2
     |  
     |  FixedString = 2
     |  
     |  PatternSyntax = <class 'PythonQt.QtCore.PatternSyntax'>
     |  
     |  
     |  RegExp = 0
     |  
     |  RegExp2 = 3
     |  
     |  W3CXmlSchema11 = 5
     |  
     |  Wildcard = 1
     |  
     |  WildcardUnix = 4
     |  
     |  cap = <unbound qt slot cap of QRegExp type>
     |      X.cap(a, b) -> str
     |  
     |  captureCount = <unbound qt slot captureCount of QRegExp type>
     |      X.captureCount(a) -> int
     |  
     |  capturedTexts = <unbound qt slot capturedTexts of QRegExp type>
     |      X.capturedTexts(a) -> tuple
     |  
     |  caseSensitivity = <unbound qt slot caseSensitivity of QRegExp type>
     |      X.caseSensitivity(a)
     |  
     |  className = <built-in method className of PythonQt.PythonQtClassWrappe...
     |      Return the classname of the object
     |  
     |  delete = <built-in method delete of PythonQt.PythonQtClassWrapper obje...
     |      Deletes the given C++ object
     |  
     |  errorString = <unbound qt slot errorString of QRegExp type>
     |      X.errorString(a) -> str
     |  
     |  escape = <unbound qt slot static_QRegExp_escape of QRegExp type>
     |      X.escape(a) -> str
     |  
     |  exactMatch = <unbound qt slot exactMatch of QRegExp type>
     |      X.exactMatch(a, b) -> bool
     |  
     |  help = <built-in method help of PythonQt.PythonQtClassWrapper object>
     |      Shows the help of available methods for this class
     |  
     |  indexIn = <unbound qt slot indexIn of QRegExp type>
     |      X.indexIn(a, b, c, d) -> int
     |  
     |  inherits = <built-in method inherits of PythonQt.PythonQtClassWrapper ...
     |      Returns if the class inherits or is of given type name
     |  
     |  isEmpty = <unbound qt slot isEmpty of QRegExp type>
     |      X.isEmpty(a) -> bool
     |  
     |  isMinimal = <unbound qt slot isMinimal of QRegExp type>
     |      X.isMinimal(a) -> bool
     |  
     |  isValid = <unbound qt slot isValid of QRegExp type>
     |      X.isValid(a) -> bool
     |  
     |  lastIndexIn = <unbound qt slot lastIndexIn of QRegExp type>
     |      X.lastIndexIn(a, b, c, d) -> int
     |  
     |  matchedLength = <unbound qt slot matchedLength of QRegExp type>
     |      X.matchedLength(a) -> int
     |  
     |  pattern = <unbound qt slot pattern of QRegExp type>
     |      X.pattern(a) -> str
     |  
     |  patternSyntax = <unbound qt slot patternSyntax of QRegExp type>
     |      X.patternSyntax(a)
     |  
     |  pos = <unbound qt slot pos of QRegExp type>
     |      X.pos(a, b) -> int
     |  
     |  readFrom = <unbound qt slot readFrom of QRegExp type>
     |      X.readFrom(a, b)
     |  
     |  setCaseSensitivity = <unbound qt slot setCaseSensitivity of QRegExp ty...
     |      X.setCaseSensitivity(a, b)
     |  
     |  setMinimal = <unbound qt slot setMinimal of QRegExp type>
     |      X.setMinimal(a, b)
     |  
     |  setPattern = <unbound qt slot setPattern of QRegExp type>
     |      X.setPattern(a, b)
     |  
     |  setPatternSyntax = <unbound qt slot setPatternSyntax of QRegExp type>
     |      X.setPatternSyntax(a, b)
     |  
     |  swap = <unbound qt slot swap of QRegExp type>
     |      X.swap(a, b)
     |  
     |  writeTo = <unbound qt slot writeTo of QRegExp type>
     |      X.writeTo(a, b)
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __delattr__(...)
     |      x.__delattr__('name') <==> del x.name
     |  
     |  __ge__(...)
     |      x.__ge__(y) <==> x>=y
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __gt__(...)
     |      x.__gt__(y) <==> x>y
     |  
     |  __hash__(...)
     |      x.__hash__() <==> hash(x)
     |  
     |  __le__(...)
     |      x.__le__(y) <==> x<=y
     |  
     |  __lt__(...)
     |      x.__lt__(y) <==> x<y
     |  
     |  __nonzero__(...)
     |      x.__nonzero__() <==> x != 0
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __setattr__(...)
     |      x.__setattr__('name', value) <==> x.name = value
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __new__ = <built-in method __new__ of PythonQt.PythonQtClassWrapper ob...
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
    
    class QRegularExpression(PythonQt.PythonQtInstanceWrapper)
     |  Method resolution order:
     |      QRegularExpression
     |      PythonQt.PythonQtInstanceWrapper
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  __eq__(...)
     |      x.__eq__(y) <==> x==y
     |  
     |  __init__(...)
     |      x.__init__(...) initializes x; see help(type(x)) for signature
     |  
     |  __ne__(...)
     |      x.__ne__(y) <==> x!=y
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  AnchoredMatchOption = 1
     |  
     |  CaseInsensitiveOption = 1
     |  
     |  DontAutomaticallyOptimizeOption = 256
     |  
     |  DontCaptureOption = 32
     |  
     |  DontCheckSubjectStringMatchOption = 2
     |  
     |  DotMatchesEverythingOption = 2
     |  
     |  ExtendedPatternSyntaxOption = 8
     |  
     |  InvertedGreedinessOption = 16
     |  
     |  MatchOption = <class 'PythonQt.QtCore.MatchOption'>
     |  
     |  
     |  MatchOptions = <class 'PythonQt.QtCore.MatchOptions'>
     |  
     |  
     |  MatchType = <class 'PythonQt.QtCore.MatchType'>
     |  
     |  
     |  MultilineOption = 4
     |  
     |  NoMatch = 3
     |  
     |  NoMatchOption = 0
     |  
     |  NoPatternOption = 0
     |  
     |  NormalMatch = 0
     |  
     |  OptimizeOnFirstUsageOption = 128
     |  
     |  PartialPreferCompleteMatch = 1
     |  
     |  PartialPreferFirstMatch = 2
     |  
     |  PatternOption = <class 'PythonQt.QtCore.PatternOption'>
     |  
     |  
     |  PatternOptions = <class 'PythonQt.QtCore.PatternOptions'>
     |  
     |  
     |  UseUnicodePropertiesOption = 64
     |  
     |  captureCount = <unbound qt slot captureCount of QRegularExpression typ...
     |      X.captureCount(a) -> int
     |  
     |  className = <built-in method className of PythonQt.PythonQtClassWrappe...
     |      Return the classname of the object
     |  
     |  delete = <built-in method delete of PythonQt.PythonQtClassWrapper obje...
     |      Deletes the given C++ object
     |  
     |  errorString = <unbound qt slot errorString of QRegularExpression type>
     |      X.errorString(a) -> str
     |  
     |  escape = <unbound qt slot static_QRegularExpression_escape of QRegular...
     |      X.escape(a) -> str
     |  
     |  globalMatch = <unbound qt slot globalMatch of QRegularExpression type>
     |      X.globalMatch(a, b, c, d, e) -> PythonQt.QtCore.QRegularExpressionMatchIterator
     |  
     |  help = <built-in method help of PythonQt.PythonQtClassWrapper object>
     |      Shows the help of available methods for this class
     |  
     |  inherits = <built-in method inherits of PythonQt.PythonQtClassWrapper ...
     |      Returns if the class inherits or is of given type name
     |  
     |  isValid = <unbound qt slot isValid of QRegularExpression type>
     |      X.isValid(a) -> bool
     |  
     |  match = <unbound qt slot match of QRegularExpression type>
     |      X.match(a, b, c, d, e) -> PythonQt.QtCore.QRegularExpressionMatch
     |  
     |  namedCaptureGroups = <unbound qt slot namedCaptureGroups of QRegularEx...
     |      X.namedCaptureGroups(a) -> tuple
     |  
     |  operator_assign = <unbound qt slot operator_assign of QRegularExpressi...
     |      X.operator_assign(a, b) -> PythonQt.QtCore.QRegularExpression
     |  
     |  optimize = <unbound qt slot optimize of QRegularExpression type>
     |      X.optimize(a)
     |  
     |  pattern = <unbound qt slot pattern of QRegularExpression type>
     |      X.pattern(a) -> str
     |  
     |  patternErrorOffset = <unbound qt slot patternErrorOffset of QRegularEx...
     |      X.patternErrorOffset(a) -> int
     |  
     |  patternOptions = <unbound qt slot patternOptions of QRegularExpression...
     |      X.patternOptions(a)
     |  
     |  readFrom = <unbound qt slot readFrom of QRegularExpression type>
     |      X.readFrom(a, b)
     |  
     |  setPattern = <unbound qt slot setPattern of QRegularExpression type>
     |      X.setPattern(a, b)
     |  
     |  setPatternOptions = <unbound qt slot setPatternOptions of QRegularExpr...
     |      X.setPatternOptions(a, b)
     |  
     |  swap = <unbound qt slot swap of QRegularExpression type>
     |      X.swap(a, b)
     |  
     |  writeTo = <unbound qt slot writeTo of QRegularExpression type>
     |      X.writeTo(a, b)
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __delattr__(...)
     |      x.__delattr__('name') <==> del x.name
     |  
     |  __ge__(...)
     |      x.__ge__(y) <==> x>=y
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __gt__(...)
     |      x.__gt__(y) <==> x>y
     |  
     |  __hash__(...)
     |      x.__hash__() <==> hash(x)
     |  
     |  __le__(...)
     |      x.__le__(y) <==> x<=y
     |  
     |  __lt__(...)
     |      x.__lt__(y) <==> x<y
     |  
     |  __nonzero__(...)
     |      x.__nonzero__() <==> x != 0
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __setattr__(...)
     |      x.__setattr__('name', value) <==> x.name = value
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __new__ = <built-in method __new__ of PythonQt.PythonQtClassWrapper ob...
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
    
    class QRegularExpressionMatch(PythonQt.PythonQtInstanceWrapper)
     |  Method resolution order:
     |      QRegularExpressionMatch
     |      PythonQt.PythonQtInstanceWrapper
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  __init__(...)
     |      x.__init__(...) initializes x; see help(type(x)) for signature
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  captured = <unbound qt slot captured of QRegularExpressionMatch type>
     |      X.captured(a, b) -> str
     |  
     |  capturedEnd = <unbound qt slot capturedEnd of QRegularExpressionMatch ...
     |      X.capturedEnd(a, b) -> int
     |  
     |  capturedLength = <unbound qt slot capturedLength of QRegularExpression...
     |      X.capturedLength(a, b) -> int
     |  
     |  capturedRef = <unbound qt slot capturedRef of QRegularExpressionMatch ...
     |      X.capturedRef(a, b)
     |  
     |  capturedStart = <unbound qt slot capturedStart of QRegularExpressionMa...
     |      X.capturedStart(a, b) -> int
     |  
     |  capturedTexts = <unbound qt slot capturedTexts of QRegularExpressionMa...
     |      X.capturedTexts(a) -> tuple
     |  
     |  className = <built-in method className of PythonQt.PythonQtClassWrappe...
     |      Return the classname of the object
     |  
     |  delete = <built-in method delete of PythonQt.PythonQtClassWrapper obje...
     |      Deletes the given C++ object
     |  
     |  hasMatch = <unbound qt slot hasMatch of QRegularExpressionMatch type>
     |      X.hasMatch(a) -> bool
     |  
     |  hasPartialMatch = <unbound qt slot hasPartialMatch of QRegularExpressi...
     |      X.hasPartialMatch(a) -> bool
     |  
     |  help = <built-in method help of PythonQt.PythonQtClassWrapper object>
     |      Shows the help of available methods for this class
     |  
     |  inherits = <built-in method inherits of PythonQt.PythonQtClassWrapper ...
     |      Returns if the class inherits or is of given type name
     |  
     |  isValid = <unbound qt slot isValid of QRegularExpressionMatch type>
     |      X.isValid(a) -> bool
     |  
     |  lastCapturedIndex = <unbound qt slot lastCapturedIndex of QRegularExpr...
     |      X.lastCapturedIndex(a) -> int
     |  
     |  matchOptions = <unbound qt slot matchOptions of QRegularExpressionMatc...
     |      X.matchOptions(a)
     |  
     |  matchType = <unbound qt slot matchType of QRegularExpressionMatch type...
     |      X.matchType(a)
     |  
     |  operator_assign = <unbound qt slot operator_assign of QRegularExpressi...
     |      X.operator_assign(a, b) -> PythonQt.QtCore.QRegularExpressionMatch
     |  
     |  regularExpression = <unbound qt slot regularExpression of QRegularExpr...
     |      X.regularExpression(a) -> PythonQt.QtCore.QRegularExpression
     |  
     |  swap = <unbound qt slot swap of QRegularExpressionMatch type>
     |      X.swap(a, b)
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __delattr__(...)
     |      x.__delattr__('name') <==> del x.name
     |  
     |  __eq__(...)
     |      x.__eq__(y) <==> x==y
     |  
     |  __ge__(...)
     |      x.__ge__(y) <==> x>=y
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __gt__(...)
     |      x.__gt__(y) <==> x>y
     |  
     |  __hash__(...)
     |      x.__hash__() <==> hash(x)
     |  
     |  __le__(...)
     |      x.__le__(y) <==> x<=y
     |  
     |  __lt__(...)
     |      x.__lt__(y) <==> x<y
     |  
     |  __ne__(...)
     |      x.__ne__(y) <==> x!=y
     |  
     |  __nonzero__(...)
     |      x.__nonzero__() <==> x != 0
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __setattr__(...)
     |      x.__setattr__('name', value) <==> x.name = value
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __new__ = <built-in method __new__ of PythonQt.PythonQtClassWrapper ob...
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
    
    class QRegularExpressionMatchIterator(PythonQt.PythonQtInstanceWrapper)
     |  Method resolution order:
     |      QRegularExpressionMatchIterator
     |      PythonQt.PythonQtInstanceWrapper
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  __init__(...)
     |      x.__init__(...) initializes x; see help(type(x)) for signature
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  className = <built-in method className of PythonQt.PythonQtClassWrappe...
     |      Return the classname of the object
     |  
     |  delete = <built-in method delete of PythonQt.PythonQtClassWrapper obje...
     |      Deletes the given C++ object
     |  
     |  hasNext = <unbound qt slot hasNext of QRegularExpressionMatchIterator ...
     |      X.hasNext(a) -> bool
     |  
     |  help = <built-in method help of PythonQt.PythonQtClassWrapper object>
     |      Shows the help of available methods for this class
     |  
     |  inherits = <built-in method inherits of PythonQt.PythonQtClassWrapper ...
     |      Returns if the class inherits or is of given type name
     |  
     |  isValid = <unbound qt slot isValid of QRegularExpressionMatchIterator ...
     |      X.isValid(a) -> bool
     |  
     |  matchOptions = <unbound qt slot matchOptions of QRegularExpressionMatc...
     |      X.matchOptions(a)
     |  
     |  matchType = <unbound qt slot matchType of QRegularExpressionMatchItera...
     |      X.matchType(a)
     |  
     |  next = <unbound qt slot next of QRegularExpressionMatchIterator type>
     |      X.next(a) -> PythonQt.QtCore.QRegularExpressionMatch
     |  
     |  operator_assign = <unbound qt slot operator_assign of QRegularExpressi...
     |      X.operator_assign(a, b) -> PythonQt.QtCore.QRegularExpressionMatchIterator
     |  
     |  peekNext = <unbound qt slot peekNext of QRegularExpressionMatchIterato...
     |      X.peekNext(a) -> PythonQt.QtCore.QRegularExpressionMatch
     |  
     |  regularExpression = <unbound qt slot regularExpression of QRegularExpr...
     |      X.regularExpression(a) -> PythonQt.QtCore.QRegularExpression
     |  
     |  swap = <unbound qt slot swap of QRegularExpressionMatchIterator type>
     |      X.swap(a, b)
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __delattr__(...)
     |      x.__delattr__('name') <==> del x.name
     |  
     |  __eq__(...)
     |      x.__eq__(y) <==> x==y
     |  
     |  __ge__(...)
     |      x.__ge__(y) <==> x>=y
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __gt__(...)
     |      x.__gt__(y) <==> x>y
     |  
     |  __hash__(...)
     |      x.__hash__() <==> hash(x)
     |  
     |  __le__(...)
     |      x.__le__(y) <==> x<=y
     |  
     |  __lt__(...)
     |      x.__lt__(y) <==> x<y
     |  
     |  __ne__(...)
     |      x.__ne__(y) <==> x!=y
     |  
     |  __nonzero__(...)
     |      x.__nonzero__() <==> x != 0
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __setattr__(...)
     |      x.__setattr__('name', value) <==> x.name = value
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __new__ = <built-in method __new__ of PythonQt.PythonQtClassWrapper ob...
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
    
    class QResource(PythonQt.PythonQtInstanceWrapper)
     |  Method resolution order:
     |      QResource
     |      PythonQt.PythonQtInstanceWrapper
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  __init__(...)
     |      x.__init__(...) initializes x; see help(type(x)) for signature
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  absoluteFilePath = <unbound qt slot absoluteFilePath of QResource type...
     |      X.absoluteFilePath(a) -> str
     |  
     |  addSearchPath = <unbound qt slot static_QResource_addSearchPath of QRe...
     |      X.addSearchPath(a)
     |  
     |  children = <unbound qt slot children of QResource type>
     |      X.children(a) -> tuple
     |  
     |  className = <built-in method className of PythonQt.PythonQtClassWrappe...
     |      Return the classname of the object
     |  
     |  data = <unbound qt slot data of QResource type>
     |      X.data(a) -> int
     |  
     |  delete = <built-in method delete of PythonQt.PythonQtClassWrapper obje...
     |      Deletes the given C++ object
     |  
     |  fileName = <unbound qt slot fileName of QResource type>
     |      X.fileName(a) -> str
     |  
     |  help = <built-in method help of PythonQt.PythonQtClassWrapper object>
     |      Shows the help of available methods for this class
     |  
     |  inherits = <built-in method inherits of PythonQt.PythonQtClassWrapper ...
     |      Returns if the class inherits or is of given type name
     |  
     |  isCompressed = <unbound qt slot isCompressed of QResource type>
     |      X.isCompressed(a) -> bool
     |  
     |  isDir = <unbound qt slot isDir of QResource type>
     |      X.isDir(a) -> bool
     |  
     |  isFile = <unbound qt slot isFile of QResource type>
     |      X.isFile(a) -> bool
     |  
     |  isValid = <unbound qt slot isValid of QResource type>
     |      X.isValid(a) -> bool
     |  
     |  locale = <unbound qt slot locale of QResource type>
     |      X.locale(a) -> PythonQt.QtCore.QLocale
     |  
     |  registerResource = <unbound qt slot static_QResource_registerResource ...
     |      X.registerResource(a, b) -> bool
     |  
     |  searchPaths = <unbound qt slot static_QResource_searchPaths of QResour...
     |      X.searchPaths() -> tuple
     |  
     |  setFileName = <unbound qt slot setFileName of QResource type>
     |      X.setFileName(a, b)
     |  
     |  setLocale = <unbound qt slot setLocale of QResource type>
     |      X.setLocale(a, b)
     |  
     |  size = <unbound qt slot size of QResource type>
     |      X.size(a) -> int
     |  
     |  unregisterResource = <unbound qt slot static_QResource_unregisterResou...
     |      X.unregisterResource(a, b) -> bool
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __delattr__(...)
     |      x.__delattr__('name') <==> del x.name
     |  
     |  __eq__(...)
     |      x.__eq__(y) <==> x==y
     |  
     |  __ge__(...)
     |      x.__ge__(y) <==> x>=y
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __gt__(...)
     |      x.__gt__(y) <==> x>y
     |  
     |  __hash__(...)
     |      x.__hash__() <==> hash(x)
     |  
     |  __le__(...)
     |      x.__le__(y) <==> x<=y
     |  
     |  __lt__(...)
     |      x.__lt__(y) <==> x<y
     |  
     |  __ne__(...)
     |      x.__ne__(y) <==> x!=y
     |  
     |  __nonzero__(...)
     |      x.__nonzero__() <==> x != 0
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __setattr__(...)
     |      x.__setattr__('name', value) <==> x.name = value
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __new__ = <built-in method __new__ of PythonQt.PythonQtClassWrapper ob...
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
    
    class QRunnable(PythonQt.PythonQtInstanceWrapper)
     |  Method resolution order:
     |      QRunnable
     |      PythonQt.PythonQtInstanceWrapper
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  __init__(...)
     |      x.__init__(...) initializes x; see help(type(x)) for signature
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  autoDelete = <unbound qt slot autoDelete of QRunnable type>
     |      X.autoDelete(a) -> bool
     |  
     |  className = <built-in method className of PythonQt.PythonQtClassWrappe...
     |      Return the classname of the object
     |  
     |  delete = <built-in method delete of PythonQt.PythonQtClassWrapper obje...
     |      Deletes the given C++ object
     |  
     |  help = <built-in method help of PythonQt.PythonQtClassWrapper object>
     |      Shows the help of available methods for this class
     |  
     |  inherits = <built-in method inherits of PythonQt.PythonQtClassWrapper ...
     |      Returns if the class inherits or is of given type name
     |  
     |  run = <unbound qt slot py_q_run of QRunnable type>
     |      X.run(a)
     |  
     |  setAutoDelete = <unbound qt slot setAutoDelete of QRunnable type>
     |      X.setAutoDelete(a, b)
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __delattr__(...)
     |      x.__delattr__('name') <==> del x.name
     |  
     |  __eq__(...)
     |      x.__eq__(y) <==> x==y
     |  
     |  __ge__(...)
     |      x.__ge__(y) <==> x>=y
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __gt__(...)
     |      x.__gt__(y) <==> x>y
     |  
     |  __hash__(...)
     |      x.__hash__() <==> hash(x)
     |  
     |  __le__(...)
     |      x.__le__(y) <==> x<=y
     |  
     |  __lt__(...)
     |      x.__lt__(y) <==> x<y
     |  
     |  __ne__(...)
     |      x.__ne__(y) <==> x!=y
     |  
     |  __nonzero__(...)
     |      x.__nonzero__() <==> x != 0
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __setattr__(...)
     |      x.__setattr__('name', value) <==> x.name = value
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __new__ = <built-in method __new__ of PythonQt.PythonQtClassWrapper ob...
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
    
    class QSaveFile(PythonQt.PythonQtInstanceWrapper)
     |  Method resolution order:
     |      QSaveFile
     |      PythonQt.PythonQtInstanceWrapper
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  __init__(...)
     |      x.__init__(...) initializes x; see help(type(x)) for signature
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  AbortError = 6
     |  
     |  Append = 4
     |  
     |  AutoCloseHandle = 1
     |  
     |  CopyError = 14
     |  
     |  DontCloseHandle = 0
     |  
     |  ExeGroup = 16
     |  
     |  ExeOther = 1
     |  
     |  ExeOwner = 4096
     |  
     |  ExeUser = 256
     |  
     |  FatalError = 3
     |  
     |  FileError = <class 'PythonQt.QtCore.FileError'>
     |  
     |  
     |  FileHandleFlag = <class 'PythonQt.QtCore.FileHandleFlag'>
     |  
     |  
     |  FileHandleFlags = <class 'PythonQt.QtCore.FileHandleFlags'>
     |  
     |  
     |  MapPrivateOption = 1
     |  
     |  MemoryMapFlags = <class 'PythonQt.QtCore.MemoryMapFlags'>
     |  
     |  
     |  NoError = 0
     |  
     |  NoOptions = 0
     |  
     |  NotOpen = 0
     |  
     |  OpenError = 5
     |  
     |  OpenMode = <class 'PythonQt.QtCore.OpenMode'>
     |  
     |  
     |  OpenModeFlag = <class 'PythonQt.QtCore.OpenModeFlag'>
     |  
     |  
     |  Permission = <class 'PythonQt.QtCore.Permission'>
     |  
     |  
     |  Permissions = <class 'PythonQt.QtCore.Permissions'>
     |  
     |  
     |  PermissionsError = 13
     |  
     |  PositionError = 11
     |  
     |  ReadError = 1
     |  
     |  ReadGroup = 64
     |  
     |  ReadOnly = 1
     |  
     |  ReadOther = 4
     |  
     |  ReadOwner = 16384
     |  
     |  ReadUser = 1024
     |  
     |  ReadWrite = 3
     |  
     |  RemoveError = 9
     |  
     |  RenameError = 10
     |  
     |  ResizeError = 12
     |  
     |  ResourceError = 4
     |  
     |  Text = 16
     |  
     |  TimeOutError = 7
     |  
     |  Truncate = 8
     |  
     |  Unbuffered = 32
     |  
     |  UnspecifiedError = 8
     |  
     |  WriteError = 2
     |  
     |  WriteGroup = 32
     |  
     |  WriteOnly = 2
     |  
     |  WriteOther = 2
     |  
     |  WriteOwner = 8192
     |  
     |  WriteUser = 512
     |  
     |  aboutToClose = <unbound qt signal aboutToClose of QSaveFile type>
     |  
     |  
     |  atEnd = <unbound qt slot py_q_atEnd of QSaveFile type>
     |      X.atEnd(a) -> bool
     |  
     |  blockSignals = <unbound qt slot blockSignals of QSaveFile type>
     |      X.blockSignals(a, b) -> bool
     |  
     |  bytesAvailable = <unbound qt slot py_q_bytesAvailable of QSaveFile typ...
     |      X.bytesAvailable(a) -> int
     |  
     |  bytesToWrite = <unbound qt slot py_q_bytesToWrite of QSaveFile type>
     |      X.bytesToWrite(a) -> int
     |  
     |  bytesWritten = <unbound qt signal bytesWritten of QSaveFile type>
     |  
     |  
     |  canReadLine = <unbound qt slot py_q_canReadLine of QSaveFile type>
     |      X.canReadLine(a) -> bool
     |  
     |  cancelWriting = <unbound qt slot cancelWriting of QSaveFile type>
     |      X.cancelWriting(a)
     |  
     |  channelBytesWritten = <unbound qt signal channelBytesWritten of QSaveF...
     |  
     |  
     |  channelReadyRead = <unbound qt signal channelReadyRead of QSaveFile ty...
     |  
     |  
     |  childEvent = <unbound qt slot py_q_childEvent of QSaveFile type>
     |      X.childEvent(a, b)
     |  
     |  children = <unbound qt slot children of QSaveFile type>
     |      X.children(a) -> tuple
     |  
     |  className = <built-in method className of PythonQt.PythonQtClassWrappe...
     |      Return the classname of the object
     |  
     |  close = <unbound qt slot py_q_close of QSaveFile type>
     |      X.close(a)
     |  
     |  commit = <unbound qt slot commit of QSaveFile type>
     |      X.commit(a) -> bool
     |  
     |  connect = <unbound qt slot connect of QSaveFile type>
     |      X.connect(a, b, c, d, e) -> bool
     |  
     |  customEvent = <unbound qt slot py_q_customEvent of QSaveFile type>
     |      X.customEvent(a, b)
     |  
     |  delete = <built-in method delete of PythonQt.PythonQtClassWrapper obje...
     |      Deletes the given C++ object
     |  
     |  deleteLater = <unbound qt slot deleteLater of QSaveFile type>
     |      X.deleteLater()
     |  
     |  destroyed = <unbound qt signal destroyed of QSaveFile type>
     |  
     |  
     |  directWriteFallback = <unbound qt slot directWriteFallback of QSaveFil...
     |      X.directWriteFallback(a) -> bool
     |  
     |  disconnect = <unbound qt slot disconnect of QSaveFile type>
     |      X.disconnect(a, b, c, d) -> bool
     |  
     |  dumpObjectInfo = <unbound qt slot dumpObjectInfo of QSaveFile type>
     |      X.dumpObjectInfo(a)
     |  
     |  dumpObjectTree = <unbound qt slot dumpObjectTree of QSaveFile type>
     |      X.dumpObjectTree(a)
     |  
     |  dynamicPropertyNames = <unbound qt slot dynamicPropertyNames of QSaveF...
     |      X.dynamicPropertyNames(a)
     |  
     |  error = <unbound qt slot error of QSaveFile type>
     |      X.error(a)
     |  
     |  errorString = <unbound qt slot errorString of QSaveFile type>
     |      X.errorString(a) -> str
     |  
     |  event = <unbound qt slot py_q_event of QSaveFile type>
     |      X.event(a, b) -> bool
     |  
     |  eventFilter = <unbound qt slot py_q_eventFilter of QSaveFile type>
     |      X.eventFilter(a, b, c) -> bool
     |  
     |  fileName = <unbound qt slot py_q_fileName of QSaveFile type>
     |      X.fileName(a) -> str
     |  
     |  findChild = <unbound qt slot findChild of QSaveFile type>
     |      X.findChild(a, b, c) -> PythonQt.private.QObject
     |  
     |  findChildren = <unbound qt slot findChildren of QSaveFile type>
     |      X.findChildren(a, b, c) -> tuple
     |  
     |  flush = <unbound qt slot flush of QSaveFile type>
     |      X.flush(a) -> bool
     |  
     |  getChar = <unbound qt slot getChar of QSaveFile type>
     |      X.getChar(a, b) -> bool
     |  
     |  handle = <unbound qt slot handle of QSaveFile type>
     |      X.handle(a) -> int
     |  
     |  help = <built-in method help of PythonQt.PythonQtClassWrapper object>
     |      Shows the help of available methods for this class
     |  
     |  inherits = <built-in method inherits of PythonQt.PythonQtClassWrapper ...
     |      Returns if the class inherits or is of given type name
     |  
     |  installEventFilter = <unbound qt slot installEventFilter of QSaveFile ...
     |      X.installEventFilter(a, b)
     |  
     |  isOpen = <unbound qt slot isOpen of QSaveFile type>
     |      X.isOpen(a) -> bool
     |  
     |  isReadable = <unbound qt slot isReadable of QSaveFile type>
     |      X.isReadable(a) -> bool
     |  
     |  isSequential = <unbound qt slot py_q_isSequential of QSaveFile type>
     |      X.isSequential(a) -> bool
     |  
     |  isSignalConnected = <unbound qt slot isSignalConnected of QSaveFile ty...
     |      X.isSignalConnected(a, b) -> bool
     |  
     |  isTextModeEnabled = <unbound qt slot isTextModeEnabled of QSaveFile ty...
     |      X.isTextModeEnabled(a) -> bool
     |  
     |  isWidgetType = <unbound qt slot isWidgetType of QSaveFile type>
     |      X.isWidgetType(a) -> bool
     |  
     |  isWindowType = <unbound qt slot isWindowType of QSaveFile type>
     |      X.isWindowType(a) -> bool
     |  
     |  isWritable = <unbound qt slot isWritable of QSaveFile type>
     |      X.isWritable(a) -> bool
     |  
     |  killTimer = <unbound qt slot killTimer of QSaveFile type>
     |      X.killTimer(a, b)
     |  
     |  map = <unbound qt slot map of QSaveFile type>
     |      X.map(a, b, c, d) -> int
     |  
     |  metaObject = <unbound qt slot metaObject of QSaveFile type>
     |      X.metaObject(a) -> PythonQt.QtCore.QMetaObject
     |  
     |  moveToThread = <unbound qt slot moveToThread of QSaveFile type>
     |      X.moveToThread(a, b)
     |  
     |  objectName = None
     |  
     |  objectNameChanged = <unbound qt signal objectNameChanged of QSaveFile ...
     |  
     |  
     |  open = <unbound qt slot py_q_open of QSaveFile type>
     |      X.open(a, b) -> bool
     |  
     |  openMode = <unbound qt slot openMode of QSaveFile type>
     |      X.openMode(a)
     |  
     |  parent = <unbound qt slot parent of QSaveFile type>
     |      X.parent(a) -> PythonQt.private.QObject
     |  
     |  peek = <unbound qt slot peek of QSaveFile type>
     |      X.peek(a, b) -> PythonQt.QtCore.QByteArray
     |  
     |  permissions = <unbound qt slot py_q_permissions of QSaveFile type>
     |      X.permissions(a)
     |  
     |  pos = <unbound qt slot py_q_pos of QSaveFile type>
     |      X.pos(a) -> int
     |  
     |  property = <unbound qt slot property of QSaveFile type>
     |      X.property(a, b) -> object
     |  
     |  putChar = <unbound qt slot putChar of QSaveFile type>
     |      X.putChar(a, b) -> bool
     |  
     |  read = <unbound qt slot read of QSaveFile type>
     |      X.read(a, b) -> PythonQt.QtCore.QByteArray
     |  
     |  readAll = <unbound qt slot readAll of QSaveFile type>
     |      X.readAll(a) -> PythonQt.QtCore.QByteArray
     |  
     |  readChannelFinished = <unbound qt signal readChannelFinished of QSaveF...
     |  
     |  
     |  readData = <unbound qt slot py_q_readData of QSaveFile type>
     |      X.readData(a, b, c) -> int
     |  
     |  readLine = <unbound qt slot readLine of QSaveFile type>
     |      X.readLine(a, b) -> PythonQt.QtCore.QByteArray
     |  
     |  readLineData = <unbound qt slot py_q_readLineData of QSaveFile type>
     |      X.readLineData(a, b, c) -> int
     |  
     |  readyRead = <unbound qt signal readyRead of QSaveFile type>
     |  
     |  
     |  removeEventFilter = <unbound qt slot removeEventFilter of QSaveFile ty...
     |      X.removeEventFilter(a, b)
     |  
     |  reset = <unbound qt slot py_q_reset of QSaveFile type>
     |      X.reset(a) -> bool
     |  
     |  resize = <unbound qt slot py_q_resize of QSaveFile type>
     |      X.resize(a, b) -> bool
     |  
     |  seek = <unbound qt slot py_q_seek of QSaveFile type>
     |      X.seek(a, b) -> bool
     |  
     |  sender = <unbound qt slot sender of QSaveFile type>
     |      X.sender(a) -> PythonQt.private.QObject
     |  
     |  senderSignalIndex = <unbound qt slot senderSignalIndex of QSaveFile ty...
     |      X.senderSignalIndex(a) -> int
     |  
     |  setDirectWriteFallback = <unbound qt slot setDirectWriteFallback of QS...
     |      X.setDirectWriteFallback(a, b)
     |  
     |  setErrorString = <unbound qt slot setErrorString of QSaveFile type>
     |      X.setErrorString(a, b)
     |  
     |  setFileName = <unbound qt slot setFileName of QSaveFile type>
     |      X.setFileName(a, b)
     |  
     |  setObjectName = <unbound qt slot setObjectName of QSaveFile type>
     |      X.setObjectName(a, b)
     |  
     |  setOpenMode = <unbound qt slot setOpenMode of QSaveFile type>
     |      X.setOpenMode(a, b)
     |  
     |  setParent = <unbound qt slot setParent of QSaveFile type>
     |      X.setParent(a, b)
     |  
     |  setPermissions = <unbound qt slot py_q_setPermissions of QSaveFile typ...
     |      X.setPermissions(a, b) -> bool
     |  
     |  setProperty = <unbound qt slot setProperty of QSaveFile type>
     |      X.setProperty(a, b, c) -> bool
     |  
     |  setTextModeEnabled = <unbound qt slot setTextModeEnabled of QSaveFile ...
     |      X.setTextModeEnabled(a, b)
     |  
     |  signalsBlocked = <unbound qt slot signalsBlocked of QSaveFile type>
     |      X.signalsBlocked(a) -> bool
     |  
     |  size = <unbound qt slot py_q_size of QSaveFile type>
     |      X.size(a) -> int
     |  
     |  startTimer = <unbound qt slot startTimer of QSaveFile type>
     |      X.startTimer(a, b, c) -> int
     |  
     |  thread = <unbound qt slot thread of QSaveFile type>
     |      X.thread(a)
     |  
     |  timerEvent = <unbound qt slot py_q_timerEvent of QSaveFile type>
     |      X.timerEvent(a, b)
     |  
     |  tr = <unbound qt slot tr of QSaveFile type>
     |      X.tr(a, b, c, d) -> str
     |  
     |  ungetChar = <unbound qt slot ungetChar of QSaveFile type>
     |      X.ungetChar(a, b)
     |  
     |  unmap = <unbound qt slot unmap of QSaveFile type>
     |      X.unmap(a, b) -> bool
     |  
     |  unsetError = <unbound qt slot unsetError of QSaveFile type>
     |      X.unsetError(a)
     |  
     |  waitForBytesWritten = <unbound qt slot py_q_waitForBytesWritten of QSa...
     |      X.waitForBytesWritten(a, b) -> bool
     |  
     |  waitForReadyRead = <unbound qt slot py_q_waitForReadyRead of QSaveFile...
     |      X.waitForReadyRead(a, b) -> bool
     |  
     |  write = <unbound qt slot write of QSaveFile type>
     |      X.write(a, b) -> int
     |  
     |  writeData = <unbound qt slot py_q_writeData of QSaveFile type>
     |      X.writeData(a, b, c) -> int
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __delattr__(...)
     |      x.__delattr__('name') <==> del x.name
     |  
     |  __eq__(...)
     |      x.__eq__(y) <==> x==y
     |  
     |  __ge__(...)
     |      x.__ge__(y) <==> x>=y
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __gt__(...)
     |      x.__gt__(y) <==> x>y
     |  
     |  __hash__(...)
     |      x.__hash__() <==> hash(x)
     |  
     |  __le__(...)
     |      x.__le__(y) <==> x<=y
     |  
     |  __lt__(...)
     |      x.__lt__(y) <==> x<y
     |  
     |  __ne__(...)
     |      x.__ne__(y) <==> x!=y
     |  
     |  __nonzero__(...)
     |      x.__nonzero__() <==> x != 0
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __setattr__(...)
     |      x.__setattr__('name', value) <==> x.name = value
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __new__ = <built-in method __new__ of PythonQt.PythonQtClassWrapper ob...
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
    
    class QSemaphore(PythonQt.PythonQtInstanceWrapper)
     |  Method resolution order:
     |      QSemaphore
     |      PythonQt.PythonQtInstanceWrapper
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  __init__(...)
     |      x.__init__(...) initializes x; see help(type(x)) for signature
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  acquire = <unbound qt slot acquire of QSemaphore type>
     |      X.acquire(a, b)
     |  
     |  available = <unbound qt slot available of QSemaphore type>
     |      X.available(a) -> int
     |  
     |  className = <built-in method className of PythonQt.PythonQtClassWrappe...
     |      Return the classname of the object
     |  
     |  delete = <built-in method delete of PythonQt.PythonQtClassWrapper obje...
     |      Deletes the given C++ object
     |  
     |  help = <built-in method help of PythonQt.PythonQtClassWrapper object>
     |      Shows the help of available methods for this class
     |  
     |  inherits = <built-in method inherits of PythonQt.PythonQtClassWrapper ...
     |      Returns if the class inherits or is of given type name
     |  
     |  release = <unbound qt slot release of QSemaphore type>
     |      X.release(a, b)
     |  
     |  tryAcquire = <unbound qt slot tryAcquire of QSemaphore type>
     |      X.tryAcquire(a, b, c) -> bool
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __delattr__(...)
     |      x.__delattr__('name') <==> del x.name
     |  
     |  __eq__(...)
     |      x.__eq__(y) <==> x==y
     |  
     |  __ge__(...)
     |      x.__ge__(y) <==> x>=y
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __gt__(...)
     |      x.__gt__(y) <==> x>y
     |  
     |  __hash__(...)
     |      x.__hash__() <==> hash(x)
     |  
     |  __le__(...)
     |      x.__le__(y) <==> x<=y
     |  
     |  __lt__(...)
     |      x.__lt__(y) <==> x<y
     |  
     |  __ne__(...)
     |      x.__ne__(y) <==> x!=y
     |  
     |  __nonzero__(...)
     |      x.__nonzero__() <==> x != 0
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __setattr__(...)
     |      x.__setattr__('name', value) <==> x.name = value
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __new__ = <built-in method __new__ of PythonQt.PythonQtClassWrapper ob...
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
    
    class QSequentialAnimationGroup(PythonQt.PythonQtInstanceWrapper)
     |  Method resolution order:
     |      QSequentialAnimationGroup
     |      PythonQt.PythonQtInstanceWrapper
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  __init__(...)
     |      x.__init__(...) initializes x; see help(type(x)) for signature
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  Backward = 1
     |  
     |  DeleteWhenStopped = 1
     |  
     |  DeletionPolicy = <class 'PythonQt.QtCore.DeletionPolicy'>
     |  
     |  
     |  Direction = <class 'PythonQt.QtCore.Direction'>
     |  
     |  
     |  Forward = 0
     |  
     |  KeepWhenStopped = 0
     |  
     |  Paused = 1
     |  
     |  Running = 2
     |  
     |  State = <class 'PythonQt.QtCore.State'>
     |  
     |  
     |  Stopped = 0
     |  
     |  addAnimation = <unbound qt slot addAnimation of QSequentialAnimationGr...
     |      X.addAnimation(a, b)
     |  
     |  addPause = <unbound qt slot addPause of QSequentialAnimationGroup type...
     |      X.addPause(a, b) -> PythonQt.QtCore.QPauseAnimation
     |  
     |  animationAt = <unbound qt slot animationAt of QSequentialAnimationGrou...
     |      X.animationAt(a, b) -> PythonQt.QtCore.QAbstractAnimation
     |  
     |  animationCount = <unbound qt slot animationCount of QSequentialAnimati...
     |      X.animationCount(a) -> int
     |  
     |  blockSignals = <unbound qt slot blockSignals of QSequentialAnimationGr...
     |      X.blockSignals(a, b) -> bool
     |  
     |  childEvent = <unbound qt slot py_q_childEvent of QSequentialAnimationG...
     |      X.childEvent(a, b)
     |  
     |  children = <unbound qt slot children of QSequentialAnimationGroup type...
     |      X.children(a) -> tuple
     |  
     |  className = <built-in method className of PythonQt.PythonQtClassWrappe...
     |      Return the classname of the object
     |  
     |  clear = <unbound qt slot clear of QSequentialAnimationGroup type>
     |      X.clear(a)
     |  
     |  connect = <unbound qt slot connect of QSequentialAnimationGroup type>
     |      X.connect(a, b, c, d, e) -> bool
     |  
     |  currentAnimation = QAbstractAnimation (QAbstractAnimation at: 0x0)
     |  
     |  currentAnimationChanged = <unbound qt signal currentAnimationChanged o...
     |  
     |  
     |  currentLoop = None
     |  
     |  currentLoopChanged = <unbound qt signal currentLoopChanged of QSequent...
     |  
     |  
     |  currentLoopTime = <unbound qt slot currentLoopTime of QSequentialAnima...
     |      X.currentLoopTime(a) -> int
     |  
     |  currentTime = None
     |  
     |  customEvent = <unbound qt slot py_q_customEvent of QSequentialAnimatio...
     |      X.customEvent(a, b)
     |  
     |  delete = <built-in method delete of PythonQt.PythonQtClassWrapper obje...
     |      Deletes the given C++ object
     |  
     |  deleteLater = <unbound qt slot deleteLater of QSequentialAnimationGrou...
     |      X.deleteLater()
     |  
     |  destroyed = <unbound qt signal destroyed of QSequentialAnimationGroup ...
     |  
     |  
     |  direction = None
     |  
     |  directionChanged = <unbound qt signal directionChanged of QSequentialA...
     |  
     |  
     |  disconnect = <unbound qt slot disconnect of QSequentialAnimationGroup ...
     |      X.disconnect(a, b, c, d) -> bool
     |  
     |  dumpObjectInfo = <unbound qt slot dumpObjectInfo of QSequentialAnimati...
     |      X.dumpObjectInfo(a)
     |  
     |  dumpObjectTree = <unbound qt slot dumpObjectTree of QSequentialAnimati...
     |      X.dumpObjectTree(a)
     |  
     |  duration = None
     |  
     |  dynamicPropertyNames = <unbound qt slot dynamicPropertyNames of QSeque...
     |      X.dynamicPropertyNames(a)
     |  
     |  event = <unbound qt slot py_q_event of QSequentialAnimationGroup type>
     |      X.event(a, b) -> bool
     |  
     |  eventFilter = <unbound qt slot py_q_eventFilter of QSequentialAnimatio...
     |      X.eventFilter(a, b, c) -> bool
     |  
     |  findChild = <unbound qt slot findChild of QSequentialAnimationGroup ty...
     |      X.findChild(a, b, c) -> PythonQt.private.QObject
     |  
     |  findChildren = <unbound qt slot findChildren of QSequentialAnimationGr...
     |      X.findChildren(a, b, c) -> tuple
     |  
     |  finished = <unbound qt signal finished of QSequentialAnimationGroup ty...
     |  
     |  
     |  group = <unbound qt slot group of QSequentialAnimationGroup type>
     |      X.group(a) -> PythonQt.QtCore.QAnimationGroup
     |  
     |  help = <built-in method help of PythonQt.PythonQtClassWrapper object>
     |      Shows the help of available methods for this class
     |  
     |  indexOfAnimation = <unbound qt slot indexOfAnimation of QSequentialAni...
     |      X.indexOfAnimation(a, b) -> int
     |  
     |  inherits = <built-in method inherits of PythonQt.PythonQtClassWrapper ...
     |      Returns if the class inherits or is of given type name
     |  
     |  insertAnimation = <unbound qt slot insertAnimation of QSequentialAnima...
     |      X.insertAnimation(a, b, c)
     |  
     |  insertPause = <unbound qt slot insertPause of QSequentialAnimationGrou...
     |      X.insertPause(a, b, c) -> PythonQt.QtCore.QPauseAnimation
     |  
     |  installEventFilter = <unbound qt slot installEventFilter of QSequentia...
     |      X.installEventFilter(a, b)
     |  
     |  isSignalConnected = <unbound qt slot isSignalConnected of QSequentialA...
     |      X.isSignalConnected(a, b) -> bool
     |  
     |  isWidgetType = <unbound qt slot isWidgetType of QSequentialAnimationGr...
     |      X.isWidgetType(a) -> bool
     |  
     |  isWindowType = <unbound qt slot isWindowType of QSequentialAnimationGr...
     |      X.isWindowType(a) -> bool
     |  
     |  killTimer = <unbound qt slot killTimer of QSequentialAnimationGroup ty...
     |      X.killTimer(a, b)
     |  
     |  loopCount = None
     |  
     |  metaObject = <unbound qt slot metaObject of QSequentialAnimationGroup ...
     |      X.metaObject(a) -> PythonQt.QtCore.QMetaObject
     |  
     |  moveToThread = <unbound qt slot moveToThread of QSequentialAnimationGr...
     |      X.moveToThread(a, b)
     |  
     |  objectName = None
     |  
     |  objectNameChanged = <unbound qt signal objectNameChanged of QSequentia...
     |  
     |  
     |  parent = <unbound qt slot parent of QSequentialAnimationGroup type>
     |      X.parent(a) -> PythonQt.private.QObject
     |  
     |  pause = <unbound qt slot pause of QSequentialAnimationGroup type>
     |      X.pause()
     |  
     |  property = <unbound qt slot property of QSequentialAnimationGroup type...
     |      X.property(a, b) -> object
     |  
     |  removeAnimation = <unbound qt slot removeAnimation of QSequentialAnima...
     |      X.removeAnimation(a, b)
     |  
     |  removeEventFilter = <unbound qt slot removeEventFilter of QSequentialA...
     |      X.removeEventFilter(a, b)
     |  
     |  resume = <unbound qt slot resume of QSequentialAnimationGroup type>
     |      X.resume()
     |  
     |  sender = <unbound qt slot sender of QSequentialAnimationGroup type>
     |      X.sender(a) -> PythonQt.private.QObject
     |  
     |  senderSignalIndex = <unbound qt slot senderSignalIndex of QSequentialA...
     |      X.senderSignalIndex(a) -> int
     |  
     |  setCurrentTime = <unbound qt slot setCurrentTime of QSequentialAnimati...
     |      X.setCurrentTime(a)
     |  
     |  setDirection = <unbound qt slot setDirection of QSequentialAnimationGr...
     |      X.setDirection(a, b)
     |  
     |  setLoopCount = <unbound qt slot setLoopCount of QSequentialAnimationGr...
     |      X.setLoopCount(a, b)
     |  
     |  setObjectName = <unbound qt slot setObjectName of QSequentialAnimation...
     |      X.setObjectName(a, b)
     |  
     |  setParent = <unbound qt slot setParent of QSequentialAnimationGroup ty...
     |      X.setParent(a, b)
     |  
     |  setPaused = <unbound qt slot setPaused of QSequentialAnimationGroup ty...
     |      X.setPaused(a)
     |  
     |  setProperty = <unbound qt slot setProperty of QSequentialAnimationGrou...
     |      X.setProperty(a, b, c) -> bool
     |  
     |  signalsBlocked = <unbound qt slot signalsBlocked of QSequentialAnimati...
     |      X.signalsBlocked(a) -> bool
     |  
     |  start = <unbound qt slot start of QSequentialAnimationGroup type>
     |      X.start(a)
     |  
     |  startTimer = <unbound qt slot startTimer of QSequentialAnimationGroup ...
     |      X.startTimer(a, b, c) -> int
     |  
     |  state = None
     |  
     |  stateChanged = <unbound qt signal stateChanged of QSequentialAnimation...
     |  
     |  
     |  stop = <unbound qt slot stop of QSequentialAnimationGroup type>
     |      X.stop()
     |  
     |  takeAnimation = <unbound qt slot takeAnimation of QSequentialAnimation...
     |      X.takeAnimation(a, b) -> PythonQt.QtCore.QAbstractAnimation
     |  
     |  thread = <unbound qt slot thread of QSequentialAnimationGroup type>
     |      X.thread(a)
     |  
     |  timerEvent = <unbound qt slot py_q_timerEvent of QSequentialAnimationG...
     |      X.timerEvent(a, b)
     |  
     |  totalDuration = <unbound qt slot totalDuration of QSequentialAnimation...
     |      X.totalDuration(a) -> int
     |  
     |  tr = <unbound qt slot tr of QSequentialAnimationGroup type>
     |      X.tr(a, b, c, d) -> str
     |  
     |  updateCurrentTime = <unbound qt slot py_q_updateCurrentTime of QSequen...
     |      X.updateCurrentTime(a, b)
     |  
     |  updateDirection = <unbound qt slot py_q_updateDirection of QSequential...
     |      X.updateDirection(a, b)
     |  
     |  updateState = <unbound qt slot py_q_updateState of QSequentialAnimatio...
     |      X.updateState(a, b, c)
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __delattr__(...)
     |      x.__delattr__('name') <==> del x.name
     |  
     |  __eq__(...)
     |      x.__eq__(y) <==> x==y
     |  
     |  __ge__(...)
     |      x.__ge__(y) <==> x>=y
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __gt__(...)
     |      x.__gt__(y) <==> x>y
     |  
     |  __hash__(...)
     |      x.__hash__() <==> hash(x)
     |  
     |  __le__(...)
     |      x.__le__(y) <==> x<=y
     |  
     |  __lt__(...)
     |      x.__lt__(y) <==> x<y
     |  
     |  __ne__(...)
     |      x.__ne__(y) <==> x!=y
     |  
     |  __nonzero__(...)
     |      x.__nonzero__() <==> x != 0
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __setattr__(...)
     |      x.__setattr__('name', value) <==> x.name = value
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __new__ = <built-in method __new__ of PythonQt.PythonQtClassWrapper ob...
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
    
    class QSettings(PythonQt.PythonQtInstanceWrapper)
     |  Method resolution order:
     |      QSettings
     |      PythonQt.PythonQtInstanceWrapper
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  __init__(...)
     |      x.__init__(...) initializes x; see help(type(x)) for signature
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  AccessError = 1
     |  
     |  CustomFormat1 = 17
     |  
     |  CustomFormat10 = 26
     |  
     |  CustomFormat11 = 27
     |  
     |  CustomFormat12 = 28
     |  
     |  CustomFormat13 = 29
     |  
     |  CustomFormat14 = 30
     |  
     |  CustomFormat15 = 31
     |  
     |  CustomFormat16 = 32
     |  
     |  CustomFormat2 = 18
     |  
     |  CustomFormat3 = 19
     |  
     |  CustomFormat4 = 20
     |  
     |  CustomFormat5 = 21
     |  
     |  CustomFormat6 = 22
     |  
     |  CustomFormat7 = 23
     |  
     |  CustomFormat8 = 24
     |  
     |  CustomFormat9 = 25
     |  
     |  Format = <class 'PythonQt.QtCore.Format'>
     |  
     |  
     |  FormatError = 2
     |  
     |  IniFormat = 1
     |  
     |  InvalidFormat = 16
     |  
     |  NativeFormat = 0
     |  
     |  NoError = 0
     |  
     |  Scope = <class 'PythonQt.QtCore.Scope'>
     |  
     |  
     |  Status = <class 'PythonQt.QtCore.Status'>
     |  
     |  
     |  SystemScope = 1
     |  
     |  UserScope = 0
     |  
     |  allKeys = <unbound qt slot allKeys of QSettings type>
     |      X.allKeys(a) -> tuple
     |  
     |  applicationName = <unbound qt slot applicationName of QSettings type>
     |      X.applicationName(a) -> str
     |  
     |  beginGroup = <unbound qt slot beginGroup of QSettings type>
     |      X.beginGroup(a, b)
     |  
     |  beginReadArray = <unbound qt slot beginReadArray of QSettings type>
     |      X.beginReadArray(a, b) -> int
     |  
     |  beginWriteArray = <unbound qt slot beginWriteArray of QSettings type>
     |      X.beginWriteArray(a, b, c)
     |  
     |  blockSignals = <unbound qt slot blockSignals of QSettings type>
     |      X.blockSignals(a, b) -> bool
     |  
     |  childEvent = <unbound qt slot py_q_childEvent of QSettings type>
     |      X.childEvent(a, b)
     |  
     |  childGroups = <unbound qt slot childGroups of QSettings type>
     |      X.childGroups(a) -> tuple
     |  
     |  childKeys = <unbound qt slot childKeys of QSettings type>
     |      X.childKeys(a) -> tuple
     |  
     |  children = <unbound qt slot children of QSettings type>
     |      X.children(a) -> tuple
     |  
     |  className = <built-in method className of PythonQt.PythonQtClassWrappe...
     |      Return the classname of the object
     |  
     |  clear = <unbound qt slot clear of QSettings type>
     |      X.clear(a)
     |  
     |  connect = <unbound qt slot connect of QSettings type>
     |      X.connect(a, b, c, d, e) -> bool
     |  
     |  contains = <unbound qt slot contains of QSettings type>
     |      X.contains(a, b) -> bool
     |  
     |  customEvent = <unbound qt slot py_q_customEvent of QSettings type>
     |      X.customEvent(a, b)
     |  
     |  defaultFormat = <unbound qt slot static_QSettings_defaultFormat of QSe...
     |      X.defaultFormat()
     |  
     |  delete = <built-in method delete of PythonQt.PythonQtClassWrapper obje...
     |      Deletes the given C++ object
     |  
     |  deleteLater = <unbound qt slot deleteLater of QSettings type>
     |      X.deleteLater()
     |  
     |  destroyed = <unbound qt signal destroyed of QSettings type>
     |  
     |  
     |  disconnect = <unbound qt slot disconnect of QSettings type>
     |      X.disconnect(a, b, c, d) -> bool
     |  
     |  dumpObjectInfo = <unbound qt slot dumpObjectInfo of QSettings type>
     |      X.dumpObjectInfo(a)
     |  
     |  dumpObjectTree = <unbound qt slot dumpObjectTree of QSettings type>
     |      X.dumpObjectTree(a)
     |  
     |  dynamicPropertyNames = <unbound qt slot dynamicPropertyNames of QSetti...
     |      X.dynamicPropertyNames(a)
     |  
     |  endArray = <unbound qt slot endArray of QSettings type>
     |      X.endArray(a)
     |  
     |  endGroup = <unbound qt slot endGroup of QSettings type>
     |      X.endGroup(a)
     |  
     |  event = <unbound qt slot py_q_event of QSettings type>
     |      X.event(a, b) -> bool
     |  
     |  eventFilter = <unbound qt slot py_q_eventFilter of QSettings type>
     |      X.eventFilter(a, b, c) -> bool
     |  
     |  fallbacksEnabled = <unbound qt slot fallbacksEnabled of QSettings type...
     |      X.fallbacksEnabled(a) -> bool
     |  
     |  fileName = <unbound qt slot fileName of QSettings type>
     |      X.fileName(a) -> str
     |  
     |  findChild = <unbound qt slot findChild of QSettings type>
     |      X.findChild(a, b, c) -> PythonQt.private.QObject
     |  
     |  findChildren = <unbound qt slot findChildren of QSettings type>
     |      X.findChildren(a, b, c) -> tuple
     |  
     |  format = <unbound qt slot format of QSettings type>
     |      X.format(a)
     |  
     |  group = <unbound qt slot group of QSettings type>
     |      X.group(a) -> str
     |  
     |  help = <built-in method help of PythonQt.PythonQtClassWrapper object>
     |      Shows the help of available methods for this class
     |  
     |  inherits = <built-in method inherits of PythonQt.PythonQtClassWrapper ...
     |      Returns if the class inherits or is of given type name
     |  
     |  iniCodec = <unbound qt slot iniCodec of QSettings type>
     |      X.iniCodec(a) -> PythonQt.QtCore.QTextCodec
     |  
     |  installEventFilter = <unbound qt slot installEventFilter of QSettings ...
     |      X.installEventFilter(a, b)
     |  
     |  isSignalConnected = <unbound qt slot isSignalConnected of QSettings ty...
     |      X.isSignalConnected(a, b) -> bool
     |  
     |  isWidgetType = <unbound qt slot isWidgetType of QSettings type>
     |      X.isWidgetType(a) -> bool
     |  
     |  isWindowType = <unbound qt slot isWindowType of QSettings type>
     |      X.isWindowType(a) -> bool
     |  
     |  isWritable = <unbound qt slot isWritable of QSettings type>
     |      X.isWritable(a) -> bool
     |  
     |  killTimer = <unbound qt slot killTimer of QSettings type>
     |      X.killTimer(a, b)
     |  
     |  metaObject = <unbound qt slot metaObject of QSettings type>
     |      X.metaObject(a) -> PythonQt.QtCore.QMetaObject
     |  
     |  moveToThread = <unbound qt slot moveToThread of QSettings type>
     |      X.moveToThread(a, b)
     |  
     |  objectName = None
     |  
     |  objectNameChanged = <unbound qt signal objectNameChanged of QSettings ...
     |  
     |  
     |  organizationName = <unbound qt slot organizationName of QSettings type...
     |      X.organizationName(a) -> str
     |  
     |  parent = <unbound qt slot parent of QSettings type>
     |      X.parent(a) -> PythonQt.private.QObject
     |  
     |  property = <unbound qt slot property of QSettings type>
     |      X.property(a, b) -> object
     |  
     |  remove = <unbound qt slot remove of QSettings type>
     |      X.remove(a, b)
     |  
     |  removeEventFilter = <unbound qt slot removeEventFilter of QSettings ty...
     |      X.removeEventFilter(a, b)
     |  
     |  scope = <unbound qt slot scope of QSettings type>
     |      X.scope(a)
     |  
     |  sender = <unbound qt slot sender of QSettings type>
     |      X.sender(a) -> PythonQt.private.QObject
     |  
     |  senderSignalIndex = <unbound qt slot senderSignalIndex of QSettings ty...
     |      X.senderSignalIndex(a) -> int
     |  
     |  setArrayIndex = <unbound qt slot setArrayIndex of QSettings type>
     |      X.setArrayIndex(a, b)
     |  
     |  setDefaultFormat = <unbound qt slot static_QSettings_setDefaultFormat ...
     |      X.setDefaultFormat(a)
     |  
     |  setFallbacksEnabled = <unbound qt slot setFallbacksEnabled of QSetting...
     |      X.setFallbacksEnabled(a, b)
     |  
     |  setIniCodec = <unbound qt slot setIniCodec of QSettings type>
     |      X.setIniCodec(a, b)
     |  
     |  setObjectName = <unbound qt slot setObjectName of QSettings type>
     |      X.setObjectName(a, b)
     |  
     |  setParent = <unbound qt slot setParent of QSettings type>
     |      X.setParent(a, b)
     |  
     |  setPath = <unbound qt slot static_QSettings_setPath of QSettings type>
     |      X.setPath(a, b, c)
     |  
     |  setProperty = <unbound qt slot setProperty of QSettings type>
     |      X.setProperty(a, b, c) -> bool
     |  
     |  setValue = <unbound qt slot setValue of QSettings type>
     |      X.setValue(a, b, c)
     |  
     |  signalsBlocked = <unbound qt slot signalsBlocked of QSettings type>
     |      X.signalsBlocked(a) -> bool
     |  
     |  startTimer = <unbound qt slot startTimer of QSettings type>
     |      X.startTimer(a, b, c) -> int
     |  
     |  status = <unbound qt slot status of QSettings type>
     |      X.status(a)
     |  
     |  sync = <unbound qt slot sync of QSettings type>
     |      X.sync(a)
     |  
     |  thread = <unbound qt slot thread of QSettings type>
     |      X.thread(a)
     |  
     |  timerEvent = <unbound qt slot py_q_timerEvent of QSettings type>
     |      X.timerEvent(a, b)
     |  
     |  tr = <unbound qt slot tr of QSettings type>
     |      X.tr(a, b, c, d) -> str
     |  
     |  value = <unbound qt slot value of QSettings type>
     |      X.value(a, b, c) -> object
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __delattr__(...)
     |      x.__delattr__('name') <==> del x.name
     |  
     |  __eq__(...)
     |      x.__eq__(y) <==> x==y
     |  
     |  __ge__(...)
     |      x.__ge__(y) <==> x>=y
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __gt__(...)
     |      x.__gt__(y) <==> x>y
     |  
     |  __hash__(...)
     |      x.__hash__() <==> hash(x)
     |  
     |  __le__(...)
     |      x.__le__(y) <==> x<=y
     |  
     |  __lt__(...)
     |      x.__lt__(y) <==> x<y
     |  
     |  __ne__(...)
     |      x.__ne__(y) <==> x!=y
     |  
     |  __nonzero__(...)
     |      x.__nonzero__() <==> x != 0
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __setattr__(...)
     |      x.__setattr__('name', value) <==> x.name = value
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __new__ = <built-in method __new__ of PythonQt.PythonQtClassWrapper ob...
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
    
    class QSharedMemory(PythonQt.PythonQtInstanceWrapper)
     |  Method resolution order:
     |      QSharedMemory
     |      PythonQt.PythonQtInstanceWrapper
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  __init__(...)
     |      x.__init__(...) initializes x; see help(type(x)) for signature
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  AccessMode = <class 'PythonQt.QtCore.AccessMode'>
     |  
     |  
     |  AlreadyExists = 4
     |  
     |  InvalidSize = 2
     |  
     |  KeyError = 3
     |  
     |  LockError = 6
     |  
     |  NoError = 0
     |  
     |  NotFound = 5
     |  
     |  OutOfResources = 7
     |  
     |  PermissionDenied = 1
     |  
     |  ReadOnly = 0
     |  
     |  ReadWrite = 1
     |  
     |  SharedMemoryError = <class 'PythonQt.QtCore.SharedMemoryError'>
     |  
     |  
     |  UnknownError = 8
     |  
     |  attach = <unbound qt slot attach of QSharedMemory type>
     |      X.attach(a, b) -> bool
     |  
     |  blockSignals = <unbound qt slot blockSignals of QSharedMemory type>
     |      X.blockSignals(a, b) -> bool
     |  
     |  childEvent = <unbound qt slot py_q_childEvent of QSharedMemory type>
     |      X.childEvent(a, b)
     |  
     |  children = <unbound qt slot children of QSharedMemory type>
     |      X.children(a) -> tuple
     |  
     |  className = <built-in method className of PythonQt.PythonQtClassWrappe...
     |      Return the classname of the object
     |  
     |  connect = <unbound qt slot connect of QSharedMemory type>
     |      X.connect(a, b, c, d, e) -> bool
     |  
     |  constData = <unbound qt slot constData of QSharedMemory type>
     |      X.constData(a)
     |  
     |  create = <unbound qt slot create of QSharedMemory type>
     |      X.create(a, b, c) -> bool
     |  
     |  customEvent = <unbound qt slot py_q_customEvent of QSharedMemory type>
     |      X.customEvent(a, b)
     |  
     |  data = <unbound qt slot data of QSharedMemory type>
     |      X.data(a)
     |  
     |  delete = <built-in method delete of PythonQt.PythonQtClassWrapper obje...
     |      Deletes the given C++ object
     |  
     |  deleteLater = <unbound qt slot deleteLater of QSharedMemory type>
     |      X.deleteLater()
     |  
     |  destroyed = <unbound qt signal destroyed of QSharedMemory type>
     |  
     |  
     |  disconnect = <unbound qt slot disconnect of QSharedMemory type>
     |      X.disconnect(a, b, c, d) -> bool
     |  
     |  dumpObjectInfo = <unbound qt slot dumpObjectInfo of QSharedMemory type...
     |      X.dumpObjectInfo(a)
     |  
     |  dumpObjectTree = <unbound qt slot dumpObjectTree of QSharedMemory type...
     |      X.dumpObjectTree(a)
     |  
     |  dynamicPropertyNames = <unbound qt slot dynamicPropertyNames of QShare...
     |      X.dynamicPropertyNames(a)
     |  
     |  error = <unbound qt slot error of QSharedMemory type>
     |      X.error(a)
     |  
     |  errorString = <unbound qt slot errorString of QSharedMemory type>
     |      X.errorString(a) -> str
     |  
     |  event = <unbound qt slot py_q_event of QSharedMemory type>
     |      X.event(a, b) -> bool
     |  
     |  eventFilter = <unbound qt slot py_q_eventFilter of QSharedMemory type>
     |      X.eventFilter(a, b, c) -> bool
     |  
     |  findChild = <unbound qt slot findChild of QSharedMemory type>
     |      X.findChild(a, b, c) -> PythonQt.private.QObject
     |  
     |  findChildren = <unbound qt slot findChildren of QSharedMemory type>
     |      X.findChildren(a, b, c) -> tuple
     |  
     |  help = <built-in method help of PythonQt.PythonQtClassWrapper object>
     |      Shows the help of available methods for this class
     |  
     |  inherits = <built-in method inherits of PythonQt.PythonQtClassWrapper ...
     |      Returns if the class inherits or is of given type name
     |  
     |  installEventFilter = <unbound qt slot installEventFilter of QSharedMem...
     |      X.installEventFilter(a, b)
     |  
     |  isAttached = <unbound qt slot isAttached of QSharedMemory type>
     |      X.isAttached(a) -> bool
     |  
     |  isSignalConnected = <unbound qt slot isSignalConnected of QSharedMemor...
     |      X.isSignalConnected(a, b) -> bool
     |  
     |  isWidgetType = <unbound qt slot isWidgetType of QSharedMemory type>
     |      X.isWidgetType(a) -> bool
     |  
     |  isWindowType = <unbound qt slot isWindowType of QSharedMemory type>
     |      X.isWindowType(a) -> bool
     |  
     |  key = <unbound qt slot key of QSharedMemory type>
     |      X.key(a) -> str
     |  
     |  killTimer = <unbound qt slot killTimer of QSharedMemory type>
     |      X.killTimer(a, b)
     |  
     |  lock = <unbound qt slot lock of QSharedMemory type>
     |      X.lock(a) -> bool
     |  
     |  metaObject = <unbound qt slot metaObject of QSharedMemory type>
     |      X.metaObject(a) -> PythonQt.QtCore.QMetaObject
     |  
     |  moveToThread = <unbound qt slot moveToThread of QSharedMemory type>
     |      X.moveToThread(a, b)
     |  
     |  nativeKey = <unbound qt slot nativeKey of QSharedMemory type>
     |      X.nativeKey(a) -> str
     |  
     |  objectName = None
     |  
     |  objectNameChanged = <unbound qt signal objectNameChanged of QSharedMem...
     |  
     |  
     |  parent = <unbound qt slot parent of QSharedMemory type>
     |      X.parent(a) -> PythonQt.private.QObject
     |  
     |  property = <unbound qt slot property of QSharedMemory type>
     |      X.property(a, b) -> object
     |  
     |  removeEventFilter = <unbound qt slot removeEventFilter of QSharedMemor...
     |      X.removeEventFilter(a, b)
     |  
     |  sender = <unbound qt slot sender of QSharedMemory type>
     |      X.sender(a) -> PythonQt.private.QObject
     |  
     |  senderSignalIndex = <unbound qt slot senderSignalIndex of QSharedMemor...
     |      X.senderSignalIndex(a) -> int
     |  
     |  setKey = <unbound qt slot setKey of QSharedMemory type>
     |      X.setKey(a, b)
     |  
     |  setNativeKey = <unbound qt slot setNativeKey of QSharedMemory type>
     |      X.setNativeKey(a, b)
     |  
     |  setObjectName = <unbound qt slot setObjectName of QSharedMemory type>
     |      X.setObjectName(a, b)
     |  
     |  setParent = <unbound qt slot setParent of QSharedMemory type>
     |      X.setParent(a, b)
     |  
     |  setProperty = <unbound qt slot setProperty of QSharedMemory type>
     |      X.setProperty(a, b, c) -> bool
     |  
     |  signalsBlocked = <unbound qt slot signalsBlocked of QSharedMemory type...
     |      X.signalsBlocked(a) -> bool
     |  
     |  size = <unbound qt slot size of QSharedMemory type>
     |      X.size(a) -> int
     |  
     |  startTimer = <unbound qt slot startTimer of QSharedMemory type>
     |      X.startTimer(a, b, c) -> int
     |  
     |  thread = <unbound qt slot thread of QSharedMemory type>
     |      X.thread(a)
     |  
     |  timerEvent = <unbound qt slot py_q_timerEvent of QSharedMemory type>
     |      X.timerEvent(a, b)
     |  
     |  tr = <unbound qt slot tr of QSharedMemory type>
     |      X.tr(a, b, c, d) -> str
     |  
     |  unlock = <unbound qt slot unlock of QSharedMemory type>
     |      X.unlock(a) -> bool
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __delattr__(...)
     |      x.__delattr__('name') <==> del x.name
     |  
     |  __eq__(...)
     |      x.__eq__(y) <==> x==y
     |  
     |  __ge__(...)
     |      x.__ge__(y) <==> x>=y
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __gt__(...)
     |      x.__gt__(y) <==> x>y
     |  
     |  __hash__(...)
     |      x.__hash__() <==> hash(x)
     |  
     |  __le__(...)
     |      x.__le__(y) <==> x<=y
     |  
     |  __lt__(...)
     |      x.__lt__(y) <==> x<y
     |  
     |  __ne__(...)
     |      x.__ne__(y) <==> x!=y
     |  
     |  __nonzero__(...)
     |      x.__nonzero__() <==> x != 0
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __setattr__(...)
     |      x.__setattr__('name', value) <==> x.name = value
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __new__ = <built-in method __new__ of PythonQt.PythonQtClassWrapper ob...
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
    
    class QSignalBlocker(PythonQt.PythonQtInstanceWrapper)
     |  Method resolution order:
     |      QSignalBlocker
     |      PythonQt.PythonQtInstanceWrapper
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  __init__(...)
     |      x.__init__(...) initializes x; see help(type(x)) for signature
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  className = <built-in method className of PythonQt.PythonQtClassWrappe...
     |      Return the classname of the object
     |  
     |  delete = <built-in method delete of PythonQt.PythonQtClassWrapper obje...
     |      Deletes the given C++ object
     |  
     |  help = <built-in method help of PythonQt.PythonQtClassWrapper object>
     |      Shows the help of available methods for this class
     |  
     |  inherits = <built-in method inherits of PythonQt.PythonQtClassWrapper ...
     |      Returns if the class inherits or is of given type name
     |  
     |  reblock = <unbound qt slot reblock of QSignalBlocker type>
     |      X.reblock(a)
     |  
     |  unblock = <unbound qt slot unblock of QSignalBlocker type>
     |      X.unblock(a)
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __delattr__(...)
     |      x.__delattr__('name') <==> del x.name
     |  
     |  __eq__(...)
     |      x.__eq__(y) <==> x==y
     |  
     |  __ge__(...)
     |      x.__ge__(y) <==> x>=y
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __gt__(...)
     |      x.__gt__(y) <==> x>y
     |  
     |  __hash__(...)
     |      x.__hash__() <==> hash(x)
     |  
     |  __le__(...)
     |      x.__le__(y) <==> x<=y
     |  
     |  __lt__(...)
     |      x.__lt__(y) <==> x<y
     |  
     |  __ne__(...)
     |      x.__ne__(y) <==> x!=y
     |  
     |  __nonzero__(...)
     |      x.__nonzero__() <==> x != 0
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __setattr__(...)
     |      x.__setattr__('name', value) <==> x.name = value
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __new__ = <built-in method __new__ of PythonQt.PythonQtClassWrapper ob...
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
    
    class QSignalMapper(PythonQt.PythonQtInstanceWrapper)
     |  Method resolution order:
     |      QSignalMapper
     |      PythonQt.PythonQtInstanceWrapper
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  __init__(...)
     |      x.__init__(...) initializes x; see help(type(x)) for signature
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  blockSignals = <unbound qt slot blockSignals of QSignalMapper type>
     |      X.blockSignals(a, b) -> bool
     |  
     |  childEvent = <unbound qt slot py_q_childEvent of QSignalMapper type>
     |      X.childEvent(a, b)
     |  
     |  children = <unbound qt slot children of QSignalMapper type>
     |      X.children(a) -> tuple
     |  
     |  className = <built-in method className of PythonQt.PythonQtClassWrappe...
     |      Return the classname of the object
     |  
     |  connect = <unbound qt slot connect of QSignalMapper type>
     |      X.connect(a, b, c, d, e) -> bool
     |  
     |  customEvent = <unbound qt slot py_q_customEvent of QSignalMapper type>
     |      X.customEvent(a, b)
     |  
     |  delete = <built-in method delete of PythonQt.PythonQtClassWrapper obje...
     |      Deletes the given C++ object
     |  
     |  deleteLater = <unbound qt slot deleteLater of QSignalMapper type>
     |      X.deleteLater()
     |  
     |  destroyed = <unbound qt signal destroyed of QSignalMapper type>
     |  
     |  
     |  disconnect = <unbound qt slot disconnect of QSignalMapper type>
     |      X.disconnect(a, b, c, d) -> bool
     |  
     |  dumpObjectInfo = <unbound qt slot dumpObjectInfo of QSignalMapper type...
     |      X.dumpObjectInfo(a)
     |  
     |  dumpObjectTree = <unbound qt slot dumpObjectTree of QSignalMapper type...
     |      X.dumpObjectTree(a)
     |  
     |  dynamicPropertyNames = <unbound qt slot dynamicPropertyNames of QSigna...
     |      X.dynamicPropertyNames(a)
     |  
     |  event = <unbound qt slot py_q_event of QSignalMapper type>
     |      X.event(a, b) -> bool
     |  
     |  eventFilter = <unbound qt slot py_q_eventFilter of QSignalMapper type>
     |      X.eventFilter(a, b, c) -> bool
     |  
     |  findChild = <unbound qt slot findChild of QSignalMapper type>
     |      X.findChild(a, b, c) -> PythonQt.private.QObject
     |  
     |  findChildren = <unbound qt slot findChildren of QSignalMapper type>
     |      X.findChildren(a, b, c) -> tuple
     |  
     |  help = <built-in method help of PythonQt.PythonQtClassWrapper object>
     |      Shows the help of available methods for this class
     |  
     |  inherits = <built-in method inherits of PythonQt.PythonQtClassWrapper ...
     |      Returns if the class inherits or is of given type name
     |  
     |  installEventFilter = <unbound qt slot installEventFilter of QSignalMap...
     |      X.installEventFilter(a, b)
     |  
     |  isSignalConnected = <unbound qt slot isSignalConnected of QSignalMappe...
     |      X.isSignalConnected(a, b) -> bool
     |  
     |  isWidgetType = <unbound qt slot isWidgetType of QSignalMapper type>
     |      X.isWidgetType(a) -> bool
     |  
     |  isWindowType = <unbound qt slot isWindowType of QSignalMapper type>
     |      X.isWindowType(a) -> bool
     |  
     |  killTimer = <unbound qt slot killTimer of QSignalMapper type>
     |      X.killTimer(a, b)
     |  
     |  map = <unbound qt slot map of QSignalMapper type>
     |      X.map(a)
     |  
     |  mapped = <unbound qt signal mapped of QSignalMapper type>
     |  
     |  
     |  mapping = <unbound qt slot mapping of QSignalMapper type>
     |      X.mapping(a, b) -> PythonQt.private.QObject
     |  
     |  metaObject = <unbound qt slot metaObject of QSignalMapper type>
     |      X.metaObject(a) -> PythonQt.QtCore.QMetaObject
     |  
     |  moveToThread = <unbound qt slot moveToThread of QSignalMapper type>
     |      X.moveToThread(a, b)
     |  
     |  objectName = None
     |  
     |  objectNameChanged = <unbound qt signal objectNameChanged of QSignalMap...
     |  
     |  
     |  parent = <unbound qt slot parent of QSignalMapper type>
     |      X.parent(a) -> PythonQt.private.QObject
     |  
     |  property = <unbound qt slot property of QSignalMapper type>
     |      X.property(a, b) -> object
     |  
     |  removeEventFilter = <unbound qt slot removeEventFilter of QSignalMappe...
     |      X.removeEventFilter(a, b)
     |  
     |  removeMappings = <unbound qt slot removeMappings of QSignalMapper type...
     |      X.removeMappings(a, b)
     |  
     |  sender = <unbound qt slot sender of QSignalMapper type>
     |      X.sender(a) -> PythonQt.private.QObject
     |  
     |  senderSignalIndex = <unbound qt slot senderSignalIndex of QSignalMappe...
     |      X.senderSignalIndex(a) -> int
     |  
     |  setMapping = <unbound qt slot setMapping of QSignalMapper type>
     |      X.setMapping(a, b, c)
     |  
     |  setObjectName = <unbound qt slot setObjectName of QSignalMapper type>
     |      X.setObjectName(a, b)
     |  
     |  setParent = <unbound qt slot setParent of QSignalMapper type>
     |      X.setParent(a, b)
     |  
     |  setProperty = <unbound qt slot setProperty of QSignalMapper type>
     |      X.setProperty(a, b, c) -> bool
     |  
     |  signalsBlocked = <unbound qt slot signalsBlocked of QSignalMapper type...
     |      X.signalsBlocked(a) -> bool
     |  
     |  startTimer = <unbound qt slot startTimer of QSignalMapper type>
     |      X.startTimer(a, b, c) -> int
     |  
     |  thread = <unbound qt slot thread of QSignalMapper type>
     |      X.thread(a)
     |  
     |  timerEvent = <unbound qt slot py_q_timerEvent of QSignalMapper type>
     |      X.timerEvent(a, b)
     |  
     |  tr = <unbound qt slot tr of QSignalMapper type>
     |      X.tr(a, b, c, d) -> str
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __delattr__(...)
     |      x.__delattr__('name') <==> del x.name
     |  
     |  __eq__(...)
     |      x.__eq__(y) <==> x==y
     |  
     |  __ge__(...)
     |      x.__ge__(y) <==> x>=y
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __gt__(...)
     |      x.__gt__(y) <==> x>y
     |  
     |  __hash__(...)
     |      x.__hash__() <==> hash(x)
     |  
     |  __le__(...)
     |      x.__le__(y) <==> x<=y
     |  
     |  __lt__(...)
     |      x.__lt__(y) <==> x<y
     |  
     |  __ne__(...)
     |      x.__ne__(y) <==> x!=y
     |  
     |  __nonzero__(...)
     |      x.__nonzero__() <==> x != 0
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __setattr__(...)
     |      x.__setattr__('name', value) <==> x.name = value
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __new__ = <built-in method __new__ of PythonQt.PythonQtClassWrapper ob...
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
    
    class QSignalTransition(PythonQt.PythonQtInstanceWrapper)
     |  Method resolution order:
     |      QSignalTransition
     |      PythonQt.PythonQtInstanceWrapper
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  __init__(...)
     |      x.__init__(...) initializes x; see help(type(x)) for signature
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  ExternalTransition = 0
     |  
     |  InternalTransition = 1
     |  
     |  TransitionType = <class 'PythonQt.QtCore.TransitionType'>
     |  
     |  
     |  addAnimation = <unbound qt slot addAnimation of QSignalTransition type...
     |      X.addAnimation(a, b)
     |  
     |  animations = <unbound qt slot animations of QSignalTransition type>
     |      X.animations(a) -> tuple
     |  
     |  blockSignals = <unbound qt slot blockSignals of QSignalTransition type...
     |      X.blockSignals(a, b) -> bool
     |  
     |  childEvent = <unbound qt slot py_q_childEvent of QSignalTransition typ...
     |      X.childEvent(a, b)
     |  
     |  children = <unbound qt slot children of QSignalTransition type>
     |      X.children(a) -> tuple
     |  
     |  className = <built-in method className of PythonQt.PythonQtClassWrappe...
     |      Return the classname of the object
     |  
     |  connect = <unbound qt slot connect of QSignalTransition type>
     |      X.connect(a, b, c, d, e) -> bool
     |  
     |  customEvent = <unbound qt slot py_q_customEvent of QSignalTransition t...
     |      X.customEvent(a, b)
     |  
     |  delete = <built-in method delete of PythonQt.PythonQtClassWrapper obje...
     |      Deletes the given C++ object
     |  
     |  deleteLater = <unbound qt slot deleteLater of QSignalTransition type>
     |      X.deleteLater()
     |  
     |  destroyed = <unbound qt signal destroyed of QSignalTransition type>
     |  
     |  
     |  disconnect = <unbound qt slot disconnect of QSignalTransition type>
     |      X.disconnect(a, b, c, d) -> bool
     |  
     |  dumpObjectInfo = <unbound qt slot dumpObjectInfo of QSignalTransition ...
     |      X.dumpObjectInfo(a)
     |  
     |  dumpObjectTree = <unbound qt slot dumpObjectTree of QSignalTransition ...
     |      X.dumpObjectTree(a)
     |  
     |  dynamicPropertyNames = <unbound qt slot dynamicPropertyNames of QSigna...
     |      X.dynamicPropertyNames(a)
     |  
     |  event = <unbound qt slot py_q_event of QSignalTransition type>
     |      X.event(a, b) -> bool
     |  
     |  eventFilter = <unbound qt slot py_q_eventFilter of QSignalTransition t...
     |      X.eventFilter(a, b, c) -> bool
     |  
     |  eventTest = <unbound qt slot py_q_eventTest of QSignalTransition type>
     |      X.eventTest(a, b) -> bool
     |  
     |  findChild = <unbound qt slot findChild of QSignalTransition type>
     |      X.findChild(a, b, c) -> PythonQt.private.QObject
     |  
     |  findChildren = <unbound qt slot findChildren of QSignalTransition type...
     |      X.findChildren(a, b, c) -> tuple
     |  
     |  help = <built-in method help of PythonQt.PythonQtClassWrapper object>
     |      Shows the help of available methods for this class
     |  
     |  inherits = <built-in method inherits of PythonQt.PythonQtClassWrapper ...
     |      Returns if the class inherits or is of given type name
     |  
     |  installEventFilter = <unbound qt slot installEventFilter of QSignalTra...
     |      X.installEventFilter(a, b)
     |  
     |  isSignalConnected = <unbound qt slot isSignalConnected of QSignalTrans...
     |      X.isSignalConnected(a, b) -> bool
     |  
     |  isWidgetType = <unbound qt slot isWidgetType of QSignalTransition type...
     |      X.isWidgetType(a) -> bool
     |  
     |  isWindowType = <unbound qt slot isWindowType of QSignalTransition type...
     |      X.isWindowType(a) -> bool
     |  
     |  killTimer = <unbound qt slot killTimer of QSignalTransition type>
     |      X.killTimer(a, b)
     |  
     |  machine = <unbound qt slot machine of QSignalTransition type>
     |      X.machine(a) -> PythonQt.QtCore.QStateMachine
     |  
     |  metaObject = <unbound qt slot metaObject of QSignalTransition type>
     |      X.metaObject(a) -> PythonQt.QtCore.QMetaObject
     |  
     |  moveToThread = <unbound qt slot moveToThread of QSignalTransition type...
     |      X.moveToThread(a, b)
     |  
     |  objectName = None
     |  
     |  objectNameChanged = <unbound qt signal objectNameChanged of QSignalTra...
     |  
     |  
     |  onTransition = <unbound qt slot py_q_onTransition of QSignalTransition...
     |      X.onTransition(a, b)
     |  
     |  parent = <unbound qt slot parent of QSignalTransition type>
     |      X.parent(a) -> PythonQt.private.QObject
     |  
     |  property = <unbound qt slot property of QSignalTransition type>
     |      X.property(a, b) -> object
     |  
     |  removeAnimation = <unbound qt slot removeAnimation of QSignalTransitio...
     |      X.removeAnimation(a, b)
     |  
     |  removeEventFilter = <unbound qt slot removeEventFilter of QSignalTrans...
     |      X.removeEventFilter(a, b)
     |  
     |  sender = <unbound qt slot sender of QSignalTransition type>
     |      X.sender(a) -> PythonQt.private.QObject
     |  
     |  senderObject = QObject (QObject at: 0x0)
     |  
     |  senderObjectChanged = <unbound qt signal senderObjectChanged of QSigna...
     |  
     |  
     |  senderSignalIndex = <unbound qt slot senderSignalIndex of QSignalTrans...
     |      X.senderSignalIndex(a) -> int
     |  
     |  setObjectName = <unbound qt slot setObjectName of QSignalTransition ty...
     |      X.setObjectName(a, b)
     |  
     |  setParent = <unbound qt slot setParent of QSignalTransition type>
     |      X.setParent(a, b)
     |  
     |  setProperty = <unbound qt slot setProperty of QSignalTransition type>
     |      X.setProperty(a, b, c) -> bool
     |  
     |  setSenderObject = <unbound qt slot setSenderObject of QSignalTransitio...
     |      X.setSenderObject(a, b)
     |  
     |  setSignal = <unbound qt slot setSignal of QSignalTransition type>
     |      X.setSignal(a, b)
     |  
     |  setTargetState = <unbound qt slot setTargetState of QSignalTransition ...
     |      X.setTargetState(a, b)
     |  
     |  setTargetStates = <unbound qt slot setTargetStates of QSignalTransitio...
     |      X.setTargetStates(a, b)
     |  
     |  setTransitionType = <unbound qt slot setTransitionType of QSignalTrans...
     |      X.setTransitionType(a, b)
     |  
     |  signal = QByteArray (QByteArray at: 0x0)
     |  
     |  signalChanged = <unbound qt signal signalChanged of QSignalTransition ...
     |  
     |  
     |  signalsBlocked = <unbound qt slot signalsBlocked of QSignalTransition ...
     |      X.signalsBlocked(a) -> bool
     |  
     |  sourceState = QState (QState at: 0x0)
     |  
     |  startTimer = <unbound qt slot startTimer of QSignalTransition type>
     |      X.startTimer(a, b, c) -> int
     |  
     |  targetState = QAbstractState (QAbstractState at: 0x0)
     |  
     |  targetStateChanged = <unbound qt signal targetStateChanged of QSignalT...
     |  
     |  
     |  targetStates = None
     |  
     |  targetStatesChanged = <unbound qt signal targetStatesChanged of QSigna...
     |  
     |  
     |  thread = <unbound qt slot thread of QSignalTransition type>
     |      X.thread(a)
     |  
     |  timerEvent = <unbound qt slot py_q_timerEvent of QSignalTransition typ...
     |      X.timerEvent(a, b)
     |  
     |  tr = <unbound qt slot tr of QSignalTransition type>
     |      X.tr(a, b, c, d) -> str
     |  
     |  transitionType = None
     |  
     |  triggered = <unbound qt signal triggered of QSignalTransition type>
     |  
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __delattr__(...)
     |      x.__delattr__('name') <==> del x.name
     |  
     |  __eq__(...)
     |      x.__eq__(y) <==> x==y
     |  
     |  __ge__(...)
     |      x.__ge__(y) <==> x>=y
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __gt__(...)
     |      x.__gt__(y) <==> x>y
     |  
     |  __hash__(...)
     |      x.__hash__() <==> hash(x)
     |  
     |  __le__(...)
     |      x.__le__(y) <==> x<=y
     |  
     |  __lt__(...)
     |      x.__lt__(y) <==> x<y
     |  
     |  __ne__(...)
     |      x.__ne__(y) <==> x!=y
     |  
     |  __nonzero__(...)
     |      x.__nonzero__() <==> x != 0
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __setattr__(...)
     |      x.__setattr__('name', value) <==> x.name = value
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __new__ = <built-in method __new__ of PythonQt.PythonQtClassWrapper ob...
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
    
    class QSize(PythonQt.PythonQtInstanceWrapper)
     |  Method resolution order:
     |      QSize
     |      PythonQt.PythonQtInstanceWrapper
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  __add__(...)
     |      x.__add__(y) <==> x+y
     |  
     |  __div__(...)
     |      x.__div__(y) <==> x/y
     |  
     |  __eq__(...)
     |      x.__eq__(y) <==> x==y
     |  
     |  __iadd__(...)
     |      x.__iadd__(y) <==> x+=y
     |  
     |  __idiv__(...)
     |      x.__idiv__(y) <==> x/=y
     |  
     |  __imul__(...)
     |      x.__imul__(y) <==> x*=y
     |  
     |  __init__(...)
     |      x.__init__(...) initializes x; see help(type(x)) for signature
     |  
     |  __isub__(...)
     |      x.__isub__(y) <==> x-=y
     |  
     |  __itruediv__(...)
     |      x.__itruediv__(y) <==> x/=y
     |  
     |  __mul__(...)
     |      x.__mul__(y) <==> x*y
     |  
     |  __neg__(...)
     |      x.__neg__() <==> -x
     |  
     |  __nonzero__(...)
     |      x.__nonzero__() <==> x != 0
     |  
     |  __radd__(...)
     |      x.__radd__(y) <==> y+x
     |  
     |  __rdiv__(...)
     |      x.__rdiv__(y) <==> y/x
     |  
     |  __rmul__(...)
     |      x.__rmul__(y) <==> y*x
     |  
     |  __rsub__(...)
     |      x.__rsub__(y) <==> y-x
     |  
     |  __rtruediv__(...)
     |      x.__rtruediv__(y) <==> y/x
     |  
     |  __sub__(...)
     |      x.__sub__(y) <==> x-y
     |  
     |  __truediv__(...)
     |      x.__truediv__(y) <==> x/y
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  boundedTo = <unbound qt slot boundedTo of QSize type>
     |      X.boundedTo(a, b) -> PythonQt.QtCore.QSize
     |  
     |  className = <built-in method className of PythonQt.PythonQtClassWrappe...
     |      Return the classname of the object
     |  
     |  delete = <built-in method delete of PythonQt.PythonQtClassWrapper obje...
     |      Deletes the given C++ object
     |  
     |  expandedTo = <unbound qt slot expandedTo of QSize type>
     |      X.expandedTo(a, b) -> PythonQt.QtCore.QSize
     |  
     |  height = <unbound qt slot height of QSize type>
     |      X.height(a) -> int
     |  
     |  help = <built-in method help of PythonQt.PythonQtClassWrapper object>
     |      Shows the help of available methods for this class
     |  
     |  inherits = <built-in method inherits of PythonQt.PythonQtClassWrapper ...
     |      Returns if the class inherits or is of given type name
     |  
     |  isEmpty = <unbound qt slot isEmpty of QSize type>
     |      X.isEmpty(a) -> bool
     |  
     |  isNull = <unbound qt slot isNull of QSize type>
     |      X.isNull(a) -> bool
     |  
     |  isValid = <unbound qt slot isValid of QSize type>
     |      X.isValid(a) -> bool
     |  
     |  readFrom = <unbound qt slot readFrom of QSize type>
     |      X.readFrom(a, b)
     |  
     |  scale = <unbound qt slot scale of QSize type>
     |      X.scale(a, b, c, d)
     |  
     |  scaled = <unbound qt slot scaled of QSize type>
     |      X.scaled(a, b, c, d) -> PythonQt.QtCore.QSize
     |  
     |  setHeight = <unbound qt slot setHeight of QSize type>
     |      X.setHeight(a, b)
     |  
     |  setWidth = <unbound qt slot setWidth of QSize type>
     |      X.setWidth(a, b)
     |  
     |  transpose = <unbound qt slot transpose of QSize type>
     |      X.transpose(a)
     |  
     |  transposed = <unbound qt slot transposed of QSize type>
     |      X.transposed(a) -> PythonQt.QtCore.QSize
     |  
     |  width = <unbound qt slot width of QSize type>
     |      X.width(a) -> int
     |  
     |  writeTo = <unbound qt slot writeTo of QSize type>
     |      X.writeTo(a, b)
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __delattr__(...)
     |      x.__delattr__('name') <==> del x.name
     |  
     |  __ge__(...)
     |      x.__ge__(y) <==> x>=y
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __gt__(...)
     |      x.__gt__(y) <==> x>y
     |  
     |  __hash__(...)
     |      x.__hash__() <==> hash(x)
     |  
     |  __le__(...)
     |      x.__le__(y) <==> x<=y
     |  
     |  __lt__(...)
     |      x.__lt__(y) <==> x<y
     |  
     |  __ne__(...)
     |      x.__ne__(y) <==> x!=y
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __setattr__(...)
     |      x.__setattr__('name', value) <==> x.name = value
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __new__ = <built-in method __new__ of PythonQt.PythonQtClassWrapper ob...
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
    
    class QSizeF(PythonQt.PythonQtInstanceWrapper)
     |  Method resolution order:
     |      QSizeF
     |      PythonQt.PythonQtInstanceWrapper
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  __add__(...)
     |      x.__add__(y) <==> x+y
     |  
     |  __div__(...)
     |      x.__div__(y) <==> x/y
     |  
     |  __eq__(...)
     |      x.__eq__(y) <==> x==y
     |  
     |  __iadd__(...)
     |      x.__iadd__(y) <==> x+=y
     |  
     |  __idiv__(...)
     |      x.__idiv__(y) <==> x/=y
     |  
     |  __imul__(...)
     |      x.__imul__(y) <==> x*=y
     |  
     |  __init__(...)
     |      x.__init__(...) initializes x; see help(type(x)) for signature
     |  
     |  __isub__(...)
     |      x.__isub__(y) <==> x-=y
     |  
     |  __itruediv__(...)
     |      x.__itruediv__(y) <==> x/=y
     |  
     |  __mul__(...)
     |      x.__mul__(y) <==> x*y
     |  
     |  __neg__(...)
     |      x.__neg__() <==> -x
     |  
     |  __nonzero__(...)
     |      x.__nonzero__() <==> x != 0
     |  
     |  __radd__(...)
     |      x.__radd__(y) <==> y+x
     |  
     |  __rdiv__(...)
     |      x.__rdiv__(y) <==> y/x
     |  
     |  __rmul__(...)
     |      x.__rmul__(y) <==> y*x
     |  
     |  __rsub__(...)
     |      x.__rsub__(y) <==> y-x
     |  
     |  __rtruediv__(...)
     |      x.__rtruediv__(y) <==> y/x
     |  
     |  __sub__(...)
     |      x.__sub__(y) <==> x-y
     |  
     |  __truediv__(...)
     |      x.__truediv__(y) <==> x/y
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  boundedTo = <unbound qt slot boundedTo of QSizeF type>
     |      X.boundedTo(a, b) -> PythonQt.QtCore.QSizeF
     |  
     |  className = <built-in method className of PythonQt.PythonQtClassWrappe...
     |      Return the classname of the object
     |  
     |  delete = <built-in method delete of PythonQt.PythonQtClassWrapper obje...
     |      Deletes the given C++ object
     |  
     |  expandedTo = <unbound qt slot expandedTo of QSizeF type>
     |      X.expandedTo(a, b) -> PythonQt.QtCore.QSizeF
     |  
     |  height = <unbound qt slot height of QSizeF type>
     |      X.height(a) -> float
     |  
     |  help = <built-in method help of PythonQt.PythonQtClassWrapper object>
     |      Shows the help of available methods for this class
     |  
     |  inherits = <built-in method inherits of PythonQt.PythonQtClassWrapper ...
     |      Returns if the class inherits or is of given type name
     |  
     |  isEmpty = <unbound qt slot isEmpty of QSizeF type>
     |      X.isEmpty(a) -> bool
     |  
     |  isNull = <unbound qt slot isNull of QSizeF type>
     |      X.isNull(a) -> bool
     |  
     |  isValid = <unbound qt slot isValid of QSizeF type>
     |      X.isValid(a) -> bool
     |  
     |  readFrom = <unbound qt slot readFrom of QSizeF type>
     |      X.readFrom(a, b)
     |  
     |  scale = <unbound qt slot scale of QSizeF type>
     |      X.scale(a, b, c, d)
     |  
     |  scaled = <unbound qt slot scaled of QSizeF type>
     |      X.scaled(a, b, c, d) -> PythonQt.QtCore.QSizeF
     |  
     |  setHeight = <unbound qt slot setHeight of QSizeF type>
     |      X.setHeight(a, b)
     |  
     |  setWidth = <unbound qt slot setWidth of QSizeF type>
     |      X.setWidth(a, b)
     |  
     |  toSize = <unbound qt slot toSize of QSizeF type>
     |      X.toSize(a) -> PythonQt.QtCore.QSize
     |  
     |  transpose = <unbound qt slot transpose of QSizeF type>
     |      X.transpose(a)
     |  
     |  transposed = <unbound qt slot transposed of QSizeF type>
     |      X.transposed(a) -> PythonQt.QtCore.QSizeF
     |  
     |  width = <unbound qt slot width of QSizeF type>
     |      X.width(a) -> float
     |  
     |  writeTo = <unbound qt slot writeTo of QSizeF type>
     |      X.writeTo(a, b)
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __delattr__(...)
     |      x.__delattr__('name') <==> del x.name
     |  
     |  __ge__(...)
     |      x.__ge__(y) <==> x>=y
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __gt__(...)
     |      x.__gt__(y) <==> x>y
     |  
     |  __hash__(...)
     |      x.__hash__() <==> hash(x)
     |  
     |  __le__(...)
     |      x.__le__(y) <==> x<=y
     |  
     |  __lt__(...)
     |      x.__lt__(y) <==> x<y
     |  
     |  __ne__(...)
     |      x.__ne__(y) <==> x!=y
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __setattr__(...)
     |      x.__setattr__('name', value) <==> x.name = value
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __new__ = <built-in method __new__ of PythonQt.PythonQtClassWrapper ob...
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
    
    class QSocketNotifier(PythonQt.PythonQtInstanceWrapper)
     |  Method resolution order:
     |      QSocketNotifier
     |      PythonQt.PythonQtInstanceWrapper
     |      __builtin__.object
     |  
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  Exception = 2
     |  
     |  Read = 0
     |  
     |  Type = <class 'PythonQt.QtCore.Type'>
     |  
     |  
     |  Write = 1
     |  
     |  activated = <unbound qt signal activated of QSocketNotifier type>
     |  
     |  
     |  blockSignals = <unbound qt slot blockSignals of QSocketNotifier type>
     |      X.blockSignals(a, b) -> bool
     |  
     |  childEvent = <unbound qt slot py_q_childEvent of QSocketNotifier type>
     |      X.childEvent(a, b)
     |  
     |  children = <unbound qt slot children of QSocketNotifier type>
     |      X.children(a) -> tuple
     |  
     |  className = <built-in method className of PythonQt.PythonQtClassWrappe...
     |      Return the classname of the object
     |  
     |  connect = <unbound qt slot connect of QSocketNotifier type>
     |      X.connect(a, b, c, d, e) -> bool
     |  
     |  customEvent = <unbound qt slot py_q_customEvent of QSocketNotifier typ...
     |      X.customEvent(a, b)
     |  
     |  delete = <built-in method delete of PythonQt.PythonQtClassWrapper obje...
     |      Deletes the given C++ object
     |  
     |  deleteLater = <unbound qt slot deleteLater of QSocketNotifier type>
     |      X.deleteLater()
     |  
     |  destroyed = <unbound qt signal destroyed of QSocketNotifier type>
     |  
     |  
     |  disconnect = <unbound qt slot disconnect of QSocketNotifier type>
     |      X.disconnect(a, b, c, d) -> bool
     |  
     |  dumpObjectInfo = <unbound qt slot dumpObjectInfo of QSocketNotifier ty...
     |      X.dumpObjectInfo(a)
     |  
     |  dumpObjectTree = <unbound qt slot dumpObjectTree of QSocketNotifier ty...
     |      X.dumpObjectTree(a)
     |  
     |  dynamicPropertyNames = <unbound qt slot dynamicPropertyNames of QSocke...
     |      X.dynamicPropertyNames(a)
     |  
     |  event = <unbound qt slot py_q_event of QSocketNotifier type>
     |      X.event(a, b) -> bool
     |  
     |  eventFilter = <unbound qt slot py_q_eventFilter of QSocketNotifier typ...
     |      X.eventFilter(a, b, c) -> bool
     |  
     |  findChild = <unbound qt slot findChild of QSocketNotifier type>
     |      X.findChild(a, b, c) -> PythonQt.private.QObject
     |  
     |  findChildren = <unbound qt slot findChildren of QSocketNotifier type>
     |      X.findChildren(a, b, c) -> tuple
     |  
     |  help = <built-in method help of PythonQt.PythonQtClassWrapper object>
     |      Shows the help of available methods for this class
     |  
     |  inherits = <built-in method inherits of PythonQt.PythonQtClassWrapper ...
     |      Returns if the class inherits or is of given type name
     |  
     |  installEventFilter = <unbound qt slot installEventFilter of QSocketNot...
     |      X.installEventFilter(a, b)
     |  
     |  isEnabled = <unbound qt slot isEnabled of QSocketNotifier type>
     |      X.isEnabled(a) -> bool
     |  
     |  isSignalConnected = <unbound qt slot isSignalConnected of QSocketNotif...
     |      X.isSignalConnected(a, b) -> bool
     |  
     |  isWidgetType = <unbound qt slot isWidgetType of QSocketNotifier type>
     |      X.isWidgetType(a) -> bool
     |  
     |  isWindowType = <unbound qt slot isWindowType of QSocketNotifier type>
     |      X.isWindowType(a) -> bool
     |  
     |  killTimer = <unbound qt slot killTimer of QSocketNotifier type>
     |      X.killTimer(a, b)
     |  
     |  metaObject = <unbound qt slot metaObject of QSocketNotifier type>
     |      X.metaObject(a) -> PythonQt.QtCore.QMetaObject
     |  
     |  moveToThread = <unbound qt slot moveToThread of QSocketNotifier type>
     |      X.moveToThread(a, b)
     |  
     |  objectName = None
     |  
     |  objectNameChanged = <unbound qt signal objectNameChanged of QSocketNot...
     |  
     |  
     |  parent = <unbound qt slot parent of QSocketNotifier type>
     |      X.parent(a) -> PythonQt.private.QObject
     |  
     |  property = <unbound qt slot property of QSocketNotifier type>
     |      X.property(a, b) -> object
     |  
     |  removeEventFilter = <unbound qt slot removeEventFilter of QSocketNotif...
     |      X.removeEventFilter(a, b)
     |  
     |  sender = <unbound qt slot sender of QSocketNotifier type>
     |      X.sender(a) -> PythonQt.private.QObject
     |  
     |  senderSignalIndex = <unbound qt slot senderSignalIndex of QSocketNotif...
     |      X.senderSignalIndex(a) -> int
     |  
     |  setEnabled = <unbound qt slot setEnabled of QSocketNotifier type>
     |      X.setEnabled(a)
     |  
     |  setObjectName = <unbound qt slot setObjectName of QSocketNotifier type...
     |      X.setObjectName(a, b)
     |  
     |  setParent = <unbound qt slot setParent of QSocketNotifier type>
     |      X.setParent(a, b)
     |  
     |  setProperty = <unbound qt slot setProperty of QSocketNotifier type>
     |      X.setProperty(a, b, c) -> bool
     |  
     |  signalsBlocked = <unbound qt slot signalsBlocked of QSocketNotifier ty...
     |      X.signalsBlocked(a) -> bool
     |  
     |  startTimer = <unbound qt slot startTimer of QSocketNotifier type>
     |      X.startTimer(a, b, c) -> int
     |  
     |  thread = <unbound qt slot thread of QSocketNotifier type>
     |      X.thread(a)
     |  
     |  timerEvent = <unbound qt slot py_q_timerEvent of QSocketNotifier type>
     |      X.timerEvent(a, b)
     |  
     |  tr = <unbound qt slot tr of QSocketNotifier type>
     |      X.tr(a, b, c, d) -> str
     |  
     |  type = <unbound qt slot type of QSocketNotifier type>
     |      X.type(a)
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __delattr__(...)
     |      x.__delattr__('name') <==> del x.name
     |  
     |  __eq__(...)
     |      x.__eq__(y) <==> x==y
     |  
     |  __ge__(...)
     |      x.__ge__(y) <==> x>=y
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __gt__(...)
     |      x.__gt__(y) <==> x>y
     |  
     |  __hash__(...)
     |      x.__hash__() <==> hash(x)
     |  
     |  __init__(...)
     |      x.__init__(...) initializes x; see help(type(x)) for signature
     |  
     |  __le__(...)
     |      x.__le__(y) <==> x<=y
     |  
     |  __lt__(...)
     |      x.__lt__(y) <==> x<y
     |  
     |  __ne__(...)
     |      x.__ne__(y) <==> x!=y
     |  
     |  __nonzero__(...)
     |      x.__nonzero__() <==> x != 0
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __setattr__(...)
     |      x.__setattr__('name', value) <==> x.name = value
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __new__ = <built-in method __new__ of PythonQt.PythonQtClassWrapper ob...
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
    
    class QStandardPaths(PythonQt.PythonQtInstanceWrapper)
     |  Method resolution order:
     |      QStandardPaths
     |      PythonQt.PythonQtInstanceWrapper
     |      __builtin__.object
     |  
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  AppConfigLocation = 18
     |  
     |  AppDataLocation = 17
     |  
     |  AppLocalDataLocation = 9
     |  
     |  ApplicationsLocation = 3
     |  
     |  CacheLocation = 10
     |  
     |  ConfigLocation = 13
     |  
     |  DataLocation = 9
     |  
     |  DesktopLocation = 0
     |  
     |  DocumentsLocation = 1
     |  
     |  DownloadLocation = 14
     |  
     |  FontsLocation = 2
     |  
     |  GenericCacheLocation = 15
     |  
     |  GenericConfigLocation = 16
     |  
     |  GenericDataLocation = 11
     |  
     |  HomeLocation = 8
     |  
     |  LocateDirectory = 1
     |  
     |  LocateFile = 0
     |  
     |  LocateOption = <class 'PythonQt.QtCore.LocateOption'>
     |  
     |  
     |  LocateOptions = <class 'PythonQt.QtCore.LocateOptions'>
     |  
     |  
     |  MoviesLocation = 5
     |  
     |  MusicLocation = 4
     |  
     |  PicturesLocation = 6
     |  
     |  RuntimeLocation = 12
     |  
     |  StandardLocation = <class 'PythonQt.QtCore.StandardLocation'>
     |  
     |  
     |  TempLocation = 7
     |  
     |  className = <built-in method className of PythonQt.PythonQtClassWrappe...
     |      Return the classname of the object
     |  
     |  delete = <built-in method delete of PythonQt.PythonQtClassWrapper obje...
     |      Deletes the given C++ object
     |  
     |  displayName = <unbound qt slot static_QStandardPaths_displayName of QS...
     |      X.displayName(a) -> str
     |  
     |  enableTestMode = <unbound qt slot static_QStandardPaths_enableTestMode...
     |      X.enableTestMode(a)
     |  
     |  findExecutable = <unbound qt slot static_QStandardPaths_findExecutable...
     |      X.findExecutable(a, b) -> str
     |  
     |  help = <built-in method help of PythonQt.PythonQtClassWrapper object>
     |      Shows the help of available methods for this class
     |  
     |  inherits = <built-in method inherits of PythonQt.PythonQtClassWrapper ...
     |      Returns if the class inherits or is of given type name
     |  
     |  isTestModeEnabled = <unbound qt slot static_QStandardPaths_isTestModeE...
     |      X.isTestModeEnabled() -> bool
     |  
     |  locate = <unbound qt slot static_QStandardPaths_locate of QStandardPat...
     |      X.locate(a, b, c) -> str
     |  
     |  locateAll = <unbound qt slot static_QStandardPaths_locateAll of QStand...
     |      X.locateAll(a, b, c) -> tuple
     |  
     |  setTestModeEnabled = <unbound qt slot static_QStandardPaths_setTestMod...
     |      X.setTestModeEnabled(a)
     |  
     |  standardLocations = <unbound qt slot static_QStandardPaths_standardLoc...
     |      X.standardLocations(a) -> tuple
     |  
     |  writableLocation = <unbound qt slot static_QStandardPaths_writableLoca...
     |      X.writableLocation(a) -> str
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __delattr__(...)
     |      x.__delattr__('name') <==> del x.name
     |  
     |  __eq__(...)
     |      x.__eq__(y) <==> x==y
     |  
     |  __ge__(...)
     |      x.__ge__(y) <==> x>=y
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __gt__(...)
     |      x.__gt__(y) <==> x>y
     |  
     |  __hash__(...)
     |      x.__hash__() <==> hash(x)
     |  
     |  __init__(...)
     |      x.__init__(...) initializes x; see help(type(x)) for signature
     |  
     |  __le__(...)
     |      x.__le__(y) <==> x<=y
     |  
     |  __lt__(...)
     |      x.__lt__(y) <==> x<y
     |  
     |  __ne__(...)
     |      x.__ne__(y) <==> x!=y
     |  
     |  __nonzero__(...)
     |      x.__nonzero__() <==> x != 0
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __setattr__(...)
     |      x.__setattr__('name', value) <==> x.name = value
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __new__ = <built-in method __new__ of PythonQt.PythonQtClassWrapper ob...
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
    
    class QState(PythonQt.PythonQtInstanceWrapper)
     |  Method resolution order:
     |      QState
     |      PythonQt.PythonQtInstanceWrapper
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  __init__(...)
     |      x.__init__(...) initializes x; see help(type(x)) for signature
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  ChildMode = <class 'PythonQt.QtCore.ChildMode'>
     |  
     |  
     |  DontRestoreProperties = 0
     |  
     |  ExclusiveStates = 0
     |  
     |  ParallelStates = 1
     |  
     |  RestorePolicy = <class 'PythonQt.QtCore.RestorePolicy'>
     |  
     |  
     |  RestoreProperties = 1
     |  
     |  active = None
     |  
     |  activeChanged = <unbound qt signal activeChanged of QState type>
     |  
     |  
     |  addTransition = <unbound qt slot addTransition of QState type>
     |      X.addTransition(a, b, c, d) -> PythonQt.QtCore.QAbstractTransition
     |  
     |  assignProperty = <unbound qt slot assignProperty of QState type>
     |      X.assignProperty(a, b, c, d)
     |  
     |  blockSignals = <unbound qt slot blockSignals of QState type>
     |      X.blockSignals(a, b) -> bool
     |  
     |  childEvent = <unbound qt slot py_q_childEvent of QState type>
     |      X.childEvent(a, b)
     |  
     |  childMode = None
     |  
     |  childModeChanged = <unbound qt signal childModeChanged of QState type>
     |  
     |  
     |  children = <unbound qt slot children of QState type>
     |      X.children(a) -> tuple
     |  
     |  className = <built-in method className of PythonQt.PythonQtClassWrappe...
     |      Return the classname of the object
     |  
     |  connect = <unbound qt slot connect of QState type>
     |      X.connect(a, b, c, d, e) -> bool
     |  
     |  customEvent = <unbound qt slot py_q_customEvent of QState type>
     |      X.customEvent(a, b)
     |  
     |  delete = <built-in method delete of PythonQt.PythonQtClassWrapper obje...
     |      Deletes the given C++ object
     |  
     |  deleteLater = <unbound qt slot deleteLater of QState type>
     |      X.deleteLater()
     |  
     |  destroyed = <unbound qt signal destroyed of QState type>
     |  
     |  
     |  disconnect = <unbound qt slot disconnect of QState type>
     |      X.disconnect(a, b, c, d) -> bool
     |  
     |  dumpObjectInfo = <unbound qt slot dumpObjectInfo of QState type>
     |      X.dumpObjectInfo(a)
     |  
     |  dumpObjectTree = <unbound qt slot dumpObjectTree of QState type>
     |      X.dumpObjectTree(a)
     |  
     |  dynamicPropertyNames = <unbound qt slot dynamicPropertyNames of QState...
     |      X.dynamicPropertyNames(a)
     |  
     |  entered = <unbound qt signal entered of QState type>
     |  
     |  
     |  errorState = QAbstractState (QAbstractState at: 0x0)
     |  
     |  errorStateChanged = <unbound qt signal errorStateChanged of QState typ...
     |  
     |  
     |  event = <unbound qt slot py_q_event of QState type>
     |      X.event(a, b) -> bool
     |  
     |  eventFilter = <unbound qt slot py_q_eventFilter of QState type>
     |      X.eventFilter(a, b, c) -> bool
     |  
     |  exited = <unbound qt signal exited of QState type>
     |  
     |  
     |  findChild = <unbound qt slot findChild of QState type>
     |      X.findChild(a, b, c) -> PythonQt.private.QObject
     |  
     |  findChildren = <unbound qt slot findChildren of QState type>
     |      X.findChildren(a, b, c) -> tuple
     |  
     |  finished = <unbound qt signal finished of QState type>
     |  
     |  
     |  help = <built-in method help of PythonQt.PythonQtClassWrapper object>
     |      Shows the help of available methods for this class
     |  
     |  inherits = <built-in method inherits of PythonQt.PythonQtClassWrapper ...
     |      Returns if the class inherits or is of given type name
     |  
     |  initialState = QAbstractState (QAbstractState at: 0x0)
     |  
     |  initialStateChanged = <unbound qt signal initialStateChanged of QState...
     |  
     |  
     |  installEventFilter = <unbound qt slot installEventFilter of QState typ...
     |      X.installEventFilter(a, b)
     |  
     |  isSignalConnected = <unbound qt slot isSignalConnected of QState type>
     |      X.isSignalConnected(a, b) -> bool
     |  
     |  isWidgetType = <unbound qt slot isWidgetType of QState type>
     |      X.isWidgetType(a) -> bool
     |  
     |  isWindowType = <unbound qt slot isWindowType of QState type>
     |      X.isWindowType(a) -> bool
     |  
     |  killTimer = <unbound qt slot killTimer of QState type>
     |      X.killTimer(a, b)
     |  
     |  machine = <unbound qt slot machine of QState type>
     |      X.machine(a) -> PythonQt.QtCore.QStateMachine
     |  
     |  metaObject = <unbound qt slot metaObject of QState type>
     |      X.metaObject(a) -> PythonQt.QtCore.QMetaObject
     |  
     |  moveToThread = <unbound qt slot moveToThread of QState type>
     |      X.moveToThread(a, b)
     |  
     |  objectName = None
     |  
     |  objectNameChanged = <unbound qt signal objectNameChanged of QState typ...
     |  
     |  
     |  onEntry = <unbound qt slot py_q_onEntry of QState type>
     |      X.onEntry(a, b)
     |  
     |  onExit = <unbound qt slot py_q_onExit of QState type>
     |      X.onExit(a, b)
     |  
     |  parent = <unbound qt slot parent of QState type>
     |      X.parent(a) -> PythonQt.private.QObject
     |  
     |  parentState = <unbound qt slot parentState of QState type>
     |      X.parentState(a) -> PythonQt.QtCore.QState
     |  
     |  propertiesAssigned = <unbound qt signal propertiesAssigned of QState t...
     |  
     |  
     |  property = <unbound qt slot property of QState type>
     |      X.property(a, b) -> object
     |  
     |  removeEventFilter = <unbound qt slot removeEventFilter of QState type>
     |      X.removeEventFilter(a, b)
     |  
     |  removeTransition = <unbound qt slot removeTransition of QState type>
     |      X.removeTransition(a, b)
     |  
     |  sender = <unbound qt slot sender of QState type>
     |      X.sender(a) -> PythonQt.private.QObject
     |  
     |  senderSignalIndex = <unbound qt slot senderSignalIndex of QState type>
     |      X.senderSignalIndex(a) -> int
     |  
     |  setChildMode = <unbound qt slot setChildMode of QState type>
     |      X.setChildMode(a, b)
     |  
     |  setErrorState = <unbound qt slot setErrorState of QState type>
     |      X.setErrorState(a, b)
     |  
     |  setInitialState = <unbound qt slot setInitialState of QState type>
     |      X.setInitialState(a, b)
     |  
     |  setObjectName = <unbound qt slot setObjectName of QState type>
     |      X.setObjectName(a, b)
     |  
     |  setParent = <unbound qt slot setParent of QState type>
     |      X.setParent(a, b)
     |  
     |  setProperty = <unbound qt slot setProperty of QState type>
     |      X.setProperty(a, b, c) -> bool
     |  
     |  signalsBlocked = <unbound qt slot signalsBlocked of QState type>
     |      X.signalsBlocked(a) -> bool
     |  
     |  startTimer = <unbound qt slot startTimer of QState type>
     |      X.startTimer(a, b, c) -> int
     |  
     |  thread = <unbound qt slot thread of QState type>
     |      X.thread(a)
     |  
     |  timerEvent = <unbound qt slot py_q_timerEvent of QState type>
     |      X.timerEvent(a, b)
     |  
     |  tr = <unbound qt slot tr of QState type>
     |      X.tr(a, b, c, d) -> str
     |  
     |  transitions = <unbound qt slot transitions of QState type>
     |      X.transitions(a) -> tuple
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __delattr__(...)
     |      x.__delattr__('name') <==> del x.name
     |  
     |  __eq__(...)
     |      x.__eq__(y) <==> x==y
     |  
     |  __ge__(...)
     |      x.__ge__(y) <==> x>=y
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __gt__(...)
     |      x.__gt__(y) <==> x>y
     |  
     |  __hash__(...)
     |      x.__hash__() <==> hash(x)
     |  
     |  __le__(...)
     |      x.__le__(y) <==> x<=y
     |  
     |  __lt__(...)
     |      x.__lt__(y) <==> x<y
     |  
     |  __ne__(...)
     |      x.__ne__(y) <==> x!=y
     |  
     |  __nonzero__(...)
     |      x.__nonzero__() <==> x != 0
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __setattr__(...)
     |      x.__setattr__('name', value) <==> x.name = value
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __new__ = <built-in method __new__ of PythonQt.PythonQtClassWrapper ob...
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
    
    class QStateMachine(PythonQt.PythonQtInstanceWrapper)
     |  Method resolution order:
     |      QStateMachine
     |      PythonQt.PythonQtInstanceWrapper
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  __init__(...)
     |      x.__init__(...) initializes x; see help(type(x)) for signature
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  ChildMode = <class 'PythonQt.QtCore.ChildMode'>
     |  
     |  
     |  DontRestoreProperties = 0
     |  
     |  Error = <class 'PythonQt.QtCore.Error'>
     |  
     |  
     |  EventPriority = <class 'PythonQt.QtCore.EventPriority'>
     |  
     |  
     |  ExclusiveStates = 0
     |  
     |  HighPriority = 1
     |  
     |  NoCommonAncestorForTransitionError = 3
     |  
     |  NoDefaultStateInHistoryStateError = 2
     |  
     |  NoError = 0
     |  
     |  NoInitialStateError = 1
     |  
     |  NormalPriority = 0
     |  
     |  ParallelStates = 1
     |  
     |  RestorePolicy = <class 'PythonQt.QtCore.RestorePolicy'>
     |  
     |  
     |  RestoreProperties = 1
     |  
     |  SignalEvent = <class 'PythonQt.QtCore.SignalEvent'>
     |  
     |  
     |  WrappedEvent = <class 'PythonQt.QtCore.WrappedEvent'>
     |  
     |  
     |  active = None
     |  
     |  activeChanged = <unbound qt signal activeChanged of QStateMachine type...
     |  
     |  
     |  addDefaultAnimation = <unbound qt slot addDefaultAnimation of QStateMa...
     |      X.addDefaultAnimation(a, b)
     |  
     |  addState = <unbound qt slot addState of QStateMachine type>
     |      X.addState(a, b)
     |  
     |  addTransition = <unbound qt slot addTransition of QStateMachine type>
     |      X.addTransition(a, b, c, d) -> PythonQt.QtCore.QAbstractTransition
     |  
     |  animated = None
     |  
     |  assignProperty = <unbound qt slot assignProperty of QStateMachine type...
     |      X.assignProperty(a, b, c, d)
     |  
     |  beginMicrostep = <unbound qt slot py_q_beginMicrostep of QStateMachine...
     |      X.beginMicrostep(a, b)
     |  
     |  beginSelectTransitions = <unbound qt slot py_q_beginSelectTransitions ...
     |      X.beginSelectTransitions(a, b)
     |  
     |  blockSignals = <unbound qt slot blockSignals of QStateMachine type>
     |      X.blockSignals(a, b) -> bool
     |  
     |  cancelDelayedEvent = <unbound qt slot cancelDelayedEvent of QStateMach...
     |      X.cancelDelayedEvent(a, b) -> bool
     |  
     |  childEvent = <unbound qt slot py_q_childEvent of QStateMachine type>
     |      X.childEvent(a, b)
     |  
     |  childMode = None
     |  
     |  childModeChanged = <unbound qt signal childModeChanged of QStateMachin...
     |  
     |  
     |  children = <unbound qt slot children of QStateMachine type>
     |      X.children(a) -> tuple
     |  
     |  className = <built-in method className of PythonQt.PythonQtClassWrappe...
     |      Return the classname of the object
     |  
     |  clearError = <unbound qt slot clearError of QStateMachine type>
     |      X.clearError(a)
     |  
     |  configuration = <unbound qt slot configuration of QStateMachine type>
     |      X.configuration(a)
     |  
     |  connect = <unbound qt slot connect of QStateMachine type>
     |      X.connect(a, b, c, d, e) -> bool
     |  
     |  customEvent = <unbound qt slot py_q_customEvent of QStateMachine type>
     |      X.customEvent(a, b)
     |  
     |  defaultAnimations = <unbound qt slot defaultAnimations of QStateMachin...
     |      X.defaultAnimations(a) -> tuple
     |  
     |  delete = <built-in method delete of PythonQt.PythonQtClassWrapper obje...
     |      Deletes the given C++ object
     |  
     |  deleteLater = <unbound qt slot deleteLater of QStateMachine type>
     |      X.deleteLater()
     |  
     |  destroyed = <unbound qt signal destroyed of QStateMachine type>
     |  
     |  
     |  disconnect = <unbound qt slot disconnect of QStateMachine type>
     |      X.disconnect(a, b, c, d) -> bool
     |  
     |  dumpObjectInfo = <unbound qt slot dumpObjectInfo of QStateMachine type...
     |      X.dumpObjectInfo(a)
     |  
     |  dumpObjectTree = <unbound qt slot dumpObjectTree of QStateMachine type...
     |      X.dumpObjectTree(a)
     |  
     |  dynamicPropertyNames = <unbound qt slot dynamicPropertyNames of QState...
     |      X.dynamicPropertyNames(a)
     |  
     |  endMicrostep = <unbound qt slot py_q_endMicrostep of QStateMachine typ...
     |      X.endMicrostep(a, b)
     |  
     |  endSelectTransitions = <unbound qt slot py_q_endSelectTransitions of Q...
     |      X.endSelectTransitions(a, b)
     |  
     |  entered = <unbound qt signal entered of QStateMachine type>
     |  
     |  
     |  error = <unbound qt slot error of QStateMachine type>
     |      X.error(a)
     |  
     |  errorState = QAbstractState (QAbstractState at: 0x0)
     |  
     |  errorStateChanged = <unbound qt signal errorStateChanged of QStateMach...
     |  
     |  
     |  errorString = None
     |  
     |  event = <unbound qt slot py_q_event of QStateMachine type>
     |      X.event(a, b) -> bool
     |  
     |  eventFilter = <unbound qt slot py_q_eventFilter of QStateMachine type>
     |      X.eventFilter(a, b, c) -> bool
     |  
     |  exited = <unbound qt signal exited of QStateMachine type>
     |  
     |  
     |  findChild = <unbound qt slot findChild of QStateMachine type>
     |      X.findChild(a, b, c) -> PythonQt.private.QObject
     |  
     |  findChildren = <unbound qt slot findChildren of QStateMachine type>
     |      X.findChildren(a, b, c) -> tuple
     |  
     |  finished = <unbound qt signal finished of QStateMachine type>
     |  
     |  
     |  globalRestorePolicy = None
     |  
     |  help = <built-in method help of PythonQt.PythonQtClassWrapper object>
     |      Shows the help of available methods for this class
     |  
     |  inherits = <built-in method inherits of PythonQt.PythonQtClassWrapper ...
     |      Returns if the class inherits or is of given type name
     |  
     |  initialState = QAbstractState (QAbstractState at: 0x0)
     |  
     |  initialStateChanged = <unbound qt signal initialStateChanged of QState...
     |  
     |  
     |  installEventFilter = <unbound qt slot installEventFilter of QStateMach...
     |      X.installEventFilter(a, b)
     |  
     |  isAnimated = <unbound qt slot isAnimated of QStateMachine type>
     |      X.isAnimated(a) -> bool
     |  
     |  isRunning = <unbound qt slot isRunning of QStateMachine type>
     |      X.isRunning(a) -> bool
     |  
     |  isSignalConnected = <unbound qt slot isSignalConnected of QStateMachin...
     |      X.isSignalConnected(a, b) -> bool
     |  
     |  isWidgetType = <unbound qt slot isWidgetType of QStateMachine type>
     |      X.isWidgetType(a) -> bool
     |  
     |  isWindowType = <unbound qt slot isWindowType of QStateMachine type>
     |      X.isWindowType(a) -> bool
     |  
     |  killTimer = <unbound qt slot killTimer of QStateMachine type>
     |      X.killTimer(a, b)
     |  
     |  machine = <unbound qt slot machine of QStateMachine type>
     |      X.machine(a) -> PythonQt.QtCore.QStateMachine
     |  
     |  metaObject = <unbound qt slot metaObject of QStateMachine type>
     |      X.metaObject(a) -> PythonQt.QtCore.QMetaObject
     |  
     |  moveToThread = <unbound qt slot moveToThread of QStateMachine type>
     |      X.moveToThread(a, b)
     |  
     |  objectName = None
     |  
     |  objectNameChanged = <unbound qt signal objectNameChanged of QStateMach...
     |  
     |  
     |  onEntry = <unbound qt slot py_q_onEntry of QStateMachine type>
     |      X.onEntry(a, b)
     |  
     |  onExit = <unbound qt slot py_q_onExit of QStateMachine type>
     |      X.onExit(a, b)
     |  
     |  parent = <unbound qt slot parent of QStateMachine type>
     |      X.parent(a) -> PythonQt.private.QObject
     |  
     |  parentState = <unbound qt slot parentState of QStateMachine type>
     |      X.parentState(a) -> PythonQt.QtCore.QState
     |  
     |  postDelayedEvent = <unbound qt slot postDelayedEvent of QStateMachine ...
     |      X.postDelayedEvent(a, b, c) -> int
     |  
     |  postEvent = <unbound qt slot postEvent of QStateMachine type>
     |      X.postEvent(a, b, c)
     |  
     |  propertiesAssigned = <unbound qt signal propertiesAssigned of QStateMa...
     |  
     |  
     |  property = <unbound qt slot property of QStateMachine type>
     |      X.property(a, b) -> object
     |  
     |  removeDefaultAnimation = <unbound qt slot removeDefaultAnimation of QS...
     |      X.removeDefaultAnimation(a, b)
     |  
     |  removeEventFilter = <unbound qt slot removeEventFilter of QStateMachin...
     |      X.removeEventFilter(a, b)
     |  
     |  removeState = <unbound qt slot removeState of QStateMachine type>
     |      X.removeState(a, b)
     |  
     |  removeTransition = <unbound qt slot removeTransition of QStateMachine ...
     |      X.removeTransition(a, b)
     |  
     |  running = None
     |  
     |  runningChanged = <unbound qt signal runningChanged of QStateMachine ty...
     |  
     |  
     |  sender = <unbound qt slot sender of QStateMachine type>
     |      X.sender(a) -> PythonQt.private.QObject
     |  
     |  senderSignalIndex = <unbound qt slot senderSignalIndex of QStateMachin...
     |      X.senderSignalIndex(a) -> int
     |  
     |  setAnimated = <unbound qt slot setAnimated of QStateMachine type>
     |      X.setAnimated(a, b)
     |  
     |  setChildMode = <unbound qt slot setChildMode of QStateMachine type>
     |      X.setChildMode(a, b)
     |  
     |  setErrorState = <unbound qt slot setErrorState of QStateMachine type>
     |      X.setErrorState(a, b)
     |  
     |  setGlobalRestorePolicy = <unbound qt slot setGlobalRestorePolicy of QS...
     |      X.setGlobalRestorePolicy(a, b)
     |  
     |  setInitialState = <unbound qt slot setInitialState of QStateMachine ty...
     |      X.setInitialState(a, b)
     |  
     |  setObjectName = <unbound qt slot setObjectName of QStateMachine type>
     |      X.setObjectName(a, b)
     |  
     |  setParent = <unbound qt slot setParent of QStateMachine type>
     |      X.setParent(a, b)
     |  
     |  setProperty = <unbound qt slot setProperty of QStateMachine type>
     |      X.setProperty(a, b, c) -> bool
     |  
     |  setRunning = <unbound qt slot setRunning of QStateMachine type>
     |      X.setRunning(a)
     |  
     |  signalsBlocked = <unbound qt slot signalsBlocked of QStateMachine type...
     |      X.signalsBlocked(a) -> bool
     |  
     |  start = <unbound qt slot start of QStateMachine type>
     |      X.start()
     |  
     |  startTimer = <unbound qt slot startTimer of QStateMachine type>
     |      X.startTimer(a, b, c) -> int
     |  
     |  started = <unbound qt signal started of QStateMachine type>
     |  
     |  
     |  stop = <unbound qt slot stop of QStateMachine type>
     |      X.stop()
     |  
     |  stopped = <unbound qt signal stopped of QStateMachine type>
     |  
     |  
     |  thread = <unbound qt slot thread of QStateMachine type>
     |      X.thread(a)
     |  
     |  timerEvent = <unbound qt slot py_q_timerEvent of QStateMachine type>
     |      X.timerEvent(a, b)
     |  
     |  tr = <unbound qt slot tr of QStateMachine type>
     |      X.tr(a, b, c, d) -> str
     |  
     |  transitions = <unbound qt slot transitions of QStateMachine type>
     |      X.transitions(a) -> tuple
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __delattr__(...)
     |      x.__delattr__('name') <==> del x.name
     |  
     |  __eq__(...)
     |      x.__eq__(y) <==> x==y
     |  
     |  __ge__(...)
     |      x.__ge__(y) <==> x>=y
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __gt__(...)
     |      x.__gt__(y) <==> x>y
     |  
     |  __hash__(...)
     |      x.__hash__() <==> hash(x)
     |  
     |  __le__(...)
     |      x.__le__(y) <==> x<=y
     |  
     |  __lt__(...)
     |      x.__lt__(y) <==> x<y
     |  
     |  __ne__(...)
     |      x.__ne__(y) <==> x!=y
     |  
     |  __nonzero__(...)
     |      x.__nonzero__() <==> x != 0
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __setattr__(...)
     |      x.__setattr__('name', value) <==> x.name = value
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __new__ = <built-in method __new__ of PythonQt.PythonQtClassWrapper ob...
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
    
    class QStorageInfo(PythonQt.PythonQtInstanceWrapper)
     |  Method resolution order:
     |      QStorageInfo
     |      PythonQt.PythonQtInstanceWrapper
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  __eq__(...)
     |      x.__eq__(y) <==> x==y
     |  
     |  __init__(...)
     |      x.__init__(...) initializes x; see help(type(x)) for signature
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  blockSize = <unbound qt slot blockSize of QStorageInfo type>
     |      X.blockSize(a) -> int
     |  
     |  bytesAvailable = <unbound qt slot bytesAvailable of QStorageInfo type>
     |      X.bytesAvailable(a) -> int
     |  
     |  bytesFree = <unbound qt slot bytesFree of QStorageInfo type>
     |      X.bytesFree(a) -> int
     |  
     |  bytesTotal = <unbound qt slot bytesTotal of QStorageInfo type>
     |      X.bytesTotal(a) -> int
     |  
     |  className = <built-in method className of PythonQt.PythonQtClassWrappe...
     |      Return the classname of the object
     |  
     |  delete = <built-in method delete of PythonQt.PythonQtClassWrapper obje...
     |      Deletes the given C++ object
     |  
     |  device = <unbound qt slot device of QStorageInfo type>
     |      X.device(a) -> PythonQt.QtCore.QByteArray
     |  
     |  displayName = <unbound qt slot displayName of QStorageInfo type>
     |      X.displayName(a) -> str
     |  
     |  fileSystemType = <unbound qt slot fileSystemType of QStorageInfo type>
     |      X.fileSystemType(a) -> PythonQt.QtCore.QByteArray
     |  
     |  help = <built-in method help of PythonQt.PythonQtClassWrapper object>
     |      Shows the help of available methods for this class
     |  
     |  inherits = <built-in method inherits of PythonQt.PythonQtClassWrapper ...
     |      Returns if the class inherits or is of given type name
     |  
     |  isReadOnly = <unbound qt slot isReadOnly of QStorageInfo type>
     |      X.isReadOnly(a) -> bool
     |  
     |  isReady = <unbound qt slot isReady of QStorageInfo type>
     |      X.isReady(a) -> bool
     |  
     |  isRoot = <unbound qt slot isRoot of QStorageInfo type>
     |      X.isRoot(a) -> bool
     |  
     |  isValid = <unbound qt slot isValid of QStorageInfo type>
     |      X.isValid(a) -> bool
     |  
     |  mountedVolumes = <unbound qt slot static_QStorageInfo_mountedVolumes o...
     |      X.mountedVolumes() -> tuple
     |  
     |  name = <unbound qt slot name of QStorageInfo type>
     |      X.name(a) -> str
     |  
     |  operator_assign = <unbound qt slot operator_assign of QStorageInfo typ...
     |      X.operator_assign(a, b) -> PythonQt.QtCore.QStorageInfo
     |  
     |  refresh = <unbound qt slot refresh of QStorageInfo type>
     |      X.refresh(a)
     |  
     |  root = <unbound qt slot static_QStorageInfo_root of QStorageInfo type>
     |      X.root() -> PythonQt.QtCore.QStorageInfo
     |  
     |  rootPath = <unbound qt slot rootPath of QStorageInfo type>
     |      X.rootPath(a) -> str
     |  
     |  setPath = <unbound qt slot setPath of QStorageInfo type>
     |      X.setPath(a, b)
     |  
     |  swap = <unbound qt slot swap of QStorageInfo type>
     |      X.swap(a, b)
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __delattr__(...)
     |      x.__delattr__('name') <==> del x.name
     |  
     |  __ge__(...)
     |      x.__ge__(y) <==> x>=y
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __gt__(...)
     |      x.__gt__(y) <==> x>y
     |  
     |  __hash__(...)
     |      x.__hash__() <==> hash(x)
     |  
     |  __le__(...)
     |      x.__le__(y) <==> x<=y
     |  
     |  __lt__(...)
     |      x.__lt__(y) <==> x<y
     |  
     |  __ne__(...)
     |      x.__ne__(y) <==> x!=y
     |  
     |  __nonzero__(...)
     |      x.__nonzero__() <==> x != 0
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __setattr__(...)
     |      x.__setattr__('name', value) <==> x.name = value
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __new__ = <built-in method __new__ of PythonQt.PythonQtClassWrapper ob...
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
    
    class QStringMatcher(PythonQt.PythonQtInstanceWrapper)
     |  Method resolution order:
     |      QStringMatcher
     |      PythonQt.PythonQtInstanceWrapper
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  __init__(...)
     |      x.__init__(...) initializes x; see help(type(x)) for signature
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  caseSensitivity = <unbound qt slot caseSensitivity of QStringMatcher t...
     |      X.caseSensitivity(a)
     |  
     |  className = <built-in method className of PythonQt.PythonQtClassWrappe...
     |      Return the classname of the object
     |  
     |  delete = <built-in method delete of PythonQt.PythonQtClassWrapper obje...
     |      Deletes the given C++ object
     |  
     |  help = <built-in method help of PythonQt.PythonQtClassWrapper object>
     |      Shows the help of available methods for this class
     |  
     |  indexIn = <unbound qt slot indexIn of QStringMatcher type>
     |      X.indexIn(a, b, c) -> int
     |  
     |  inherits = <built-in method inherits of PythonQt.PythonQtClassWrapper ...
     |      Returns if the class inherits or is of given type name
     |  
     |  pattern = <unbound qt slot pattern of QStringMatcher type>
     |      X.pattern(a) -> str
     |  
     |  setCaseSensitivity = <unbound qt slot setCaseSensitivity of QStringMat...
     |      X.setCaseSensitivity(a, b)
     |  
     |  setPattern = <unbound qt slot setPattern of QStringMatcher type>
     |      X.setPattern(a, b)
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __delattr__(...)
     |      x.__delattr__('name') <==> del x.name
     |  
     |  __eq__(...)
     |      x.__eq__(y) <==> x==y
     |  
     |  __ge__(...)
     |      x.__ge__(y) <==> x>=y
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __gt__(...)
     |      x.__gt__(y) <==> x>y
     |  
     |  __hash__(...)
     |      x.__hash__() <==> hash(x)
     |  
     |  __le__(...)
     |      x.__le__(y) <==> x<=y
     |  
     |  __lt__(...)
     |      x.__lt__(y) <==> x<y
     |  
     |  __ne__(...)
     |      x.__ne__(y) <==> x!=y
     |  
     |  __nonzero__(...)
     |      x.__nonzero__() <==> x != 0
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __setattr__(...)
     |      x.__setattr__('name', value) <==> x.name = value
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __new__ = <built-in method __new__ of PythonQt.PythonQtClassWrapper ob...
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
    
    class QSysInfo(PythonQt.PythonQtInstanceWrapper)
     |  Method resolution order:
     |      QSysInfo
     |      PythonQt.PythonQtInstanceWrapper
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  __init__(...)
     |      x.__init__(...) initializes x; see help(type(x)) for signature
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  BigEndian = 0
     |  
     |  ByteOrder = 1
     |  
     |  Endian = <class 'PythonQt.QtCore.Endian'>
     |  
     |  
     |  LittleEndian = 1
     |  
     |  Sizes = <class 'PythonQt.QtCore.Sizes'>
     |  
     |  
     |  WordSize = 64
     |  
     |  buildAbi = <unbound qt slot static_QSysInfo_buildAbi of QSysInfo type>
     |      X.buildAbi() -> str
     |  
     |  buildCpuArchitecture = <unbound qt slot static_QSysInfo_buildCpuArchit...
     |      X.buildCpuArchitecture() -> str
     |  
     |  className = <built-in method className of PythonQt.PythonQtClassWrappe...
     |      Return the classname of the object
     |  
     |  currentCpuArchitecture = <unbound qt slot static_QSysInfo_currentCpuAr...
     |      X.currentCpuArchitecture() -> str
     |  
     |  delete = <built-in method delete of PythonQt.PythonQtClassWrapper obje...
     |      Deletes the given C++ object
     |  
     |  help = <built-in method help of PythonQt.PythonQtClassWrapper object>
     |      Shows the help of available methods for this class
     |  
     |  inherits = <built-in method inherits of PythonQt.PythonQtClassWrapper ...
     |      Returns if the class inherits or is of given type name
     |  
     |  kernelType = <unbound qt slot static_QSysInfo_kernelType of QSysInfo t...
     |      X.kernelType() -> str
     |  
     |  kernelVersion = <unbound qt slot static_QSysInfo_kernelVersion of QSys...
     |      X.kernelVersion() -> str
     |  
     |  machineHostName = <unbound qt slot static_QSysInfo_machineHostName of ...
     |      X.machineHostName() -> str
     |  
     |  prettyProductName = <unbound qt slot static_QSysInfo_prettyProductName...
     |      X.prettyProductName() -> str
     |  
     |  productType = <unbound qt slot static_QSysInfo_productType of QSysInfo...
     |      X.productType() -> str
     |  
     |  productVersion = <unbound qt slot static_QSysInfo_productVersion of QS...
     |      X.productVersion() -> str
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __delattr__(...)
     |      x.__delattr__('name') <==> del x.name
     |  
     |  __eq__(...)
     |      x.__eq__(y) <==> x==y
     |  
     |  __ge__(...)
     |      x.__ge__(y) <==> x>=y
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __gt__(...)
     |      x.__gt__(y) <==> x>y
     |  
     |  __hash__(...)
     |      x.__hash__() <==> hash(x)
     |  
     |  __le__(...)
     |      x.__le__(y) <==> x<=y
     |  
     |  __lt__(...)
     |      x.__lt__(y) <==> x<y
     |  
     |  __ne__(...)
     |      x.__ne__(y) <==> x!=y
     |  
     |  __nonzero__(...)
     |      x.__nonzero__() <==> x != 0
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __setattr__(...)
     |      x.__setattr__('name', value) <==> x.name = value
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __new__ = <built-in method __new__ of PythonQt.PythonQtClassWrapper ob...
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
    
    class QSystemSemaphore(PythonQt.PythonQtInstanceWrapper)
     |  Method resolution order:
     |      QSystemSemaphore
     |      PythonQt.PythonQtInstanceWrapper
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  __init__(...)
     |      x.__init__(...) initializes x; see help(type(x)) for signature
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  AccessMode = <class 'PythonQt.QtCore.AccessMode'>
     |  
     |  
     |  AlreadyExists = 3
     |  
     |  Create = 1
     |  
     |  KeyError = 2
     |  
     |  NoError = 0
     |  
     |  NotFound = 4
     |  
     |  Open = 0
     |  
     |  OutOfResources = 5
     |  
     |  PermissionDenied = 1
     |  
     |  SystemSemaphoreError = <class 'PythonQt.QtCore.SystemSemaphoreError'>
     |  
     |  
     |  UnknownError = 6
     |  
     |  acquire = <unbound qt slot acquire of QSystemSemaphore type>
     |      X.acquire(a) -> bool
     |  
     |  className = <built-in method className of PythonQt.PythonQtClassWrappe...
     |      Return the classname of the object
     |  
     |  delete = <built-in method delete of PythonQt.PythonQtClassWrapper obje...
     |      Deletes the given C++ object
     |  
     |  error = <unbound qt slot error of QSystemSemaphore type>
     |      X.error(a)
     |  
     |  errorString = <unbound qt slot errorString of QSystemSemaphore type>
     |      X.errorString(a) -> str
     |  
     |  help = <built-in method help of PythonQt.PythonQtClassWrapper object>
     |      Shows the help of available methods for this class
     |  
     |  inherits = <built-in method inherits of PythonQt.PythonQtClassWrapper ...
     |      Returns if the class inherits or is of given type name
     |  
     |  key = <unbound qt slot key of QSystemSemaphore type>
     |      X.key(a) -> str
     |  
     |  release = <unbound qt slot release of QSystemSemaphore type>
     |      X.release(a, b) -> bool
     |  
     |  setKey = <unbound qt slot setKey of QSystemSemaphore type>
     |      X.setKey(a, b, c, d)
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __delattr__(...)
     |      x.__delattr__('name') <==> del x.name
     |  
     |  __eq__(...)
     |      x.__eq__(y) <==> x==y
     |  
     |  __ge__(...)
     |      x.__ge__(y) <==> x>=y
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __gt__(...)
     |      x.__gt__(y) <==> x>y
     |  
     |  __hash__(...)
     |      x.__hash__() <==> hash(x)
     |  
     |  __le__(...)
     |      x.__le__(y) <==> x<=y
     |  
     |  __lt__(...)
     |      x.__lt__(y) <==> x<y
     |  
     |  __ne__(...)
     |      x.__ne__(y) <==> x!=y
     |  
     |  __nonzero__(...)
     |      x.__nonzero__() <==> x != 0
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __setattr__(...)
     |      x.__setattr__('name', value) <==> x.name = value
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __new__ = <built-in method __new__ of PythonQt.PythonQtClassWrapper ob...
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
    
    class QTemporaryDir(PythonQt.PythonQtInstanceWrapper)
     |  Method resolution order:
     |      QTemporaryDir
     |      PythonQt.PythonQtInstanceWrapper
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  __init__(...)
     |      x.__init__(...) initializes x; see help(type(x)) for signature
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  autoRemove = <unbound qt slot autoRemove of QTemporaryDir type>
     |      X.autoRemove(a) -> bool
     |  
     |  className = <built-in method className of PythonQt.PythonQtClassWrappe...
     |      Return the classname of the object
     |  
     |  delete = <built-in method delete of PythonQt.PythonQtClassWrapper obje...
     |      Deletes the given C++ object
     |  
     |  errorString = <unbound qt slot errorString of QTemporaryDir type>
     |      X.errorString(a) -> str
     |  
     |  help = <built-in method help of PythonQt.PythonQtClassWrapper object>
     |      Shows the help of available methods for this class
     |  
     |  inherits = <built-in method inherits of PythonQt.PythonQtClassWrapper ...
     |      Returns if the class inherits or is of given type name
     |  
     |  isValid = <unbound qt slot isValid of QTemporaryDir type>
     |      X.isValid(a) -> bool
     |  
     |  path = <unbound qt slot path of QTemporaryDir type>
     |      X.path(a) -> str
     |  
     |  remove = <unbound qt slot remove of QTemporaryDir type>
     |      X.remove(a) -> bool
     |  
     |  setAutoRemove = <unbound qt slot setAutoRemove of QTemporaryDir type>
     |      X.setAutoRemove(a, b)
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __delattr__(...)
     |      x.__delattr__('name') <==> del x.name
     |  
     |  __eq__(...)
     |      x.__eq__(y) <==> x==y
     |  
     |  __ge__(...)
     |      x.__ge__(y) <==> x>=y
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __gt__(...)
     |      x.__gt__(y) <==> x>y
     |  
     |  __hash__(...)
     |      x.__hash__() <==> hash(x)
     |  
     |  __le__(...)
     |      x.__le__(y) <==> x<=y
     |  
     |  __lt__(...)
     |      x.__lt__(y) <==> x<y
     |  
     |  __ne__(...)
     |      x.__ne__(y) <==> x!=y
     |  
     |  __nonzero__(...)
     |      x.__nonzero__() <==> x != 0
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __setattr__(...)
     |      x.__setattr__('name', value) <==> x.name = value
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __new__ = <built-in method __new__ of PythonQt.PythonQtClassWrapper ob...
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
    
    class QTemporaryFile(PythonQt.PythonQtInstanceWrapper)
     |  Method resolution order:
     |      QTemporaryFile
     |      PythonQt.PythonQtInstanceWrapper
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  __init__(...)
     |      x.__init__(...) initializes x; see help(type(x)) for signature
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  AbortError = 6
     |  
     |  Append = 4
     |  
     |  AutoCloseHandle = 1
     |  
     |  CopyError = 14
     |  
     |  DontCloseHandle = 0
     |  
     |  ExeGroup = 16
     |  
     |  ExeOther = 1
     |  
     |  ExeOwner = 4096
     |  
     |  ExeUser = 256
     |  
     |  FatalError = 3
     |  
     |  FileError = <class 'PythonQt.QtCore.FileError'>
     |  
     |  
     |  FileHandleFlag = <class 'PythonQt.QtCore.FileHandleFlag'>
     |  
     |  
     |  FileHandleFlags = <class 'PythonQt.QtCore.FileHandleFlags'>
     |  
     |  
     |  MapPrivateOption = 1
     |  
     |  MemoryMapFlags = <class 'PythonQt.QtCore.MemoryMapFlags'>
     |  
     |  
     |  NoError = 0
     |  
     |  NoOptions = 0
     |  
     |  NotOpen = 0
     |  
     |  OpenError = 5
     |  
     |  OpenMode = <class 'PythonQt.QtCore.OpenMode'>
     |  
     |  
     |  OpenModeFlag = <class 'PythonQt.QtCore.OpenModeFlag'>
     |  
     |  
     |  Permission = <class 'PythonQt.QtCore.Permission'>
     |  
     |  
     |  Permissions = <class 'PythonQt.QtCore.Permissions'>
     |  
     |  
     |  PermissionsError = 13
     |  
     |  PositionError = 11
     |  
     |  ReadError = 1
     |  
     |  ReadGroup = 64
     |  
     |  ReadOnly = 1
     |  
     |  ReadOther = 4
     |  
     |  ReadOwner = 16384
     |  
     |  ReadUser = 1024
     |  
     |  ReadWrite = 3
     |  
     |  RemoveError = 9
     |  
     |  RenameError = 10
     |  
     |  ResizeError = 12
     |  
     |  ResourceError = 4
     |  
     |  Text = 16
     |  
     |  TimeOutError = 7
     |  
     |  Truncate = 8
     |  
     |  Unbuffered = 32
     |  
     |  UnspecifiedError = 8
     |  
     |  WriteError = 2
     |  
     |  WriteGroup = 32
     |  
     |  WriteOnly = 2
     |  
     |  WriteOther = 2
     |  
     |  WriteOwner = 8192
     |  
     |  WriteUser = 512
     |  
     |  aboutToClose = <unbound qt signal aboutToClose of QTemporaryFile type>
     |  
     |  
     |  atEnd = <unbound qt slot py_q_atEnd of QTemporaryFile type>
     |      X.atEnd(a) -> bool
     |  
     |  autoRemove = <unbound qt slot autoRemove of QTemporaryFile type>
     |      X.autoRemove(a) -> bool
     |  
     |  blockSignals = <unbound qt slot blockSignals of QTemporaryFile type>
     |      X.blockSignals(a, b) -> bool
     |  
     |  bytesAvailable = <unbound qt slot py_q_bytesAvailable of QTemporaryFil...
     |      X.bytesAvailable(a) -> int
     |  
     |  bytesToWrite = <unbound qt slot py_q_bytesToWrite of QTemporaryFile ty...
     |      X.bytesToWrite(a) -> int
     |  
     |  bytesWritten = <unbound qt signal bytesWritten of QTemporaryFile type>
     |  
     |  
     |  canReadLine = <unbound qt slot py_q_canReadLine of QTemporaryFile type...
     |      X.canReadLine(a) -> bool
     |  
     |  channelBytesWritten = <unbound qt signal channelBytesWritten of QTempo...
     |  
     |  
     |  channelReadyRead = <unbound qt signal channelReadyRead of QTemporaryFi...
     |  
     |  
     |  childEvent = <unbound qt slot py_q_childEvent of QTemporaryFile type>
     |      X.childEvent(a, b)
     |  
     |  children = <unbound qt slot children of QTemporaryFile type>
     |      X.children(a) -> tuple
     |  
     |  className = <built-in method className of PythonQt.PythonQtClassWrappe...
     |      Return the classname of the object
     |  
     |  close = <unbound qt slot py_q_close of QTemporaryFile type>
     |      X.close(a)
     |  
     |  connect = <unbound qt slot connect of QTemporaryFile type>
     |      X.connect(a, b, c, d, e) -> bool
     |  
     |  copy = <unbound qt slot static_QFile_copy of QTemporaryFile type>
     |      X.copy(a, b) -> bool
     |  
     |  createLocalFile = <unbound qt slot static_QTemporaryFile_createLocalFi...
     |      X.createLocalFile(a) -> PythonQt.QtCore.QTemporaryFile
     |  
     |  createNativeFile = <unbound qt slot static_QTemporaryFile_createNative...
     |      X.createNativeFile(a) -> PythonQt.QtCore.QTemporaryFile
     |  
     |  customEvent = <unbound qt slot py_q_customEvent of QTemporaryFile type...
     |      X.customEvent(a, b)
     |  
     |  decodeName = <unbound qt slot static_QFile_decodeName of QTemporaryFil...
     |      X.decodeName(a) -> str
     |  
     |  delete = <built-in method delete of PythonQt.PythonQtClassWrapper obje...
     |      Deletes the given C++ object
     |  
     |  deleteLater = <unbound qt slot deleteLater of QTemporaryFile type>
     |      X.deleteLater()
     |  
     |  destroyed = <unbound qt signal destroyed of QTemporaryFile type>
     |  
     |  
     |  disconnect = <unbound qt slot disconnect of QTemporaryFile type>
     |      X.disconnect(a, b, c, d) -> bool
     |  
     |  dumpObjectInfo = <unbound qt slot dumpObjectInfo of QTemporaryFile typ...
     |      X.dumpObjectInfo(a)
     |  
     |  dumpObjectTree = <unbound qt slot dumpObjectTree of QTemporaryFile typ...
     |      X.dumpObjectTree(a)
     |  
     |  dynamicPropertyNames = <unbound qt slot dynamicPropertyNames of QTempo...
     |      X.dynamicPropertyNames(a)
     |  
     |  encodeName = <unbound qt slot static_QFile_encodeName of QTemporaryFil...
     |      X.encodeName(a) -> PythonQt.QtCore.QByteArray
     |  
     |  error = <unbound qt slot error of QTemporaryFile type>
     |      X.error(a)
     |  
     |  errorString = <unbound qt slot errorString of QTemporaryFile type>
     |      X.errorString(a) -> str
     |  
     |  event = <unbound qt slot py_q_event of QTemporaryFile type>
     |      X.event(a, b) -> bool
     |  
     |  eventFilter = <unbound qt slot py_q_eventFilter of QTemporaryFile type...
     |      X.eventFilter(a, b, c) -> bool
     |  
     |  exists = <unbound qt slot exists of QTemporaryFile type>
     |      X.exists(a) -> bool
     |  
     |  fileName = <unbound qt slot py_q_fileName of QTemporaryFile type>
     |      X.fileName(a) -> str
     |  
     |  fileTemplate = <unbound qt slot fileTemplate of QTemporaryFile type>
     |      X.fileTemplate(a) -> str
     |  
     |  findChild = <unbound qt slot findChild of QTemporaryFile type>
     |      X.findChild(a, b, c) -> PythonQt.private.QObject
     |  
     |  findChildren = <unbound qt slot findChildren of QTemporaryFile type>
     |      X.findChildren(a, b, c) -> tuple
     |  
     |  flush = <unbound qt slot flush of QTemporaryFile type>
     |      X.flush(a) -> bool
     |  
     |  getChar = <unbound qt slot getChar of QTemporaryFile type>
     |      X.getChar(a, b) -> bool
     |  
     |  handle = <unbound qt slot handle of QTemporaryFile type>
     |      X.handle(a) -> int
     |  
     |  help = <built-in method help of PythonQt.PythonQtClassWrapper object>
     |      Shows the help of available methods for this class
     |  
     |  inherits = <built-in method inherits of PythonQt.PythonQtClassWrapper ...
     |      Returns if the class inherits or is of given type name
     |  
     |  installEventFilter = <unbound qt slot installEventFilter of QTemporary...
     |      X.installEventFilter(a, b)
     |  
     |  isOpen = <unbound qt slot isOpen of QTemporaryFile type>
     |      X.isOpen(a) -> bool
     |  
     |  isReadable = <unbound qt slot isReadable of QTemporaryFile type>
     |      X.isReadable(a) -> bool
     |  
     |  isSequential = <unbound qt slot py_q_isSequential of QTemporaryFile ty...
     |      X.isSequential(a) -> bool
     |  
     |  isSignalConnected = <unbound qt slot isSignalConnected of QTemporaryFi...
     |      X.isSignalConnected(a, b) -> bool
     |  
     |  isTextModeEnabled = <unbound qt slot isTextModeEnabled of QTemporaryFi...
     |      X.isTextModeEnabled(a) -> bool
     |  
     |  isWidgetType = <unbound qt slot isWidgetType of QTemporaryFile type>
     |      X.isWidgetType(a) -> bool
     |  
     |  isWindowType = <unbound qt slot isWindowType of QTemporaryFile type>
     |      X.isWindowType(a) -> bool
     |  
     |  isWritable = <unbound qt slot isWritable of QTemporaryFile type>
     |      X.isWritable(a) -> bool
     |  
     |  killTimer = <unbound qt slot killTimer of QTemporaryFile type>
     |      X.killTimer(a, b)
     |  
     |  link = <unbound qt slot link of QTemporaryFile type>
     |      X.link(a, b) -> bool
     |  
     |  map = <unbound qt slot map of QTemporaryFile type>
     |      X.map(a, b, c, d) -> int
     |  
     |  metaObject = <unbound qt slot metaObject of QTemporaryFile type>
     |      X.metaObject(a) -> PythonQt.QtCore.QMetaObject
     |  
     |  moveToThread = <unbound qt slot moveToThread of QTemporaryFile type>
     |      X.moveToThread(a, b)
     |  
     |  objectName = None
     |  
     |  objectNameChanged = <unbound qt signal objectNameChanged of QTemporary...
     |  
     |  
     |  open = <unbound qt slot py_q_open of QTemporaryFile type>
     |      X.open(a, b) -> bool
     |  
     |  openMode = <unbound qt slot openMode of QTemporaryFile type>
     |      X.openMode(a)
     |  
     |  parent = <unbound qt slot parent of QTemporaryFile type>
     |      X.parent(a) -> PythonQt.private.QObject
     |  
     |  peek = <unbound qt slot peek of QTemporaryFile type>
     |      X.peek(a, b) -> PythonQt.QtCore.QByteArray
     |  
     |  permissions = <unbound qt slot py_q_permissions of QTemporaryFile type...
     |      X.permissions(a)
     |  
     |  pos = <unbound qt slot py_q_pos of QTemporaryFile type>
     |      X.pos(a) -> int
     |  
     |  property = <unbound qt slot property of QTemporaryFile type>
     |      X.property(a, b) -> object
     |  
     |  putChar = <unbound qt slot putChar of QTemporaryFile type>
     |      X.putChar(a, b) -> bool
     |  
     |  read = <unbound qt slot read of QTemporaryFile type>
     |      X.read(a, b) -> PythonQt.QtCore.QByteArray
     |  
     |  readAll = <unbound qt slot readAll of QTemporaryFile type>
     |      X.readAll(a) -> PythonQt.QtCore.QByteArray
     |  
     |  readChannelFinished = <unbound qt signal readChannelFinished of QTempo...
     |  
     |  
     |  readData = <unbound qt slot py_q_readData of QTemporaryFile type>
     |      X.readData(a, b, c) -> int
     |  
     |  readLine = <unbound qt slot readLine of QTemporaryFile type>
     |      X.readLine(a, b) -> PythonQt.QtCore.QByteArray
     |  
     |  readLineData = <unbound qt slot py_q_readLineData of QTemporaryFile ty...
     |      X.readLineData(a, b, c) -> int
     |  
     |  readyRead = <unbound qt signal readyRead of QTemporaryFile type>
     |  
     |  
     |  remove = <unbound qt slot remove of QTemporaryFile type>
     |      X.remove(a) -> bool
     |  
     |  removeEventFilter = <unbound qt slot removeEventFilter of QTemporaryFi...
     |      X.removeEventFilter(a, b)
     |  
     |  rename = <unbound qt slot rename of QTemporaryFile type>
     |      X.rename(a, b) -> bool
     |  
     |  reset = <unbound qt slot py_q_reset of QTemporaryFile type>
     |      X.reset(a) -> bool
     |  
     |  resize = <unbound qt slot py_q_resize of QTemporaryFile type>
     |      X.resize(a, b) -> bool
     |  
     |  seek = <unbound qt slot py_q_seek of QTemporaryFile type>
     |      X.seek(a, b) -> bool
     |  
     |  sender = <unbound qt slot sender of QTemporaryFile type>
     |      X.sender(a) -> PythonQt.private.QObject
     |  
     |  senderSignalIndex = <unbound qt slot senderSignalIndex of QTemporaryFi...
     |      X.senderSignalIndex(a) -> int
     |  
     |  setAutoRemove = <unbound qt slot setAutoRemove of QTemporaryFile type>
     |      X.setAutoRemove(a, b)
     |  
     |  setErrorString = <unbound qt slot setErrorString of QTemporaryFile typ...
     |      X.setErrorString(a, b)
     |  
     |  setFileName = <unbound qt slot setFileName of QTemporaryFile type>
     |      X.setFileName(a, b)
     |  
     |  setFileTemplate = <unbound qt slot setFileTemplate of QTemporaryFile t...
     |      X.setFileTemplate(a, b)
     |  
     |  setObjectName = <unbound qt slot setObjectName of QTemporaryFile type>
     |      X.setObjectName(a, b)
     |  
     |  setOpenMode = <unbound qt slot setOpenMode of QTemporaryFile type>
     |      X.setOpenMode(a, b)
     |  
     |  setParent = <unbound qt slot setParent of QTemporaryFile type>
     |      X.setParent(a, b)
     |  
     |  setPermissions = <unbound qt slot py_q_setPermissions of QTemporaryFil...
     |      X.setPermissions(a, b) -> bool
     |  
     |  setProperty = <unbound qt slot setProperty of QTemporaryFile type>
     |      X.setProperty(a, b, c) -> bool
     |  
     |  setTextModeEnabled = <unbound qt slot setTextModeEnabled of QTemporary...
     |      X.setTextModeEnabled(a, b)
     |  
     |  signalsBlocked = <unbound qt slot signalsBlocked of QTemporaryFile typ...
     |      X.signalsBlocked(a) -> bool
     |  
     |  size = <unbound qt slot py_q_size of QTemporaryFile type>
     |      X.size(a) -> int
     |  
     |  startTimer = <unbound qt slot startTimer of QTemporaryFile type>
     |      X.startTimer(a, b, c) -> int
     |  
     |  symLinkTarget = <unbound qt slot symLinkTarget of QTemporaryFile type>
     |      X.symLinkTarget(a) -> str
     |  
     |  thread = <unbound qt slot thread of QTemporaryFile type>
     |      X.thread(a)
     |  
     |  timerEvent = <unbound qt slot py_q_timerEvent of QTemporaryFile type>
     |      X.timerEvent(a, b)
     |  
     |  tr = <unbound qt slot tr of QTemporaryFile type>
     |      X.tr(a, b, c, d) -> str
     |  
     |  ungetChar = <unbound qt slot ungetChar of QTemporaryFile type>
     |      X.ungetChar(a, b)
     |  
     |  unmap = <unbound qt slot unmap of QTemporaryFile type>
     |      X.unmap(a, b) -> bool
     |  
     |  unsetError = <unbound qt slot unsetError of QTemporaryFile type>
     |      X.unsetError(a)
     |  
     |  waitForBytesWritten = <unbound qt slot py_q_waitForBytesWritten of QTe...
     |      X.waitForBytesWritten(a, b) -> bool
     |  
     |  waitForReadyRead = <unbound qt slot py_q_waitForReadyRead of QTemporar...
     |      X.waitForReadyRead(a, b) -> bool
     |  
     |  write = <unbound qt slot write of QTemporaryFile type>
     |      X.write(a, b) -> int
     |  
     |  writeData = <unbound qt slot py_q_writeData of QTemporaryFile type>
     |      X.writeData(a, b, c) -> int
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __delattr__(...)
     |      x.__delattr__('name') <==> del x.name
     |  
     |  __eq__(...)
     |      x.__eq__(y) <==> x==y
     |  
     |  __ge__(...)
     |      x.__ge__(y) <==> x>=y
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __gt__(...)
     |      x.__gt__(y) <==> x>y
     |  
     |  __hash__(...)
     |      x.__hash__() <==> hash(x)
     |  
     |  __le__(...)
     |      x.__le__(y) <==> x<=y
     |  
     |  __lt__(...)
     |      x.__lt__(y) <==> x<y
     |  
     |  __ne__(...)
     |      x.__ne__(y) <==> x!=y
     |  
     |  __nonzero__(...)
     |      x.__nonzero__() <==> x != 0
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __setattr__(...)
     |      x.__setattr__('name', value) <==> x.name = value
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __new__ = <built-in method __new__ of PythonQt.PythonQtClassWrapper ob...
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
    
    class QTextBoundaryFinder(PythonQt.PythonQtInstanceWrapper)
     |  Method resolution order:
     |      QTextBoundaryFinder
     |      PythonQt.PythonQtInstanceWrapper
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  __init__(...)
     |      x.__init__(...) initializes x; see help(type(x)) for signature
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  BoundaryReason = <class 'PythonQt.QtCore.BoundaryReason'>
     |  
     |  
     |  BoundaryReasons = <class 'PythonQt.QtCore.BoundaryReasons'>
     |  
     |  
     |  BoundaryType = <class 'PythonQt.QtCore.BoundaryType'>
     |  
     |  
     |  BreakOpportunity = 31
     |  
     |  EndOfItem = 64
     |  
     |  Grapheme = 0
     |  
     |  Line = 3
     |  
     |  MandatoryBreak = 128
     |  
     |  NotAtBoundary = 0
     |  
     |  Sentence = 2
     |  
     |  SoftHyphen = 256
     |  
     |  StartOfItem = 32
     |  
     |  Word = 1
     |  
     |  boundaryReasons = <unbound qt slot boundaryReasons of QTextBoundaryFin...
     |      X.boundaryReasons(a)
     |  
     |  className = <built-in method className of PythonQt.PythonQtClassWrappe...
     |      Return the classname of the object
     |  
     |  delete = <built-in method delete of PythonQt.PythonQtClassWrapper obje...
     |      Deletes the given C++ object
     |  
     |  help = <built-in method help of PythonQt.PythonQtClassWrapper object>
     |      Shows the help of available methods for this class
     |  
     |  inherits = <built-in method inherits of PythonQt.PythonQtClassWrapper ...
     |      Returns if the class inherits or is of given type name
     |  
     |  isAtBoundary = <unbound qt slot isAtBoundary of QTextBoundaryFinder ty...
     |      X.isAtBoundary(a) -> bool
     |  
     |  isValid = <unbound qt slot isValid of QTextBoundaryFinder type>
     |      X.isValid(a) -> bool
     |  
     |  position = <unbound qt slot position of QTextBoundaryFinder type>
     |      X.position(a) -> int
     |  
     |  setPosition = <unbound qt slot setPosition of QTextBoundaryFinder type...
     |      X.setPosition(a, b)
     |  
     |  string = <unbound qt slot string of QTextBoundaryFinder type>
     |      X.string(a) -> str
     |  
     |  toEnd = <unbound qt slot toEnd of QTextBoundaryFinder type>
     |      X.toEnd(a)
     |  
     |  toNextBoundary = <unbound qt slot toNextBoundary of QTextBoundaryFinde...
     |      X.toNextBoundary(a) -> int
     |  
     |  toPreviousBoundary = <unbound qt slot toPreviousBoundary of QTextBound...
     |      X.toPreviousBoundary(a) -> int
     |  
     |  toStart = <unbound qt slot toStart of QTextBoundaryFinder type>
     |      X.toStart(a)
     |  
     |  type = <unbound qt slot type of QTextBoundaryFinder type>
     |      X.type(a)
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __delattr__(...)
     |      x.__delattr__('name') <==> del x.name
     |  
     |  __eq__(...)
     |      x.__eq__(y) <==> x==y
     |  
     |  __ge__(...)
     |      x.__ge__(y) <==> x>=y
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __gt__(...)
     |      x.__gt__(y) <==> x>y
     |  
     |  __hash__(...)
     |      x.__hash__() <==> hash(x)
     |  
     |  __le__(...)
     |      x.__le__(y) <==> x<=y
     |  
     |  __lt__(...)
     |      x.__lt__(y) <==> x<y
     |  
     |  __ne__(...)
     |      x.__ne__(y) <==> x!=y
     |  
     |  __nonzero__(...)
     |      x.__nonzero__() <==> x != 0
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __setattr__(...)
     |      x.__setattr__('name', value) <==> x.name = value
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __new__ = <built-in method __new__ of PythonQt.PythonQtClassWrapper ob...
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
    
    class QTextCodec(PythonQt.PythonQtInstanceWrapper)
     |  Method resolution order:
     |      QTextCodec
     |      PythonQt.PythonQtInstanceWrapper
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  __init__(...)
     |      x.__init__(...) initializes x; see help(type(x)) for signature
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  ConversionFlag = <class 'PythonQt.QtCore.ConversionFlag'>
     |  
     |  
     |  ConversionFlags = <class 'PythonQt.QtCore.ConversionFlags'>
     |  
     |  
     |  ConvertInvalidToNull = -2147483648
     |  
     |  DefaultConversion = 0
     |  
     |  FreeFunction = 2
     |  
     |  IgnoreHeader = 1
     |  
     |  aliases = <unbound qt slot py_q_aliases of QTextCodec type>
     |      X.aliases(a)
     |  
     |  availableCodecs = <unbound qt slot static_QTextCodec_availableCodecs o...
     |      X.availableCodecs()
     |  
     |  availableMibs = <unbound qt slot static_QTextCodec_availableMibs of QT...
     |      X.availableMibs() -> tuple
     |  
     |  canEncode = <unbound qt slot canEncode of QTextCodec type>
     |      X.canEncode(a, b) -> bool
     |  
     |  className = <built-in method className of PythonQt.PythonQtClassWrappe...
     |      Return the classname of the object
     |  
     |  codecForHtml = <unbound qt slot static_QTextCodec_codecForHtml of QTex...
     |      X.codecForHtml(a, b) -> PythonQt.QtCore.QTextCodec
     |  
     |  codecForLocale = <unbound qt slot static_QTextCodec_codecForLocale of ...
     |      X.codecForLocale() -> PythonQt.QtCore.QTextCodec
     |  
     |  codecForMib = <unbound qt slot static_QTextCodec_codecForMib of QTextC...
     |      X.codecForMib(a) -> PythonQt.QtCore.QTextCodec
     |  
     |  codecForName = <unbound qt slot static_QTextCodec_codecForName of QTex...
     |      X.codecForName(a) -> PythonQt.QtCore.QTextCodec
     |  
     |  codecForUtfText = <unbound qt slot static_QTextCodec_codecForUtfText o...
     |      X.codecForUtfText(a, b) -> PythonQt.QtCore.QTextCodec
     |  
     |  convertFromUnicode = <unbound qt slot py_q_convertFromUnicode of QText...
     |      X.convertFromUnicode(a, b, c, d) -> PythonQt.QtCore.QByteArray
     |  
     |  convertToUnicode = <unbound qt slot py_q_convertToUnicode of QTextCode...
     |      X.convertToUnicode(a, b, c, d) -> str
     |  
     |  delete = <built-in method delete of PythonQt.PythonQtClassWrapper obje...
     |      Deletes the given C++ object
     |  
     |  fromUnicode = <unbound qt slot fromUnicode of QTextCodec type>
     |      X.fromUnicode(a, b) -> PythonQt.QtCore.QByteArray
     |  
     |  help = <built-in method help of PythonQt.PythonQtClassWrapper object>
     |      Shows the help of available methods for this class
     |  
     |  inherits = <built-in method inherits of PythonQt.PythonQtClassWrapper ...
     |      Returns if the class inherits or is of given type name
     |  
     |  makeDecoder = <unbound qt slot makeDecoder of QTextCodec type>
     |      X.makeDecoder(a, b) -> PythonQt.QtCore.QTextDecoder
     |  
     |  makeEncoder = <unbound qt slot makeEncoder of QTextCodec type>
     |      X.makeEncoder(a, b) -> PythonQt.QtCore.QTextEncoder
     |  
     |  mibEnum = <unbound qt slot py_q_mibEnum of QTextCodec type>
     |      X.mibEnum(a) -> int
     |  
     |  name = <unbound qt slot py_q_name of QTextCodec type>
     |      X.name(a) -> PythonQt.QtCore.QByteArray
     |  
     |  setCodecForLocale = <unbound qt slot static_QTextCodec_setCodecForLoca...
     |      X.setCodecForLocale(a)
     |  
     |  toUnicode = <unbound qt slot toUnicode of QTextCodec type>
     |      X.toUnicode(a, b) -> str
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __delattr__(...)
     |      x.__delattr__('name') <==> del x.name
     |  
     |  __eq__(...)
     |      x.__eq__(y) <==> x==y
     |  
     |  __ge__(...)
     |      x.__ge__(y) <==> x>=y
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __gt__(...)
     |      x.__gt__(y) <==> x>y
     |  
     |  __hash__(...)
     |      x.__hash__() <==> hash(x)
     |  
     |  __le__(...)
     |      x.__le__(y) <==> x<=y
     |  
     |  __lt__(...)
     |      x.__lt__(y) <==> x<y
     |  
     |  __ne__(...)
     |      x.__ne__(y) <==> x!=y
     |  
     |  __nonzero__(...)
     |      x.__nonzero__() <==> x != 0
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __setattr__(...)
     |      x.__setattr__('name', value) <==> x.name = value
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __new__ = <built-in method __new__ of PythonQt.PythonQtClassWrapper ob...
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
    
    class QTextDecoder(PythonQt.PythonQtInstanceWrapper)
     |  Method resolution order:
     |      QTextDecoder
     |      PythonQt.PythonQtInstanceWrapper
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  __init__(...)
     |      x.__init__(...) initializes x; see help(type(x)) for signature
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  className = <built-in method className of PythonQt.PythonQtClassWrappe...
     |      Return the classname of the object
     |  
     |  delete = <built-in method delete of PythonQt.PythonQtClassWrapper obje...
     |      Deletes the given C++ object
     |  
     |  hasFailure = <unbound qt slot hasFailure of QTextDecoder type>
     |      X.hasFailure(a) -> bool
     |  
     |  help = <built-in method help of PythonQt.PythonQtClassWrapper object>
     |      Shows the help of available methods for this class
     |  
     |  inherits = <built-in method inherits of PythonQt.PythonQtClassWrapper ...
     |      Returns if the class inherits or is of given type name
     |  
     |  toUnicode = <unbound qt slot toUnicode of QTextDecoder type>
     |      X.toUnicode(a, b) -> str
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __delattr__(...)
     |      x.__delattr__('name') <==> del x.name
     |  
     |  __eq__(...)
     |      x.__eq__(y) <==> x==y
     |  
     |  __ge__(...)
     |      x.__ge__(y) <==> x>=y
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __gt__(...)
     |      x.__gt__(y) <==> x>y
     |  
     |  __hash__(...)
     |      x.__hash__() <==> hash(x)
     |  
     |  __le__(...)
     |      x.__le__(y) <==> x<=y
     |  
     |  __lt__(...)
     |      x.__lt__(y) <==> x<y
     |  
     |  __ne__(...)
     |      x.__ne__(y) <==> x!=y
     |  
     |  __nonzero__(...)
     |      x.__nonzero__() <==> x != 0
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __setattr__(...)
     |      x.__setattr__('name', value) <==> x.name = value
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __new__ = <built-in method __new__ of PythonQt.PythonQtClassWrapper ob...
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
    
    class QTextEncoder(PythonQt.PythonQtInstanceWrapper)
     |  Method resolution order:
     |      QTextEncoder
     |      PythonQt.PythonQtInstanceWrapper
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  __init__(...)
     |      x.__init__(...) initializes x; see help(type(x)) for signature
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  className = <built-in method className of PythonQt.PythonQtClassWrappe...
     |      Return the classname of the object
     |  
     |  delete = <built-in method delete of PythonQt.PythonQtClassWrapper obje...
     |      Deletes the given C++ object
     |  
     |  fromUnicode = <unbound qt slot fromUnicode of QTextEncoder type>
     |      X.fromUnicode(a, b) -> PythonQt.QtCore.QByteArray
     |  
     |  hasFailure = <unbound qt slot hasFailure of QTextEncoder type>
     |      X.hasFailure(a) -> bool
     |  
     |  help = <built-in method help of PythonQt.PythonQtClassWrapper object>
     |      Shows the help of available methods for this class
     |  
     |  inherits = <built-in method inherits of PythonQt.PythonQtClassWrapper ...
     |      Returns if the class inherits or is of given type name
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __delattr__(...)
     |      x.__delattr__('name') <==> del x.name
     |  
     |  __eq__(...)
     |      x.__eq__(y) <==> x==y
     |  
     |  __ge__(...)
     |      x.__ge__(y) <==> x>=y
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __gt__(...)
     |      x.__gt__(y) <==> x>y
     |  
     |  __hash__(...)
     |      x.__hash__() <==> hash(x)
     |  
     |  __le__(...)
     |      x.__le__(y) <==> x<=y
     |  
     |  __lt__(...)
     |      x.__lt__(y) <==> x<y
     |  
     |  __ne__(...)
     |      x.__ne__(y) <==> x!=y
     |  
     |  __nonzero__(...)
     |      x.__nonzero__() <==> x != 0
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __setattr__(...)
     |      x.__setattr__('name', value) <==> x.name = value
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __new__ = <built-in method __new__ of PythonQt.PythonQtClassWrapper ob...
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
    
    class QTextStream(PythonQt.PythonQtInstanceWrapper)
     |  Method resolution order:
     |      QTextStream
     |      PythonQt.PythonQtInstanceWrapper
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  __init__(...)
     |      x.__init__(...) initializes x; see help(type(x)) for signature
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  AlignAccountingStyle = 3
     |  
     |  AlignCenter = 2
     |  
     |  AlignLeft = 0
     |  
     |  AlignRight = 1
     |  
     |  FieldAlignment = <class 'PythonQt.QtCore.FieldAlignment'>
     |  
     |  
     |  FixedNotation = 1
     |  
     |  ForcePoint = 2
     |  
     |  ForceSign = 4
     |  
     |  NumberFlag = <class 'PythonQt.QtCore.NumberFlag'>
     |  
     |  
     |  NumberFlags = <class 'PythonQt.QtCore.NumberFlags'>
     |  
     |  
     |  Ok = 0
     |  
     |  ReadCorruptData = 2
     |  
     |  ReadPastEnd = 1
     |  
     |  RealNumberNotation = <class 'PythonQt.QtCore.RealNumberNotation'>
     |  
     |  
     |  ScientificNotation = 2
     |  
     |  ShowBase = 1
     |  
     |  SmartNotation = 0
     |  
     |  Status = <class 'PythonQt.QtCore.Status'>
     |  
     |  
     |  UppercaseBase = 8
     |  
     |  UppercaseDigits = 16
     |  
     |  WriteFailed = 3
     |  
     |  __lshift__ = <unbound qt slot __lshift__ of QTextStream type>
     |      X.__lshift__(a, b) -> PythonQt.QtCore.QTextStream
     |  
     |  atEnd = <unbound qt slot atEnd of QTextStream type>
     |      X.atEnd(a) -> bool
     |  
     |  autoDetectUnicode = <unbound qt slot autoDetectUnicode of QTextStream ...
     |      X.autoDetectUnicode(a) -> bool
     |  
     |  className = <built-in method className of PythonQt.PythonQtClassWrappe...
     |      Return the classname of the object
     |  
     |  codec = <unbound qt slot codec of QTextStream type>
     |      X.codec(a) -> PythonQt.QtCore.QTextCodec
     |  
     |  delete = <built-in method delete of PythonQt.PythonQtClassWrapper obje...
     |      Deletes the given C++ object
     |  
     |  device = <unbound qt slot device of QTextStream type>
     |      X.device(a) -> PythonQt.QtCore.QIODevice
     |  
     |  fieldAlignment = <unbound qt slot fieldAlignment of QTextStream type>
     |      X.fieldAlignment(a)
     |  
     |  fieldWidth = <unbound qt slot fieldWidth of QTextStream type>
     |      X.fieldWidth(a) -> int
     |  
     |  flush = <unbound qt slot flush of QTextStream type>
     |      X.flush(a)
     |  
     |  generateByteOrderMark = <unbound qt slot generateByteOrderMark of QTex...
     |      X.generateByteOrderMark(a) -> bool
     |  
     |  help = <built-in method help of PythonQt.PythonQtClassWrapper object>
     |      Shows the help of available methods for this class
     |  
     |  inherits = <built-in method inherits of PythonQt.PythonQtClassWrapper ...
     |      Returns if the class inherits or is of given type name
     |  
     |  integerBase = <unbound qt slot integerBase of QTextStream type>
     |      X.integerBase(a) -> int
     |  
     |  locale = <unbound qt slot locale of QTextStream type>
     |      X.locale(a) -> PythonQt.QtCore.QLocale
     |  
     |  numberFlags = <unbound qt slot numberFlags of QTextStream type>
     |      X.numberFlags(a)
     |  
     |  padChar = <unbound qt slot padChar of QTextStream type>
     |      X.padChar(a)
     |  
     |  pos = <unbound qt slot pos of QTextStream type>
     |      X.pos(a) -> int
     |  
     |  read = <unbound qt slot read of QTextStream type>
     |      X.read(a, b) -> str
     |  
     |  readAll = <unbound qt slot readAll of QTextStream type>
     |      X.readAll(a) -> str
     |  
     |  readByte = <unbound qt slot readByte of QTextStream type>
     |      X.readByte(a, b) -> PythonQt.QtCore.QTextStream
     |  
     |  readDouble = <unbound qt slot readDouble of QTextStream type>
     |      X.readDouble(a, b) -> PythonQt.QtCore.QTextStream
     |  
     |  readFloat = <unbound qt slot readFloat of QTextStream type>
     |      X.readFloat(a, b) -> PythonQt.QtCore.QTextStream
     |  
     |  readInt = <unbound qt slot readInt of QTextStream type>
     |      X.readInt(a, b) -> PythonQt.QtCore.QTextStream
     |  
     |  readLine = <unbound qt slot readLine of QTextStream type>
     |      X.readLine(a, b) -> str
     |  
     |  readLineInto = <unbound qt slot readLineInto of QTextStream type>
     |      X.readLineInto(a, b, c) -> bool
     |  
     |  readLongLong = <unbound qt slot readLongLong of QTextStream type>
     |      X.readLongLong(a, b) -> PythonQt.QtCore.QTextStream
     |  
     |  readShort = <unbound qt slot readShort of QTextStream type>
     |      X.readShort(a, b) -> PythonQt.QtCore.QTextStream
     |  
     |  realNumberNotation = <unbound qt slot realNumberNotation of QTextStrea...
     |      X.realNumberNotation(a)
     |  
     |  realNumberPrecision = <unbound qt slot realNumberPrecision of QTextStr...
     |      X.realNumberPrecision(a) -> int
     |  
     |  reset = <unbound qt slot reset of QTextStream type>
     |      X.reset(a)
     |  
     |  resetStatus = <unbound qt slot resetStatus of QTextStream type>
     |      X.resetStatus(a)
     |  
     |  seek = <unbound qt slot seek of QTextStream type>
     |      X.seek(a, b) -> bool
     |  
     |  setAutoDetectUnicode = <unbound qt slot setAutoDetectUnicode of QTextS...
     |      X.setAutoDetectUnicode(a, b)
     |  
     |  setCodec = <unbound qt slot setCodec of QTextStream type>
     |      X.setCodec(a, b)
     |  
     |  setDevice = <unbound qt slot setDevice of QTextStream type>
     |      X.setDevice(a, b)
     |  
     |  setFieldAlignment = <unbound qt slot setFieldAlignment of QTextStream ...
     |      X.setFieldAlignment(a, b)
     |  
     |  setFieldWidth = <unbound qt slot setFieldWidth of QTextStream type>
     |      X.setFieldWidth(a, b)
     |  
     |  setGenerateByteOrderMark = <unbound qt slot setGenerateByteOrderMark o...
     |      X.setGenerateByteOrderMark(a, b)
     |  
     |  setIntegerBase = <unbound qt slot setIntegerBase of QTextStream type>
     |      X.setIntegerBase(a, b)
     |  
     |  setLocale = <unbound qt slot setLocale of QTextStream type>
     |      X.setLocale(a, b)
     |  
     |  setNumberFlags = <unbound qt slot setNumberFlags of QTextStream type>
     |      X.setNumberFlags(a, b)
     |  
     |  setPadChar = <unbound qt slot setPadChar of QTextStream type>
     |      X.setPadChar(a, b)
     |  
     |  setRealNumberNotation = <unbound qt slot setRealNumberNotation of QTex...
     |      X.setRealNumberNotation(a, b)
     |  
     |  setRealNumberPrecision = <unbound qt slot setRealNumberPrecision of QT...
     |      X.setRealNumberPrecision(a, b)
     |  
     |  setStatus = <unbound qt slot setStatus of QTextStream type>
     |      X.setStatus(a, b)
     |  
     |  skipWhiteSpace = <unbound qt slot skipWhiteSpace of QTextStream type>
     |      X.skipWhiteSpace(a)
     |  
     |  status = <unbound qt slot status of QTextStream type>
     |      X.status(a)
     |  
     |  writeByte = <unbound qt slot writeByte of QTextStream type>
     |      X.writeByte(a, b) -> PythonQt.QtCore.QTextStream
     |  
     |  writeDouble = <unbound qt slot writeDouble of QTextStream type>
     |      X.writeDouble(a, b) -> PythonQt.QtCore.QTextStream
     |  
     |  writeFloat = <unbound qt slot writeFloat of QTextStream type>
     |      X.writeFloat(a, b) -> PythonQt.QtCore.QTextStream
     |  
     |  writeInt = <unbound qt slot writeInt of QTextStream type>
     |      X.writeInt(a, b) -> PythonQt.QtCore.QTextStream
     |  
     |  writeLongLong = <unbound qt slot writeLongLong of QTextStream type>
     |      X.writeLongLong(a, b) -> PythonQt.QtCore.QTextStream
     |  
     |  writeShort = <unbound qt slot writeShort of QTextStream type>
     |      X.writeShort(a, b) -> PythonQt.QtCore.QTextStream
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __delattr__(...)
     |      x.__delattr__('name') <==> del x.name
     |  
     |  __eq__(...)
     |      x.__eq__(y) <==> x==y
     |  
     |  __ge__(...)
     |      x.__ge__(y) <==> x>=y
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __gt__(...)
     |      x.__gt__(y) <==> x>y
     |  
     |  __hash__(...)
     |      x.__hash__() <==> hash(x)
     |  
     |  __le__(...)
     |      x.__le__(y) <==> x<=y
     |  
     |  __lt__(...)
     |      x.__lt__(y) <==> x<y
     |  
     |  __ne__(...)
     |      x.__ne__(y) <==> x!=y
     |  
     |  __nonzero__(...)
     |      x.__nonzero__() <==> x != 0
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __setattr__(...)
     |      x.__setattr__('name', value) <==> x.name = value
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __new__ = <built-in method __new__ of PythonQt.PythonQtClassWrapper ob...
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
    
    class QThreadPool(PythonQt.PythonQtInstanceWrapper)
     |  Method resolution order:
     |      QThreadPool
     |      PythonQt.PythonQtInstanceWrapper
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  __init__(...)
     |      x.__init__(...) initializes x; see help(type(x)) for signature
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  activeThreadCount = None
     |  
     |  blockSignals = <unbound qt slot blockSignals of QThreadPool type>
     |      X.blockSignals(a, b) -> bool
     |  
     |  cancel = <unbound qt slot cancel of QThreadPool type>
     |      X.cancel(a, b)
     |  
     |  childEvent = <unbound qt slot py_q_childEvent of QThreadPool type>
     |      X.childEvent(a, b)
     |  
     |  children = <unbound qt slot children of QThreadPool type>
     |      X.children(a) -> tuple
     |  
     |  className = <built-in method className of PythonQt.PythonQtClassWrappe...
     |      Return the classname of the object
     |  
     |  clear = <unbound qt slot clear of QThreadPool type>
     |      X.clear(a)
     |  
     |  connect = <unbound qt slot connect of QThreadPool type>
     |      X.connect(a, b, c, d, e) -> bool
     |  
     |  customEvent = <unbound qt slot py_q_customEvent of QThreadPool type>
     |      X.customEvent(a, b)
     |  
     |  delete = <built-in method delete of PythonQt.PythonQtClassWrapper obje...
     |      Deletes the given C++ object
     |  
     |  deleteLater = <unbound qt slot deleteLater of QThreadPool type>
     |      X.deleteLater()
     |  
     |  destroyed = <unbound qt signal destroyed of QThreadPool type>
     |  
     |  
     |  disconnect = <unbound qt slot disconnect of QThreadPool type>
     |      X.disconnect(a, b, c, d) -> bool
     |  
     |  dumpObjectInfo = <unbound qt slot dumpObjectInfo of QThreadPool type>
     |      X.dumpObjectInfo(a)
     |  
     |  dumpObjectTree = <unbound qt slot dumpObjectTree of QThreadPool type>
     |      X.dumpObjectTree(a)
     |  
     |  dynamicPropertyNames = <unbound qt slot dynamicPropertyNames of QThrea...
     |      X.dynamicPropertyNames(a)
     |  
     |  event = <unbound qt slot py_q_event of QThreadPool type>
     |      X.event(a, b) -> bool
     |  
     |  eventFilter = <unbound qt slot py_q_eventFilter of QThreadPool type>
     |      X.eventFilter(a, b, c) -> bool
     |  
     |  expiryTimeout = None
     |  
     |  findChild = <unbound qt slot findChild of QThreadPool type>
     |      X.findChild(a, b, c) -> PythonQt.private.QObject
     |  
     |  findChildren = <unbound qt slot findChildren of QThreadPool type>
     |      X.findChildren(a, b, c) -> tuple
     |  
     |  globalInstance = <unbound qt slot static_QThreadPool_globalInstance of...
     |      X.globalInstance() -> PythonQt.QtCore.QThreadPool
     |  
     |  help = <built-in method help of PythonQt.PythonQtClassWrapper object>
     |      Shows the help of available methods for this class
     |  
     |  inherits = <built-in method inherits of PythonQt.PythonQtClassWrapper ...
     |      Returns if the class inherits or is of given type name
     |  
     |  installEventFilter = <unbound qt slot installEventFilter of QThreadPoo...
     |      X.installEventFilter(a, b)
     |  
     |  isSignalConnected = <unbound qt slot isSignalConnected of QThreadPool ...
     |      X.isSignalConnected(a, b) -> bool
     |  
     |  isWidgetType = <unbound qt slot isWidgetType of QThreadPool type>
     |      X.isWidgetType(a) -> bool
     |  
     |  isWindowType = <unbound qt slot isWindowType of QThreadPool type>
     |      X.isWindowType(a) -> bool
     |  
     |  killTimer = <unbound qt slot killTimer of QThreadPool type>
     |      X.killTimer(a, b)
     |  
     |  maxThreadCount = None
     |  
     |  metaObject = <unbound qt slot metaObject of QThreadPool type>
     |      X.metaObject(a) -> PythonQt.QtCore.QMetaObject
     |  
     |  moveToThread = <unbound qt slot moveToThread of QThreadPool type>
     |      X.moveToThread(a, b)
     |  
     |  objectName = None
     |  
     |  objectNameChanged = <unbound qt signal objectNameChanged of QThreadPoo...
     |  
     |  
     |  parent = <unbound qt slot parent of QThreadPool type>
     |      X.parent(a) -> PythonQt.private.QObject
     |  
     |  property = <unbound qt slot property of QThreadPool type>
     |      X.property(a, b) -> object
     |  
     |  releaseThread = <unbound qt slot releaseThread of QThreadPool type>
     |      X.releaseThread(a)
     |  
     |  removeEventFilter = <unbound qt slot removeEventFilter of QThreadPool ...
     |      X.removeEventFilter(a, b)
     |  
     |  reserveThread = <unbound qt slot reserveThread of QThreadPool type>
     |      X.reserveThread(a)
     |  
     |  sender = <unbound qt slot sender of QThreadPool type>
     |      X.sender(a) -> PythonQt.private.QObject
     |  
     |  senderSignalIndex = <unbound qt slot senderSignalIndex of QThreadPool ...
     |      X.senderSignalIndex(a) -> int
     |  
     |  setExpiryTimeout = <unbound qt slot setExpiryTimeout of QThreadPool ty...
     |      X.setExpiryTimeout(a, b)
     |  
     |  setMaxThreadCount = <unbound qt slot setMaxThreadCount of QThreadPool ...
     |      X.setMaxThreadCount(a, b)
     |  
     |  setObjectName = <unbound qt slot setObjectName of QThreadPool type>
     |      X.setObjectName(a, b)
     |  
     |  setParent = <unbound qt slot setParent of QThreadPool type>
     |      X.setParent(a, b)
     |  
     |  setProperty = <unbound qt slot setProperty of QThreadPool type>
     |      X.setProperty(a, b, c) -> bool
     |  
     |  signalsBlocked = <unbound qt slot signalsBlocked of QThreadPool type>
     |      X.signalsBlocked(a) -> bool
     |  
     |  start = <unbound qt slot start of QThreadPool type>
     |      X.start(a, b, c)
     |  
     |  startTimer = <unbound qt slot startTimer of QThreadPool type>
     |      X.startTimer(a, b, c) -> int
     |  
     |  thread = <unbound qt slot thread of QThreadPool type>
     |      X.thread(a)
     |  
     |  timerEvent = <unbound qt slot py_q_timerEvent of QThreadPool type>
     |      X.timerEvent(a, b)
     |  
     |  tr = <unbound qt slot tr of QThreadPool type>
     |      X.tr(a, b, c, d) -> str
     |  
     |  tryStart = <unbound qt slot tryStart of QThreadPool type>
     |      X.tryStart(a, b) -> bool
     |  
     |  waitForDone = <unbound qt slot waitForDone of QThreadPool type>
     |      X.waitForDone(a, b) -> bool
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __delattr__(...)
     |      x.__delattr__('name') <==> del x.name
     |  
     |  __eq__(...)
     |      x.__eq__(y) <==> x==y
     |  
     |  __ge__(...)
     |      x.__ge__(y) <==> x>=y
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __gt__(...)
     |      x.__gt__(y) <==> x>y
     |  
     |  __hash__(...)
     |      x.__hash__() <==> hash(x)
     |  
     |  __le__(...)
     |      x.__le__(y) <==> x<=y
     |  
     |  __lt__(...)
     |      x.__lt__(y) <==> x<y
     |  
     |  __ne__(...)
     |      x.__ne__(y) <==> x!=y
     |  
     |  __nonzero__(...)
     |      x.__nonzero__() <==> x != 0
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __setattr__(...)
     |      x.__setattr__('name', value) <==> x.name = value
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __new__ = <built-in method __new__ of PythonQt.PythonQtClassWrapper ob...
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
    
    class QTime(PythonQt.PythonQtInstanceWrapper)
     |  Method resolution order:
     |      QTime
     |      PythonQt.PythonQtInstanceWrapper
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  __eq__(...)
     |      x.__eq__(y) <==> x==y
     |  
     |  __ge__(...)
     |      x.__ge__(y) <==> x>=y
     |  
     |  __gt__(...)
     |      x.__gt__(y) <==> x>y
     |  
     |  __init__(...)
     |      x.__init__(...) initializes x; see help(type(x)) for signature
     |  
     |  __le__(...)
     |      x.__le__(y) <==> x<=y
     |  
     |  __lt__(...)
     |      x.__lt__(y) <==> x<y
     |  
     |  __ne__(...)
     |      x.__ne__(y) <==> x!=y
     |  
     |  __nonzero__(...)
     |      x.__nonzero__() <==> x != 0
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  addMSecs = <unbound qt slot addMSecs of QTime type>
     |      X.addMSecs(a, b) -> PythonQt.QtCore.QTime
     |  
     |  addSecs = <unbound qt slot addSecs of QTime type>
     |      X.addSecs(a, b) -> PythonQt.QtCore.QTime
     |  
     |  className = <built-in method className of PythonQt.PythonQtClassWrappe...
     |      Return the classname of the object
     |  
     |  currentTime = <unbound qt slot static_QTime_currentTime of QTime type>
     |      X.currentTime() -> PythonQt.QtCore.QTime
     |  
     |  delete = <built-in method delete of PythonQt.PythonQtClassWrapper obje...
     |      Deletes the given C++ object
     |  
     |  elapsed = <unbound qt slot elapsed of QTime type>
     |      X.elapsed(a) -> int
     |  
     |  fromMSecsSinceStartOfDay = <unbound qt slot static_QTime_fromMSecsSinc...
     |      X.fromMSecsSinceStartOfDay(a) -> PythonQt.QtCore.QTime
     |  
     |  fromString = <unbound qt slot static_QTime_fromString of QTime type>
     |      X.fromString(a, b) -> PythonQt.QtCore.QTime
     |  
     |  help = <built-in method help of PythonQt.PythonQtClassWrapper object>
     |      Shows the help of available methods for this class
     |  
     |  hour = <unbound qt slot hour of QTime type>
     |      X.hour(a) -> int
     |  
     |  inherits = <built-in method inherits of PythonQt.PythonQtClassWrapper ...
     |      Returns if the class inherits or is of given type name
     |  
     |  isNull = <unbound qt slot isNull of QTime type>
     |      X.isNull(a) -> bool
     |  
     |  isValid = <unbound qt slot isValid of QTime type>
     |      X.isValid(a, b, c, d) -> bool
     |  
     |  minute = <unbound qt slot minute of QTime type>
     |      X.minute(a) -> int
     |  
     |  msec = <unbound qt slot msec of QTime type>
     |      X.msec(a) -> int
     |  
     |  msecsSinceStartOfDay = <unbound qt slot msecsSinceStartOfDay of QTime ...
     |      X.msecsSinceStartOfDay(a) -> int
     |  
     |  msecsTo = <unbound qt slot msecsTo of QTime type>
     |      X.msecsTo(a, b) -> int
     |  
     |  readFrom = <unbound qt slot readFrom of QTime type>
     |      X.readFrom(a, b)
     |  
     |  restart = <unbound qt slot restart of QTime type>
     |      X.restart(a) -> int
     |  
     |  second = <unbound qt slot second of QTime type>
     |      X.second(a) -> int
     |  
     |  secsTo = <unbound qt slot secsTo of QTime type>
     |      X.secsTo(a, b) -> int
     |  
     |  setHMS = <unbound qt slot setHMS of QTime type>
     |      X.setHMS(a, b, c, d, e) -> bool
     |  
     |  start = <unbound qt slot start of QTime type>
     |      X.start(a)
     |  
     |  toString = <unbound qt slot toString of QTime type>
     |      X.toString(a, b) -> str
     |  
     |  writeTo = <unbound qt slot writeTo of QTime type>
     |      X.writeTo(a, b)
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __delattr__(...)
     |      x.__delattr__('name') <==> del x.name
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __hash__(...)
     |      x.__hash__() <==> hash(x)
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __setattr__(...)
     |      x.__setattr__('name', value) <==> x.name = value
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __new__ = <built-in method __new__ of PythonQt.PythonQtClassWrapper ob...
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
    
    class QTimeLine(PythonQt.PythonQtInstanceWrapper)
     |  Method resolution order:
     |      QTimeLine
     |      PythonQt.PythonQtInstanceWrapper
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  __init__(...)
     |      x.__init__(...) initializes x; see help(type(x)) for signature
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  Backward = 1
     |  
     |  CosineCurve = 5
     |  
     |  CurveShape = <class 'PythonQt.QtCore.CurveShape'>
     |  
     |  
     |  Direction = <class 'PythonQt.QtCore.Direction'>
     |  
     |  
     |  EaseInCurve = 0
     |  
     |  EaseInOutCurve = 2
     |  
     |  EaseOutCurve = 1
     |  
     |  Forward = 0
     |  
     |  LinearCurve = 3
     |  
     |  NotRunning = 0
     |  
     |  Paused = 1
     |  
     |  Running = 2
     |  
     |  SineCurve = 4
     |  
     |  State = <class 'PythonQt.QtCore.State'>
     |  
     |  
     |  blockSignals = <unbound qt slot blockSignals of QTimeLine type>
     |      X.blockSignals(a, b) -> bool
     |  
     |  childEvent = <unbound qt slot py_q_childEvent of QTimeLine type>
     |      X.childEvent(a, b)
     |  
     |  children = <unbound qt slot children of QTimeLine type>
     |      X.children(a) -> tuple
     |  
     |  className = <built-in method className of PythonQt.PythonQtClassWrappe...
     |      Return the classname of the object
     |  
     |  connect = <unbound qt slot connect of QTimeLine type>
     |      X.connect(a, b, c, d, e) -> bool
     |  
     |  currentFrame = <unbound qt slot currentFrame of QTimeLine type>
     |      X.currentFrame(a) -> int
     |  
     |  currentTime = None
     |  
     |  currentValue = <unbound qt slot currentValue of QTimeLine type>
     |      X.currentValue(a) -> float
     |  
     |  curveShape = None
     |  
     |  customEvent = <unbound qt slot py_q_customEvent of QTimeLine type>
     |      X.customEvent(a, b)
     |  
     |  delete = <built-in method delete of PythonQt.PythonQtClassWrapper obje...
     |      Deletes the given C++ object
     |  
     |  deleteLater = <unbound qt slot deleteLater of QTimeLine type>
     |      X.deleteLater()
     |  
     |  destroyed = <unbound qt signal destroyed of QTimeLine type>
     |  
     |  
     |  direction = None
     |  
     |  disconnect = <unbound qt slot disconnect of QTimeLine type>
     |      X.disconnect(a, b, c, d) -> bool
     |  
     |  dumpObjectInfo = <unbound qt slot dumpObjectInfo of QTimeLine type>
     |      X.dumpObjectInfo(a)
     |  
     |  dumpObjectTree = <unbound qt slot dumpObjectTree of QTimeLine type>
     |      X.dumpObjectTree(a)
     |  
     |  duration = None
     |  
     |  dynamicPropertyNames = <unbound qt slot dynamicPropertyNames of QTimeL...
     |      X.dynamicPropertyNames(a)
     |  
     |  easingCurve = QEasingCurve (QEasingCurve at: 0x0)
     |  
     |  endFrame = <unbound qt slot endFrame of QTimeLine type>
     |      X.endFrame(a) -> int
     |  
     |  event = <unbound qt slot py_q_event of QTimeLine type>
     |      X.event(a, b) -> bool
     |  
     |  eventFilter = <unbound qt slot py_q_eventFilter of QTimeLine type>
     |      X.eventFilter(a, b, c) -> bool
     |  
     |  findChild = <unbound qt slot findChild of QTimeLine type>
     |      X.findChild(a, b, c) -> PythonQt.private.QObject
     |  
     |  findChildren = <unbound qt slot findChildren of QTimeLine type>
     |      X.findChildren(a, b, c) -> tuple
     |  
     |  finished = <unbound qt signal finished of QTimeLine type>
     |  
     |  
     |  frameChanged = <unbound qt signal frameChanged of QTimeLine type>
     |  
     |  
     |  frameForTime = <unbound qt slot frameForTime of QTimeLine type>
     |      X.frameForTime(a, b) -> int
     |  
     |  help = <built-in method help of PythonQt.PythonQtClassWrapper object>
     |      Shows the help of available methods for this class
     |  
     |  inherits = <built-in method inherits of PythonQt.PythonQtClassWrapper ...
     |      Returns if the class inherits or is of given type name
     |  
     |  installEventFilter = <unbound qt slot installEventFilter of QTimeLine ...
     |      X.installEventFilter(a, b)
     |  
     |  isSignalConnected = <unbound qt slot isSignalConnected of QTimeLine ty...
     |      X.isSignalConnected(a, b) -> bool
     |  
     |  isWidgetType = <unbound qt slot isWidgetType of QTimeLine type>
     |      X.isWidgetType(a) -> bool
     |  
     |  isWindowType = <unbound qt slot isWindowType of QTimeLine type>
     |      X.isWindowType(a) -> bool
     |  
     |  killTimer = <unbound qt slot killTimer of QTimeLine type>
     |      X.killTimer(a, b)
     |  
     |  loopCount = None
     |  
     |  metaObject = <unbound qt slot metaObject of QTimeLine type>
     |      X.metaObject(a) -> PythonQt.QtCore.QMetaObject
     |  
     |  moveToThread = <unbound qt slot moveToThread of QTimeLine type>
     |      X.moveToThread(a, b)
     |  
     |  objectName = None
     |  
     |  objectNameChanged = <unbound qt signal objectNameChanged of QTimeLine ...
     |  
     |  
     |  parent = <unbound qt slot parent of QTimeLine type>
     |      X.parent(a) -> PythonQt.private.QObject
     |  
     |  property = <unbound qt slot property of QTimeLine type>
     |      X.property(a, b) -> object
     |  
     |  removeEventFilter = <unbound qt slot removeEventFilter of QTimeLine ty...
     |      X.removeEventFilter(a, b)
     |  
     |  resume = <unbound qt slot resume of QTimeLine type>
     |      X.resume()
     |  
     |  sender = <unbound qt slot sender of QTimeLine type>
     |      X.sender(a) -> PythonQt.private.QObject
     |  
     |  senderSignalIndex = <unbound qt slot senderSignalIndex of QTimeLine ty...
     |      X.senderSignalIndex(a) -> int
     |  
     |  setCurrentTime = <unbound qt slot setCurrentTime of QTimeLine type>
     |      X.setCurrentTime(a)
     |  
     |  setCurveShape = <unbound qt slot setCurveShape of QTimeLine type>
     |      X.setCurveShape(a, b)
     |  
     |  setDirection = <unbound qt slot setDirection of QTimeLine type>
     |      X.setDirection(a, b)
     |  
     |  setDuration = <unbound qt slot setDuration of QTimeLine type>
     |      X.setDuration(a, b)
     |  
     |  setEasingCurve = <unbound qt slot setEasingCurve of QTimeLine type>
     |      X.setEasingCurve(a, b)
     |  
     |  setEndFrame = <unbound qt slot setEndFrame of QTimeLine type>
     |      X.setEndFrame(a, b)
     |  
     |  setFrameRange = <unbound qt slot setFrameRange of QTimeLine type>
     |      X.setFrameRange(a, b, c)
     |  
     |  setLoopCount = <unbound qt slot setLoopCount of QTimeLine type>
     |      X.setLoopCount(a, b)
     |  
     |  setObjectName = <unbound qt slot setObjectName of QTimeLine type>
     |      X.setObjectName(a, b)
     |  
     |  setParent = <unbound qt slot setParent of QTimeLine type>
     |      X.setParent(a, b)
     |  
     |  setPaused = <unbound qt slot setPaused of QTimeLine type>
     |      X.setPaused(a)
     |  
     |  setProperty = <unbound qt slot setProperty of QTimeLine type>
     |      X.setProperty(a, b, c) -> bool
     |  
     |  setStartFrame = <unbound qt slot setStartFrame of QTimeLine type>
     |      X.setStartFrame(a, b)
     |  
     |  setUpdateInterval = <unbound qt slot setUpdateInterval of QTimeLine ty...
     |      X.setUpdateInterval(a, b)
     |  
     |  signalsBlocked = <unbound qt slot signalsBlocked of QTimeLine type>
     |      X.signalsBlocked(a) -> bool
     |  
     |  start = <unbound qt slot start of QTimeLine type>
     |      X.start()
     |  
     |  startFrame = <unbound qt slot startFrame of QTimeLine type>
     |      X.startFrame(a) -> int
     |  
     |  startTimer = <unbound qt slot startTimer of QTimeLine type>
     |      X.startTimer(a, b, c) -> int
     |  
     |  state = <unbound qt slot state of QTimeLine type>
     |      X.state(a)
     |  
     |  stateChanged = <unbound qt signal stateChanged of QTimeLine type>
     |  
     |  
     |  stop = <unbound qt slot stop of QTimeLine type>
     |      X.stop()
     |  
     |  thread = <unbound qt slot thread of QTimeLine type>
     |      X.thread(a)
     |  
     |  timerEvent = <unbound qt slot py_q_timerEvent of QTimeLine type>
     |      X.timerEvent(a, b)
     |  
     |  toggleDirection = <unbound qt slot toggleDirection of QTimeLine type>
     |      X.toggleDirection()
     |  
     |  tr = <unbound qt slot tr of QTimeLine type>
     |      X.tr(a, b, c, d) -> str
     |  
     |  updateInterval = None
     |  
     |  valueChanged = <unbound qt signal valueChanged of QTimeLine type>
     |  
     |  
     |  valueForTime = <unbound qt slot py_q_valueForTime of QTimeLine type>
     |      X.valueForTime(a, b) -> float
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __delattr__(...)
     |      x.__delattr__('name') <==> del x.name
     |  
     |  __eq__(...)
     |      x.__eq__(y) <==> x==y
     |  
     |  __ge__(...)
     |      x.__ge__(y) <==> x>=y
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __gt__(...)
     |      x.__gt__(y) <==> x>y
     |  
     |  __hash__(...)
     |      x.__hash__() <==> hash(x)
     |  
     |  __le__(...)
     |      x.__le__(y) <==> x<=y
     |  
     |  __lt__(...)
     |      x.__lt__(y) <==> x<y
     |  
     |  __ne__(...)
     |      x.__ne__(y) <==> x!=y
     |  
     |  __nonzero__(...)
     |      x.__nonzero__() <==> x != 0
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __setattr__(...)
     |      x.__setattr__('name', value) <==> x.name = value
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __new__ = <built-in method __new__ of PythonQt.PythonQtClassWrapper ob...
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
    
    class QTimeZone(PythonQt.PythonQtInstanceWrapper)
     |  Method resolution order:
     |      QTimeZone
     |      PythonQt.PythonQtInstanceWrapper
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  __eq__(...)
     |      x.__eq__(y) <==> x==y
     |  
     |  __init__(...)
     |      x.__init__(...) initializes x; see help(type(x)) for signature
     |  
     |  __ne__(...)
     |      x.__ne__(y) <==> x!=y
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  DaylightTime = 1
     |  
     |  DefaultName = 0
     |  
     |  GenericTime = 2
     |  
     |  LongName = 1
     |  
     |  NameType = <class 'PythonQt.QtCore.NameType'>
     |  
     |  
     |  OffsetName = 3
     |  
     |  ShortName = 2
     |  
     |  StandardTime = 0
     |  
     |  TimeType = <class 'PythonQt.QtCore.TimeType'>
     |  
     |  
     |  abbreviation = <unbound qt slot abbreviation of QTimeZone type>
     |      X.abbreviation(a, b) -> str
     |  
     |  availableTimeZoneIds = <unbound qt slot static_QTimeZone_availableTime...
     |      X.availableTimeZoneIds(a)
     |  
     |  className = <built-in method className of PythonQt.PythonQtClassWrappe...
     |      Return the classname of the object
     |  
     |  comment = <unbound qt slot comment of QTimeZone type>
     |      X.comment(a) -> str
     |  
     |  country = <unbound qt slot country of QTimeZone type>
     |      X.country(a)
     |  
     |  daylightTimeOffset = <unbound qt slot daylightTimeOffset of QTimeZone ...
     |      X.daylightTimeOffset(a, b) -> int
     |  
     |  delete = <built-in method delete of PythonQt.PythonQtClassWrapper obje...
     |      Deletes the given C++ object
     |  
     |  displayName = <unbound qt slot displayName of QTimeZone type>
     |      X.displayName(a, b, c, d) -> str
     |  
     |  hasDaylightTime = <unbound qt slot hasDaylightTime of QTimeZone type>
     |      X.hasDaylightTime(a) -> bool
     |  
     |  hasTransitions = <unbound qt slot hasTransitions of QTimeZone type>
     |      X.hasTransitions(a) -> bool
     |  
     |  help = <built-in method help of PythonQt.PythonQtClassWrapper object>
     |      Shows the help of available methods for this class
     |  
     |  ianaIdToWindowsId = <unbound qt slot static_QTimeZone_ianaIdToWindowsI...
     |      X.ianaIdToWindowsId(a) -> PythonQt.QtCore.QByteArray
     |  
     |  id = <unbound qt slot id of QTimeZone type>
     |      X.id(a) -> PythonQt.QtCore.QByteArray
     |  
     |  inherits = <built-in method inherits of PythonQt.PythonQtClassWrapper ...
     |      Returns if the class inherits or is of given type name
     |  
     |  isDaylightTime = <unbound qt slot isDaylightTime of QTimeZone type>
     |      X.isDaylightTime(a, b) -> bool
     |  
     |  isTimeZoneIdAvailable = <unbound qt slot static_QTimeZone_isTimeZoneId...
     |      X.isTimeZoneIdAvailable(a) -> bool
     |  
     |  isValid = <unbound qt slot isValid of QTimeZone type>
     |      X.isValid(a) -> bool
     |  
     |  offsetFromUtc = <unbound qt slot offsetFromUtc of QTimeZone type>
     |      X.offsetFromUtc(a, b) -> int
     |  
     |  operator_assign = <unbound qt slot operator_assign of QTimeZone type>
     |      X.operator_assign(a, b) -> PythonQt.QtCore.QTimeZone
     |  
     |  readFrom = <unbound qt slot readFrom of QTimeZone type>
     |      X.readFrom(a, b)
     |  
     |  standardTimeOffset = <unbound qt slot standardTimeOffset of QTimeZone ...
     |      X.standardTimeOffset(a, b) -> int
     |  
     |  swap = <unbound qt slot swap of QTimeZone type>
     |      X.swap(a, b)
     |  
     |  systemTimeZone = <unbound qt slot static_QTimeZone_systemTimeZone of Q...
     |      X.systemTimeZone() -> PythonQt.QtCore.QTimeZone
     |  
     |  systemTimeZoneId = <unbound qt slot static_QTimeZone_systemTimeZoneId ...
     |      X.systemTimeZoneId() -> PythonQt.QtCore.QByteArray
     |  
     |  utc = <unbound qt slot static_QTimeZone_utc of QTimeZone type>
     |      X.utc() -> PythonQt.QtCore.QTimeZone
     |  
     |  windowsIdToDefaultIanaId = <unbound qt slot static_QTimeZone_windowsId...
     |      X.windowsIdToDefaultIanaId(a, b) -> PythonQt.QtCore.QByteArray
     |  
     |  windowsIdToIanaIds = <unbound qt slot static_QTimeZone_windowsIdToIana...
     |      X.windowsIdToIanaIds(a, b)
     |  
     |  writeTo = <unbound qt slot writeTo of QTimeZone type>
     |      X.writeTo(a, b)
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __delattr__(...)
     |      x.__delattr__('name') <==> del x.name
     |  
     |  __ge__(...)
     |      x.__ge__(y) <==> x>=y
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __gt__(...)
     |      x.__gt__(y) <==> x>y
     |  
     |  __hash__(...)
     |      x.__hash__() <==> hash(x)
     |  
     |  __le__(...)
     |      x.__le__(y) <==> x<=y
     |  
     |  __lt__(...)
     |      x.__lt__(y) <==> x<y
     |  
     |  __nonzero__(...)
     |      x.__nonzero__() <==> x != 0
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __setattr__(...)
     |      x.__setattr__('name', value) <==> x.name = value
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __new__ = <built-in method __new__ of PythonQt.PythonQtClassWrapper ob...
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
    
    class QTimer(PythonQt.PythonQtInstanceWrapper)
     |  Method resolution order:
     |      QTimer
     |      PythonQt.PythonQtInstanceWrapper
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  __init__(...)
     |      x.__init__(...) initializes x; see help(type(x)) for signature
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  active = None
     |  
     |  blockSignals = <unbound qt slot blockSignals of QTimer type>
     |      X.blockSignals(a, b) -> bool
     |  
     |  childEvent = <unbound qt slot py_q_childEvent of QTimer type>
     |      X.childEvent(a, b)
     |  
     |  children = <unbound qt slot children of QTimer type>
     |      X.children(a) -> tuple
     |  
     |  className = <built-in method className of PythonQt.PythonQtClassWrappe...
     |      Return the classname of the object
     |  
     |  connect = <unbound qt slot connect of QTimer type>
     |      X.connect(a, b, c, d, e) -> bool
     |  
     |  customEvent = <unbound qt slot py_q_customEvent of QTimer type>
     |      X.customEvent(a, b)
     |  
     |  delete = <built-in method delete of PythonQt.PythonQtClassWrapper obje...
     |      Deletes the given C++ object
     |  
     |  deleteLater = <unbound qt slot deleteLater of QTimer type>
     |      X.deleteLater()
     |  
     |  destroyed = <unbound qt signal destroyed of QTimer type>
     |  
     |  
     |  disconnect = <unbound qt slot disconnect of QTimer type>
     |      X.disconnect(a, b, c, d) -> bool
     |  
     |  dumpObjectInfo = <unbound qt slot dumpObjectInfo of QTimer type>
     |      X.dumpObjectInfo(a)
     |  
     |  dumpObjectTree = <unbound qt slot dumpObjectTree of QTimer type>
     |      X.dumpObjectTree(a)
     |  
     |  dynamicPropertyNames = <unbound qt slot dynamicPropertyNames of QTimer...
     |      X.dynamicPropertyNames(a)
     |  
     |  event = <unbound qt slot py_q_event of QTimer type>
     |      X.event(a, b) -> bool
     |  
     |  eventFilter = <unbound qt slot py_q_eventFilter of QTimer type>
     |      X.eventFilter(a, b, c) -> bool
     |  
     |  findChild = <unbound qt slot findChild of QTimer type>
     |      X.findChild(a, b, c) -> PythonQt.private.QObject
     |  
     |  findChildren = <unbound qt slot findChildren of QTimer type>
     |      X.findChildren(a, b, c) -> tuple
     |  
     |  help = <built-in method help of PythonQt.PythonQtClassWrapper object>
     |      Shows the help of available methods for this class
     |  
     |  inherits = <built-in method inherits of PythonQt.PythonQtClassWrapper ...
     |      Returns if the class inherits or is of given type name
     |  
     |  installEventFilter = <unbound qt slot installEventFilter of QTimer typ...
     |      X.installEventFilter(a, b)
     |  
     |  interval = None
     |  
     |  isActive = <unbound qt slot isActive of QTimer type>
     |      X.isActive(a) -> bool
     |  
     |  isSignalConnected = <unbound qt slot isSignalConnected of QTimer type>
     |      X.isSignalConnected(a, b) -> bool
     |  
     |  isSingleShot = <unbound qt slot isSingleShot of QTimer type>
     |      X.isSingleShot(a) -> bool
     |  
     |  isWidgetType = <unbound qt slot isWidgetType of QTimer type>
     |      X.isWidgetType(a) -> bool
     |  
     |  isWindowType = <unbound qt slot isWindowType of QTimer type>
     |      X.isWindowType(a) -> bool
     |  
     |  killTimer = <unbound qt slot killTimer of QTimer type>
     |      X.killTimer(a, b)
     |  
     |  metaObject = <unbound qt slot metaObject of QTimer type>
     |      X.metaObject(a) -> PythonQt.QtCore.QMetaObject
     |  
     |  moveToThread = <unbound qt slot moveToThread of QTimer type>
     |      X.moveToThread(a, b)
     |  
     |  objectName = None
     |  
     |  objectNameChanged = <unbound qt signal objectNameChanged of QTimer typ...
     |  
     |  
     |  parent = <unbound qt slot parent of QTimer type>
     |      X.parent(a) -> PythonQt.private.QObject
     |  
     |  property = <unbound qt slot property of QTimer type>
     |      X.property(a, b) -> object
     |  
     |  remainingTime = None
     |  
     |  removeEventFilter = <unbound qt slot removeEventFilter of QTimer type>
     |      X.removeEventFilter(a, b)
     |  
     |  sender = <unbound qt slot sender of QTimer type>
     |      X.sender(a) -> PythonQt.private.QObject
     |  
     |  senderSignalIndex = <unbound qt slot senderSignalIndex of QTimer type>
     |      X.senderSignalIndex(a) -> int
     |  
     |  setInterval = <unbound qt slot setInterval of QTimer type>
     |      X.setInterval(a, b)
     |  
     |  setObjectName = <unbound qt slot setObjectName of QTimer type>
     |      X.setObjectName(a, b)
     |  
     |  setParent = <unbound qt slot setParent of QTimer type>
     |      X.setParent(a, b)
     |  
     |  setProperty = <unbound qt slot setProperty of QTimer type>
     |      X.setProperty(a, b, c) -> bool
     |  
     |  setSingleShot = <unbound qt slot setSingleShot of QTimer type>
     |      X.setSingleShot(a, b)
     |  
     |  setTimerType = <unbound qt slot setTimerType of QTimer type>
     |      X.setTimerType(a, b)
     |  
     |  signalsBlocked = <unbound qt slot signalsBlocked of QTimer type>
     |      X.signalsBlocked(a) -> bool
     |  
     |  singleShot = <unbound qt slot static_QTimer_singleShot of QTimer type>
     |      X.singleShot(a, b, c, d)
     |  
     |  start = <unbound qt slot start of QTimer type>
     |      X.start(a)
     |  
     |  startTimer = <unbound qt slot startTimer of QTimer type>
     |      X.startTimer(a, b, c) -> int
     |  
     |  stop = <unbound qt slot stop of QTimer type>
     |      X.stop()
     |  
     |  thread = <unbound qt slot thread of QTimer type>
     |      X.thread(a)
     |  
     |  timeout = <unbound qt signal timeout of QTimer type>
     |  
     |  
     |  timerEvent = <unbound qt slot py_q_timerEvent of QTimer type>
     |      X.timerEvent(a, b)
     |  
     |  timerId = <unbound qt slot timerId of QTimer type>
     |      X.timerId(a) -> int
     |  
     |  timerType = None
     |  
     |  tr = <unbound qt slot tr of QTimer type>
     |      X.tr(a, b, c, d) -> str
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __delattr__(...)
     |      x.__delattr__('name') <==> del x.name
     |  
     |  __eq__(...)
     |      x.__eq__(y) <==> x==y
     |  
     |  __ge__(...)
     |      x.__ge__(y) <==> x>=y
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __gt__(...)
     |      x.__gt__(y) <==> x>y
     |  
     |  __hash__(...)
     |      x.__hash__() <==> hash(x)
     |  
     |  __le__(...)
     |      x.__le__(y) <==> x<=y
     |  
     |  __lt__(...)
     |      x.__lt__(y) <==> x<y
     |  
     |  __ne__(...)
     |      x.__ne__(y) <==> x!=y
     |  
     |  __nonzero__(...)
     |      x.__nonzero__() <==> x != 0
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __setattr__(...)
     |      x.__setattr__('name', value) <==> x.name = value
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __new__ = <built-in method __new__ of PythonQt.PythonQtClassWrapper ob...
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
    
    class QTimerEvent(PythonQt.PythonQtInstanceWrapper)
     |  Method resolution order:
     |      QTimerEvent
     |      PythonQt.PythonQtInstanceWrapper
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  __init__(...)
     |      x.__init__(...) initializes x; see help(type(x)) for signature
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  AcceptDropsChange = 152
     |  
     |  ActionAdded = 114
     |  
     |  ActionChanged = 113
     |  
     |  ActionRemoved = 115
     |  
     |  ActivateControl = 80
     |  
     |  ActivationChange = 99
     |  
     |  ApplicationActivate = 121
     |  
     |  ApplicationActivated = 121
     |  
     |  ApplicationDeactivate = 122
     |  
     |  ApplicationDeactivated = 122
     |  
     |  ApplicationFontChange = 36
     |  
     |  ApplicationLayoutDirectionChange = 37
     |  
     |  ApplicationPaletteChange = 38
     |  
     |  ApplicationStateChange = 214
     |  
     |  ApplicationWindowIconChange = 35
     |  
     |  ChildAdded = 68
     |  
     |  ChildPolished = 69
     |  
     |  ChildRemoved = 71
     |  
     |  Clipboard = 40
     |  
     |  Close = 19
     |  
     |  CloseSoftwareInputPanel = 200
     |  
     |  ContentsRectChange = 178
     |  
     |  ContextMenu = 82
     |  
     |  Create = 15
     |  
     |  CursorChange = 183
     |  
     |  DeactivateControl = 81
     |  
     |  DeferredDelete = 52
     |  
     |  Destroy = 16
     |  
     |  DragEnter = 60
     |  
     |  DragLeave = 62
     |  
     |  DragMove = 61
     |  
     |  DragResponse = 64
     |  
     |  Drop = 63
     |  
     |  DynamicPropertyChange = 170
     |  
     |  EmbeddingControl = 79
     |  
     |  EnabledChange = 98
     |  
     |  Enter = 10
     |  
     |  EnterWhatsThisMode = 124
     |  
     |  Expose = 206
     |  
     |  FileOpen = 116
     |  
     |  FocusAboutToChange = 23
     |  
     |  FocusIn = 8
     |  
     |  FocusOut = 9
     |  
     |  FontChange = 97
     |  
     |  FutureCallOut = 180
     |  
     |  Gesture = 198
     |  
     |  GestureOverride = 202
     |  
     |  GrabKeyboard = 188
     |  
     |  GrabMouse = 186
     |  
     |  GraphicsSceneContextMenu = 159
     |  
     |  GraphicsSceneDragEnter = 164
     |  
     |  GraphicsSceneDragLeave = 166
     |  
     |  GraphicsSceneDragMove = 165
     |  
     |  GraphicsSceneDrop = 167
     |  
     |  GraphicsSceneHelp = 163
     |  
     |  GraphicsSceneHoverEnter = 160
     |  
     |  GraphicsSceneHoverLeave = 162
     |  
     |  GraphicsSceneHoverMove = 161
     |  
     |  GraphicsSceneMouseDoubleClick = 158
     |  
     |  GraphicsSceneMouseMove = 155
     |  
     |  GraphicsSceneMousePress = 156
     |  
     |  GraphicsSceneMouseRelease = 157
     |  
     |  GraphicsSceneMove = 182
     |  
     |  GraphicsSceneResize = 181
     |  
     |  GraphicsSceneWheel = 168
     |  
     |  HelpRequest = 95
     |  
     |  Hide = 18
     |  
     |  HideToParent = 27
     |  
     |  HoverEnter = 127
     |  
     |  HoverLeave = 128
     |  
     |  HoverMove = 129
     |  
     |  IconDrag = 96
     |  
     |  IconTextChange = 101
     |  
     |  InputMethod = 83
     |  
     |  InputMethodQuery = 207
     |  
     |  KeyPress = 6
     |  
     |  KeyRelease = 7
     |  
     |  KeyboardLayoutChange = 169
     |  
     |  LanguageChange = 89
     |  
     |  LayoutDirectionChange = 90
     |  
     |  LayoutRequest = 76
     |  
     |  Leave = 11
     |  
     |  LeaveWhatsThisMode = 125
     |  
     |  LocaleChange = 88
     |  
     |  MacGLClearDrawable = 191
     |  
     |  MacGLWindowChange = 179
     |  
     |  MacSizeChange = 177
     |  
     |  MaxUser = 65535
     |  
     |  MetaCall = 43
     |  
     |  ModifiedChange = 102
     |  
     |  MouseButtonDblClick = 4
     |  
     |  MouseButtonPress = 2
     |  
     |  MouseButtonRelease = 3
     |  
     |  MouseMove = 5
     |  
     |  MouseTrackingChange = 109
     |  
     |  Move = 13
     |  
     |  NativeGesture = 197
     |  
     |  NetworkReplyUpdated = 185
     |  
     |  NonClientAreaMouseButtonDblClick = 176
     |  
     |  NonClientAreaMouseButtonPress = 174
     |  
     |  NonClientAreaMouseButtonRelease = 175
     |  
     |  NonClientAreaMouseMove = 173
     |  
     |  None = 0
     |  
     |  OkRequest = 94
     |  
     |  OrientationChange = 208
     |  
     |  Paint = 12
     |  
     |  PaletteChange = 39
     |  
     |  ParentAboutToChange = 131
     |  
     |  ParentChange = 21
     |  
     |  PlatformPanel = 212
     |  
     |  PlatformSurface = 217
     |  
     |  Polish = 75
     |  
     |  PolishRequest = 74
     |  
     |  QueryWhatsThis = 123
     |  
     |  Quit = 20
     |  
     |  ReadOnlyChange = 106
     |  
     |  RequestSoftwareInputPanel = 199
     |  
     |  Resize = 14
     |  
     |  ScreenChangeInternal = 216
     |  
     |  Scroll = 205
     |  
     |  ScrollPrepare = 204
     |  
     |  Shortcut = 117
     |  
     |  ShortcutOverride = 51
     |  
     |  Show = 17
     |  
     |  ShowToParent = 26
     |  
     |  ShowWindowRequest = 73
     |  
     |  SockAct = 50
     |  
     |  SockClose = 211
     |  
     |  Speech = 42
     |  
     |  StateMachineSignal = 192
     |  
     |  StateMachineWrapped = 193
     |  
     |  StatusTip = 112
     |  
     |  Style = 91
     |  
     |  StyleAnimationUpdate = 213
     |  
     |  StyleChange = 100
     |  
     |  TabletEnterProximity = 171
     |  
     |  TabletLeaveProximity = 172
     |  
     |  TabletMove = 87
     |  
     |  TabletPress = 92
     |  
     |  TabletRelease = 93
     |  
     |  ThemeChange = 210
     |  
     |  ThreadChange = 22
     |  
     |  Timer = 1
     |  
     |  ToolBarChange = 120
     |  
     |  ToolTip = 110
     |  
     |  ToolTipChange = 184
     |  
     |  TouchBegin = 194
     |  
     |  TouchCancel = 209
     |  
     |  TouchEnd = 196
     |  
     |  TouchUpdate = 195
     |  
     |  Type = <class 'PythonQt.QtCore.Type'>
     |  
     |  
     |  UngrabKeyboard = 189
     |  
     |  UngrabMouse = 187
     |  
     |  UpdateLater = 78
     |  
     |  UpdateRequest = 77
     |  
     |  User = 1000
     |  
     |  WhatsThis = 111
     |  
     |  WhatsThisClicked = 118
     |  
     |  Wheel = 31
     |  
     |  WinEventAct = 132
     |  
     |  WinIdChange = 203
     |  
     |  WindowActivate = 24
     |  
     |  WindowBlocked = 103
     |  
     |  WindowChangeInternal = 215
     |  
     |  WindowDeactivate = 25
     |  
     |  WindowIconChange = 34
     |  
     |  WindowStateChange = 105
     |  
     |  WindowTitleChange = 33
     |  
     |  WindowUnblocked = 104
     |  
     |  ZOrderChange = 126
     |  
     |  ZeroTimerEvent = 154
     |  
     |  accept = <unbound qt slot accept of QTimerEvent type>
     |      X.accept(a)
     |  
     |  className = <built-in method className of PythonQt.PythonQtClassWrappe...
     |      Return the classname of the object
     |  
     |  delete = <built-in method delete of PythonQt.PythonQtClassWrapper obje...
     |      Deletes the given C++ object
     |  
     |  help = <built-in method help of PythonQt.PythonQtClassWrapper object>
     |      Shows the help of available methods for this class
     |  
     |  ignore = <unbound qt slot ignore of QTimerEvent type>
     |      X.ignore(a)
     |  
     |  inherits = <built-in method inherits of PythonQt.PythonQtClassWrapper ...
     |      Returns if the class inherits or is of given type name
     |  
     |  isAccepted = <unbound qt slot isAccepted of QTimerEvent type>
     |      X.isAccepted(a) -> bool
     |  
     |  operator_assign = <unbound qt slot operator_assign of QTimerEvent type...
     |      X.operator_assign(a, b) -> PythonQt.QtCore.QEvent
     |  
     |  registerEventType = <unbound qt slot static_QEvent_registerEventType o...
     |      X.registerEventType(a) -> int
     |  
     |  setAccepted = <unbound qt slot setAccepted of QTimerEvent type>
     |      X.setAccepted(a, b)
     |  
     |  spontaneous = <unbound qt slot spontaneous of QTimerEvent type>
     |      X.spontaneous(a) -> bool
     |  
     |  timerId = <unbound qt slot timerId of QTimerEvent type>
     |      X.timerId(a) -> int
     |  
     |  type = <unbound qt slot type of QTimerEvent type>
     |      X.type(a)
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __delattr__(...)
     |      x.__delattr__('name') <==> del x.name
     |  
     |  __eq__(...)
     |      x.__eq__(y) <==> x==y
     |  
     |  __ge__(...)
     |      x.__ge__(y) <==> x>=y
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __gt__(...)
     |      x.__gt__(y) <==> x>y
     |  
     |  __hash__(...)
     |      x.__hash__() <==> hash(x)
     |  
     |  __le__(...)
     |      x.__le__(y) <==> x<=y
     |  
     |  __lt__(...)
     |      x.__lt__(y) <==> x<y
     |  
     |  __ne__(...)
     |      x.__ne__(y) <==> x!=y
     |  
     |  __nonzero__(...)
     |      x.__nonzero__() <==> x != 0
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __setattr__(...)
     |      x.__setattr__('name', value) <==> x.name = value
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __new__ = <built-in method __new__ of PythonQt.PythonQtClassWrapper ob...
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
    
    class QTranslator(PythonQt.PythonQtInstanceWrapper)
     |  Method resolution order:
     |      QTranslator
     |      PythonQt.PythonQtInstanceWrapper
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  __init__(...)
     |      x.__init__(...) initializes x; see help(type(x)) for signature
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  blockSignals = <unbound qt slot blockSignals of QTranslator type>
     |      X.blockSignals(a, b) -> bool
     |  
     |  childEvent = <unbound qt slot py_q_childEvent of QTranslator type>
     |      X.childEvent(a, b)
     |  
     |  children = <unbound qt slot children of QTranslator type>
     |      X.children(a) -> tuple
     |  
     |  className = <built-in method className of PythonQt.PythonQtClassWrappe...
     |      Return the classname of the object
     |  
     |  connect = <unbound qt slot connect of QTranslator type>
     |      X.connect(a, b, c, d, e) -> bool
     |  
     |  customEvent = <unbound qt slot py_q_customEvent of QTranslator type>
     |      X.customEvent(a, b)
     |  
     |  delete = <built-in method delete of PythonQt.PythonQtClassWrapper obje...
     |      Deletes the given C++ object
     |  
     |  deleteLater = <unbound qt slot deleteLater of QTranslator type>
     |      X.deleteLater()
     |  
     |  destroyed = <unbound qt signal destroyed of QTranslator type>
     |  
     |  
     |  disconnect = <unbound qt slot disconnect of QTranslator type>
     |      X.disconnect(a, b, c, d) -> bool
     |  
     |  dumpObjectInfo = <unbound qt slot dumpObjectInfo of QTranslator type>
     |      X.dumpObjectInfo(a)
     |  
     |  dumpObjectTree = <unbound qt slot dumpObjectTree of QTranslator type>
     |      X.dumpObjectTree(a)
     |  
     |  dynamicPropertyNames = <unbound qt slot dynamicPropertyNames of QTrans...
     |      X.dynamicPropertyNames(a)
     |  
     |  event = <unbound qt slot py_q_event of QTranslator type>
     |      X.event(a, b) -> bool
     |  
     |  eventFilter = <unbound qt slot py_q_eventFilter of QTranslator type>
     |      X.eventFilter(a, b, c) -> bool
     |  
     |  findChild = <unbound qt slot findChild of QTranslator type>
     |      X.findChild(a, b, c) -> PythonQt.private.QObject
     |  
     |  findChildren = <unbound qt slot findChildren of QTranslator type>
     |      X.findChildren(a, b, c) -> tuple
     |  
     |  help = <built-in method help of PythonQt.PythonQtClassWrapper object>
     |      Shows the help of available methods for this class
     |  
     |  inherits = <built-in method inherits of PythonQt.PythonQtClassWrapper ...
     |      Returns if the class inherits or is of given type name
     |  
     |  installEventFilter = <unbound qt slot installEventFilter of QTranslato...
     |      X.installEventFilter(a, b)
     |  
     |  isEmpty = <unbound qt slot py_q_isEmpty of QTranslator type>
     |      X.isEmpty(a) -> bool
     |  
     |  isSignalConnected = <unbound qt slot isSignalConnected of QTranslator ...
     |      X.isSignalConnected(a, b) -> bool
     |  
     |  isWidgetType = <unbound qt slot isWidgetType of QTranslator type>
     |      X.isWidgetType(a) -> bool
     |  
     |  isWindowType = <unbound qt slot isWindowType of QTranslator type>
     |      X.isWindowType(a) -> bool
     |  
     |  killTimer = <unbound qt slot killTimer of QTranslator type>
     |      X.killTimer(a, b)
     |  
     |  load = <unbound qt slot load of QTranslator type>
     |      X.load(a, b, c, d, e, f) -> bool
     |  
     |  metaObject = <unbound qt slot metaObject of QTranslator type>
     |      X.metaObject(a) -> PythonQt.QtCore.QMetaObject
     |  
     |  moveToThread = <unbound qt slot moveToThread of QTranslator type>
     |      X.moveToThread(a, b)
     |  
     |  objectName = None
     |  
     |  objectNameChanged = <unbound qt signal objectNameChanged of QTranslato...
     |  
     |  
     |  parent = <unbound qt slot parent of QTranslator type>
     |      X.parent(a) -> PythonQt.private.QObject
     |  
     |  property = <unbound qt slot property of QTranslator type>
     |      X.property(a, b) -> object
     |  
     |  removeEventFilter = <unbound qt slot removeEventFilter of QTranslator ...
     |      X.removeEventFilter(a, b)
     |  
     |  sender = <unbound qt slot sender of QTranslator type>
     |      X.sender(a) -> PythonQt.private.QObject
     |  
     |  senderSignalIndex = <unbound qt slot senderSignalIndex of QTranslator ...
     |      X.senderSignalIndex(a) -> int
     |  
     |  setObjectName = <unbound qt slot setObjectName of QTranslator type>
     |      X.setObjectName(a, b)
     |  
     |  setParent = <unbound qt slot setParent of QTranslator type>
     |      X.setParent(a, b)
     |  
     |  setProperty = <unbound qt slot setProperty of QTranslator type>
     |      X.setProperty(a, b, c) -> bool
     |  
     |  signalsBlocked = <unbound qt slot signalsBlocked of QTranslator type>
     |      X.signalsBlocked(a) -> bool
     |  
     |  startTimer = <unbound qt slot startTimer of QTranslator type>
     |      X.startTimer(a, b, c) -> int
     |  
     |  thread = <unbound qt slot thread of QTranslator type>
     |      X.thread(a)
     |  
     |  timerEvent = <unbound qt slot py_q_timerEvent of QTranslator type>
     |      X.timerEvent(a, b)
     |  
     |  tr = <unbound qt slot tr of QTranslator type>
     |      X.tr(a, b, c, d) -> str
     |  
     |  translate = <unbound qt slot py_q_translate of QTranslator type>
     |      X.translate(a, b, c, d, e) -> str
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __delattr__(...)
     |      x.__delattr__('name') <==> del x.name
     |  
     |  __eq__(...)
     |      x.__eq__(y) <==> x==y
     |  
     |  __ge__(...)
     |      x.__ge__(y) <==> x>=y
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __gt__(...)
     |      x.__gt__(y) <==> x>y
     |  
     |  __hash__(...)
     |      x.__hash__() <==> hash(x)
     |  
     |  __le__(...)
     |      x.__le__(y) <==> x<=y
     |  
     |  __lt__(...)
     |      x.__lt__(y) <==> x<y
     |  
     |  __ne__(...)
     |      x.__ne__(y) <==> x!=y
     |  
     |  __nonzero__(...)
     |      x.__nonzero__() <==> x != 0
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __setattr__(...)
     |      x.__setattr__('name', value) <==> x.name = value
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __new__ = <built-in method __new__ of PythonQt.PythonQtClassWrapper ob...
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
    
    class QUrl(PythonQt.PythonQtInstanceWrapper)
     |  Method resolution order:
     |      QUrl
     |      PythonQt.PythonQtInstanceWrapper
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  __eq__(...)
     |      x.__eq__(y) <==> x==y
     |  
     |  __init__(...)
     |      x.__init__(...) initializes x; see help(type(x)) for signature
     |  
     |  __lt__(...)
     |      x.__lt__(y) <==> x<y
     |  
     |  __ne__(...)
     |      x.__ne__(y) <==> x!=y
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  AssumeLocalFile = 1
     |  
     |  ComponentFormattingOption = <class 'PythonQt.QtCore.ComponentFormattin...
     |  
     |  
     |  ComponentFormattingOptions = <class 'PythonQt.QtCore.ComponentFormatti...
     |  
     |  
     |  DecodeReserved = 33554432
     |  
     |  DecodedMode = 2
     |  
     |  DefaultResolution = 0
     |  
     |  EncodeDelimiters = 12582912
     |  
     |  EncodeReserved = 16777216
     |  
     |  EncodeSpaces = 1048576
     |  
     |  EncodeUnicode = 2097152
     |  
     |  FullyDecoded = 133169152
     |  
     |  FullyEncoded = 32505856
     |  
     |  None = 0
     |  
     |  NormalizePathSegments = 4096
     |  
     |  ParsingMode = <class 'PythonQt.QtCore.ParsingMode'>
     |  
     |  
     |  PreferLocalFile = 512
     |  
     |  PrettyDecoded = 0
     |  
     |  RemoveAuthority = 30
     |  
     |  RemoveFilename = 2048
     |  
     |  RemoveFragment = 128
     |  
     |  RemovePassword = 2
     |  
     |  RemovePath = 32
     |  
     |  RemovePort = 8
     |  
     |  RemoveQuery = 64
     |  
     |  RemoveScheme = 1
     |  
     |  RemoveUserInfo = 6
     |  
     |  StrictMode = 1
     |  
     |  StripTrailingSlash = 1024
     |  
     |  TolerantMode = 0
     |  
     |  UrlFormattingOption = <class 'PythonQt.QtCore.UrlFormattingOption'>
     |  
     |  
     |  UserInputResolutionOption = <class 'PythonQt.QtCore.UserInputResolutio...
     |  
     |  
     |  adjusted = <unbound qt slot adjusted of QUrl type>
     |      X.adjusted(a, b) -> PythonQt.QtCore.QUrl
     |  
     |  authority = <unbound qt slot authority of QUrl type>
     |      X.authority(a, b) -> str
     |  
     |  className = <built-in method className of PythonQt.PythonQtClassWrappe...
     |      Return the classname of the object
     |  
     |  clear = <unbound qt slot clear of QUrl type>
     |      X.clear(a)
     |  
     |  delete = <built-in method delete of PythonQt.PythonQtClassWrapper obje...
     |      Deletes the given C++ object
     |  
     |  errorString = <unbound qt slot errorString of QUrl type>
     |      X.errorString(a) -> str
     |  
     |  fileName = <unbound qt slot fileName of QUrl type>
     |      X.fileName(a, b) -> str
     |  
     |  fragment = <unbound qt slot fragment of QUrl type>
     |      X.fragment(a, b) -> str
     |  
     |  fromAce = <unbound qt slot static_QUrl_fromAce of QUrl type>
     |      X.fromAce(a) -> str
     |  
     |  fromEncoded = <unbound qt slot static_QUrl_fromEncoded of QUrl type>
     |      X.fromEncoded(a, b) -> PythonQt.QtCore.QUrl
     |  
     |  fromLocalFile = <unbound qt slot static_QUrl_fromLocalFile of QUrl typ...
     |      X.fromLocalFile(a) -> PythonQt.QtCore.QUrl
     |  
     |  fromPercentEncoding = <unbound qt slot static_QUrl_fromPercentEncoding...
     |      X.fromPercentEncoding(a) -> str
     |  
     |  fromStringList = <unbound qt slot static_QUrl_fromStringList of QUrl t...
     |      X.fromStringList(a, b) -> tuple
     |  
     |  fromUserInput = <unbound qt slot static_QUrl_fromUserInput of QUrl typ...
     |      X.fromUserInput(a) -> PythonQt.QtCore.QUrl
     |  
     |  hasFragment = <unbound qt slot hasFragment of QUrl type>
     |      X.hasFragment(a) -> bool
     |  
     |  hasQuery = <unbound qt slot hasQuery of QUrl type>
     |      X.hasQuery(a) -> bool
     |  
     |  help = <built-in method help of PythonQt.PythonQtClassWrapper object>
     |      Shows the help of available methods for this class
     |  
     |  host = <unbound qt slot host of QUrl type>
     |      X.host(a, b) -> str
     |  
     |  idnWhitelist = <unbound qt slot static_QUrl_idnWhitelist of QUrl type>
     |      X.idnWhitelist() -> tuple
     |  
     |  inherits = <built-in method inherits of PythonQt.PythonQtClassWrapper ...
     |      Returns if the class inherits or is of given type name
     |  
     |  isEmpty = <unbound qt slot isEmpty of QUrl type>
     |      X.isEmpty(a) -> bool
     |  
     |  isLocalFile = <unbound qt slot isLocalFile of QUrl type>
     |      X.isLocalFile(a) -> bool
     |  
     |  isParentOf = <unbound qt slot isParentOf of QUrl type>
     |      X.isParentOf(a, b) -> bool
     |  
     |  isRelative = <unbound qt slot isRelative of QUrl type>
     |      X.isRelative(a) -> bool
     |  
     |  isValid = <unbound qt slot isValid of QUrl type>
     |      X.isValid(a) -> bool
     |  
     |  matches = <unbound qt slot matches of QUrl type>
     |      X.matches(a, b, c) -> bool
     |  
     |  password = <unbound qt slot password of QUrl type>
     |      X.password(a, b) -> str
     |  
     |  path = <unbound qt slot path of QUrl type>
     |      X.path(a, b) -> str
     |  
     |  port = <unbound qt slot port of QUrl type>
     |      X.port(a, b) -> int
     |  
     |  query = <unbound qt slot query of QUrl type>
     |      X.query(a, b) -> str
     |  
     |  readFrom = <unbound qt slot readFrom of QUrl type>
     |      X.readFrom(a, b)
     |  
     |  resolved = <unbound qt slot resolved of QUrl type>
     |      X.resolved(a, b) -> PythonQt.QtCore.QUrl
     |  
     |  scheme = <unbound qt slot scheme of QUrl type>
     |      X.scheme(a) -> str
     |  
     |  setAuthority = <unbound qt slot setAuthority of QUrl type>
     |      X.setAuthority(a, b, c)
     |  
     |  setFragment = <unbound qt slot setFragment of QUrl type>
     |      X.setFragment(a, b, c)
     |  
     |  setHost = <unbound qt slot setHost of QUrl type>
     |      X.setHost(a, b, c)
     |  
     |  setIdnWhitelist = <unbound qt slot static_QUrl_setIdnWhitelist of QUrl...
     |      X.setIdnWhitelist(a)
     |  
     |  setPassword = <unbound qt slot setPassword of QUrl type>
     |      X.setPassword(a, b, c)
     |  
     |  setPath = <unbound qt slot setPath of QUrl type>
     |      X.setPath(a, b, c)
     |  
     |  setPort = <unbound qt slot setPort of QUrl type>
     |      X.setPort(a, b)
     |  
     |  setQuery = <unbound qt slot setQuery of QUrl type>
     |      X.setQuery(a, b, c)
     |  
     |  setScheme = <unbound qt slot setScheme of QUrl type>
     |      X.setScheme(a, b)
     |  
     |  setUrl = <unbound qt slot setUrl of QUrl type>
     |      X.setUrl(a, b, c)
     |  
     |  setUserInfo = <unbound qt slot setUserInfo of QUrl type>
     |      X.setUserInfo(a, b, c)
     |  
     |  setUserName = <unbound qt slot setUserName of QUrl type>
     |      X.setUserName(a, b, c)
     |  
     |  swap = <unbound qt slot swap of QUrl type>
     |      X.swap(a, b)
     |  
     |  toAce = <unbound qt slot static_QUrl_toAce of QUrl type>
     |      X.toAce(a) -> PythonQt.QtCore.QByteArray
     |  
     |  toDisplayString = <unbound qt slot toDisplayString of QUrl type>
     |      X.toDisplayString(a, b) -> str
     |  
     |  toEncoded = <unbound qt slot toEncoded of QUrl type>
     |      X.toEncoded(a, b) -> PythonQt.QtCore.QByteArray
     |  
     |  toLocalFile = <unbound qt slot toLocalFile of QUrl type>
     |      X.toLocalFile(a) -> str
     |  
     |  toPercentEncoding = <unbound qt slot static_QUrl_toPercentEncoding of ...
     |      X.toPercentEncoding(a, b, c) -> PythonQt.QtCore.QByteArray
     |  
     |  toString = <unbound qt slot toString of QUrl type>
     |      X.toString(a, b) -> str
     |  
     |  toStringList = <unbound qt slot static_QUrl_toStringList of QUrl type>
     |      X.toStringList(a, b) -> tuple
     |  
     |  topLevelDomain = <unbound qt slot topLevelDomain of QUrl type>
     |      X.topLevelDomain(a, b) -> str
     |  
     |  url = <unbound qt slot url of QUrl type>
     |      X.url(a, b) -> str
     |  
     |  userInfo = <unbound qt slot userInfo of QUrl type>
     |      X.userInfo(a, b) -> str
     |  
     |  userName = <unbound qt slot userName of QUrl type>
     |      X.userName(a, b) -> str
     |  
     |  writeTo = <unbound qt slot writeTo of QUrl type>
     |      X.writeTo(a, b)
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __delattr__(...)
     |      x.__delattr__('name') <==> del x.name
     |  
     |  __ge__(...)
     |      x.__ge__(y) <==> x>=y
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __gt__(...)
     |      x.__gt__(y) <==> x>y
     |  
     |  __hash__(...)
     |      x.__hash__() <==> hash(x)
     |  
     |  __le__(...)
     |      x.__le__(y) <==> x<=y
     |  
     |  __nonzero__(...)
     |      x.__nonzero__() <==> x != 0
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __setattr__(...)
     |      x.__setattr__('name', value) <==> x.name = value
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __new__ = <built-in method __new__ of PythonQt.PythonQtClassWrapper ob...
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
    
    class QUrlQuery(PythonQt.PythonQtInstanceWrapper)
     |  Method resolution order:
     |      QUrlQuery
     |      PythonQt.PythonQtInstanceWrapper
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  __eq__(...)
     |      x.__eq__(y) <==> x==y
     |  
     |  __init__(...)
     |      x.__init__(...) initializes x; see help(type(x)) for signature
     |  
     |  __ne__(...)
     |      x.__ne__(y) <==> x!=y
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  addQueryItem = <unbound qt slot addQueryItem of QUrlQuery type>
     |      X.addQueryItem(a, b, c)
     |  
     |  allQueryItemValues = <unbound qt slot allQueryItemValues of QUrlQuery ...
     |      X.allQueryItemValues(a, b, c) -> tuple
     |  
     |  className = <built-in method className of PythonQt.PythonQtClassWrappe...
     |      Return the classname of the object
     |  
     |  clear = <unbound qt slot clear of QUrlQuery type>
     |      X.clear(a)
     |  
     |  defaultQueryPairDelimiter = <unbound qt slot static_QUrlQuery_defaultQ...
     |      X.defaultQueryPairDelimiter()
     |  
     |  defaultQueryValueDelimiter = <unbound qt slot static_QUrlQuery_default...
     |      X.defaultQueryValueDelimiter()
     |  
     |  delete = <built-in method delete of PythonQt.PythonQtClassWrapper obje...
     |      Deletes the given C++ object
     |  
     |  hasQueryItem = <unbound qt slot hasQueryItem of QUrlQuery type>
     |      X.hasQueryItem(a, b) -> bool
     |  
     |  help = <built-in method help of PythonQt.PythonQtClassWrapper object>
     |      Shows the help of available methods for this class
     |  
     |  inherits = <built-in method inherits of PythonQt.PythonQtClassWrapper ...
     |      Returns if the class inherits or is of given type name
     |  
     |  isEmpty = <unbound qt slot isEmpty of QUrlQuery type>
     |      X.isEmpty(a) -> bool
     |  
     |  operator_assign = <unbound qt slot operator_assign of QUrlQuery type>
     |      X.operator_assign(a, b) -> PythonQt.QtCore.QUrlQuery
     |  
     |  query = <unbound qt slot query of QUrlQuery type>
     |      X.query(a, b) -> str
     |  
     |  queryItemValue = <unbound qt slot queryItemValue of QUrlQuery type>
     |      X.queryItemValue(a, b, c) -> str
     |  
     |  queryItems = <unbound qt slot queryItems of QUrlQuery type>
     |      X.queryItems(a, b) -> tuple
     |  
     |  queryPairDelimiter = <unbound qt slot queryPairDelimiter of QUrlQuery ...
     |      X.queryPairDelimiter(a)
     |  
     |  queryValueDelimiter = <unbound qt slot queryValueDelimiter of QUrlQuer...
     |      X.queryValueDelimiter(a)
     |  
     |  removeAllQueryItems = <unbound qt slot removeAllQueryItems of QUrlQuer...
     |      X.removeAllQueryItems(a, b)
     |  
     |  removeQueryItem = <unbound qt slot removeQueryItem of QUrlQuery type>
     |      X.removeQueryItem(a, b)
     |  
     |  setQuery = <unbound qt slot setQuery of QUrlQuery type>
     |      X.setQuery(a, b)
     |  
     |  setQueryDelimiters = <unbound qt slot setQueryDelimiters of QUrlQuery ...
     |      X.setQueryDelimiters(a, b, c)
     |  
     |  setQueryItems = <unbound qt slot setQueryItems of QUrlQuery type>
     |      X.setQueryItems(a, b)
     |  
     |  swap = <unbound qt slot swap of QUrlQuery type>
     |      X.swap(a, b)
     |  
     |  toString = <unbound qt slot toString of QUrlQuery type>
     |      X.toString(a, b) -> str
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __delattr__(...)
     |      x.__delattr__('name') <==> del x.name
     |  
     |  __ge__(...)
     |      x.__ge__(y) <==> x>=y
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __gt__(...)
     |      x.__gt__(y) <==> x>y
     |  
     |  __hash__(...)
     |      x.__hash__() <==> hash(x)
     |  
     |  __le__(...)
     |      x.__le__(y) <==> x<=y
     |  
     |  __lt__(...)
     |      x.__lt__(y) <==> x<y
     |  
     |  __nonzero__(...)
     |      x.__nonzero__() <==> x != 0
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __setattr__(...)
     |      x.__setattr__('name', value) <==> x.name = value
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __new__ = <built-in method __new__ of PythonQt.PythonQtClassWrapper ob...
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
    
    class QUuid(PythonQt.PythonQtInstanceWrapper)
     |  Method resolution order:
     |      QUuid
     |      PythonQt.PythonQtInstanceWrapper
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  __eq__(...)
     |      x.__eq__(y) <==> x==y
     |  
     |  __ge__(...)
     |      x.__ge__(y) <==> x>=y
     |  
     |  __gt__(...)
     |      x.__gt__(y) <==> x>y
     |  
     |  __init__(...)
     |      x.__init__(...) initializes x; see help(type(x)) for signature
     |  
     |  __le__(...)
     |      x.__le__(y) <==> x<=y
     |  
     |  __lt__(...)
     |      x.__lt__(y) <==> x<y
     |  
     |  __ne__(...)
     |      x.__ne__(y) <==> x!=y
     |  
     |  __nonzero__(...)
     |      x.__nonzero__() <==> x != 0
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  DCE = 2
     |  
     |  EmbeddedPOSIX = 2
     |  
     |  Md5 = 3
     |  
     |  Microsoft = 6
     |  
     |  NCS = 0
     |  
     |  Name = 3
     |  
     |  Random = 4
     |  
     |  Reserved = 7
     |  
     |  Sha1 = 5
     |  
     |  Time = 1
     |  
     |  VarUnknown = -1
     |  
     |  Variant = <class 'PythonQt.QtCore.Variant'>
     |  
     |  
     |  VerUnknown = -1
     |  
     |  Version = <class 'PythonQt.QtCore.Version'>
     |  
     |  
     |  className = <built-in method className of PythonQt.PythonQtClassWrappe...
     |      Return the classname of the object
     |  
     |  createUuid = <unbound qt slot static_QUuid_createUuid of QUuid type>
     |      X.createUuid() -> PythonQt.QtCore.QUuid
     |  
     |  createUuidV3 = <unbound qt slot static_QUuid_createUuidV3 of QUuid typ...
     |      X.createUuidV3(a, b) -> PythonQt.QtCore.QUuid
     |  
     |  createUuidV5 = <unbound qt slot static_QUuid_createUuidV5 of QUuid typ...
     |      X.createUuidV5(a, b) -> PythonQt.QtCore.QUuid
     |  
     |  data1 = None
     |  
     |  data2 = None
     |  
     |  data3 = None
     |  
     |  delete = <built-in method delete of PythonQt.PythonQtClassWrapper obje...
     |      Deletes the given C++ object
     |  
     |  fromRfc4122 = <unbound qt slot static_QUuid_fromRfc4122 of QUuid type>
     |      X.fromRfc4122(a) -> PythonQt.QtCore.QUuid
     |  
     |  help = <built-in method help of PythonQt.PythonQtClassWrapper object>
     |      Shows the help of available methods for this class
     |  
     |  inherits = <built-in method inherits of PythonQt.PythonQtClassWrapper ...
     |      Returns if the class inherits or is of given type name
     |  
     |  isNull = <unbound qt slot isNull of QUuid type>
     |      X.isNull(a) -> bool
     |  
     |  readFrom = <unbound qt slot readFrom of QUuid type>
     |      X.readFrom(a, b)
     |  
     |  toByteArray = <unbound qt slot toByteArray of QUuid type>
     |      X.toByteArray(a) -> PythonQt.QtCore.QByteArray
     |  
     |  toRfc4122 = <unbound qt slot toRfc4122 of QUuid type>
     |      X.toRfc4122(a) -> PythonQt.QtCore.QByteArray
     |  
     |  toString = <unbound qt slot toString of QUuid type>
     |      X.toString(a) -> str
     |  
     |  variant = <unbound qt slot variant of QUuid type>
     |      X.variant(a)
     |  
     |  version = <unbound qt slot version of QUuid type>
     |      X.version(a)
     |  
     |  writeTo = <unbound qt slot writeTo of QUuid type>
     |      X.writeTo(a, b)
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __delattr__(...)
     |      x.__delattr__('name') <==> del x.name
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __hash__(...)
     |      x.__hash__() <==> hash(x)
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __setattr__(...)
     |      x.__setattr__('name', value) <==> x.name = value
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __new__ = <built-in method __new__ of PythonQt.PythonQtClassWrapper ob...
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
    
    class QVariantAnimation(PythonQt.PythonQtInstanceWrapper)
     |  Method resolution order:
     |      QVariantAnimation
     |      PythonQt.PythonQtInstanceWrapper
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  __init__(...)
     |      x.__init__(...) initializes x; see help(type(x)) for signature
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  Backward = 1
     |  
     |  DeleteWhenStopped = 1
     |  
     |  DeletionPolicy = <class 'PythonQt.QtCore.DeletionPolicy'>
     |  
     |  
     |  Direction = <class 'PythonQt.QtCore.Direction'>
     |  
     |  
     |  Forward = 0
     |  
     |  KeepWhenStopped = 0
     |  
     |  Paused = 1
     |  
     |  Running = 2
     |  
     |  State = <class 'PythonQt.QtCore.State'>
     |  
     |  
     |  Stopped = 0
     |  
     |  blockSignals = <unbound qt slot blockSignals of QVariantAnimation type...
     |      X.blockSignals(a, b) -> bool
     |  
     |  childEvent = <unbound qt slot py_q_childEvent of QVariantAnimation typ...
     |      X.childEvent(a, b)
     |  
     |  children = <unbound qt slot children of QVariantAnimation type>
     |      X.children(a) -> tuple
     |  
     |  className = <built-in method className of PythonQt.PythonQtClassWrappe...
     |      Return the classname of the object
     |  
     |  connect = <unbound qt slot connect of QVariantAnimation type>
     |      X.connect(a, b, c, d, e) -> bool
     |  
     |  currentLoop = None
     |  
     |  currentLoopChanged = <unbound qt signal currentLoopChanged of QVariant...
     |  
     |  
     |  currentLoopTime = <unbound qt slot currentLoopTime of QVariantAnimatio...
     |      X.currentLoopTime(a) -> int
     |  
     |  currentTime = None
     |  
     |  currentValue = None
     |  
     |  customEvent = <unbound qt slot py_q_customEvent of QVariantAnimation t...
     |      X.customEvent(a, b)
     |  
     |  delete = <built-in method delete of PythonQt.PythonQtClassWrapper obje...
     |      Deletes the given C++ object
     |  
     |  deleteLater = <unbound qt slot deleteLater of QVariantAnimation type>
     |      X.deleteLater()
     |  
     |  destroyed = <unbound qt signal destroyed of QVariantAnimation type>
     |  
     |  
     |  direction = None
     |  
     |  directionChanged = <unbound qt signal directionChanged of QVariantAnim...
     |  
     |  
     |  disconnect = <unbound qt slot disconnect of QVariantAnimation type>
     |      X.disconnect(a, b, c, d) -> bool
     |  
     |  dumpObjectInfo = <unbound qt slot dumpObjectInfo of QVariantAnimation ...
     |      X.dumpObjectInfo(a)
     |  
     |  dumpObjectTree = <unbound qt slot dumpObjectTree of QVariantAnimation ...
     |      X.dumpObjectTree(a)
     |  
     |  duration = None
     |  
     |  dynamicPropertyNames = <unbound qt slot dynamicPropertyNames of QVaria...
     |      X.dynamicPropertyNames(a)
     |  
     |  easingCurve = QEasingCurve (QEasingCurve at: 0x0)
     |  
     |  endValue = None
     |  
     |  event = <unbound qt slot py_q_event of QVariantAnimation type>
     |      X.event(a, b) -> bool
     |  
     |  eventFilter = <unbound qt slot py_q_eventFilter of QVariantAnimation t...
     |      X.eventFilter(a, b, c) -> bool
     |  
     |  findChild = <unbound qt slot findChild of QVariantAnimation type>
     |      X.findChild(a, b, c) -> PythonQt.private.QObject
     |  
     |  findChildren = <unbound qt slot findChildren of QVariantAnimation type...
     |      X.findChildren(a, b, c) -> tuple
     |  
     |  finished = <unbound qt signal finished of QVariantAnimation type>
     |  
     |  
     |  group = <unbound qt slot group of QVariantAnimation type>
     |      X.group(a) -> PythonQt.QtCore.QAnimationGroup
     |  
     |  help = <built-in method help of PythonQt.PythonQtClassWrapper object>
     |      Shows the help of available methods for this class
     |  
     |  inherits = <built-in method inherits of PythonQt.PythonQtClassWrapper ...
     |      Returns if the class inherits or is of given type name
     |  
     |  installEventFilter = <unbound qt slot installEventFilter of QVariantAn...
     |      X.installEventFilter(a, b)
     |  
     |  interpolated = <unbound qt slot py_q_interpolated of QVariantAnimation...
     |      X.interpolated(a, b, c, d) -> object
     |  
     |  isSignalConnected = <unbound qt slot isSignalConnected of QVariantAnim...
     |      X.isSignalConnected(a, b) -> bool
     |  
     |  isWidgetType = <unbound qt slot isWidgetType of QVariantAnimation type...
     |      X.isWidgetType(a) -> bool
     |  
     |  isWindowType = <unbound qt slot isWindowType of QVariantAnimation type...
     |      X.isWindowType(a) -> bool
     |  
     |  keyValueAt = <unbound qt slot keyValueAt of QVariantAnimation type>
     |      X.keyValueAt(a, b) -> object
     |  
     |  keyValues = <unbound qt slot keyValues of QVariantAnimation type>
     |      X.keyValues(a) -> tuple
     |  
     |  killTimer = <unbound qt slot killTimer of QVariantAnimation type>
     |      X.killTimer(a, b)
     |  
     |  loopCount = None
     |  
     |  metaObject = <unbound qt slot metaObject of QVariantAnimation type>
     |      X.metaObject(a) -> PythonQt.QtCore.QMetaObject
     |  
     |  moveToThread = <unbound qt slot moveToThread of QVariantAnimation type...
     |      X.moveToThread(a, b)
     |  
     |  objectName = None
     |  
     |  objectNameChanged = <unbound qt signal objectNameChanged of QVariantAn...
     |  
     |  
     |  parent = <unbound qt slot parent of QVariantAnimation type>
     |      X.parent(a) -> PythonQt.private.QObject
     |  
     |  pause = <unbound qt slot pause of QVariantAnimation type>
     |      X.pause()
     |  
     |  property = <unbound qt slot property of QVariantAnimation type>
     |      X.property(a, b) -> object
     |  
     |  removeEventFilter = <unbound qt slot removeEventFilter of QVariantAnim...
     |      X.removeEventFilter(a, b)
     |  
     |  resume = <unbound qt slot resume of QVariantAnimation type>
     |      X.resume()
     |  
     |  sender = <unbound qt slot sender of QVariantAnimation type>
     |      X.sender(a) -> PythonQt.private.QObject
     |  
     |  senderSignalIndex = <unbound qt slot senderSignalIndex of QVariantAnim...
     |      X.senderSignalIndex(a) -> int
     |  
     |  setCurrentTime = <unbound qt slot setCurrentTime of QVariantAnimation ...
     |      X.setCurrentTime(a)
     |  
     |  setDirection = <unbound qt slot setDirection of QVariantAnimation type...
     |      X.setDirection(a, b)
     |  
     |  setDuration = <unbound qt slot setDuration of QVariantAnimation type>
     |      X.setDuration(a, b)
     |  
     |  setEasingCurve = <unbound qt slot setEasingCurve of QVariantAnimation ...
     |      X.setEasingCurve(a, b)
     |  
     |  setEndValue = <unbound qt slot setEndValue of QVariantAnimation type>
     |      X.setEndValue(a, b)
     |  
     |  setKeyValueAt = <unbound qt slot setKeyValueAt of QVariantAnimation ty...
     |      X.setKeyValueAt(a, b, c)
     |  
     |  setKeyValues = <unbound qt slot setKeyValues of QVariantAnimation type...
     |      X.setKeyValues(a, b)
     |  
     |  setLoopCount = <unbound qt slot setLoopCount of QVariantAnimation type...
     |      X.setLoopCount(a, b)
     |  
     |  setObjectName = <unbound qt slot setObjectName of QVariantAnimation ty...
     |      X.setObjectName(a, b)
     |  
     |  setParent = <unbound qt slot setParent of QVariantAnimation type>
     |      X.setParent(a, b)
     |  
     |  setPaused = <unbound qt slot setPaused of QVariantAnimation type>
     |      X.setPaused(a)
     |  
     |  setProperty = <unbound qt slot setProperty of QVariantAnimation type>
     |      X.setProperty(a, b, c) -> bool
     |  
     |  setStartValue = <unbound qt slot setStartValue of QVariantAnimation ty...
     |      X.setStartValue(a, b)
     |  
     |  signalsBlocked = <unbound qt slot signalsBlocked of QVariantAnimation ...
     |      X.signalsBlocked(a) -> bool
     |  
     |  start = <unbound qt slot start of QVariantAnimation type>
     |      X.start(a)
     |  
     |  startTimer = <unbound qt slot startTimer of QVariantAnimation type>
     |      X.startTimer(a, b, c) -> int
     |  
     |  startValue = None
     |  
     |  state = None
     |  
     |  stateChanged = <unbound qt signal stateChanged of QVariantAnimation ty...
     |  
     |  
     |  stop = <unbound qt slot stop of QVariantAnimation type>
     |      X.stop()
     |  
     |  thread = <unbound qt slot thread of QVariantAnimation type>
     |      X.thread(a)
     |  
     |  timerEvent = <unbound qt slot py_q_timerEvent of QVariantAnimation typ...
     |      X.timerEvent(a, b)
     |  
     |  totalDuration = <unbound qt slot totalDuration of QVariantAnimation ty...
     |      X.totalDuration(a) -> int
     |  
     |  tr = <unbound qt slot tr of QVariantAnimation type>
     |      X.tr(a, b, c, d) -> str
     |  
     |  updateCurrentTime = <unbound qt slot py_q_updateCurrentTime of QVarian...
     |      X.updateCurrentTime(a, b)
     |  
     |  updateCurrentValue = <unbound qt slot py_q_updateCurrentValue of QVari...
     |      X.updateCurrentValue(a, b)
     |  
     |  updateDirection = <unbound qt slot py_q_updateDirection of QVariantAni...
     |      X.updateDirection(a, b)
     |  
     |  updateState = <unbound qt slot py_q_updateState of QVariantAnimation t...
     |      X.updateState(a, b, c)
     |  
     |  valueChanged = <unbound qt signal valueChanged of QVariantAnimation ty...
     |  
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __delattr__(...)
     |      x.__delattr__('name') <==> del x.name
     |  
     |  __eq__(...)
     |      x.__eq__(y) <==> x==y
     |  
     |  __ge__(...)
     |      x.__ge__(y) <==> x>=y
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __gt__(...)
     |      x.__gt__(y) <==> x>y
     |  
     |  __hash__(...)
     |      x.__hash__() <==> hash(x)
     |  
     |  __le__(...)
     |      x.__le__(y) <==> x<=y
     |  
     |  __lt__(...)
     |      x.__lt__(y) <==> x<y
     |  
     |  __ne__(...)
     |      x.__ne__(y) <==> x!=y
     |  
     |  __nonzero__(...)
     |      x.__nonzero__() <==> x != 0
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __setattr__(...)
     |      x.__setattr__('name', value) <==> x.name = value
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __new__ = <built-in method __new__ of PythonQt.PythonQtClassWrapper ob...
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
    
    class QWaitCondition(PythonQt.PythonQtInstanceWrapper)
     |  Method resolution order:
     |      QWaitCondition
     |      PythonQt.PythonQtInstanceWrapper
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  __init__(...)
     |      x.__init__(...) initializes x; see help(type(x)) for signature
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  className = <built-in method className of PythonQt.PythonQtClassWrappe...
     |      Return the classname of the object
     |  
     |  delete = <built-in method delete of PythonQt.PythonQtClassWrapper obje...
     |      Deletes the given C++ object
     |  
     |  help = <built-in method help of PythonQt.PythonQtClassWrapper object>
     |      Shows the help of available methods for this class
     |  
     |  inherits = <built-in method inherits of PythonQt.PythonQtClassWrapper ...
     |      Returns if the class inherits or is of given type name
     |  
     |  wait = <unbound qt slot wait of QWaitCondition type>
     |      X.wait(a, b, c) -> bool
     |  
     |  wakeAll = <unbound qt slot wakeAll of QWaitCondition type>
     |      X.wakeAll(a)
     |  
     |  wakeOne = <unbound qt slot wakeOne of QWaitCondition type>
     |      X.wakeOne(a)
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __delattr__(...)
     |      x.__delattr__('name') <==> del x.name
     |  
     |  __eq__(...)
     |      x.__eq__(y) <==> x==y
     |  
     |  __ge__(...)
     |      x.__ge__(y) <==> x>=y
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __gt__(...)
     |      x.__gt__(y) <==> x>y
     |  
     |  __hash__(...)
     |      x.__hash__() <==> hash(x)
     |  
     |  __le__(...)
     |      x.__le__(y) <==> x<=y
     |  
     |  __lt__(...)
     |      x.__lt__(y) <==> x<y
     |  
     |  __ne__(...)
     |      x.__ne__(y) <==> x!=y
     |  
     |  __nonzero__(...)
     |      x.__nonzero__() <==> x != 0
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __setattr__(...)
     |      x.__setattr__('name', value) <==> x.name = value
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __new__ = <built-in method __new__ of PythonQt.PythonQtClassWrapper ob...
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
    
    class QXmlStreamEntityResolver(PythonQt.PythonQtInstanceWrapper)
     |  Method resolution order:
     |      QXmlStreamEntityResolver
     |      PythonQt.PythonQtInstanceWrapper
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  __init__(...)
     |      x.__init__(...) initializes x; see help(type(x)) for signature
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  className = <built-in method className of PythonQt.PythonQtClassWrappe...
     |      Return the classname of the object
     |  
     |  delete = <built-in method delete of PythonQt.PythonQtClassWrapper obje...
     |      Deletes the given C++ object
     |  
     |  help = <built-in method help of PythonQt.PythonQtClassWrapper object>
     |      Shows the help of available methods for this class
     |  
     |  inherits = <built-in method inherits of PythonQt.PythonQtClassWrapper ...
     |      Returns if the class inherits or is of given type name
     |  
     |  resolveEntity = <unbound qt slot py_q_resolveEntity of QXmlStreamEntit...
     |      X.resolveEntity(a, b, c) -> str
     |  
     |  resolveUndeclaredEntity = <unbound qt slot py_q_resolveUndeclaredEntit...
     |      X.resolveUndeclaredEntity(a, b) -> str
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __delattr__(...)
     |      x.__delattr__('name') <==> del x.name
     |  
     |  __eq__(...)
     |      x.__eq__(y) <==> x==y
     |  
     |  __ge__(...)
     |      x.__ge__(y) <==> x>=y
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __gt__(...)
     |      x.__gt__(y) <==> x>y
     |  
     |  __hash__(...)
     |      x.__hash__() <==> hash(x)
     |  
     |  __le__(...)
     |      x.__le__(y) <==> x<=y
     |  
     |  __lt__(...)
     |      x.__lt__(y) <==> x<y
     |  
     |  __ne__(...)
     |      x.__ne__(y) <==> x!=y
     |  
     |  __nonzero__(...)
     |      x.__nonzero__() <==> x != 0
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __setattr__(...)
     |      x.__setattr__('name', value) <==> x.name = value
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __new__ = <built-in method __new__ of PythonQt.PythonQtClassWrapper ob...
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
    
    class Qt(PythonQt.PythonQtInstanceWrapper)
     |  Method resolution order:
     |      Qt
     |      PythonQt.PythonQtInstanceWrapper
     |      __builtin__.object
     |  
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  AA_AttributeCount = 28
     |  
     |  AA_DisableHighDpiScaling = 21
     |  
     |  AA_DontCreateNativeWidgetSiblings = 4
     |  
     |  AA_DontShowIconsInMenus = 2
     |  
     |  AA_DontUseNativeMenuBar = 6
     |  
     |  AA_EnableHighDpiScaling = 20
     |  
     |  AA_ForceRasterWidgets = 14
     |  
     |  AA_ImmediateWidgetCreation = 0
     |  
     |  AA_MSWindowsUseDirect3DByDefault = 1
     |  
     |  AA_MacDontSwapCtrlAndMeta = 7
     |  
     |  AA_MacPluginApplication = 5
     |  
     |  AA_NativeWindows = 3
     |  
     |  AA_SetPalette = 19
     |  
     |  AA_ShareOpenGLContexts = 18
     |  
     |  AA_SynthesizeMouseForUnhandledTouchEvents = 12
     |  
     |  AA_SynthesizeTouchForUnhandledMouseEvents = 11
     |  
     |  AA_Use96Dpi = 8
     |  
     |  AA_UseDesktopOpenGL = 15
     |  
     |  AA_UseHighDpiPixmaps = 13
     |  
     |  AA_UseOpenGLES = 16
     |  
     |  AA_UseSoftwareOpenGL = 17
     |  
     |  AA_X11InitThreads = 10
     |  
     |  AbsoluteSize = 0
     |  
     |  AccessibleDescriptionRole = 12
     |  
     |  AccessibleTextRole = 11
     |  
     |  ActionMask = 255
     |  
     |  ActionsContextMenu = 2
     |  
     |  ActiveWindowFocusReason = 3
     |  
     |  AddToSelection = 1
     |  
     |  AlignAbsolute = 16
     |  
     |  AlignBaseline = 256
     |  
     |  AlignBottom = 64
     |  
     |  AlignCenter = 132
     |  
     |  AlignHCenter = 4
     |  
     |  AlignHorizontal_Mask = 31
     |  
     |  AlignJustify = 8
     |  
     |  AlignLeading = 1
     |  
     |  AlignLeft = 1
     |  
     |  AlignRight = 2
     |  
     |  AlignTop = 32
     |  
     |  AlignTrailing = 2
     |  
     |  AlignVCenter = 128
     |  
     |  AlignVertical_Mask = 480
     |  
     |  Alignment = <class 'PythonQt.QtCore.Alignment'>
     |  
     |  
     |  AlignmentFlag = <class 'PythonQt.QtCore.AlignmentFlag'>
     |  
     |  
     |  AllButtons = 134217727
     |  
     |  AllDockWidgetAreas = 15
     |  
     |  AllToolBarAreas = 15
     |  
     |  AlphaDither_Mask = 12
     |  
     |  AltModifier = 134217728
     |  
     |  AnchorBottom = 5
     |  
     |  AnchorHorizontalCenter = 1
     |  
     |  AnchorLeft = 0
     |  
     |  AnchorPoint = <class 'PythonQt.QtCore.AnchorPoint'>
     |  
     |  
     |  AnchorRight = 2
     |  
     |  AnchorTop = 3
     |  
     |  AnchorVerticalCenter = 4
     |  
     |  ApplicationActive = 4
     |  
     |  ApplicationAttribute = <class 'PythonQt.QtCore.ApplicationAttribute'>
     |  
     |  
     |  ApplicationHidden = 1
     |  
     |  ApplicationInactive = 2
     |  
     |  ApplicationModal = 2
     |  
     |  ApplicationShortcut = 2
     |  
     |  ApplicationState = <class 'PythonQt.QtCore.ApplicationState'>
     |  
     |  
     |  ApplicationSuspended = 0
     |  
     |  ArrowCursor = 0
     |  
     |  ArrowType = <class 'PythonQt.QtCore.ArrowType'>
     |  
     |  
     |  AscendingOrder = 0
     |  
     |  AspectRatioMode = <class 'PythonQt.QtCore.AspectRatioMode'>
     |  
     |  
     |  AutoColor = 0
     |  
     |  AutoConnection = 0
     |  
     |  AutoDither = 0
     |  
     |  AutoText = 2
     |  
     |  AvoidDither = 128
     |  
     |  Axis = <class 'PythonQt.QtCore.Axis'>
     |  
     |  
     |  BDiagPattern = 12
     |  
     |  BGMode = <class 'PythonQt.QtCore.BGMode'>
     |  
     |  
     |  BackButton = 8
     |  
     |  BackgroundColorRole = 8
     |  
     |  BackgroundRole = 8
     |  
     |  BacktabFocusReason = 2
     |  
     |  BeginNativeGesture = 0
     |  
     |  BevelJoin = 64
     |  
     |  BitmapCursor = 24
     |  
     |  BlankCursor = 10
     |  
     |  BlockingQueuedConnection = 3
     |  
     |  BottomDockWidgetArea = 8
     |  
     |  BottomEdge = 8
     |  
     |  BottomLeftCorner = 2
     |  
     |  BottomLeftSection = 8
     |  
     |  BottomRightCorner = 3
     |  
     |  BottomRightSection = 6
     |  
     |  BottomSection = 7
     |  
     |  BottomToolBarArea = 8
     |  
     |  BrushStyle = <class 'PythonQt.QtCore.BrushStyle'>
     |  
     |  
     |  BusyCursor = 16
     |  
     |  BypassGraphicsProxyWidget = 536870912
     |  
     |  BypassWindowManagerHint = 1024
     |  
     |  CaseInsensitive = 0
     |  
     |  CaseSensitive = 1
     |  
     |  CaseSensitivity = <class 'PythonQt.QtCore.CaseSensitivity'>
     |  
     |  
     |  CheckState = <class 'PythonQt.QtCore.CheckState'>
     |  
     |  
     |  CheckStateRole = 10
     |  
     |  Checked = 2
     |  
     |  ClickFocus = 2
     |  
     |  ClipOperation = <class 'PythonQt.QtCore.ClipOperation'>
     |  
     |  
     |  ClosedHandCursor = 18
     |  
     |  CoarseTimer = 1
     |  
     |  ColorMode_Mask = 3
     |  
     |  ColorOnly = 3
     |  
     |  ConicalGradientPattern = 17
     |  
     |  ConnectionType = <class 'PythonQt.QtCore.ConnectionType'>
     |  
     |  
     |  ContainsItemBoundingRect = 2
     |  
     |  ContainsItemShape = 0
     |  
     |  ContextMenuPolicy = <class 'PythonQt.QtCore.ContextMenuPolicy'>
     |  
     |  
     |  ControlModifier = 67108864
     |  
     |  CoordinateSystem = <class 'PythonQt.QtCore.CoordinateSystem'>
     |  
     |  
     |  CopyAction = 1
     |  
     |  Corner = <class 'PythonQt.QtCore.Corner'>
     |  
     |  
     |  CoverWindow = 65
     |  
     |  CrossCursor = 2
     |  
     |  CrossPattern = 11
     |  
     |  CursorMoveStyle = <class 'PythonQt.QtCore.CursorMoveStyle'>
     |  
     |  
     |  CursorShape = <class 'PythonQt.QtCore.CursorShape'>
     |  
     |  
     |  CustomContextMenu = 3
     |  
     |  CustomCursor = 25
     |  
     |  CustomDashLine = 6
     |  
     |  CustomGesture = 256
     |  
     |  CustomizeWindowHint = 33554432
     |  
     |  DashDotDotLine = 5
     |  
     |  DashDotLine = 4
     |  
     |  DashLine = 2
     |  
     |  DateFormat = <class 'PythonQt.QtCore.DateFormat'>
     |  
     |  
     |  DayOfWeek = <class 'PythonQt.QtCore.DayOfWeek'>
     |  
     |  
     |  DecorationPropertyRole = 28
     |  
     |  DecorationRole = 1
     |  
     |  DefaultContextMenu = 1
     |  
     |  DefaultLocaleLongDate = 7
     |  
     |  DefaultLocaleShortDate = 6
     |  
     |  Dense1Pattern = 2
     |  
     |  Dense2Pattern = 3
     |  
     |  Dense3Pattern = 4
     |  
     |  Dense4Pattern = 5
     |  
     |  Dense5Pattern = 6
     |  
     |  Dense6Pattern = 7
     |  
     |  Dense7Pattern = 8
     |  
     |  DescendingOrder = 1
     |  
     |  Desktop = 17
     |  
     |  DeviceCoordinates = 0
     |  
     |  DiagCrossPattern = 14
     |  
     |  Dialog = 3
     |  
     |  DiffuseAlphaDither = 8
     |  
     |  DiffuseDither = 0
     |  
     |  DirectConnection = 1
     |  
     |  DisplayPropertyRole = 27
     |  
     |  DisplayRole = 0
     |  
     |  DitherMode_Mask = 192
     |  
     |  Dither_Mask = 48
     |  
     |  DockWidgetArea = <class 'PythonQt.QtCore.DockWidgetArea'>
     |  
     |  
     |  DockWidgetAreaSizes = <class 'PythonQt.QtCore.DockWidgetAreaSizes'>
     |  
     |  
     |  DockWidgetArea_Mask = 15
     |  
     |  DockWidgetAreas = <class 'PythonQt.QtCore.DockWidgetAreas'>
     |  
     |  
     |  DontStartGestureOnChildren = 1
     |  
     |  DotLine = 3
     |  
     |  DownArrow = 2
     |  
     |  DragCopyCursor = 19
     |  
     |  DragLinkCursor = 21
     |  
     |  DragMoveCursor = 20
     |  
     |  Drawer = 7
     |  
     |  DropAction = <class 'PythonQt.QtCore.DropAction'>
     |  
     |  
     |  DropActions = <class 'PythonQt.QtCore.DropActions'>
     |  
     |  
     |  Edge = <class 'PythonQt.QtCore.Edge'>
     |  
     |  
     |  EditRole = 2
     |  
     |  ElideLeft = 0
     |  
     |  ElideMiddle = 2
     |  
     |  ElideNone = 3
     |  
     |  ElideRight = 1
     |  
     |  EndNativeGesture = 1
     |  
     |  EnterKeyDefault = 0
     |  
     |  EnterKeyDone = 2
     |  
     |  EnterKeyGo = 3
     |  
     |  EnterKeyNext = 6
     |  
     |  EnterKeyPrevious = 7
     |  
     |  EnterKeyReturn = 1
     |  
     |  EnterKeySearch = 5
     |  
     |  EnterKeySend = 4
     |  
     |  EnterKeyType = <class 'PythonQt.QtCore.EnterKeyType'>
     |  
     |  
     |  EventPriority = <class 'PythonQt.QtCore.EventPriority'>
     |  
     |  
     |  ExactHit = 0
     |  
     |  ExtraButton1 = 8
     |  
     |  ExtraButton10 = 4096
     |  
     |  ExtraButton11 = 8192
     |  
     |  ExtraButton12 = 16384
     |  
     |  ExtraButton13 = 32768
     |  
     |  ExtraButton14 = 65536
     |  
     |  ExtraButton15 = 131072
     |  
     |  ExtraButton16 = 262144
     |  
     |  ExtraButton17 = 524288
     |  
     |  ExtraButton18 = 1048576
     |  
     |  ExtraButton19 = 2097152
     |  
     |  ExtraButton2 = 16
     |  
     |  ExtraButton20 = 4194304
     |  
     |  ExtraButton21 = 8388608
     |  
     |  ExtraButton22 = 16777216
     |  
     |  ExtraButton23 = 33554432
     |  
     |  ExtraButton24 = 67108864
     |  
     |  ExtraButton3 = 32
     |  
     |  ExtraButton4 = 64
     |  
     |  ExtraButton5 = 128
     |  
     |  ExtraButton6 = 256
     |  
     |  ExtraButton7 = 512
     |  
     |  ExtraButton8 = 1024
     |  
     |  ExtraButton9 = 2048
     |  
     |  FDiagPattern = 13
     |  
     |  FastTransformation = 0
     |  
     |  FillRule = <class 'PythonQt.QtCore.FillRule'>
     |  
     |  
     |  FindChildOption = <class 'PythonQt.QtCore.FindChildOption'>
     |  
     |  
     |  FindChildOptions = <class 'PythonQt.QtCore.FindChildOptions'>
     |  
     |  
     |  FindChildrenRecursively = 1
     |  
     |  FindDirectChildrenOnly = 0
     |  
     |  FlatCap = 0
     |  
     |  FocusPolicy = <class 'PythonQt.QtCore.FocusPolicy'>
     |  
     |  
     |  FocusReason = <class 'PythonQt.QtCore.FocusReason'>
     |  
     |  
     |  FontRole = 6
     |  
     |  ForbiddenCursor = 14
     |  
     |  ForegroundRole = 9
     |  
     |  ForeignWindow = 33
     |  
     |  ForwardButton = 16
     |  
     |  FramelessWindowHint = 2048
     |  
     |  Friday = 5
     |  
     |  FuzzyHit = 1
     |  
     |  GestureCanceled = 4
     |  
     |  GestureFinished = 3
     |  
     |  GestureFlag = <class 'PythonQt.QtCore.GestureFlag'>
     |  
     |  
     |  GestureFlags = <class 'PythonQt.QtCore.GestureFlags'>
     |  
     |  
     |  GestureStarted = 1
     |  
     |  GestureState = <class 'PythonQt.QtCore.GestureState'>
     |  
     |  
     |  GestureType = <class 'PythonQt.QtCore.GestureType'>
     |  
     |  
     |  GestureUpdated = 2
     |  
     |  GlobalColor = <class 'PythonQt.QtCore.GlobalColor'>
     |  
     |  
     |  GroupSwitchModifier = 1073741824
     |  
     |  HighEventPriority = 1
     |  
     |  HitTestAccuracy = <class 'PythonQt.QtCore.HitTestAccuracy'>
     |  
     |  
     |  HorPattern = 9
     |  
     |  Horizontal = 1
     |  
     |  IBeamCursor = 4
     |  
     |  ISODate = 1
     |  
     |  IgnoreAction = 0
     |  
     |  IgnoreAspectRatio = 0
     |  
     |  IgnoredGesturesPropagateToParent = 4
     |  
     |  ImAbsolutePosition = 1024
     |  
     |  ImAnchorPosition = 128
     |  
     |  ImCurrentSelection = 32
     |  
     |  ImCursorPosition = 8
     |  
     |  ImCursorRectangle = 2
     |  
     |  ImEnabled = 1
     |  
     |  ImEnterKeyType = 8192
     |  
     |  ImFont = 4
     |  
     |  ImHints = 256
     |  
     |  ImMaximumTextLength = 64
     |  
     |  ImMicroFocus = 2
     |  
     |  ImPlatformData = -2147483648
     |  
     |  ImPreferredLanguage = 512
     |  
     |  ImQueryAll = -1
     |  
     |  ImQueryInput = 16570
     |  
     |  ImSurroundingText = 16
     |  
     |  ImTextAfterCursor = 4096
     |  
     |  ImTextBeforeCursor = 2048
     |  
     |  ImageConversionFlag = <class 'PythonQt.QtCore.ImageConversionFlag'>
     |  
     |  
     |  ImageConversionFlags = <class 'PythonQt.QtCore.ImageConversionFlags'>
     |  
     |  
     |  ImhDate = 128
     |  
     |  ImhDialableCharactersOnly = 1048576
     |  
     |  ImhDigitsOnly = 65536
     |  
     |  ImhEmailCharactersOnly = 2097152
     |  
     |  ImhExclusiveInputMask = -65536
     |  
     |  ImhFormattedNumbersOnly = 131072
     |  
     |  ImhHiddenText = 1
     |  
     |  ImhLatinOnly = 8388608
     |  
     |  ImhLowercaseOnly = 524288
     |  
     |  ImhMultiLine = 1024
     |  
     |  ImhNoAutoUppercase = 4
     |  
     |  ImhNoPredictiveText = 64
     |  
     |  ImhNone = 0
     |  
     |  ImhPreferLatin = 512
     |  
     |  ImhPreferLowercase = 32
     |  
     |  ImhPreferNumbers = 8
     |  
     |  ImhPreferUppercase = 16
     |  
     |  ImhSensitiveData = 2
     |  
     |  ImhTime = 256
     |  
     |  ImhUppercaseOnly = 262144
     |  
     |  ImhUrlCharactersOnly = 4194304
     |  
     |  InitialSortOrderRole = 14
     |  
     |  InputMethodHint = <class 'PythonQt.QtCore.InputMethodHint'>
     |  
     |  
     |  InputMethodHints = <class 'PythonQt.QtCore.InputMethodHints'>
     |  
     |  
     |  InputMethodQueries = <class 'PythonQt.QtCore.InputMethodQueries'>
     |  
     |  
     |  InputMethodQuery = <class 'PythonQt.QtCore.InputMethodQuery'>
     |  
     |  
     |  IntersectClip = 2
     |  
     |  IntersectsItemBoundingRect = 3
     |  
     |  IntersectsItemShape = 1
     |  
     |  InvertedLandscapeOrientation = 8
     |  
     |  InvertedPortraitOrientation = 4
     |  
     |  ItemDataRole = <class 'PythonQt.QtCore.ItemDataRole'>
     |  
     |  
     |  ItemFlag = <class 'PythonQt.QtCore.ItemFlag'>
     |  
     |  
     |  ItemFlags = <class 'PythonQt.QtCore.ItemFlags'>
     |  
     |  
     |  ItemIsAutoTristate = 64
     |  
     |  ItemIsDragEnabled = 4
     |  
     |  ItemIsDropEnabled = 8
     |  
     |  ItemIsEditable = 2
     |  
     |  ItemIsEnabled = 32
     |  
     |  ItemIsSelectable = 1
     |  
     |  ItemIsTristate = 64
     |  
     |  ItemIsUserCheckable = 16
     |  
     |  ItemIsUserTristate = 256
     |  
     |  ItemNeverHasChildren = 128
     |  
     |  ItemSelectionMode = <class 'PythonQt.QtCore.ItemSelectionMode'>
     |  
     |  
     |  ItemSelectionOperation = <class 'PythonQt.QtCore.ItemSelectionOperatio...
     |  
     |  
     |  KeepAspectRatio = 1
     |  
     |  KeepAspectRatioByExpanding = 2
     |  
     |  Key = <class 'PythonQt.QtCore.Key'>
     |  
     |  
     |  Key_0 = 48
     |  
     |  Key_1 = 49
     |  
     |  Key_2 = 50
     |  
     |  Key_3 = 51
     |  
     |  Key_4 = 52
     |  
     |  Key_5 = 53
     |  
     |  Key_6 = 54
     |  
     |  Key_7 = 55
     |  
     |  Key_8 = 56
     |  
     |  Key_9 = 57
     |  
     |  Key_A = 65
     |  
     |  Key_AE = 198
     |  
     |  Key_Aacute = 193
     |  
     |  Key_Acircumflex = 194
     |  
     |  Key_AddFavorite = 16777408
     |  
     |  Key_Adiaeresis = 196
     |  
     |  Key_Agrave = 192
     |  
     |  Key_Alt = 16777251
     |  
     |  Key_AltGr = 16781571
     |  
     |  Key_Ampersand = 38
     |  
     |  Key_Any = 32
     |  
     |  Key_Apostrophe = 39
     |  
     |  Key_ApplicationLeft = 16777415
     |  
     |  Key_ApplicationRight = 16777416
     |  
     |  Key_Aring = 197
     |  
     |  Key_AsciiCircum = 94
     |  
     |  Key_AsciiTilde = 126
     |  
     |  Key_Asterisk = 42
     |  
     |  Key_At = 64
     |  
     |  Key_Atilde = 195
     |  
     |  Key_AudioCycleTrack = 16777478
     |  
     |  Key_AudioForward = 16777474
     |  
     |  Key_AudioRandomPlay = 16777476
     |  
     |  Key_AudioRepeat = 16777475
     |  
     |  Key_AudioRewind = 16777413
     |  
     |  Key_Away = 16777464
     |  
     |  Key_B = 66
     |  
     |  Key_Back = 16777313
     |  
     |  Key_BackForward = 16777414
     |  
     |  Key_Backslash = 92
     |  
     |  Key_Backspace = 16777219
     |  
     |  Key_Backtab = 16777218
     |  
     |  Key_Bar = 124
     |  
     |  Key_BassBoost = 16777331
     |  
     |  Key_BassDown = 16777333
     |  
     |  Key_BassUp = 16777332
     |  
     |  Key_Battery = 16777470
     |  
     |  Key_Blue = 16777495
     |  
     |  Key_Bluetooth = 16777471
     |  
     |  Key_Book = 16777417
     |  
     |  Key_BraceLeft = 123
     |  
     |  Key_BraceRight = 125
     |  
     |  Key_BracketLeft = 91
     |  
     |  Key_BracketRight = 93
     |  
     |  Key_BrightnessAdjust = 16777410
     |  
     |  Key_C = 67
     |  
     |  Key_CD = 16777418
     |  
     |  Key_Calculator = 16777419
     |  
     |  Key_Calendar = 16777444
     |  
     |  Key_Call = 17825796
     |  
     |  Key_Camera = 17825824
     |  
     |  Key_CameraFocus = 17825825
     |  
     |  Key_Cancel = 16908289
     |  
     |  Key_CapsLock = 16777252
     |  
     |  Key_Ccedilla = 199
     |  
     |  Key_ChannelDown = 16777497
     |  
     |  Key_ChannelUp = 16777496
     |  
     |  Key_Clear = 16777227
     |  
     |  Key_ClearGrab = 16777421
     |  
     |  Key_Close = 16777422
     |  
     |  Key_Codeinput = 16781623
     |  
     |  Key_Colon = 58
     |  
     |  Key_Comma = 44
     |  
     |  Key_Community = 16777412
     |  
     |  Key_Context1 = 17825792
     |  
     |  Key_Context2 = 17825793
     |  
     |  Key_Context3 = 17825794
     |  
     |  Key_Context4 = 17825795
     |  
     |  Key_ContrastAdjust = 16777485
     |  
     |  Key_Control = 16777249
     |  
     |  Key_Copy = 16777423
     |  
     |  Key_Cut = 16777424
     |  
     |  Key_D = 68
     |  
     |  Key_DOS = 16777426
     |  
     |  Key_Dead_Abovedot = 16781910
     |  
     |  Key_Dead_Abovering = 16781912
     |  
     |  Key_Dead_Acute = 16781905
     |  
     |  Key_Dead_Belowdot = 16781920
     |  
     |  Key_Dead_Breve = 16781909
     |  
     |  Key_Dead_Caron = 16781914
     |  
     |  Key_Dead_Cedilla = 16781915
     |  
     |  Key_Dead_Circumflex = 16781906
     |  
     |  Key_Dead_Diaeresis = 16781911
     |  
     |  Key_Dead_Doubleacute = 16781913
     |  
     |  Key_Dead_Grave = 16781904
     |  
     |  Key_Dead_Hook = 16781921
     |  
     |  Key_Dead_Horn = 16781922
     |  
     |  Key_Dead_Iota = 16781917
     |  
     |  Key_Dead_Macron = 16781908
     |  
     |  Key_Dead_Ogonek = 16781916
     |  
     |  Key_Dead_Semivoiced_Sound = 16781919
     |  
     |  Key_Dead_Tilde = 16781907
     |  
     |  Key_Dead_Voiced_Sound = 16781918
     |  
     |  Key_Delete = 16777223
     |  
     |  Key_Direction_L = 16777305
     |  
     |  Key_Direction_R = 16777312
     |  
     |  Key_Display = 16777425
     |  
     |  Key_Documents = 16777427
     |  
     |  Key_Dollar = 36
     |  
     |  Key_Down = 16777237
     |  
     |  Key_E = 69
     |  
     |  Key_ETH = 208
     |  
     |  Key_Eacute = 201
     |  
     |  Key_Ecircumflex = 202
     |  
     |  Key_Ediaeresis = 203
     |  
     |  Key_Egrave = 200
     |  
     |  Key_Eisu_Shift = 16781615
     |  
     |  Key_Eisu_toggle = 16781616
     |  
     |  Key_Eject = 16777401
     |  
     |  Key_End = 16777233
     |  
     |  Key_Enter = 16777221
     |  
     |  Key_Equal = 61
     |  
     |  Key_Escape = 16777216
     |  
     |  Key_Excel = 16777428
     |  
     |  Key_Exclam = 33
     |  
     |  Key_Execute = 16908291
     |  
     |  Key_Exit = 16908298
     |  
     |  Key_Explorer = 16777429
     |  
     |  Key_F = 70
     |  
     |  Key_F1 = 16777264
     |  
     |  Key_F10 = 16777273
     |  
     |  Key_F11 = 16777274
     |  
     |  Key_F12 = 16777275
     |  
     |  Key_F13 = 16777276
     |  
     |  Key_F14 = 16777277
     |  
     |  Key_F15 = 16777278
     |  
     |  Key_F16 = 16777279
     |  
     |  Key_F17 = 16777280
     |  
     |  Key_F18 = 16777281
     |  
     |  Key_F19 = 16777282
     |  
     |  Key_F2 = 16777265
     |  
     |  Key_F20 = 16777283
     |  
     |  Key_F21 = 16777284
     |  
     |  Key_F22 = 16777285
     |  
     |  Key_F23 = 16777286
     |  
     |  Key_F24 = 16777287
     |  
     |  Key_F25 = 16777288
     |  
     |  Key_F26 = 16777289
     |  
     |  Key_F27 = 16777290
     |  
     |  Key_F28 = 16777291
     |  
     |  Key_F29 = 16777292
     |  
     |  Key_F3 = 16777266
     |  
     |  Key_F30 = 16777293
     |  
     |  Key_F31 = 16777294
     |  
     |  Key_F32 = 16777295
     |  
     |  Key_F33 = 16777296
     |  
     |  Key_F34 = 16777297
     |  
     |  Key_F35 = 16777298
     |  
     |  Key_F4 = 16777267
     |  
     |  Key_F5 = 16777268
     |  
     |  Key_F6 = 16777269
     |  
     |  Key_F7 = 16777270
     |  
     |  Key_F8 = 16777271
     |  
     |  Key_F9 = 16777272
     |  
     |  Key_Favorites = 16777361
     |  
     |  Key_Finance = 16777411
     |  
     |  Key_Find = 16777506
     |  
     |  Key_Flip = 17825798
     |  
     |  Key_Forward = 16777314
     |  
     |  Key_G = 71
     |  
     |  Key_Game = 16777430
     |  
     |  Key_Go = 16777431
     |  
     |  Key_Greater = 62
     |  
     |  Key_Green = 16777493
     |  
     |  Key_Guide = 16777498
     |  
     |  Key_H = 72
     |  
     |  Key_Hangul = 16781617
     |  
     |  Key_Hangul_Banja = 16781625
     |  
     |  Key_Hangul_End = 16781619
     |  
     |  Key_Hangul_Hanja = 16781620
     |  
     |  Key_Hangul_Jamo = 16781621
     |  
     |  Key_Hangul_Jeonja = 16781624
     |  
     |  Key_Hangul_PostHanja = 16781627
     |  
     |  Key_Hangul_PreHanja = 16781626
     |  
     |  Key_Hangul_Romaja = 16781622
     |  
     |  Key_Hangul_Special = 16781631
     |  
     |  Key_Hangul_Start = 16781618
     |  
     |  Key_Hangup = 17825797
     |  
     |  Key_Hankaku = 16781609
     |  
     |  Key_Help = 16777304
     |  
     |  Key_Henkan = 16781603
     |  
     |  Key_Hibernate = 16777480
     |  
     |  Key_Hiragana = 16781605
     |  
     |  Key_Hiragana_Katakana = 16781607
     |  
     |  Key_History = 16777407
     |  
     |  Key_Home = 16777232
     |  
     |  Key_HomePage = 16777360
     |  
     |  Key_HotLinks = 16777409
     |  
     |  Key_Hyper_L = 16777302
     |  
     |  Key_Hyper_R = 16777303
     |  
     |  Key_I = 73
     |  
     |  Key_Iacute = 205
     |  
     |  Key_Icircumflex = 206
     |  
     |  Key_Idiaeresis = 207
     |  
     |  Key_Igrave = 204
     |  
     |  Key_Info = 16777499
     |  
     |  Key_Insert = 16777222
     |  
     |  Key_J = 74
     |  
     |  Key_K = 75
     |  
     |  Key_Kana_Lock = 16781613
     |  
     |  Key_Kana_Shift = 16781614
     |  
     |  Key_Kanji = 16781601
     |  
     |  Key_Katakana = 16781606
     |  
     |  Key_KeyboardBrightnessDown = 16777398
     |  
     |  Key_KeyboardBrightnessUp = 16777397
     |  
     |  Key_KeyboardLightOnOff = 16777396
     |  
     |  Key_L = 76
     |  
     |  Key_LastNumberRedial = 17825801
     |  
     |  Key_Launch0 = 16777378
     |  
     |  Key_Launch1 = 16777379
     |  
     |  Key_Launch2 = 16777380
     |  
     |  Key_Launch3 = 16777381
     |  
     |  Key_Launch4 = 16777382
     |  
     |  Key_Launch5 = 16777383
     |  
     |  Key_Launch6 = 16777384
     |  
     |  Key_Launch7 = 16777385
     |  
     |  Key_Launch8 = 16777386
     |  
     |  Key_Launch9 = 16777387
     |  
     |  Key_LaunchA = 16777388
     |  
     |  Key_LaunchB = 16777389
     |  
     |  Key_LaunchC = 16777390
     |  
     |  Key_LaunchD = 16777391
     |  
     |  Key_LaunchE = 16777392
     |  
     |  Key_LaunchF = 16777393
     |  
     |  Key_LaunchG = 16777486
     |  
     |  Key_LaunchH = 16777487
     |  
     |  Key_LaunchMail = 16777376
     |  
     |  Key_LaunchMedia = 16777377
     |  
     |  Key_Left = 16777234
     |  
     |  Key_Less = 60
     |  
     |  Key_LightBulb = 16777405
     |  
     |  Key_LogOff = 16777433
     |  
     |  Key_M = 77
     |  
     |  Key_MailForward = 16777467
     |  
     |  Key_Market = 16777434
     |  
     |  Key_Massyo = 16781612
     |  
     |  Key_MediaLast = 16842751
     |  
     |  Key_MediaNext = 16777347
     |  
     |  Key_MediaPause = 16777349
     |  
     |  Key_MediaPlay = 16777344
     |  
     |  Key_MediaPrevious = 16777346
     |  
     |  Key_MediaRecord = 16777348
     |  
     |  Key_MediaStop = 16777345
     |  
     |  Key_MediaTogglePlayPause = 16777350
     |  
     |  Key_Meeting = 16777435
     |  
     |  Key_Memo = 16777404
     |  
     |  Key_Menu = 16777301
     |  
     |  Key_MenuKB = 16777436
     |  
     |  Key_MenuPB = 16777437
     |  
     |  Key_Messenger = 16777465
     |  
     |  Key_Meta = 16777250
     |  
     |  Key_MicMute = 16777491
     |  
     |  Key_MicVolumeDown = 16777502
     |  
     |  Key_MicVolumeUp = 16777501
     |  
     |  Key_Minus = 45
     |  
     |  Key_Mode_switch = 16781694
     |  
     |  Key_MonBrightnessDown = 16777395
     |  
     |  Key_MonBrightnessUp = 16777394
     |  
     |  Key_Muhenkan = 16781602
     |  
     |  Key_Multi_key = 16781600
     |  
     |  Key_MultipleCandidate = 16781629
     |  
     |  Key_Music = 16777469
     |  
     |  Key_MySites = 16777438
     |  
     |  Key_N = 78
     |  
     |  Key_New = 16777504
     |  
     |  Key_News = 16777439
     |  
     |  Key_No = 16842754
     |  
     |  Key_Ntilde = 209
     |  
     |  Key_NumLock = 16777253
     |  
     |  Key_NumberSign = 35
     |  
     |  Key_O = 79
     |  
     |  Key_Oacute = 211
     |  
     |  Key_Ocircumflex = 212
     |  
     |  Key_Odiaeresis = 214
     |  
     |  Key_OfficeHome = 16777440
     |  
     |  Key_Ograve = 210
     |  
     |  Key_Ooblique = 216
     |  
     |  Key_Open = 16777505
     |  
     |  Key_OpenUrl = 16777364
     |  
     |  Key_Option = 16777441
     |  
     |  Key_Otilde = 213
     |  
     |  Key_P = 80
     |  
     |  Key_PageDown = 16777239
     |  
     |  Key_PageUp = 16777238
     |  
     |  Key_ParenLeft = 40
     |  
     |  Key_ParenRight = 41
     |  
     |  Key_Paste = 16777442
     |  
     |  Key_Pause = 16777224
     |  
     |  Key_Percent = 37
     |  
     |  Key_Period = 46
     |  
     |  Key_Phone = 16777443
     |  
     |  Key_Pictures = 16777468
     |  
     |  Key_Play = 16908293
     |  
     |  Key_Plus = 43
     |  
     |  Key_PowerDown = 16777483
     |  
     |  Key_PowerOff = 16777399
     |  
     |  Key_PreviousCandidate = 16781630
     |  
     |  Key_Print = 16777225
     |  
     |  Key_Printer = 16908290
     |  
     |  Key_Q = 81
     |  
     |  Key_Question = 63
     |  
     |  Key_QuoteDbl = 34
     |  
     |  Key_QuoteLeft = 96
     |  
     |  Key_R = 82
     |  
     |  Key_Red = 16777492
     |  
     |  Key_Redo = 16777508
     |  
     |  Key_Refresh = 16777316
     |  
     |  Key_Reload = 16777446
     |  
     |  Key_Reply = 16777445
     |  
     |  Key_Return = 16777220
     |  
     |  Key_Right = 16777236
     |  
     |  Key_Romaji = 16781604
     |  
     |  Key_RotateWindows = 16777447
     |  
     |  Key_RotationKB = 16777449
     |  
     |  Key_RotationPB = 16777448
     |  
     |  Key_S = 83
     |  
     |  Key_Save = 16777450
     |  
     |  Key_ScreenSaver = 16777402
     |  
     |  Key_ScrollLock = 16777254
     |  
     |  Key_Search = 16777362
     |  
     |  Key_Select = 16842752
     |  
     |  Key_Semicolon = 59
     |  
     |  Key_Send = 16777451
     |  
     |  Key_Settings = 16777500
     |  
     |  Key_Shift = 16777248
     |  
     |  Key_Shop = 16777406
     |  
     |  Key_SingleCandidate = 16781628
     |  
     |  Key_Slash = 47
     |  
     |  Key_Sleep = 16908292
     |  
     |  Key_Space = 32
     |  
     |  Key_Spell = 16777452
     |  
     |  Key_SplitScreen = 16777453
     |  
     |  Key_Standby = 16777363
     |  
     |  Key_Stop = 16777315
     |  
     |  Key_Subtitle = 16777477
     |  
     |  Key_Super_L = 16777299
     |  
     |  Key_Super_R = 16777300
     |  
     |  Key_Support = 16777454
     |  
     |  Key_Suspend = 16777484
     |  
     |  Key_SysReq = 16777226
     |  
     |  Key_T = 84
     |  
     |  Key_THORN = 222
     |  
     |  Key_Tab = 16777217
     |  
     |  Key_TaskPane = 16777455
     |  
     |  Key_Terminal = 16777456
     |  
     |  Key_Time = 16777479
     |  
     |  Key_ToDoList = 16777420
     |  
     |  Key_ToggleCallHangup = 17825799
     |  
     |  Key_Tools = 16777457
     |  
     |  Key_TopMenu = 16777482
     |  
     |  Key_TouchpadOff = 16777490
     |  
     |  Key_TouchpadOn = 16777489
     |  
     |  Key_TouchpadToggle = 16777488
     |  
     |  Key_Touroku = 16781611
     |  
     |  Key_Travel = 16777458
     |  
     |  Key_TrebleDown = 16777335
     |  
     |  Key_TrebleUp = 16777334
     |  
     |  Key_U = 85
     |  
     |  Key_UWB = 16777473
     |  
     |  Key_Uacute = 218
     |  
     |  Key_Ucircumflex = 219
     |  
     |  Key_Udiaeresis = 220
     |  
     |  Key_Ugrave = 217
     |  
     |  Key_Underscore = 95
     |  
     |  Key_Undo = 16777507
     |  
     |  Key_Up = 16777235
     |  
     |  Key_V = 86
     |  
     |  Key_Video = 16777459
     |  
     |  Key_View = 16777481
     |  
     |  Key_VoiceDial = 17825800
     |  
     |  Key_VolumeDown = 16777328
     |  
     |  Key_VolumeMute = 16777329
     |  
     |  Key_VolumeUp = 16777330
     |  
     |  Key_W = 87
     |  
     |  Key_WLAN = 16777472
     |  
     |  Key_WWW = 16777403
     |  
     |  Key_WakeUp = 16777400
     |  
     |  Key_WebCam = 16777466
     |  
     |  Key_Word = 16777460
     |  
     |  Key_X = 88
     |  
     |  Key_Xfer = 16777461
     |  
     |  Key_Y = 89
     |  
     |  Key_Yacute = 221
     |  
     |  Key_Yellow = 16777494
     |  
     |  Key_Yes = 16842753
     |  
     |  Key_Z = 90
     |  
     |  Key_Zenkaku = 16781608
     |  
     |  Key_Zenkaku_Hankaku = 16781610
     |  
     |  Key_Zoom = 16908294
     |  
     |  Key_ZoomIn = 16777462
     |  
     |  Key_ZoomOut = 16777463
     |  
     |  Key_acute = 180
     |  
     |  Key_brokenbar = 166
     |  
     |  Key_cedilla = 184
     |  
     |  Key_cent = 162
     |  
     |  Key_copyright = 169
     |  
     |  Key_currency = 164
     |  
     |  Key_degree = 176
     |  
     |  Key_diaeresis = 168
     |  
     |  Key_division = 247
     |  
     |  Key_exclamdown = 161
     |  
     |  Key_guillemotleft = 171
     |  
     |  Key_guillemotright = 187
     |  
     |  Key_hyphen = 173
     |  
     |  Key_iTouch = 16777432
     |  
     |  Key_macron = 175
     |  
     |  Key_masculine = 186
     |  
     |  Key_mu = 181
     |  
     |  Key_multiply = 215
     |  
     |  Key_nobreakspace = 160
     |  
     |  Key_notsign = 172
     |  
     |  Key_onehalf = 189
     |  
     |  Key_onequarter = 188
     |  
     |  Key_onesuperior = 185
     |  
     |  Key_ordfeminine = 170
     |  
     |  Key_paragraph = 182
     |  
     |  Key_periodcentered = 183
     |  
     |  Key_plusminus = 177
     |  
     |  Key_questiondown = 191
     |  
     |  Key_registered = 174
     |  
     |  Key_section = 167
     |  
     |  Key_ssharp = 223
     |  
     |  Key_sterling = 163
     |  
     |  Key_threequarters = 190
     |  
     |  Key_threesuperior = 179
     |  
     |  Key_twosuperior = 178
     |  
     |  Key_unknown = 33554431
     |  
     |  Key_ydiaeresis = 255
     |  
     |  Key_yen = 165
     |  
     |  KeyboardModifier = <class 'PythonQt.QtCore.KeyboardModifier'>
     |  
     |  
     |  KeyboardModifierMask = -33554432
     |  
     |  KeyboardModifiers = <class 'PythonQt.QtCore.KeyboardModifiers'>
     |  
     |  
     |  KeypadModifier = 536870912
     |  
     |  LandscapeOrientation = 2
     |  
     |  LastCursor = 21
     |  
     |  LastGestureType = -1
     |  
     |  LayoutDirection = <class 'PythonQt.QtCore.LayoutDirection'>
     |  
     |  
     |  LayoutDirectionAuto = 2
     |  
     |  LeftArrow = 3
     |  
     |  LeftButton = 1
     |  
     |  LeftDockWidgetArea = 1
     |  
     |  LeftEdge = 2
     |  
     |  LeftSection = 1
     |  
     |  LeftToRight = 0
     |  
     |  LeftToolBarArea = 1
     |  
     |  LinearGradientPattern = 15
     |  
     |  LinkAction = 4
     |  
     |  LinksAccessibleByKeyboard = 8
     |  
     |  LinksAccessibleByMouse = 4
     |  
     |  LocalDate = 2
     |  
     |  LocalTime = 0
     |  
     |  LocaleDate = 3
     |  
     |  LogicalCoordinates = 1
     |  
     |  LogicalMoveStyle = 0
     |  
     |  LowEventPriority = -1
     |  
     |  MPenCapStyle = 48
     |  
     |  MPenJoinStyle = 448
     |  
     |  MPenStyle = 15
     |  
     |  MSWindowsFixedSizeDialogHint = 256
     |  
     |  MSWindowsOwnDC = 512
     |  
     |  MacWindowToolBarButtonHint = 268435456
     |  
     |  MaskInColor = 0
     |  
     |  MaskMode = <class 'PythonQt.QtCore.MaskMode'>
     |  
     |  
     |  MaskOutColor = 1
     |  
     |  MatchCaseSensitive = 16
     |  
     |  MatchContains = 1
     |  
     |  MatchEndsWith = 3
     |  
     |  MatchExactly = 0
     |  
     |  MatchFixedString = 8
     |  
     |  MatchFlag = <class 'PythonQt.QtCore.MatchFlag'>
     |  
     |  
     |  MatchFlags = <class 'PythonQt.QtCore.MatchFlags'>
     |  
     |  
     |  MatchRecursive = 64
     |  
     |  MatchRegExp = 4
     |  
     |  MatchStartsWith = 2
     |  
     |  MatchWildcard = 5
     |  
     |  MatchWrap = 32
     |  
     |  MaxMouseButton = 67108864
     |  
     |  MaximizeUsingFullscreenGeometryHint = 4194304
     |  
     |  MaximumSize = 2
     |  
     |  MenuBarFocusReason = 6
     |  
     |  MetaModifier = 268435456
     |  
     |  MidButton = 4
     |  
     |  MiddleButton = 4
     |  
     |  MinimumDescent = 3
     |  
     |  MinimumSize = 0
     |  
     |  MiterJoin = 0
     |  
     |  Monday = 1
     |  
     |  MonoOnly = 2
     |  
     |  MouseButton = <class 'PythonQt.QtCore.MouseButton'>
     |  
     |  
     |  MouseButtonMask = -1
     |  
     |  MouseButtons = <class 'PythonQt.QtCore.MouseButtons'>
     |  
     |  
     |  MouseEventCreatedDoubleClick = 1
     |  
     |  MouseEventFlag = <class 'PythonQt.QtCore.MouseEventFlag'>
     |  
     |  
     |  MouseEventFlagMask = 255
     |  
     |  MouseEventFlags = <class 'PythonQt.QtCore.MouseEventFlags'>
     |  
     |  
     |  MouseEventNotSynthesized = 0
     |  
     |  MouseEventSource = <class 'PythonQt.QtCore.MouseEventSource'>
     |  
     |  
     |  MouseEventSynthesizedByApplication = 3
     |  
     |  MouseEventSynthesizedByQt = 2
     |  
     |  MouseEventSynthesizedBySystem = 1
     |  
     |  MouseFocusReason = 0
     |  
     |  MoveAction = 2
     |  
     |  NDockWidgetAreas = 4
     |  
     |  NSizeHints = 4
     |  
     |  NToolBarAreas = 4
     |  
     |  NativeGestureType = <class 'PythonQt.QtCore.NativeGestureType'>
     |  
     |  
     |  NavigationMode = <class 'PythonQt.QtCore.NavigationMode'>
     |  
     |  
     |  NavigationModeCursorAuto = 3
     |  
     |  NavigationModeCursorForceVisible = 4
     |  
     |  NavigationModeKeypadDirectional = 2
     |  
     |  NavigationModeKeypadTabOrder = 1
     |  
     |  NavigationModeNone = 0
     |  
     |  NoAlpha = 12
     |  
     |  NoArrow = 0
     |  
     |  NoBrush = 0
     |  
     |  NoButton = 0
     |  
     |  NoClip = 0
     |  
     |  NoContextMenu = 0
     |  
     |  NoDockWidgetArea = 0
     |  
     |  NoDropShadowWindowHint = 1073741824
     |  
     |  NoFocus = 0
     |  
     |  NoFocusReason = 8
     |  
     |  NoFormatConversion = 512
     |  
     |  NoGesture = 0
     |  
     |  NoItemFlags = 0
     |  
     |  NoModifier = 0
     |  
     |  NoOpaqueDetection = 256
     |  
     |  NoPen = 0
     |  
     |  NoSection = 0
     |  
     |  NoTabFocus = 0
     |  
     |  NoTextInteraction = 0
     |  
     |  NoToolBarArea = 0
     |  
     |  NonModal = 0
     |  
     |  NormalEventPriority = 0
     |  
     |  OddEvenFill = 0
     |  
     |  OffsetFromUTC = 2
     |  
     |  OpaqueMode = 1
     |  
     |  OpenHandCursor = 17
     |  
     |  OrderedAlphaDither = 4
     |  
     |  OrderedDither = 16
     |  
     |  Orientation = <class 'PythonQt.QtCore.Orientation'>
     |  
     |  
     |  Orientations = <class 'PythonQt.QtCore.Orientations'>
     |  
     |  
     |  OtherFocusReason = 7
     |  
     |  PanGesture = 3
     |  
     |  PanNativeGesture = 2
     |  
     |  PartiallyChecked = 1
     |  
     |  PenCapStyle = <class 'PythonQt.QtCore.PenCapStyle'>
     |  
     |  
     |  PenJoinStyle = <class 'PythonQt.QtCore.PenJoinStyle'>
     |  
     |  
     |  PenStyle = <class 'PythonQt.QtCore.PenStyle'>
     |  
     |  
     |  PinchGesture = 4
     |  
     |  PlainText = 0
     |  
     |  PointingHandCursor = 13
     |  
     |  Popup = 9
     |  
     |  PopupFocusReason = 4
     |  
     |  PortraitOrientation = 1
     |  
     |  PreciseTimer = 0
     |  
     |  PreferDither = 64
     |  
     |  PreferredSize = 1
     |  
     |  PreventContextMenu = 4
     |  
     |  PrimaryOrientation = 0
     |  
     |  QueuedConnection = 2
     |  
     |  RFC2822Date = 8
     |  
     |  RadialGradientPattern = 16
     |  
     |  ReceivePartialGestures = 2
     |  
     |  RelativeSize = 1
     |  
     |  RepeatTile = 1
     |  
     |  ReplaceClip = 1
     |  
     |  ReplaceSelection = 0
     |  
     |  RichText = 1
     |  
     |  RightArrow = 4
     |  
     |  RightButton = 2
     |  
     |  RightDockWidgetArea = 2
     |  
     |  RightEdge = 4
     |  
     |  RightSection = 5
     |  
     |  RightToLeft = 1
     |  
     |  RightToolBarArea = 2
     |  
     |  RotateNativeGesture = 5
     |  
     |  RoundCap = 32
     |  
     |  RoundJoin = 128
     |  
     |  RoundTile = 2
     |  
     |  SIGNAL = <unbound qt slot static_Qt_SIGNAL of Qt type>
     |      X.SIGNAL(a) -> str
     |  
     |  SLOT = <unbound qt slot static_Qt_SLOT of Qt type>
     |      X.SLOT(a) -> str
     |  
     |  Saturday = 6
     |  
     |  ScreenOrientation = <class 'PythonQt.QtCore.ScreenOrientation'>
     |  
     |  
     |  ScreenOrientations = <class 'PythonQt.QtCore.ScreenOrientations'>
     |  
     |  
     |  ScrollBarAlwaysOff = 1
     |  
     |  ScrollBarAlwaysOn = 2
     |  
     |  ScrollBarAsNeeded = 0
     |  
     |  ScrollBarPolicy = <class 'PythonQt.QtCore.ScrollBarPolicy'>
     |  
     |  
     |  ScrollBegin = 1
     |  
     |  ScrollEnd = 3
     |  
     |  ScrollPhase = <class 'PythonQt.QtCore.ScrollPhase'>
     |  
     |  
     |  ScrollUpdate = 2
     |  
     |  Sheet = 5
     |  
     |  ShiftModifier = 33554432
     |  
     |  ShortcutContext = <class 'PythonQt.QtCore.ShortcutContext'>
     |  
     |  
     |  ShortcutFocusReason = 5
     |  
     |  SizeAllCursor = 9
     |  
     |  SizeBDiagCursor = 7
     |  
     |  SizeFDiagCursor = 8
     |  
     |  SizeHint = <class 'PythonQt.QtCore.SizeHint'>
     |  
     |  
     |  SizeHintRole = 13
     |  
     |  SizeHorCursor = 6
     |  
     |  SizeMode = <class 'PythonQt.QtCore.SizeMode'>
     |  
     |  
     |  SizeVerCursor = 5
     |  
     |  SmartZoomNativeGesture = 4
     |  
     |  SmoothTransformation = 1
     |  
     |  SolidLine = 1
     |  
     |  SolidPattern = 1
     |  
     |  SortOrder = <class 'PythonQt.QtCore.SortOrder'>
     |  
     |  
     |  SplashScreen = 15
     |  
     |  SplitHCursor = 12
     |  
     |  SplitVCursor = 11
     |  
     |  SquareCap = 16
     |  
     |  StatusTipPropertyRole = 30
     |  
     |  StatusTipRole = 4
     |  
     |  StretchTile = 0
     |  
     |  StrongFocus = 11
     |  
     |  SubWindow = 18
     |  
     |  Sunday = 7
     |  
     |  SvgMiterJoin = 256
     |  
     |  SwipeGesture = 5
     |  
     |  SwipeNativeGesture = 6
     |  
     |  SystemLocaleDate = 2
     |  
     |  SystemLocaleLongDate = 5
     |  
     |  SystemLocaleShortDate = 4
     |  
     |  TabFocus = 1
     |  
     |  TabFocusAllControls = 255
     |  
     |  TabFocusBehavior = <class 'PythonQt.QtCore.TabFocusBehavior'>
     |  
     |  
     |  TabFocusListControls = 2
     |  
     |  TabFocusReason = 1
     |  
     |  TabFocusTextControls = 1
     |  
     |  TapAndHoldGesture = 2
     |  
     |  TapGesture = 1
     |  
     |  TargetMoveAction = 32770
     |  
     |  TaskButton = 32
     |  
     |  TextAlignmentRole = 7
     |  
     |  TextBrowserInteraction = 13
     |  
     |  TextBypassShaping = 1048576
     |  
     |  TextColorRole = 9
     |  
     |  TextDate = 0
     |  
     |  TextDontClip = 512
     |  
     |  TextDontPrint = 16384
     |  
     |  TextEditable = 16
     |  
     |  TextEditorInteraction = 19
     |  
     |  TextElideMode = <class 'PythonQt.QtCore.TextElideMode'>
     |  
     |  
     |  TextExpandTabs = 1024
     |  
     |  TextFlag = <class 'PythonQt.QtCore.TextFlag'>
     |  
     |  
     |  TextForceLeftToRight = 131072
     |  
     |  TextForceRightToLeft = 262144
     |  
     |  TextFormat = <class 'PythonQt.QtCore.TextFormat'>
     |  
     |  
     |  TextHideMnemonic = 32768
     |  
     |  TextIncludeTrailingSpaces = 134217728
     |  
     |  TextInteractionFlag = <class 'PythonQt.QtCore.TextInteractionFlag'>
     |  
     |  
     |  TextInteractionFlags = <class 'PythonQt.QtCore.TextInteractionFlags'>
     |  
     |  
     |  TextJustificationForced = 65536
     |  
     |  TextLongestVariant = 524288
     |  
     |  TextSelectableByKeyboard = 2
     |  
     |  TextSelectableByMouse = 1
     |  
     |  TextShowMnemonic = 2048
     |  
     |  TextSingleLine = 256
     |  
     |  TextWordWrap = 4096
     |  
     |  TextWrapAnywhere = 8192
     |  
     |  TexturePattern = 24
     |  
     |  ThresholdAlphaDither = 0
     |  
     |  ThresholdDither = 32
     |  
     |  Thursday = 4
     |  
     |  TileRule = <class 'PythonQt.QtCore.TileRule'>
     |  
     |  
     |  TimeSpec = <class 'PythonQt.QtCore.TimeSpec'>
     |  
     |  
     |  TimeZone = 3
     |  
     |  TimerType = <class 'PythonQt.QtCore.TimerType'>
     |  
     |  
     |  TitleBarArea = 9
     |  
     |  Tool = 11
     |  
     |  ToolBarArea = <class 'PythonQt.QtCore.ToolBarArea'>
     |  
     |  
     |  ToolBarAreaSizes = <class 'PythonQt.QtCore.ToolBarAreaSizes'>
     |  
     |  
     |  ToolBarArea_Mask = 15
     |  
     |  ToolBarAreas = <class 'PythonQt.QtCore.ToolBarAreas'>
     |  
     |  
     |  ToolButtonFollowStyle = 4
     |  
     |  ToolButtonIconOnly = 0
     |  
     |  ToolButtonStyle = <class 'PythonQt.QtCore.ToolButtonStyle'>
     |  
     |  
     |  ToolButtonTextBesideIcon = 2
     |  
     |  ToolButtonTextOnly = 1
     |  
     |  ToolButtonTextUnderIcon = 3
     |  
     |  ToolTip = 13
     |  
     |  ToolTipPropertyRole = 29
     |  
     |  ToolTipRole = 3
     |  
     |  TopDockWidgetArea = 4
     |  
     |  TopEdge = 1
     |  
     |  TopLeftCorner = 0
     |  
     |  TopLeftSection = 2
     |  
     |  TopRightCorner = 1
     |  
     |  TopRightSection = 4
     |  
     |  TopSection = 3
     |  
     |  TopToolBarArea = 4
     |  
     |  TouchPointMoved = 2
     |  
     |  TouchPointPressed = 1
     |  
     |  TouchPointReleased = 8
     |  
     |  TouchPointState = <class 'PythonQt.QtCore.TouchPointState'>
     |  
     |  
     |  TouchPointStates = <class 'PythonQt.QtCore.TouchPointStates'>
     |  
     |  
     |  TouchPointStationary = 4
     |  
     |  TransformationMode = <class 'PythonQt.QtCore.TransformationMode'>
     |  
     |  
     |  TransparentMode = 0
     |  
     |  Tuesday = 2
     |  
     |  UIEffect = <class 'PythonQt.QtCore.UIEffect'>
     |  
     |  
     |  UI_AnimateCombo = 3
     |  
     |  UI_AnimateMenu = 1
     |  
     |  UI_AnimateToolBox = 6
     |  
     |  UI_AnimateTooltip = 4
     |  
     |  UI_FadeMenu = 2
     |  
     |  UI_FadeTooltip = 5
     |  
     |  UI_General = 0
     |  
     |  UTC = 1
     |  
     |  Unchecked = 0
     |  
     |  UniqueConnection = 128
     |  
     |  UpArrow = 1
     |  
     |  UpArrowCursor = 1
     |  
     |  UserRole = 256
     |  
     |  VerPattern = 10
     |  
     |  Vertical = 2
     |  
     |  VeryCoarseTimer = 2
     |  
     |  VisualMoveStyle = 1
     |  
     |  WA_AcceptDrops = 78
     |  
     |  WA_AcceptTouchEvents = 121
     |  
     |  WA_AlwaysShowToolTips = 84
     |  
     |  WA_AlwaysStackOnTop = 128
     |  
     |  WA_AttributeCount = 131
     |  
     |  WA_CanHostQMdiSubWindowTitleBar = 95
     |  
     |  WA_ContentsPropagated = 3
     |  
     |  WA_CustomWhatsThis = 47
     |  
     |  WA_DeleteOnClose = 55
     |  
     |  WA_Disabled = 0
     |  
     |  WA_DontCreateNativeAncestors = 101
     |  
     |  WA_DontShowOnScreen = 103
     |  
     |  WA_DropSiteRegistered = 79
     |  
     |  WA_ForceAcceptDrops = 79
     |  
     |  WA_ForceDisabled = 32
     |  
     |  WA_ForceUpdatesDisabled = 59
     |  
     |  WA_GrabbedShortcut = 50
     |  
     |  WA_GroupLeader = 72
     |  
     |  WA_Hover = 74
     |  
     |  WA_InputMethodEnabled = 14
     |  
     |  WA_InputMethodTransparent = 75
     |  
     |  WA_InvalidSize = 45
     |  
     |  WA_KeyCompression = 33
     |  
     |  WA_KeyboardFocusChange = 77
     |  
     |  WA_LaidOut = 7
     |  
     |  WA_LayoutOnEntireRect = 48
     |  
     |  WA_LayoutUsesWidgetRect = 92
     |  
     |  WA_MSWindowsUseDirect3D = 94
     |  
     |  WA_MacAlwaysShowToolWindow = 96
     |  
     |  WA_MacBrushedMetal = 46
     |  
     |  WA_MacFrameworkScaled = 117
     |  
     |  WA_MacMetalStyle = 46
     |  
     |  WA_MacMiniSize = 91
     |  
     |  WA_MacNoClickThrough = 12
     |  
     |  WA_MacNoShadow = 127
     |  
     |  WA_MacNormalSize = 89
     |  
     |  WA_MacOpaqueSizeGrip = 85
     |  
     |  WA_MacShowFocusRect = 88
     |  
     |  WA_MacSmallSize = 90
     |  
     |  WA_MacVariableSize = 102
     |  
     |  WA_Mapped = 11
     |  
     |  WA_MouseNoMask = 71
     |  
     |  WA_MouseTracking = 2
     |  
     |  WA_Moved = 43
     |  
     |  WA_NativeWindow = 100
     |  
     |  WA_NoBackground = 4
     |  
     |  WA_NoChildEventsForParent = 58
     |  
     |  WA_NoChildEventsFromChildren = 39
     |  
     |  WA_NoMousePropagation = 73
     |  
     |  WA_NoMouseReplay = 54
     |  
     |  WA_NoSystemBackground = 9
     |  
     |  WA_NoX11EventCompression = 81
     |  
     |  WA_OpaquePaintEvent = 4
     |  
     |  WA_OutsideWSRange = 49
     |  
     |  WA_PaintOnScreen = 8
     |  
     |  WA_PaintUnclipped = 52
     |  
     |  WA_PendingMoveEvent = 34
     |  
     |  WA_PendingResizeEvent = 35
     |  
     |  WA_PendingUpdate = 44
     |  
     |  WA_QuitOnClose = 76
     |  
     |  WA_Resized = 42
     |  
     |  WA_RightToLeft = 56
     |  
     |  WA_SetCursor = 38
     |  
     |  WA_SetFont = 37
     |  
     |  WA_SetLayoutDirection = 57
     |  
     |  WA_SetLocale = 87
     |  
     |  WA_SetPalette = 36
     |  
     |  WA_SetStyle = 86
     |  
     |  WA_SetWindowIcon = 53
     |  
     |  WA_SetWindowModality = 118
     |  
     |  WA_ShowModal = 70
     |  
     |  WA_ShowWithoutActivating = 98
     |  
     |  WA_StaticContents = 5
     |  
     |  WA_StyleSheet = 97
     |  
     |  WA_StyledBackground = 93
     |  
     |  WA_TintedBackground = 82
     |  
     |  WA_TouchPadAcceptSingleTouchEvents = 123
     |  
     |  WA_TranslucentBackground = 120
     |  
     |  WA_TransparentForMouseEvents = 51
     |  
     |  WA_UnderMouse = 1
     |  
     |  WA_UpdatesDisabled = 10
     |  
     |  WA_WState_AcceptedTouchBeginEvent = 122
     |  
     |  WA_WState_CompressKeys = 61
     |  
     |  WA_WState_ConfigPending = 64
     |  
     |  WA_WState_Created = 60
     |  
     |  WA_WState_DND = 67
     |  
     |  WA_WState_ExplicitShowHide = 69
     |  
     |  WA_WState_Hidden = 16
     |  
     |  WA_WState_InPaintEvent = 62
     |  
     |  WA_WState_OwnSizePolicy = 68
     |  
     |  WA_WState_Polished = 66
     |  
     |  WA_WState_Reparented = 63
     |  
     |  WA_WState_Visible = 15
     |  
     |  WA_WState_WindowOpacitySet = 119
     |  
     |  WA_WindowModified = 41
     |  
     |  WA_WindowPropagation = 80
     |  
     |  WA_X11BypassTransientForHint = 99
     |  
     |  WA_X11DoNotAcceptFocus = 126
     |  
     |  WA_X11NetWmWindowTypeCombo = 115
     |  
     |  WA_X11NetWmWindowTypeDND = 116
     |  
     |  WA_X11NetWmWindowTypeDesktop = 104
     |  
     |  WA_X11NetWmWindowTypeDialog = 110
     |  
     |  WA_X11NetWmWindowTypeDock = 105
     |  
     |  WA_X11NetWmWindowTypeDropDownMenu = 111
     |  
     |  WA_X11NetWmWindowTypeMenu = 107
     |  
     |  WA_X11NetWmWindowTypeNotification = 114
     |  
     |  WA_X11NetWmWindowTypePopupMenu = 112
     |  
     |  WA_X11NetWmWindowTypeSplash = 109
     |  
     |  WA_X11NetWmWindowTypeToolBar = 106
     |  
     |  WA_X11NetWmWindowTypeToolTip = 113
     |  
     |  WA_X11NetWmWindowTypeUtility = 108
     |  
     |  WA_X11OpenGLOverlay = 83
     |  
     |  WaitCursor = 3
     |  
     |  Wednesday = 3
     |  
     |  WhatsThisCursor = 15
     |  
     |  WhatsThisPropertyRole = 31
     |  
     |  WhatsThisRole = 5
     |  
     |  WheelFocus = 15
     |  
     |  WhiteSpaceMode = <class 'PythonQt.QtCore.WhiteSpaceMode'>
     |  
     |  
     |  WhiteSpaceModeUndefined = -1
     |  
     |  WhiteSpaceNoWrap = 2
     |  
     |  WhiteSpaceNormal = 0
     |  
     |  WhiteSpacePre = 1
     |  
     |  Widget = 0
     |  
     |  WidgetAttribute = <class 'PythonQt.QtCore.WidgetAttribute'>
     |  
     |  
     |  WidgetShortcut = 0
     |  
     |  WidgetWithChildrenShortcut = 3
     |  
     |  WindingFill = 1
     |  
     |  Window = 1
     |  
     |  WindowActive = 8
     |  
     |  WindowCloseButtonHint = 134217728
     |  
     |  WindowContextHelpButtonHint = 65536
     |  
     |  WindowDoesNotAcceptFocus = 2097152
     |  
     |  WindowFlags = <class 'PythonQt.QtCore.WindowFlags'>
     |  
     |  
     |  WindowFrameSection = <class 'PythonQt.QtCore.WindowFrameSection'>
     |  
     |  
     |  WindowFullScreen = 4
     |  
     |  WindowFullscreenButtonHint = -2147483648
     |  
     |  WindowMaximizeButtonHint = 32768
     |  
     |  WindowMaximized = 2
     |  
     |  WindowMinMaxButtonsHint = 49152
     |  
     |  WindowMinimizeButtonHint = 16384
     |  
     |  WindowMinimized = 1
     |  
     |  WindowModal = 1
     |  
     |  WindowModality = <class 'PythonQt.QtCore.WindowModality'>
     |  
     |  
     |  WindowNoState = 0
     |  
     |  WindowOverridesSystemGestures = 1048576
     |  
     |  WindowShadeButtonHint = 131072
     |  
     |  WindowShortcut = 1
     |  
     |  WindowState = <class 'PythonQt.QtCore.WindowState'>
     |  
     |  
     |  WindowStates = <class 'PythonQt.QtCore.WindowStates'>
     |  
     |  
     |  WindowStaysOnBottomHint = 67108864
     |  
     |  WindowStaysOnTopHint = 262144
     |  
     |  WindowSystemMenuHint = 8192
     |  
     |  WindowTitleHint = 4096
     |  
     |  WindowTransparentForInput = 524288
     |  
     |  WindowType = <class 'PythonQt.QtCore.WindowType'>
     |  
     |  
     |  WindowType_Mask = 255
     |  
     |  X11BypassWindowManagerHint = 1024
     |  
     |  XAxis = 0
     |  
     |  XButton1 = 8
     |  
     |  XButton2 = 16
     |  
     |  YAxis = 1
     |  
     |  ZAxis = 2
     |  
     |  ZoomNativeGesture = 3
     |  
     |  black = 2
     |  
     |  blue = 9
     |  
     |  className = <built-in method className of PythonQt.PythonQtClassWrappe...
     |      Return the classname of the object
     |  
     |  codecForHtml = <unbound qt slot static_Qt_codecForHtml of Qt type>
     |      X.codecForHtml(a) -> PythonQt.QtCore.QTextCodec
     |  
     |  color0 = 0
     |  
     |  color1 = 1
     |  
     |  convertFromPlainText = <unbound qt slot static_Qt_convertFromPlainText...
     |      X.convertFromPlainText(a, b) -> str
     |  
     |  cyan = 10
     |  
     |  darkBlue = 15
     |  
     |  darkCyan = 16
     |  
     |  darkGray = 4
     |  
     |  darkGreen = 14
     |  
     |  darkMagenta = 17
     |  
     |  darkRed = 13
     |  
     |  darkYellow = 18
     |  
     |  delete = <built-in method delete of PythonQt.PythonQtClassWrapper obje...
     |      Deletes the given C++ object
     |  
     |  gray = 5
     |  
     |  green = 8
     |  
     |  help = <built-in method help of PythonQt.PythonQtClassWrapper object>
     |      Shows the help of available methods for this class
     |  
     |  inherits = <built-in method inherits of PythonQt.PythonQtClassWrapper ...
     |      Returns if the class inherits or is of given type name
     |  
     |  lightGray = 6
     |  
     |  magenta = 11
     |  
     |  mightBeRichText = <unbound qt slot static_Qt_mightBeRichText of Qt typ...
     |      X.mightBeRichText(a) -> bool
     |  
     |  qAbs = <unbound qt slot static_Qt_qAbs of Qt type>
     |      X.qAbs(a) -> float
     |  
     |  qBound = <unbound qt slot static_Qt_qBound of Qt type>
     |      X.qBound(a, b, c) -> float
     |  
     |  qCritical = <unbound qt slot static_Qt_qCritical of Qt type>
     |      X.qCritical(a)
     |  
     |  qDebug = <unbound qt slot static_Qt_qDebug of Qt type>
     |      X.qDebug(a)
     |  
     |  qFatal = <unbound qt slot static_Qt_qFatal of Qt type>
     |      X.qFatal(a)
     |  
     |  qFuzzyCompare = <unbound qt slot static_Qt_qFuzzyCompare of Qt type>
     |      X.qFuzzyCompare(a, b) -> bool
     |  
     |  qMax = <unbound qt slot static_Qt_qMax of Qt type>
     |      X.qMax(a, b) -> float
     |  
     |  qMin = <unbound qt slot static_Qt_qMin of Qt type>
     |      X.qMin(a, b) -> float
     |  
     |  qRound = <unbound qt slot static_Qt_qRound of Qt type>
     |      X.qRound(a) -> int
     |  
     |  qRound64 = <unbound qt slot static_Qt_qRound64 of Qt type>
     |      X.qRound64(a) -> int
     |  
     |  qVersion = <unbound qt slot static_Qt_qVersion of Qt type>
     |      X.qVersion() -> int
     |  
     |  qWarning = <unbound qt slot static_Qt_qWarning of Qt type>
     |      X.qWarning(a)
     |  
     |  qrand = <unbound qt slot static_Qt_qrand of Qt type>
     |      X.qrand() -> int
     |  
     |  qsrand = <unbound qt slot static_Qt_qsrand of Qt type>
     |      X.qsrand(a)
     |  
     |  red = 7
     |  
     |  transparent = 19
     |  
     |  white = 3
     |  
     |  yellow = 12
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __delattr__(...)
     |      x.__delattr__('name') <==> del x.name
     |  
     |  __eq__(...)
     |      x.__eq__(y) <==> x==y
     |  
     |  __ge__(...)
     |      x.__ge__(y) <==> x>=y
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __gt__(...)
     |      x.__gt__(y) <==> x>y
     |  
     |  __hash__(...)
     |      x.__hash__() <==> hash(x)
     |  
     |  __init__(...)
     |      x.__init__(...) initializes x; see help(type(x)) for signature
     |  
     |  __le__(...)
     |      x.__le__(y) <==> x<=y
     |  
     |  __lt__(...)
     |      x.__lt__(y) <==> x<y
     |  
     |  __ne__(...)
     |      x.__ne__(y) <==> x!=y
     |  
     |  __nonzero__(...)
     |      x.__nonzero__() <==> x != 0
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __setattr__(...)
     |      x.__setattr__('name', value) <==> x.name = value
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from PythonQt.PythonQtInstanceWrapper:
     |  
     |  __new__ = <built-in method __new__ of PythonQt.PythonQtClassWrapper ob...
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
    
    class Signal(__builtin__.object)
     |  Signal(*types) -> Signal
     |  
     |  Methods defined here:
     |  
     |  __call__(...)
     |      x.__call__(...) <==> x(...)
     |  
     |  __cmp__(...)
     |      x.__cmp__(y) <==> cmp(x,y)
     |  
     |  __eq__(...)
     |      x.__eq__(y) <==> x==y
     |  
     |  __ge__(...)
     |      x.__ge__(y) <==> x>=y
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __gt__(...)
     |      x.__gt__(y) <==> x>y
     |  
     |  __hash__(...)
     |      x.__hash__() <==> hash(x)
     |  
     |  __init__(...)
     |      x.__init__(...) initializes x; see help(type(x)) for signature
     |  
     |  __le__(...)
     |      x.__le__(y) <==> x<=y
     |  
     |  __lt__(...)
     |      x.__lt__(y) <==> x<y
     |  
     |  __ne__(...)
     |      x.__ne__(y) <==> x!=y
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  connect(...)
     |      Connects the signal to the Python callable
     |  
     |  disconnect(...)
     |      Disconnects the signal from the given Python callable or disconnects all if no argument is passed.
     |  
     |  emit(...)
     |      Emits the signal with given arguments
     |  
     |  parameterNames(...)
     |      Returns a tuple of tuples of the C++ parameter type names (if available), for all overloads of the signal
     |  
     |  parameterTypes(...)
     |      Returns a tuple of tuples of the C++ parameter types for all overloads of the signal
     |  
     |  typeName(...)
     |      Returns a tuple of the C++ return value types of each signal overload
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __self__
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  __new__ = <built-in method __new__ of type object>
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
    
    class Slot(__builtin__.object)
     |  Slot(*types, result=type) -> Slot
     |  
     |  Methods defined here:
     |  
     |  __call__(...)
     |      x.__call__(...) <==> x(...)
     |  
     |  __init__(...)
     |      x.__init__(...) initializes x; see help(type(x)) for signature
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  __new__ = <built-in method __new__ of type object>
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T

DATA
    QtCriticalMsg = 2
    QtDebugMsg = 0
    QtFatalMsg = 3
    QtSystemMsg = 2
    QtWarningMsg = 1
    SIGNAL = <unbound qt slot static_Qt_SIGNAL of Qt type>
    SLOT = <unbound qt slot static_Qt_SLOT of Qt type>
    qAbs = <unbound qt slot static_Qt_qAbs of Qt type>
    qBound = <unbound qt slot static_Qt_qBound of Qt type>
    qCritical = <unbound qt slot static_Qt_qCritical of Qt type>
    qDebug = <unbound qt slot static_Qt_qDebug of Qt type>
    qFatal = <unbound qt slot static_Qt_qFatal of Qt type>
    qFuzzyCompare = <unbound qt slot static_Qt_qFuzzyCompare of Qt type>
    qMax = <unbound qt slot static_Qt_qMax of Qt type>
    qMin = <unbound qt slot static_Qt_qMin of Qt type>
    qRound = <unbound qt slot static_Qt_qRound of Qt type>
    qRound64 = <unbound qt slot static_Qt_qRound64 of Qt type>
    qVersion = <unbound qt slot static_Qt_qVersion of Qt type>
    qWarning = <unbound qt slot static_Qt_qWarning of Qt type>
    qrand = <unbound qt slot static_Qt_qrand of Qt type>
    qsrand = <unbound qt slot static_Qt_qsrand of Qt type>

```
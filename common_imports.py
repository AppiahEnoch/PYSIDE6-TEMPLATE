# PySide6 Widgets
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QMainWindow,
    QDialog,
    QVBoxLayout,
    QHBoxLayout,
    QGridLayout,
    QStackedWidget,
    QScrollArea,
    QLabel,
    QLineEdit,
    QPushButton,
    QRadioButton,
    QCheckBox,
    QComboBox,
    QSpinBox,
    QDoubleSpinBox,
    QSlider,
    QProgressBar,
    QTextEdit,
    QPlainTextEdit,
    QTableWidget,
    QTableWidgetItem,
    QTreeWidget,
    QTreeWidgetItem,
    QListWidget,
    QListWidgetItem,
    QTabWidget,
    QGroupBox,
    QFormLayout,
    QDockWidget,
    QToolBar,
    QMenuBar,
    QStatusBar,
    QMessageBox,
    QFileDialog,
    QInputDialog,
    QCalendarWidget,
    QFontDialog,
    QColorDialog,
    QSplitter,
    QFrame,
    QSizePolicy,
    QSpacerItem,
    QSystemTrayIcon,
    QHeaderView,
    QAbstractItemView,
    QCompleter,
    QStyledItemDelegate,
    QStyleFactory,
    QListView,
    QDialogButtonBox
)

# PySide6 GUI
from PySide6.QtGui import (
    QFont,
    QColor,
    QPalette,
    QIcon,
    QPixmap,
    QImage,
    QPainter,
    QPen,
    QBrush,
    QCursor,
    QKeySequence,
    QTextCursor,
    QTextDocument,
    QTextFormat,
    QTextCharFormat,
    QValidator,
    QIntValidator,
    QDoubleValidator,
    QRegularExpressionValidator,
    QLinearGradient,
    QDesktopServices,
    # Moved back to QtGui
)

# PySide6 Core
from PySide6.QtCore import (
    Qt,
    QObject,
    QThread,
    QTimer,
    QDateTime,
    QDate,
    QTime,
    QSize,
    QPoint,
    QRect,
    QMargins,
    QUrl,
    QMimeData,
    QEvent,
    QRegularExpression,
    QSettings,
    QTranslator,
    QLocale,
    Signal,
    Slot,
    QRunnable,
    QThreadPool,
    QStringListModel,
    QAbstractListModel,
    QModelIndex,
    QPropertyAnimation,
    QEasingCurve
)
# System imports
import sys
import os
import json
import csv
import datetime
import random
import math
import re
import logging
import sqlite3  # for basic database operations
import requests  # for HTTP requests (you may need to install this separately)
import uuid
from collections import defaultdict
import pyperclip

# Third-party libraries
from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.style import WD_STYLE_TYPE
from docx.enum.text import WD_ALIGN_PARAGRAPH
import threading
import time
from PySide6.QtGui import QIcon, QGuiApplication


from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow

# Custom imports
from database_connection import get_db_connection

# Cryptography
import bcrypt
import shutil
from PySide6.QtCore import Signal, Qt, QTimer  
# You can add more specific imports here as needed for your project
from PySide6.QtCore import QDir
from PySide6.QtWidgets import QApplication, QMessageBox, QSplashScreen
from PySide6.QtCore import QObject, Slot, QTimer, Qt
from PySide6.QtGui import QPixmap
import bcrypt
import sqlite3
import sys
import time

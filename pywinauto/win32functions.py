# GUI Application automation and testing library
# Copyright (C) 2006-2018 Mark Mc Mahon and Contributors
# https://github.com/pywinauto/pywinauto/graphs/contributors
# http://pywinauto.readthedocs.io/en/latest/credits.html
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# * Redistributions of source code must retain the above copyright notice, this
#   list of conditions and the following disclaimer.
#
# * Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
#
# * Neither the name of pywinauto nor the names of its
#   contributors may be used to endorse or promote products derived from
#   this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

"""Defines Windows(tm) functions"""

import ctypes
from ctypes import wintypes
from . import win32defines, win32structures
from .actionlogger import ActionLogger
from ctypes import c_short
from ctypes import c_long
from ctypes import WINFUNCTYPE

import sys
if sys.platform == "cygwin":
    windll = ctypes.cdll
    HRESULT = c_long


SHORT = c_short


CreateBrushIndirect = ctypes.windll.gdi32.CreateBrushIndirect
CreateBrushIndirect.restype = wintypes.HBRUSH
CreateBrushIndirect.argtypes = [
    ctypes.c_void_p,
]
CreateDC = ctypes.windll.gdi32.CreateDCW
CreateDC.restype = wintypes.HDC
CreateDC.argtypes = [
    wintypes.LPCWSTR,
    wintypes.LPCWSTR,
    wintypes.LPCWSTR,
    ctypes.c_void_p,
]
CreateFontIndirect = ctypes.windll.gdi32.CreateFontIndirectW
CreateFontIndirect.restype = wintypes.HFONT
CreateFontIndirect.argtypes = [
    ctypes.POINTER(win32structures.LOGFONTW),
]
CreatePen = ctypes.windll.gdi32.CreatePen
CreatePen.restype = wintypes.HPEN
CreatePen.argtypes = [
    ctypes.c_int,
    ctypes.c_int,
    wintypes.COLORREF,
]
DeleteDC = ctypes.windll.gdi32.DeleteDC
DeleteDC.restype = wintypes.BOOL
DeleteDC.argtypes = [
    wintypes.HDC,
]
GetObject = ctypes.windll.gdi32.GetObjectW
GetObject.restype = ctypes.c_int
GetObject.argtypes = [
    wintypes.HANDLE,
    ctypes.c_int,
    wintypes.LPVOID,
]
DeleteObject = ctypes.windll.gdi32.DeleteObject
DeleteObject.restype = wintypes.BOOL
DeleteObject.argtypes = [
    wintypes.HGDIOBJ,
]
DrawText = ctypes.windll.user32.DrawTextW
DrawText.restype = ctypes.c_int
DrawText.argtypes = [
    wintypes.HDC,
    wintypes.LPCWSTR,
    ctypes.c_int,
    ctypes.POINTER(win32structures.RECT),
    wintypes.UINT,
]
TextOut = ctypes.windll.gdi32.TextOutW
TextOut.restype = wintypes.BOOL
TextOut.argtypes = [
    wintypes.HDC,
    ctypes.c_int,
    ctypes.c_int,
    wintypes.LPCWSTR,
    ctypes.c_int,
]
Rectangle = ctypes.windll.gdi32.Rectangle
Rectangle.restype = wintypes.BOOL
Rectangle.argtypes = [
    wintypes.HDC,
    ctypes.c_int,
    ctypes.c_int,
    ctypes.c_int,
    ctypes.c_int,
]
SelectObject = ctypes.windll.gdi32.SelectObject
SelectObject.restype = wintypes.HGDIOBJ
SelectObject.argtypes = [
    wintypes.HDC,
    wintypes.HGDIOBJ,
]
GetStockObject = ctypes.windll.gdi32.GetStockObject
GetStockObject.restype = wintypes.HGDIOBJ
GetStockObject.argtypes = [
    ctypes.c_int,
]
GetSystemMetrics = ctypes.windll.user32.GetSystemMetrics
GetSystemMetrics.restype = ctypes.c_int
GetSystemMetrics.argtypes = [
    ctypes.c_int,
]
GetTextMetrics = ctypes.windll.gdi32.GetTextMetricsW
GetTextMetrics.restype = wintypes.BOOL
GetTextMetrics.argtypes = [
    wintypes.HDC,
    ctypes.POINTER(win32structures.TEXTMETRICW),
]
EnumChildWindows = ctypes.windll.user32.EnumChildWindows
EnumChildWindows.restype = wintypes.BOOL
EnumChildWindows.argtypes = [
    wintypes.HWND,
    WINFUNCTYPE(wintypes.BOOL, wintypes.HWND, wintypes.LPARAM),
    wintypes.LPARAM,
]
EnumDesktopWindows = ctypes.windll.user32.EnumDesktopWindows
EnumDesktopWindows.restype = wintypes.BOOL
EnumDesktopWindows.argtypes = [
    wintypes.LPVOID,
    WINFUNCTYPE(wintypes.BOOL, wintypes.HWND, wintypes.LPARAM),
    wintypes.LPARAM,
]
EnumWindows = ctypes.windll.user32.EnumWindows
EnumWindows.restype = wintypes.BOOL
EnumWindows.argtypes = [
    WINFUNCTYPE(wintypes.BOOL, wintypes.HWND, wintypes.LPARAM),
    wintypes.LPARAM,
]
GetDC = ctypes.windll.user32.GetDC
GetDC.restype = wintypes.LPVOID
GetDC.argtypes = [
    wintypes.HWND,
]
GetDesktopWindow = ctypes.windll.user32.GetDesktopWindow
GetDesktopWindow.restype = wintypes.HWND
GetDesktopWindow.argtypes = [
]
SendInput = ctypes.windll.user32.SendInput
SendInput.restype = wintypes.UINT
SendInput.argtypes = [
    wintypes.UINT,
    ctypes.c_void_p,  # using ctypes.POINTER(win32structures.INPUT) needs rework in keyboard.py
    ctypes.c_int,
]
SetCursorPos = ctypes.windll.user32.SetCursorPos
SetCursorPos.restype = wintypes.BOOL
SetCursorPos.argtypes = [
    ctypes.c_int,
    ctypes.c_int,
]
GetCursorPos = ctypes.windll.user32.GetCursorPos
GetCursorPos.restype = wintypes.BOOL
GetCursorPos.argtypes = [
    ctypes.POINTER(win32structures.POINT),
]
GetCaretPos = ctypes.windll.user32.GetCaretPos
GetCaretPos.restype = wintypes.BOOL
GetCaretPos.argtypes = [
    ctypes.POINTER(win32structures.POINT),
]

# menu functions
DrawMenuBar = ctypes.windll.user32.DrawMenuBar
DrawMenuBar.restype = wintypes.BOOL
DrawMenuBar.argstype = [
    wintypes.HWND,
]
GetMenu = ctypes.windll.user32.GetMenu
GetMenu.restype = wintypes.HMENU
GetMenu.argtypes = [
    wintypes.HWND,
]
GetMenuBarInfo = ctypes.windll.user32.GetMenuBarInfo
GetMenuBarInfo.restype = wintypes.BOOL
GetMenuBarInfo.argtypes = [
    wintypes.HWND,
    wintypes.LONG,
    wintypes.LONG,
    ctypes.POINTER(MENUBARINFO),
]
GetMenuInfo         =   ctypes.windll.user32.GetMenuInfo
GetMenuItemCount	=	ctypes.windll.user32.GetMenuItemCount
GetMenuItemInfo		=	ctypes.windll.user32.GetMenuItemInfoW
SetMenuItemInfo     =   ctypes.windll.user32.SetMenuItemInfoW
GetMenuItemRect     =   ctypes.windll.user32.GetMenuItemRect
CheckMenuItem		=	ctypes.windll.user32.CheckMenuItem
GetMenuState		=	ctypes.windll.user32.GetMenuState
GetSubMenu	        =	ctypes.windll.user32.GetSubMenu
GetSystemMenu		=	ctypes.windll.user32.GetSystemMenu
HiliteMenuItem		=	ctypes.windll.user32.HiliteMenuItem
IsMenu				=	ctypes.windll.user32.IsMenu
MenuItemFromPoint	=	ctypes.windll.user32.MenuItemFromPoint

BringWindowToTop    =   ctypes.windll.user32.BringWindowToTop

GetVersion          =   ctypes.windll.kernel32.GetVersion

GetParent			=	ctypes.windll.user32.GetParent
GetWindow			=	ctypes.windll.user32.GetWindow
ShowWindow			= 	ctypes.windll.user32.ShowWindow
GetWindowContextHelpId =	ctypes.windll.user32.GetWindowContextHelpId
GetWindowLong		=	ctypes.windll.user32.GetWindowLongW
GetWindowLong.argtypes = [wintypes.HWND, ctypes.c_int]
GetWindowLong.restype = wintypes.LONG
GetWindowPlacement  =   ctypes.windll.user32.GetWindowPlacement
GetWindowRect		=	ctypes.windll.user32.GetWindowRect
GetWindowText		=	ctypes.windll.user32.GetWindowTextW
GetWindowTextLength	=	ctypes.windll.user32.GetWindowTextLengthW
GetClassName        =   ctypes.windll.user32.GetClassNameW
GetClassName.argtypes = [wintypes.HWND, wintypes.LPWSTR, ctypes.c_int]
GetClassName.restype = ctypes.c_int
GetClientRect       =   ctypes.windll.user32.GetClientRect
IsChild				=	ctypes.windll.user32.IsChild
IsWindow 			=	ctypes.windll.user32.IsWindow
IsWindow.argtypes = [wintypes.HWND]
IsWindow.restype = wintypes.BOOL
IsWindowUnicode		=	ctypes.windll.user32.IsWindowUnicode
IsWindowUnicode.argtypes = [wintypes.HWND]
IsWindowUnicode.restype = wintypes.BOOL
IsWindowVisible		=	ctypes.windll.user32.IsWindowVisible
IsWindowVisible.argtypes = [wintypes.HWND]
IsWindowVisible.restype = wintypes.BOOL
IsWindowEnabled		=	ctypes.windll.user32.IsWindowEnabled
IsWindowEnabled.argtypes = [wintypes.HWND]
IsWindowEnabled.restype = wintypes.BOOL
ClientToScreen      =   ctypes.windll.user32.ClientToScreen
ScreenToClient      =   ctypes.windll.user32.ScreenToClient

GetCurrentThreadId  =   ctypes.windll.Kernel32.GetCurrentThreadId
GetWindowThreadProcessId =  ctypes.windll.user32.GetWindowThreadProcessId
GetGUIThreadInfo    =   ctypes.windll.user32.GetGUIThreadInfo
AttachThreadInput   =   ctypes.windll.user32.AttachThreadInput
AttachThreadInput.restype = wintypes.BOOL
AttachThreadInput.argtypes = [wintypes.DWORD, wintypes.DWORD, wintypes.BOOL]
#GetWindowThreadProcessId    =   ctypes.windll.user32.GetWindowThreadProcessId
GetLastError = ctypes.windll.kernel32.GetLastError

OpenProcess = ctypes.windll.kernel32.OpenProcess
OpenProcess.restype = wintypes.HANDLE
OpenProcess.argtypes = [
    wintypes.DWORD,
    wintypes.BOOL,
    wintypes.DWORD,
]
CloseHandle = ctypes.windll.kernel32.CloseHandle
CloseHandle.restype = wintypes.BOOL
CloseHandle.argtypes = [ wintypes.HANDLE ]
CreateProcess       = ctypes.windll.kernel32.CreateProcessW
TerminateProcess    = ctypes.windll.kernel32.TerminateProcess
ExitProcess         = ctypes.windll.kernel32.ExitProcess

ReadProcessMemory = ctypes.windll.kernel32.ReadProcessMemory
ReadProcessMemory.restype = wintypes.BOOL
ReadProcessMemory.argtypes = [
    wintypes.HANDLE,
    wintypes.LPVOID,
    wintypes.LPVOID,
    ctypes.c_size_t,
    ctypes.POINTER(ctypes.c_size_t),
]
GlobalAlloc = ctypes.windll.kernel32.GlobalAlloc
GlobalLock = ctypes.windll.kernel32.GlobalLock
GlobalUnlock = ctypes.windll.kernel32.GlobalUnlock

SendMessage			=	ctypes.windll.user32.SendMessageW
SendMessage.argtypes = [wintypes.HWND, wintypes.UINT, wintypes.WPARAM,
                        wintypes.LPVOID]
SendMessage.restype = wintypes.LPARAM

SendMessageTimeout  =   ctypes.windll.user32.SendMessageTimeoutW
SendMessageTimeout.argtypes = [wintypes.HWND, wintypes.UINT, wintypes.WPARAM,
                               wintypes.LPARAM, wintypes.UINT, wintypes.UINT,
                               win32structures.PDWORD_PTR]
SendMessageTimeout.restype = wintypes.LPARAM
SendMessageA		=	ctypes.windll.user32.SendMessageA
PostMessage			=	ctypes.windll.user32.PostMessageW
GetMessage          =   ctypes.windll.user32.GetMessageW
RegisterWindowMessage = ctypes.windll.user32.RegisterWindowMessageW
RegisterWindowMessage.restype = wintypes.UINT

MoveWindow          =   ctypes.windll.user32.MoveWindow
EnableWindow        =   ctypes.windll.user32.EnableWindow
SetActiveWindow		=	ctypes.windll.user32.SetActiveWindow
GetFocus			=	ctypes.windll.user32.GetFocus
SetFocus			=	ctypes.windll.user32.SetFocus
SetForegroundWindow	=	ctypes.windll.user32.SetForegroundWindow
GetForegroundWindow	=	ctypes.windll.user32.GetForegroundWindow
SetWindowLong		=	ctypes.windll.user32.SetWindowLongW
try:
    SetWindowLongPtr    =   ctypes.windll.user32.SetWindowLongPtrW
    SetWindowLongPtr.argtypes = [wintypes.HWND, ctypes.c_int, wintypes.LONG_PTR]
    SetWindowLongPtr.restype = wintypes.LONG_PTR
except AttributeError:
    SetWindowLongPtr = SetWindowLong
SystemParametersInfo =	ctypes.windll.user32.SystemParametersInfoW
VirtualAllocEx = ctypes.windll.kernel32.VirtualAllocEx
VirtualAllocEx.restype = wintypes.LPVOID
VirtualAllocEx.argtypes = [
    wintypes.HANDLE,
    wintypes.LPVOID,
    ctypes.c_size_t,
    wintypes.DWORD,
    wintypes.DWORD,
]
VirtualFreeEx =	ctypes.windll.kernel32.VirtualFreeEx
VirtualFreeEx.restype = wintypes.BOOL
VirtualFreeEx.argtypes = [
    wintypes.HANDLE,
    wintypes.LPVOID,
    ctypes.c_size_t,
    wintypes.DWORD,
]
DebugBreakProcess	=	ctypes.windll.kernel32.DebugBreakProcess

VirtualAlloc = ctypes.windll.kernel32.VirtualAlloc
VirtualAlloc.restype = wintypes.LPVOID
VirtualAlloc.argtypes = [
    wintypes.LPVOID,
    ctypes.c_size_t,
    wintypes.DWORD,
    wintypes.DWORD,
]
VirtualFree = ctypes.windll.kernel32.VirtualFree
VirtualFree.retype = wintypes.BOOL
VirtualFree.argtypes = [
    wintypes.LPVOID,
    ctypes.c_size_t,
    wintypes.DWORD,
]
WriteProcessMemory = ctypes.windll.kernel32.WriteProcessMemory
WriteProcessMemory.restype = wintypes.BOOL
WriteProcessMemory.argtypes = [
    wintypes.HANDLE,
    wintypes.LPVOID,
    wintypes.LPVOID,
    ctypes.c_size_t,
    ctypes.POINTER(ctypes.c_size_t),
]

GetActiveWindow		=	ctypes.windll.user32.GetActiveWindow
GetLastActivePopup 	=	ctypes.windll.user32.GetLastActivePopup
FindWindow			=	ctypes.windll.user32.FindWindowW
GetTopWindow		=	ctypes.windll.user32.GetTopWindow

SetCapture			=	ctypes.windll.user32.SetCapture
ReleaseCapture		=	ctypes.windll.user32.ReleaseCapture

ShowOwnedPopups		=	ctypes.windll.user32.ShowOwnedPopups
WindowFromPoint 	=	ctypes.windll.user32.WindowFromPoint

WideCharToMultiByte	=	ctypes.windll.kernel32.WideCharToMultiByte
GetACP				=	ctypes.windll.kernel32.GetACP

WaitForSingleObject = ctypes.windll.kernel32.WaitForSingleObject
WaitForInputIdle	= ctypes.windll.user32.WaitForInputIdle

IsHungAppWindow     = ctypes.windll.user32.IsHungAppWindow
IsHungAppWindow.restype = wintypes.BOOL
IsHungAppWindow.argtypes = [wintypes.HWND]

GetModuleFileNameEx = ctypes.windll.psapi.GetModuleFileNameExW

GetClipboardData = ctypes.windll.user32.GetClipboardData
OpenClipboard    = ctypes.windll.user32.OpenClipboard
EmptyClipboard   = ctypes.windll.user32.EmptyClipboard
CloseClipboard   = ctypes.windll.user32.CloseClipboard
CountClipboardFormats  = ctypes.windll.user32.CountClipboardFormats
EnumClipboardFormats   = ctypes.windll.user32.EnumClipboardFormats
GetClipboardFormatName = ctypes.windll.user32.GetClipboardFormatNameW

# DPIAware API funcs are not available on WinXP
try:
    IsProcessDPIAware = ctypes.windll.user32.IsProcessDPIAware
    SetProcessDPIAware = ctypes.windll.user32.SetProcessDPIAware
except AttributeError:
    IsProcessDPIAware = None
    SetProcessDPIAware = None

# DpiAwareness API funcs are available only from win 8.1 and greater
# Supported types of DPI awareness described here:
# https://msdn.microsoft.com/en-us/library/windows/desktop/dn280512(v=vs.85).aspx
# typedef enum _Process_DPI_Awareness {
#   Process_DPI_Unaware            = 0,
#   Process_System_DPI_Aware       = 1,
#   Process_Per_Monitor_DPI_Aware  = 2
# } Process_DPI_Awareness;
try:
    shcore = ctypes.windll.LoadLibrary("Shcore.dll")
    SetProcessDpiAwareness = shcore.SetProcessDpiAwareness
    GetProcessDpiAwareness = shcore.GetProcessDpiAwareness
    Process_DPI_Awareness = {
        "Process_DPI_Unaware"           : 0,
        "Process_System_DPI_Aware"      : 1,
        "Process_Per_Monitor_DPI_Aware" : 2
        }
except (OSError, AttributeError):
    SetProcessDpiAwareness = None
    GetProcessDpiAwareness = None
    Process_DPI_Awareness = None

# Setup DPI awareness for the python process if any is supported
if SetProcessDpiAwareness:
    ActionLogger().log("Call SetProcessDpiAwareness")
    SetProcessDpiAwareness(
            Process_DPI_Awareness["Process_Per_Monitor_DPI_Aware"])
elif SetProcessDPIAware:
    ActionLogger().log("Call SetProcessDPIAware")
    SetProcessDPIAware()

GetQueueStatus = ctypes.windll.user32.GetQueueStatus

LoadString = ctypes.windll.user32.LoadStringW


#def VkKeyScanW(p1):
#    # C:/PROGRA~1/MICROS~4/VC98/Include/winuser.h 4225
#    return VkKeyScanW._api_(p1)
#VkKeyScan = stdcall(SHORT, 'user32', [c_wchar]) (VkKeyScanW)
#
#def MapVirtualKeyExW(p1, p2, p3):
#    # C:/PROGRA~1/MICROS~4/VC98/Include/winuser.h 4376
#    return MapVirtualKeyExW._api_(p1, p2, p3)
#MapVirtualKeyEx = stdcall(
#    UINT, 'user32', [c_uint, c_uint, c_long]) (MapVirtualKeyExW)
#
#def MapVirtualKeyW(p1, p2):
#    # C:/PROGRA~1/MICROS~4/VC98/Include/winuser.h 4355
#    return MapVirtualKeyW._api_(p1, p2)
#MapVirtualKey = stdcall(UINT, 'user32', [c_uint, c_uint]) (MapVirtualKeyW)


#====================================================================
def MakeLong(high, low):
    """Pack high into the high word of a long and low into the low word"""

    # we need to AND each value with 0xFFFF to account for numbers
    # greater then normal WORD (short) size
    return ((high & 0xFFFF) << 16) | (low & 0xFFFF)

#====================================================================
def HiWord(value):
    """Return the high word from a long"""
    #return (value & (~ 0xFFFF)) / 0xFFFF
    return (value >> 16) & 0xffff

#====================================================================
def LoWord(value):
    """Return the low word from a long"""
    return value & 0xFFFF

#====================================================================
def WaitGuiThreadIdle(handle):
    """Wait until the thread of the specified handle is ready"""
    process_id = wintypes.DWORD(0)
    GetWindowThreadProcessId(handle, ctypes.POINTER(wintypes.DWORD)(process_id))

    # ask the control if it has finished processing the message
    hprocess = OpenProcess(
        win32defines.PROCESS_QUERY_INFORMATION,
        0,
        process_id.value)

    # WaitForInputIdle call is removed because it's useful only
    # while an app is starting (should be called only once)
    if IsHungAppWindow(handle) == win32defines.TRUE:
        raise RuntimeError('Window (hwnd={0}) is not responding!'.format(handle))

    CloseHandle(hprocess)

#====================================================================
def GetDpiAwarenessByPid(pid):
    """Get DPI awareness properties of a process specified by ID"""
    dpi_awareness = -1
    hProcess = None
    if GetProcessDpiAwareness and pid:
        hProcess = OpenProcess(
                    win32defines.PROCESS_QUERY_INFORMATION,
                    0,
                    pid)
        if not hProcess:
            # process doesn't exist, exit with a default return value
            return dpi_awareness

        try:
            dpi_awareness = ctypes.c_int()
            hRes = GetProcessDpiAwareness(
                    hProcess,
                    ctypes.byref(dpi_awareness))
            CloseHandle(hProcess)
            if hRes == 0:
                return dpi_awareness.value
        finally:
            if hProcess:
                CloseHandle(hProcess)

    # GetProcessDpiAwareness is not supported or pid is not specified,
    # return a default value
    return dpi_awareness

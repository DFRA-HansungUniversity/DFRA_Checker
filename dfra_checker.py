import tkinter as tk
import os
import winreg

def check_vmware_usb_arbitration():
    # VMware USB Arbitration Service 폴더 존재 여부 확인
    path = "C:\\ProgramData\\VMware\\VMware USB Arbitration Service"
    if os.path.exists(path):
        return "위험"
    else:
        return "안전"

def check_enable_lua():
    # EnableLUA 레지스트리 값 확인
    try:
        reg_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System", 0, winreg.KEY_READ)
        enable_lua, _ = winreg.QueryValueEx(reg_key, "EnableLUA")
        winreg.CloseKey(reg_key)
        
        if enable_lua == 0:
            return "위험"
        else:
            return "안전"
    except FileNotFoundError:
        return "레지스트리 경로를 찾을 수 없습니다."

def analyze_system():
    # VMware USB 유틸리티 확인 결과
    vmware_result = check_vmware_usb_arbitration()
    result_vmware_label.config(text=f"VMware USB 유틸리티: {vmware_result}")

    # 윈도우 잠금 설정 확인 결과
    lua_result = check_enable_lua()
    result_lua_label.config(text=f"윈도우 잠금: {lua_result}")

# GUI 구성
root = tk.Tk()
root.title("DFRA Checker (Windows 보안 위험요소 자동 식별 도구)")
root.geometry("400x200")

# 안내 텍스트
info_label = tk.Label(root, text="Windows 위험 요소 분석 결과", font=("Arial", 14))
info_label.pack(pady=10)

# 분석 결과 라벨
result_vmware_label = tk.Label(root, text="VMware USB 유틸리티: 미확인", font=("Arial", 12))
result_vmware_label.pack(pady=5)

result_lua_label = tk.Label(root, text="윈도우 잠금: 미확인", font=("Arial", 12))
result_lua_label.pack(pady=5)

# 분석 버튼
analyze_button = tk.Button(root, text="위험 요소 분석", command=analyze_system)
analyze_button.pack(pady=20)

# GUI 실행
root.mainloop()

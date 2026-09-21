from machine import ADC, Pin
import time

# MQ2 가스 센서 아날로그 핀 설정 (GP26 = ADC0)
gas_sensor = ADC(Pin(26))

# LED 핀 설정 (단계별로 3개 사용 예시)
led_safe = Pin(15, Pin.OUT)      # 초록 - 안전
led_warning = Pin(16, Pin.OUT)   # 노랑 - 주의
led_danger = Pin(17, Pin.OUT)    # 빨강 - 위험

# 임계값 설정 (실제 환경에서 테스트하며 조정 필요!)
THRESHOLD_SAFE = 20000      # 이 값 이하면 안전
THRESHOLD_WARNING = 35000   # 이 값 이하면 주의
# 이 값 초과하면 위험

def all_led_off():
    led_safe.value(0)
    led_warning.value(0)
    led_danger.value(0)

def update_led(gas_value):
    all_led_off()
    if gas_value < THRESHOLD_SAFE:
        led_safe.value(1)
        print(f"안전 단계 (가스값: {gas_value})")
    elif gas_value < THRESHOLD_WARNING:
        led_warning.value(1)
        print(f"주의 단계 (가스값: {gas_value})")
    else:
        led_danger.value(1)
        print(f"위험 단계! 환기하세요! (가스값: {gas_value})")

# 메인 루프
while True:
    gas_value = gas_sensor.read_u16()  # 0~65535 범위 값 읽기
    update_led(gas_value)
    time.sleep(1)  # 1초마다 측정

def print_hex_with_lines(binary_data, start_line=None, end_line=None, bytes_per_line=16):
    # 전체 라인 수 계산 (마지막 라인이 덜 차 있을 수 있으므로 올림 처리)
    total_lines = (len(binary_data) + bytes_per_line - 1) // bytes_per_line

    # 시작 줄이 지정되지 않았으면 0부터 시작
    if start_line is None:
        start_line = 0

    # 끝 줄이 지정되지 않았거나 범위를 넘으면 마지막 줄까지로 설정
    if end_line is None or end_line >= total_lines:
        end_line = total_lines - 1

    # 바이트 인덱스 범위 계산
    start = start_line * bytes_per_line
    end = (end_line + 1) * bytes_per_line

    # 지정된 줄 범위만큼 출력
    for i in range(start, min(end, len(binary_data)), bytes_per_line):
        line_data = binary_data[i:i+bytes_per_line]

        # 16진수 부분: 바이트를 2자리 대문자 헥스로 출력, 바이트 간 두 칸 간격
        hex_part = '  '.join(f'{b:02X}' for b in line_data)

        # ASCII 부분: 출력 가능한 문자(32~126)만 그대로, 나머지는 '.' 처리
        ascii_part = ''.join(chr(b) if 32 <= b <= 126 else '.' for b in line_data)

        # 줄 번호(주소), 헥스 값, ASCII 출력
        print(f'{i:08X}  {hex_part:<{bytes_per_line*3}}  {ascii_part}')


# 사용 예시
with open('example.bin', 'rb') as f:
    data = f.read()
    # 줄 범위 지정 없이 전체 출력
    print_hex_with_lines(data)

# 사용 예시
with open('example.bin', 'rb') as f:
    data = f.read()
    # 줄 범위 지정 후 지정한 부분만 출력
    print_hex_with_lines(data, start_line=0, end_line=20, bytes_per_line=16)

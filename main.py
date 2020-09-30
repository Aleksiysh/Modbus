import modbus_tk.defines as cst
import modbus_tk.modbus_tcp as modbus_tcp
import struct



def to_float(arr):
    group_array = [tuple(arr[d:d + 4]) for d in range(0, len(arr), 4)]
    return float_arr(group_array)


def float_arr(arr):
    dd = []
    for t in arr:
        k, = struct.unpack("!f", t[2] + t[3] + t[0] + t[1])
        dd.append(k)
    return tuple(dd)


def main():
    host = "192.168.1.2"
    port = "502"
    master = modbus_tcp.TcpMaster(host=host, port=int(port), timeout_in_sec=5)
    slave = 1
    function_code = cst.READ_INPUT_REGISTERS
    starting_address = 0
    quantity_of_x = 84
    while True:
        get_di = master.execute(slave,
                                function_code,
                                starting_address,
                                quantity_of_x,
                                data_format=f"{quantity_of_x * 2}c"
                                )
        f = to_float(get_di)
        round_f = tuple(map(lambda a: round(a, 3), f))
        # print(round_f)
        # ext = [(round_f[d:d + 5]) for d in range(0, len(round_f), 6)]
        print(*[(round_f[d:d + 5]) for d in range(0, len(round_f), 6)], sep="\n")
        print()

    f_100 = [17.269498825073242, 0.0, 18.0, 0.5, 50.0, 1.1020946175206465e-39, 0.0, 0.0, 0.0, 0.0, -50.0,
             1.1020946175206465e-39, 0.0, 0.0, 0.0, 0.0, 0.0, 1.1020946175206465e-39, 0.0, 0.0, 0.0, 0.0, 0.0,
             1.1020946175206465e-39, 0.0, 0.0, 0.0, 0.0, 0.0, 1.1020946175206465e-39, 0.0, 0.0, 0.0, 0.0, 0.0,
             1.1020946175206465e-39, 0.0, 0.0, 0.0, 0.0, 0.0, 1.1020946175206465e-39, 1.8664011850778872e-14,
             1.8661978971705462e-14, 0.0, 9.42324492633588e-15, 6.77377320901229e-10, 6.411114972237897e-10,
             2.6175301075931356e-12, 0.002688419073820114]
    get_id_for_7_nods = (
    b'\xe9', b'\xd7', b'@', b'$', b'\xc2', b'\xd3', b'E', b'\x05', b'\x00', b'\x00', b'?', b'\x80', b'\xcc', b'\xcd',
    b'=', b'\xcc', b'\x00', b'\x00', b'?', b'\x80', b'\x00', b'G', b'\x00', b'\r', b'\xa0', b'\x1b', b'@', b'\x8e',
    b']', b'\xd2', b'E', b'g', b'\x00', b'\x00', b'@', b'\x00', b'\xcc', b'\xcd', b'>', b'L', b'\x00', b'\x00', b'@',
    b'\x00', b'\x00', b'G', b'\x00', b'\r', b'\x16', b'\xdb', b'@', b'\xca', b'\xea', b'\x10', b'E', b'\xa3', b'\x00',
    b'\x00', b'@', b'@', b'\x99', b'\x9a', b'>', b'\x99', b'\x00', b'\x00', b'@', b'@', b'\x00', b'G', b'\x00', b'\r',
    b'*', b'\xdf', b'A', b'\x02', b'(', b'C', b'E', b'\xd3', b'\x00', b'\x00', b'@', b'\x80', b'\xcc', b'\xcd', b'>',
    b'\xcc', b'\x00', b'\x00', b'@', b'\x80', b'\x00', b'G', b'\x00', b'\r', b'\x1b', b'\xa7', b'A', b'\x1f', b'\r',
    b'a', b'F', b'\x01', b'\x00', b'\x00', b'@', b'\xa0', b'\x00', b'\x00', b'?', b'\x00', b'\x00', b'\x00', b'@',
    b'\xa0', b'\x00', b'G', b'\x00', b'\r', b'\xe9', b'\x04', b'A', b';', b'i', b'\xe7', b'F', b'\x18', b'\x00',
    b'\x00', b'@', b'\xc0', b'\x99', b'\x9a', b'?', b'\x19', b'\x00', b'\x00', b'@', b'\xc0', b'\x00', b'G', b'\x00',
    b'\r', b'\x98', b'\x14', b'A', b'X', b'\xad', b'\xd9', b'F', b'/', b'\x00', b'\x00', b'@', b'\xe0', b'3', b'3',
    b'?', b'3', b'\x00', b'\x00', b'@', b'\xe0', b'\x00', b'G', b'\x00', b'\r')

    qwe_100 = (
        b"'", b'\xef', b'A', b'\x8a', b'\x00', b'\x00', b'\x00', b'\x00', b'\x00', b'\x00', b'A', b'\x90', b'\x00',
        b'\x00',
        b'?', b'\x00', b'\x00', b'\x00', b'B', b'H', b'\x00', b'1', b'\x00', b'\x0c', b'\x00', b'\x00', b'\x00',
        b'\x00',
        b'\x00', b'\x00', b'\x00', b'\x00', b'\x00', b'\x00', b'\x00', b'\x00', b'\x00', b'\x00', b'\x00', b'\x00',
        b'\x00',
        b'\x00', b'\xc2', b'H', b'\x00', b'1', b'\x00', b'\x0c', b'\x00', b'\x00', b'\x00', b'\x00', b'\x00', b'\x00',
        b'\x00', b'\x00', b'\x00', b'\x00', b'\x00', b'\x00', b'\x00', b'\x00', b'\x00', b'\x00', b'\x00', b'\x00',
        b'\x00',
        b'\x00', b'\x00', b'1', b'\x00', b'\x0c', b'\x00', b'\x00', b'\x00', b'\x00', b'\x00', b'\x00', b'\x00',
        b'\x00',
        b'\x00', b'\x00', b'\x00', b'\x00', b'\x00', b'\x00', b'\x00', b'\x00', b'\x00', b'\x00', b'\x00', b'\x00',
        b'\x00',
        b'1', b'\x00', b'\x0c', b'\x00', b'\x00', b'\x00', b'\x00', b'\x00', b'\x00', b'\x00', b'\x00', b'\x00',
        b'\x00',
        b'\x00', b'\x00', b'\x00', b'\x00', b'\x00', b'\x00', b'\x00', b'\x00', b'\x00', b'\x00', b'\x00', b'1',
        b'\x00',
        b'\x0c', b'\x00', b'\x00', b'\x00', b'\x00', b'\x00', b'\x00', b'\x00', b'\x00', b'\x00', b'\x00', b'\x00',
        b'\x00',
        b'\x00', b'\x00', b'\x00', b'\x00', b'\x00', b'\x00', b'\x00', b'\x00', b'\x00', b'1', b'\x00', b'\x0c',
        b'\x00',
        b'\x00', b'\x00', b'\x00', b'\x00', b'\x00', b'\x00', b'\x00', b'\x00', b'\x00', b'\x00', b'\x00', b'\x00',
        b'\x00',
        b'\x00', b'\x00', b'\x00', b'\x00', b'\x00', b'\x00', b'\x00', b'1', b'\x00', b'\x0c', b'\x1c', b'H', b'(',
        b'\xa8',
        b'\x17', b'\x98', b'(', b'\xa8', b'\x00', b'\x00', b'\x00', b'\x00', b'\xc1', b'\x0c', b'(', b')', b'2', b'1',
        b'0',
        b':', b':', b'6', b'0', b'0', b'1', b';', b',', b'8', b'0', b'0', b';', b'0')


if __name__ == '__main__':
    main()

import modbus_tk.defines as cst
import modbus_tk.modbus_tcp as modbus_tcp
import struct


def to_float(arr):
    group_array = [list(arr[d:d+4]) for d in range(0, len(arr), 4)]
    return float_arr(group_array)


def float_arr(arr):
    dd = []
    for t in arr:
        k, = struct.unpack("!f", t[2] + t[3] + t[0] + t[1])
        dd.append(k)
    return dd


def main():
    host = "192.168.1.2"
    port = "502"
    master = modbus_tcp.TcpMaster(host=host, port=int(port), timeout_in_sec=5)
    slave = 1
    function_code = cst.READ_INPUT_REGISTERS
    starting_address = 0
    quantity_of_x = 100

    get_di = master.execute(slave,
                            function_code,
                            starting_address,
                            quantity_of_x,
                            data_format=f"{quantity_of_x * 2}c"
                            )
    f = to_float(get_di)
    print(f)

    f_100 = [17.269498825073242, 0.0, 18.0, 0.5, 50.0, 1.1020946175206465e-39, 0.0, 0.0, 0.0, 0.0, -50.0,
             1.1020946175206465e-39, 0.0, 0.0, 0.0, 0.0, 0.0, 1.1020946175206465e-39, 0.0, 0.0, 0.0, 0.0, 0.0,
             1.1020946175206465e-39, 0.0, 0.0, 0.0, 0.0, 0.0, 1.1020946175206465e-39, 0.0, 0.0, 0.0, 0.0, 0.0,
             1.1020946175206465e-39, 0.0, 0.0, 0.0, 0.0, 0.0, 1.1020946175206465e-39, 1.8664011850778872e-14,
             1.8661978971705462e-14, 0.0, 9.42324492633588e-15, 6.77377320901229e-10, 6.411114972237897e-10,
             2.6175301075931356e-12, 0.002688419073820114]

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

    pass


if __name__ == '__main__':
    main()

import modbus_tk
import modbus_tk.defines as cst
import modbus_tk.modbus_tcp as modbus_tcp
import struct


def to_float(arr):
    ss = []
    for i in range(0, len(arr), 4):
        ss.append(arr[i + 2])
        ss.append(arr[i + 3])
        ss.append(arr[i + 0])
        ss.append(arr[i + 1])

    ss = [([arr[d + 2], arr[d + 3], arr[d], arr[d + 1]]) for d in range(0, len(arr), 4)]

    res = [(ss[d:d + 4]) for d in range(0, len(ss), 4)]

    k = float_arr(res)
    return res

    pass


def float_arr(arr):
    dd = []
    for t in arr:
        a, b, c, d = tuple(t)
        k, = struct.unpack("!f", a + b + c + d)
        dd.append(k)

    pass


def main():
    host = "192.168.1.2"
    port = "502"
    master = modbus_tcp.TcpMaster(host=host, port=int(port), timeout_in_sec=5)
    slave = 1
    function_code = cst.READ_INPUT_REGISTERS
    starting_address = 0
    quantity_of_x = 20
    data_format = f"{quantity_of_x // 4}c"

    getDI = master.execute(slave,
                           function_code,
                           starting_address,
                           quantity_of_x,
                           data_format=f"{quantity_of_x * 2}c"
                           )

    pp = struct.pack("!f", -50.0)
    aa = to_float(getDI)

    a, b, c, d = to_float(getDI)[0]
    h = struct.unpack("!f", a + b + c + d)

    print(struct.unpack("!f", a + b + c + d))

    pass


if __name__ == '__main__':
    main()

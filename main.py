import modbus_tk
import modbus_tk.defines as cst
import modbus_tk.modbus_tcp as modbus_tcp
import struct


def to_float(arr):
    s = arr
    ss = []
    for i in range(0, len(arr), 4):
        ss.append(arr[i+3])
        ss.append(arr[i+4])
        ss.append(arr[i+0])
        ss.append(arr[i+1])

    res = [(ss[d:d + 4]) for d in range(0, len(ss), 4)]
    return res

    pass


def main():
    host = "192.168.1.2"
    port = "502"
    master = modbus_tcp.TcpMaster(host=host, port=int(port), timeout_in_sec=5)

    getDI = master.execute(1, cst.READ_INPUT_REGISTERS, 8, 2, data_format="!4c")

    pp = struct.pack("!f", -50.0)

    aa = to_float(getDI)

    a, b, c, d = to_float(getDI)[0]
    h = struct.unpack("f", a + b + c + d)

    print(struct.unpack("!f", a + b + c + d))

    pass


if __name__ == '__main__':
    main()

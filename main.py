import modbus_tk.defines as cst
import modbus_tk.modbus_tcp as modbus_tcp
import struct
import tkinter as tk

import table


def read_floats_from_modbas_tcp(master, slave, starting_address, quantity_of_x):
    '''
    функция чтения чисел типа float по MODBUS-TCP
    :param master: экземпляр подключения
    :param slave: slave = 1
    :param starting_address: начальный адрес
    :param quantity_of_x: количество чисел
    :return:
    '''
    tuple_of_bytes = master.execute(slave,
                                    cst.READ_INPUT_REGISTERS,
                                    starting_address,
                                    quantity_of_x * 2,
                                    data_format=f"{quantity_of_x * 4}c"
                                    )
    group_array = [tuple(tuple_of_bytes[d:d + 4]) for d in range(0, len(tuple_of_bytes), 4)]
    array_of_float = []
    for t in group_array:
        k, = struct.unpack("!f", t[2] + t[3] + t[0] + t[1])
        array_of_float.append(k)
    return tuple(array_of_float)


def main():
    """
    Точка входа
    :return: None
    """
    master = modbus_tcp.TcpMaster(host='192.168.1.2', port=502, timeout_in_sec=5)
    read_floats_from_modbas_tcp(master, 1, 0, 42)

    root = tk.Tk()
    # res = read_floats_from_modbas_tcp(master, 1, 0, 42)
    table1 = table.Table(root, headings=(
        'Узел', 'Массовый расход', 'Объемный расход', 'Перепад', 'Давление', 'Температура'),
                         rows=
                         to_rows(read_floats_from_modbas_tcp(master, 1, 0, 42), 6)
                         )
    table1.pack(expand=tk.YES, fill=tk.BOTH)
    root.mainloop()


def to_rows(tuple_in, len_group, prefix=(), suffix=()):
    """
    Разбивка на плоского кортежа на кортеж кортежей
    :param tuple_in: входной плоский кортеж
    :param len_group: длина внутреннего кортежа
    :param suffix: начало
    :param prefix: окончание
    :return: кортеж кортежей
    """
    print("AAAAAAAAAAAAAAAAAAAA")
    tt = [tuple_in[d:d + len_group] for d in range(0, len(tuple_in), len_group)]
    aa = list(map(lambda x: ('',) + x, list(tt)))
    return aa


if __name__ == '__main__':
    main()

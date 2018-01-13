import smbus
import time


class MPL():

    def __init__(self):

        self.pressure = 0
        self.cTemp = 0
        self.fTemp = 0
        self.altitude = 0

    def Value(self):

        bus = smbus.SMBus(1)


        bus.write_byte_data(0x60, 0x26, 0xB9)


        bus.write_byte_data(0x60, 0x13, 0x07)


        bus.write_byte_data(0x60, 0x26, 0xB9)

        time.sleep(1)

        data = bus.read_i2c_block_data(0x60, 0x00, 6)



        tHeight = ((data[1] * 65536) + (data[2] *256) + (data[3] & 0xF0)) / 16

        temp = ((data[4] * 256) + (data[5] & 0xF0)) / 16

        altitude = tHeight / 16.0

        cTemp = temp / 16.0

        fTemp = cTemp * 1.8 + 32
        bus.write_byte_data(0x60, 0x26, 0x39)

        time.sleep(1)


        data = bus.read_i2c_block_data(0x60, 0x00, 4)



        pres = ((data[1] + 65536) + (data[2] * 256) + (data[3] & 0xF0)) / 16

        pressure = (pres / 4.0) / 1000.0


        self.pressure = pressure
        self.fTemp = fTemp
        self.cTemp = cTemp
        self.altitude = altitude


        value = {'pressure': self.pressure, 'fTemp': self.fTemp, 'cTemp': self.cTemp, 'altitude': self.altitude}


        return value



    def get_pressure(self):

        return self.pressure

    def get_fTemp(self):
        return self.fTemp

    def get_cTemp(self):
        return self.cTemp

    def get_altitude(self):
        return self.altitude



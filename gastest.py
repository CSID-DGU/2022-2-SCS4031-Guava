import spidev
import time
spi=spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz=500000
def read_spi_adc(adcChannel):
    adcValue=0
    buff=spi.xfer([1,(8+adcChannel)<<4,0])
    adcValue=((buff[1]&3)<<8)+buff[2]
    return adcValue                                                                                                        
try:
    while True:
        adcChannel=0
        adcValue=read_spi_adc(adcChannel)
        print("gas %d"%adcValue)
        time.sleep(2.0)
except KeyboardInterrupt:
    spi.close()
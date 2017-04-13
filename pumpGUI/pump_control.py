# always seem to need this
import sys
import math
import serial
import time
import glob

# This gets the Qt stuff
import PyQt5
from PyQt5.QtWidgets import *

# This is our window from QtCreator
import mainwindow_auto

# create class for our GUI
class MainWindow(QMainWindow, mainwindow_auto.Ui_MainWindow):
    global screw_draw
    screw_draw = 5
    global steps
    steps = 200
    global gearing
    gearing = 100
    global stop
    stop = "s"
    stop = stop.encode()
    
    global min_freq
    min_freq = 31
    global max_freq
    max_freq = 970
    global ser1
    global out1
    
#   Define signals to be sent for fast empty/fill
    global fast_fill
    global fast_empty
    fast_fill = str(2) + " 0" + str(max_freq) + " " + str(9999) + " " + str(999)
    fast_fill = fast_fill.encode()
    fast_empty = str(1) + " 0" + str(max_freq) + " " + str(9999) + " " + str(999)
    fast_empty = fast_empty.encode()
    
    def serial_port_scan(self):
#       clear existing elements in comboBox
        self.serial_port.clear()
        if sys.platform.startswith('win'):
            ports = ['COM%s' % (i + 1) for i in range(256)]
        elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
            # this excludes your current terminal "/dev/tty"
            ports = glob.glob('/dev/tty[A-Za-z]*')
        elif sys.platform.startswith('darwin'):
            ports = glob.glob('/dev/tty.*')
        else:
            raise EnvironmentError('Unsupported platform')
    
        result = []
        for port in ports:
            try:
                s = serial.Serial(port)
                s.close()
                result.append(port)
            except (OSError, serial.SerialException):
                pass
#        Loop through array of port strings and add them to comboBox
        for port in result:
            self.serial_port.addItem(port)
        
        self.OK_btn.setEnabled(1)
        print(result)

    
    def pressedOKButton(self):
#            global ser1
#            serialPort = self.serial_port.currentText()
#        
#            ser1 = serial.Serial(serialPort,
#                                baudrate=9600,
#                                bytesize=serial.EIGHTBITS,
#                                parity=serial.PARITY_NONE,
#                                stopbits=serial.STOPBITS_ONE,
#                                timeout=1,
#                                xonxoff=0,
#                                rtscts=0
#                                )
#        
#            ser1.setDTR(False)
#            time.sleep(1)
#            ser1.flushInput()
#            ser1.flushOutput()
#            ser1.setDTR(True)
            self.syringe_btn.setEnabled(0)
            self.rate_btn.setEnabled(0)
            self.target_btn.setEnabled(0)
            self.run_btn.setEnabled(0)
            self.checkBox.setCheckable(0)
            self.stackedWidget.setCurrentIndex(0)


#    ser1 = serial.Serial('/dev/tty.usbmodemFA131',
#                         baudrate=9600,
#                         bytesize=serial.EIGHTBITS,
#                         parity=serial.PARITY_NONE,
#                         stopbits=serial.STOPBITS_ONE,
#                         timeout=1,
#                         xonxoff=0,
#                         rtscts=0
#                         )
#    # Serial port 2 to control ethanol syringe
#    ser2 = serial.Serial('/dev/tty.usbmodemFD121',
#                        baudrate=9600,
#                        bytesize=serial.EIGHTBITS,
#                        parity=serial.PARITY_NONE,
#                        stopbits=serial.STOPBITS_ONE,
#                        timeout=1,
#                        xonxoff=0,
#                        rtscts=0
#                        )
#                         
#    ser1.setDTR(False)
#    time.sleep(1)
#    ser1.flushInput()
#    ser1.flushOutput()
#    ser1.setDTR(True)
#    
#    ser2.setDTR(False)
#    time.sleep(1)
#    ser2.flushInput()
#    ser2.flushOutput()
#    ser2.setDTR(True)

    def encodePumpInstructions(self, dir, freq, secs, millis):
        dir = str(dir)
        freq = str(freq)
        secs = str(secs)
        millis = str(millis)
        
        if len(freq) == 1:
            freq = "000"+freq
        elif len(freq) ==2:
            freq = "00" + freq
        elif len(freq) == 3:
            freq = "0" + freq
        else:
            freq = freq
        
        if len(secs) == 1:
            secs = "000"+secs
        elif len(secs) ==2:
            secs = "00" + secs
        elif len(secs) == 3:
            secs = "0" + secs
        else:
            secs = secs
        
        if len(millis) == 1:
            millis = "00"+millis
        elif len(millis) ==2:
            millis = "0" + millis
        else:
            millis = millis
        
        out = dir + " " + freq + " " + secs + " " + millis
        out = out.encode()
        print(out)
        return out
    
    # Writes instructions to serial port.
    def serWrite(self, out):
        ser1.write(out)

    def sendStopInstructions(self):
        ser1.write(stop)
        ser1.close()
        ser1.open()


    def pressedModeButton(self):
#       When Mode button pressed, uncheck checkbox, clear subsequent display fields, and set all subsequent buttons to unclickable (except syringe button)
        self.checkBox.setChecked(0)
        self.rate_btn.setEnabled(0)
        self.target_btn.setEnabled(0)
        self.run_btn.setEnabled(0)
        self.checkBox.setCheckable(0)
        self.syringe_table.setItem(0,0,QTableWidgetItem(str(' ')))
        self.rate_table.setItem(0,0,QTableWidgetItem(str(' ')))
        self.target_table_time.setItem(0,0,QTableWidgetItem(str(' ')))
        self.target_table_vol.setItem(0,0,QTableWidgetItem(str(' ')))
        
#        Change to 'Mode' page
        self.stackedWidget.setCurrentIndex(1)

    def pressedSyringeButton(self):
#        When Syringe button pressed, uncheck checkbox, clear subsequent display fields, set all subsequent buttons to unclickable (except rate button)
        self.checkBox.setChecked(0)
        self.target_btn.setEnabled(0)
        self.run_btn.setEnabled(0)
        self.checkBox.setCheckable(0)
        self.rate_table.setItem(0,0,QTableWidgetItem(str(' ')))
        self.target_table_time.setItem(0,0,QTableWidgetItem(str(' ')))
        self.target_table_vol.setItem(0,0,QTableWidgetItem(str(' ')))
        
#        Change to 'Syringe' page
        self.stackedWidget.setCurrentIndex(2)
    
    def pressedRateButton(self):
#        When rate button pressed, uncheck checkbox, clear target display field, make checkbox & run button unclickable
        self.checkBox.setChecked(0)
        self.run_btn.setEnabled(0)
        self.checkBox.setCheckable(0)
        
        self.target_table_time.setItem(0,0,QTableWidgetItem(str(' ')))
        self.target_table_vol.setItem(0,0,QTableWidgetItem(str(' ')))

#       Depending on which rate units selected, min/max rates are adjusted
        global adjust
        global units
        global time_units
        
        if self.comboBox_3.currentIndex()==0:
            adjust = 1
            units = ' ul/sec'
            time_units = ' secs'
        elif self.comboBox_3.currentIndex()==1:
            adjust = 60
            units = ' ul/min'
            time_units = ' mins'
        elif self.comboBox_3.currentIndex()==2:
            adjust = 1/1000
            units = ' ml/sec'
            time_units = ' secs'
        elif self.comboBox_3.currentIndex()==3:
            adjust = 60/1000
            units = ' ml/min'
            time_units = ' mins'

#       Display min/max rates and step resolution
        self.maxrate_table.setItem(0,0,QTableWidgetItem(str(round(max_rate_uls*adjust,2))+ units))
        self.minrate_table.setItem(0,0,QTableWidgetItem(str(round(min_rate_uls*adjust,2))+ units))
        self.stepres_table.setItem(0,0,QTableWidgetItem(str(round(min_rate_uls/min_freq,3))+ ' ul/step'))
        self.units_table.setItem(0,0,QTableWidgetItem(units))

#       Change to 'Rates' page
        self.stackedWidget.setCurrentIndex(3)
    
    def pressedTargetButton(self):
#        Unchecks and sets checkbox to unclickable
        self.checkBox.setCheckable(0)
        self.checkBox.setChecked(0)
        self.stackedWidget.setCurrentIndex(4)
    
    def pressedRunButton(self):
#        Re-enable Stop button in case of stop/restart
        self.stop_btn.setEnabled(1)
        
        global microstepping
        microstepping = 1
        
#        Redundant checkBox verification
        if self.checkBox.isChecked()==1:
#            Checks if target is volume or time, converts to volume
            if self.radioButton.isChecked()==1:
                volume = target_ul
            else:
                volume = rate_uls*target_sec
            
#            Performs calculations for frequency with microstepping off
            steps_rev = steps*gearing*microstepping
            vol_rev = plunger_area*screw_draw
            vol_step = vol_rev/steps_rev
            min_volsec = vol_step*min_freq
            
#            If calculated rate is below min rate, turn microstepping on
#            Use while loop to increase microstepping until condition satisfied?
            if min_volsec>rate_uls:
                microstepping = 8
            else:
                microstepping = 1
            
#            Re-perform calculations with new microstepping value to calculate drive freq
            steps_rev = steps*gearing*microstepping
            vol_rev = plunger_area*screw_draw
            vol_step = vol_rev/steps_rev
            freq = round(rate_uls/vol_step)
            
#            Calculate pump time and split into secs/millis
            pump_time = volume/rate_uls
            pump_time_secs = math.floor(pump_time)
            pump_time_millis = (pump_time-pump_time_secs)*1000
            
#           Changes time display to minutes if larger than 60 secs, possible problem with 'time_units', 'adjust' and 'units' being declared as global in both 'RateChanged' function and 'RatePressed' function
            if time_units == ' mins':
                pump_time = pump_time/60

            
#            Print results to Terminal for verification purposes
            print(freq)
            print(pump_time)
            print(mode)
            print(microstepping)
            
#            out = self.encodePumpInstructions(mode,freq,pump_time_secs,pump_time_millis)
#            serWrite(out)

#            Create display parameters for 'Progress' page
            if mode == 1:
                mode_str = 'Pumping'
            elif mode == 2:
                mode_str = 'Filling'
            
#            Display parameters on 'Progress' page
            self.display_mode_table.setItem(0,0,QTableWidgetItem(mode_str))
#            For some reason this is not converting to selected rate units, always stays at ul/s and secs
            self.display_rate_table.setItem(0,0,QTableWidgetItem(str(round(rate_uls*adjust,2))+ units))
            self.display_time_table.setItem(0,0,QTableWidgetItem(str(round(pump_time,2))+time_units))
            print(rate_uls)
            print(adjust)
            print(units)
#           Sets page to 'Progress' page
            self.stackedWidget.setCurrentIndex(5)
            
#            Listen for 'finished pumping' signal from Arduino, might be bocking the stop button?
            while 1:
                finished = ser1.readLine()
                if finished == "end":
                    ser1.close()
                    ser1.open()
                    self.stackedWidget.setCurrentIndex(1)
                    exit()
                else:
                    continue



    def pressedDoneButton(self):
#        Defines different actions depending on which 'Done' button is pressed, might be better to have individiual functions for each

        if self.stackedWidget.currentIndex()==1: # Set mode
            global mode
            if self.comboBox.currentIndex()==0:
                self.mode_table.setItem(0,0,QTableWidgetItem('Pumping'))
                mode = 1
            else:
                self.mode_table.setItem(0,0,QTableWidgetItem('Filling'))
                mode = 2
            
#            Enable syringe button to be pressed
            self.syringe_btn.setEnabled(1)

        elif self.stackedWidget.currentIndex()==2: # Set syringe dimensions
            global syringe_vol_ml
            global plunger_area
            global max_rate_uls
            global min_rate_uls
            
#            Hamilton 5ml and 10ml hard-coded, Custom setting is default
            if self.comboBox_2.currentIndex()==1:
                syringe_vol_ml = 5
                plunger_area = 83.32
                dimensions = ' '
            elif self.comboBox_2.currentIndex()==2:
                syringe_vol_ml = 10
                plunger_area = 166.73
                dimensions = ' '
            elif self.comboBox_2.currentIndex()==0:
                syringe_vol_ml = self.spinBox_4.value()
                plunger_area = math.pi*math.pow(self.doubleSpinBox.value()/2,2)
                dimensions = ' ' + str(syringe_vol_ml) + 'ml'
    
#           Calculates max and min rates, based on 31Hz and 970Hz limits of Uno (might be useful to re-test max rate with motor)
            max_rate_uls = max_freq*(plunger_area*screw_draw)/(steps*gearing)
            min_rate_uls = min_freq*(plunger_area*screw_draw)/(steps*gearing)
            
#           Sets the min and max rates of spinBox on 'Rates' page
            self.rate_box.setMinimum(round(min_rate_uls,2))
            self.rate_box.setMaximum(round(max_rate_uls,2))
            
#           Enable 'Rate' button
            self.rate_btn.setEnabled(1)
            
#            Update 'Syringe' display field
            self.syringe_table.setItem(0,0,QTableWidgetItem(self.comboBox_2.currentText() + dimensions))
        
        elif self.stackedWidget.currentIndex()==3: # Set flow rates
            global rate_uls
#           Depending on rates units, define rate_uls as always in ul/sec
            if self.comboBox_3.currentIndex()==0:
                rate_uls = self.rate_box.value()
            elif self.comboBox_3.currentIndex()==1:
                rate_uls = self.rate_box.value()/60
            elif self.comboBox_3.currentIndex()==2:
                rate_uls = self.rate_box.value()*1000
            elif self.comboBox_3.currentIndex()==3:
                rate_uls = self.rate_box.value()*1000/60
            
#           Set max volume/time display fields of 'Target' page
            self.max_vol_table.setItem(0,0,QTableWidgetItem(str(syringe_vol_ml)+ 'ml'))
            self.max_time_table.setItem(0,0,QTableWidgetItem(str(round((syringe_vol_ml*1000)/rate_uls))+ ' secs'))

#           Set max values of spinBoxes on 'Target' page
            self.spinBox_2.setMaximum(syringe_vol_ml*1000)
            self.spinBox_3.setMaximum(round((syringe_vol_ml*1000)/rate_uls))

#           Set display field on 'Configuration' page to show selected rate
            self.rate_table.setItem(0,0,QTableWidgetItem(str(self.rate_box.value())+ ' ' + self.comboBox_3.currentText()))

#           Enable 'Target' button
            self.target_btn.setEnabled(1)
        
        elif self.stackedWidget.currentIndex()==4: # Set target vol or time
            global target_ul
            global target_sec

#           Depending on target mode selected, update target volume or time values
            if self.radioButton.isChecked()==1:
                target_ul = self.spinBox_2.value()
                target_sec = target_ul/rate_uls
                self.target_table_vol.setItem(0,0,QTableWidgetItem(str(target_ul) + ' ul'))
                self.target_table_time.setItem(0,0,QTableWidgetItem(str(round(target_sec,2))+ ' secs'))
            else:
                target_sec = self.spinBox_3.value()
                target_ul = target_sec*rate_uls
                self.target_table_time.setItem(0,0,QTableWidgetItem(str(target_sec) + ' secs'))
                self.target_table_vol.setItem(0,0,QTableWidgetItem(str(round(target_ul,2))+ ' ul'))

#           Set checkBox to checkable after all fields have been filled
            self.checkBox.setCheckable(1)
                
#       After each press of 'Done' button, always revert to 'Configuration' screen
        self.stackedWidget.setCurrentIndex(0)
    
    def pressedStopButton(self):
#       Send stop instructions, delay for 100ms, then revert to 'Configuration' page. Also clear display fields for 'Progress' page
        #self.sendStopInstructions()
        self.stop_btn.setEnabled(0)
        time.sleep(0.1)
        self.stackedWidget.setCurrentIndex(0)
        self.display_mode_table.setItem(0,0,QTableWidgetItem(' '))
        self.display_time_table.setItem(0,0,QTableWidgetItem(' '))
        self.display_rate_table.setItem(0,0,QTableWidgetItem(' '))

    def checkBoxChanged(self):
#       Every time checkBox is checked/unchecked, enable/disable 'Run' button
        if self.checkBox.isChecked()==1:
            self.run_btn.setEnabled(1)
        else:
            self.run_btn.setEnabled(0)


    def pressedFillButton(self):
#        self.serWrite(fast_fill)
        print('x')
    
    def releasedFillButton(self):
#        self.sendStopInstructions()
        print('stop')
    
    def pressedEmptyButton(self):
#        self.serWrite(fast_empty)
        print('x')
    
    def releasedEmptyButton(self):
#        self.sendStopInstructions()
        print('stop')
    
    def rateChanged(self):
        global adjust
        global units
        global time_units
        
#       Every time the 'rates' comboBox is changed, update adjust parameter and units
        if self.comboBox_3.currentIndex()==0:
            adjust = 1
            units = ' ul/sec'
            time_units = ' secs'
        elif self.comboBox_3.currentIndex()==1:
            adjust = 60
            units = ' ul/min'
            time_units = ' mins'
        elif self.comboBox_3.currentIndex()==2:
            adjust = 1/1000
            units = ' ml/sec'
            time_units = ' secs'
        elif self.comboBox_3.currentIndex()==3:
            adjust = 60/1000
            units = ' ml/min'
            time_units = ' mins'

#       Update the max/min rates to reflect change in units
        self.maxrate_table.setItem(0,0,QTableWidgetItem(str(round(max_rate_uls*adjust,2))+ units))
        self.minrate_table.setItem(0,0,QTableWidgetItem(str(round(min_rate_uls*adjust,2))+ units))
        
#        Update max/min constraints to reflect change in units
        self.rate_box.setMinimum(round(min_rate_uls*adjust,2))
        self.rate_box.setMaximum(round(max_rate_uls*adjust,2))
        
#        Update units field to the right of rate_box
        self.units_table.setItem(0,0,QTableWidgetItem(units))




    # access variables inside of the UI's file
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self) # gets defined in the UI file
        self.scan_btn.clicked.connect(lambda: self.serial_port_scan())
        self.mode_btn.clicked.connect(lambda: self.pressedModeButton())
        self.OK_btn.clicked.connect(lambda: self.pressedOKButton())
        self.rate_btn.clicked.connect(lambda: self.pressedRateButton())
        self.run_btn.clicked.connect(lambda: self.pressedRunButton())
        self.syringe_btn.clicked.connect(lambda: self.pressedSyringeButton())
        self.target_btn.clicked.connect(lambda: self.pressedTargetButton())
        self.done1_btn.clicked.connect(lambda: self.pressedDoneButton())
        self.done2_btn.clicked.connect(lambda: self.pressedDoneButton())
        self.done3_btn.clicked.connect(lambda: self.pressedDoneButton())
        self.done4_btn.clicked.connect(lambda: self.pressedDoneButton())
        self.stop_btn.clicked.connect(lambda: self.pressedStopButton())
        self.comboBox_3.currentIndexChanged.connect(lambda: self.rateChanged())
        self.checkBox.stateChanged.connect(lambda: self.checkBoxChanged())
        self.fill_btn.pressed.connect(lambda: self.pressedFillButton())
        self.fill_btn.released.connect(lambda: self.releasedFillButton())
        self.empty_btn.pressed.connect(lambda: self.pressedEmptyButton())
        self.empty_btn.released.connect(lambda: self.releasedEmptyButton())


# I feel better having one of these
def main():
    # a new app instance
    app = QApplication(sys.argv)
    form = MainWindow()
    form.show()
    # without this, the script exits immediately.
    sys.exit(app.exec_())

# python bit to figure how who started This
if __name__ == "__main__":
    main()
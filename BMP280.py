#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""BMP280: The BMP280 is an absolute barometric pressure sensor especially designed for mobile applications."""

__author__     = "ChISL"
__copyright__  = "TBD"
__credits__    = ["Bosch Sensortec"]
__license__    = "TBD"
__version__    = "Version 0.1"
__maintainer__ = "https://chisl.io"
__email__      = "info@chisl.io"
__status__     = "Test"

#
#   THIS FILE IS AUTOMATICALLY CREATED
#    D O     N O T     M O D I F Y  !
#

from BMP280_constants import *

# name:        BMP280
# description: The BMP280 is an absolute barometric pressure sensor especially designed for mobile applications.
# manuf:       Bosch Sensortec
# version:     Version 0.1
# url:         https://ae-bst.resource.bosch.com/media/_tech/media/datasheets/BST-BMP280-DS001-18.pdf
# date:        2017-09-02


# Derive from this class and implement read and write
class BMP280_Base:
	"""The BMP280 is an absolute barometric pressure sensor especially designed for mobile applications."""
	# Register DEVID
	# Fixed device ID 
	
	def setDEVID(self, val):
		"""Set register DEVID"""
		self.write(REG.DEVID, val, 8)
	
	def getDEVID(self):
		"""Get register DEVID"""
		return self.read(REG.DEVID, 8)
	
	# Bits DEVID
	# Register ID
	# The "id" register contains the chip identification number chip_id[7:0], which is 'h58.
	#       This number can be read as soon as the device finished the power-on-reset. 
	
	
	def setID(self, val):
		"""Set register ID"""
		self.write(REG.ID, val, 8)
	
	def getID(self):
		"""Get register ID"""
		return self.read(REG.ID, 8)
	
	# Bits ID
	# Register RESET
	# The "reset" register contains the soft reset word reset[7:0].
	#       If the value 'hB6 is written to the register, the device is reset using the
	#       complete power-on-reset procedure. Writing other values than 'hB6 has no effect.
	#       The readout value is always 0x00. 
	
	
	def setRESET(self, val):
		"""Set register RESET"""
		self.write(REG.RESET, val, 8)
	
	def getRESET(self):
		"""Get register RESET"""
		return self.read(REG.RESET, 8)
	
	# Bits RESET
	# Register STATUS
	# The "status" register contains two bits which indicate the status of the device. 
	
	def setSTATUS(self, val):
		"""Set register STATUS"""
		self.write(REG.STATUS, val, 8)
	
	def getSTATUS(self):
		"""Get register STATUS"""
		return self.read(REG.STATUS, 8)
	
	# Bits IM_UPDATE
	# Automatically set to ‘1’ whenever a conversion is running and
	#           back to ‘0’ when the results have been transferred to the data registers. 
	
	# Bits MEASURING
	# Automatically set to ‘1’ when the NVM data are being copied to image registers
	#           and back to ‘0’ when the copying is done. The data are copied at power-on-reset
	#           and before every conversion. 
	
	# Register CTRL_MEAS
	# The "ctrl_meas" register sets the data acquisition options of the device. 
	
	def setCTRL_MEAS(self, val):
		"""Set register CTRL_MEAS"""
		self.write(REG.CTRL_MEAS, val, 8)
	
	def getCTRL_MEAS(self):
		"""Get register CTRL_MEAS"""
		return self.read(REG.CTRL_MEAS, 8)
	
	# Bits OSRS_T
	# Controls oversampling of temperature data. See chapter 3.3.2 for details. 
	# Bits OSRS_P
	# Controls oversampling of pressure data. See chapter 3.3.1 for details. 
	# Bits MODE
	# Controls the power mode of the device. See chapter 3.6 for details. 
	# Register CONFIG
	# The "config" register sets the rate, filter and interface options of the device. Writes to the "config"
	#       register in normal mode may be ignored. In sleep mode writes are not ignored. 
	
	
	def setCONFIG(self, val):
		"""Set register CONFIG"""
		self.write(REG.CONFIG, val, 8)
	
	def getCONFIG(self):
		"""Get register CONFIG"""
		return self.read(REG.CONFIG, 8)
	
	# Bits T_SB
	# Controls inactive duration tstandby in normal mode. See chapter 3.6.3 for details. 
	# Bits FILTER
	# Controls the time constant of the IIR filter. See chapter 3.3.3 for details. 
	# Bits unused_0
	# Bits SPI3WEN
	# Enables 3-wire SPI interface when set to ‘1’. See chapter 5.3 for details. 
	# Register PRESS
	# The "press" register contains the raw pressure measurement output data up[19:0].
	#       For details on how to read out the pressure and temperature information from the device,
	#       please consult chapter 3.9.
	
	
	def setPRESS(self, val):
		"""Set register PRESS"""
		self.write(REG.PRESS, val, 24)
	
	def getPRESS(self):
		"""Get register PRESS"""
		return self.read(REG.PRESS, 24)
	
	# Bits PRESS
	# raw pressure measurement output data §
	# Register TEMP
	# The "temp" register contains the raw temperature measurement output data ut[19:0].
	#       For details on how to read out the pressure and temperature information from the device,
	#       please consult chapter 3.9. 
	
	
	def setTEMP(self, val):
		"""Set register TEMP"""
		self.write(REG.TEMP, val, 24)
	
	def getTEMP(self):
		"""Get register TEMP"""
		return self.read(REG.TEMP, 24)
	
	# Bits TEMP
	# raw temperature measurement output data §
	# Register CALIB
	
	
	def setCALIB(self, val):
		"""Set register CALIB"""
		self.write(REG.CALIB, val, 208)
	
	def getCALIB(self):
		"""Get register CALIB"""
		return self.read(REG.CALIB, 208)
	
	# Bits CALIB

#!/usr/bin/env python3

ActualAnalogInputs = {
    'Analog1': 167772417,
    'Analog2': 167772673,
    'Analog3': 167772929,
    'Analog4': 167773185,
}

ActualBattery = {
    'Voltage': 33556226,
    'Charge': 33556229,
    'Current': 33556238,
    'CurrentDir': 33556230,
    'ChargeCycles': 33556228,
    'Temperature': 33556227,
}

ActualGrid = {
    'GridOutputPower': 67109120,
    'GridFreq': 67110400,
    'GridCosPhi': 67110656,
    'GridLimitation': 67110144,
    'GridVoltageL1': 67109378,
    'GridCurrentL1': 67109377,
    'GridPowerL1': 67109379,
    'GridVoltageL2': 67109634,
    'GridCurrentL2': 67109633,
    'GridPowerL2': 67109635,
    'GridVoltageL3': 67109890,
    'GridCurrentL3': 67109889,
    'GridPowerL3': 67109891,
}

ActualHome = {
    'AktHomeConsumptionSolar': 83886336,
    'AktHomeConsumptionBat': 83886592,
    'AktHomeConsumptionGrid': 83886848,
    'PhaseSelHomeConsumpL1': 83887106,
    'PhaseSelHomeConsumpL2': 83887362,
    'PhaseSelHomeConsumpL3': 83887618,
}

ActualGenerator = {
    'dc1Voltage': 33555202,
    'dc1Current': 33555201,
    'dc1Power': 33555203,
    'dc2Voltage': 33555458,
    'dc2Current': 33555457,
    'dc2Power': 33555459,
    'dc3Voltage': 33555714,
    'dc3Current': 33555713,
    'dc3Power': 33555715,
}

ActualSZeroIn = {
    'S0InPulseCnt': 184549632,
    'Loginterval': 150995968,
}

Home = {
    'dcPowerPV': 33556736,
    'acPower': 67109120,
    'ownConsumption': 83888128,
    'batStateOfCharge': 33556229,
    # TODO: statusCodes
    'operatingStatus': 16780032,
}

InfoVersions = {
    'VersionUI': 16779267,
    'VersionFW': 16779265,
    'VersionHW': 16779266,
    'VersionPAR': 16779268,
    'SerialNumber': 16777728,
    'ArticleNumber': 16777472,
    'CountrySettingsName': 16779522,
    'CountrySettingsVersion': 16779521,
}

StatisticDay = {
    'Yield': 251658754,
    'HomeConsumption': 251659010,
    'OwnConsumption': 251659266,
    'OwnConsRate': 251659278,
    'AutonomyDegree': 251659279,
}

StatisticTotal = {
    'Yield': 251658753,
    'OperatingTime': 251658496,
    'HomeConsumption': 251659009,
    'OwnConsumption': 251659265,
    'OwnConsRate': 251659280,
    'AutonomyDegree': 251659281,
}
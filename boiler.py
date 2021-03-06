# -*- coding: utf-8 -*-
"""
Module consists class representing boilers.
"""
import annuity
import database


class Boiler(annuity.Annuity):
    """
    Class representing boiler technology.

    Attributes:
        model_name: Model of the boiler.
        th_capacity: Thermal capacity of the boiler [kW].
        efficiency: Efficiency of the boiler [decimal<1].
        heat_hourly: Hourly values of the heat provided by the boiler unit [kWh].
        heat_yearly: Sum value of heat provided by the boiler unit over the year [kWh].
        annuity: Annuity of the boiler [Euros].
        emissions: CO2 emissions of the boiler [kg of CO2].
    Extends:
        Annuity class
    """

    def __init__(self, model):
        """
        Constructor method for class Boiler.

        :param model: Tuple containing information about the boiler model in the form (model_name, thermal capacity,
                                                                                       thermal efficiency)
        :return: none
        """
        self.model_name = model[0]
        self.th_capacity = model[1]
        self.efficiency = model[2]
        # Initialising other variables to zero.
        self.heat_hourly = [0]*8760
        self.heat_yearly = 0
        self.annuity = 0
        self.emissions = 0
        # The depreciation period, finst, fwins and effop are different for
        # different capacities according to VDI 2067.
        super(Boiler, self).__init__(deperiod=database.annuity_factors['B'][0],
                                     effop=database.annuity_factors['B'][1],
                                     fwins=database.annuity_factors['B'][2],
                                     finst=database.annuity_factors['B'][3],
                                     obperiod=database.annuity_factors['Common'][0],
                                     q=database.annuity_factors['B'][4],
                                     r=database.annuity_factors['B'][5],
                                     gas_price=database.annuity_factors['Common'][1],
                                     electricity_price=database.annuity_factors['Common'][2])

    def get_heat(self, required_heat, hour):
        """
        Given the required heat, function calculates the hourly heat met by the boiler and returns the value for
        unsatisfied thermal demand.

        :param required_heat: Hourly thermal demand [kWh].
        :param hour: Hour of the year[hour].
        :return: required_heat: Hourly thermal demand not met by the boiler unit [kWh].
        """
        # If thermal capacity is more than hourly thermal demand, meet the
        # demand entirely.
        if required_heat <= self.th_capacity:
            self.heat_yearly += required_heat
            self.heat_hourly[hour] = required_heat
            required_heat = 0
        # If hourly thermal demand is greater than the capacity, meet as much
        # as possible.
        else:
            self.heat_yearly += self.th_capacity
            self.heat_hourly[hour] = self.th_capacity
            required_heat -= self.th_capacity
        return required_heat

    def set_emissions(self):
        """
        Calculates the CO2 emissions of the boiler unit.

        :param: none
        :return: none
        """
        # CO2 emissions of condensing boilers are about 56 g/MJ or 201.6 g/kWh.
        # [R Dones, Thomas Heck, and S Hirschberg. Greenhouse gas emissions
        # from energy systems:comparison and overview. 2004.]
        self.emissions = (201.6*self.heat_yearly/1000)
        return

    def set_annuity(self):
        """
        Calculates the annuity of the boiler unit.

        :param: none
        :return: none
        """
        # Capital related costs for the boiler include price of purchase and
        # installation costs.
        self.A0 = 79.061*self.th_capacity + 1229.8
        self.set_ank()

        # Demand related costs include price of fuel to produce required heat
        drc = self.gas_price*self.heat_yearly/self.efficiency
        self.Anv = drc*self.a*self.bv

        # Operation related costs include maintenance and repair
        orc = 30*self.effop
        ain = self.A0*(self.finst + self.fwins)/100   # finst and fwins in %
        self.Anb = orc*self.a*self.bb + ain*self.a*self.bi

        # Other costs
        self.Ans = 0

        # Proceeds
        self.Ane = 0

        self.annuity = self.Ane - (self.Ank + self.Anv + self.Anb + self.Ans)
        return
# b=Boiler('Model',11.2,0.98)
# print b.emissions

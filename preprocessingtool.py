# -*- coding: utf-8 -*-
from xlrd import open_workbook
from xlutils.copy import copy
import os
import itertools
import xlsxwriter
import shutil
import CHP
import Boiler
import ElectricHeater

class PreProcessingTool:
    """PreProcessingTool
    
    Attributes:
    building_id : Building ID of the particular building
    th_technologies : List of the thermal technologies to be considered
    el_technologies : List of the thermal technologies to be considered
    max_el_technologies : Maximum number of electrical technologies to be considered
    min_el_technologies : Minimum number of electrical technologies to be considered
    max_th_technologies : Maximum number of thermal technologies to be considered
    min_th_technologies : Minimum number of thermal technologies to be considered
    Location : Address of the folder where the ouput folder is to be created"""
    
    def __init__(self,building_id,thermal_profile,\
                maxr_thermal_power=0,
                maxr_hours=0,
                peak_thermal_power=0,th_technologies = ["CHP","B","ElHe"],\
                el_technologies = ["CHP"],\
                max_el_technologies = 1,\
                min_el_technologies = 1,\
                max_th_technologies = 2,\
                min_th_technologies = 0,\
                hourly_excels = True,\
                location = "D:/aja-gmu/Simulation_Files/Output"):
        self.thermal_profile = thermal_profile
        self.building_id = building_id
        self.th_technologies = th_technologies
        self.el_technologies = el_technologies
        self.max_el_technologies = max_el_technologies
        self.min_el_technologies = min_el_technologies
        self.max_th_technologies = max_th_technologies
        self.min_th_technologies = min_th_technologies
        self.location = location
        self.hourly_excels = hourly_excels
        self.maxr_thermal_power,self.maxr_hours = self.getMaximumRectangle(thermal_profile)
        self.peak_thermal_power = max(thermal_profile)
        self.KPI = []
        self.EconomicFactors = []

    def generateCases(self):
        """Generates the scenarios"""
        
        os.chdir(self.location)
        if not os.path.exists(self.location+"/"+self.building_id):  # Make the output folder if it does not exist
            os.makedirs(self.location+"/"+self.building_id)
        
        os.chdir(self.location+"/"+self.building_id)  # Change to the folder
        for the_file in os.listdir(self.location+"/"+self.building_id): # Delete all the old files and folders
            file_path = os.path.join(self.location+"/"+self.building_id, the_file)
            if os.path.isfile(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path): 
                shutil.rmtree(file_path)
    
        
        #Load thermal profile and weather data
        technologies = list(set(self.th_technologies).union(self.el_technologies))
        
        #------------------------------------------------------------------------------
        #Iterating from 1 to the maximum number of technologies 
        for number in range(1,len(technologies)+1):
            
            os.chdir(self.location+"/"+self.building_id)  # Change to the folder
            #Make seperate directories depending on the number of technologies present
            #in the system
            if (number <= self.max_el_technologies + self.max_th_technologies-1 \
            and number >= self.min_el_technologies+ self.min_th_technologies) and self.hourly_excels:      
                if not os.path.exists(str(number)+'technologies'):
                    os.makedirs(str(number)+'technologies')
        
                #Changing to the required directory in output directory
                os.chdir('./'+str(number)+'technologies')
                    
            #----------------------------------------------------------------------
            #Iterating through the various possible combinations.
            for system in itertools.combinations(technologies,number):
                    
                #Proceed further only if there is CHP present in the system
                if 'CHP' in system:
                    
                    #Proceed further is the number of technologies in the system are suitable
                    if (len(set(system) & set(self.el_technologies)) <= self.max_el_technologies\
                    and len(set(system) & set(self.th_technologies)) <= self.max_th_technologies \
                    and len(set(system) & set(self.el_technologies)) >= self.min_el_technologies \
                    and len(set(system) & set(self.th_technologies)) >= self.min_th_technologies):               
                                
                        # Create classes of the technologies
                        print '\n\n====================System-',system
                        self.initialiseTechnologies(system)
                        
                                                #Create excel with the corresponding name
                        if self.hourly_excels:
                            excel = xlsxwriter.Workbook(self.getSystemName(system)+".xls")
                            for th_order in itertools.permutations(set(system) & set(self.th_technologies)):
                                excel.add_worksheet(self.getThermalPriority(th_order))
                            excel.close()

                        #------------------------------------------------------
                        #Generating different thermal priorities for each electrical
                        #priority and iterating through them
                        for th_order in itertools.permutations(set(system) & set(self.th_technologies)):
                            self.performCalculations(th_order)
                            self.updateKPI(system,th_order)
                            if self.hourly_excels:
                                self.writeHourlyExcel(self.getSystemName(system)+".xls",self.getThermalPriority(th_order),th_order)
        self.writeKPIExcel()
                                
        return
        
    def updateKPI(self,system,th_order):
        CHP_annuity = 0
        boiler_annuity=0
        th_storage_annuity = 0
        sol_thermal_annuity = 0
        el_heater_annuity = 0
        PV_annuity = 0
        CHP_a,CHP_CRC,CHP_bonus,CHP_Ank,CHP_Anv,CHP_Anb,CHP_Ane = 0,0,0,0,0,0,0
        boiler_CRC,boiler_Ank,boiler_Anv,boiler_Anb=0,0,0,0     
        Total_emissions = 0
        Total_loss = 0
        CHP_capacity = 0
        CHP_heat = 0
        CHP_on_count = 0
        CHP_hours = 0
        boiler_capacity = 0
        boiler_heat = 0
        ThSt_capacity = 0
        ThSt_heat = 0
        SolTh_capacity = 0
        SolTh_heat = 0
        ElHe_capacity = 0
        ElHe_heat = 0
        PV_capacity = 0
        PV_heat = 0
        CHP_annuity = 0
        boiler_annuity = 0
        th_storage_annuity = 0
        sol_thermal_annuity = 0
        el_heater_annuity = 0
        PV_annuity = 0
        sc_percentage = 0
        
        if 'CHP' in system:
            CHP_a,CHP_CRC,CHP_bonus,CHP_Ank,CHP_Anv,CHP_Anb,CHP_Ane,CHP_annuity = self.OnOffCHP.getAnnuity()
            Total_emissions += self.OnOffCHP.getEmissions()
            CHP_capacity = self.OnOffCHP.thermal_capacity
            CHP_heat = self.OnOffCHP.heat
            CHP_on_count = 0
            CHP_hours = 0
            
        if 'B' in system:
            boiler_CRC,boiler_Ank,boiler_Anv,boiler_Anb,boiler_annuity = self.B.getAnnuity()
            Total_emissions += self.B.getEmissions()
            boiler_capacity = self.B.thermal_capacity
            boiler_heat = self.B.heat
            
        if 'ElHe' in system:
            el_heater_annuity = self.ElHe.getAnnuity()
            Total_emissions += self.ElHe.getEmissions()
            ElHe_capacity = self.ElHe.thermal_capacity
            ElHe_heat = self.ElHe.heat
            
        if 'ThSt' in system:
            th_storage_annuity = self.ThSt.getAnnuity()
            Total_loss = self.ThSt.getLosses()
            ThSt_capacity = self.ThSt.thermal_capacity_l
            ThSt_heat = self.ThSt.heat
            
        if 'SolTh' in system:
            sol_thermal_annuity = self.SolTh.getAnnuity()
            SolTh_capacity = self.SolTh.capacity
            SolTh_heat = self.SolTh.heat
            
        if 'PV' in system:
            PV_annuity = self.PV.getAnnuity()
            Total_emissions += self.PV.getEmissions()
            PV_capacity = self.PV.capacity
            PV_heat = self.PV.heat
            
        Total_annuity = CHP_annuity + boiler_annuity + th_storage_annuity + sol_thermal_annuity + el_heater_annuity + PV_annuity
        Total_pef = 0
            
        self.KPI.append([self.getSystemName(system), self.getThermalPriority(th_order), '', \
        Total_annuity,Total_emissions,Total_pef, Total_loss, \
        CHP_capacity , CHP_heat,\
        CHP_on_count, CHP_hours,\
        boiler_capacity, boiler_heat,\
        ThSt_capacity , ThSt_heat,\
        SolTh_capacity , SolTh_heat,\
        ElHe_capacity, ElHe_heat,\
        PV_capacity , PV_heat,\
        CHP_annuity,\
        boiler_annuity,\
        th_storage_annuity,\
        sol_thermal_annuity,\
        el_heater_annuity,\
        PV_annuity,\
        sc_percentage])
        
        self.EconomicFactors.append([self.getSystemName(system),self.getThermalPriority(th_order),Total_annuity,CHP_capacity , CHP_heat, CHP_heat*.5,CHP_a,CHP_CRC,CHP_bonus,CHP_Ank,CHP_Anv,CHP_Anb,CHP_Ane,CHP_annuity,\
    boiler_capacity, boiler_heat, boiler_CRC,boiler_Ank,boiler_Anv,boiler_Anb,boiler_annuity])        
        
    def getMaximumRectangle(self,thermal_profile):
        
        #Sort thermal demand in decreasing order for the load distribution curve
        thermal_profile = sorted(thermal_profile, reverse=True)
        
        #Finding the maximum rectangle
        q_yearly = 0
        maxr = 0
        for k in range(0,8760):
            q_yearly += thermal_profile[k]
            if k*thermal_profile[k]>maxr:
                maxr=k*thermal_profile[k]
                hours=k
        print maxr,hours,thermal_profile[hours]
        return thermal_profile[hours],hours
        
    def initialiseTechnologies(self, system):
        
        #------------------------------------------------------------------------------
        #CHP    
        #If CHP is present, it will check for a peak load device. If peak load 
        #device is present, CHP is sized according to maximum rectangle method. 
        # Otherwise it is sized according to peak thermal load.
        if 'CHP' in system:
            if 'ElHe' in system or 'B' in system:
                self.OnOffCHP = CHP.OnOffCHP('YahooCHP',self.maxr_thermal_power,0.3*self.maxr_thermal_power,0.6,0.3)
            else:
                self.OnOffCHP = CHP.OnOffCHP('YahooCHP',self.peak_thermal_power,0.3*self.maxr_thermal_power,0.6,0.3)
    
    #------------------------------------------------------------------------------
    #Boiler    
        #If boiler is present, dimension it to peak thermal demand
        if 'B' in system:
            self.B = Boiler.Boiler('YahooB',self.peak_thermal_power,0.98)
                
            
    #------------------------------------------------------------------------------
    #Electric Resistance Heater
        #If electric heater is present, dimension it to peak thermal demand 
        if 'ElHe' in system:
            self.ElHe = ElectricHeater.ElectricHeater('Model',self.peak_thermal_power,0.98)
        
        return
        
    def performCalculations(self,th_order):
        for i in range (0,8760):
            q_hourly=self.thermal_profile[i]
            
            for technology in th_order:
                if technology is 'CHP' and q_hourly>0:
                    q_hourly=self.OnOffCHP.getHeat(q_hourly,i)
                if technology is 'B' and q_hourly>0:
                    q_hourly=self.B.getHeat(q_hourly,i)
                if technology is 'ElHe' and q_hourly>0:
                    q_hourly = self.ElHe.getHeat(q_hourly,i)
        return
            
        
    def writeHourlyExcel(self,workbook_name,worksheet_name,th_order):  

        #--------------------------------------------------------------------------
        #write all values into the worksheet   

        workbook = open_workbook(workbook_name,worksheet_name)
        idx = workbook.sheet_names().index(worksheet_name)
        workbook = copy(workbook)
        worksheet = workbook.get_sheet(idx)
        worksheet.write(0,0,"Hour")
        worksheet.write(0,1,"Hourly Thermal Demand")
        count = 2
        for technology in th_order:
            if technology is 'CHP':
                worksheet.write(0,count,"CHP Production")
            elif technology is 'B':
                worksheet.write(0,count,"Boiler Production")
            elif technology is 'ElHe':
                worksheet.write(0,count,"Electrical Resistance Heater Production")
            count += 1
               
        for i in range (0,8760):
            worksheet.write(i+1,0,i)
            worksheet.write(i+1,1,self.thermal_profile[i])
            count = 2
            for technology in th_order:
                if technology is 'CHP':
                    worksheet.write(i+1,count,self.OnOffCHP.heat_hourly[i])
                elif technology is 'B':
                    worksheet.write(i+1,count,self.B.heat_hourly[i])
                elif technology is 'ElHe':
                    worksheet.write(i+1,count,self.ElHe.heat_hourly[i])
                count += 1     
        workbook.save(workbook_name)
        
    def getSystemName(self,system):
        system_name = ""
        count = 1
        for i in system:
            if len(set(system)) == count:
                system_name += i
            else:
                system_name += i + "-"
                count += 1
        return system_name
        
    def getThermalPriority(self,th_order):
        th_priority = ""
        count = 1
        for elements in th_order:
            if len(set(th_order)&set(self.th_technologies)) == count:
                th_priority += elements
            else:
                th_priority += elements + ">"
                count += 1
        return th_priority
        
    def writeKPIExcel(self):
        os.chdir(self.location+"/"+self.building_id)
        excel = xlsxwriter.Workbook(self.building_id+".xls")  
        worksheet = excel.add_worksheet("Thermal Profile")
        for row in range(0,len(self.thermal_profile)):
            worksheet.write(row,0,row)
            worksheet.write(row,1,self.thermal_profile[row])
        
        # Create a new Chart object.
        chart = excel.add_chart({'type': 'line'})
        
        chart.set_x_axis({
        'name': 'Hours',
        'name_font': {'size': 10, 'bold': True},
        'label_position': 'low'
        })
    
        chart.set_y_axis({
        'name': 'Thermal Demand in kWh',
        'name_font': {'size': 10, 'bold': True}
        })
            
        chart.set_title({'name': 'Thermal Load Profile'})
            
            
        # Configure the chart.
        chart.add_series({'values':['Thermal Profile',0,1,8760,1],
                          'categories':['Thermal Profile',0,0,8760,0]})
        chart.set_legend({'none': True})
        # Insert the chart into the worksheet.
        worksheet.insert_chart('D4', chart)
                      
        worksheet = excel.add_worksheet("KPI")
        worksheet.write(0,0,"System")
        worksheet.write(0,1,"Thermal Priority")
        worksheet.write(0,2,"Electrical Priority")
        worksheet.write(0,3,"Annuity (Euros)")
        worksheet.write(0,4,"Emissions (kg of CO2)")
        worksheet.write(0,5,"Primary Energy Factor")
        worksheet.write(0,6,"Total Losses (kWh)")
        worksheet.write(0,7,"CHP capacity (kW)")
        worksheet.write(0,8,"CHP heat (kWh)")
        worksheet.write(0,9,"CHP_On_Count")
        worksheet.write(0,10,"CHP_Hours (hours)")                       
        worksheet.write(0,11,"Boiler capacity (kW)")
        worksheet.write(0,12,"Boiler heat (kWh)")
        worksheet.write(0,13,"Storage capacity (liters)")
        worksheet.write(0,14,"Storage heat (kWh)")
        worksheet.write(0,15,"Solar Thermal Are (m2)")
        worksheet.write(0,16,"Solar Thermal heat (kWh)")
        worksheet.write(0,17,"El heater capacity (kW)")
        worksheet.write(0,18,"El heater heat (kWh)")
        worksheet.write(0,19,"PV area (m2)")
        worksheet.write(0,20,"PV El (kWh)")
        worksheet.write(0,21,"CHP Annuity(Euros)")
        worksheet.write(0,22,"Boiler Annuity(Euros)")
        worksheet.write(0,23,"Th Storage Annuity(Euros)")
        worksheet.write(0,24,"Sol Thermal Annuity(Euros)")
        worksheet.write(0,25,"El Heater Annuity(Euros)")
        worksheet.write(0,26,"PV Annuity(Euros)")
        worksheet.write(0,27,"Self Consumption needed for break-even with boiler(%)")
        row = 1
        for item in self.KPI:
            for column in range(0,28):
                worksheet.write(row,column,item[column])
                column +=1
            row += 1
            
        # Create a new Chart object.
        chart = excel.add_chart({'type': 'scatter'})
        
        chart.set_x_axis({
        'name': 'Yearly Emissions',
        'name_font': {'size': 10, 'bold': True},
        'label_position': 'low'
        })
    
        chart.set_y_axis({
        'name': 'Annuity',
        'name_font': {'size': 10, 'bold': True}
        })
            
        chart.set_title({'name': 'Results'})
            
            
        # Configure the chart. In simplest case we add one or more data series.
        chart.add_series({'values':['KPI',1,3,row,3],
                          'categories':['KPI',1,4,row,4]})
        chart.set_legend({'none': True})
        # Insert the chart into the worksheet.
        worksheet.insert_chart('V4', chart)
        
        worksheet = excel.add_worksheet("Economic Factors in Detail")
        worksheet.write(0,0,"System")
        worksheet.write(0,1,"Thermal Priority")   
        worksheet.write(0,2,"Total Annuity(Euros)")
        worksheet.write(0,3,"Th Capacity of CHP(kW)")
        worksheet.write(0,4,"Heat generated by the CHP(kWh)")
        worksheet.write(0,5,"Electricity generated by the CHP(kWh)")
        worksheet.write(0,6,"Annuity factor")
        worksheet.write(0,7,"CHP Capital Costs(Euros)")
        worksheet.write(0,8,"CHP bonus(Euros)")
        worksheet.write(0,9,"CHP Capital related Annuity(Euros)")
        worksheet.write(0,10,"CHP demand related Annuity(Euros)")
        worksheet.write(0,11,"CHP operation related Annuity(Euros)")
        worksheet.write(0,12,"CHP proceeds related Annuity(Euros)")
        worksheet.write(0,13,"CHP Total Annuity(Euros)")
        worksheet.write(0,14,"Boiler Capacity(kW)")
        worksheet.write(0,15,"Heat generated by the Boiler(kWh)")                       
        worksheet.write(0,16,"Boiler Capital related Costs(Euros)")
        worksheet.write(0,17,"Boiler Capital related Annuity(Euros)")
        worksheet.write(0,18,"Boiler demand related Annuity(Euros)")
        worksheet.write(0,19,"Boiler operation related Annuity(Euros)")
        worksheet.write(0,20,"Total Boielr Annuity(Euros)")
        row = 1
        for item in self.EconomicFactors:
            for column in range(0,21):
                worksheet.write(row,column,item[column])
                column +=1
            row += 1
        
        excel.close()     
        return
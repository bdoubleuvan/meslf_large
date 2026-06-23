# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 15:23:25 2024

@author: bnguyen2
"""

# %%
import copy
import networkx as nx
import numpy as np
import os
import pandas as pd
import re

from lxml import etree
from meslf.networks.gas_network import GasNetwork, GasNode, GasLink, GasHalfLink
from meslf.networks.carrier import Gas
from tqdm import tqdm

# %%

class GasLibNetwork():
    def __init__(self, network_name):
        self.network_name = network_name
        # self.path = os.path.join(os.path.dirname(os.path.abspath('.')), 'data', network_name, network_name)
        self.path = os.path.join(os.path.abspath('.'), 'data', network_name, network_name)

    def convert_to_meter(self, value=0, unit='meter'):
        if unit in {'mm', 'millimeter', 'millimetre'}:
            return 10**-3 * value
        elif unit in {'cm', 'centimeter', 'centimetre'}:
            return 10**-2 * value
        elif unit in {'dm', 'decimeter', 'decimetre'}:
            return 10**-1 * value
        elif unit in {'m', 'meter', 'metre'}:
            return value
        elif unit in {'km', 'kilometer', 'kilometre'}:
            return 10**3 * value
        elif unit in {'in', 'inch'}:
            return 0.0254 * value
        elif unit in {'ft', 'foot'}:
            return 0.3048 * value
        else:
            raise ValueError("Unit '{}' not implemented or wrong".format(unit))


    def convert_to_pa(self, value=0, unit='Pa'):
        if bool(re.match(r"\b[pP][aA]\b", unit)):
            return value
        elif bool(re.match(r"\b[mM][bB][aA][rR][aA]{0,1}", unit)):
            return 10**3 * value
        elif bool(re.match(r"\b[bB][aA][rR][aA]{0,1}\b", unit)):
            return 10**5 * value
        elif bool(re.match(r"\b[mM][bB][aA][rR][gG]", unit)):
            return 10**3 * value + 101325
        elif bool(re.match(r"\b[bB][aA][rR][gG]", unit)):
            return 10**5 * value + 101325
        else:
            raise ValueError("Unit '{}' not implemented or wrong".format(unit))


    def convert_to_kg_per_second(self, value=0, rho=1, unit='kg_per_second'):
        if bool(re.match(r"\b[kK][gG]_[pP][eE][rR]_[sS][eE][cC][oO][nN][dD]\b", unit)) or bool(re.match(r"\b[kK][gG]\[sS]\b", unit)):
            return value
        if bool(re.match(r"\b[kK][gG]_[pP][eE][rR]_[hH][oO][uU][rR]\b", unit)):
            return value / 3600
        elif bool(re.match(r"\b[mM]_[cC][uU][bB][eE]_[pP][eE][rR]_[sS][eE][cC][oO][nN][dD]\b", unit)):
            return value * rho
        elif bool(re.match(r"\b[mM]_[cC][uU][bB][eE]_[pP][eE][rR]_[hH][oO][uU][rR]\b", unit)):
            return value * rho / 3600
        elif bool(re.match(r"\b1000[mM]_[cC][uU][bB][eE]_[pP][eE][rR]_[sS][eE][cC][oO][nN][dD]\b", unit)):
            return 1000 * value * rho
        elif bool(re.match(r"\b1000[mM]_[cC][uU][bB][eE]_[pP][eE][rR]_[hH][oO][uU][rR]\b", unit)):
            return 1000 * value * rho / 3600
        else:
            raise ValueError("Unit '{}' not implemented or wrong".format(unit))


    def gaslib_get_tag(self, element):
        return element.tag.split("}")[-1]


    def gaslib_to_pandas(self):
        # Convert GasLib topology data to Pandas dataframes
        xml = etree.parse(r"{}.net".format(self.path))

        node_data = []
        link_data = []

        for element in xml.findall("./*/*/[@id]"):
            element_storage = {}
            for key, value in element.attrib.items():
                element_storage[key] = value
            for element_child in element.iter():
                for key, value in element_child.attrib.items():
                    if key == 'unit':
                        key = "{}_unit".format(self.gaslib_get_tag(element_child))
                    elif key == 'value':
                        key = "{}_value".format(self.gaslib_get_tag(element_child))
                    if bool(re.match(r".*_value\b", key)):
                        element_storage[key] = float(value)
                    else:
                        element_storage[key] = value
            if self.gaslib_get_tag(element) in {'source', 'sink', 'innode'}:
                element_storage['bc_type'] = self.gaslib_get_tag(element)
                node_data.append(element_storage)
            else:
                element_storage['link_type'] = self.gaslib_get_tag(element)
                link_data.append(element_storage)

        node_data = pd.DataFrame(node_data)
        link_data = pd.DataFrame(link_data)

        # Add boundary conditions to Pandas dataframe
        xml = etree.parse("{}.scn".format(self.path))

        column_names = ['q_min_value',
                        'q_min_unit',
                        'q_max_value',
                        'q_max_unit',
                        'p_min_value',
                        'p_min_unit',
                        'p_max_value',
                        'p_max_unit',
                        'contractPressureMax_value',
                        'contractPressureMax_unit']
        node_data[column_names] = None

        node_data_id_list = list(node_data['id'])

        for element in xml.findall("./*/*/[@id]"):
            if element.attrib['id'] in node_data_id_list:
                index = node_data_id_list.index(element.attrib['id'])

                for element_child in element:
                    if self.gaslib_get_tag(element_child) == 'flow':
                        if element_child.attrib['bound'] == 'both':
                            node_data.at[index, 'q_min_value'] = float(element_child.attrib['value'])
                            node_data.at[index, 'q_min_unit'] = element_child.attrib['unit']
                            node_data.at[index, 'q_max_value'] = float(element_child.attrib['value'])
                            node_data.at[index, 'q_max_unit'] = element_child.attrib['unit']
                        else:
                            if element_child.attrib['bound'] == 'lower':
                                attrib = 'min'
                            else:
                                attrib = 'max'
                            node_data.at[index, 'q_{}_value'.format(attrib)] = float(element_child.attrib['value'])
                            node_data.at[index, 'q_{}_unit'.format(attrib)] = element_child.attrib['unit']
                    elif self.gaslib_get_tag(element_child) == 'pressure':
                        if element_child.attrib['bound'] == 'both':
                            node_data.at[index, 'p_min_value'] = float(element_child.attrib['value'])
                            node_data.at[index, 'p_min_unit'] = element_child.attrib['unit']
                            node_data.at[index, 'p_max_value'] = float(element_child.attrib['value'])
                            node_data.at[index, 'p_max_unit'] = element_child.attrib['unit']
                        else:
                            if element_child.attrib['bound'] == 'lower':
                                attrib = 'min'
                            else:
                                attrib = 'max'
                            node_data.at[index, "p_{}_value".format(attrib)] = float(element_child.attrib['value'])
                            node_data.at[index, "p_{}_unit".format(attrib)] = element_child.attrib['unit']
                    elif self.gaslib_get_tag(element_child) == 'contractPressureMax':
                        node_data.at[index, 'contractPressureMax_value'] = float(element_child.attrib['value'])
                        node_data.at[index, 'contractPressureMax_unit'] = element_child.attrib['unit']

        return node_data, link_data


    def gaslib_compressor(self):
        xml = etree.parse("{}.cs".format(self.path))

        compressor_data = []

        for element in xml.findall("./*/[@id]"):
            element_storage = {}
            for key, value in element.attrib.items():
                for element_child in element.iter():
                    element_storage["{}_{}".format(self.gaslib_get_tag(element), key)] = value
                    for key, value in element_child.attrib.items():
                        if self.gaslib_get_tag(element_child) in {'turboCompressor', 'pistonCompressor'}:
                            element_storage[key] = value

                        tag = self.gaslib_get_tag(element_child)
                        if tag in {'turboCompressor', 'pistonCompressor'}:
                            element_storage['type'] = tag
                        else:
                            key = "{}_{}".format(tag, key)
                            if bool(re.match(r".*_value\b", key)):
                                element_storage[key] = float(value)
                            else:
                                element_storage[key] = value

            compressor_data.append(element_storage)

        return pd.DataFrame(compressor_data)

        
    def create_gas(self, gas_type='gas', data=None, M=28.9652e-3, R=8.31446261815324, Z=1):
        # Set-up gas properties
        R_air = R / M # [J/kgK] specific gas constant for air
        
        pn = 101325 # [Pa] standard condition
        Tn = 273.15 # [K] standard condition
        
        if gas_type == 'natural':
            mu = 1.02 * 10**-5 # based on methane
            S = 0.7611058 / 1.2922 # specific gravity of natural gas
        elif gas_type == 'hydrogen':
            mu = 8.4 * 10**-5
            S = 0.08988 / 1.2922 # specific gravity of hydrogen gas
            
        R_gas = R_air / S
        
        if gas_type == 'natural': # set temperature of gas equal to first node in data
            if data['gasTemperature_unit'] in {'C', 'Celsius'}:
                T_gas = 273.15 + data['gasTemperature_value']
            elif data['gasTemperature_unit'] in {'K', 'Kelvin'}:
                T_gas = data['gasTemperature_value']
            else:
                # T_gas = Tn
                raise ValueError("Invalid temperature unit " + \
                                "'{}', which is not implemented or wrong name. ".format(data['gasTemperature_unit']) + \
                                "Use 'C', 'Celsius', 'K' or 'Kelvin'.")
        else: # set temperature equal to normal temperature
            T_gas = Tn
        
        return Gas('gas', R_gas=R_gas, T=T_gas, Z=Z, pn=pn, Tn=Tn, mu=mu)

    # %% Create network

    def create_network(self, flow='average', pressure='max', gas_type='hydrogen', link_settings={}, resistor=True, scale_var=None, 
                       slack_position=0, change_first_slack=False, number_of_clones=1, number_of_merges=0):
        if number_of_clones > 1:
            try:
                slack_data = np.genfromtxt(os.path.join(os.path.abspath('.'), "gaslib", "results", "slack_value.txt"), dtype=['<U20', float])
                slack_mass_flow = {}
                for data in slack_data:
                    slack_mass_flow[data[0]] = data[1]
            except:
                print("No slack value data of network {}".format(self.network_name))
          
        # get date from GasLib
        node_data, link_data = self.gaslib_to_pandas()
                
        # compute pressure difference in all nodes
        pressure_difference = node_data.pressureMax_value - node_data.pressureMin_value
        # match nodes equal to largest linear pressure difference
        pressure_difference_max_indices = pressure_difference == pressure_difference.max()
        # find the largest max pressure corresponding to the largest pressure difference
        pressure_max_index = node_data.pressureMax_value[pressure_difference_max_indices].argmax()
        # assign minimum pressure
        pressureMin = self.convert_to_pa(value=node_data.at[pressure_max_index, 'pressureMin_value'],
                                         unit=node_data.at[pressure_max_index, 'pressureMin_unit'])
        # assign maximum pressure
        pressureMax = self.convert_to_pa(value=node_data.at[pressure_max_index, 'pressureMax_value'],
                                         unit=node_data.at[pressure_max_index, 'pressureMax_unit'],)

        # First node of the dataset becomes a reference node
        if change_first_slack:
            node_data.at[slack_position, 'bc_type'] = 'reference sink'
            node_data.at[slack_position, 'p_min_value'] = pressureMin
            node_data.at[slack_position, 'p_min_unit'] = 'Pa'
            node_data.at[slack_position, 'p_max_value'] = pressureMax
            node_data.at[slack_position, 'p_max_unit'] = 'Pa'
            node_data.at[slack_position, 'q_min_value'] = 0
            node_data.at[slack_position, 'q_min_unit'] = 'kg_per_second'
            node_data.at[slack_position, 'q_max_value'] = 0
            node_data.at[slack_position, 'q_max_unit'] = 'kg_per_second'

        else:
            node_data.at[slack_position, 'bc_type'] = 'reference'
            node_data.at[slack_position, 'p_min_value'] = pressureMin
            node_data.at[slack_position, 'p_min_unit'] = 'Pa'
            node_data.at[slack_position, 'p_max_value'] = pressureMax
            node_data.at[slack_position, 'p_max_unit'] = 'Pa'
        
        # Computing per unit scaling parameters
        qbase = self.convert_to_kg_per_second(value=node_data['q_max_value'].max(), \
                                              rho=node_data['normDensity_value'].max(), \
                                              unit=node_data['q_max_unit'][node_data['q_max_value'].argmax()])
        pbase = self.convert_to_pa(value=node_data['pressureMax_value'].max(), \
                                   unit=node_data['pressureMax_unit'][node_data['pressureMax_value'].argmax()])

        # scaling settings
        scale_var_params = {'qbase': qbase, 
                            'pbase': pbase}
        
        # Initialise gas network
        network = GasNetwork(name=self.network_name, formulation='full')
                
        # coupling_start_node = []
        # coupling_end_node = []
        
        slack_node = None
        
        save_node = {}
        save_merge_q_node_even = {}
        save_merge_q_node_odd = {}
        
        for clone_number in tqdm(range(number_of_clones)):
            number_of_merge_q_nodes = 0
            # first_coupling_start_node = True
            # first_coupling_end_node = True
            
            # Add nodes to network
            nodes = {}
            # node_index = {}
            
            if (clone_number % 2) == 0:
                merge_q_node_even = {}
            else:
                merge_q_node_odd = {}
            
            for i, data in node_data.iterrows():
                # node_index["{} ({})".format(data['id'], clone_number)] = i + clone_number * node_data.shape[0] 
                bc_type = data['bc_type']

                p_min_value = data['p_min_value']
                p_min_unit = data['p_min_unit']
                p_max_value = data.at['p_max_value']
                p_max_unit = data.at['p_max_unit']

                if pd.isna(p_min_value):
                    p_min_value = 0
                    data['p_min_value'] = p_min_value
                if pd.isna(p_min_unit):
                    p_min_unit = 'Pa'
                    data['p_min_unit'] = p_min_unit
                if pd.isna(p_max_value):
                    p_max_value = p_min_value
                    data['p_max_value'] = p_max_value
                if pd.isna(p_max_unit):
                    p_max_unit = 'Pa'
                    data['p_max_unit'] = p_max_unit

                if pressure == 'average':
                    p = self.convert_to_pa(value=p_min_value, unit=p_min_unit) + self.convert_to_pa(value=p_max_value, unit=p_max_unit)
                    p *= 0.5
                elif pressure == 'min':
                    p = self.convert_to_pa(value=p_min_value, unit=p_min_unit)
                elif pressure == 'max':
                    p = self.convert_to_pa(value=p_max_value, unit=p_max_unit)
                else:
                    raise ValueError("Invalid value encountered for input argument 'pressure'. " + \
                                     "It must be 'average', 'min', or 'max', not '{}'".format(pressure))

                if bc_type in {'innode', 'sink', 'source', 'reference sink', 'reference source'}:
                    q_min_value = data['q_min_value']
                    q_min_unit = data['q_min_unit']
                    q_max_value = data['q_max_value']
                    q_max_unit = data['q_max_unit']

                    if pd.isna(q_min_value):
                        q_min_value = 0
                        data['q_min_value'] = q_min_value
                    if pd.isna(q_min_unit):
                        q_min_unit = 'kg_per_second'
                        data['q_min_unit'] = q_min_unit
                    if pd.isna(q_max_value):
                        q_max_value = q_min_value
                        data['q_max_value'] = q_max_value
                    if pd.isna(q_max_unit):
                        q_max_unit = 'kg_per_second'
                        data['q_max_unit'] = q_max_unit
                    
                    # use density from GasLib data if not hydrogen
                    if gas_type == 'hydrogen':
                        rho = 0.08988
                    else:
                        rho = data['normDensity_value']
                        if pd.isna(rho):
                            rho = node_data['normDensity_value'].max()
                            
                    if flow == 'average':
                        q = self.convert_to_kg_per_second(value=q_min_value, rho=rho, unit=q_min_unit) + \
                            self.convert_to_kg_per_second(value=q_max_value, rho=rho, unit=q_max_unit)
                        q *= 0.5
                    elif flow == 'min':
                        q = self.convert_to_kg_per_second(value=q_min_value, rho=rho, unit=q_min_unit)
                    elif flow == 'max':
                        q = self.convert_to_kg_per_second(value=q_max_value, rho=rho, unit=q_max_unit)
                    else:
                        raise ValueError("Invalid value encountered for input argument 'flow'. " + \
                                         "It must be 'average', 'min', or 'max', not '{}'".format(flow))

                    # swap sign, because terminal link points outwards
                    if bc_type in {'source', 'reference source'}:
                        q = -q

                if bc_type in {'junction', 'innode'}:
                    if clone_number == 0:
                        save_node[data['id']] = len(save_node.keys())
                    
                    # node = GasNode(name="{} ({})".format(data['id'], clone_number), bc_type=['q'], scale_var=scale_var, scale_var_params=scale_var_params)
                    # network.add_node(node)
                    
                    # nodes[data['id']] = node
                    
                    if clone_number > 0:
                        if (clone_number % 2) == 0:
                            no_merge = merge_q_node_odd.get(data['id']) is None
                        else:
                            no_merge = merge_q_node_even.get(data['id']) is None
                    else:
                        no_merge = True
                    
                    if no_merge:
                        node = GasNode(name="{} ({})".format(data['id'], clone_number), bc_type=['q'], scale_var=scale_var, scale_var_params=scale_var_params)
                        network.add_node(node)
                                                
                        nodes[data['id']] = node
                        
                        if number_of_merge_q_nodes < number_of_merges:
                            if data['id'] not in set(['innode_2',
                                                      'innode_3',
                                                      'innode_4',
                                                      'innode_6',
                                                      'innode_7',
                                                      'innode_8',
                                                      'innode_9',
                                                      'innode_10',
                                                      'innode_11',
                                                      'innode_12',
                                                      'innode_14',
                                                      'innode_15',
                                                      'innode_16',
                                                      'innode_17',
                                                      'innode_18',
                                                      'innode_19',
                                                      'innode_20',
                                                      'innode_24',
                                                      'innode_25',
                                                      'innode_27',
                                                      'innode_28',
                                                      'innode_29',
                                                      'innode_33',
                                                      'innode_34',
                                                      'innode_35',
                                                      'innode_36',
                                                      'innode_39',
                                                      'innode_40',
                                                      'innode_41',
                                                      'innode_42',
                                                      'innode_43',
                                                      'innode_44',
                                                      'innode_45',
                                                      'innode_46',
                                                      'innode_48',
                                                      'innode_67',
                                                      'innode_68',
                                                      'innode_69',
                                                      'innode_70',
                                                      'innode_74',
                                                      'innode_78',
                                                      'innode_89',
                                                      'innode_92',
                                                      'innode_93',
                                                      'innode_95',
                                                      'innode_99',
                                                      'innode_103',
                                                      'innode_104',
                                                      'innode_109',
                                                      'innode_110',
                                                      'innode_121',
                                                      'innode_123',
                                                      'innode_124',
                                                      'innode_125',
                                                      'innode_390',
                                                      'innode_1067',
                                                      'innode_1272',
                                                      'innode_1273',
                                                      'innode_1289',
                                                      'innode_1325',
                                                      'innode_1331',
                                                      'innode_1723',
                                                      'innode_1814',
                                                      'innode_1890',
                                                      'innode_2064',
                                                      'innode_2373',
                                                      'innode_3102',
                                                      'innode_3133']):
                                if (clone_number % 2) == 0:
                                    merge_q_node_even[data['id']] = node
                                else:
                                    merge_q_node_odd[data['id']] = node
                                number_of_merge_q_nodes += 1
                                
                                if clone_number == 0:
                                    save_merge_q_node_even[data['id']] = save_node[data['id']]
                                elif clone_number == 1:
                                    save_merge_q_node_odd[data['id']] = save_node[data['id']]
                    else:
                        if (clone_number % 2) == 0:
                            nodes[data['id']] = merge_q_node_odd[data['id']]
                        else:
                            nodes[data['id']] = merge_q_node_even[data['id']]
                elif bc_type in {'reference'}:
                    if True: # clone_number == 0:
                        node = GasNode(name="{} ({})".format(data['id'], clone_number), bc_type=['p'], p=p, scale_var=scale_var, scale_var_params=scale_var_params)
                        network.add_node(node)
                        
                        # Does not need a terminal link, but just created for being consistent with other node types.
                        half_link = GasHalfLink(name="half_link_{} ({})".format(data['id'], clone_number), start_node=node, q=0)
                        network.add_half_link(half_link)
                        
                        nodes[data['id']] = node
                        slack_node = node
                    else:
                        nodes[data['id']] = slack_node
                    # else:
                    #     node = GasNode(name="{} ({})".format(data['id'], clone_number), bc_type=['p', 'q'], p=p, scale_var=scale_var, scale_var_params=scale_var_params)
                    #     network.add_node(node)
                        
                    #     # The slack mass flow is calculated at the end, we are pre defining the terminal link.
                    #     half_link = GasHalfLink(name="half_link_{} ({})".format(data['id'], clone_number), start_node=node, q=0)
                    #     network.add_half_link(half_link)
                        
                        # if first_coupling_end_node:
                        #     coupling_end_node.append(node)
                        #     first_coupling_end_node = False
                elif bc_type in {'reference sink', 'reference source'}:
                    node = GasNode(name="{} ({})".format(data['id'], clone_number), bc_type=['p', 'q'], p=p, scale_var=scale_var, scale_var_params=scale_var_params)
                    network.add_node(node)

                    half_link = GasHalfLink(name="half_link_{} ({})".format(data['id'], clone_number), start_node=node, q=q)
                    network.add_half_link(half_link)
                    
                    nodes[data['id']] = node
                elif bc_type in {'reference innode'}:
                    node = GasNode(name="{} ({})".format(data['id'], clone_number), bc_type=['p', 'q'], p=p, scale_var=scale_var, scale_var_params=scale_var_params)
                    network.add_node(node)

                    half_link = GasHalfLink(name="half_link_{} ({})".format(data['id'], clone_number), start_node=node, q=0)
                    network.add_half_link(half_link)
                    
                    nodes[data['id']] = node
                elif bc_type in {'slack'}:
                    if clone_number == 0:
                        save_node[data['id']] = len(save_node.keys())
                    
                    node = GasNode(name="{} ({})".format(data['id'], clone_number), bc_type=[], scale_var=scale_var, scale_var_params=scale_var_params)
                    network.add_node(node)
                    
                    # The slack mass flow is calculated at the end, we are pre defining the terminal link.
                    half_link = GasHalfLink(name="half_link_{} ({})".format(data['id'], clone_number), start_node=node, q=0)
                    network.add_half_link(half_link)
                    
                    nodes[data['id']] = node
                elif bc_type in {'sink', 'source'}:
                    if clone_number == 0:
                        save_node[data['id']] = len(save_node.keys())

                    node = GasNode(name="{} ({})".format(data['id'], clone_number), bc_type=['q'], scale_var=scale_var, scale_var_params=scale_var_params)
                    network.add_node(node)
                    
                    half_link = GasHalfLink(name="half_link_{} ({})".format(data['id'], clone_number), start_node=node, q=q)
                    network.add_half_link(half_link)
                    
                    nodes[data['id']] = node
                 
                    # if clone_number > 0:
                    #     if (clone_number % 2) == 0:
                    #         no_merge = merge_q_node_odd.get(data['id']) is None
                    #     else:
                    #         no_merge = merge_q_node_even.get(data['id']) is None
                    # else:
                    #     no_merge = True
                    
                    # if no_merge:
                    #     node = GasNode(name="{} ({})".format(data['id'], clone_number), bc_type=['q'], scale_var=scale_var, scale_var_params=scale_var_params)
                    #     network.add_node(node)
                        
                    #     half_link = GasHalfLink(name="half_link_{} ({})".format(data['id'], clone_number), start_node=node, q=q)
                    #     network.add_half_link(half_link)
                        
                    #     nodes[data['id']] = node
                        
                    #     if number_of_merge_q_nodes < number_of_merges:
                    #         if (clone_number % 2) == 0:
                    #             merge_q_node_even[data['id']] = node
                    #         else:
                    #             merge_q_node_odd[data['id']] = node
                    #         number_of_merge_q_nodes += 1
                            
                    #         if clone_number == 0:
                    #             save_merge_q_node_even[data['id']] = save_node[data['id']]
                    #         elif clone_number == 1:
                    #             save_merge_q_node_odd[data['id']] = save_node[data['id']]
                        
                    #     # if first_coupling_start_node and (bc_type == 'sink'):
                    #     #     coupling_start_node.append(node)
                    #     #     first_coupling_start_node = False
                    # else:
                    #     if (clone_number % 2) == 0:
                    #         nodes[data['id']] = merge_q_node_odd[data['id']]
                    #     else:
                    #         nodes[data['id']] = merge_q_node_even[data['id']]
                            
                    #     nodes[data['id']].half_links[0].q += q
                else:
                    raise ValueError("Node type called '{}' not implemented or wrong name".format(bc_type))
            
            gas = self.create_gas(gas_type=gas_type, data=node_data.iloc[0, :])
            
            # Add links to network
            for i, data in link_data.iterrows():
                start_node = nodes[data['from']]
                end_node = nodes[data['to']]
                
                # if clone_number == 0:
                #     if (save_merge_q_node_odd.get(data['from']) is not None) and (save_merge_q_node_odd.get(data['to']) is not None):
                #         print(data['id'], data['link_type'], data['from'], data['to'])
                # elif clone_number == 1:
                #     if (save_merge_q_node_even.get(data['from']) is not None) and (save_merge_q_node_even.get(data['to']) is not None):
                #         print(data['id'], data['link_type'], data['from'], data['to'])
                # start_node = network.nodes[node_index["{} ({})".format(data['from'], clone_number)]]
                # end_node = network.nodes[node_index["{} ({})".format(data['to'], clone_number)]]

                if data['link_type'] in {'compressorStation'}:
                    link_type = 'compressor'
                    link_params = {'r' : 1}
                elif data['link_type'] in {'controlValve', 'valve'}:
                    link_type = 'resistor'
                    link_params = {'C' : 1}
                elif data['link_type'] in {'resistor'}:
                    if resistor:
                        try:
                            link_type = 'resistor'
                            D = self.convert_to_meter(data['diameter_value'], data['diameter_unit'])
                            C = 0.5 * data['dragFactor_value'] / (gas.rhon*0.25*np.pi*D**2)**2
                            link_params = {'C' : C}
                        except ValueError:
                            link_type = 'resistor_fixed'
                            C = self.convert_to_pa(data['pressureLoss_value'], data['pressureLoss_unit'])
                            link_params = {'C' : C}
                    else:
                        try:
                            link_type = 'resistor'
                            link_params = {'C' : 1}
                            # link_type = 'resistor'
                            # D = self.convert_to_meter(data['diameter_value'], data['diameter_unit'])
                            # C = 0.5 * data['dragFactor_value'] / (gas.rhon*0.25*np.pi*D**2)**2
                            # link_params = {'C' : C}
                        except ValueError:
                            link_type = 'resistor'
                            link_params = {'C' : 1}
                            # link_type = 'resistor_fixed'
                            # C = self.convert_to_pa(data['pressureLoss_value'], data['pressureLoss_unit'])
                            # link_params = {'C' : C}
                elif data['link_type'] in {'shortPipe'}:
                    link_type = 'resistor'
                    link_params = {'C' : 1}         
                else:
                    D = self.convert_to_meter(data['diameter_value'], data['diameter_unit'])
                    L = self.convert_to_meter(data['length_value'], data['length_unit'])
                    roughness = self.convert_to_meter(data['roughness_value'], data['roughness_unit'])
                    
                    link_type = link_settings['link_type']
                    link_params = {'D' : D,
                                   'E' : 1, # Efficiency factor for Weymouth's friction factor
                                   'L' : L,
                                   'carrier': gas,
                                   'friction' : link_settings['friction'],
                                   'roughness' : roughness # Roughness of inner wall of pipe for Nikuradse's friction factor
                                  }

                link = GasLink(name="{}".format(data['id']),
                               start_node=start_node,
                               end_node=end_node,
                               link_type=link_type,
                               link_params=link_params,
                               link_equation_formulation=link_settings['link_equation_formulation'],
                               scale_var=scale_var,
                               scale_var_params=scale_var_params)
                
                network.add_link(link)
                
            # if clone_number > 0:                
            #     start_node = coupling_start_node[clone_number-1]
            #     end_node = coupling_end_node[clone_number-1]
                
            #     link = GasLink(name="{}-{}".format(start_node.name, end_node.name),
            #                    start_node=start_node,
            #                    end_node=end_node,
            #                    link_type='dummy',
            #                    link_equation_formulation=link_settings['link_equation_formulation'],
            #                    scale_var=scale_var,
            #                    scale_var_params=scale_var_params)
                
            #     network.add_link(link)
                
            #     start_node.half_links[0].q += 1*slack_mass_flow[self.network_name]
        
        # print(save_merge_q_node_even)
        # print(save_merge_q_node_odd)
        
        return network, node_data, link_data, save_node, save_merge_q_node_even, save_merge_q_node_odd
 
 
    # %% Solve
        
    def solve(self, flow='average', pressure='max', gas_type='natural', 
              link_settings={}, resistor=True,
              initial_guess='standard', solver='nr', solver_parameters={},
              lin_solver='lu', lin_solver_parameters={},
              scale_var=None):
        if 'linear' in initial_guess:
            link_settings_linear = copy.deepcopy(link_settings)
            link_settings_linear['friction'] = 'friction_pole'
            link_settings_linear['link_type'] = 'pipe_low'
            
            solver_parameters_linear = copy.deepcopy(solver_parameters)
            
            if initial_guess == 'linear_dp_satisfy_conservation_of_mass':
                solver_parameters_linear['residual_q'] = True
        elif 'simplify_resistor' in initial_guess:
            link_settings_linear = copy.deepcopy(link_settings)
            
            solver_parameters_linear = copy.deepcopy(solver_parameters)
            
            if initial_guess == 'simplify_resistor_satisfy_conservation_of_mass':
                    solver_parameters_linear['residual_q'] = True
        
        final_error = []

        self.network, self.node_data, self.link_data = self.create_network(gas_type=gas_type,
                                                                           flow=flow,
                                                                           pressure=pressure,
                                                                           link_settings=link_settings,
                                                                           resistor=resistor,
                                                                           scale_var=scale_var)
        self.network.initialize()
        
        # network topology
        print(50 * "-")
        print(self.node_data.bc_type.value_counts(), end="\n" + 50 * "-" + "\n")
        print(self.link_data.link_type.value_counts(), end="\n" + 50 * "-" + "\n")
        
        # start solving
        lin_solver_parameters['block_size'] = (len(self.network.links) + len(self.network.nodes)) // 10
        
        # Computing per unit scaling parameters
        q_init = 0.1 * np.ones(len(self.network.links))
        if scale_var is None:
            qbase = self.convert_to_kg_per_second(value=self.node_data['q_max_value'].max(), \
                                                  rho=self.node_data['normDensity_value'].max(), \
                                                  unit=self.node_data['q_max_unit'][self.node_data['q_max_value'].argmax()])
            q_init *= qbase

        # initial pressure deviates from 5% to 10% of the reference pressure

        p_init = np.linspace(0.95, 0.9, self.network.number_of_unknown_p)
        if scale_var is None:
            pbase = self.convert_to_pa(value=self.node_data['pressureMax_value'].max(), \
                                       unit=self.node_data['pressureMax_unit'][self.node_data['pressureMax_value'].argmax()])
            p_init *= pbase
        
        # initial guess
        x_init = np.concatenate([q_init, p_init])
        
        if initial_guess not in {'standard'}:
            if 'linear' in initial_guess:
                self.network_altered, self.node_data_altered, self.link_data_altered = self.create_network(flow=flow,
                                                                                                           pressure=pressure,
                                                                                                           gas_type=gas_type, 
                                                                                                           link_settings=link_settings_linear,
                                                                                                           resistor=resistor,
                                                                                                           scale_var=scale_var)
            else:
                self.network_altered, self.node_data_altered, self.link_data_altered = self.create_network(flow=flow,
                                                                                                           pressure=pressure,
                                                                                                           gas_type=gas_type, 
                                                                                                           link_settings=link_settings_linear,
                                                                                                           resistor=False,
                                                                                                           scale_var=scale_var)
            self.network_altered.initialize()
            
            # solve linear
            output = self.network_altered.solve_network(x_init=x_init,
                                                        solver=solver,
                                                        solver_parameters=solver_parameters_linear,
                                                        lin_solver=lin_solver,
                                                        lin_solver_parameters=lin_solver_parameters,
                                                        post_processing=False)
            
            if initial_guess in {'linear_dp', 'linear_dp_satisfy_conservation_of_mass'}:
                x_init[:len(q_init)] = output[0][:len(q_init)]
            else:
                x_init = output[0]
                            
        # solve original
        output = self.network.solve_network(x_init=x_init,
                                            solver=solver,
                                            solver_parameters=solver_parameters,
                                            lin_solver=lin_solver,
                                            lin_solver_parameters=lin_solver_parameters,
                                            post_processing=True)
            
        final_error.append(self.network.solver.errors[-1])

        # print some convergence results
        if initial_guess == 'standard':
            print("Number of iterations = {}".format(self.network.solver.iterations))
        else:
            print("Number of iterations = {} + {}".format(self.network_altered.solver.iterations, self.network.solver.iterations))
        print("Final error = {:.4e}".format(final_error[-1]))
        if re.fullmatch(r'nr', solver, flags=re.IGNORECASE):
            print("Average F time in seconds = {:.4e}".format(np.average(self.network.solver.F_times)))
            print("Average J time in seconds = {:.4e}".format(np.average(self.network.solver.J_times)))
            print("Average linear solve time in seconds = {:.4e}".format(np.average(self.network.solver.linear_solve_times)))
        print("Average non-linear solve time in seconds = {:.4e}".format(np.average(self.network.solver.nonlinear_solve_times)))
        print("Total time in seconds = {:.4e}".format(self.network.solver.total_time))
        
        print()
        print("{:21s}{:14.3f} Pa".format("Min. pressure = ", np.min(output[-3])))
        print("{:21s}{:14.3f} Pa".format("Max. pressure = ", np.max(output[-3])))
        print("{:21s}{:14.3f} Pa".format("Reference pressure = ", output[-3][0]))
        
        print()
        print("Slack mass flow = {:17.3f} 1000m^3 / hour".format(3.6 * output[-1][0] / self.node_data.at[0, 'normDensity_value']))
        print("Sum injected mass flow = {:10.3e} kg / s".format(np.sum(output[-1])))
    
    
    # %% Others                                
    
    def node_color(self, bc_type):
        if bc_type in {'reference'}:
            result = 'blue'
        elif bc_type in {'sink'}:
            result = 'red'
        elif bc_type in {'source'}:
            result = 'green'
        elif bc_type in {'junction', 'innode'}:
            result = 'gray'
        elif bc_type in {'slack'}:
            result = 'orange'
        elif bc_type in {'reference load'}:
            result = 'purple'
        return result


    def create_networkx(self):
        nodes, links = self.gaslib_to_pandas()

        G = nx.from_pandas_edgelist(links, source='from', target='to', create_using=nx.DiGraph())

        pos = {key: {'x': float(x), 'y': float(y), 'color': self.node_color(bc_type)}
            for key, x, y, bc_type in zip(nodes.id, nodes.x, nodes.y, nodes.bc_type)}
        nx.set_node_attributes(G, pos)

        nx.write_gexf(G, "{}.gexf".format(self.path))
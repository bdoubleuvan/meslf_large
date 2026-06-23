<?xml version="1.0" encoding="UTF-8"?>

<!-- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -->
<!--                                                                                   -->
<!--                  This file is part of the BMWi project 0328006                    -->
<!--                      Technical Capacities of Gas Networks                         -->
<!--                                                                                   -->
<!-- Copyright (C) 2013                                                                -->
<!-- FAU Erlangen-Nuremberg, HU Berlin, LU Hannover, TU Darmstadt,                     -->
<!-- University Duisburg-Essen, WIAS Berlin, Zuse Institute Berlin                     -->
<!-- Contact: Thorsten Koch (koch@zib.de)                                              -->
<!-- All rights reserved.                                                              -->
<!--                                                                                   -->
<!-- This work is licensed under the Creative Commons Attribution 3.0 Unported License.-->
<!-- To view a copy of this license, visit http://creativecommons.org/licenses/by/3.0/ -->
<!-- or send a letter to Creative Commons, 444 Castro Street, Suite 900, Mountain View,-->
<!-- California, 94041, USA.                                                           -->
<!--                                                                                   -->
<!--                         Please note that you have to cite                         -->
<!-- Pfetsch et al. (2012) "Validation of Nominations in Gas Network Optimization:     -->
<!-- Models, Methods, and Solutions", ZIB-Report 12-41                                 -->
<!--                               if you use this data                                -->
<!--                                                                                   -->
<!-- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -->


<compressorStations xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                    xmlns="http://gaslib.zib.de/CompressorStations"
                    xsi:schemaLocation="http://gaslib.zib.de/CompressorStations
                                        http://gaslib.zib.de/schema/CompressorStations.xsd"
                    xmlns:gas="http://gaslib.zib.de/Gas"
                    xmlns:framework="http://gaslib.zib.de/CompressorStations">
  <compressorStation id="compressorStation_8">
    <compressors>
      <turboCompressor drive="drive_1" id="compressor_1">
        <speedMin unit="per_min" value="4340"/>
        <speedMax unit="per_min" value="6825"/>
        <n_isoline_coeff_1 value="-190.759571322"/>
        <n_isoline_coeff_2 value="0.0772865132496"/>
        <n_isoline_coeff_3 value="-7.59106748684e-06"/>
        <n_isoline_coeff_4 value="90.3515687416"/>
        <n_isoline_coeff_5 value="-0.0266710526962"/>
        <n_isoline_coeff_6 value="3.39112590646e-06"/>
        <n_isoline_coeff_7 value="-22.2044156634"/>
        <n_isoline_coeff_8 value="0.00480988340213"/>
        <n_isoline_coeff_9 value="-4.2872113465e-07"/>
        <eta_ad_isoline_coeff_1 value="1.92662677697"/>
        <eta_ad_isoline_coeff_2 value="-0.000603411239138"/>
        <eta_ad_isoline_coeff_3 value="4.11618537812e-08"/>
        <eta_ad_isoline_coeff_4 value="-0.0576070740743"/>
        <eta_ad_isoline_coeff_5 value="0.000275668515201"/>
        <eta_ad_isoline_coeff_6 value="-2.83343221336e-08"/>
        <eta_ad_isoline_coeff_7 value="-0.25991929629"/>
        <eta_ad_isoline_coeff_8 value="3.300000599e-05"/>
        <eta_ad_isoline_coeff_9 value="-5.35440702059e-10"/>
        <surgeline_coeff_1 value="-75.7999202863"/>
        <surgeline_coeff_2 value="75.0846962322"/>
        <surgeline_coeff_3 value="-6.63021036552"/>
        <chokeline_coeff_1 value="-10.222850716"/>
        <chokeline_coeff_2 value="7.88471503267"/>
        <chokeline_coeff_3 value="1.36990892472"/>
        <efficiencyOfChokeline value="0.72"/>
        <surgelineMeasurements>
          <measurement>
            <speed unit="per_min" value="4340"/>
            <adiabaticHead unit="kJ_per_kg" value="41.6"/>
            <volumetricFlowrate unit="m_cube_per_s" value="1.88"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="5360"/>
            <adiabaticHead unit="kJ_per_kg" value="62.7"/>
            <volumetricFlowrate unit="m_cube_per_s" value="2.3"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="5800"/>
            <adiabaticHead unit="kJ_per_kg" value="74.3"/>
            <volumetricFlowrate unit="m_cube_per_s" value="2.6"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="6200"/>
            <adiabaticHead unit="kJ_per_kg" value="84.7"/>
            <volumetricFlowrate unit="m_cube_per_s" value="2.87"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="6500"/>
            <adiabaticHead unit="kJ_per_kg" value="93.1"/>
            <volumetricFlowrate unit="m_cube_per_s" value="3.1"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="6825"/>
            <adiabaticHead unit="kJ_per_kg" value="101.6"/>
            <volumetricFlowrate unit="m_cube_per_s" value="3.35"/>
          </measurement>
        </surgelineMeasurements>
        <characteristicDiagramMeasurements>
          <adiabaticEfficiency value="0.78">
            <measurement>
              <speed unit="per_min" value="4340"/>
              <adiabaticHead unit="kJ_per_kg" value="41.3"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.94"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5360"/>
              <adiabaticHead unit="kJ_per_kg" value="63"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.52"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5800"/>
              <adiabaticHead unit="kJ_per_kg" value="73.3"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.81"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6200"/>
              <adiabaticHead unit="kJ_per_kg" value="83.5"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.05"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6500"/>
              <adiabaticHead unit="kJ_per_kg" value="91.7"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.3"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6825"/>
              <adiabaticHead unit="kJ_per_kg" value="99.8"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.72"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.8">
            <measurement>
              <speed unit="per_min" value="4340"/>
              <adiabaticHead unit="kJ_per_kg" value="40"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.28"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5360"/>
              <adiabaticHead unit="kJ_per_kg" value="61"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.92"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5800"/>
              <adiabaticHead unit="kJ_per_kg" value="71.3"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.25"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6200"/>
              <adiabaticHead unit="kJ_per_kg" value="80.7"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.6"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6500"/>
              <adiabaticHead unit="kJ_per_kg" value="88.7"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.8"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6825"/>
              <adiabaticHead unit="kJ_per_kg" value="0"/>
              <volumetricFlowrate unit="m_cube_per_s" value="0"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.8">
            <measurement>
              <speed unit="per_min" value="4340"/>
              <adiabaticHead unit="kJ_per_kg" value="36.7"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.69"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5360"/>
              <adiabaticHead unit="kJ_per_kg" value="55.7"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.49"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5800"/>
              <adiabaticHead unit="kJ_per_kg" value="65.4"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.8"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6200"/>
              <adiabaticHead unit="kJ_per_kg" value="80.7"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.6"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6500"/>
              <adiabaticHead unit="kJ_per_kg" value="88.7"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.8"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6825"/>
              <adiabaticHead unit="kJ_per_kg" value="0"/>
              <volumetricFlowrate unit="m_cube_per_s" value="0"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.78">
            <measurement>
              <speed unit="per_min" value="4340"/>
              <adiabaticHead unit="kJ_per_kg" value="34.3"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.9"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5360"/>
              <adiabaticHead unit="kJ_per_kg" value="51.8"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.68"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5800"/>
              <adiabaticHead unit="kJ_per_kg" value="61.2"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.05"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6200"/>
              <adiabaticHead unit="kJ_per_kg" value="70.2"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.32"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6500"/>
              <adiabaticHead unit="kJ_per_kg" value="78.1"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.56"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6825"/>
              <adiabaticHead unit="kJ_per_kg" value="87.3"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.71"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.76">
            <measurement>
              <speed unit="per_min" value="4340"/>
              <adiabaticHead unit="kJ_per_kg" value="32.3"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.02"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5360"/>
              <adiabaticHead unit="kJ_per_kg" value="49.3"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.82"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5800"/>
              <adiabaticHead unit="kJ_per_kg" value="58.2"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.18"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6200"/>
              <adiabaticHead unit="kJ_per_kg" value="65.9"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.52"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6500"/>
              <adiabaticHead unit="kJ_per_kg" value="73.8"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.73"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6825"/>
              <adiabaticHead unit="kJ_per_kg" value="82.5"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.99"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.74">
            <measurement>
              <speed unit="per_min" value="4340"/>
              <adiabaticHead unit="kJ_per_kg" value="30.8"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.1"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5360"/>
              <adiabaticHead unit="kJ_per_kg" value="46.2"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.9"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5800"/>
              <adiabaticHead unit="kJ_per_kg" value="54.7"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.28"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6200"/>
              <adiabaticHead unit="kJ_per_kg" value="63.1"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.63"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6500"/>
              <adiabaticHead unit="kJ_per_kg" value="70"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.89"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6825"/>
              <adiabaticHead unit="kJ_per_kg" value="78.1"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.1"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.72">
            <measurement>
              <speed unit="per_min" value="4340"/>
              <adiabaticHead unit="kJ_per_kg" value="30.8"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.1"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5360"/>
              <adiabaticHead unit="kJ_per_kg" value="44.9"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5800"/>
              <adiabaticHead unit="kJ_per_kg" value="51.5"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.4"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6200"/>
              <adiabaticHead unit="kJ_per_kg" value="58"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.8"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6500"/>
              <adiabaticHead unit="kJ_per_kg" value="61.7"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.09"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6825"/>
              <adiabaticHead unit="kJ_per_kg" value="71.2"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.3"/>
            </measurement>
          </adiabaticEfficiency>
        </characteristicDiagramMeasurements>
      </turboCompressor>
      <turboCompressor drive="drive_2" id="compressor_2">
        <speedMin unit="per_min" value="4225"/>
        <speedMax unit="per_min" value="6825"/>
        <n_isoline_coeff_1 value="0"/>
        <n_isoline_coeff_2 value="0.01651075604395605"/>
        <n_isoline_coeff_3 value="0"/>
        <n_isoline_coeff_4 value="0"/>
        <n_isoline_coeff_5 value="0"/>
        <n_isoline_coeff_6 value="0"/>
        <n_isoline_coeff_7 value="-3.635113397487842"/>
        <n_isoline_coeff_8 value="0.0001331543369043166"/>
        <n_isoline_coeff_9 value="0"/>
        <eta_ad_isoline_coeff_1 value="0.8387418089755319"/>
        <eta_ad_isoline_coeff_2 value="-1.259936732203346e-05"/>
        <eta_ad_isoline_coeff_3 value="6.721307087997821e-10"/>
        <eta_ad_isoline_coeff_4 value="0.03328334270807284"/>
        <eta_ad_isoline_coeff_5 value="8.331577259454142e-06"/>
        <eta_ad_isoline_coeff_6 value="-8.206207125714276e-10"/>
        <eta_ad_isoline_coeff_7 value="-0.04165047378826588"/>
        <eta_ad_isoline_coeff_8 value="6.039403069291699e-06"/>
        <eta_ad_isoline_coeff_9 value="-2.810466698730507e-10"/>
        <surgeline_coeff_1 value="27.19889077678573"/>
        <surgeline_coeff_2 value="152.0230524241864"/>
        <surgeline_coeff_3 value="0"/>
        <chokeline_coeff_1 value="-20.90143037824673"/>
        <chokeline_coeff_2 value="8.813856328151072"/>
        <chokeline_coeff_3 value="0"/>
        <efficiencyOfChokeline value="0.65"/>
        <surgelineMeasurements>
          <measurement>
            <speed unit="per_min" value="4225"/>
            <adiabaticHead unit="kJ_per_kg" value="69.51982822589282"/>
            <volumetricFlowrate unit="m_cube_per_s" value="0.2783849999999998"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="4550"/>
            <adiabaticHead unit="kJ_per_kg" value="74.82661090674951"/>
            <volumetricFlowrate unit="m_cube_per_s" value="0.3132927498197396"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="4875"/>
            <adiabaticHead unit="kJ_per_kg" value="80.12797812889536"/>
            <volumetricFlowrate unit="m_cube_per_s" value="0.3481648770241952"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="5200"/>
            <adiabaticHead unit="kJ_per_kg" value="85.42426010674609"/>
            <volumetricFlowrate unit="m_cube_per_s" value="0.3830035537472006"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="5525"/>
            <adiabaticHead unit="kJ_per_kg" value="90.71578432048142"/>
            <volumetricFlowrate unit="m_cube_per_s" value="0.4178109341369227"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="5850"/>
            <adiabaticHead unit="kJ_per_kg" value="96.00287566465683"/>
            <volumetricFlowrate unit="m_cube_per_s" value="0.4525891553334223"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="6175"/>
            <adiabaticHead unit="kJ_per_kg" value="101.2858565936614"/>
            <volumetricFlowrate unit="m_cube_per_s" value="0.487340338425468"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="6500"/>
            <adiabaticHead unit="kJ_per_kg" value="106.5650472642022"/>
            <volumetricFlowrate unit="m_cube_per_s" value="0.522066589387792"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="6825"/>
            <adiabaticHead unit="kJ_per_kg" value="111.8407656750004"/>
            <volumetricFlowrate unit="m_cube_per_s" value="0.556770000000003"/>
          </measurement>
        </surgelineMeasurements>
        <characteristicDiagramMeasurements>
          <adiabaticEfficiency value="0.82">
            <measurement>
              <speed unit="per_min" value="4225"/>
              <adiabaticHead unit="kJ_per_kg" value="67.90257190569668"/>
              <volumetricFlowrate unit="m_cube_per_s" value="0.7770823245514026"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4550"/>
              <adiabaticHead unit="kJ_per_kg" value="72.99251798274594"/>
              <volumetricFlowrate unit="m_cube_per_s" value="0.838815342168451"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4875"/>
              <adiabaticHead unit="kJ_per_kg" value="78.06920370151747"/>
              <volumetricFlowrate unit="m_cube_per_s" value="0.90038753255496"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5200"/>
              <adiabaticHead unit="kJ_per_kg" value="83.13368343377147"/>
              <volumetricFlowrate unit="m_cube_per_s" value="0.9618116835773353"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5525"/>
              <adiabaticHead unit="kJ_per_kg" value="88.18698855543323"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.023100304198777"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5850"/>
              <adiabaticHead unit="kJ_per_kg" value="93.23012917390713"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.084265645428872"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6175"/>
              <adiabaticHead unit="kJ_per_kg" value="98.26409576552973"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.145319720183319"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6500"/>
              <adiabaticHead unit="kJ_per_kg" value="103.2898607311637"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.206274322150828"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6825"/>
              <adiabaticHead unit="kJ_per_kg" value="108.3083798772639"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.267141043756119"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.82">
            <measurement>
              <speed unit="per_min" value="4225"/>
              <adiabaticHead unit="kJ_per_kg" value="64.44759040992865"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.314659301568553"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4550"/>
              <adiabaticHead unit="kJ_per_kg" value="69.16289900234783"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.402790111403415"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4875"/>
              <adiabaticHead unit="kJ_per_kg" value="73.8562110971323"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.490509798803323"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5200"/>
              <adiabaticHead unit="kJ_per_kg" value="78.52965213168783"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.577858088956172"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5525"/>
              <adiabaticHead unit="kJ_per_kg" value="83.18526382714037"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.664873142362546"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5850"/>
              <adiabaticHead unit="kJ_per_kg" value="87.82501239802065"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.751591708277664"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6175"/>
              <adiabaticHead unit="kJ_per_kg" value="92.45079604478099"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.83804926474921"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6500"/>
              <adiabaticHead unit="kJ_per_kg" value="97.06445181794624"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.924280146910781"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6825"/>
              <adiabaticHead unit="kJ_per_kg" value="101.6677619311494"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.010317664974783"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.82">
            <measurement>
              <speed unit="per_min" value="4225"/>
              <adiabaticHead unit="kJ_per_kg" value="59.04918407140575"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.866900122185891"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4550"/>
              <adiabaticHead unit="kJ_per_kg" value="63.26207832227901"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.978828101074527"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4875"/>
              <adiabaticHead unit="kJ_per_kg" value="67.44676656824163"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.090006704134059"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5200"/>
              <adiabaticHead unit="kJ_per_kg" value="71.60646080292274"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.200521267462122"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5525"/>
              <adiabaticHead unit="kJ_per_kg" value="75.7441896475038"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.310452255325671"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5850"/>
              <adiabaticHead unit="kJ_per_kg" value="79.86282053735638"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.419875849614548"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6175"/>
              <adiabaticHead unit="kJ_per_kg" value="83.96507924473229"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.528864468519405"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6500"/>
              <adiabaticHead unit="kJ_per_kg" value="88.05356715725965"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.637487225585986"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6825"/>
              <adiabaticHead unit="kJ_per_kg" value="92.1307766597846"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.745810338379183"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.82">
            <measurement>
              <speed unit="per_min" value="4225"/>
              <adiabaticHead unit="kJ_per_kg" value="51.93911530414776"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.408191764584287"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4550"/>
              <adiabaticHead unit="kJ_per_kg" value="55.58027641269688"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.540005345359965"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4875"/>
              <adiabaticHead unit="kJ_per_kg" value="59.19144690091276"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.670733236450963"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5200"/>
              <adiabaticHead unit="kJ_per_kg" value="62.77655015700085"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.800517468334022"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5525"/>
              <adiabaticHead unit="kJ_per_kg" value="66.3392281772522"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.929489884824337"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5850"/>
              <adiabaticHead unit="kJ_per_kg" value="69.88288119316798"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.057773577616088"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6175"/>
              <adiabaticHead unit="kJ_per_kg" value="73.41070150679153"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.185484111154438"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6500"/>
              <adiabaticHead unit="kJ_per_kg" value="76.92570260827731"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.312730576719899"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6825"/>
              <adiabaticHead unit="kJ_per_kg" value="80.43074442963793"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.439616506638596"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.7775">
            <measurement>
              <speed unit="per_min" value="4225"/>
              <adiabaticHead unit="kJ_per_kg" value="43.58697224502217"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.918511532686512"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4550"/>
              <adiabaticHead unit="kJ_per_kg" value="46.64588610025369"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.066103389448235"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4875"/>
              <adiabaticHead unit="kJ_per_kg" value="49.67694617002701"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.212351307770308"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5200"/>
              <adiabaticHead unit="kJ_per_kg" value="52.68425055173691"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.357453019864987"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5525"/>
              <adiabaticHead unit="kJ_per_kg" value="55.67156117187025"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.501590037779184"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5850"/>
              <adiabaticHead unit="kJ_per_kg" value="58.64235629209639"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.644930186800692"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6175"/>
              <adiabaticHead unit="kJ_per_kg" value="61.59987436511803"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.787629721492419"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6500"/>
              <adiabaticHead unit="kJ_per_kg" value="64.54715102139596"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.929835110292954"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6825"/>
              <adiabaticHead unit="kJ_per_kg" value="67.48705056138441"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.071684555009332"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.735">
            <measurement>
              <speed unit="per_min" value="4225"/>
              <adiabaticHead unit="kJ_per_kg" value="34.52345486567516"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.386378345423104"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4550"/>
              <adiabaticHead unit="kJ_per_kg" value="37.02992173331009"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.546173942508812"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4875"/>
              <adiabaticHead unit="kJ_per_kg" value="39.51290479303901"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.704472368754306"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5200"/>
              <adiabaticHead unit="kJ_per_kg" value="41.97623205877142"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.861517672774878"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5525"/>
              <adiabaticHead unit="kJ_per_kg" value="44.42339350683091"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.017532352165705"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5850"/>
              <adiabaticHead unit="kJ_per_kg" value="46.85759764030605"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.172720959667305"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6175"/>
              <adiabaticHead unit="kJ_per_kg" value="49.28181804841773"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.327273071480015"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6500"/>
              <adiabaticHead unit="kJ_per_kg" value="51.69883215983712"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.481365757916874"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6825"/>
              <adiabaticHead unit="kJ_per_kg" value="54.11125385335708"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.635165662442357"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.6925">
            <measurement>
              <speed unit="per_min" value="4225"/>
              <adiabaticHead unit="kJ_per_kg" value="25.20740067650657"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.807833855836864"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4550"/>
              <adiabaticHead unit="kJ_per_kg" value="27.21093827342259"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.977025095375212"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4875"/>
              <adiabaticHead unit="kJ_per_kg" value="29.1960477573144"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.144660149848843"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5200"/>
              <adiabaticHead unit="kJ_per_kg" value="31.16602701879957"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.311017513757839"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5525"/>
              <adiabaticHead unit="kJ_per_kg" value="33.12387228528181"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.476350207274696"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5850"/>
              <adiabaticHead unit="kJ_per_kg" value="35.07233097322241"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.640890239420522"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6175"/>
              <adiabaticHead unit="kJ_per_kg" value="37.0139448060873"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.804852249214033"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6500"/>
              <adiabaticHead unit="kJ_per_kg" value="38.95108542432805"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.968436512800962"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6825"/>
              <adiabaticHead unit="kJ_per_kg" value="40.88598415040945"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.131831456999059"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.65">
            <measurement>
              <speed unit="per_min" value="4225"/>
              <adiabaticHead unit="kJ_per_kg" value="15.97442242028812"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.183849999999999"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4550"/>
              <adiabaticHead unit="kJ_per_kg" value="17.52996379715266"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.360338170325194"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4875"/>
              <adiabaticHead unit="kJ_per_kg" value="19.07187995001227"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.535280453867394"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5200"/>
              <adiabaticHead unit="kJ_per_kg" value="20.60283522861107"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.708979141660727"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5525"/>
              <adiabaticHead unit="kJ_per_kg" value="22.1252475763795"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.881708568041993"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5850"/>
              <adiabaticHead unit="kJ_per_kg" value="23.64133307817007"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.053720164934973"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6175"/>
              <adiabaticHead unit="kJ_per_kg" value="25.15314212665421"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.225246565207177"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6500"/>
              <adiabaticHead unit="kJ_per_kg" value="26.6625891705144"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.396504977831749"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6825"/>
              <adiabaticHead unit="kJ_per_kg" value="28.17147749999999"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.567699999999999"/>
            </measurement>
          </adiabaticEfficiency>
        </characteristicDiagramMeasurements>
      </turboCompressor>
    </compressors>
    <drives>
      <gasTurbine id="drive_1">
        <energy_rate_fun_coeff_1 value="27000"/>
        <energy_rate_fun_coeff_2 value="1.83"/>
        <energy_rate_fun_coeff_3 value="2.50638780425e-19"/>
        <power_fun_coeff_1 value="218.901581627"/>
        <power_fun_coeff_2 value="3.39006873561"/>
        <power_fun_coeff_3 value="-0.000240713587488"/>
        <power_fun_coeff_4 value="-0.956199536368"/>
        <power_fun_coeff_5 value="-0.0210381500319"/>
        <power_fun_coeff_6 value="1.49313052539e-06"/>
        <power_fun_coeff_7 value="-0.0378285128524"/>
        <power_fun_coeff_8 value="3.70211499791e-05"/>
        <power_fun_coeff_9 value="-2.68548655643e-09"/>
        <specificEnergyConsumptionMeasurements>
          <measurement>
            <compressorPower unit="kW" value="10500"/>
            <fuelConsumption unit="kW" value="46215"/>
          </measurement>
          <measurement>
            <compressorPower unit="kW" value="9000"/>
            <fuelConsumption unit="kW" value="43470"/>
          </measurement>
          <measurement>
            <compressorPower unit="kW" value="7500"/>
            <fuelConsumption unit="kW" value="40725"/>
          </measurement>
          <measurement>
            <compressorPower unit="kW" value="6000"/>
            <fuelConsumption unit="kW" value="37980"/>
          </measurement>
          <measurement>
            <compressorPower unit="kW" value="3000"/>
            <fuelConsumption unit="kW" value="32490"/>
          </measurement>
        </specificEnergyConsumptionMeasurements>
        <maximalPowerMeasurements>
          <ambientTemperature unit="Celsius" value="-5">
            <measurement>
              <speed unit="per_min" value="4778"/>
              <maximalPower unit="kW" value="11260"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5460"/>
              <maximalPower unit="kW" value="11912"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6143"/>
              <maximalPower unit="kW" value="12331"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6825"/>
              <maximalPower unit="kW" value="12521"/>
            </measurement>
          </ambientTemperature>
          <ambientTemperature unit="Celsius" value="5">
            <measurement>
              <speed unit="per_min" value="4778"/>
              <maximalPower unit="kW" value="10586"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5460"/>
              <maximalPower unit="kW" value="11199"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6143"/>
              <maximalPower unit="kW" value="11593"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6825"/>
              <maximalPower unit="kW" value="11771"/>
            </measurement>
          </ambientTemperature>
          <ambientTemperature unit="Celsius" value="15">
            <measurement>
              <speed unit="per_min" value="4778"/>
              <maximalPower unit="kW" value="9928"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5460"/>
              <maximalPower unit="kW" value="10502"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6143"/>
              <maximalPower unit="kW" value="10872"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6825"/>
              <maximalPower unit="kW" value="11039"/>
            </measurement>
          </ambientTemperature>
          <ambientTemperature unit="Celsius" value="25">
            <measurement>
              <speed unit="per_min" value="4778"/>
              <maximalPower unit="kW" value="9285"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5460"/>
              <maximalPower unit="kW" value="9823"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6143"/>
              <maximalPower unit="kW" value="10169"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6825"/>
              <maximalPower unit="kW" value="10325"/>
            </measurement>
          </ambientTemperature>
        </maximalPowerMeasurements>
      </gasTurbine>
      <gasTurbine id="drive_2">
        <energy_rate_fun_coeff_1 value="0.01"/>
        <energy_rate_fun_coeff_2 value="0"/>
        <energy_rate_fun_coeff_3 value="0"/>
        <power_fun_coeff_1 value="-1743.258239586096"/>
        <power_fun_coeff_2 value="5.380445436367578"/>
        <power_fun_coeff_3 value="-0.00031084838845578"/>
        <power_fun_coeff_4 value="10.48674425062359"/>
        <power_fun_coeff_5 value="-0.03236660751938755"/>
        <power_fun_coeff_6 value="1.869939562843102e-06"/>
        <power_fun_coeff_7 value="-0.03485446394332248"/>
        <power_fun_coeff_8 value="0.0001075758813022527"/>
        <power_fun_coeff_9 value="-6.215059651657992e-09"/>
      </gasTurbine>
    </drives>
    <configurations>
      <configuration nrOfSerialStages="1" confId="config_1">
        <stage nrOfParallelUnits="1" stageNr="1">
          <compressor nominalSpeed="5200" id="compressor_2"/>
        </stage>
      </configuration>
      <configuration nrOfSerialStages="1" confId="config_2">
        <stage nrOfParallelUnits="1" stageNr="1">
          <compressor nominalSpeed="6200" id="compressor_1"/>
        </stage>
      </configuration>
      <configuration nrOfSerialStages="2" confId="config_3">
        <stage nrOfParallelUnits="1" stageNr="1">
          <compressor nominalSpeed="5200" id="compressor_2"/>
        </stage>
        <stage nrOfParallelUnits="1" stageNr="2">
          <compressor nominalSpeed="6200" id="compressor_1"/>
        </stage>
      </configuration>
    </configurations>
  </compressorStation>
  <compressorStation id="compressorStation_12">
    <compressors>
      <turboCompressor drive="drive_3" id="compressor_3">
        <speedMin unit="per_min" value="4700"/>
        <speedMax unit="per_min" value="7400"/>
        <n_isoline_coeff_1 value="-12.828760366"/>
        <n_isoline_coeff_2 value="0.00568165806425"/>
        <n_isoline_coeff_3 value="-3.07217609149e-07"/>
        <n_isoline_coeff_4 value="9.90693751693"/>
        <n_isoline_coeff_5 value="-0.00357107779441"/>
        <n_isoline_coeff_6 value="4.54424235134e-07"/>
        <n_isoline_coeff_7 value="-3.30773241055"/>
        <n_isoline_coeff_8 value="0.00079761397412"/>
        <n_isoline_coeff_9 value="-8.05398922586e-08"/>
        <eta_ad_isoline_coeff_1 value="0.516290484583"/>
        <eta_ad_isoline_coeff_2 value="5.57204971423e-06"/>
        <eta_ad_isoline_coeff_3 value="-1.27363080433e-08"/>
        <eta_ad_isoline_coeff_4 value="0.568534759852"/>
        <eta_ad_isoline_coeff_5 value="-1.89496484328e-08"/>
        <eta_ad_isoline_coeff_6 value="1.57994603275e-11"/>
        <eta_ad_isoline_coeff_7 value="-0.369065724356"/>
        <eta_ad_isoline_coeff_8 value="6.35851255542e-05"/>
        <eta_ad_isoline_coeff_9 value="-3.39826932989e-09"/>
        <surgeline_coeff_1 value="-15.7221895543"/>
        <surgeline_coeff_2 value="14.5435343192"/>
        <surgeline_coeff_3 value="-0.14243232248"/>
        <chokeline_coeff_1 value="-10.1829000103"/>
        <chokeline_coeff_2 value="5.50675544767"/>
        <chokeline_coeff_3 value="-0.228906345577"/>
        <efficiencyOfChokeline value="0.65"/>
        <surgelineMeasurements>
          <measurement>
            <speed unit="per_min" value="4700"/>
            <adiabaticHead unit="kJ_per_kg" value="8.6"/>
            <volumetricFlowrate unit="m_cube_per_s" value="1.7"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="5500"/>
            <adiabaticHead unit="kJ_per_kg" value="11.8"/>
            <volumetricFlowrate unit="m_cube_per_s" value="1.93"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="6250"/>
            <adiabaticHead unit="kJ_per_kg" value="15.3"/>
            <volumetricFlowrate unit="m_cube_per_s" value="2.18"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="7000"/>
            <adiabaticHead unit="kJ_per_kg" value="19.5"/>
            <volumetricFlowrate unit="m_cube_per_s" value="2.48"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="7400"/>
            <adiabaticHead unit="kJ_per_kg" value="21.8"/>
            <volumetricFlowrate unit="m_cube_per_s" value="2.65"/>
          </measurement>
        </surgelineMeasurements>
        <characteristicDiagramMeasurements>
          <adiabaticEfficiency value="0.8">
            <measurement>
              <speed unit="per_min" value="4700"/>
              <adiabaticHead unit="kJ_per_kg" value="8.7"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.56"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5500"/>
              <adiabaticHead unit="kJ_per_kg" value="12"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.81"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6250"/>
              <adiabaticHead unit="kJ_per_kg" value="15.4"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.1"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="7000"/>
              <adiabaticHead unit="kJ_per_kg" value="19.4"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.54"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="7400"/>
              <adiabaticHead unit="kJ_per_kg" value="21.5"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.8"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.8">
            <measurement>
              <speed unit="per_min" value="4700"/>
              <adiabaticHead unit="kJ_per_kg" value="8.2"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.96"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5500"/>
              <adiabaticHead unit="kJ_per_kg" value="11.1"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.32"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6250"/>
              <adiabaticHead unit="kJ_per_kg" value="14.3"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.72"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="7000"/>
              <adiabaticHead unit="kJ_per_kg" value="17.9"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.17"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="7400"/>
              <adiabaticHead unit="kJ_per_kg" value="19.8"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.41"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.8">
            <measurement>
              <speed unit="per_min" value="4700"/>
              <adiabaticHead unit="kJ_per_kg" value="7.1"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.39"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5500"/>
              <adiabaticHead unit="kJ_per_kg" value="9.6"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.83"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6250"/>
              <adiabaticHead unit="kJ_per_kg" value="12.4"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.28"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="7000"/>
              <adiabaticHead unit="kJ_per_kg" value="15.6"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.7"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="7400"/>
              <adiabaticHead unit="kJ_per_kg" value="17.3"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.92"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.78">
            <measurement>
              <speed unit="per_min" value="4700"/>
              <adiabaticHead unit="kJ_per_kg" value="6.5"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.55"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5500"/>
              <adiabaticHead unit="kJ_per_kg" value="8.8"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.02"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6250"/>
              <adiabaticHead unit="kJ_per_kg" value="11.5"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.48"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="7000"/>
              <adiabaticHead unit="kJ_per_kg" value="14.4"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.91"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="7400"/>
              <adiabaticHead unit="kJ_per_kg" value="15.9"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.14"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.75">
            <measurement>
              <speed unit="per_min" value="4700"/>
              <adiabaticHead unit="kJ_per_kg" value="5.6"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.7"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5500"/>
              <adiabaticHead unit="kJ_per_kg" value="8.2"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.16"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6250"/>
              <adiabaticHead unit="kJ_per_kg" value="10.8"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.63"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="7000"/>
              <adiabaticHead unit="kJ_per_kg" value="13.3"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.08"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="7400"/>
              <adiabaticHead unit="kJ_per_kg" value="14.7"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.31"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.7">
            <measurement>
              <speed unit="per_min" value="4700"/>
              <adiabaticHead unit="kJ_per_kg" value="5.3"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.85"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5500"/>
              <adiabaticHead unit="kJ_per_kg" value="7.2"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.36"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6250"/>
              <adiabaticHead unit="kJ_per_kg" value="9.5"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.86"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="7000"/>
              <adiabaticHead unit="kJ_per_kg" value="11.7"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.31"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="7400"/>
              <adiabaticHead unit="kJ_per_kg" value="12.9"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.55"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.65">
            <measurement>
              <speed unit="per_min" value="4700"/>
              <adiabaticHead unit="kJ_per_kg" value="4.9"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.95"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5500"/>
              <adiabaticHead unit="kJ_per_kg" value="6.6"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.48"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6250"/>
              <adiabaticHead unit="kJ_per_kg" value="8.5"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.02"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="7000"/>
              <adiabaticHead unit="kJ_per_kg" value="10.3"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.49"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="7400"/>
              <adiabaticHead unit="kJ_per_kg" value="11.4"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.73"/>
            </measurement>
          </adiabaticEfficiency>
        </characteristicDiagramMeasurements>
      </turboCompressor>
      <turboCompressor drive="drive_4" id="compressor_4">
        <speedMin unit="per_min" value="5800"/>
        <speedMax unit="per_min" value="11600"/>
        <n_isoline_coeff_1 value="-3.55677690526"/>
        <n_isoline_coeff_2 value="0.00140436957412"/>
        <n_isoline_coeff_3 value="1.14159685994e-07"/>
        <n_isoline_coeff_4 value="0.111275137208"/>
        <n_isoline_coeff_5 value="0.00109381515256"/>
        <n_isoline_coeff_6 value="8.17154160382e-08"/>
        <n_isoline_coeff_7 value="-5.12896883178"/>
        <n_isoline_coeff_8 value="-7.83210404682e-05"/>
        <n_isoline_coeff_9 value="-6.16403710757e-09"/>
        <eta_ad_isoline_coeff_1 value="1.41344171072"/>
        <eta_ad_isoline_coeff_2 value="-0.000193539345469"/>
        <eta_ad_isoline_coeff_3 value="4.87930540359e-09"/>
        <eta_ad_isoline_coeff_4 value="-0.307062063409"/>
        <eta_ad_isoline_coeff_5 value="0.000232726476953"/>
        <eta_ad_isoline_coeff_6 value="-1.17341619906e-08"/>
        <eta_ad_isoline_coeff_7 value="-0.375256134373"/>
        <eta_ad_isoline_coeff_8 value="9.29913632073e-06"/>
        <eta_ad_isoline_coeff_9 value="7.51985490004e-10"/>
        <surgeline_coeff_1 value="-125.529895357"/>
        <surgeline_coeff_2 value="133.606615682"/>
        <surgeline_coeff_3 value="-0.180658214605"/>
        <chokeline_coeff_1 value="-9.00914210563"/>
        <chokeline_coeff_2 value="6.96887983079"/>
        <chokeline_coeff_3 value="1.62347986398"/>
        <efficiencyOfChokeline value="0.7"/>
        <surgelineMeasurements>
          <measurement>
            <speed unit="per_min" value="5800"/>
            <adiabaticHead unit="kJ_per_kg" value="11.74"/>
            <volumetricFlowrate unit="m_cube_per_s" value="1.029"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="6960"/>
            <adiabaticHead unit="kJ_per_kg" value="17.41"/>
            <volumetricFlowrate unit="m_cube_per_s" value="1.071"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="8120"/>
            <adiabaticHead unit="kJ_per_kg" value="23.98"/>
            <volumetricFlowrate unit="m_cube_per_s" value="1.121"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="8700"/>
            <adiabaticHead unit="kJ_per_kg" value="27.6"/>
            <volumetricFlowrate unit="m_cube_per_s" value="1.148"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="9280"/>
            <adiabaticHead unit="kJ_per_kg" value="31.45"/>
            <volumetricFlowrate unit="m_cube_per_s" value="1.177"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="9860"/>
            <adiabaticHead unit="kJ_per_kg" value="35.53"/>
            <volumetricFlowrate unit="m_cube_per_s" value="1.207"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="10440"/>
            <adiabaticHead unit="kJ_per_kg" value="39.84"/>
            <volumetricFlowrate unit="m_cube_per_s" value="1.24"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="11020"/>
            <adiabaticHead unit="kJ_per_kg" value="44.4"/>
            <volumetricFlowrate unit="m_cube_per_s" value="1.274"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="11600"/>
            <adiabaticHead unit="kJ_per_kg" value="49.18"/>
            <volumetricFlowrate unit="m_cube_per_s" value="1.31"/>
          </measurement>
        </surgelineMeasurements>
        <characteristicDiagramMeasurements>
          <adiabaticEfficiency value="0.78">
            <measurement>
              <speed unit="per_min" value="5800"/>
              <adiabaticHead unit="kJ_per_kg" value="12.11"/>
              <volumetricFlowrate unit="m_cube_per_s" value="0.854"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6960"/>
              <adiabaticHead unit="kJ_per_kg" value="17.46"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.043"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="8120"/>
              <adiabaticHead unit="kJ_per_kg" value="23.8"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.236"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="8700"/>
              <adiabaticHead unit="kJ_per_kg" value="27.34"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.334"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="9280"/>
              <adiabaticHead unit="kJ_per_kg" value="31.12"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.432"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="9860"/>
              <adiabaticHead unit="kJ_per_kg" value="35.15"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.531"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="10440"/>
              <adiabaticHead unit="kJ_per_kg" value="39.42"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.63"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="11020"/>
              <adiabaticHead unit="kJ_per_kg" value="43.94"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.73"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="11600"/>
              <adiabaticHead unit="kJ_per_kg" value="48.71"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.83"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.8">
            <measurement>
              <speed unit="per_min" value="5800"/>
              <adiabaticHead unit="kJ_per_kg" value="11.95"/>
              <volumetricFlowrate unit="m_cube_per_s" value="0.943"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6960"/>
              <adiabaticHead unit="kJ_per_kg" value="17.23"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.153"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="8120"/>
              <adiabaticHead unit="kJ_per_kg" value="23.46"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.366"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="8700"/>
              <adiabaticHead unit="kJ_per_kg" value="26.94"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.474"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="9280"/>
              <adiabaticHead unit="kJ_per_kg" value="30.66"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.583"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="9860"/>
              <adiabaticHead unit="kJ_per_kg" value="34.62"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.692"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="10440"/>
              <adiabaticHead unit="kJ_per_kg" value="38.82"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.802"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="11020"/>
              <adiabaticHead unit="kJ_per_kg" value="43.26"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.913"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="11600"/>
              <adiabaticHead unit="kJ_per_kg" value="47.94"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.024"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.82">
            <measurement>
              <speed unit="per_min" value="5800"/>
              <adiabaticHead unit="kJ_per_kg" value="11.46"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.112"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6960"/>
              <adiabaticHead unit="kJ_per_kg" value="16.48"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.362"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="8120"/>
              <adiabaticHead unit="kJ_per_kg" value="22.38"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.619"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="8700"/>
              <adiabaticHead unit="kJ_per_kg" value="25.65"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.75"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="9280"/>
              <adiabaticHead unit="kJ_per_kg" value="29.13"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.885"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="9860"/>
              <adiabaticHead unit="kJ_per_kg" value="32.8"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.023"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="10440"/>
              <adiabaticHead unit="kJ_per_kg" value="36.62"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.171"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="11020"/>
              <adiabaticHead unit="kJ_per_kg" value="40.6"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.323"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="11600"/>
              <adiabaticHead unit="kJ_per_kg" value="44.99"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.454"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.82">
            <measurement>
              <speed unit="per_min" value="5800"/>
              <adiabaticHead unit="kJ_per_kg" value="11.09"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.204"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6960"/>
              <adiabaticHead unit="kJ_per_kg" value="15.96"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.464"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="8120"/>
              <adiabaticHead unit="kJ_per_kg" value="21.74"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.724"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="8700"/>
              <adiabaticHead unit="kJ_per_kg" value="24.99"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.852"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="9280"/>
              <adiabaticHead unit="kJ_per_kg" value="28.47"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.978"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="9860"/>
              <adiabaticHead unit="kJ_per_kg" value="32.22"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.1"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="10440"/>
              <adiabaticHead unit="kJ_per_kg" value="36.27"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.214"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="11020"/>
              <adiabaticHead unit="kJ_per_kg" value="40.6"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.324"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="11600"/>
              <adiabaticHead unit="kJ_per_kg" value="44.98"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.454"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.8">
            <measurement>
              <speed unit="per_min" value="5800"/>
              <adiabaticHead unit="kJ_per_kg" value="10.26"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.358"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6960"/>
              <adiabaticHead unit="kJ_per_kg" value="14.71"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.654"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="8120"/>
              <adiabaticHead unit="kJ_per_kg" value="19.96"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.951"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="8700"/>
              <adiabaticHead unit="kJ_per_kg" value="22.89"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.099"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="9280"/>
              <adiabaticHead unit="kJ_per_kg" value="26.01"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.247"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="9860"/>
              <adiabaticHead unit="kJ_per_kg" value="29.35"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.394"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="10440"/>
              <adiabaticHead unit="kJ_per_kg" value="32.88"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.541"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="11020"/>
              <adiabaticHead unit="kJ_per_kg" value="36.63"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.688"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="11600"/>
              <adiabaticHead unit="kJ_per_kg" value="40.59"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.833"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.78">
            <measurement>
              <speed unit="per_min" value="5800"/>
              <adiabaticHead unit="kJ_per_kg" value="9.76"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.433"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6960"/>
              <adiabaticHead unit="kJ_per_kg" value="13.97"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.744"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="8120"/>
              <adiabaticHead unit="kJ_per_kg" value="18.92"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.055"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="8700"/>
              <adiabaticHead unit="kJ_per_kg" value="21.68"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.21"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="9280"/>
              <adiabaticHead unit="kJ_per_kg" value="24.62"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.364"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="9860"/>
              <adiabaticHead unit="kJ_per_kg" value="27.76"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.518"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="10440"/>
              <adiabaticHead unit="kJ_per_kg" value="31.1"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.671"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="11020"/>
              <adiabaticHead unit="kJ_per_kg" value="34.63"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.824"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="11600"/>
              <adiabaticHead unit="kJ_per_kg" value="38.35"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.975"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.75">
            <measurement>
              <speed unit="per_min" value="5800"/>
              <adiabaticHead unit="kJ_per_kg" value="9.15"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.513"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6960"/>
              <adiabaticHead unit="kJ_per_kg" value="13.06"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.839"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="8120"/>
              <adiabaticHead unit="kJ_per_kg" value="17.64"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.163"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="8700"/>
              <adiabaticHead unit="kJ_per_kg" value="20.2"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.325"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="9280"/>
              <adiabaticHead unit="kJ_per_kg" value="22.93"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.486"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="9860"/>
              <adiabaticHead unit="kJ_per_kg" value="25.84"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.646"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="10440"/>
              <adiabaticHead unit="kJ_per_kg" value="28.93"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.804"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="11020"/>
              <adiabaticHead unit="kJ_per_kg" value="32.2"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.962"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="11600"/>
              <adiabaticHead unit="kJ_per_kg" value="35.66"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.119"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.72">
            <measurement>
              <speed unit="per_min" value="5800"/>
              <adiabaticHead unit="kJ_per_kg" value="8.62"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.575"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6960"/>
              <adiabaticHead unit="kJ_per_kg" value="12.26"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.911"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="8120"/>
              <adiabaticHead unit="kJ_per_kg" value="16.53"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.246"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="8700"/>
              <adiabaticHead unit="kJ_per_kg" value="18.91"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.412"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="9280"/>
              <adiabaticHead unit="kJ_per_kg" value="21.46"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.576"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="9860"/>
              <adiabaticHead unit="kJ_per_kg" value="24.17"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.74"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="10440"/>
              <adiabaticHead unit="kJ_per_kg" value="27.06"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.903"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="11020"/>
              <adiabaticHead unit="kJ_per_kg" value="30.12"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.064"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="11600"/>
              <adiabaticHead unit="kJ_per_kg" value="33.36"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.225"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.7">
            <measurement>
              <speed unit="per_min" value="5800"/>
              <adiabaticHead unit="kJ_per_kg" value="8.28"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.61"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6960"/>
              <adiabaticHead unit="kJ_per_kg" value="11.76"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.952"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="8120"/>
              <adiabaticHead unit="kJ_per_kg" value="15.85"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.292"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="8700"/>
              <adiabaticHead unit="kJ_per_kg" value="18.12"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.46"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="9280"/>
              <adiabaticHead unit="kJ_per_kg" value="20.56"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.627"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="9860"/>
              <adiabaticHead unit="kJ_per_kg" value="23.15"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.793"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="10440"/>
              <adiabaticHead unit="kJ_per_kg" value="25.91"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.957"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="11020"/>
              <adiabaticHead unit="kJ_per_kg" value="28.84"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.121"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="11600"/>
              <adiabaticHead unit="kJ_per_kg" value="31.95"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.283"/>
            </measurement>
          </adiabaticEfficiency>
        </characteristicDiagramMeasurements>
      </turboCompressor>
      <turboCompressor drive="drive_5" id="compressor_5">
        <speedMin unit="per_min" value="3250"/>
        <speedMax unit="per_min" value="6500"/>
        <n_isoline_coeff_1 value="-4.93059217634"/>
        <n_isoline_coeff_2 value="0.00989673436957"/>
        <n_isoline_coeff_3 value="-1.28152646545e-06"/>
        <n_isoline_coeff_4 value="-7.67140073751"/>
        <n_isoline_coeff_5 value="0.00112123791708"/>
        <n_isoline_coeff_6 value="5.04637812836e-07"/>
        <n_isoline_coeff_7 value="0.369144672999"/>
        <n_isoline_coeff_8 value="-0.000471120492203"/>
        <n_isoline_coeff_9 value="-1.57256795215e-09"/>
        <eta_ad_isoline_coeff_1 value="0.839269322576"/>
        <eta_ad_isoline_coeff_2 value="0.000435531135805"/>
        <eta_ad_isoline_coeff_3 value="-1.79542626282e-07"/>
        <eta_ad_isoline_coeff_4 value="-0.734792452008"/>
        <eta_ad_isoline_coeff_5 value="0.000420052884803"/>
        <eta_ad_isoline_coeff_6 value="-6.47977653823e-09"/>
        <eta_ad_isoline_coeff_7 value="-0.145146529453"/>
        <eta_ad_isoline_coeff_8 value="-5.02020342703e-06"/>
        <eta_ad_isoline_coeff_9 value="4.97662001644e-10"/>
        <surgeline_coeff_1 value="-15.3828857552"/>
        <surgeline_coeff_2 value="17.3591597089"/>
        <surgeline_coeff_3 value="-0.778597393328"/>
        <chokeline_coeff_1 value="-4.07272990616"/>
        <chokeline_coeff_2 value="3.29475887745"/>
        <chokeline_coeff_3 value="0.170038931582"/>
        <efficiencyOfChokeline value="0.65"/>
        <surgelineMeasurements>
          <measurement>
            <speed unit="per_min" value="3250"/>
            <adiabaticHead unit="kJ_per_kg" value="11.4"/>
            <volumetricFlowrate unit="m_cube_per_s" value="1.65"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="3900"/>
            <adiabaticHead unit="kJ_per_kg" value="16.3"/>
            <volumetricFlowrate unit="m_cube_per_s" value="2.02"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="4550"/>
            <adiabaticHead unit="kJ_per_kg" value="22.2"/>
            <volumetricFlowrate unit="m_cube_per_s" value="2.45"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="5200"/>
            <adiabaticHead unit="kJ_per_kg" value="28.7"/>
            <volumetricFlowrate unit="m_cube_per_s" value="2.93"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="5850"/>
            <adiabaticHead unit="kJ_per_kg" value="36"/>
            <volumetricFlowrate unit="m_cube_per_s" value="3.47"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="6500"/>
            <adiabaticHead unit="kJ_per_kg" value="43.8"/>
            <volumetricFlowrate unit="m_cube_per_s" value="4.22"/>
          </measurement>
        </surgelineMeasurements>
        <characteristicDiagramMeasurements>
          <adiabaticEfficiency value="0.82">
            <measurement>
              <speed unit="per_min" value="3250"/>
              <adiabaticHead unit="kJ_per_kg" value="10.5"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.25"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3900"/>
              <adiabaticHead unit="kJ_per_kg" value="14.6"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.85"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4550"/>
              <adiabaticHead unit="kJ_per_kg" value="19.3"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.46"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5200"/>
              <adiabaticHead unit="kJ_per_kg" value="24.5"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.12"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5850"/>
              <adiabaticHead unit="kJ_per_kg" value="30.4"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.78"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6500"/>
              <adiabaticHead unit="kJ_per_kg" value="37.2"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.48"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.8">
            <measurement>
              <speed unit="per_min" value="3250"/>
              <adiabaticHead unit="kJ_per_kg" value="9.6"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.5"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3900"/>
              <adiabaticHead unit="kJ_per_kg" value="13.4"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.11"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4550"/>
              <adiabaticHead unit="kJ_per_kg" value="17.9"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.73"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5200"/>
              <adiabaticHead unit="kJ_per_kg" value="22.8"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.39"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5850"/>
              <adiabaticHead unit="kJ_per_kg" value="28.2"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.06"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6500"/>
              <adiabaticHead unit="kJ_per_kg" value="34.4"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.76"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.75">
            <measurement>
              <speed unit="per_min" value="3250"/>
              <adiabaticHead unit="kJ_per_kg" value="8.8"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.69"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3900"/>
              <adiabaticHead unit="kJ_per_kg" value="12.1"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.33"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4550"/>
              <adiabaticHead unit="kJ_per_kg" value="16.1"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.01"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5200"/>
              <adiabaticHead unit="kJ_per_kg" value="20.5"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.7"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5850"/>
              <adiabaticHead unit="kJ_per_kg" value="25.2"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.39"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6500"/>
              <adiabaticHead unit="kJ_per_kg" value="30.2"/>
              <volumetricFlowrate unit="m_cube_per_s" value="6.11"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.7">
            <measurement>
              <speed unit="per_min" value="3250"/>
              <adiabaticHead unit="kJ_per_kg" value="8.1"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.82"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3900"/>
              <adiabaticHead unit="kJ_per_kg" value="11.2"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.48"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4550"/>
              <adiabaticHead unit="kJ_per_kg" value="14.7"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.21"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5200"/>
              <adiabaticHead unit="kJ_per_kg" value="18.7"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.92"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5850"/>
              <adiabaticHead unit="kJ_per_kg" value="22.8"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.62"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6500"/>
              <adiabaticHead unit="kJ_per_kg" value="27.2"/>
              <volumetricFlowrate unit="m_cube_per_s" value="6.33"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.65">
            <measurement>
              <speed unit="per_min" value="3250"/>
              <adiabaticHead unit="kJ_per_kg" value="7.4"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.94"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3900"/>
              <adiabaticHead unit="kJ_per_kg" value="10.2"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.62"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4550"/>
              <adiabaticHead unit="kJ_per_kg" value="13.5"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.37"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5200"/>
              <adiabaticHead unit="kJ_per_kg" value="17"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.1"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5850"/>
              <adiabaticHead unit="kJ_per_kg" value="20.6"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.81"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6500"/>
              <adiabaticHead unit="kJ_per_kg" value="24.4"/>
              <volumetricFlowrate unit="m_cube_per_s" value="6.52"/>
            </measurement>
          </adiabaticEfficiency>
        </characteristicDiagramMeasurements>
      </turboCompressor>
      <turboCompressor drive="drive_6" id="compressor_6">
        <speedMin unit="per_min" value="3000"/>
        <speedMax unit="per_min" value="5200"/>
        <n_isoline_coeff_1 value="-40.8365206812"/>
        <n_isoline_coeff_2 value="0.023198020437"/>
        <n_isoline_coeff_3 value="-1.88602485945e-06"/>
        <n_isoline_coeff_4 value="11.2779619949"/>
        <n_isoline_coeff_5 value="-0.00244367499107"/>
        <n_isoline_coeff_6 value="8.50955873332e-07"/>
        <n_isoline_coeff_7 value="-2.76425528052"/>
        <n_isoline_coeff_8 value="0.000464540079018"/>
        <n_isoline_coeff_9 value="-6.00292490512e-08"/>
        <eta_ad_isoline_coeff_1 value="-0.11669598065"/>
        <eta_ad_isoline_coeff_2 value="0.000375549708864"/>
        <eta_ad_isoline_coeff_3 value="-9.39029631366e-08"/>
        <eta_ad_isoline_coeff_4 value="0.329320327616"/>
        <eta_ad_isoline_coeff_5 value="-1.962148064e-05"/>
        <eta_ad_isoline_coeff_6 value="8.05762485416e-09"/>
        <eta_ad_isoline_coeff_7 value="-0.085849449983"/>
        <eta_ad_isoline_coeff_8 value="1.77000414996e-05"/>
        <eta_ad_isoline_coeff_9 value="-1.42391517632e-09"/>
        <surgeline_coeff_1 value="-19.7070619317"/>
        <surgeline_coeff_2 value="21.8522221429"/>
        <surgeline_coeff_3 value="0.348221519402"/>
        <chokeline_coeff_1 value="-19.928505497"/>
        <chokeline_coeff_2 value="2.2687847928"/>
        <chokeline_coeff_3 value="0.578915971189"/>
        <efficiencyOfChokeline value="0.6"/>
        <surgelineMeasurements>
          <measurement>
            <speed unit="per_min" value="3000"/>
            <adiabaticHead unit="kJ_per_kg" value="29.4"/>
            <volumetricFlowrate unit="m_cube_per_s" value="2.18"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="3500"/>
            <adiabaticHead unit="kJ_per_kg" value="39.9"/>
            <volumetricFlowrate unit="m_cube_per_s" value="2.61"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="4000"/>
            <adiabaticHead unit="kJ_per_kg" value="52.2"/>
            <volumetricFlowrate unit="m_cube_per_s" value="3.12"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="4500"/>
            <adiabaticHead unit="kJ_per_kg" value="65.1"/>
            <volumetricFlowrate unit="m_cube_per_s" value="3.69"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="4950"/>
            <adiabaticHead unit="kJ_per_kg" value="79.9"/>
            <volumetricFlowrate unit="m_cube_per_s" value="4.26"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="5200"/>
            <adiabaticHead unit="kJ_per_kg" value="88.2"/>
            <volumetricFlowrate unit="m_cube_per_s" value="4.6"/>
          </measurement>
        </surgelineMeasurements>
        <characteristicDiagramMeasurements>
          <adiabaticEfficiency value="0.75">
            <measurement>
              <speed unit="per_min" value="3000"/>
              <adiabaticHead unit="kJ_per_kg" value="29.3"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.5"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3500"/>
              <adiabaticHead unit="kJ_per_kg" value="39.8"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.88"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4000"/>
              <adiabaticHead unit="kJ_per_kg" value="52.1"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.37"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4500"/>
              <adiabaticHead unit="kJ_per_kg" value="66"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4950"/>
              <adiabaticHead unit="kJ_per_kg" value="79.7"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.72"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5200"/>
              <adiabaticHead unit="kJ_per_kg" value="87.7"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.25"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.78">
            <measurement>
              <speed unit="per_min" value="3000"/>
              <adiabaticHead unit="kJ_per_kg" value="28.7"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.27"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3500"/>
              <adiabaticHead unit="kJ_per_kg" value="39.3"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.63"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4000"/>
              <adiabaticHead unit="kJ_per_kg" value="51.6"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.12"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4500"/>
              <adiabaticHead unit="kJ_per_kg" value="65.5"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.76"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4950"/>
              <adiabaticHead unit="kJ_per_kg" value="78.8"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.51"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5200"/>
              <adiabaticHead unit="kJ_per_kg" value="86.3"/>
              <volumetricFlowrate unit="m_cube_per_s" value="6.05"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.78">
            <measurement>
              <speed unit="per_min" value="3000"/>
              <adiabaticHead unit="kJ_per_kg" value="24.9"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.6"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3500"/>
              <adiabaticHead unit="kJ_per_kg" value="33.5"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.42"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4000"/>
              <adiabaticHead unit="kJ_per_kg" value="43.3"/>
              <volumetricFlowrate unit="m_cube_per_s" value="6.25"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4500"/>
              <adiabaticHead unit="kJ_per_kg" value="54.7"/>
              <volumetricFlowrate unit="m_cube_per_s" value="7.13"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4950"/>
              <adiabaticHead unit="kJ_per_kg" value="66.1"/>
              <volumetricFlowrate unit="m_cube_per_s" value="7.86"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5200"/>
              <adiabaticHead unit="kJ_per_kg" value="73.3"/>
              <volumetricFlowrate unit="m_cube_per_s" value="8.22"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.75">
            <measurement>
              <speed unit="per_min" value="3000"/>
              <adiabaticHead unit="kJ_per_kg" value="22.4"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3500"/>
              <adiabaticHead unit="kJ_per_kg" value="30.7"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.8"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4000"/>
              <adiabaticHead unit="kJ_per_kg" value="40.2"/>
              <volumetricFlowrate unit="m_cube_per_s" value="6.61"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4500"/>
              <adiabaticHead unit="kJ_per_kg" value="51.5"/>
              <volumetricFlowrate unit="m_cube_per_s" value="7.45"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4950"/>
              <adiabaticHead unit="kJ_per_kg" value="62.3"/>
              <volumetricFlowrate unit="m_cube_per_s" value="8.2"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5200"/>
              <adiabaticHead unit="kJ_per_kg" value="68.9"/>
              <volumetricFlowrate unit="m_cube_per_s" value="8.6"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.7">
            <measurement>
              <speed unit="per_min" value="3000"/>
              <adiabaticHead unit="kJ_per_kg" value="18.8"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.42"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3500"/>
              <adiabaticHead unit="kJ_per_kg" value="27.1"/>
              <volumetricFlowrate unit="m_cube_per_s" value="6.18"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4000"/>
              <adiabaticHead unit="kJ_per_kg" value="36.4"/>
              <volumetricFlowrate unit="m_cube_per_s" value="6.98"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4500"/>
              <adiabaticHead unit="kJ_per_kg" value="47.1"/>
              <volumetricFlowrate unit="m_cube_per_s" value="7.82"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4950"/>
              <adiabaticHead unit="kJ_per_kg" value="57.3"/>
              <volumetricFlowrate unit="m_cube_per_s" value="8.58"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5200"/>
              <adiabaticHead unit="kJ_per_kg" value="63.8"/>
              <volumetricFlowrate unit="m_cube_per_s" value="8.98"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.65">
            <measurement>
              <speed unit="per_min" value="3000"/>
              <adiabaticHead unit="kJ_per_kg" value="16.3"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.66"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3500"/>
              <adiabaticHead unit="kJ_per_kg" value="24.2"/>
              <volumetricFlowrate unit="m_cube_per_s" value="6.44"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4000"/>
              <adiabaticHead unit="kJ_per_kg" value="33.2"/>
              <volumetricFlowrate unit="m_cube_per_s" value="7.24"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4500"/>
              <adiabaticHead unit="kJ_per_kg" value="43.2"/>
              <volumetricFlowrate unit="m_cube_per_s" value="8.1"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4950"/>
              <adiabaticHead unit="kJ_per_kg" value="53.3"/>
              <volumetricFlowrate unit="m_cube_per_s" value="8.85"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5200"/>
              <adiabaticHead unit="kJ_per_kg" value="59.6"/>
              <volumetricFlowrate unit="m_cube_per_s" value="9.25"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.6">
            <measurement>
              <speed unit="per_min" value="3000"/>
              <adiabaticHead unit="kJ_per_kg" value="14.3"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.83"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3500"/>
              <adiabaticHead unit="kJ_per_kg" value="22.1"/>
              <volumetricFlowrate unit="m_cube_per_s" value="6.61"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4000"/>
              <adiabaticHead unit="kJ_per_kg" value="30.9"/>
              <volumetricFlowrate unit="m_cube_per_s" value="7.41"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4500"/>
              <adiabaticHead unit="kJ_per_kg" value="40.6"/>
              <volumetricFlowrate unit="m_cube_per_s" value="8.27"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4950"/>
              <adiabaticHead unit="kJ_per_kg" value="50.3"/>
              <volumetricFlowrate unit="m_cube_per_s" value="9.03"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5200"/>
              <adiabaticHead unit="kJ_per_kg" value="56.5"/>
              <volumetricFlowrate unit="m_cube_per_s" value="9.43"/>
            </measurement>
          </adiabaticEfficiency>
        </characteristicDiagramMeasurements>
      </turboCompressor>
      <turboCompressor drive="drive_7" id="compressor_7">
        <speedMin unit="per_min" value="3000"/>
        <speedMax unit="per_min" value="5200"/>
        <n_isoline_coeff_1 value="-33.3659259033"/>
        <n_isoline_coeff_2 value="0.0203860779648"/>
        <n_isoline_coeff_3 value="-1.46134935625e-06"/>
        <n_isoline_coeff_4 value="8.19017159855"/>
        <n_isoline_coeff_5 value="-0.00171482427509"/>
        <n_isoline_coeff_6 value="7.76818702073e-07"/>
        <n_isoline_coeff_7 value="-2.28364091477"/>
        <n_isoline_coeff_8 value="0.000339815464487"/>
        <n_isoline_coeff_9 value="-5.04004677381e-08"/>
        <eta_ad_isoline_coeff_1 value="0.34284957807"/>
        <eta_ad_isoline_coeff_2 value="0.000153300890144"/>
        <eta_ad_isoline_coeff_3 value="-5.33554978626e-08"/>
        <eta_ad_isoline_coeff_4 value="0.211748876587"/>
        <eta_ad_isoline_coeff_5 value="1.03344189514e-05"/>
        <eta_ad_isoline_coeff_6 value="2.22722187809e-09"/>
        <eta_ad_isoline_coeff_7 value="-0.0693655497044"/>
        <eta_ad_isoline_coeff_8 value="1.43875704121e-05"/>
        <eta_ad_isoline_coeff_9 value="-1.08143414598e-09"/>
        <surgeline_coeff_1 value="-161.601428844"/>
        <surgeline_coeff_2 value="77.7888001455"/>
        <surgeline_coeff_3 value="-5.92801932759"/>
        <chokeline_coeff_1 value="-19.0991651272"/>
        <chokeline_coeff_2 value="3.3597721054"/>
        <chokeline_coeff_3 value="0.48895666172"/>
        <efficiencyOfChokeline value="0.65"/>
        <surgelineMeasurements>
          <measurement>
            <speed unit="per_min" value="3000"/>
            <adiabaticHead unit="kJ_per_kg" value="28.7"/>
            <volumetricFlowrate unit="m_cube_per_s" value="3.25"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="3500"/>
            <adiabaticHead unit="kJ_per_kg" value="39.4"/>
            <volumetricFlowrate unit="m_cube_per_s" value="3.55"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="4000"/>
            <adiabaticHead unit="kJ_per_kg" value="51.8"/>
            <volumetricFlowrate unit="m_cube_per_s" value="3.9"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="4500"/>
            <adiabaticHead unit="kJ_per_kg" value="65.8"/>
            <volumetricFlowrate unit="m_cube_per_s" value="4.37"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="4950"/>
            <adiabaticHead unit="kJ_per_kg" value="79.4"/>
            <volumetricFlowrate unit="m_cube_per_s" value="5.07"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="5200"/>
            <adiabaticHead unit="kJ_per_kg" value="87.4"/>
            <volumetricFlowrate unit="m_cube_per_s" value="5.5"/>
          </measurement>
        </surgelineMeasurements>
        <characteristicDiagramMeasurements>
          <adiabaticEfficiency value="0.75">
            <measurement>
              <speed unit="per_min" value="3000"/>
              <adiabaticHead unit="kJ_per_kg" value="29.3"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.4"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3500"/>
              <adiabaticHead unit="kJ_per_kg" value="39.8"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.8"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4000"/>
              <adiabaticHead unit="kJ_per_kg" value="52.1"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.35"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4500"/>
              <adiabaticHead unit="kJ_per_kg" value="66"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.97"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4950"/>
              <adiabaticHead unit="kJ_per_kg" value="79.7"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.7"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5200"/>
              <adiabaticHead unit="kJ_per_kg" value="87.7"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.2"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.78">
            <measurement>
              <speed unit="per_min" value="3000"/>
              <adiabaticHead unit="kJ_per_kg" value="29"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.96"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3500"/>
              <adiabaticHead unit="kJ_per_kg" value="39.5"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.37"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4000"/>
              <adiabaticHead unit="kJ_per_kg" value="51.8"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.88"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4500"/>
              <adiabaticHead unit="kJ_per_kg" value="65.7"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.5"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4950"/>
              <adiabaticHead unit="kJ_per_kg" value="79.2"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.25"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5200"/>
              <adiabaticHead unit="kJ_per_kg" value="86.9"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.81"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.8">
            <measurement>
              <speed unit="per_min" value="3000"/>
              <adiabaticHead unit="kJ_per_kg" value="28.5"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.42"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3500"/>
              <adiabaticHead unit="kJ_per_kg" value="39"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.87"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4000"/>
              <adiabaticHead unit="kJ_per_kg" value="51.1"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.43"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4500"/>
              <adiabaticHead unit="kJ_per_kg" value="64.9"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.12"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4950"/>
              <adiabaticHead unit="kJ_per_kg" value="77.9"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.9"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5200"/>
              <adiabaticHead unit="kJ_per_kg" value="85.1"/>
              <volumetricFlowrate unit="m_cube_per_s" value="6.45"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.8">
            <measurement>
              <speed unit="per_min" value="3000"/>
              <adiabaticHead unit="kJ_per_kg" value="27.1"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.05"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3500"/>
              <adiabaticHead unit="kJ_per_kg" value="36.5"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.85"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4000"/>
              <adiabaticHead unit="kJ_per_kg" value="47"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.67"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4500"/>
              <adiabaticHead unit="kJ_per_kg" value="59.5"/>
              <volumetricFlowrate unit="m_cube_per_s" value="6.52"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4950"/>
              <adiabaticHead unit="kJ_per_kg" value="71.6"/>
              <volumetricFlowrate unit="m_cube_per_s" value="7.22"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5200"/>
              <adiabaticHead unit="kJ_per_kg" value="79.4"/>
              <volumetricFlowrate unit="m_cube_per_s" value="7.53"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.78">
            <measurement>
              <speed unit="per_min" value="3000"/>
              <adiabaticHead unit="kJ_per_kg" value="25.5"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.46"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3500"/>
              <adiabaticHead unit="kJ_per_kg" value="34.4"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.27"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4000"/>
              <adiabaticHead unit="kJ_per_kg" value="44.3"/>
              <volumetricFlowrate unit="m_cube_per_s" value="6.12"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4500"/>
              <adiabaticHead unit="kJ_per_kg" value="55.8"/>
              <volumetricFlowrate unit="m_cube_per_s" value="7.01"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4950"/>
              <adiabaticHead unit="kJ_per_kg" value="67.3"/>
              <volumetricFlowrate unit="m_cube_per_s" value="7.74"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5200"/>
              <adiabaticHead unit="kJ_per_kg" value="74.4"/>
              <volumetricFlowrate unit="m_cube_per_s" value="8.11"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.75">
            <measurement>
              <speed unit="per_min" value="3000"/>
              <adiabaticHead unit="kJ_per_kg" value="22.6"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.96"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3500"/>
              <adiabaticHead unit="kJ_per_kg" value="31"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.76"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4000"/>
              <adiabaticHead unit="kJ_per_kg" value="40.3"/>
              <volumetricFlowrate unit="m_cube_per_s" value="6.6"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4500"/>
              <adiabaticHead unit="kJ_per_kg" value="51.1"/>
              <volumetricFlowrate unit="m_cube_per_s" value="7.49"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4950"/>
              <adiabaticHead unit="kJ_per_kg" value="61.8"/>
              <volumetricFlowrate unit="m_cube_per_s" value="8.24"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5200"/>
              <adiabaticHead unit="kJ_per_kg" value="68.3"/>
              <volumetricFlowrate unit="m_cube_per_s" value="8.65"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.7">
            <measurement>
              <speed unit="per_min" value="3000"/>
              <adiabaticHead unit="kJ_per_kg" value="19.2"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.38"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3500"/>
              <adiabaticHead unit="kJ_per_kg" value="27.1"/>
              <volumetricFlowrate unit="m_cube_per_s" value="6.18"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4000"/>
              <adiabaticHead unit="kJ_per_kg" value="36"/>
              <volumetricFlowrate unit="m_cube_per_s" value="7.01"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4500"/>
              <adiabaticHead unit="kJ_per_kg" value="46.1"/>
              <volumetricFlowrate unit="m_cube_per_s" value="7.9"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4950"/>
              <adiabaticHead unit="kJ_per_kg" value="56.3"/>
              <volumetricFlowrate unit="m_cube_per_s" value="8.65"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5200"/>
              <adiabaticHead unit="kJ_per_kg" value="62.4"/>
              <volumetricFlowrate unit="m_cube_per_s" value="9.07"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.65">
            <measurement>
              <speed unit="per_min" value="3000"/>
              <adiabaticHead unit="kJ_per_kg" value="16.3"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.66"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3500"/>
              <adiabaticHead unit="kJ_per_kg" value="24.1"/>
              <volumetricFlowrate unit="m_cube_per_s" value="6.45"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4000"/>
              <adiabaticHead unit="kJ_per_kg" value="32.5"/>
              <volumetricFlowrate unit="m_cube_per_s" value="7.29"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4500"/>
              <adiabaticHead unit="kJ_per_kg" value="42.6"/>
              <volumetricFlowrate unit="m_cube_per_s" value="8.14"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4950"/>
              <adiabaticHead unit="kJ_per_kg" value="52.3"/>
              <volumetricFlowrate unit="m_cube_per_s" value="8.91"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5200"/>
              <adiabaticHead unit="kJ_per_kg" value="58.4"/>
              <volumetricFlowrate unit="m_cube_per_s" value="9.32"/>
            </measurement>
          </adiabaticEfficiency>
        </characteristicDiagramMeasurements>
      </turboCompressor>
      <turboCompressor drive="drive_8" id="compressor_8">
        <speedMin unit="per_min" value="3250"/>
        <speedMax unit="per_min" value="6825"/>
        <n_isoline_coeff_1 value="0"/>
        <n_isoline_coeff_2 value="0.006961182417582417"/>
        <n_isoline_coeff_3 value="0"/>
        <n_isoline_coeff_4 value="0"/>
        <n_isoline_coeff_5 value="0"/>
        <n_isoline_coeff_6 value="0"/>
        <n_isoline_coeff_7 value="-1.055591732632306"/>
        <n_isoline_coeff_8 value="3.86663638326852e-05"/>
        <n_isoline_coeff_9 value="0"/>
        <eta_ad_isoline_coeff_1 value="0.8458806099848061"/>
        <eta_ad_isoline_coeff_2 value="-1.624275291904094e-05"/>
        <eta_ad_isoline_coeff_3 value="1.282329921753092e-09"/>
        <eta_ad_isoline_coeff_4 value="0.005641876825114986"/>
        <eta_ad_isoline_coeff_5 value="1.308080734575116e-05"/>
        <eta_ad_isoline_coeff_6 value="-1.396485381010221e-09"/>
        <eta_ad_isoline_coeff_7 value="-0.02465862859621726"/>
        <eta_ad_isoline_coeff_8 value="3.713478420144851e-06"/>
        <eta_ad_isoline_coeff_9 value="-1.538758228985989e-10"/>
        <surgeline_coeff_1 value="-2.115329307142858"/>
        <surgeline_coeff_2 value="73.43947320257401"/>
        <surgeline_coeff_3 value="0"/>
        <chokeline_coeff_1 value="-0.7943487409135273"/>
        <chokeline_coeff_2 value="1.888842451841391"/>
        <chokeline_coeff_3 value="0"/>
        <efficiencyOfChokeline value="0.7"/>
        <surgelineMeasurements>
          <measurement>
            <speed unit="per_min" value="3250"/>
            <adiabaticHead unit="kJ_per_kg" value="22.51920758392847"/>
            <volumetricFlowrate unit="m_cube_per_s" value="0.3354399999999987"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="3696.875"/>
            <adiabaticHead unit="kJ_per_kg" value="25.60459595620838"/>
            <volumetricFlowrate unit="m_cube_per_s" value="0.3774526702675159"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="4143.75"/>
            <adiabaticHead unit="kJ_per_kg" value="28.68788011766395"/>
            <volumetricFlowrate unit="m_cube_per_s" value="0.4194366882213307"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="4590.625"/>
            <adiabaticHead unit="kJ_per_kg" value="31.76924609910817"/>
            <volumetricFlowrate unit="m_cube_per_s" value="0.461394586978919"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="5037.5"/>
            <adiabaticHead unit="kJ_per_kg" value="34.84887887088582"/>
            <volumetricFlowrate unit="m_cube_per_s" value="0.5033288852177266"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="5484.375"/>
            <adiabaticHead unit="kJ_per_kg" value="37.92696242064807"/>
            <volumetricFlowrate unit="m_cube_per_s" value="0.5452420882341987"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="5931.25"/>
            <adiabaticHead unit="kJ_per_kg" value="41.00367982995051"/>
            <volumetricFlowrate unit="m_cube_per_s" value="0.5871366889867896"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="6378.125"/>
            <adiabaticHead unit="kJ_per_kg" value="44.07921334976838"/>
            <volumetricFlowrate unit="m_cube_per_s" value="0.6290151691242272"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="6825"/>
            <adiabaticHead unit="kJ_per_kg" value="47.15374447499967"/>
            <volumetricFlowrate unit="m_cube_per_s" value="0.6708799999999956"/>
          </measurement>
        </surgelineMeasurements>
        <characteristicDiagramMeasurements>
          <adiabaticEfficiency value="0.82">
            <measurement>
              <speed unit="per_min" value="3250"/>
              <adiabaticHead unit="kJ_per_kg" value="22.09017452044428"/>
              <volumetricFlowrate unit="m_cube_per_s" value="0.7575503639968711"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3696.875"/>
              <adiabaticHead unit="kJ_per_kg" value="25.06915709327773"/>
              <volumetricFlowrate unit="m_cube_per_s" value="0.853907669908434"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4143.75"/>
              <adiabaticHead unit="kJ_per_kg" value="28.03746655558662"/>
              <volumetricFlowrate unit="m_cube_per_s" value="0.949919746483907"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4590.625"/>
              <adiabaticHead unit="kJ_per_kg" value="30.9961442689444"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.045620277302581"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5037.5"/>
              <adiabaticHead unit="kJ_per_kg" value="33.94620186845141"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.141041984419872"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5484.375"/>
              <adiabaticHead unit="kJ_per_kg" value="36.88862410309304"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.236216720240725"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5931.25"/>
              <adiabaticHead unit="kJ_per_kg" value="39.82437148728734"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.3311755532858"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6378.125"/>
              <adiabaticHead unit="kJ_per_kg" value="42.75438278507145"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.425948848544249"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6825"/>
              <adiabaticHead unit="kJ_per_kg" value="45.67957734614575"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.52056634303472"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.82">
            <measurement>
              <speed unit="per_min" value="3250"/>
              <adiabaticHead unit="kJ_per_kg" value="21.20932589968547"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.23333163747931"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3696.875"/>
              <adiabaticHead unit="kJ_per_kg" value="23.98003525765085"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.386551194070425"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4143.75"/>
              <adiabaticHead unit="kJ_per_kg" value="26.72630238353448"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.538419101145902"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4590.625"/>
              <adiabaticHead unit="kJ_per_kg" value="29.45096198593187"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.689092117404674"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5037.5"/>
              <adiabaticHead unit="kJ_per_kg" value="32.15666219369679"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.838716683731131"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5484.375"/>
              <adiabaticHead unit="kJ_per_kg" value="34.84588965539792"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.987430311188999"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5931.25"/>
              <adiabaticHead unit="kJ_per_kg" value="37.52099127763125"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.135362783144754"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6378.125"/>
              <adiabaticHead unit="kJ_per_kg" value="40.18419319228759"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.282637204152917"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6825"/>
              <adiabaticHead unit="kJ_per_kg" value="42.83761743062953"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.429370922028477"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.82">
            <measurement>
              <speed unit="per_min" value="3250"/>
              <adiabaticHead unit="kJ_per_kg" value="19.7879707471881"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.746301044673091"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3696.875"/>
              <adiabaticHead unit="kJ_per_kg" value="22.25185069077001"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.953489191010483"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4143.75"/>
              <adiabaticHead unit="kJ_per_kg" value="24.67771130824747"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.157480284779996"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4590.625"/>
              <adiabaticHead unit="kJ_per_kg" value="27.07087098739491"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.358721550249741"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5037.5"/>
              <adiabaticHead unit="kJ_per_kg" value="29.43607300057907"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.557611850120719"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5484.375"/>
              <adiabaticHead unit="kJ_per_kg" value="31.77758949822825"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.754510430357986"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5931.25"/>
              <adiabaticHead unit="kJ_per_kg" value="34.0993047079822"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.949743916423441"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6378.125"/>
              <adiabaticHead unit="kJ_per_kg" value="36.40478238399697"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.143611985101058"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6825"/>
              <adiabaticHead unit="kJ_per_kg" value="38.69732119049556"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.336392021710496"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.82">
            <measurement>
              <speed unit="per_min" value="3250"/>
              <adiabaticHead unit="kJ_per_kg" value="17.82364222798264"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.271985146848936"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3696.875"/>
              <adiabaticHead unit="kJ_per_kg" value="19.91382518206852"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.525455801532206"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4143.75"/>
              <adiabaticHead unit="kJ_per_kg" value="21.95844777038729"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.773401477784269"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4590.625"/>
              <adiabaticHead unit="kJ_per_kg" value="23.96499184838378"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.016729479338581"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5037.5"/>
              <adiabaticHead unit="kJ_per_kg" value="25.93984623974898"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.256214561017658"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5484.375"/>
              <adiabaticHead unit="kJ_per_kg" value="27.88855104725646"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.492528555626504"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5931.25"/>
              <adiabaticHead unit="kJ_per_kg" value="29.81597975344903"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.726262456794796"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6378.125"/>
              <adiabaticHead unit="kJ_per_kg" value="31.72647776494025"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.957943219857736"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6825"/>
              <adiabaticHead unit="kJ_per_kg" value="33.62396983786164"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.188046789040291"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.7899999999999999">
            <measurement>
              <speed unit="per_min" value="3250"/>
              <adiabaticHead unit="kJ_per_kg" value="15.40954594932228"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.785305258272372"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3696.875"/>
              <adiabaticHead unit="kJ_per_kg" value="17.10375139982852"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.075217688845954"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4143.75"/>
              <adiabaticHead unit="kJ_per_kg" value="18.75273775496144"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.357392227982519"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4590.625"/>
              <adiabaticHead unit="kJ_per_kg" value="20.36488157649351"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.633262272902329"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5037.5"/>
              <adiabaticHead unit="kJ_per_kg" value="21.94709499759836"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.904010627809099"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5484.375"/>
              <adiabaticHead unit="kJ_per_kg" value="23.50520139439565"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.170633788803399"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5931.25"/>
              <adiabaticHead unit="kJ_per_kg" value="25.04420047309688"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.433987305594091"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6378.125"/>
              <adiabaticHead unit="kJ_per_kg" value="26.56846055685628"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.694818685623551"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6825"/>
              <adiabaticHead unit="kJ_per_kg" value="28.08186156656757"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.953791860941108"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.76">
            <measurement>
              <speed unit="per_min" value="3250"/>
              <adiabaticHead unit="kJ_per_kg" value="12.69584100801363"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.267433201644335"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3696.875"/>
              <adiabaticHead unit="kJ_per_kg" value="14.00871315844831"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.584444193090063"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4143.75"/>
              <adiabaticHead unit="kJ_per_kg" value="15.28251648997935"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.892021482243335"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4590.625"/>
              <adiabaticHead unit="kJ_per_kg" value="16.52513462516704"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.192068677923331"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5037.5"/>
              <adiabaticHead unit="kJ_per_kg" value="17.74292160250717"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.486120049893156"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5484.375"/>
              <adiabaticHead unit="kJ_per_kg" value="18.94112901577795"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.775443667514891"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5931.25"/>
              <adiabaticHead unit="kJ_per_kg" value="20.12419622617238"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.061111475450261"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6378.125"/>
              <adiabaticHead unit="kJ_per_kg" value="21.29595420952258"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.344048515369424"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6825"/>
              <adiabaticHead unit="kJ_per_kg" value="22.45977300685667"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.625068529910749"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.73">
            <measurement>
              <speed unit="per_min" value="3250"/>
              <adiabaticHead unit="kJ_per_kg" value="9.836993664468942"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.708152313840845"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3696.875"/>
              <adiabaticHead unit="kJ_per_kg" value="10.80368442527009"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.044753962945242"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4143.75"/>
              <adiabaticHead unit="kJ_per_kg" value="11.74014771805541"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.370830409994388"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4590.625"/>
              <adiabaticHead unit="kJ_per_kg" value="12.65286316315169"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.688637858291349"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5037.5"/>
              <adiabaticHead unit="kJ_per_kg" value="13.54697820166996"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.999968646437985"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5484.375"/>
              <adiabaticHead unit="kJ_per_kg" value="14.42669941126553"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.306287504452704"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5931.25"/>
              <adiabaticHead unit="kJ_per_kg" value="15.29555208958248"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.60882194070601"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6378.125"/>
              <adiabaticHead unit="kJ_per_kg" value="16.15655898535405"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.908624476076043"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6825"/>
              <adiabaticHead unit="kJ_per_kg" value="17.01236743398132"/>
              <volumetricFlowrate unit="m_cube_per_s" value="6.20661691254733"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.7">
            <measurement>
              <speed unit="per_min" value="3250"/>
              <adiabaticHead unit="kJ_per_kg" value="6.958216218424276"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.104399999999999"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3696.875"/>
              <adiabaticHead unit="kJ_per_kg" value="7.620604352610146"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.455084692384015"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4143.75"/>
              <adiabaticHead unit="kJ_per_kg" value="8.262006303660979"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.794658779373401"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4590.625"/>
              <adiabaticHead unit="kJ_per_kg" value="8.887122961203758"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.125611028425919"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5037.5"/>
              <adiabaticHead unit="kJ_per_kg" value="9.499659464027797"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.449903031830909"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5484.375"/>
              <adiabaticHead unit="kJ_per_kg" value="10.10262638880576"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.769128663481736"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5931.25"/>
              <adiabaticHead unit="kJ_per_kg" value="10.69853677481065"/>
              <volumetricFlowrate unit="m_cube_per_s" value="6.084618388643276"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6378.125"/>
              <adiabaticHead unit="kJ_per_kg" value="11.28954024092534"/>
              <volumetricFlowrate unit="m_cube_per_s" value="6.397510268820226"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6825"/>
              <adiabaticHead unit="kJ_per_kg" value="11.87751749999999"/>
              <volumetricFlowrate unit="m_cube_per_s" value="6.708799999999999"/>
            </measurement>
          </adiabaticEfficiency>
        </characteristicDiagramMeasurements>
      </turboCompressor>
    </compressors>
    <drives>
      <gasTurbine id="drive_3">
        <energy_rate_fun_coeff_1 value="4001.75"/>
        <energy_rate_fun_coeff_2 value="2.60806666667"/>
        <energy_rate_fun_coeff_3 value="4.44444444444e-07"/>
        <power_fun_coeff_1 value="40.5292488128"/>
        <power_fun_coeff_2 value="0.596873936875"/>
        <power_fun_coeff_3 value="-2.49782158305e-05"/>
        <power_fun_coeff_4 value="-0.321905166853"/>
        <power_fun_coeff_5 value="-0.00366792233187"/>
        <power_fun_coeff_6 value="1.53529399121e-07"/>
        <power_fun_coeff_7 value="0.00123383043552"/>
        <power_fun_coeff_8 value="4.37942089676e-06"/>
        <power_fun_coeff_9 value="-2.00808640022e-10"/>
        <specificEnergyConsumptionMeasurements>
          <measurement>
            <compressorPower unit="kW" value="3000"/>
            <fuelConsumption unit="kW" value="11830"/>
          </measurement>
          <measurement>
            <compressorPower unit="kW" value="2250"/>
            <fuelConsumption unit="kW" value="9872"/>
          </measurement>
          <measurement>
            <compressorPower unit="kW" value="1500"/>
            <fuelConsumption unit="kW" value="7915"/>
          </measurement>
          <measurement>
            <compressorPower unit="kW" value="750"/>
            <fuelConsumption unit="kW" value="5958"/>
          </measurement>
        </specificEnergyConsumptionMeasurements>
        <maximalPowerMeasurements>
          <ambientTemperature unit="Celsius" value="-5">
            <measurement>
              <speed unit="per_min" value="5760"/>
              <maximalPower unit="kW" value="2732"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6000"/>
              <maximalPower unit="kW" value="2807"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="7000"/>
              <maximalPower unit="kW" value="3088"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="8000"/>
              <maximalPower unit="kW" value="3317"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="9000"/>
              <maximalPower unit="kW" value="3494"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="10000"/>
              <maximalPower unit="kW" value="3620"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="11000"/>
              <maximalPower unit="kW" value="3695"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="11600"/>
              <maximalPower unit="kW" value="3715"/>
            </measurement>
          </ambientTemperature>
          <ambientTemperature unit="Celsius" value="5">
            <measurement>
              <speed unit="per_min" value="5760"/>
              <maximalPower unit="kW" value="2568"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6000"/>
              <maximalPower unit="kW" value="2639"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="7000"/>
              <maximalPower unit="kW" value="2903"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="8000"/>
              <maximalPower unit="kW" value="3119"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="9000"/>
              <maximalPower unit="kW" value="3285"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="10000"/>
              <maximalPower unit="kW" value="3403"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="11000"/>
              <maximalPower unit="kW" value="3474"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="11600"/>
              <maximalPower unit="kW" value="3493"/>
            </measurement>
          </ambientTemperature>
          <ambientTemperature unit="Celsius" value="15">
            <measurement>
              <speed unit="per_min" value="5760"/>
              <maximalPower unit="kW" value="2409"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6000"/>
              <maximalPower unit="kW" value="2475"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="7000"/>
              <maximalPower unit="kW" value="2723"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="8000"/>
              <maximalPower unit="kW" value="2925"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="9000"/>
              <maximalPower unit="kW" value="3081"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="10000"/>
              <maximalPower unit="kW" value="3192"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="11000"/>
              <maximalPower unit="kW" value="3258"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="11600"/>
              <maximalPower unit="kW" value="3276"/>
            </measurement>
          </ambientTemperature>
          <ambientTemperature unit="Celsius" value="25">
            <measurement>
              <speed unit="per_min" value="5760"/>
              <maximalPower unit="kW" value="2253"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6000"/>
              <maximalPower unit="kW" value="2315"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="7000"/>
              <maximalPower unit="kW" value="2547"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="8000"/>
              <maximalPower unit="kW" value="2736"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="9000"/>
              <maximalPower unit="kW" value="2882"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="10000"/>
              <maximalPower unit="kW" value="2985"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="11000"/>
              <maximalPower unit="kW" value="3047"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="11600"/>
              <maximalPower unit="kW" value="3064"/>
            </measurement>
          </ambientTemperature>
        </maximalPowerMeasurements>
      </gasTurbine>
      <gasTurbine id="drive_4">
        <energy_rate_fun_coeff_1 value="3999.25"/>
        <energy_rate_fun_coeff_2 value="2.61124567474"/>
        <energy_rate_fun_coeff_3 value="-3.32584353371e-07"/>
        <power_fun_coeff_1 value="44.8078604044"/>
        <power_fun_coeff_2 value="0.63201008201"/>
        <power_fun_coeff_3 value="-2.64441228934e-05"/>
        <power_fun_coeff_4 value="-0.309863013696"/>
        <power_fun_coeff_5 value="-0.00388350438728"/>
        <power_fun_coeff_6 value="1.61885497754e-07"/>
        <power_fun_coeff_7 value="0.00335942596207"/>
        <power_fun_coeff_8 value="3.42440192466e-06"/>
        <power_fun_coeff_9 value="-1.13702205147e-10"/>
        <specificEnergyConsumptionMeasurements>
          <measurement>
            <compressorPower unit="kW" value="3468"/>
            <fuelConsumption unit="kW" value="13051"/>
          </measurement>
          <measurement>
            <compressorPower unit="kW" value="2601"/>
            <fuelConsumption unit="kW" value="10789"/>
          </measurement>
          <measurement>
            <compressorPower unit="kW" value="1734"/>
            <fuelConsumption unit="kW" value="8526"/>
          </measurement>
          <measurement>
            <compressorPower unit="kW" value="867"/>
            <fuelConsumption unit="kW" value="6263"/>
          </measurement>
        </specificEnergyConsumptionMeasurements>
        <maximalPowerMeasurements>
          <ambientTemperature unit="Celsius" value="-5">
            <measurement>
              <speed unit="per_min" value="5800"/>
              <maximalPower unit="kW" value="2908"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6960"/>
              <maximalPower unit="kW" value="3261"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="8120"/>
              <maximalPower unit="kW" value="3540"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="8700"/>
              <maximalPower unit="kW" value="3652"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="9280"/>
              <maximalPower unit="kW" value="3745"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="9860"/>
              <maximalPower unit="kW" value="3820"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="10440"/>
              <maximalPower unit="kW" value="3877"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="11020"/>
              <maximalPower unit="kW" value="3916"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="11600"/>
              <maximalPower unit="kW" value="3937"/>
            </measurement>
          </ambientTemperature>
          <ambientTemperature unit="Celsius" value="5">
            <measurement>
              <speed unit="per_min" value="5800"/>
              <maximalPower unit="kW" value="2734"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6960"/>
              <maximalPower unit="kW" value="3066"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="8120"/>
              <maximalPower unit="kW" value="3328"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="8700"/>
              <maximalPower unit="kW" value="3433"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="9280"/>
              <maximalPower unit="kW" value="3521"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="9860"/>
              <maximalPower unit="kW" value="3592"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="10440"/>
              <maximalPower unit="kW" value="3645"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="11020"/>
              <maximalPower unit="kW" value="3681"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="11600"/>
              <maximalPower unit="kW" value="3701"/>
            </measurement>
          </ambientTemperature>
          <ambientTemperature unit="Celsius" value="15">
            <measurement>
              <speed unit="per_min" value="5800"/>
              <maximalPower unit="kW" value="2564"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6960"/>
              <maximalPower unit="kW" value="2876"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="8120"/>
              <maximalPower unit="kW" value="3121"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="8700"/>
              <maximalPower unit="kW" value="3220"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="9280"/>
              <maximalPower unit="kW" value="3302"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="9860"/>
              <maximalPower unit="kW" value="3368"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="10440"/>
              <maximalPower unit="kW" value="3418"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="11020"/>
              <maximalPower unit="kW" value="3453"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="11600"/>
              <maximalPower unit="kW" value="3471"/>
            </measurement>
          </ambientTemperature>
          <ambientTemperature unit="Celsius" value="25">
            <measurement>
              <speed unit="per_min" value="5800"/>
              <maximalPower unit="kW" value="2398"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6960"/>
              <maximalPower unit="kW" value="2689"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="8120"/>
              <maximalPower unit="kW" value="2919"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="8700"/>
              <maximalPower unit="kW" value="3011"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="9280"/>
              <maximalPower unit="kW" value="3088"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="9860"/>
              <maximalPower unit="kW" value="3150"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="10440"/>
              <maximalPower unit="kW" value="3197"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="11020"/>
              <maximalPower unit="kW" value="3229"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="11600"/>
              <maximalPower unit="kW" value="3246"/>
            </measurement>
          </ambientTemperature>
        </maximalPowerMeasurements>
      </gasTurbine>
      <gasTurbine id="drive_5">
        <energy_rate_fun_coeff_1 value="10399.3304223"/>
        <energy_rate_fun_coeff_2 value="2.83969382239"/>
        <energy_rate_fun_coeff_3 value="3.60541969571e-08"/>
        <power_fun_coeff_1 value="-2599.19107143"/>
        <power_fun_coeff_2 value="3.73123076923"/>
        <power_fun_coeff_3 value="-0.000239818258664"/>
        <power_fun_coeff_4 value="15.1771428571"/>
        <power_fun_coeff_5 value="-0.022010989011"/>
        <power_fun_coeff_6 value="1.40997464074e-06"/>
        <power_fun_coeff_7 value="-0.0189285714286"/>
        <power_fun_coeff_8 value="4.48351648352e-05"/>
        <power_fun_coeff_9 value="-2.53592561285e-09"/>
        <specificEnergyConsumptionMeasurements>
          <measurement>
            <compressorPower unit="kW" value="10534"/>
            <fuelConsumption unit="kW" value="40317"/>
          </measurement>
          <measurement>
            <compressorPower unit="kW" value="7901"/>
            <fuelConsumption unit="kW" value="32837"/>
          </measurement>
          <measurement>
            <compressorPower unit="kW" value="5267"/>
            <fuelConsumption unit="kW" value="25358"/>
          </measurement>
          <measurement>
            <compressorPower unit="kW" value="2634"/>
            <fuelConsumption unit="kW" value="17879"/>
          </measurement>
        </specificEnergyConsumptionMeasurements>
        <maximalPowerMeasurements>
          <ambientTemperature unit="Celsius" value="-5">
            <measurement>
              <speed unit="per_min" value="3250"/>
              <maximalPower unit="kW" value="7219"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3900"/>
              <maximalPower unit="kW" value="8533"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4550"/>
              <maximalPower unit="kW" value="9683"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5200"/>
              <maximalPower unit="kW" value="10640"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5850"/>
              <maximalPower unit="kW" value="11373"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6500"/>
              <maximalPower unit="kW" value="11852"/>
            </measurement>
          </ambientTemperature>
          <ambientTemperature unit="Celsius" value="5">
            <measurement>
              <speed unit="per_min" value="3250"/>
              <maximalPower unit="kW" value="6804"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3900"/>
              <maximalPower unit="kW" value="8042"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4550"/>
              <maximalPower unit="kW" value="9126"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5200"/>
              <maximalPower unit="kW" value="10028"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5850"/>
              <maximalPower unit="kW" value="10719"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6500"/>
              <maximalPower unit="kW" value="11170"/>
            </measurement>
          </ambientTemperature>
          <ambientTemperature unit="Celsius" value="15">
            <measurement>
              <speed unit="per_min" value="3250"/>
              <maximalPower unit="kW" value="6408"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3900"/>
              <maximalPower unit="kW" value="7574"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4550"/>
              <maximalPower unit="kW" value="8595"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5200"/>
              <maximalPower unit="kW" value="9445"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5850"/>
              <maximalPower unit="kW" value="10095"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6500"/>
              <maximalPower unit="kW" value="10520"/>
            </measurement>
          </ambientTemperature>
          <ambientTemperature unit="Celsius" value="25">
            <measurement>
              <speed unit="per_min" value="3250"/>
              <maximalPower unit="kW" value="6033"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3900"/>
              <maximalPower unit="kW" value="7130"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4550"/>
              <maximalPower unit="kW" value="8091"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5200"/>
              <maximalPower unit="kW" value="8891"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5850"/>
              <maximalPower unit="kW" value="9504"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6500"/>
              <maximalPower unit="kW" value="9904"/>
            </measurement>
          </ambientTemperature>
        </maximalPowerMeasurements>
      </gasTurbine>
      <gasTurbine id="drive_6">
        <energy_rate_fun_coeff_1 value="12498.2900147"/>
        <energy_rate_fun_coeff_2 value="2.42009958771"/>
        <energy_rate_fun_coeff_3 value="-1.66956752455e-19"/>
        <power_fun_coeff_1 value="334.899643188"/>
        <power_fun_coeff_2 value="8.96347437357"/>
        <power_fun_coeff_3 value="-0.00083619727037"/>
        <power_fun_coeff_4 value="-2.18454699782"/>
        <power_fun_coeff_5 value="-0.0552612302044"/>
        <power_fun_coeff_6 value="5.15255264349e-06"/>
        <power_fun_coeff_7 value="0.00310301651687"/>
        <power_fun_coeff_8 value="6.44711022479e-05"/>
        <power_fun_coeff_9 value="-5.93865988614e-09"/>
        <specificEnergyConsumptionMeasurements>
          <measurement>
            <compressorPower unit="kW" value="21207"/>
            <fuelConsumption unit="kW" value="63821"/>
          </measurement>
          <measurement>
            <compressorPower unit="kW" value="15905"/>
            <fuelConsumption unit="kW" value="50991"/>
          </measurement>
          <measurement>
            <compressorPower unit="kW" value="10604"/>
            <fuelConsumption unit="kW" value="38160"/>
          </measurement>
          <measurement>
            <compressorPower unit="kW" value="5302"/>
            <fuelConsumption unit="kW" value="25330"/>
          </measurement>
        </specificEnergyConsumptionMeasurements>
        <maximalPowerMeasurements>
          <ambientTemperature unit="Celsius" value="-5">
            <measurement>
              <speed unit="per_min" value="3000"/>
              <maximalPower unit="kW" value="20310"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3500"/>
              <maximalPower unit="kW" value="22132"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4000"/>
              <maximalPower unit="kW" value="23518"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4500"/>
              <maximalPower unit="kW" value="24473"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4950"/>
              <maximalPower unit="kW" value="24966"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5200"/>
              <maximalPower unit="kW" value="25091"/>
            </measurement>
          </ambientTemperature>
          <ambientTemperature unit="Celsius" value="5">
            <measurement>
              <speed unit="per_min" value="3000"/>
              <maximalPower unit="kW" value="19094"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3500"/>
              <maximalPower unit="kW" value="20807"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4000"/>
              <maximalPower unit="kW" value="22110"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4500"/>
              <maximalPower unit="kW" value="23008"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4950"/>
              <maximalPower unit="kW" value="23471"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5200"/>
              <maximalPower unit="kW" value="23589"/>
            </measurement>
          </ambientTemperature>
          <ambientTemperature unit="Celsius" value="15">
            <measurement>
              <speed unit="per_min" value="3000"/>
              <maximalPower unit="kW" value="17907"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3500"/>
              <maximalPower unit="kW" value="19513"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4000"/>
              <maximalPower unit="kW" value="20736"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4500"/>
              <maximalPower unit="kW" value="21577"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4950"/>
              <maximalPower unit="kW" value="22012"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5200"/>
              <maximalPower unit="kW" value="22122"/>
            </measurement>
          </ambientTemperature>
          <ambientTemperature unit="Celsius" value="25">
            <measurement>
              <speed unit="per_min" value="3000"/>
              <maximalPower unit="kW" value="16748"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3500"/>
              <maximalPower unit="kW" value="18251"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4000"/>
              <maximalPower unit="kW" value="19394"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4500"/>
              <maximalPower unit="kW" value="20181"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4950"/>
              <maximalPower unit="kW" value="20588"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5200"/>
              <maximalPower unit="kW" value="20691"/>
            </measurement>
          </ambientTemperature>
        </maximalPowerMeasurements>
      </gasTurbine>
      <gasTurbine id="drive_7">
        <energy_rate_fun_coeff_1 value="12498.2900147"/>
        <energy_rate_fun_coeff_2 value="2.42009958771"/>
        <energy_rate_fun_coeff_3 value="-1.66956752455e-19"/>
        <power_fun_coeff_1 value="334.899643188"/>
        <power_fun_coeff_2 value="8.96347437357"/>
        <power_fun_coeff_3 value="-0.00083619727037"/>
        <power_fun_coeff_4 value="-2.18454699782"/>
        <power_fun_coeff_5 value="-0.0552612302044"/>
        <power_fun_coeff_6 value="5.15255264349e-06"/>
        <power_fun_coeff_7 value="0.00310301651687"/>
        <power_fun_coeff_8 value="6.44711022479e-05"/>
        <power_fun_coeff_9 value="-5.93865988614e-09"/>
        <specificEnergyConsumptionMeasurements>
          <measurement>
            <compressorPower unit="kW" value="21207"/>
            <fuelConsumption unit="kW" value="63821"/>
          </measurement>
          <measurement>
            <compressorPower unit="kW" value="15905"/>
            <fuelConsumption unit="kW" value="50991"/>
          </measurement>
          <measurement>
            <compressorPower unit="kW" value="10604"/>
            <fuelConsumption unit="kW" value="38160"/>
          </measurement>
          <measurement>
            <compressorPower unit="kW" value="5302"/>
            <fuelConsumption unit="kW" value="25330"/>
          </measurement>
        </specificEnergyConsumptionMeasurements>
        <maximalPowerMeasurements>
          <ambientTemperature unit="Celsius" value="-5">
            <measurement>
              <speed unit="per_min" value="3000"/>
              <maximalPower unit="kW" value="20310"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3500"/>
              <maximalPower unit="kW" value="22132"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4000"/>
              <maximalPower unit="kW" value="23518"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4500"/>
              <maximalPower unit="kW" value="24473"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4950"/>
              <maximalPower unit="kW" value="24966"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5200"/>
              <maximalPower unit="kW" value="25091"/>
            </measurement>
          </ambientTemperature>
          <ambientTemperature unit="Celsius" value="5">
            <measurement>
              <speed unit="per_min" value="3000"/>
              <maximalPower unit="kW" value="19094"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3500"/>
              <maximalPower unit="kW" value="20807"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4000"/>
              <maximalPower unit="kW" value="22110"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4500"/>
              <maximalPower unit="kW" value="23008"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4950"/>
              <maximalPower unit="kW" value="23471"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5200"/>
              <maximalPower unit="kW" value="23589"/>
            </measurement>
          </ambientTemperature>
          <ambientTemperature unit="Celsius" value="15">
            <measurement>
              <speed unit="per_min" value="3000"/>
              <maximalPower unit="kW" value="17907"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3500"/>
              <maximalPower unit="kW" value="19513"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4000"/>
              <maximalPower unit="kW" value="20736"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4500"/>
              <maximalPower unit="kW" value="21577"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4950"/>
              <maximalPower unit="kW" value="22012"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5200"/>
              <maximalPower unit="kW" value="22122"/>
            </measurement>
          </ambientTemperature>
          <ambientTemperature unit="Celsius" value="25">
            <measurement>
              <speed unit="per_min" value="3000"/>
              <maximalPower unit="kW" value="16748"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3500"/>
              <maximalPower unit="kW" value="18251"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4000"/>
              <maximalPower unit="kW" value="19394"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4500"/>
              <maximalPower unit="kW" value="20181"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4950"/>
              <maximalPower unit="kW" value="20588"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5200"/>
              <maximalPower unit="kW" value="20691"/>
            </measurement>
          </ambientTemperature>
        </maximalPowerMeasurements>
      </gasTurbine>
      <gasTurbine id="drive_8">
        <energy_rate_fun_coeff_1 value="0.01"/>
        <energy_rate_fun_coeff_2 value="0"/>
        <energy_rate_fun_coeff_3 value="0"/>
        <power_fun_coeff_1 value="-1224.325324586845"/>
        <power_fun_coeff_2 value="3.778795049244455"/>
        <power_fun_coeff_3 value="-0.0002183150754438895"/>
        <power_fun_coeff_4 value="7.365051411747453"/>
        <power_fun_coeff_5 value="-0.02273171946478677"/>
        <power_fun_coeff_6 value="1.313296165907836e-06"/>
        <power_fun_coeff_7 value="-0.02447899107067507"/>
        <power_fun_coeff_8 value="7.55527051599469e-05"/>
        <power_fun_coeff_9 value="-4.364961399608499e-09"/>
      </gasTurbine>
    </drives>
    <configurations>
      <configuration nrOfSerialStages="1" confId="config_1">
        <stage nrOfParallelUnits="2" stageNr="1">
          <compressor nominalSpeed="6700" id="compressor_3"/>
          <compressor nominalSpeed="6700" id="compressor_4"/>
        </stage>
      </configuration>
      <configuration nrOfSerialStages="1" confId="config_2">
        <stage nrOfParallelUnits="2" stageNr="1">
          <compressor nominalSpeed="3000" id="compressor_6"/>
          <compressor nominalSpeed="3000" id="compressor_7"/>
        </stage>
      </configuration>
      <configuration nrOfSerialStages="2" confId="config_3">
        <stage nrOfParallelUnits="1" stageNr="1">
          <compressor nominalSpeed="6700" id="compressor_3"/>
        </stage>
        <stage nrOfParallelUnits="1" stageNr="2">
          <compressor nominalSpeed="6700" id="compressor_4"/>
        </stage>
      </configuration>
      <configuration nrOfSerialStages="2" confId="config_4">
        <stage nrOfParallelUnits="1" stageNr="1">
          <compressor nominalSpeed="3600" id="compressor_8"/>
        </stage>
        <stage nrOfParallelUnits="1" stageNr="2">
          <compressor nominalSpeed="3600" id="compressor_5"/>
        </stage>
      </configuration>
      <configuration nrOfSerialStages="2" confId="config_5">
        <stage nrOfParallelUnits="1" stageNr="1">
          <compressor nominalSpeed="3000" id="compressor_6"/>
        </stage>
        <stage nrOfParallelUnits="1" stageNr="2">
          <compressor nominalSpeed="3000" id="compressor_7"/>
        </stage>
      </configuration>
      <configuration nrOfSerialStages="1" confId="config_6">
        <stage nrOfParallelUnits="1" stageNr="1">
          <compressor nominalSpeed="6700" id="compressor_3"/>
        </stage>
      </configuration>
      <configuration nrOfSerialStages="1" confId="config_7">
        <stage nrOfParallelUnits="1" stageNr="1">
          <compressor nominalSpeed="6700" id="compressor_4"/>
        </stage>
      </configuration>
      <configuration nrOfSerialStages="1" confId="config_8">
        <stage nrOfParallelUnits="1" stageNr="1">
          <compressor nominalSpeed="3600" id="compressor_8"/>
        </stage>
      </configuration>
      <configuration nrOfSerialStages="1" confId="config_9">
        <stage nrOfParallelUnits="1" stageNr="1">
          <compressor nominalSpeed="4000" id="compressor_5"/>
        </stage>
      </configuration>
      <configuration nrOfSerialStages="1" confId="config_10">
        <stage nrOfParallelUnits="1" stageNr="1">
          <compressor nominalSpeed="3000" id="compressor_6"/>
        </stage>
      </configuration>
      <configuration nrOfSerialStages="1" confId="config_11">
        <stage nrOfParallelUnits="1" stageNr="1">
          <compressor nominalSpeed="3000" id="compressor_7"/>
        </stage>
      </configuration>
    </configurations>
  </compressorStation>
  <compressorStation id="compressorStation_11">
    <compressors>
      <turboCompressor drive="drive_9" id="compressor_9">
        <speedMin unit="per_min" value="3000"/>
        <speedMax unit="per_min" value="5200"/>
        <n_isoline_coeff_1 value="5.02769433304"/>
        <n_isoline_coeff_2 value="-0.00196303753897"/>
        <n_isoline_coeff_3 value="8.13640064744e-07"/>
        <n_isoline_coeff_4 value="-2.20002977754"/>
        <n_isoline_coeff_5 value="0.0022881598892"/>
        <n_isoline_coeff_6 value="-8.09515969199e-08"/>
        <n_isoline_coeff_7 value="-0.4525391719"/>
        <n_isoline_coeff_8 value="-9.25135592924e-05"/>
        <n_isoline_coeff_9 value="9.08503017003e-09"/>
        <eta_ad_isoline_coeff_1 value="2.02254252508"/>
        <eta_ad_isoline_coeff_2 value="-0.000939798739175"/>
        <eta_ad_isoline_coeff_3 value="9.32298613097e-08"/>
        <eta_ad_isoline_coeff_4 value="0.00385693263099"/>
        <eta_ad_isoline_coeff_5 value="0.000206116855887"/>
        <eta_ad_isoline_coeff_6 value="-2.84132796926e-08"/>
        <eta_ad_isoline_coeff_7 value="-0.0747202392876"/>
        <eta_ad_isoline_coeff_8 value="1.09495919291e-05"/>
        <eta_ad_isoline_coeff_9 value="-8.43401216087e-11"/>
        <surgeline_coeff_1 value="-1.61612072451"/>
        <surgeline_coeff_2 value="0.617053179632"/>
        <surgeline_coeff_3 value="1.47956473424"/>
        <chokeline_coeff_1 value="-10.8609430571"/>
        <chokeline_coeff_2 value="2.51788790407"/>
        <chokeline_coeff_3 value="0.0335192983867"/>
        <efficiencyOfChokeline value="0.67"/>
        <surgelineMeasurements>
          <measurement>
            <speed unit="per_min" value="3000"/>
            <adiabaticHead unit="kJ_per_kg" value="12.8"/>
            <volumetricFlowrate unit="m_cube_per_s" value="2.92"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="3500"/>
            <adiabaticHead unit="kJ_per_kg" value="17.5"/>
            <volumetricFlowrate unit="m_cube_per_s" value="3.39"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="4000"/>
            <adiabaticHead unit="kJ_per_kg" value="23"/>
            <volumetricFlowrate unit="m_cube_per_s" value="3.88"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="4500"/>
            <adiabaticHead unit="kJ_per_kg" value="29.1"/>
            <volumetricFlowrate unit="m_cube_per_s" value="4.35"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="5000"/>
            <adiabaticHead unit="kJ_per_kg" value="35.9"/>
            <volumetricFlowrate unit="m_cube_per_s" value="4.83"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="5200"/>
            <adiabaticHead unit="kJ_per_kg" value="38.9"/>
            <volumetricFlowrate unit="m_cube_per_s" value="5.03"/>
          </measurement>
        </surgelineMeasurements>
        <characteristicDiagramMeasurements>
          <adiabaticEfficiency value="0.8">
            <measurement>
              <speed unit="per_min" value="3000"/>
              <adiabaticHead unit="kJ_per_kg" value="12.3"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.53"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3500"/>
              <adiabaticHead unit="kJ_per_kg" value="16.7"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.14"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4000"/>
              <adiabaticHead unit="kJ_per_kg" value="21.9"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.75"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4500"/>
              <adiabaticHead unit="kJ_per_kg" value="27.7"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.33"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5000"/>
              <adiabaticHead unit="kJ_per_kg" value="34.3"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.91"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5200"/>
              <adiabaticHead unit="kJ_per_kg" value="37.1"/>
              <volumetricFlowrate unit="m_cube_per_s" value="6.1"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.83">
            <measurement>
              <speed unit="per_min" value="3000"/>
              <adiabaticHead unit="kJ_per_kg" value="11.5"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.22"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3500"/>
              <adiabaticHead unit="kJ_per_kg" value="15.6"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.89"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4000"/>
              <adiabaticHead unit="kJ_per_kg" value="20.5"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.58"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4500"/>
              <adiabaticHead unit="kJ_per_kg" value="26.1"/>
              <volumetricFlowrate unit="m_cube_per_s" value="6.27"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5000"/>
              <adiabaticHead unit="kJ_per_kg" value="32.2"/>
              <volumetricFlowrate unit="m_cube_per_s" value="6.97"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5200"/>
              <adiabaticHead unit="kJ_per_kg" value="34.8"/>
              <volumetricFlowrate unit="m_cube_per_s" value="7.28"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.81">
            <measurement>
              <speed unit="per_min" value="3000"/>
              <adiabaticHead unit="kJ_per_kg" value="9.6"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.13"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3500"/>
              <adiabaticHead unit="kJ_per_kg" value="13.3"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.99"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4000"/>
              <adiabaticHead unit="kJ_per_kg" value="17.3"/>
              <volumetricFlowrate unit="m_cube_per_s" value="6.84"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4500"/>
              <adiabaticHead unit="kJ_per_kg" value="21.9"/>
              <volumetricFlowrate unit="m_cube_per_s" value="7.7"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5000"/>
              <adiabaticHead unit="kJ_per_kg" value="27.2"/>
              <volumetricFlowrate unit="m_cube_per_s" value="8.53"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5200"/>
              <adiabaticHead unit="kJ_per_kg" value="29.4"/>
              <volumetricFlowrate unit="m_cube_per_s" value="8.9"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.67">
            <measurement>
              <speed unit="per_min" value="3000"/>
              <adiabaticHead unit="kJ_per_kg" value="6.4"/>
              <volumetricFlowrate unit="m_cube_per_s" value="6.09"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3500"/>
              <adiabaticHead unit="kJ_per_kg" value="8.7"/>
              <volumetricFlowrate unit="m_cube_per_s" value="7.1"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4000"/>
              <adiabaticHead unit="kJ_per_kg" value="11.6"/>
              <volumetricFlowrate unit="m_cube_per_s" value="8.1"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4500"/>
              <adiabaticHead unit="kJ_per_kg" value="14.6"/>
              <volumetricFlowrate unit="m_cube_per_s" value="9.11"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5000"/>
              <adiabaticHead unit="kJ_per_kg" value="18.1"/>
              <volumetricFlowrate unit="m_cube_per_s" value="10.12"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5200"/>
              <adiabaticHead unit="kJ_per_kg" value="19.6"/>
              <volumetricFlowrate unit="m_cube_per_s" value="10.52"/>
            </measurement>
          </adiabaticEfficiency>
        </characteristicDiagramMeasurements>
      </turboCompressor>
      <turboCompressor drive="drive_10" id="compressor_10">
        <speedMin unit="per_min" value="3000"/>
        <speedMax unit="per_min" value="5200"/>
        <n_isoline_coeff_1 value="-39.9456823809"/>
        <n_isoline_coeff_2 value="0.0246738050993"/>
        <n_isoline_coeff_3 value="-2.76883540961e-06"/>
        <n_isoline_coeff_4 value="15.1681303513"/>
        <n_isoline_coeff_5 value="-0.00709950574929"/>
        <n_isoline_coeff_6 value="1.56992669157e-06"/>
        <n_isoline_coeff_7 value="-3.91022154979"/>
        <n_isoline_coeff_8 value="0.000976093074964"/>
        <n_isoline_coeff_9 value="-1.59311964518e-07"/>
        <eta_ad_isoline_coeff_1 value="0.111199827707"/>
        <eta_ad_isoline_coeff_2 value="0.000214135576548"/>
        <eta_ad_isoline_coeff_3 value="-5.12905364067e-08"/>
        <eta_ad_isoline_coeff_4 value="0.636940651964"/>
        <eta_ad_isoline_coeff_5 value="-0.000104959862993"/>
        <eta_ad_isoline_coeff_6 value="1.38759596858e-08"/>
        <eta_ad_isoline_coeff_7 value="-0.266566283872"/>
        <eta_ad_isoline_coeff_8 value="7.21194020588e-05"/>
        <eta_ad_isoline_coeff_9 value="-6.17300972133e-09"/>
        <surgeline_coeff_1 value="-114.910089687"/>
        <surgeline_coeff_2 value="120.028453177"/>
        <surgeline_coeff_3 value="-21.8914654129"/>
        <chokeline_coeff_1 value="-15.2091645927"/>
        <chokeline_coeff_2 value="6.49119036036"/>
        <chokeline_coeff_3 value="0.227393859323"/>
        <efficiencyOfChokeline value="0.6"/>
        <surgelineMeasurements>
          <measurement>
            <speed unit="per_min" value="3000"/>
            <adiabaticHead unit="kJ_per_kg" value="16.1"/>
            <volumetricFlowrate unit="m_cube_per_s" value="1.52"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="3500"/>
            <adiabaticHead unit="kJ_per_kg" value="22.2"/>
            <volumetricFlowrate unit="m_cube_per_s" value="1.62"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="4000"/>
            <adiabaticHead unit="kJ_per_kg" value="29.3"/>
            <volumetricFlowrate unit="m_cube_per_s" value="1.74"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="4500"/>
            <adiabaticHead unit="kJ_per_kg" value="36.8"/>
            <volumetricFlowrate unit="m_cube_per_s" value="2"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="5000"/>
            <adiabaticHead unit="kJ_per_kg" value="45.3"/>
            <volumetricFlowrate unit="m_cube_per_s" value="2.34"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="5200"/>
            <adiabaticHead unit="kJ_per_kg" value="48.9"/>
            <volumetricFlowrate unit="m_cube_per_s" value="2.49"/>
          </measurement>
        </surgelineMeasurements>
        <characteristicDiagramMeasurements>
          <adiabaticEfficiency value="0.74">
            <measurement>
              <speed unit="per_min" value="3000"/>
              <adiabaticHead unit="kJ_per_kg" value="15.9"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.66"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3500"/>
              <adiabaticHead unit="kJ_per_kg" value="22"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.77"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4000"/>
              <adiabaticHead unit="kJ_per_kg" value="28.7"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.12"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4500"/>
              <adiabaticHead unit="kJ_per_kg" value="35.9"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.64"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5000"/>
              <adiabaticHead unit="kJ_per_kg" value="44.2"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.97"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5200"/>
              <adiabaticHead unit="kJ_per_kg" value="47.8"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.08"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.75">
            <measurement>
              <speed unit="per_min" value="3000"/>
              <adiabaticHead unit="kJ_per_kg" value="15.6"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.83"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3500"/>
              <adiabaticHead unit="kJ_per_kg" value="21.8"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.92"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4000"/>
              <adiabaticHead unit="kJ_per_kg" value="28.3"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.33"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4500"/>
              <adiabaticHead unit="kJ_per_kg" value="35.3"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.94"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5000"/>
              <adiabaticHead unit="kJ_per_kg" value="43.5"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.29"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5200"/>
              <adiabaticHead unit="kJ_per_kg" value="47"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.42"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.76">
            <measurement>
              <speed unit="per_min" value="3000"/>
              <adiabaticHead unit="kJ_per_kg" value="14.8"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.25"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3500"/>
              <adiabaticHead unit="kJ_per_kg" value="21.2"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.23"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4000"/>
              <adiabaticHead unit="kJ_per_kg" value="27.4"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.71"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4500"/>
              <adiabaticHead unit="kJ_per_kg" value="33.7"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.56"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5000"/>
              <adiabaticHead unit="kJ_per_kg" value="41.5"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.96"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5200"/>
              <adiabaticHead unit="kJ_per_kg" value="44.9"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.12"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.76">
            <measurement>
              <speed unit="per_min" value="3000"/>
              <adiabaticHead unit="kJ_per_kg" value="14.8"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.25"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3500"/>
              <adiabaticHead unit="kJ_per_kg" value="20"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.71"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4000"/>
              <adiabaticHead unit="kJ_per_kg" value="25.9"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.2"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4500"/>
              <adiabaticHead unit="kJ_per_kg" value="33.7"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.56"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5000"/>
              <adiabaticHead unit="kJ_per_kg" value="41.5"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.96"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5200"/>
              <adiabaticHead unit="kJ_per_kg" value="44.9"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.12"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.75">
            <measurement>
              <speed unit="per_min" value="3000"/>
              <adiabaticHead unit="kJ_per_kg" value="13.8"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.58"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3500"/>
              <adiabaticHead unit="kJ_per_kg" value="18.9"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.99"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4000"/>
              <adiabaticHead unit="kJ_per_kg" value="24.8"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.49"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4500"/>
              <adiabaticHead unit="kJ_per_kg" value="31.7"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5000"/>
              <adiabaticHead unit="kJ_per_kg" value="39.1"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.45"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5200"/>
              <adiabaticHead unit="kJ_per_kg" value="42.3"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.62"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.73">
            <measurement>
              <speed unit="per_min" value="3000"/>
              <adiabaticHead unit="kJ_per_kg" value="13.1"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.77"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3500"/>
              <adiabaticHead unit="kJ_per_kg" value="17.8"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.23"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4000"/>
              <adiabaticHead unit="kJ_per_kg" value="23.4"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.74"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4500"/>
              <adiabaticHead unit="kJ_per_kg" value="29.9"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.26"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5000"/>
              <adiabaticHead unit="kJ_per_kg" value="36.9"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.73"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5200"/>
              <adiabaticHead unit="kJ_per_kg" value="39.9"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.92"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.68">
            <measurement>
              <speed unit="per_min" value="3000"/>
              <adiabaticHead unit="kJ_per_kg" value="11.6"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.02"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3500"/>
              <adiabaticHead unit="kJ_per_kg" value="15.8"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.53"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4000"/>
              <adiabaticHead unit="kJ_per_kg" value="20.9"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.06"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4500"/>
              <adiabaticHead unit="kJ_per_kg" value="26.6"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.58"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5000"/>
              <adiabaticHead unit="kJ_per_kg" value="32.9"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.09"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5200"/>
              <adiabaticHead unit="kJ_per_kg" value="35.5"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.3"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.6">
            <measurement>
              <speed unit="per_min" value="3000"/>
              <adiabaticHead unit="kJ_per_kg" value="9.8"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.24"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3500"/>
              <adiabaticHead unit="kJ_per_kg" value="13.5"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.78"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4000"/>
              <adiabaticHead unit="kJ_per_kg" value="17.5"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.34"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4500"/>
              <adiabaticHead unit="kJ_per_kg" value="22.2"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.88"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5000"/>
              <adiabaticHead unit="kJ_per_kg" value="27.5"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.42"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5200"/>
              <adiabaticHead unit="kJ_per_kg" value="29.7"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.64"/>
            </measurement>
          </adiabaticEfficiency>
        </characteristicDiagramMeasurements>
      </turboCompressor>
      <turboCompressor drive="drive_11" id="compressor_11">
        <speedMin unit="per_min" value="3900"/>
        <speedMax unit="per_min" value="6825"/>
        <n_isoline_coeff_1 value="0"/>
        <n_isoline_coeff_2 value="0.008190328205128205"/>
        <n_isoline_coeff_3 value="0"/>
        <n_isoline_coeff_4 value="0"/>
        <n_isoline_coeff_5 value="0"/>
        <n_isoline_coeff_6 value="0"/>
        <n_isoline_coeff_7 value="-1.013172884004266"/>
        <n_isoline_coeff_8 value="3.711255985363611e-05"/>
        <n_isoline_coeff_9 value="0"/>
        <eta_ad_isoline_coeff_1 value="0.8565207961827774"/>
        <eta_ad_isoline_coeff_2 value="-1.632443947781463e-05"/>
        <eta_ad_isoline_coeff_3 value="1.102221635130854e-09"/>
        <eta_ad_isoline_coeff_4 value="0.0234419497697267"/>
        <eta_ad_isoline_coeff_5 value="7.96434097571202e-06"/>
        <eta_ad_isoline_coeff_6 value="-8.84822435182007e-10"/>
        <eta_ad_isoline_coeff_7 value="-0.02439376964914182"/>
        <eta_ad_isoline_coeff_8 value="3.87637621646916e-06"/>
        <eta_ad_isoline_coeff_9 value="-1.859749731845474e-10"/>
        <surgeline_coeff_1 value="8.165245324999994"/>
        <surgeline_coeff_2 value="63.69921410107973"/>
        <surgeline_coeff_3 value="0"/>
        <chokeline_coeff_1 value="-1.252989172205185"/>
        <chokeline_coeff_2 value="2.050100524005114"/>
        <chokeline_coeff_3 value="0"/>
        <efficiencyOfChokeline value="0.7"/>
        <surgelineMeasurements>
          <measurement>
            <speed unit="per_min" value="3900"/>
            <adiabaticHead unit="kJ_per_kg" value="31.82249644999989"/>
            <volumetricFlowrate unit="m_cube_per_s" value="0.3713899999999984"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="4265.625"/>
            <adiabaticHead unit="kJ_per_kg" value="34.78754790944053"/>
            <volumetricFlowrate unit="m_cube_per_s" value="0.4179376929548222"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="4631.25"/>
            <adiabaticHead unit="kJ_per_kg" value="37.74998292874456"/>
            <volumetricFlowrate unit="m_cube_per_s" value="0.4644443109894365"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="4996.875"/>
            <adiabaticHead unit="kJ_per_kg" value="40.70998342851848"/>
            <volumetricFlowrate unit="m_cube_per_s" value="0.5109127100355676"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="5362.5"/>
            <adiabaticHead unit="kJ_per_kg" value="43.66773001254455"/>
            <volumetricFlowrate unit="m_cube_per_s" value="0.5573457253524072"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="5728.125"/>
            <adiabaticHead unit="kJ_per_kg" value="46.62340204703219"/>
            <volumetricFlowrate unit="m_cube_per_s" value="0.6037461727707615"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="6093.75"/>
            <adiabaticHead unit="kJ_per_kg" value="49.57717773837673"/>
            <volumetricFlowrate unit="m_cube_per_s" value="0.6501168499137698"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="6459.375"/>
            <adiabaticHead unit="kJ_per_kg" value="52.52923420951927"/>
            <volumetricFlowrate unit="m_cube_per_s" value="0.6964605373956615"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="6825"/>
            <adiabaticHead unit="kJ_per_kg" value="55.47974757500009"/>
            <volumetricFlowrate unit="m_cube_per_s" value="0.7427800000000017"/>
          </measurement>
        </surgelineMeasurements>
        <characteristicDiagramMeasurements>
          <adiabaticEfficiency value="0.8325">
            <measurement>
              <speed unit="per_min" value="3900"/>
              <adiabaticHead unit="kJ_per_kg" value="31.17457354113589"/>
              <volumetricFlowrate unit="m_cube_per_s" value="0.9402194109274092"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4265.625"/>
              <adiabaticHead unit="kJ_per_kg" value="34.02070516418974"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.035232365041772"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4631.25"/>
              <adiabaticHead unit="kJ_per_kg" value="36.85734359778332"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.129928406204084"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4996.875"/>
              <adiabaticHead unit="kJ_per_kg" value="39.68528952765844"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.224334263858981"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5362.5"/>
              <adiabaticHead unit="kJ_per_kg" value="42.50532208982526"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.318475948052304"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5728.125"/>
              <adiabaticHead unit="kJ_per_kg" value="45.31820067133337"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.41237880954658"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6093.75"/>
              <adiabaticHead unit="kJ_per_kg" value="48.12466659867167"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.506067596185198"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6459.375"/>
              <adiabaticHead unit="kJ_per_kg" value="50.92544472515367"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.599566505884397"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6825"/>
              <adiabaticHead unit="kJ_per_kg" value="53.72124492753953"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.69289923659528"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.835">
            <measurement>
              <speed unit="per_min" value="3900"/>
              <adiabaticHead unit="kJ_per_kg" value="29.79587993515397"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.572124559284826"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4265.625"/>
              <adiabaticHead unit="kJ_per_kg" value="32.41850780811955"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.71636763113406"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4631.25"/>
              <adiabaticHead unit="kJ_per_kg" value="35.02225124312676"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.859572069416809"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4996.875"/>
              <adiabaticHead unit="kJ_per_kg" value="37.60903479765409"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.001843723722146"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5362.5"/>
              <adiabaticHead unit="kJ_per_kg" value="40.18067554732781"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.143282532197157"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5728.125"/>
              <adiabaticHead unit="kJ_per_kg" value="42.73889556384456"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.283983207825726"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6093.75"/>
              <adiabaticHead unit="kJ_per_kg" value="45.28533294968581"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.424035845331685"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6459.375"/>
              <adiabaticHead unit="kJ_per_kg" value="47.82155164925435"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.563526460785858"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6825"/>
              <adiabaticHead unit="kJ_per_kg" value="50.34905021964441"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.702537473993524"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.8374999999999999">
            <measurement>
              <speed unit="per_min" value="3900"/>
              <adiabaticHead unit="kJ_per_kg" value="27.58990849293718"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.238693277024947"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4265.625"/>
              <adiabaticHead unit="kJ_per_kg" value="29.89743703963236"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.427963257581978"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4631.25"/>
              <adiabaticHead unit="kJ_per_kg" value="32.17829120965821"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.61504533075177"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4996.875"/>
              <adiabaticHead unit="kJ_per_kg" value="34.43571933474513"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.800205933837706"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5362.5"/>
              <adiabaticHead unit="kJ_per_kg" value="36.67268840609167"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.983688427801568"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5728.125"/>
              <adiabaticHead unit="kJ_per_kg" value="38.89192670256772"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.165716593748641"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6093.75"/>
              <adiabaticHead unit="kJ_per_kg" value="41.09595934511775"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.346497549199853"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6459.375"/>
              <adiabaticHead unit="kJ_per_kg" value="43.28713822174021"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.526224202622743"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6825"/>
              <adiabaticHead unit="kJ_per_kg" value="45.46766739836958"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.705077337703456"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.84">
            <measurement>
              <speed unit="per_min" value="3900"/>
              <adiabaticHead unit="kJ_per_kg" value="24.61579440842311"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.904554071173914"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4265.625"/>
              <adiabaticHead unit="kJ_per_kg" value="26.55592135527401"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.131106829060222"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4631.25"/>
              <adiabaticHead unit="kJ_per_kg" value="28.46636732997388"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.354193676579956"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4996.875"/>
              <adiabaticHead unit="kJ_per_kg" value="30.35131457057943"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.574302982583114"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5362.5"/>
              <adiabaticHead unit="kJ_per_kg" value="32.21447413662884"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.791868095400028"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5728.125"/>
              <adiabaticHead unit="kJ_per_kg" value="34.05917187403788"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.007277381145478"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6093.75"/>
              <adiabaticHead unit="kJ_per_kg" value="35.88841666470861"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.220882193370927"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6459.375"/>
              <adiabaticHead unit="kJ_per_kg" value="37.70495533499214"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.433003284842726"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6825"/>
              <adiabaticHead unit="kJ_per_kg" value="39.51131738960131"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.643936031216428"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.8049999999999999">
            <measurement>
              <speed unit="per_min" value="3900"/>
              <adiabaticHead unit="kJ_per_kg" value="21.06627621261998"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.538883703370827"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4265.625"/>
              <adiabaticHead unit="kJ_per_kg" value="22.6309295591454"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.79409945075786"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4631.25"/>
              <adiabaticHead unit="kJ_per_kg" value="24.16772227849773"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.044770759721874"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4996.875"/>
              <adiabaticHead unit="kJ_per_kg" value="25.68103798468616"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.2916126559445"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5362.5"/>
              <adiabaticHead unit="kJ_per_kg" value="27.17468473264971"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.535246283776665"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5728.125"/>
              <adiabaticHead unit="kJ_per_kg" value="28.65201328552916"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.776218197201838"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6093.75"/>
              <adiabaticHead unit="kJ_per_kg" value="30.11600767853551"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.015015132006124"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6459.375"/>
              <adiabaticHead unit="kJ_per_kg" value="31.56935575932658"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.252075511850825"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6825"/>
              <adiabaticHead unit="kJ_per_kg" value="33.01450500905391"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.48779855342678"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.77">
            <measurement>
              <speed unit="per_min" value="3900"/>
              <adiabaticHead unit="kJ_per_kg" value="17.18394369222466"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.122401781388286"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4265.625"/>
              <adiabaticHead unit="kJ_per_kg" value="18.39600638047624"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.398761366579075"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4631.25"/>
              <adiabaticHead unit="kJ_per_kg" value="19.58493678210232"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.669846613075752"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4996.875"/>
              <adiabaticHead unit="kJ_per_kg" value="20.75468596026812"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.936558393570777"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5362.5"/>
              <adiabaticHead unit="kJ_per_kg" value="21.90864006981779"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.199668777328553"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5728.125"/>
              <adiabaticHead unit="kJ_per_kg" value="23.04974517636235"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.459849489894378"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6093.75"/>
              <adiabaticHead unit="kJ_per_kg" value="24.18060059539858"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.717693195129153"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6459.375"/>
              <adiabaticHead unit="kJ_per_kg" value="25.30353009200867"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.973729729286745"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6825"/>
              <adiabaticHead unit="kJ_per_kg" value="26.42063719573598"/>
              <volumetricFlowrate unit="m_cube_per_s" value="6.228438713229729"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.735">
            <measurement>
              <speed unit="per_min" value="3900"/>
              <adiabaticHead unit="kJ_per_kg" value="13.18591835917382"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.647355708804695"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4265.625"/>
              <adiabaticHead unit="kJ_per_kg" value="14.08257291674014"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.939114486876981"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4631.25"/>
              <adiabaticHead unit="kJ_per_kg" value="14.96179678520462"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.225201563946472"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4996.875"/>
              <adiabaticHead unit="kJ_per_kg" value="15.82676062597387"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.506648628627099"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5362.5"/>
              <adiabaticHead unit="kJ_per_kg" value="16.6801613978112"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.784333233357155"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5728.125"/>
              <adiabaticHead unit="kJ_per_kg" value="17.52433163667152"/>
              <volumetricFlowrate unit="m_cube_per_s" value="6.059014352520107"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6093.75"/>
              <adiabaticHead unit="kJ_per_kg" value="18.36132001780268"/>
              <volumetricFlowrate unit="m_cube_per_s" value="6.331358596218958"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6459.375"/>
              <adiabaticHead unit="kJ_per_kg" value="19.19295205670621"/>
              <volumetricFlowrate unit="m_cube_per_s" value="6.601959961514883"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6825"/>
              <adiabaticHead unit="kJ_per_kg" value="20.02087676944344"/>
              <volumetricFlowrate unit="m_cube_per_s" value="6.87135501503436"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.7">
            <measurement>
              <speed unit="per_min" value="3900"/>
              <adiabaticHead unit="kJ_per_kg" value="9.231019897504565"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.113899999999999"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4265.625"/>
              <adiabaticHead unit="kJ_per_kg" value="9.852298587996579"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.416947915561853"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4631.25"/>
              <adiabaticHead unit="kJ_per_kg" value="10.46164569659539"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.714175832663392"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4996.875"/>
              <adiabaticHead unit="kJ_per_kg" value="11.06134486945818"/>
              <volumetricFlowrate unit="m_cube_per_s" value="6.006697670417577"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5362.5"/>
              <adiabaticHead unit="kJ_per_kg" value="11.65333198976559"/>
              <volumetricFlowrate unit="m_cube_per_s" value="6.295457715779104"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5728.125"/>
              <adiabaticHead unit="kJ_per_kg" value="12.23927744258123"/>
              <volumetricFlowrate unit="m_cube_per_s" value="6.581270750776492"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6093.75"/>
              <adiabaticHead unit="kJ_per_kg" value="12.8206462919923"/>
              <volumetricFlowrate unit="m_cube_per_s" value="6.864851405775448"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6459.375"/>
              <adiabaticHead unit="kJ_per_kg" value="13.39874332694255"/>
              <volumetricFlowrate unit="m_cube_per_s" value="7.146836131978465"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6825"/>
              <adiabaticHead unit="kJ_per_kg" value="13.9747475"/>
              <volumetricFlowrate unit="m_cube_per_s" value="7.4278"/>
            </measurement>
          </adiabaticEfficiency>
        </characteristicDiagramMeasurements>
      </turboCompressor>
    </compressors>
    <drives>
      <gasTurbine id="drive_9">
        <energy_rate_fun_coeff_1 value="10904.812076"/>
        <energy_rate_fun_coeff_2 value="2.84801332486"/>
        <energy_rate_fun_coeff_3 value="1.53960565698e-07"/>
        <power_fun_coeff_1 value="3491.14689732"/>
        <power_fun_coeff_2 value="3.12187252252"/>
        <power_fun_coeff_3 value="-0.000309742612964"/>
        <power_fun_coeff_4 value="-25.0368009734"/>
        <power_fun_coeff_5 value="-0.0222903875746"/>
        <power_fun_coeff_6 value="2.21108336325e-06"/>
        <power_fun_coeff_7 value="0.0022138668369"/>
        <power_fun_coeff_8 value="-9.7455153523e-07"/>
        <power_fun_coeff_9 value="9.93005412177e-11"/>
        <specificEnergyConsumptionMeasurements>
          <measurement>
            <compressorPower unit="kW" value="10001"/>
            <fuelConsumption unit="kW" value="39403"/>
          </measurement>
          <measurement>
            <compressorPower unit="kW" value="7501"/>
            <fuelConsumption unit="kW" value="32277"/>
          </measurement>
          <measurement>
            <compressorPower unit="kW" value="5001"/>
            <fuelConsumption unit="kW" value="25151"/>
          </measurement>
          <measurement>
            <compressorPower unit="kW" value="2500"/>
            <fuelConsumption unit="kW" value="18026"/>
          </measurement>
        </specificEnergyConsumptionMeasurements>
        <maximalPowerMeasurements>
          <ambientTemperature unit="Celsius" value="-5">
            <measurement>
              <speed unit="per_min" value="2500"/>
              <maximalPower unit="kW" value="9660"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3000"/>
              <maximalPower unit="kW" value="10472"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3500"/>
              <maximalPower unit="kW" value="11035"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4000"/>
              <maximalPower unit="kW" value="11401"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4500"/>
              <maximalPower unit="kW" value="11622"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5000"/>
              <maximalPower unit="kW" value="11752"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5200"/>
              <maximalPower unit="kW" value="11790"/>
            </measurement>
          </ambientTemperature>
          <ambientTemperature unit="Celsius" value="5">
            <measurement>
              <speed unit="per_min" value="2500"/>
              <maximalPower unit="kW" value="8993"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3000"/>
              <maximalPower unit="kW" value="9749"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3500"/>
              <maximalPower unit="kW" value="10273"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4000"/>
              <maximalPower unit="kW" value="10614"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4500"/>
              <maximalPower unit="kW" value="10820"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5000"/>
              <maximalPower unit="kW" value="10941"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5200"/>
              <maximalPower unit="kW" value="10976"/>
            </measurement>
          </ambientTemperature>
          <ambientTemperature unit="Celsius" value="15">
            <measurement>
              <speed unit="per_min" value="2500"/>
              <maximalPower unit="kW" value="8326"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3000"/>
              <maximalPower unit="kW" value="9026"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3500"/>
              <maximalPower unit="kW" value="9511"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4000"/>
              <maximalPower unit="kW" value="9827"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4500"/>
              <maximalPower unit="kW" value="10017"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5000"/>
              <maximalPower unit="kW" value="10129"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5200"/>
              <maximalPower unit="kW" value="10162"/>
            </measurement>
          </ambientTemperature>
          <ambientTemperature unit="Celsius" value="25">
            <measurement>
              <speed unit="per_min" value="2500"/>
              <maximalPower unit="kW" value="7659"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3000"/>
              <maximalPower unit="kW" value="8303"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3500"/>
              <maximalPower unit="kW" value="8750"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4000"/>
              <maximalPower unit="kW" value="9039"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4500"/>
              <maximalPower unit="kW" value="9215"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5000"/>
              <maximalPower unit="kW" value="9318"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5200"/>
              <maximalPower unit="kW" value="9348"/>
            </measurement>
          </ambientTemperature>
        </maximalPowerMeasurements>
      </gasTurbine>
      <gasTurbine id="drive_10">
        <energy_rate_fun_coeff_1 value="10904.812076"/>
        <energy_rate_fun_coeff_2 value="2.84801332486"/>
        <energy_rate_fun_coeff_3 value="1.53960565698e-07"/>
        <power_fun_coeff_1 value="3491.14689732"/>
        <power_fun_coeff_2 value="3.12187252252"/>
        <power_fun_coeff_3 value="-0.000309742612964"/>
        <power_fun_coeff_4 value="-25.0368009734"/>
        <power_fun_coeff_5 value="-0.0222903875746"/>
        <power_fun_coeff_6 value="2.21108336325e-06"/>
        <power_fun_coeff_7 value="0.0022138668369"/>
        <power_fun_coeff_8 value="-9.7455153523e-07"/>
        <power_fun_coeff_9 value="9.93005412177e-11"/>
        <specificEnergyConsumptionMeasurements>
          <measurement>
            <compressorPower unit="kW" value="10001"/>
            <fuelConsumption unit="kW" value="39403"/>
          </measurement>
          <measurement>
            <compressorPower unit="kW" value="7501"/>
            <fuelConsumption unit="kW" value="32277"/>
          </measurement>
          <measurement>
            <compressorPower unit="kW" value="5001"/>
            <fuelConsumption unit="kW" value="25151"/>
          </measurement>
          <measurement>
            <compressorPower unit="kW" value="2500"/>
            <fuelConsumption unit="kW" value="18026"/>
          </measurement>
        </specificEnergyConsumptionMeasurements>
        <maximalPowerMeasurements>
          <ambientTemperature unit="Celsius" value="-5">
            <measurement>
              <speed unit="per_min" value="2500"/>
              <maximalPower unit="kW" value="9660"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3000"/>
              <maximalPower unit="kW" value="10472"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3500"/>
              <maximalPower unit="kW" value="11035"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4000"/>
              <maximalPower unit="kW" value="11401"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4500"/>
              <maximalPower unit="kW" value="11622"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5000"/>
              <maximalPower unit="kW" value="11752"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5200"/>
              <maximalPower unit="kW" value="11790"/>
            </measurement>
          </ambientTemperature>
          <ambientTemperature unit="Celsius" value="5">
            <measurement>
              <speed unit="per_min" value="2500"/>
              <maximalPower unit="kW" value="8993"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3000"/>
              <maximalPower unit="kW" value="9749"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3500"/>
              <maximalPower unit="kW" value="10273"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4000"/>
              <maximalPower unit="kW" value="10614"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4500"/>
              <maximalPower unit="kW" value="10820"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5000"/>
              <maximalPower unit="kW" value="10941"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5200"/>
              <maximalPower unit="kW" value="10976"/>
            </measurement>
          </ambientTemperature>
          <ambientTemperature unit="Celsius" value="15">
            <measurement>
              <speed unit="per_min" value="2500"/>
              <maximalPower unit="kW" value="8326"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3000"/>
              <maximalPower unit="kW" value="9026"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3500"/>
              <maximalPower unit="kW" value="9511"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4000"/>
              <maximalPower unit="kW" value="9827"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4500"/>
              <maximalPower unit="kW" value="10017"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5000"/>
              <maximalPower unit="kW" value="10129"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5200"/>
              <maximalPower unit="kW" value="10162"/>
            </measurement>
          </ambientTemperature>
          <ambientTemperature unit="Celsius" value="25">
            <measurement>
              <speed unit="per_min" value="2500"/>
              <maximalPower unit="kW" value="7659"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3000"/>
              <maximalPower unit="kW" value="8303"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3500"/>
              <maximalPower unit="kW" value="8750"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4000"/>
              <maximalPower unit="kW" value="9039"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4500"/>
              <maximalPower unit="kW" value="9215"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5000"/>
              <maximalPower unit="kW" value="9318"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5200"/>
              <maximalPower unit="kW" value="9348"/>
            </measurement>
          </ambientTemperature>
        </maximalPowerMeasurements>
      </gasTurbine>
      <gasTurbine id="drive_11">
        <energy_rate_fun_coeff_1 value="0.01"/>
        <energy_rate_fun_coeff_2 value="0"/>
        <energy_rate_fun_coeff_3 value="0"/>
        <power_fun_coeff_1 value="-1466.062009436941"/>
        <power_fun_coeff_2 value="4.524898531372921"/>
        <power_fun_coeff_3 value="-0.0002614202547053032"/>
        <power_fun_coeff_4 value="8.819242610991948"/>
        <power_fun_coeff_5 value="-0.0272199795652746"/>
        <power_fun_coeff_6 value="1.572599681891249e-06"/>
        <power_fun_coeff_7 value="-0.02931224088677029"/>
        <power_fun_coeff_8 value="9.047019490719649e-05"/>
        <power_fun_coeff_9 value="-5.226800387212604e-09"/>
      </gasTurbine>
    </drives>
    <configurations>
      <configuration nrOfSerialStages="2" confId="config_1">
        <stage nrOfParallelUnits="1" stageNr="1">
          <compressor nominalSpeed="3200" id="compressor_9"/>
        </stage>
        <stage nrOfParallelUnits="1" stageNr="2">
          <compressor nominalSpeed="3200" id="compressor_10"/>
        </stage>
      </configuration>
      <configuration nrOfSerialStages="2" confId="config_2">
        <stage nrOfParallelUnits="1" stageNr="1">
          <compressor nominalSpeed="3200" id="compressor_9"/>
        </stage>
        <stage nrOfParallelUnits="1" stageNr="2">
          <compressor nominalSpeed="3500" id="compressor_11"/>
        </stage>
      </configuration>
      <configuration nrOfSerialStages="2" confId="config_3">
        <stage nrOfParallelUnits="1" stageNr="1">
          <compressor nominalSpeed="3200" id="compressor_10"/>
        </stage>
        <stage nrOfParallelUnits="1" stageNr="2">
          <compressor nominalSpeed="3500" id="compressor_11"/>
        </stage>
      </configuration>
      <configuration nrOfSerialStages="1" confId="config_4">
        <stage nrOfParallelUnits="1" stageNr="1">
          <compressor nominalSpeed="3200" id="compressor_9"/>
        </stage>
      </configuration>
      <configuration nrOfSerialStages="1" confId="config_5">
        <stage nrOfParallelUnits="1" stageNr="1">
          <compressor nominalSpeed="3200" id="compressor_10"/>
        </stage>
      </configuration>
      <configuration nrOfSerialStages="1" confId="config_6">
        <stage nrOfParallelUnits="1" stageNr="1">
          <compressor nominalSpeed="3500" id="compressor_11"/>
        </stage>
      </configuration>
    </configurations>
  </compressorStation>
  <compressorStation id="compressorStation_10">
    <compressors>
      <turboCompressor drive="drive_12" id="compressor_12">
        <speedMin unit="per_min" value="3370"/>
        <speedMax unit="per_min" value="5775"/>
        <n_isoline_coeff_1 value="-12.926823548"/>
        <n_isoline_coeff_2 value="0.00526049469195"/>
        <n_isoline_coeff_3 value="8.56693512348e-07"/>
        <n_isoline_coeff_4 value="6.19428089556"/>
        <n_isoline_coeff_5 value="-0.00134607709935"/>
        <n_isoline_coeff_6 value="2.34618810294e-07"/>
        <n_isoline_coeff_7 value="-1.36099661945"/>
        <n_isoline_coeff_8 value="0.000335158430248"/>
        <n_isoline_coeff_9 value="-3.16642551875e-08"/>
        <eta_ad_isoline_coeff_1 value="0.951196728774"/>
        <eta_ad_isoline_coeff_2 value="-7.07545910472e-05"/>
        <eta_ad_isoline_coeff_3 value="-2.21661208991e-08"/>
        <eta_ad_isoline_coeff_4 value="0.00174937277474"/>
        <eta_ad_isoline_coeff_5 value="5.17254769162e-05"/>
        <eta_ad_isoline_coeff_6 value="-2.63028782851e-09"/>
        <eta_ad_isoline_coeff_7 value="-0.0168318554253"/>
        <eta_ad_isoline_coeff_8 value="9.99748549681e-07"/>
        <eta_ad_isoline_coeff_9 value="1.07005895367e-11"/>
        <surgeline_coeff_1 value="-26.320802796"/>
        <surgeline_coeff_2 value="10.628637298"/>
        <surgeline_coeff_3 value="-0.00743450655191"/>
        <chokeline_coeff_1 value="-29.6305121748"/>
        <chokeline_coeff_2 value="4.84063399411"/>
        <chokeline_coeff_3 value="0.174107148951"/>
        <efficiencyOfChokeline value="0.82"/>
        <surgelineMeasurements>
          <measurement>
            <speed unit="per_min" value="3370"/>
            <adiabaticHead unit="kJ_per_kg" value="21.9"/>
            <volumetricFlowrate unit="m_cube_per_s" value="4.55"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="3850"/>
            <adiabaticHead unit="kJ_per_kg" value="28.7"/>
            <volumetricFlowrate unit="m_cube_per_s" value="5.2"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="4125"/>
            <adiabaticHead unit="kJ_per_kg" value="33.1"/>
            <volumetricFlowrate unit="m_cube_per_s" value="5.61"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="4400"/>
            <adiabaticHead unit="kJ_per_kg" value="37.7"/>
            <volumetricFlowrate unit="m_cube_per_s" value="6.05"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="4675"/>
            <adiabaticHead unit="kJ_per_kg" value="42.5"/>
            <volumetricFlowrate unit="m_cube_per_s" value="6.5"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="4950"/>
            <adiabaticHead unit="kJ_per_kg" value="47.6"/>
            <volumetricFlowrate unit="m_cube_per_s" value="6.99"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="5225"/>
            <adiabaticHead unit="kJ_per_kg" value="52.8"/>
            <volumetricFlowrate unit="m_cube_per_s" value="7.49"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="5500"/>
            <adiabaticHead unit="kJ_per_kg" value="58.4"/>
            <volumetricFlowrate unit="m_cube_per_s" value="8.01"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="5775"/>
            <adiabaticHead unit="kJ_per_kg" value="64.1"/>
            <volumetricFlowrate unit="m_cube_per_s" value="8.56"/>
          </measurement>
        </surgelineMeasurements>
        <characteristicDiagramMeasurements>
          <adiabaticEfficiency value="0.85">
            <measurement>
              <speed unit="per_min" value="3370"/>
              <adiabaticHead unit="kJ_per_kg" value="21.7"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.75"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3850"/>
              <adiabaticHead unit="kJ_per_kg" value="28.4"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.5"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4125"/>
              <adiabaticHead unit="kJ_per_kg" value="32.6"/>
              <volumetricFlowrate unit="m_cube_per_s" value="6"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4400"/>
              <adiabaticHead unit="kJ_per_kg" value="37.1"/>
              <volumetricFlowrate unit="m_cube_per_s" value="6.48"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4675"/>
              <adiabaticHead unit="kJ_per_kg" value="41.8"/>
              <volumetricFlowrate unit="m_cube_per_s" value="7.01"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4950"/>
              <adiabaticHead unit="kJ_per_kg" value="46.8"/>
              <volumetricFlowrate unit="m_cube_per_s" value="7.49"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5225"/>
              <adiabaticHead unit="kJ_per_kg" value="52.2"/>
              <volumetricFlowrate unit="m_cube_per_s" value="7.91"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5500"/>
              <adiabaticHead unit="kJ_per_kg" value="57.9"/>
              <volumetricFlowrate unit="m_cube_per_s" value="8.32"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5775"/>
              <adiabaticHead unit="kJ_per_kg" value="63.8"/>
              <volumetricFlowrate unit="m_cube_per_s" value="8.74"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.86">
            <measurement>
              <speed unit="per_min" value="3370"/>
              <adiabaticHead unit="kJ_per_kg" value="21.5"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.91"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3850"/>
              <adiabaticHead unit="kJ_per_kg" value="28.1"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.69"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4125"/>
              <adiabaticHead unit="kJ_per_kg" value="32.2"/>
              <volumetricFlowrate unit="m_cube_per_s" value="6.21"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4400"/>
              <adiabaticHead unit="kJ_per_kg" value="36.7"/>
              <volumetricFlowrate unit="m_cube_per_s" value="6.73"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4675"/>
              <adiabaticHead unit="kJ_per_kg" value="41.2"/>
              <volumetricFlowrate unit="m_cube_per_s" value="7.3"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4950"/>
              <adiabaticHead unit="kJ_per_kg" value="46.1"/>
              <volumetricFlowrate unit="m_cube_per_s" value="7.86"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5225"/>
              <adiabaticHead unit="kJ_per_kg" value="51.4"/>
              <volumetricFlowrate unit="m_cube_per_s" value="8.29"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5500"/>
              <adiabaticHead unit="kJ_per_kg" value="57"/>
              <volumetricFlowrate unit="m_cube_per_s" value="8.73"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5775"/>
              <adiabaticHead unit="kJ_per_kg" value="62.9"/>
              <volumetricFlowrate unit="m_cube_per_s" value="9.16"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.86">
            <measurement>
              <speed unit="per_min" value="3370"/>
              <adiabaticHead unit="kJ_per_kg" value="21.1"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.11"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3850"/>
              <adiabaticHead unit="kJ_per_kg" value="27.6"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.95"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4125"/>
              <adiabaticHead unit="kJ_per_kg" value="31.6"/>
              <volumetricFlowrate unit="m_cube_per_s" value="6.53"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4400"/>
              <adiabaticHead unit="kJ_per_kg" value="35.8"/>
              <volumetricFlowrate unit="m_cube_per_s" value="7.14"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4675"/>
              <adiabaticHead unit="kJ_per_kg" value="39.9"/>
              <volumetricFlowrate unit="m_cube_per_s" value="7.9"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4950"/>
              <adiabaticHead unit="kJ_per_kg" value="45"/>
              <volumetricFlowrate unit="m_cube_per_s" value="8.34"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5225"/>
              <adiabaticHead unit="kJ_per_kg" value="50.1"/>
              <volumetricFlowrate unit="m_cube_per_s" value="8.8"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5500"/>
              <adiabaticHead unit="kJ_per_kg" value="55.6"/>
              <volumetricFlowrate unit="m_cube_per_s" value="9.27"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5775"/>
              <adiabaticHead unit="kJ_per_kg" value="61.3"/>
              <volumetricFlowrate unit="m_cube_per_s" value="9.73"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.86">
            <measurement>
              <speed unit="per_min" value="3370"/>
              <adiabaticHead unit="kJ_per_kg" value="19.1"/>
              <volumetricFlowrate unit="m_cube_per_s" value="6.03"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3850"/>
              <adiabaticHead unit="kJ_per_kg" value="25.3"/>
              <volumetricFlowrate unit="m_cube_per_s" value="6.83"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4125"/>
              <adiabaticHead unit="kJ_per_kg" value="29.7"/>
              <volumetricFlowrate unit="m_cube_per_s" value="7.26"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4400"/>
              <adiabaticHead unit="kJ_per_kg" value="34.4"/>
              <volumetricFlowrate unit="m_cube_per_s" value="7.65"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4675"/>
              <adiabaticHead unit="kJ_per_kg" value="39.9"/>
              <volumetricFlowrate unit="m_cube_per_s" value="7.9"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4950"/>
              <adiabaticHead unit="kJ_per_kg" value="45"/>
              <volumetricFlowrate unit="m_cube_per_s" value="8.34"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5225"/>
              <adiabaticHead unit="kJ_per_kg" value="50.1"/>
              <volumetricFlowrate unit="m_cube_per_s" value="8.8"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5500"/>
              <adiabaticHead unit="kJ_per_kg" value="55.6"/>
              <volumetricFlowrate unit="m_cube_per_s" value="9.27"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5775"/>
              <adiabaticHead unit="kJ_per_kg" value="61.3"/>
              <volumetricFlowrate unit="m_cube_per_s" value="9.73"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.86">
            <measurement>
              <speed unit="per_min" value="3370"/>
              <adiabaticHead unit="kJ_per_kg" value="18.5"/>
              <volumetricFlowrate unit="m_cube_per_s" value="6.24"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3850"/>
              <adiabaticHead unit="kJ_per_kg" value="24.5"/>
              <volumetricFlowrate unit="m_cube_per_s" value="7.09"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4125"/>
              <adiabaticHead unit="kJ_per_kg" value="28.7"/>
              <volumetricFlowrate unit="m_cube_per_s" value="7.59"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4400"/>
              <adiabaticHead unit="kJ_per_kg" value="33.1"/>
              <volumetricFlowrate unit="m_cube_per_s" value="8.06"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4675"/>
              <adiabaticHead unit="kJ_per_kg" value="38.1"/>
              <volumetricFlowrate unit="m_cube_per_s" value="8.5"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4950"/>
              <adiabaticHead unit="kJ_per_kg" value="43.6"/>
              <volumetricFlowrate unit="m_cube_per_s" value="8.82"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5225"/>
              <adiabaticHead unit="kJ_per_kg" value="48.6"/>
              <volumetricFlowrate unit="m_cube_per_s" value="9.31"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5500"/>
              <adiabaticHead unit="kJ_per_kg" value="53.9"/>
              <volumetricFlowrate unit="m_cube_per_s" value="9.8"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5775"/>
              <adiabaticHead unit="kJ_per_kg" value="59.4"/>
              <volumetricFlowrate unit="m_cube_per_s" value="10.29"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.85">
            <measurement>
              <speed unit="per_min" value="3370"/>
              <adiabaticHead unit="kJ_per_kg" value="18.1"/>
              <volumetricFlowrate unit="m_cube_per_s" value="6.39"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3850"/>
              <adiabaticHead unit="kJ_per_kg" value="23.9"/>
              <volumetricFlowrate unit="m_cube_per_s" value="7.28"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4125"/>
              <adiabaticHead unit="kJ_per_kg" value="28"/>
              <volumetricFlowrate unit="m_cube_per_s" value="7.8"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4400"/>
              <adiabaticHead unit="kJ_per_kg" value="32.2"/>
              <volumetricFlowrate unit="m_cube_per_s" value="8.31"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4675"/>
              <adiabaticHead unit="kJ_per_kg" value="37.2"/>
              <volumetricFlowrate unit="m_cube_per_s" value="8.79"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4950"/>
              <adiabaticHead unit="kJ_per_kg" value="42.4"/>
              <volumetricFlowrate unit="m_cube_per_s" value="9.19"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5225"/>
              <adiabaticHead unit="kJ_per_kg" value="47.3"/>
              <volumetricFlowrate unit="m_cube_per_s" value="9.7"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5500"/>
              <adiabaticHead unit="kJ_per_kg" value="52.4"/>
              <volumetricFlowrate unit="m_cube_per_s" value="10.21"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5775"/>
              <adiabaticHead unit="kJ_per_kg" value="57.7"/>
              <volumetricFlowrate unit="m_cube_per_s" value="10.72"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.84">
            <measurement>
              <speed unit="per_min" value="3370"/>
              <adiabaticHead unit="kJ_per_kg" value="17.3"/>
              <volumetricFlowrate unit="m_cube_per_s" value="6.64"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3850"/>
              <adiabaticHead unit="kJ_per_kg" value="22.8"/>
              <volumetricFlowrate unit="m_cube_per_s" value="7.57"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4125"/>
              <adiabaticHead unit="kJ_per_kg" value="26.9"/>
              <volumetricFlowrate unit="m_cube_per_s" value="8.12"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4400"/>
              <adiabaticHead unit="kJ_per_kg" value="30.9"/>
              <volumetricFlowrate unit="m_cube_per_s" value="8.66"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4675"/>
              <adiabaticHead unit="kJ_per_kg" value="35.7"/>
              <volumetricFlowrate unit="m_cube_per_s" value="9.18"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4950"/>
              <adiabaticHead unit="kJ_per_kg" value="40.7"/>
              <volumetricFlowrate unit="m_cube_per_s" value="9.64"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5225"/>
              <adiabaticHead unit="kJ_per_kg" value="45.4"/>
              <volumetricFlowrate unit="m_cube_per_s" value="10.18"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5500"/>
              <adiabaticHead unit="kJ_per_kg" value="50.3"/>
              <volumetricFlowrate unit="m_cube_per_s" value="10.71"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5775"/>
              <adiabaticHead unit="kJ_per_kg" value="55.4"/>
              <volumetricFlowrate unit="m_cube_per_s" value="11.25"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.82">
            <measurement>
              <speed unit="per_min" value="3370"/>
              <adiabaticHead unit="kJ_per_kg" value="16.1"/>
              <volumetricFlowrate unit="m_cube_per_s" value="7.01"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3850"/>
              <adiabaticHead unit="kJ_per_kg" value="21.2"/>
              <volumetricFlowrate unit="m_cube_per_s" value="8"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4125"/>
              <adiabaticHead unit="kJ_per_kg" value="25.1"/>
              <volumetricFlowrate unit="m_cube_per_s" value="8.59"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4400"/>
              <adiabaticHead unit="kJ_per_kg" value="28.8"/>
              <volumetricFlowrate unit="m_cube_per_s" value="9.17"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4675"/>
              <adiabaticHead unit="kJ_per_kg" value="33.5"/>
              <volumetricFlowrate unit="m_cube_per_s" value="9.73"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4950"/>
              <adiabaticHead unit="kJ_per_kg" value="38.2"/>
              <volumetricFlowrate unit="m_cube_per_s" value="10.25"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5225"/>
              <adiabaticHead unit="kJ_per_kg" value="42.6"/>
              <volumetricFlowrate unit="m_cube_per_s" value="10.82"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5500"/>
              <adiabaticHead unit="kJ_per_kg" value="47.1"/>
              <volumetricFlowrate unit="m_cube_per_s" value="11.39"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5775"/>
              <adiabaticHead unit="kJ_per_kg" value="51.9"/>
              <volumetricFlowrate unit="m_cube_per_s" value="11.96"/>
            </measurement>
          </adiabaticEfficiency>
        </characteristicDiagramMeasurements>
      </turboCompressor>
      <turboCompressor drive="drive_13" id="compressor_13">
        <speedMin unit="per_min" value="3370"/>
        <speedMax unit="per_min" value="5775"/>
        <n_isoline_coeff_1 value="0"/>
        <n_isoline_coeff_2 value="0.01097725194805195"/>
        <n_isoline_coeff_3 value="0"/>
        <n_isoline_coeff_4 value="0"/>
        <n_isoline_coeff_5 value="0"/>
        <n_isoline_coeff_6 value="0"/>
        <n_isoline_coeff_7 value="-0.4494974006281987"/>
        <n_isoline_coeff_8 value="1.945876193195665e-05"/>
        <n_isoline_coeff_9 value="0"/>
        <eta_ad_isoline_coeff_1 value="0.8597214530286412"/>
        <eta_ad_isoline_coeff_2 value="-7.005555445565705e-06"/>
        <eta_ad_isoline_coeff_3 value="5.619036137070684e-10"/>
        <eta_ad_isoline_coeff_4 value="0.008220844614121502"/>
        <eta_ad_isoline_coeff_5 value="1.234625127473538e-06"/>
        <eta_ad_isoline_coeff_6 value="-2.081791087306332e-10"/>
        <eta_ad_isoline_coeff_7 value="-0.0033148614350077"/>
        <eta_ad_isoline_coeff_8 value="6.562181985541666e-07"/>
        <eta_ad_isoline_coeff_9 value="-3.903700514411477e-11"/>
        <surgeline_coeff_1 value="10.79777387870129"/>
        <surgeline_coeff_2 value="43.88827934041674"/>
        <surgeline_coeff_3 value="0"/>
        <chokeline_coeff_1 value="1.056318661113279"/>
        <chokeline_coeff_2 value="1.245576162995589"/>
        <chokeline_coeff_3 value="0"/>
        <efficiencyOfChokeline value="0.82"/>
        <surgelineMeasurements>
          <measurement>
            <speed unit="per_min" value="3370"/>
            <adiabaticHead unit="kJ_per_kg" value="36.85797582685068"/>
            <volumetricFlowrate unit="m_cube_per_s" value="0.5937850000000007"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="3670.625"/>
            <adiabaticHead unit="kJ_per_kg" value="40.12456241095049"/>
            <volumetricFlowrate unit="m_cube_per_s" value="0.6682145887920957"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="3971.25"/>
            <adiabaticHead unit="kJ_per_kg" value="43.38816152754541"/>
            <volumetricFlowrate unit="m_cube_per_s" value="0.7425761077589481"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="4271.875"/>
            <adiabaticHead unit="kJ_per_kg" value="46.6489742261531"/>
            <volumetricFlowrate unit="m_cube_per_s" value="0.8168741378392664"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="4572.5"/>
            <adiabaticHead unit="kJ_per_kg" value="49.90720005198905"/>
            <volumetricFlowrate unit="m_cube_per_s" value="0.8911132256960429"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="4873.125"/>
            <adiabaticHead unit="kJ_per_kg" value="53.16303713419649"/>
            <volumetricFlowrate unit="m_cube_per_s" value="0.9652978857268848"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="5173.75"/>
            <adiabaticHead unit="kJ_per_kg" value="56.41668227235634"/>
            <volumetricFlowrate unit="m_cube_per_s" value="1.039432602035154"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="5474.375"/>
            <adiabaticHead unit="kJ_per_kg" value="59.66833102139808"/>
            <volumetricFlowrate unit="m_cube_per_s" value="1.11352183036467"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="5775"/>
            <adiabaticHead unit="kJ_per_kg" value="62.91817777499996"/>
            <volumetricFlowrate unit="m_cube_per_s" value="1.187569999999999"/>
          </measurement>
        </surgelineMeasurements>
        <characteristicDiagramMeasurements>
          <adiabaticEfficiency value="0.8525">
            <measurement>
              <speed unit="per_min" value="3370"/>
              <adiabaticHead unit="kJ_per_kg" value="36.12837832340519"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.50098742279105"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3670.625"/>
              <adiabaticHead unit="kJ_per_kg" value="39.25893475029127"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.65411529809311"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3971.25"/>
              <adiabaticHead unit="kJ_per_kg" value="42.378416518379"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.806701468106958"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4271.875"/>
              <adiabaticHead unit="kJ_per_kg" value="45.48773031642035"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.958790282559359"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4572.5"/>
              <adiabaticHead unit="kJ_per_kg" value="48.58775718098693"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.110424836427652"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4873.125"/>
              <adiabaticHead unit="kJ_per_kg" value="51.67935462167443"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.26164707389189"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5173.75"/>
              <adiabaticHead unit="kJ_per_kg" value="54.76335860856145"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.412497885549301"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5474.375"/>
              <adiabaticHead unit="kJ_per_kg" value="57.84058543590214"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.563017199574853"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5775"/>
              <adiabaticHead unit="kJ_per_kg" value="60.91183347463528"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.713244067443393"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.855">
            <measurement>
              <speed unit="per_min" value="3370"/>
              <adiabaticHead unit="kJ_per_kg" value="34.56706318198968"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.513905485905604"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3670.625"/>
              <adiabaticHead unit="kJ_per_kg" value="37.44032201379128"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.747058663622782"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3971.25"/>
              <adiabaticHead unit="kJ_per_kg" value="40.29144698407523"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.978415769196764"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4271.875"/>
              <adiabaticHead unit="kJ_per_kg" value="43.12264981548748"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.208156274855191"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4572.5"/>
              <adiabaticHead unit="kJ_per_kg" value="45.93601200503569"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.436449085548905"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4873.125"/>
              <adiabaticHead unit="kJ_per_kg" value="48.73350007811644"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.663453776753738"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5173.75"/>
              <adiabaticHead unit="kJ_per_kg" value="51.51697901183519"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.889321683717911"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5474.375"/>
              <adiabaticHead unit="kJ_per_kg" value="54.28822411176849"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.114196865212602"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5775"/>
              <adiabaticHead unit="kJ_per_kg" value="57.04893157781208"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.33821696090722"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.8574999999999999">
            <measurement>
              <speed unit="per_min" value="3370"/>
              <adiabaticHead unit="kJ_per_kg" value="32.05796994498832"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.585408755809286"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3670.625"/>
              <adiabaticHead unit="kJ_per_kg" value="34.56820535726366"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.891411684990985"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3971.25"/>
              <adiabaticHead unit="kJ_per_kg" value="37.04734132896724"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.193623527542189"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4271.875"/>
              <adiabaticHead unit="kJ_per_kg" value="39.49912222562919"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.492500729425913"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4572.5"/>
              <adiabaticHead unit="kJ_per_kg" value="41.92695125019271"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.788458148174691"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4873.125"/>
              <adiabaticHead unit="kJ_per_kg" value="44.33394307669083"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.081875469045488"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5173.75"/>
              <adiabaticHead unit="kJ_per_kg" value="46.72296744116653"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.373102518843726"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5474.375"/>
              <adiabaticHead unit="kJ_per_kg" value="49.0966855830922"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.66246370820827"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5775"/>
              <adiabaticHead unit="kJ_per_kg" value="51.4575809867474"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.950261779049469"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.86">
            <measurement>
              <speed unit="per_min" value="3370"/>
              <adiabaticHead unit="kJ_per_kg" value="28.67043632914223"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.656035304321792"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3670.625"/>
              <adiabaticHead unit="kJ_per_kg" value="30.7592208704887"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.021738300546088"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3971.25"/>
              <adiabaticHead unit="kJ_per_kg" value="32.81383326982704"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.381458461072202"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4271.875"/>
              <adiabaticHead unit="kJ_per_kg" value="34.83905186417676"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.736032373939935"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4572.5"/>
              <adiabaticHead unit="kJ_per_kg" value="36.83909110319792"/>
              <volumetricFlowrate unit="m_cube_per_s" value="6.086197902168475"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4873.125"/>
              <adiabaticHead unit="kJ_per_kg" value="38.81770654230654"/>
              <volumetricFlowrate unit="m_cube_per_s" value="6.432612565880626"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5173.75"/>
              <adiabaticHead unit="kJ_per_kg" value="40.77827750788899"/>
              <volumetricFlowrate unit="m_cube_per_s" value="6.775868015273065"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5474.375"/>
              <adiabaticHead unit="kJ_per_kg" value="42.72387308646977"/>
              <volumetricFlowrate unit="m_cube_per_s" value="7.116501583955587"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5775"/>
              <adiabaticHead unit="kJ_per_kg" value="44.65730548789935"/>
              <volumetricFlowrate unit="m_cube_per_s" value="7.455005631742223"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.85">
            <measurement>
              <speed unit="per_min" value="3370"/>
              <adiabaticHead unit="kJ_per_kg" value="24.63256736841199"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.674160910364014"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3670.625"/>
              <adiabaticHead unit="kJ_per_kg" value="26.29385719273663"/>
              <volumetricFlowrate unit="m_cube_per_s" value="6.085125333891294"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3971.25"/>
              <adiabaticHead unit="kJ_per_kg" value="27.92363364073589"/>
              <volumetricFlowrate unit="m_cube_per_s" value="6.488294081826433"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4271.875"/>
              <adiabaticHead unit="kJ_per_kg" value="29.52681714295356"/>
              <volumetricFlowrate unit="m_cube_per_s" value="6.884884354125949"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4572.5"/>
              <adiabaticHead unit="kJ_per_kg" value="31.10765461609776"/>
              <volumetricFlowrate unit="m_cube_per_s" value="7.275946739104522"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4873.125"/>
              <adiabaticHead unit="kJ_per_kg" value="32.66986053166762"/>
              <volumetricFlowrate unit="m_cube_per_s" value="7.66240011052878"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5173.75"/>
              <adiabaticHead unit="kJ_per_kg" value="34.21672401113793"/>
              <volumetricFlowrate unit="m_cube_per_s" value="8.045058120472559"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5474.375"/>
              <adiabaticHead unit="kJ_per_kg" value="35.75119157991926"/>
              <volumetricFlowrate unit="m_cube_per_s" value="8.4246496707199"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5775"/>
              <adiabaticHead unit="kJ_per_kg" value="37.27593216287358"/>
              <volumetricFlowrate unit="m_cube_per_s" value="8.801834991142364"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.84">
            <measurement>
              <speed unit="per_min" value="3370"/>
              <adiabaticHead unit="kJ_per_kg" value="20.22873711520545"/>
              <volumetricFlowrate unit="m_cube_per_s" value="6.608082830654558"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3670.625"/>
              <adiabaticHead unit="kJ_per_kg" value="21.49195465079799"/>
              <volumetricFlowrate unit="m_cube_per_s" value="7.051935265300095"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3971.25"/>
              <adiabaticHead unit="kJ_per_kg" value="22.72958552335056"/>
              <volumetricFlowrate unit="m_cube_per_s" value="7.486797401469909"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4271.875"/>
              <adiabaticHead unit="kJ_per_kg" value="23.94595738694741"/>
              <volumetricFlowrate unit="m_cube_per_s" value="7.914189832211097"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4572.5"/>
              <adiabaticHead unit="kJ_per_kg" value="25.14475553964802"/>
              <volumetricFlowrate unit="m_cube_per_s" value="8.335407448126434"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4873.125"/>
              <adiabaticHead unit="kJ_per_kg" value="26.32916723852595"/>
              <volumetricFlowrate unit="m_cube_per_s" value="8.751570144857073"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5173.75"/>
              <adiabaticHead unit="kJ_per_kg" value="27.50198872513608"/>
              <volumetricFlowrate unit="m_cube_per_s" value="9.163660428255749"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5474.375"/>
              <adiabaticHead unit="kJ_per_kg" value="28.66570624500657"/>
              <volumetricFlowrate unit="m_cube_per_s" value="9.572551881929163"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5775"/>
              <adiabaticHead unit="kJ_per_kg" value="29.82255854128629"/>
              <volumetricFlowrate unit="m_cube_per_s" value="9.979031125417642"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.83">
            <measurement>
              <speed unit="per_min" value="3370"/>
              <adiabaticHead unit="kJ_per_kg" value="15.70955748863441"/>
              <volumetricFlowrate unit="m_cube_per_s" value="7.445660875279724"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3670.625"/>
              <adiabaticHead unit="kJ_per_kg" value="16.6194787961608"/>
              <volumetricFlowrate unit="m_cube_per_s" value="7.913121898393409"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3971.25"/>
              <adiabaticHead unit="kJ_per_kg" value="17.5106822202232"/>
              <volumetricFlowrate unit="m_cube_per_s" value="8.370966836157494"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4271.875"/>
              <adiabaticHead unit="kJ_per_kg" value="18.38652892856724"/>
              <volumetricFlowrate unit="m_cube_per_s" value="8.820922447688648"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4572.5"/>
              <adiabaticHead unit="kJ_per_kg" value="19.24986050862142"/>
              <volumetricFlowrate unit="m_cube_per_s" value="9.264448564024571"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4873.125"/>
              <adiabaticHead unit="kJ_per_kg" value="20.10312051720471"/>
              <volumetricFlowrate unit="m_cube_per_s" value="9.702800532810368"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5173.75"/>
              <adiabaticHead unit="kJ_per_kg" value="20.94844340057531"/>
              <volumetricFlowrate unit="m_cube_per_s" value="10.13707489989389"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5474.375"/>
              <adiabaticHead unit="kJ_per_kg" value="21.78772102019508"/>
              <volumetricFlowrate unit="m_cube_per_s" value="10.56824358612943"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5775"/>
              <adiabaticHead unit="kJ_per_kg" value="22.62265344912461"/>
              <volumetricFlowrate unit="m_cube_per_s" value="10.99717998340891"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.82">
            <measurement>
              <speed unit="per_min" value="3370"/>
              <adiabaticHead unit="kJ_per_kg" value="11.25490944729671"/>
              <volumetricFlowrate unit="m_cube_per_s" value="8.187849999999999"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3670.625"/>
              <adiabaticHead unit="kJ_per_kg" value="11.85844716190755"/>
              <volumetricFlowrate unit="m_cube_per_s" value="8.672395010205827"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3971.25"/>
              <adiabaticHead unit="kJ_per_kg" value="12.44974308577371"/>
              <volumetricFlowrate unit="m_cube_per_s" value="9.147111805077776"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4271.875"/>
              <adiabaticHead unit="kJ_per_kg" value="13.03110218024761"/>
              <volumetricFlowrate unit="m_cube_per_s" value="9.613850902810459"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4572.5"/>
              <adiabaticHead unit="kJ_per_kg" value="13.60446712514902"/>
              <volumetricFlowrate unit="m_cube_per_s" value="10.07417196701778"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4873.125"/>
              <adiabaticHead unit="kJ_per_kg" value="14.17150500774365"/>
              <volumetricFlowrate unit="m_cube_per_s" value="10.52941340422618"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5173.75"/>
              <adiabaticHead unit="kJ_per_kg" value="14.73367029035507"/>
              <volumetricFlowrate unit="m_cube_per_s" value="10.98074291687471"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5474.375"/>
              <adiabaticHead unit="kJ_per_kg" value="15.2922516385379"/>
              <volumetricFlowrate unit="m_cube_per_s" value="11.42919509890704"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5775"/>
              <adiabaticHead unit="kJ_per_kg" value="15.8484075"/>
              <volumetricFlowrate unit="m_cube_per_s" value="11.8757"/>
            </measurement>
          </adiabaticEfficiency>
        </characteristicDiagramMeasurements>
      </turboCompressor>
    </compressors>
    <drives>
      <gasTurbine id="drive_12">
        <energy_rate_fun_coeff_1 value="9000.5"/>
        <energy_rate_fun_coeff_2 value="2.2799692426"/>
        <energy_rate_fun_coeff_3 value="1.88170237013e-20"/>
        <power_fun_coeff_1 value="2212.3797619"/>
        <power_fun_coeff_2 value="8.85120469303"/>
        <power_fun_coeff_3 value="-0.000821522485779"/>
        <power_fun_coeff_4 value="-41.2123809524"/>
        <power_fun_coeff_5 value="-0.166319874065"/>
        <power_fun_coeff_6 value="1.54413080033e-05"/>
        <power_fun_coeff_7 value="0.561952380953"/>
        <power_fun_coeff_8 value="0.00235479535616"/>
        <power_fun_coeff_9 value="-2.18847268434e-07"/>
        <specificEnergyConsumptionMeasurements>
          <measurement>
            <compressorPower unit="kW" value="20808"/>
            <fuelConsumption unit="kW" value="56442"/>
          </measurement>
          <measurement>
            <compressorPower unit="kW" value="15606"/>
            <fuelConsumption unit="kW" value="44582"/>
          </measurement>
          <measurement>
            <compressorPower unit="kW" value="10404"/>
            <fuelConsumption unit="kW" value="32721"/>
          </measurement>
          <measurement>
            <compressorPower unit="kW" value="5202"/>
            <fuelConsumption unit="kW" value="20861"/>
          </measurement>
        </specificEnergyConsumptionMeasurements>
        <maximalPowerMeasurements>
          <ambientTemperature unit="Celsius" value="-5">
            <measurement>
              <speed unit="per_min" value="3300"/>
              <maximalPower unit="kW" value="24760"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3575"/>
              <maximalPower unit="kW" value="25729"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3850"/>
              <maximalPower unit="kW" value="26563"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4125"/>
              <maximalPower unit="kW" value="27259"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4400"/>
              <maximalPower unit="kW" value="27820"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4675"/>
              <maximalPower unit="kW" value="28243"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4950"/>
              <maximalPower unit="kW" value="28529"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5225"/>
              <maximalPower unit="kW" value="28678"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5500"/>
              <maximalPower unit="kW" value="28689"/>
            </measurement>
          </ambientTemperature>
          <ambientTemperature unit="Celsius" value="5">
            <measurement>
              <speed unit="per_min" value="3300"/>
              <maximalPower unit="kW" value="20437"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3575"/>
              <maximalPower unit="kW" value="21237"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3850"/>
              <maximalPower unit="kW" value="21925"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4125"/>
              <maximalPower unit="kW" value="22500"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4400"/>
              <maximalPower unit="kW" value="22962"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4675"/>
              <maximalPower unit="kW" value="23312"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4950"/>
              <maximalPower unit="kW" value="23548"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5225"/>
              <maximalPower unit="kW" value="23671"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5500"/>
              <maximalPower unit="kW" value="23680"/>
            </measurement>
          </ambientTemperature>
          <ambientTemperature unit="Celsius" value="15">
            <measurement>
              <speed unit="per_min" value="3300"/>
              <maximalPower unit="kW" value="17563"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3575"/>
              <maximalPower unit="kW" value="18251"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3850"/>
              <maximalPower unit="kW" value="18842"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4125"/>
              <maximalPower unit="kW" value="19336"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4400"/>
              <maximalPower unit="kW" value="19734"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4675"/>
              <maximalPower unit="kW" value="20034"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4950"/>
              <maximalPower unit="kW" value="20237"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5225"/>
              <maximalPower unit="kW" value="20342"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5500"/>
              <maximalPower unit="kW" value="20351"/>
            </measurement>
          </ambientTemperature>
          <ambientTemperature unit="Celsius" value="25">
            <measurement>
              <speed unit="per_min" value="3300"/>
              <maximalPower unit="kW" value="15620"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3575"/>
              <maximalPower unit="kW" value="16232"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3850"/>
              <maximalPower unit="kW" value="16758"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4125"/>
              <maximalPower unit="kW" value="17197"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4400"/>
              <maximalPower unit="kW" value="17551"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4675"/>
              <maximalPower unit="kW" value="17818"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4950"/>
              <maximalPower unit="kW" value="17998"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5225"/>
              <maximalPower unit="kW" value="18092"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5500"/>
              <maximalPower unit="kW" value="18099"/>
            </measurement>
          </ambientTemperature>
        </maximalPowerMeasurements>
      </gasTurbine>
      <gasTurbine id="drive_13">
        <energy_rate_fun_coeff_1 value="0.01"/>
        <energy_rate_fun_coeff_2 value="0"/>
        <energy_rate_fun_coeff_3 value="0"/>
        <power_fun_coeff_1 value="-2630.376212358265"/>
        <power_fun_coeff_2 value="9.59455950004968"/>
        <power_fun_coeff_3 value="-0.0006550977325623112"/>
        <power_fun_coeff_4 value="15.82329111977949"/>
        <power_fun_coeff_5 value="-0.0577170320435722"/>
        <power_fun_coeff_6 value="3.940805914203213e-06"/>
        <power_fun_coeff_7 value="-0.05259137789750652"/>
        <power_fun_coeff_8 value="0.000191832294580718"/>
        <power_fun_coeff_9 value="-1.309793338729131e-08"/>
      </gasTurbine>
    </drives>
    <configurations>
      <configuration nrOfSerialStages="2" confId="config_1">
        <stage nrOfParallelUnits="1" stageNr="1">
          <compressor nominalSpeed="5500" id="compressor_12"/>
        </stage>
        <stage nrOfParallelUnits="1" stageNr="2">
          <compressor nominalSpeed="5500" id="compressor_13"/>
        </stage>
      </configuration>
      <configuration nrOfSerialStages="1" confId="config_2">
        <stage nrOfParallelUnits="1" stageNr="1">
          <compressor nominalSpeed="5500" id="compressor_12"/>
        </stage>
      </configuration>
      <configuration nrOfSerialStages="1" confId="config_3">
        <stage nrOfParallelUnits="1" stageNr="1">
          <compressor nominalSpeed="5500" id="compressor_13"/>
        </stage>
      </configuration>
    </configurations>
  </compressorStation>
  <compressorStation id="compressorStation_2">
    <compressors>
      <turboCompressor drive="drive_14" id="compressor_14">
        <speedMin unit="per_min" value="3200"/>
        <speedMax unit="per_min" value="5000"/>
        <n_isoline_coeff_1 value="0"/>
        <n_isoline_coeff_2 value="0.008559888"/>
        <n_isoline_coeff_3 value="0"/>
        <n_isoline_coeff_4 value="0"/>
        <n_isoline_coeff_5 value="0"/>
        <n_isoline_coeff_6 value="0"/>
        <n_isoline_coeff_7 value="-0.7399162157530732"/>
        <n_isoline_coeff_8 value="3.699581078765366e-05"/>
        <n_isoline_coeff_9 value="0"/>
        <eta_ad_isoline_coeff_1 value="0.8459998143917549"/>
        <eta_ad_isoline_coeff_2 value="-3.365751076041496e-05"/>
        <eta_ad_isoline_coeff_3 value="2.686721232315269e-09"/>
        <eta_ad_isoline_coeff_4 value="0.03951571000943077"/>
        <eta_ad_isoline_coeff_5 value="1.380612832519401e-05"/>
        <eta_ad_isoline_coeff_6 value="-1.991496893680525e-09"/>
        <eta_ad_isoline_coeff_7 value="-0.03612996797976415"/>
        <eta_ad_isoline_coeff_8 value="7.835173433373271e-06"/>
        <eta_ad_isoline_coeff_9 value="-5.262585288696349e-10"/>
        <surgeline_coeff_1 value="12.125081352"/>
        <surgeline_coeff_2 value="39.90975326802971"/>
        <surgeline_coeff_3 value="0"/>
        <chokeline_coeff_1 value="-0.003607215319654244"/>
        <chokeline_coeff_2 value="1.407332485085748"/>
        <chokeline_coeff_3 value="0"/>
        <efficiencyOfChokeline value="0.6"/>
        <surgelineMeasurements>
          <measurement>
            <speed unit="per_min" value="3200"/>
            <adiabaticHead unit="kJ_per_kg" value="27.30176277600002"/>
            <volumetricFlowrate unit="m_cube_per_s" value="0.3802750000000005"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="3425"/>
            <adiabaticHead unit="kJ_per_kg" value="29.20530212429689"/>
            <volumetricFlowrate unit="m_cube_per_s" value="0.427971094122981"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="3650"/>
            <adiabaticHead unit="kJ_per_kg" value="31.10676114341154"/>
            <volumetricFlowrate unit="m_cube_per_s" value="0.4756150624117513"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="3875"/>
            <adiabaticHead unit="kJ_per_kg" value="33.00625923592524"/>
            <volumetricFlowrate unit="m_cube_per_s" value="0.52320989668088"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="4100"/>
            <adiabaticHead unit="kJ_per_kg" value="34.90391475126786"/>
            <volumetricFlowrate unit="m_cube_per_s" value="0.5707585623566152"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="4325"/>
            <adiabaticHead unit="kJ_per_kg" value="36.79984504044076"/>
            <volumetricFlowrate unit="m_cube_per_s" value="0.6182639998480483"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="4550"/>
            <adiabaticHead unit="kJ_per_kg" value="38.69416650951855"/>
            <volumetricFlowrate unit="m_cube_per_s" value="0.6657291258876837"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="4775"/>
            <adiabaticHead unit="kJ_per_kg" value="40.58699467198817"/>
            <volumetricFlowrate unit="m_cube_per_s" value="0.7131568348428754"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="5000"/>
            <adiabaticHead unit="kJ_per_kg" value="42.47844419999986"/>
            <volumetricFlowrate unit="m_cube_per_s" value="0.7605499999999965"/>
          </measurement>
        </surgelineMeasurements>
        <characteristicDiagramMeasurements>
          <adiabaticEfficiency value="0.805">
            <measurement>
              <speed unit="per_min" value="3200"/>
              <adiabaticHead unit="kJ_per_kg" value="26.72930232239816"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.032308110253006"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3425"/>
              <adiabaticHead unit="kJ_per_kg" value="28.54520055482505"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.122335096060465"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3650"/>
              <adiabaticHead unit="kJ_per_kg" value="30.35496883787062"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.212058176695212"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3875"/>
              <adiabaticHead unit="kJ_per_kg" value="32.15905656661958"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.301499631866644"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4100"/>
              <adiabaticHead unit="kJ_per_kg" value="33.95790093648489"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.390681136459695"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4325"/>
              <adiabaticHead unit="kJ_per_kg" value="35.75192786133405"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.479623806052881"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4550"/>
              <adiabaticHead unit="kJ_per_kg" value="37.54155283487788"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.568348239623467"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4775"/>
              <adiabaticHead unit="kJ_per_kg" value="39.32718174062619"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.65687455970273"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5000"/>
              <adiabaticHead unit="kJ_per_kg" value="41.10921161521603"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.745222450219566"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.8100000000000001">
            <measurement>
              <speed unit="per_min" value="3200"/>
              <adiabaticHead unit="kJ_per_kg" value="25.48606460178629"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.750984635572953"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3425"/>
              <adiabaticHead unit="kJ_per_kg" value="27.14334612219469"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.883014746838579"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3650"/>
              <adiabaticHead unit="kJ_per_kg" value="28.78965694408772"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.014170859011226"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3875"/>
              <adiabaticHead unit="kJ_per_kg" value="30.4259880556759"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.144531920828383"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4100"/>
              <adiabaticHead unit="kJ_per_kg" value="32.05327897234962"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.274172780359012"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4325"/>
              <adiabaticHead unit="kJ_per_kg" value="33.67242312011471"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.403164613883972"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4550"/>
              <adiabaticHead unit="kJ_per_kg" value="35.28427264210054"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.531575308814541"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4775"/>
              <adiabaticHead unit="kJ_per_kg" value="36.88964270834724"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.659469807038852"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5000"/>
              <adiabaticHead unit="kJ_per_kg" value="38.48931539677443"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.786910414105766"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.8149999999999999">
            <measurement>
              <speed unit="per_min" value="3200"/>
              <adiabaticHead unit="kJ_per_kg" value="23.50990736587966"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.499090497825869"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3425"/>
              <adiabaticHead unit="kJ_per_kg" value="24.95134234438321"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.668409341409983"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3650"/>
              <adiabaticHead unit="kJ_per_kg" value="26.37844074037427"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.836044131527817"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3875"/>
              <adiabaticHead unit="kJ_per_kg" value="27.79275365258324"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.002177068727601"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4100"/>
              <adiabaticHead unit="kJ_per_kg" value="29.19571319359776"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.166976376793852"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4325"/>
              <adiabaticHead unit="kJ_per_kg" value="30.58864848352823"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.330598181450888"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4550"/>
              <adiabaticHead unit="kJ_per_kg" value="31.97279926961679"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.49318811019666"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4775"/>
              <adiabaticHead unit="kJ_per_kg" value="33.34932760574711"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.654882664241905"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5000"/>
              <adiabaticHead unit="kJ_per_kg" value="34.71932793680332"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.815810403074156"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.82">
            <measurement>
              <speed unit="per_min" value="3200"/>
              <adiabaticHead unit="kJ_per_kg" value="20.88868494556888"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.234629283417787"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3425"/>
              <adiabaticHead unit="kJ_per_kg" value="22.08670586783604"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.433945914892603"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3650"/>
              <adiabaticHead unit="kJ_per_kg" value="23.26974575183583"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.630770127388796"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3875"/>
              <adiabaticHead unit="kJ_per_kg" value="24.4396734707207"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.82541284828207"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4100"/>
              <adiabaticHead unit="kJ_per_kg" value="25.59817759627744"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.018155007925384"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4325"/>
              <adiabaticHead unit="kJ_per_kg" value="26.74679508484479"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.209252312170339"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4550"/>
              <adiabaticHead unit="kJ_per_kg" value="27.88693479662496"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.398939155312145"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4775"/>
              <adiabaticHead unit="kJ_per_kg" value="29.01989697039368"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.587431860127872"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5000"/>
              <adiabaticHead unit="kJ_per_kg" value="30.14688950180557"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.774931386123797"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.7649999999999999">
            <measurement>
              <speed unit="per_min" value="3200"/>
              <adiabaticHead unit="kJ_per_kg" value="17.81797934189224"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.924715092990402"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3425"/>
              <adiabaticHead unit="kJ_per_kg" value="18.7739201637342"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.146611992263691"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3650"/>
              <adiabaticHead unit="kJ_per_kg" value="19.71649815328135"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.365407056168121"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3875"/>
              <adiabaticHead unit="kJ_per_kg" value="20.64756972314057"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.581531202802202"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4100"/>
              <adiabaticHead unit="kJ_per_kg" value="21.56878757240736"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.795368063449737"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4325"/>
              <adiabaticHead unit="kJ_per_kg" value="22.48163668393407"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.007262338413173"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4550"/>
              <adiabaticHead unit="kJ_per_kg" value="23.38746307106211"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.217526469822835"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4775"/>
              <adiabaticHead unit="kJ_per_kg" value="24.28749701811793"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.426446036316047"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5000"/>
              <adiabaticHead unit="kJ_per_kg" value="25.18287208812297"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.634284165184625"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.71">
            <measurement>
              <speed unit="per_min" value="3200"/>
              <adiabaticHead unit="kJ_per_kg" value="14.51595314952485"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.551497558961744"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3425"/>
              <adiabaticHead unit="kJ_per_kg" value="15.24888982830963"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.789876889443365"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3650"/>
              <adiabaticHead unit="kJ_per_kg" value="15.97119008422767"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.024796844190242"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3875"/>
              <adiabaticHead unit="kJ_per_kg" value="16.68445879087965"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.256779390113716"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4100"/>
              <adiabaticHead unit="kJ_per_kg" value="17.39011243901497"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.486285224742312"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4325"/>
              <adiabaticHead unit="kJ_per_kg" value="18.08941457593307"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.713725302484487"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4550"/>
              <adiabaticHead unit="kJ_per_kg" value="18.78350364779865"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.93946989002547"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4775"/>
              <adiabaticHead unit="kJ_per_kg" value="19.47341518236348"/>
              <volumetricFlowrate unit="m_cube_per_s" value="6.163855781005559"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5000"/>
              <adiabaticHead unit="kJ_per_kg" value="20.16009969611815"/>
              <volumetricFlowrate unit="m_cube_per_s" value="6.387192120117881"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.655">
            <measurement>
              <speed unit="per_min" value="3200"/>
              <adiabaticHead unit="kJ_per_kg" value="11.16263336558722"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.109931456415109"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3425"/>
              <adiabaticHead unit="kJ_per_kg" value="11.69844622446194"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.360307223275967"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3650"/>
              <adiabaticHead unit="kJ_per_kg" value="12.22653982848222"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.607075920388934"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3875"/>
              <adiabaticHead unit="kJ_per_kg" value="12.74815930462578"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.850819373323755"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4100"/>
              <adiabaticHead unit="kJ_per_kg" value="13.26439909177397"/>
              <volumetricFlowrate unit="m_cube_per_s" value="6.092048993797519"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4325"/>
              <adiabaticHead unit="kJ_per_kg" value="13.77623234174558"/>
              <volumetricFlowrate unit="m_cube_per_s" value="6.331219518252007"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4550"/>
              <adiabaticHead unit="kJ_per_kg" value="14.28453380752023"/>
              <volumetricFlowrate unit="m_cube_per_s" value="6.56873970311114"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4775"/>
              <adiabaticHead unit="kJ_per_kg" value="14.79009793336629"/>
              <volumetricFlowrate unit="m_cube_per_s" value="6.804980777974263"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5000"/>
              <adiabaticHead unit="kJ_per_kg" value="15.29365335665315"/>
              <volumetricFlowrate unit="m_cube_per_s" value="7.040283222053655"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.6">
            <measurement>
              <speed unit="per_min" value="3200"/>
              <adiabaticHead unit="kJ_per_kg" value="7.881324865494521"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.60275"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3425"/>
              <adiabaticHead unit="kJ_per_kg" value="8.24614811555908"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.861980319722444"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3650"/>
              <adiabaticHead unit="kJ_per_kg" value="8.605888849383476"/>
              <volumetricFlowrate unit="m_cube_per_s" value="6.117599185652677"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3875"/>
              <adiabaticHead unit="kJ_per_kg" value="8.96141527452612"/>
              <volumetricFlowrate unit="m_cube_per_s" value="6.370223514949661"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4100"/>
              <adiabaticHead unit="kJ_per_kg" value="9.313489608236621"/>
              <volumetricFlowrate unit="m_cube_per_s" value="6.620394911859504"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4325"/>
              <adiabaticHead unit="kJ_per_kg" value="9.662789193477378"/>
              <volumetricFlowrate unit="m_cube_per_s" value="6.86859467200323"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4550"/>
              <adiabaticHead unit="kJ_per_kg" value="10.00992286501319"/>
              <volumetricFlowrate unit="m_cube_per_s" value="7.11525541153321"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4775"/>
              <adiabaticHead unit="kJ_per_kg" value="10.35544383654968"/>
              <volumetricFlowrate unit="m_cube_per_s" value="7.360770224271604"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5000"/>
              <adiabaticHead unit="kJ_per_kg" value="10.69986"/>
              <volumetricFlowrate unit="m_cube_per_s" value="7.6055"/>
            </measurement>
          </adiabaticEfficiency>
        </characteristicDiagramMeasurements>
      </turboCompressor>
    </compressors>
    <drives>
      <gasTurbine id="drive_14">
        <energy_rate_fun_coeff_1 value="0.01"/>
        <energy_rate_fun_coeff_2 value="0"/>
        <energy_rate_fun_coeff_3 value="0"/>
        <power_fun_coeff_1 value="-1447.344623120817"/>
        <power_fun_coeff_2 value="6.097630564902852"/>
        <power_fun_coeff_3 value="-0.0004808660856595387"/>
        <power_fun_coeff_4 value="8.706646302034349"/>
        <power_fun_coeff_5 value="-0.03668090637225615"/>
        <power_fun_coeff_6 value="2.892698020637114e-06"/>
        <power_fun_coeff_7 value="-0.02893800805559579"/>
        <power_fun_coeff_8 value="0.0001219151814905913"/>
        <power_fun_coeff_9 value="-9.614369955977631e-09"/>
      </gasTurbine>
    </drives>
    <configurations>
      <configuration nrOfSerialStages="1" confId="config_1">
        <stage nrOfParallelUnits="1" stageNr="1">
          <compressor nominalSpeed="3200" id="compressor_14"/>
        </stage>
      </configuration>
    </configurations>
  </compressorStation>
  <compressorStation id="compressorStation_1">
    <compressors>
      <turboCompressor drive="drive_15" id="compressor_15">
        <speedMin unit="per_min" value="3200"/>
        <speedMax unit="per_min" value="5000"/>
        <n_isoline_coeff_1 value="0"/>
        <n_isoline_coeff_2 value="0.008516796"/>
        <n_isoline_coeff_3 value="0"/>
        <n_isoline_coeff_4 value="0"/>
        <n_isoline_coeff_5 value="0"/>
        <n_isoline_coeff_6 value="0"/>
        <n_isoline_coeff_7 value="-0.7757594230885926"/>
        <n_isoline_coeff_8 value="3.878797115442963e-05"/>
        <n_isoline_coeff_9 value="0"/>
        <eta_ad_isoline_coeff_1 value="0.8416775113510657"/>
        <eta_ad_isoline_coeff_2 value="-3.150920705368534e-05"/>
        <eta_ad_isoline_coeff_3 value="2.445122032934506e-09"/>
        <eta_ad_isoline_coeff_4 value="0.04259121206748872"/>
        <eta_ad_isoline_coeff_5 value="1.274965843247456e-05"/>
        <eta_ad_isoline_coeff_6 value="-1.851740707333718e-09"/>
        <eta_ad_isoline_coeff_7 value="-0.03686254302055068"/>
        <eta_ad_isoline_coeff_8 value="7.872424382734326e-06"/>
        <eta_ad_isoline_coeff_9 value="-5.252524609975944e-10"/>
        <surgeline_coeff_1 value="12.06404153399999"/>
        <surgeline_coeff_2 value="40.76199030368473"/>
        <surgeline_coeff_3 value="0"/>
        <chokeline_coeff_1 value="-1.556054237862702"/>
        <chokeline_coeff_2 value="1.646922558761332"/>
        <chokeline_coeff_3 value="0"/>
        <efficiencyOfChokeline value="0.6"/>
        <surgelineMeasurements>
          <measurement>
            <speed unit="per_min" value="3200"/>
            <adiabaticHead unit="kJ_per_kg" value="27.16432084200007"/>
            <volumetricFlowrate unit="m_cube_per_s" value="0.3704500000000018"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="3425"/>
            <adiabaticHead unit="kJ_per_kg" value="29.05827743435469"/>
            <volumetricFlowrate unit="m_cube_per_s" value="0.4169137908562449"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="3650"/>
            <adiabaticHead unit="kJ_per_kg" value="30.95016417027451"/>
            <volumetricFlowrate unit="m_cube_per_s" value="0.4633268026308147"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="3875"/>
            <adiabaticHead unit="kJ_per_kg" value="32.8400998512471"/>
            <volumetricFlowrate unit="m_cube_per_s" value="0.5096919498400704"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="4100"/>
            <adiabaticHead unit="kJ_per_kg" value="34.72820223090966"/>
            <volumetricFlowrate unit="m_cube_per_s" value="0.5560121212938151"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="4325"/>
            <adiabaticHead unit="kJ_per_kg" value="36.61458806949864"/>
            <volumetricFlowrate unit="m_cube_per_s" value="0.6022901814310909"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="4550"/>
            <adiabaticHead unit="kJ_per_kg" value="38.49937318707924"/>
            <volumetricFlowrate unit="m_cube_per_s" value="0.6485289716260395"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="4775"/>
            <adiabaticHead unit="kJ_per_kg" value="40.38267251562286"/>
            <volumetricFlowrate unit="m_cube_per_s" value="0.6947313114654996"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="5000"/>
            <adiabaticHead unit="kJ_per_kg" value="42.26460014999994"/>
            <volumetricFlowrate unit="m_cube_per_s" value="0.7408999999999983"/>
          </measurement>
        </surgelineMeasurements>
        <characteristicDiagramMeasurements>
          <adiabaticEfficiency value="0.805">
            <measurement>
              <speed unit="per_min" value="3200"/>
              <adiabaticHead unit="kJ_per_kg" value="26.58020838750471"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.016665627208996"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3425"/>
              <adiabaticHead unit="kJ_per_kg" value="28.3883843739501"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.102626999373814"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3650"/>
              <adiabaticHead unit="kJ_per_kg" value="30.19078187308257"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.188313660060224"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3875"/>
              <adiabaticHead unit="kJ_per_kg" value="31.98782679786461"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.273745857331996"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4100"/>
              <adiabaticHead unit="kJ_per_kg" value="33.77993402355796"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.35894331451642"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4325"/>
              <adiabaticHead unit="kJ_per_kg" value="35.56750820991188"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.443925269291445"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4550"/>
              <adiabaticHead unit="kJ_per_kg" value="37.35094457440393"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.528710510445846"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4775"/>
              <adiabaticHead unit="kJ_per_kg" value="39.13062962102898"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.613317412526124"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5000"/>
              <adiabaticHead unit="kJ_per_kg" value="40.90694182871724"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.697763968564164"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.8100000000000001">
            <measurement>
              <speed unit="per_min" value="3200"/>
              <adiabaticHead unit="kJ_per_kg" value="25.31525800248024"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.724759396835367"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3425"/>
              <adiabaticHead unit="kJ_per_kg" value="26.970228446086"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.849762992737493"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3650"/>
              <adiabaticHead unit="kJ_per_kg" value="28.61509069712191"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.9740030943886"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3875"/>
              <adiabaticHead unit="kJ_per_kg" value="30.25075886377156"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.097548746411465"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4100"/>
              <adiabaticHead unit="kJ_per_kg" value="31.87810251589625"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.2204656293504"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4325"/>
              <adiabaticHead unit="kJ_per_kg" value="33.49795122564082"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.342816402633289"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4550"/>
              <adiabaticHead unit="kJ_per_kg" value="35.11109864460481"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.464661012529398"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4775"/>
              <adiabaticHead unit="kJ_per_kg" value="36.71830617983013"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.586056969804885"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5000"/>
              <adiabaticHead unit="kJ_per_kg" value="38.32030632169277"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.707059601085865"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.8149999999999999">
            <measurement>
              <speed unit="per_min" value="3200"/>
              <adiabaticHead unit="kJ_per_kg" value="23.31401631308476"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.458839072936158"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3425"/>
              <adiabaticHead unit="kJ_per_kg" value="24.76170044529"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.618554058530338"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3650"/>
              <adiabaticHead unit="kJ_per_kg" value="26.19627844307218"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.776823116781663"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3875"/>
              <adiabaticHead unit="kJ_per_kg" value="27.61916270403739"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.933802069708409"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4100"/>
              <adiabaticHead unit="kJ_per_kg" value="29.03166468090865"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.089635602638065"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4325"/>
              <adiabaticHead unit="kJ_per_kg" value="30.43500797368297"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.244458708592621"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4550"/>
              <adiabaticHead unit="kJ_per_kg" value="31.8303395786647"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.398397929332222"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4775"/>
              <adiabaticHead unit="kJ_per_kg" value="33.21873961726476"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.551572428679799"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5000"/>
              <adiabaticHead unit="kJ_per_kg" value="34.601229804185"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.704094926769015"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.82">
            <measurement>
              <speed unit="per_min" value="3200"/>
              <adiabaticHead unit="kJ_per_kg" value="20.66706349731786"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.179290640698127"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3425"/>
              <adiabaticHead unit="kJ_per_kg" value="21.88098453301881"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.367130268896847"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3650"/>
              <adiabaticHead unit="kJ_per_kg" value="23.08118591463334"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.552846946222474"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3875"/>
              <adiabaticHead unit="kJ_per_kg" value="24.26936912091226"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.736703955974778"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4100"/>
              <adiabaticHead unit="kJ_per_kg" value="25.44708298855143"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.918940961937921"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4325"/>
              <adiabaticHead unit="kJ_per_kg" value="26.61574704090353"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.099777618217026"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4550"/>
              <adiabaticHead unit="kJ_per_kg" value="27.77667083491251"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.279416562942765"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4775"/>
              <adiabaticHead unit="kJ_per_kg" value="28.93107015277952"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.458045923736225"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5000"/>
              <adiabaticHead unit="kJ_per_kg" value="30.08008067235708"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.635841433037405"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.7649999999999999">
            <measurement>
              <speed unit="per_min" value="3200"/>
              <adiabaticHead unit="kJ_per_kg" value="17.56806217503191"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.855333908805649"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3425"/>
              <adiabaticHead unit="kJ_per_kg" value="18.54859932264427"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.064584281333251"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3650"/>
              <adiabaticHead unit="kJ_per_kg" value="19.5167968979223"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.271201341992885"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3875"/>
              <adiabaticHead unit="kJ_per_kg" value="20.47436149776141"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.475549285080496"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4100"/>
              <adiabaticHead unit="kJ_per_kg" value="21.42282556185124"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.677955139079104"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4325"/>
              <adiabaticHead unit="kJ_per_kg" value="22.3635769108562"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.87871507021937"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4550"/>
              <adiabaticHead unit="kJ_per_kg" value="23.29788264193339"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.078099481874383"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4775"/>
              <adiabaticHead unit="kJ_per_kg" value="24.22690867919758"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.276357186703558"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5000"/>
              <adiabaticHead unit="kJ_per_kg" value="25.15173594215502"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.473718857058175"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.71">
            <measurement>
              <speed unit="per_min" value="3200"/>
              <adiabaticHead unit="kJ_per_kg" value="14.23218402909342"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.470214760354388"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3425"/>
              <adiabaticHead unit="kJ_per_kg" value="14.99650500042573"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.695302526207968"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3650"/>
              <adiabaticHead unit="kJ_per_kg" value="15.75086893857882"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.917458007802836"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3875"/>
              <adiabaticHead unit="kJ_per_kg" value="16.49677715093977"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.137123330814323"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4100"/>
              <adiabaticHead unit="kJ_per_kg" value="17.23556695932256"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.354692328187778"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4325"/>
              <adiabaticHead unit="kJ_per_kg" value="17.9684413391818"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.570519268702435"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4550"/>
              <adiabaticHead unit="kJ_per_kg" value="18.69649252485902"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.784925808569425"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4775"/>
              <adiabaticHead unit="kJ_per_kg" value="19.42072105352176"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.998206599753217"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5000"/>
              <adiabaticHead unit="kJ_per_kg" value="20.14205131805354"/>
              <volumetricFlowrate unit="m_cube_per_s" value="6.210633870200882"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.655">
            <measurement>
              <speed unit="per_min" value="3200"/>
              <adiabaticHead unit="kJ_per_kg" value="10.83805842273072"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.019106164935128"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3425"/>
              <adiabaticHead unit="kJ_per_kg" value="11.41010449792493"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.255877374467439"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3650"/>
              <adiabaticHead unit="kJ_per_kg" value="11.9747739236004"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.489595371497145"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3875"/>
              <adiabaticHead unit="kJ_per_kg" value="12.53326199620021"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.720754892019911"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4100"/>
              <adiabaticHead unit="kJ_per_kg" value="13.08662933630437"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.949794929376443"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4325"/>
              <adiabaticHead unit="kJ_per_kg" value="13.63582717784202"/>
              <volumetricFlowrate unit="m_cube_per_s" value="6.177109201516595"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4550"/>
              <adiabaticHead unit="kJ_per_kg" value="14.18171733036736"/>
              <volumetricFlowrate unit="m_cube_per_s" value="6.40305441343212"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4775"/>
              <adiabaticHead unit="kJ_per_kg" value="14.72508815848485"/>
              <volumetricFlowrate unit="m_cube_per_s" value="6.627956871078164"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5000"/>
              <adiabaticHead unit="kJ_per_kg" value="15.26666754338386"/>
              <volumetricFlowrate unit="m_cube_per_s" value="6.852117846182781"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.6">
            <measurement>
              <speed unit="per_min" value="3200"/>
              <adiabaticHead unit="kJ_per_kg" value="7.509430986839053"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.5045"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3425"/>
              <adiabaticHead unit="kJ_per_kg" value="7.913758379334867"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.75000479944844"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3650"/>
              <adiabaticHead unit="kJ_per_kg" value="8.31306102355035"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.99245860645428"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3875"/>
              <adiabaticHead unit="kJ_per_kg" value="8.708206524782735"/>
              <volumetricFlowrate unit="m_cube_per_s" value="6.23238822496019"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4100"/>
              <adiabaticHead unit="kJ_per_kg" value="9.099963866564144"/>
              <volumetricFlowrate unit="m_cube_per_s" value="6.470260576454394"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4325"/>
              <adiabaticHead unit="kJ_per_kg" value="9.489022357277772"/>
              <volumetricFlowrate unit="m_cube_per_s" value="6.706494204225115"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4550"/>
              <adiabaticHead unit="kJ_per_kg" value="9.876006519840123"/>
              <volumetricFlowrate unit="m_cube_per_s" value="6.941468314272771"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4775"/>
              <adiabaticHead unit="kJ_per_kg" value="10.26148796622906"/>
              <volumetricFlowrate unit="m_cube_per_s" value="7.175529985441367"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5000"/>
              <adiabaticHead unit="kJ_per_kg" value="10.64599500000001"/>
              <volumetricFlowrate unit="m_cube_per_s" value="7.409"/>
            </measurement>
          </adiabaticEfficiency>
        </characteristicDiagramMeasurements>
      </turboCompressor>
    </compressors>
    <drives>
      <gasTurbine id="drive_15">
        <energy_rate_fun_coeff_1 value="0.01"/>
        <energy_rate_fun_coeff_2 value="0"/>
        <energy_rate_fun_coeff_3 value="0"/>
        <power_fun_coeff_1 value="-1350.43877304712"/>
        <power_fun_coeff_2 value="5.68936838332708"/>
        <power_fun_coeff_3 value="-0.0004486700654042032"/>
        <power_fun_coeff_4 value="8.123699471188786"/>
        <power_fun_coeff_5 value="-0.03422496439638269"/>
        <power_fun_coeff_6 value="2.699019641474102e-06"/>
        <power_fun_coeff_7 value="-0.02700048590277199"/>
        <power_fun_coeff_8 value="0.0001137524439431505"/>
        <power_fun_coeff_9 value="-8.970647183513059e-09"/>
      </gasTurbine>
    </drives>
    <configurations>
      <configuration nrOfSerialStages="1" confId="config_1">
        <stage nrOfParallelUnits="1" stageNr="1">
          <compressor nominalSpeed="3200" id="compressor_15"/>
        </stage>
      </configuration>
    </configurations>
  </compressorStation>
  <compressorStation id="compressorStation_3">
    <compressors>
      <turboCompressor drive="drive_16" id="compressor_16">
        <speedMin unit="per_min" value="3250"/>
        <speedMax unit="per_min" value="6500"/>
        <n_isoline_coeff_1 value="0"/>
        <n_isoline_coeff_2 value="0.005827470769230769"/>
        <n_isoline_coeff_3 value="0"/>
        <n_isoline_coeff_4 value="0"/>
        <n_isoline_coeff_5 value="0"/>
        <n_isoline_coeff_6 value="0"/>
        <n_isoline_coeff_7 value="-0.3717562294538965"/>
        <n_isoline_coeff_8 value="1.429831651745755e-05"/>
        <n_isoline_coeff_9 value="0"/>
        <eta_ad_isoline_coeff_1 value="0.8410114198223591"/>
        <eta_ad_isoline_coeff_2 value="-2.990317884233911e-05"/>
        <eta_ad_isoline_coeff_3 value="2.377845387729706e-09"/>
        <eta_ad_isoline_coeff_4 value="0.02791873868558987"/>
        <eta_ad_isoline_coeff_5 value="1.167408343990321e-05"/>
        <eta_ad_isoline_coeff_6 value="-1.446146827201401e-09"/>
        <eta_ad_isoline_coeff_7 value="-0.02152428547796412"/>
        <eta_ad_isoline_coeff_8 value="3.560321089600557e-06"/>
        <eta_ad_isoline_coeff_9 value="-1.712509076336017e-10"/>
        <surgeline_coeff_1 value="0.1183704999999975"/>
        <surgeline_coeff_2 value="37.12673769825939"/>
        <surgeline_coeff_3 value="0"/>
        <chokeline_coeff_1 value="-1.74172624739939"/>
        <chokeline_coeff_2 value="1.110685078154505"/>
        <chokeline_coeff_3 value="0"/>
        <efficiencyOfChokeline value="0.6"/>
        <surgelineMeasurements>
          <measurement>
            <speed unit="per_min" value="3250"/>
            <adiabaticHead unit="kJ_per_kg" value="18.85642065000005"/>
            <volumetricFlowrate unit="m_cube_per_s" value="0.5047050000000013"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="3656.25"/>
            <adiabaticHead unit="kJ_per_kg" value="21.20364523834"/>
            <volumetricFlowrate unit="m_cube_per_s" value="0.5679269455266075"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="4062.5"/>
            <adiabaticHead unit="kJ_per_kg" value="23.54916831029519"/>
            <volumetricFlowrate unit="m_cube_per_s" value="0.6311030611071894"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="4468.75"/>
            <adiabaticHead unit="kJ_per_kg" value="25.89313187550216"/>
            <volumetricFlowrate unit="m_cube_per_s" value="0.6942371717381073"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="4875"/>
            <adiabaticHead unit="kJ_per_kg" value="28.23567708697763"/>
            <volumetricFlowrate unit="m_cube_per_s" value="0.7573330793428655"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="5281.25"/>
            <adiabaticHead unit="kJ_per_kg" value="30.57694430097455"/>
            <volumetricFlowrate unit="m_cube_per_s" value="0.8203945643843233"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="5687.5"/>
            <adiabaticHead unit="kJ_per_kg" value="32.91707313588622"/>
            <volumetricFlowrate unit="m_cube_per_s" value="0.8834253874512633"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="6093.75"/>
            <adiabaticHead unit="kJ_per_kg" value="35.25620253026083"/>
            <volumetricFlowrate unit="m_cube_per_s" value="0.9464292908209976"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="6500"/>
            <adiabaticHead unit="kJ_per_kg" value="37.5944707999999"/>
            <volumetricFlowrate unit="m_cube_per_s" value="1.009409999999997"/>
          </measurement>
        </surgelineMeasurements>
        <characteristicDiagramMeasurements>
          <adiabaticEfficiency value="0.805">
            <measurement>
              <speed unit="per_min" value="3250"/>
              <adiabaticHead unit="kJ_per_kg" value="18.47874050880534"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.189872108826158"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3656.25"/>
              <adiabaticHead unit="kJ_per_kg" value="20.7428454078107"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.328492860096451"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4062.5"/>
              <adiabaticHead unit="kJ_per_kg" value="22.99937779563791"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.466649981263309"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4468.75"/>
              <adiabaticHead unit="kJ_per_kg" value="25.24905840566725"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.604387599523611"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4875"/>
              <adiabaticHead unit="kJ_per_kg" value="27.4925885530489"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.741748653185136"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5281.25"/>
              <adiabaticHead unit="kJ_per_kg" value="29.73065192412378"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.878775001224584"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5687.5"/>
              <adiabaticHead unit="kJ_per_kg" value="31.9639162527635"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.015507525922175"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6093.75"/>
              <adiabaticHead unit="kJ_per_kg" value="34.19303489597166"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.151986229328489"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6500"/>
              <adiabaticHead unit="kJ_per_kg" value="36.41864831985979"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.288250324243948"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.8100000000000001">
            <measurement>
              <speed unit="per_min" value="3250"/>
              <adiabaticHead unit="kJ_per_kg" value="17.69524794820683"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.955611718918145"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3656.25"/>
              <adiabaticHead unit="kJ_per_kg" value="19.79918414796728"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.172246060505358"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4062.5"/>
              <adiabaticHead unit="kJ_per_kg" value="21.88661393130841"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.387180798913838"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4468.75"/>
              <adiabaticHead unit="kJ_per_kg" value="23.95939926616829"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.600607653929749"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4875"/>
              <adiabaticHead unit="kJ_per_kg" value="26.01929052015653"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.812706854276133"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5281.25"/>
              <adiabaticHead unit="kJ_per_kg" value="28.06794068406023"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.023648602153442"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5687.5"/>
              <adiabaticHead unit="kJ_per_kg" value="30.10691782993004"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.233594356001478"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6093.75"/>
              <adiabaticHead unit="kJ_per_kg" value="32.13771609549777"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.442697961523267"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6500"/>
              <adiabaticHead unit="kJ_per_kg" value="34.16176543475864"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.651106655665577"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.8149999999999999">
            <measurement>
              <speed unit="per_min" value="3250"/>
              <adiabaticHead unit="kJ_per_kg" value="16.43807704041583"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.772945366906355"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3656.25"/>
              <adiabaticHead unit="kJ_per_kg" value="18.30970078979265"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.062824444948763"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4062.5"/>
              <adiabaticHead unit="kJ_per_kg" value="20.15638249492321"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.348840472635559"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4468.75"/>
              <adiabaticHead unit="kJ_per_kg" value="21.98147835078151"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.631513261015905"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4875"/>
              <adiabaticHead unit="kJ_per_kg" value="23.78801958228993"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.911312289431537"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5281.25"/>
              <adiabaticHead unit="kJ_per_kg" value="25.57876715126331"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.18866517858649"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5687.5"/>
              <adiabaticHead unit="kJ_per_kg" value="27.35625643388405"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.463964610241982"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6093.75"/>
              <adiabaticHead unit="kJ_per_kg" value="29.12283412685547"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.737574043280725"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6500"/>
              <adiabaticHead unit="kJ_per_kg" value="30.88068907599569"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.009832488472349"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.82">
            <measurement>
              <speed unit="per_min" value="3250"/>
              <adiabaticHead unit="kJ_per_kg" value="14.71852793441202"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.602149778880675"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3656.25"/>
              <adiabaticHead unit="kJ_per_kg" value="16.31092771871224"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.954398177232253"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4062.5"/>
              <adiabaticHead unit="kJ_per_kg" value="17.87395300388914"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.300148759915563"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4468.75"/>
              <adiabaticHead unit="kJ_per_kg" value="19.41219932688279"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.640418087308639"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4875"/>
              <adiabaticHead unit="kJ_per_kg" value="20.92966661785997"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.976090967993254"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5281.25"/>
              <adiabaticHead unit="kJ_per_kg" value="22.42988174797005"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.307947567054716"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5687.5"/>
              <adiabaticHead unit="kJ_per_kg" value="23.9159926339201"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.63668422257919"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6093.75"/>
              <adiabaticHead unit="kJ_per_kg" value="25.3908417561696"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.962929708320018"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6500"/>
              <adiabaticHead unit="kJ_per_kg" value="26.85702453246482"/>
              <volumetricFlowrate unit="m_cube_per_s" value="6.287258146274194"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.7649999999999999">
            <measurement>
              <speed unit="per_min" value="3250"/>
              <adiabaticHead unit="kJ_per_kg" value="12.62769856155301"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.404898862001899"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3656.25"/>
              <adiabaticHead unit="kJ_per_kg" value="13.9268437321946"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.806214755261804"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4062.5"/>
              <adiabaticHead unit="kJ_per_kg" value="15.19706331821114"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.198595313892296"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4468.75"/>
              <adiabaticHead unit="kJ_per_kg" value="16.4434347909981"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.583609007695384"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4875"/>
              <adiabaticHead unit="kJ_per_kg" value="17.67025231835626"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.962582337993414"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5281.25"/>
              <adiabaticHead unit="kJ_per_kg" value="18.88121061272203"/>
              <volumetricFlowrate unit="m_cube_per_s" value="6.336656629755502"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5687.5"/>
              <adiabaticHead unit="kJ_per_kg" value="20.07953959719101"/>
              <volumetricFlowrate unit="m_cube_per_s" value="6.706829630963599"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6093.75"/>
              <adiabaticHead unit="kJ_per_kg" value="21.26810531704277"/>
              <volumetricFlowrate unit="m_cube_per_s" value="7.073986684955374"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6500"/>
              <adiabaticHead unit="kJ_per_kg" value="22.44948715317802"/>
              <volumetricFlowrate unit="m_cube_per_s" value="7.438924582246329"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.71">
            <measurement>
              <speed unit="per_min" value="3250"/>
              <adiabaticHead unit="kJ_per_kg" value="10.29845520599619"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.154000374618079"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3656.25"/>
              <adiabaticHead unit="kJ_per_kg" value="11.31638567601492"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.592022032520605"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4062.5"/>
              <adiabaticHead unit="kJ_per_kg" value="12.30930793658383"/>
              <volumetricFlowrate unit="m_cube_per_s" value="6.019282506150716"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4468.75"/>
              <adiabaticHead unit="kJ_per_kg" value="13.28199766388416"/>
              <volumetricFlowrate unit="m_cube_per_s" value="6.437836797947297"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4875"/>
              <adiabaticHead unit="kJ_per_kg" value="14.23841549073127"/>
              <volumetricFlowrate unit="m_cube_per_s" value="6.849389192243342"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5281.25"/>
              <adiabaticHead unit="kJ_per_kg" value="15.18191466967768"/>
              <volumetricFlowrate unit="m_cube_per_s" value="7.255382613959243"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5687.5"/>
              <adiabaticHead unit="kJ_per_kg" value="16.11538831719182"/>
              <volumetricFlowrate unit="m_cube_per_s" value="7.657061988666383"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6093.75"/>
              <adiabaticHead unit="kJ_per_kg" value="17.04137669519887"/>
              <volumetricFlowrate unit="m_cube_per_s" value="8.055520406485096"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6500"/>
              <adiabaticHead unit="kJ_per_kg" value="17.96214732062452"/>
              <volumetricFlowrate unit="m_cube_per_s" value="8.451733593707472"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.655">
            <measurement>
              <speed unit="per_min" value="3250"/>
              <adiabaticHead unit="kJ_per_kg" value="7.861274117948462"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.835762942287306"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3656.25"/>
              <adiabaticHead unit="kJ_per_kg" value="8.624057573575545"/>
              <volumetricFlowrate unit="m_cube_per_s" value="6.300633497097484"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4062.5"/>
              <adiabaticHead unit="kJ_per_kg" value="9.367304070147638"/>
              <volumetricFlowrate unit="m_cube_per_s" value="6.753597452559972"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4468.75"/>
              <adiabaticHead unit="kJ_per_kg" value="10.09498336132935"/>
              <volumetricFlowrate unit="m_cube_per_s" value="7.19707413433648"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4875"/>
              <adiabaticHead unit="kJ_per_kg" value="10.81034875580966"/>
              <volumetricFlowrate unit="m_cube_per_s" value="7.633046238045356"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5281.25"/>
              <adiabaticHead unit="kJ_per_kg" value="11.51612895856871"/>
              <volumetricFlowrate unit="m_cube_per_s" value="8.063176744954308"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5687.5"/>
              <adiabaticHead unit="kJ_per_kg" value="12.21466132560324"/>
              <volumetricFlowrate unit="m_cube_per_s" value="8.488890132706336"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6093.75"/>
              <adiabaticHead unit="kJ_per_kg" value="12.9079872741207"/>
              <volumetricFlowrate unit="m_cube_per_s" value="8.911430522084128"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6500"/>
              <adiabaticHead unit="kJ_per_kg" value="13.59792247968512"/>
              <volumetricFlowrate unit="m_cube_per_s" value="9.331904457940711"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.6">
            <measurement>
              <speed unit="per_min" value="3250"/>
              <adiabaticHead unit="kJ_per_kg" value="5.41891598571661"/>
              <volumetricFlowrate unit="m_cube_per_s" value="6.447049999999998"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3656.25"/>
              <adiabaticHead unit="kJ_per_kg" value="5.957019550656375"/>
              <volumetricFlowrate unit="m_cube_per_s" value="6.931528972053777"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4062.5"/>
              <adiabaticHead unit="kJ_per_kg" value="6.481247223724054"/>
              <volumetricFlowrate unit="m_cube_per_s" value="7.4035148512003"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4468.75"/>
              <adiabaticHead unit="kJ_per_kg" value="6.994555542189884"/>
              <volumetricFlowrate unit="m_cube_per_s" value="7.865669541635805"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4875"/>
              <adiabaticHead unit="kJ_per_kg" value="7.499352132734264"/>
              <volumetricFlowrate unit="m_cube_per_s" value="8.320160738531277"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5281.25"/>
              <adiabaticHead unit="kJ_per_kg" value="7.997647081004839"/>
              <volumetricFlowrate unit="m_cube_per_s" value="8.768798212889473"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5687.5"/>
              <adiabaticHead unit="kJ_per_kg" value="8.491156814948425"/>
              <volumetricFlowrate unit="m_cube_per_s" value="9.21312734240618"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6093.75"/>
              <adiabaticHead unit="kJ_per_kg" value="8.981377745102456"/>
              <volumetricFlowrate unit="m_cube_per_s" value="9.654495413154526"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6500"/>
              <adiabaticHead unit="kJ_per_kg" value="9.469639999999998"/>
              <volumetricFlowrate unit="m_cube_per_s" value="10.0941"/>
            </measurement>
          </adiabaticEfficiency>
        </characteristicDiagramMeasurements>
      </turboCompressor>
    </compressors>
    <drives>
      <gasTurbine id="drive_16">
        <energy_rate_fun_coeff_1 value="0.01"/>
        <energy_rate_fun_coeff_2 value="0"/>
        <energy_rate_fun_coeff_3 value="0"/>
        <power_fun_coeff_1 value="-1474.507009429534"/>
        <power_fun_coeff_2 value="4.7785116089535"/>
        <power_fun_coeff_3 value="-0.0002898760489162038"/>
        <power_fun_coeff_4 value="8.870044352872641"/>
        <power_fun_coeff_5 value="-0.02874561439252346"/>
        <power_fun_coeff_6 value="1.743778357294465e-06"/>
        <power_fun_coeff_7 value="-0.02948108904767908"/>
        <power_fun_coeff_8 value="9.554089967563408e-05"/>
        <power_fun_coeff_9 value="-5.795741597860734e-09"/>
      </gasTurbine>
    </drives>
    <configurations>
      <configuration nrOfSerialStages="1" confId="config_1">
        <stage nrOfParallelUnits="1" stageNr="1">
          <compressor nominalSpeed="3575" id="compressor_16"/>
        </stage>
      </configuration>
    </configurations>
  </compressorStation>
  <compressorStation id="compressorStation_9">
    <compressors>
      <turboCompressor drive="drive_17" id="compressor_17">
        <speedMin unit="per_min" value="3000"/>
        <speedMax unit="per_min" value="5200"/>
        <n_isoline_coeff_1 value="8.25676074787"/>
        <n_isoline_coeff_2 value="-0.00414695552593"/>
        <n_isoline_coeff_3 value="1.43831752662e-06"/>
        <n_isoline_coeff_4 value="-3.24678879644"/>
        <n_isoline_coeff_5 value="0.00241300524772"/>
        <n_isoline_coeff_6 value="-1.43922188229e-07"/>
        <n_isoline_coeff_7 value="-0.180099687128"/>
        <n_isoline_coeff_8 value="-0.00016220388004"/>
        <n_isoline_coeff_9 value="1.62105762322e-08"/>
        <eta_ad_isoline_coeff_1 value="1.76575734526"/>
        <eta_ad_isoline_coeff_2 value="-0.00073228674697"/>
        <eta_ad_isoline_coeff_3 value="6.91713662069e-08"/>
        <eta_ad_isoline_coeff_4 value="0.00555391782987"/>
        <eta_ad_isoline_coeff_5 value="0.000179359512019"/>
        <eta_ad_isoline_coeff_6 value="-2.42843175563e-08"/>
        <eta_ad_isoline_coeff_7 value="-0.0701881280272"/>
        <eta_ad_isoline_coeff_8 value="1.01366056093e-05"/>
        <eta_ad_isoline_coeff_9 value="-7.34372377207e-11"/>
        <surgeline_coeff_1 value="2.17951957895"/>
        <surgeline_coeff_2 value="-1.64578704068"/>
        <surgeline_coeff_3 value="1.51223143938"/>
        <chokeline_coeff_1 value="-11.8414577545"/>
        <chokeline_coeff_2 value="2.94121421541"/>
        <chokeline_coeff_3 value="0.0350822825348"/>
        <efficiencyOfChokeline value="0.7"/>
        <surgelineMeasurements>
          <measurement>
            <speed unit="per_min" value="3000"/>
            <adiabaticHead unit="kJ_per_kg" value="12.2"/>
            <volumetricFlowrate unit="m_cube_per_s" value="3.18"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="3500"/>
            <adiabaticHead unit="kJ_per_kg" value="16.7"/>
            <volumetricFlowrate unit="m_cube_per_s" value="3.68"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="4000"/>
            <adiabaticHead unit="kJ_per_kg" value="22.1"/>
            <volumetricFlowrate unit="m_cube_per_s" value="4.22"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="4500"/>
            <adiabaticHead unit="kJ_per_kg" value="28.2"/>
            <volumetricFlowrate unit="m_cube_per_s" value="4.73"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="5000"/>
            <adiabaticHead unit="kJ_per_kg" value="35"/>
            <volumetricFlowrate unit="m_cube_per_s" value="5.23"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="5200"/>
            <adiabaticHead unit="kJ_per_kg" value="37.8"/>
            <volumetricFlowrate unit="m_cube_per_s" value="5.43"/>
          </measurement>
        </surgelineMeasurements>
        <characteristicDiagramMeasurements>
          <adiabaticEfficiency value="0.83">
            <measurement>
              <speed unit="per_min" value="3000"/>
              <adiabaticHead unit="kJ_per_kg" value="11.9"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.47"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3500"/>
              <adiabaticHead unit="kJ_per_kg" value="16.2"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.04"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4000"/>
              <adiabaticHead unit="kJ_per_kg" value="21.6"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.62"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4500"/>
              <adiabaticHead unit="kJ_per_kg" value="27.6"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.18"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5000"/>
              <adiabaticHead unit="kJ_per_kg" value="34.1"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.77"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5200"/>
              <adiabaticHead unit="kJ_per_kg" value="36.9"/>
              <volumetricFlowrate unit="m_cube_per_s" value="6"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.84">
            <measurement>
              <speed unit="per_min" value="3000"/>
              <adiabaticHead unit="kJ_per_kg" value="10.8"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.25"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3500"/>
              <adiabaticHead unit="kJ_per_kg" value="14.7"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.93"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4000"/>
              <adiabaticHead unit="kJ_per_kg" value="19.8"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.62"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4500"/>
              <adiabaticHead unit="kJ_per_kg" value="25.1"/>
              <volumetricFlowrate unit="m_cube_per_s" value="6.32"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5000"/>
              <adiabaticHead unit="kJ_per_kg" value="31.2"/>
              <volumetricFlowrate unit="m_cube_per_s" value="7.02"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5200"/>
              <adiabaticHead unit="kJ_per_kg" value="33.7"/>
              <volumetricFlowrate unit="m_cube_per_s" value="7.32"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.82">
            <measurement>
              <speed unit="per_min" value="3000"/>
              <adiabaticHead unit="kJ_per_kg" value="9.3"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.99"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3500"/>
              <adiabaticHead unit="kJ_per_kg" value="12.7"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.8"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4000"/>
              <adiabaticHead unit="kJ_per_kg" value="17.1"/>
              <volumetricFlowrate unit="m_cube_per_s" value="6.6"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4500"/>
              <adiabaticHead unit="kJ_per_kg" value="21.4"/>
              <volumetricFlowrate unit="m_cube_per_s" value="7.44"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5000"/>
              <adiabaticHead unit="kJ_per_kg" value="26.7"/>
              <volumetricFlowrate unit="m_cube_per_s" value="8.29"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5200"/>
              <adiabaticHead unit="kJ_per_kg" value="28.8"/>
              <volumetricFlowrate unit="m_cube_per_s" value="8.63"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.7">
            <measurement>
              <speed unit="per_min" value="3000"/>
              <adiabaticHead unit="kJ_per_kg" value="7.1"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.76"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3500"/>
              <adiabaticHead unit="kJ_per_kg" value="9.7"/>
              <volumetricFlowrate unit="m_cube_per_s" value="6.72"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4000"/>
              <adiabaticHead unit="kJ_per_kg" value="12.6"/>
              <volumetricFlowrate unit="m_cube_per_s" value="7.65"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4500"/>
              <adiabaticHead unit="kJ_per_kg" value="16"/>
              <volumetricFlowrate unit="m_cube_per_s" value="8.62"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5000"/>
              <adiabaticHead unit="kJ_per_kg" value="19.8"/>
              <volumetricFlowrate unit="m_cube_per_s" value="9.57"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5200"/>
              <adiabaticHead unit="kJ_per_kg" value="21.3"/>
              <volumetricFlowrate unit="m_cube_per_s" value="9.96"/>
            </measurement>
          </adiabaticEfficiency>
        </characteristicDiagramMeasurements>
      </turboCompressor>
      <turboCompressor drive="drive_18" id="compressor_18">
        <speedMin unit="per_min" value="3200"/>
        <speedMax unit="per_min" value="5200"/>
        <n_isoline_coeff_1 value="0"/>
        <n_isoline_coeff_2 value="0.006818215384615385"/>
        <n_isoline_coeff_3 value="0"/>
        <n_isoline_coeff_4 value="0"/>
        <n_isoline_coeff_5 value="0"/>
        <n_isoline_coeff_6 value="0"/>
        <n_isoline_coeff_7 value="-0.2895346713994936"/>
        <n_isoline_coeff_8 value="1.391993612497565e-05"/>
        <n_isoline_coeff_9 value="0"/>
        <eta_ad_isoline_coeff_1 value="0.8402199449429988"/>
        <eta_ad_isoline_coeff_2 value="-9.332681566802747e-06"/>
        <eta_ad_isoline_coeff_3 value="6.683041246378517e-10"/>
        <eta_ad_isoline_coeff_4 value="0.01339321086624312"/>
        <eta_ad_isoline_coeff_5 value="1.926379309832219e-06"/>
        <eta_ad_isoline_coeff_6 value="-3.074377386911282e-10"/>
        <eta_ad_isoline_coeff_7 value="-0.005618463249999764"/>
        <eta_ad_isoline_coeff_8 value="1.102135172660098e-06"/>
        <eta_ad_isoline_coeff_9 value="-6.910665924085718e-11"/>
        <surgeline_coeff_1 value="8.297768123076928"/>
        <surgeline_coeff_2 value="24.30081735504846"/>
        <surgeline_coeff_3 value="0"/>
        <chokeline_coeff_1 value="-6.459243060516478"/>
        <chokeline_coeff_2 value="1.384697409204536"/>
        <chokeline_coeff_3 value="0"/>
        <efficiencyOfChokeline value="0.76"/>
        <surgelineMeasurements>
          <measurement>
            <speed unit="per_min" value="3200"/>
            <adiabaticHead unit="kJ_per_kg" value="21.74328886153832"/>
            <volumetricFlowrate unit="m_cube_per_s" value="0.5532949999999941"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="3450"/>
            <adiabaticHead unit="kJ_per_kg" value="23.42920440068414"/>
            <volumetricFlowrate unit="m_cube_per_s" value="0.6226719067317165"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="3700"/>
            <adiabaticHead unit="kJ_per_kg" value="25.11341946209394"/>
            <volumetricFlowrate unit="m_cube_per_s" value="0.6919788373095026"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="3950"/>
            <adiabaticHead unit="kJ_per_kg" value="26.79603881849965"/>
            <volumetricFlowrate unit="m_cube_per_s" value="0.7612201032233896"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="4200"/>
            <adiabaticHead unit="kJ_per_kg" value="28.47716638439474"/>
            <volumetricFlowrate unit="m_cube_per_s" value="0.8303999806461476"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="4450"/>
            <adiabaticHead unit="kJ_per_kg" value="30.15690526304824"/>
            <volumetricFlowrate unit="m_cube_per_s" value="0.8995227123679488"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="4700"/>
            <adiabaticHead unit="kJ_per_kg" value="31.83535779253243"/>
            <volumetricFlowrate unit="m_cube_per_s" value="0.9685925096904447"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="4950"/>
            <adiabaticHead unit="kJ_per_kg" value="33.51262559081904"/>
            <volumetricFlowrate unit="m_cube_per_s" value="1.037613554282518"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="5200"/>
            <adiabaticHead unit="kJ_per_kg" value="35.18880959999989"/>
            <volumetricFlowrate unit="m_cube_per_s" value="1.106589999999995"/>
          </measurement>
        </surgelineMeasurements>
        <characteristicDiagramMeasurements>
          <adiabaticEfficiency value="0.8325">
            <measurement>
              <speed unit="per_min" value="3200"/>
              <adiabaticHead unit="kJ_per_kg" value="21.23878624226295"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.537987780196777"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3450"/>
              <adiabaticHead unit="kJ_per_kg" value="22.85619106759869"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.661426890979794"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3700"/>
              <adiabaticHead unit="kJ_per_kg" value="24.4693650955215"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.784543110509877"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3950"/>
              <adiabaticHead unit="kJ_per_kg" value="26.0786472465478"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.907362304944042"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4200"/>
              <adiabaticHead unit="kJ_per_kg" value="27.6843690232527"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.029909774307646"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4450"/>
              <adiabaticHead unit="kJ_per_kg" value="29.28685507134396"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.152210295315128"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4700"/>
              <adiabaticHead unit="kJ_per_kg" value="30.88642371143978"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.27428816195488"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4950"/>
              <adiabaticHead unit="kJ_per_kg" value="32.48338744417218"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.39616722403836"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5200"/>
              <adiabaticHead unit="kJ_per_kg" value="34.07805343102293"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.517870923897124"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.835">
            <measurement>
              <speed unit="per_min" value="3200"/>
              <adiabaticHead unit="kJ_per_kg" value="20.1615942399837"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.600436926484174"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3450"/>
              <adiabaticHead unit="kJ_per_kg" value="21.66016834464754"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.777155200626876"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3700"/>
              <adiabaticHead unit="kJ_per_kg" value="23.15166329523739"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.953038670613782"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3950"/>
              <adiabaticHead unit="kJ_per_kg" value="24.63676723121634"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.128168484796449"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4200"/>
              <adiabaticHead unit="kJ_per_kg" value="26.11614090691253"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.302622562154087"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4450"/>
              <adiabaticHead unit="kJ_per_kg" value="27.59042039846444"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.476475911508124"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4700"/>
              <adiabaticHead unit="kJ_per_kg" value="29.06021957214728"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.649800922597829"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4950"/>
              <adiabaticHead unit="kJ_per_kg" value="30.52613234387023"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.822667632529893"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5200"/>
              <adiabaticHead unit="kJ_per_kg" value="31.98873475572899"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.995143970654404"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.8374999999999999">
            <measurement>
              <speed unit="per_min" value="3200"/>
              <adiabaticHead unit="kJ_per_kg" value="18.47725691902634"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.692881592558326"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3450"/>
              <adiabaticHead unit="kJ_per_kg" value="19.81607424930029"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.91768388609311"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3700"/>
              <adiabaticHead unit="kJ_per_kg" value="21.14576309651531"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.140953405976303"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3950"/>
              <adiabaticHead unit="kJ_per_kg" value="22.46736856316874"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.362865636520112"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4200"/>
              <adiabaticHead unit="kJ_per_kg" value="23.78187523333695"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.583585900321988"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4450"/>
              <adiabaticHead unit="kJ_per_kg" value="25.0902145641702"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.803270599378653"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4700"/>
              <adiabaticHead unit="kJ_per_kg" value="26.39327137939359"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.02206830541702"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4950"/>
              <adiabaticHead unit="kJ_per_kg" value="27.69188960774816"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.240120723442152"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5200"/>
              <adiabaticHead unit="kJ_per_kg" value="28.9868773844526"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.457563548329324"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.84">
            <measurement>
              <speed unit="per_min" value="3200"/>
              <adiabaticHead unit="kJ_per_kg" value="16.25687514569893"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.764503618462585"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3450"/>
              <adiabaticHead unit="kJ_per_kg" value="17.41360171727943"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.029505424273738"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3700"/>
              <adiabaticHead unit="kJ_per_kg" value="18.56058530649537"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.292275148637096"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3950"/>
              <adiabaticHead unit="kJ_per_kg" value="19.69910663762061"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.553106200776289"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4200"/>
              <adiabaticHead unit="kJ_per_kg" value="20.83035303579205"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.812270592515977"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4450"/>
              <adiabaticHead unit="kJ_per_kg" value="21.95543172000433"/>
              <volumetricFlowrate unit="m_cube_per_s" value="6.070021983658062"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4700"/>
              <adiabaticHead unit="kJ_per_kg" value="23.07538112717908"/>
              <volumetricFlowrate unit="m_cube_per_s" value="6.326598276284347"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4950"/>
              <adiabaticHead unit="kJ_per_kg" value="24.19118063661507"/>
              <volumetricFlowrate unit="m_cube_per_s" value="6.582223842592311"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5200"/>
              <adiabaticHead unit="kJ_per_kg" value="25.30375898754935"/>
              <volumetricFlowrate unit="m_cube_per_s" value="6.837111453327428"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.82">
            <measurement>
              <speed unit="per_min" value="3200"/>
              <adiabaticHead unit="kJ_per_kg" value="13.64663846897844"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.775371743050683"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3450"/>
              <adiabaticHead unit="kJ_per_kg" value="14.61776450010044"/>
              <volumetricFlowrate unit="m_cube_per_s" value="6.07226221536299"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3700"/>
              <adiabaticHead unit="kJ_per_kg" value="15.5798180162464"/>
              <volumetricFlowrate unit="m_cube_per_s" value="6.366379058743549"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3950"/>
              <adiabaticHead unit="kJ_per_kg" value="16.53413913235483"/>
              <volumetricFlowrate unit="m_cube_per_s" value="6.658131970125913"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4200"/>
              <adiabaticHead unit="kJ_per_kg" value="17.48195599866138"/>
              <volumetricFlowrate unit="m_cube_per_s" value="6.947896416845779"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4450"/>
              <adiabaticHead unit="kJ_per_kg" value="18.42440248729732"/>
              <volumetricFlowrate unit="m_cube_per_s" value="7.236019043748209"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4700"/>
              <adiabaticHead unit="kJ_per_kg" value="19.3625329231213"/>
              <volumetricFlowrate unit="m_cube_per_s" value="7.52282217666448"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4950"/>
              <adiabaticHead unit="kJ_per_kg" value="20.29733447486206"/>
              <volumetricFlowrate unit="m_cube_per_s" value="7.808607610604443"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5200"/>
              <adiabaticHead unit="kJ_per_kg" value="21.22973768027627"/>
              <volumetricFlowrate unit="m_cube_per_s" value="8.093659827484169"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.8">
            <measurement>
              <speed unit="per_min" value="3200"/>
              <adiabaticHead unit="kJ_per_kg" value="10.81257863924248"/>
              <volumetricFlowrate unit="m_cube_per_s" value="6.702457812194872"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3450"/>
              <adiabaticHead unit="kJ_per_kg" value="11.60754981291373"/>
              <volumetricFlowrate unit="m_cube_per_s" value="7.023991982137772"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3700"/>
              <adiabaticHead unit="kJ_per_kg" value="12.39485786276687"/>
              <volumetricFlowrate unit="m_cube_per_s" value="7.34242672377732"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3950"/>
              <adiabaticHead unit="kJ_per_kg" value="13.1757552841201"/>
              <volumetricFlowrate unit="m_cube_per_s" value="7.658268621573218"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4200"/>
              <adiabaticHead unit="kJ_per_kg" value="13.95138178477154"/>
              <volumetricFlowrate unit="m_cube_per_s" value="7.971978641926495"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4450"/>
              <adiabaticHead unit="kJ_per_kg" value="14.72278337917889"/>
              <volumetricFlowrate unit="m_cube_per_s" value="8.283979856014501"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4700"/>
              <adiabaticHead unit="kJ_per_kg" value="15.49092805448755"/>
              <volumetricFlowrate unit="m_cube_per_s" value="8.594663776075185"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4950"/>
              <adiabaticHead unit="kJ_per_kg" value="16.25671877146567"/>
              <volumetricFlowrate unit="m_cube_per_s" value="8.904395613767406"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5200"/>
              <adiabaticHead unit="kJ_per_kg" value="17.02100437513671"/>
              <volumetricFlowrate unit="m_cube_per_s" value="9.213518693087137"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.78">
            <measurement>
              <speed unit="per_min" value="3200"/>
              <adiabaticHead unit="kJ_per_kg" value="7.898608879863422"/>
              <volumetricFlowrate unit="m_cube_per_s" value="7.537714362026844"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3450"/>
              <adiabaticHead unit="kJ_per_kg" value="8.533225497131424"/>
              <volumetricFlowrate unit="m_cube_per_s" value="7.878198439155946"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3700"/>
              <adiabaticHead unit="kJ_per_kg" value="9.161821159071891"/>
              <volumetricFlowrate unit="m_cube_per_s" value="8.21545215741585"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3950"/>
              <adiabaticHead unit="kJ_per_kg" value="9.785474462481751"/>
              <volumetricFlowrate unit="m_cube_per_s" value="8.550054204828591"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4200"/>
              <adiabaticHead unit="kJ_per_kg" value="10.40516329612586"/>
              <volumetricFlowrate unit="m_cube_per_s" value="8.882529237611129"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4450"/>
              <adiabaticHead unit="kJ_per_kg" value="11.02178269319135"/>
              <volumetricFlowrate unit="m_cube_per_s" value="9.213357458362058"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4700"/>
              <adiabaticHead unit="kJ_per_kg" value="11.63615934468043"/>
              <volumetricFlowrate unit="m_cube_per_s" value="9.542982402777259"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4950"/>
              <adiabaticHead unit="kJ_per_kg" value="12.24906354735529"/>
              <volumetricFlowrate unit="m_cube_per_s" value="9.871817349953199"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5200"/>
              <adiabaticHead unit="kJ_per_kg" value="12.86121916147787"/>
              <volumetricFlowrate unit="m_cube_per_s" value="10.20025066490673"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.76">
            <measurement>
              <speed unit="per_min" value="3200"/>
              <adiabaticHead unit="kJ_per_kg" value="5.010136345054238"/>
              <volumetricFlowrate unit="m_cube_per_s" value="8.282950000000001"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3450"/>
              <adiabaticHead unit="kJ_per_kg" value="5.501953589902873"/>
              <volumetricFlowrate unit="m_cube_per_s" value="8.638130302627395"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3700"/>
              <adiabaticHead unit="kJ_per_kg" value="5.98931584274015"/>
              <volumetricFlowrate unit="m_cube_per_s" value="8.990093301617371"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3950"/>
              <adiabaticHead unit="kJ_per_kg" value="6.473093355044683"/>
              <volumetricFlowrate unit="m_cube_per_s" value="9.339467474695695"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4200"/>
              <adiabaticHead unit="kJ_per_kg" value="6.954074155876255"/>
              <volumetricFlowrate unit="m_cube_per_s" value="9.686821920247723"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4450"/>
              <adiabaticHead unit="kJ_per_kg" value="7.432979090486563"/>
              <volumetricFlowrate unit="m_cube_per_s" value="10.03267721789389"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4700"/>
              <adiabaticHead unit="kJ_per_kg" value="7.910473984604852"/>
              <volumetricFlowrate unit="m_cube_per_s" value="10.37751421328669"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4950"/>
              <adiabaticHead unit="kJ_per_kg" value="8.387179616478328"/>
              <volumetricFlowrate unit="m_cube_per_s" value="10.72178121971326"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5200"/>
              <adiabaticHead unit="kJ_per_kg" value="8.863679999999999"/>
              <volumetricFlowrate unit="m_cube_per_s" value="11.0659"/>
            </measurement>
          </adiabaticEfficiency>
        </characteristicDiagramMeasurements>
      </turboCompressor>
    </compressors>
    <drives>
      <gasTurbine id="drive_17">
        <energy_rate_fun_coeff_1 value="10899.0775876"/>
        <energy_rate_fun_coeff_2 value="2.84512681206"/>
        <energy_rate_fun_coeff_3 value="-1.61964766054e-19"/>
        <power_fun_coeff_1 value="4482.26525722"/>
        <power_fun_coeff_2 value="2.75499508123"/>
        <power_fun_coeff_3 value="-0.000265650722022"/>
        <power_fun_coeff_4 value="-31.9514364949"/>
        <power_fun_coeff_5 value="-0.0197601378405"/>
        <power_fun_coeff_6 value="1.90728585494e-06"/>
        <power_fun_coeff_7 value="-0.00443674105651"/>
        <power_fun_coeff_8 value="2.96734492932e-06"/>
        <power_fun_coeff_9 value="-4.1680341318e-10"/>
        <specificEnergyConsumptionMeasurements>
          <measurement>
            <compressorPower unit="kW" value="10187"/>
            <fuelConsumption unit="kW" value="39882"/>
          </measurement>
          <measurement>
            <compressorPower unit="kW" value="7640"/>
            <fuelConsumption unit="kW" value="32637"/>
          </measurement>
          <measurement>
            <compressorPower unit="kW" value="5094"/>
            <fuelConsumption unit="kW" value="25391"/>
          </measurement>
          <measurement>
            <compressorPower unit="kW" value="2547"/>
            <fuelConsumption unit="kW" value="18146"/>
          </measurement>
        </specificEnergyConsumptionMeasurements>
        <maximalPowerMeasurements>
          <ambientTemperature unit="Celsius" value="-5">
            <measurement>
              <speed unit="per_min" value="3000"/>
              <maximalPower unit="kW" value="10711"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3500"/>
              <maximalPower unit="kW" value="11287"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4000"/>
              <maximalPower unit="kW" value="11660"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4500"/>
              <maximalPower unit="kW" value="11887"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5000"/>
              <maximalPower unit="kW" value="12020"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5200"/>
              <maximalPower unit="kW" value="12059"/>
            </measurement>
          </ambientTemperature>
          <ambientTemperature unit="Celsius" value="5">
            <measurement>
              <speed unit="per_min" value="3000"/>
              <maximalPower unit="kW" value="9972"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3500"/>
              <maximalPower unit="kW" value="10507"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4000"/>
              <maximalPower unit="kW" value="10855"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4500"/>
              <maximalPower unit="kW" value="11066"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5000"/>
              <maximalPower unit="kW" value="11190"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5200"/>
              <maximalPower unit="kW" value="11226"/>
            </measurement>
          </ambientTemperature>
          <ambientTemperature unit="Celsius" value="15">
            <measurement>
              <speed unit="per_min" value="3000"/>
              <maximalPower unit="kW" value="9232"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3500"/>
              <maximalPower unit="kW" value="9728"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4000"/>
              <maximalPower unit="kW" value="10050"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4500"/>
              <maximalPower unit="kW" value="10246"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5000"/>
              <maximalPower unit="kW" value="10360"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5200"/>
              <maximalPower unit="kW" value="10394"/>
            </measurement>
          </ambientTemperature>
          <ambientTemperature unit="Celsius" value="25">
            <measurement>
              <speed unit="per_min" value="3000"/>
              <maximalPower unit="kW" value="8493"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3500"/>
              <maximalPower unit="kW" value="8949"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4000"/>
              <maximalPower unit="kW" value="9245"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4500"/>
              <maximalPower unit="kW" value="9425"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5000"/>
              <maximalPower unit="kW" value="9530"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5200"/>
              <maximalPower unit="kW" value="9561"/>
            </measurement>
          </ambientTemperature>
        </maximalPowerMeasurements>
      </gasTurbine>
      <gasTurbine id="drive_18">
        <energy_rate_fun_coeff_1 value="0.01"/>
        <energy_rate_fun_coeff_2 value="0"/>
        <energy_rate_fun_coeff_3 value="0"/>
        <power_fun_coeff_1 value="-1609.845977268487"/>
        <power_fun_coeff_2 value="6.521389557500937"/>
        <power_fun_coeff_3 value="-0.000494504040449993"/>
        <power_fun_coeff_4 value="9.684189446606691"/>
        <power_fun_coeff_5 value="-0.03923007096437828"/>
        <power_fun_coeff_6 value="2.974738501353854e-06"/>
        <power_fun_coeff_7 value="-0.03218703763725195"/>
        <power_fun_coeff_8 value="0.0001303877601325689"/>
        <power_fun_coeff_9 value="-9.887045336314517e-09"/>
      </gasTurbine>
    </drives>
    <configurations>
      <configuration nrOfSerialStages="1" confId="config_1">
        <stage nrOfParallelUnits="1" stageNr="1">
          <compressor nominalSpeed="3200" id="compressor_18"/>
        </stage>
      </configuration>
      <configuration nrOfSerialStages="1" confId="config_2">
        <stage nrOfParallelUnits="1" stageNr="1">
          <compressor nominalSpeed="3200" id="compressor_17"/>
        </stage>
      </configuration>
      <configuration nrOfSerialStages="2" confId="config_3">
        <stage nrOfParallelUnits="1" stageNr="1">
          <compressor nominalSpeed="3200" id="compressor_18"/>
        </stage>
        <stage nrOfParallelUnits="1" stageNr="2">
          <compressor nominalSpeed="3200" id="compressor_17"/>
        </stage>
      </configuration>
    </configurations>
  </compressorStation>
  <compressorStation id="compressorStation_4">
    <compressors>
      <turboCompressor drive="drive_19" id="compressor_19">
        <speedMin unit="per_min" value="3000"/>
        <speedMax unit="per_min" value="5200"/>
        <n_isoline_coeff_1 value="0"/>
        <n_isoline_coeff_2 value="0.004631925"/>
        <n_isoline_coeff_3 value="0"/>
        <n_isoline_coeff_4 value="0"/>
        <n_isoline_coeff_5 value="0"/>
        <n_isoline_coeff_6 value="0"/>
        <n_isoline_coeff_7 value="-0.1162846959477519"/>
        <n_isoline_coeff_8 value="5.590610382103455e-06"/>
        <n_isoline_coeff_9 value="0"/>
        <eta_ad_isoline_coeff_1 value="0.8606685888002635"/>
        <eta_ad_isoline_coeff_2 value="-3.128861765821441e-05"/>
        <eta_ad_isoline_coeff_3 value="2.747117912453289e-09"/>
        <eta_ad_isoline_coeff_4 value="0.01091887969753493"/>
        <eta_ad_isoline_coeff_5 value="9.724011606132598e-06"/>
        <eta_ad_isoline_coeff_6 value="-1.297384277595773e-09"/>
        <eta_ad_isoline_coeff_7 value="-0.009490669812112277"/>
        <eta_ad_isoline_coeff_8 value="1.941519504746482e-06"/>
        <eta_ad_isoline_coeff_9 value="-1.198164155670792e-10"/>
        <surgeline_coeff_1 value="3.783124743750001"/>
        <surgeline_coeff_2 value="13.9815454288841"/>
        <surgeline_coeff_3 value="0"/>
        <chokeline_coeff_1 value="-0.3549701008899033"/>
        <chokeline_coeff_2 value="0.4430567399173085"/>
        <chokeline_coeff_3 value="0"/>
        <efficiencyOfChokeline value="0.6"/>
        <surgelineMeasurements>
          <measurement>
            <speed unit="per_min" value="3000"/>
            <adiabaticHead unit="kJ_per_kg" value="13.84424483437503"/>
            <volumetricFlowrate unit="m_cube_per_s" value="0.7196000000000018"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="3275"/>
            <adiabaticHead unit="kJ_per_kg" value="15.10530527509204"/>
            <volumetricFlowrate unit="m_cube_per_s" value="0.8097946388638734"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="3550"/>
            <adiabaticHead unit="kJ_per_kg" value="16.36523484723462"/>
            <volumetricFlowrate unit="m_cube_per_s" value="0.8999083947824237"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="3825"/>
            <adiabaticHead unit="kJ_per_kg" value="17.62411103035944"/>
            <volumetricFlowrate unit="m_cube_per_s" value="0.9899468093144925"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="4100"/>
            <adiabaticHead unit="kJ_per_kg" value="18.88201073475536"/>
            <volumetricFlowrate unit="m_cube_per_s" value="1.079915383303263"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="4375"/>
            <adiabaticHead unit="kJ_per_kg" value="20.13901033530701"/>
            <volumetricFlowrate unit="m_cube_per_s" value="1.169819579298281"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="4650"/>
            <adiabaticHead unit="kJ_per_kg" value="21.39518570471023"/>
            <volumetricFlowrate unit="m_cube_per_s" value="1.259664823931118"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="4925"/>
            <adiabaticHead unit="kJ_per_kg" value="22.65061224608117"/>
            <volumetricFlowrate unit="m_cube_per_s" value="1.349456510247667"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="5200"/>
            <adiabaticHead unit="kJ_per_kg" value="23.90536492499993"/>
            <volumetricFlowrate unit="m_cube_per_s" value="1.439199999999995"/>
          </measurement>
        </surgelineMeasurements>
        <characteristicDiagramMeasurements>
          <adiabaticEfficiency value="0.82">
            <measurement>
              <speed unit="per_min" value="3000"/>
              <adiabaticHead unit="kJ_per_kg" value="13.56334664267137"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.827718960976833"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3275"/>
              <adiabaticHead unit="kJ_per_kg" value="14.77318265628703"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.011373404049605"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3550"/>
              <adiabaticHead unit="kJ_per_kg" value="15.97894302133754"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.194409159168829"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3825"/>
              <adiabaticHead unit="kJ_per_kg" value="17.18096755446038"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.376877810875384"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4100"/>
              <adiabaticHead unit="kJ_per_kg" value="18.37958684899313"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.558829543603041"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4375"/>
              <adiabaticHead unit="kJ_per_kg" value="19.57512304062709"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.740313257905521"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4650"/>
              <adiabaticHead unit="kJ_per_kg" value="20.76789052500844"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.921376679389152"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4925"/>
              <adiabaticHead unit="kJ_per_kg" value="21.95819663212617"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.102066461085692"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5200"/>
              <adiabaticHead unit="kJ_per_kg" value="23.14634226185605"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.282428279928611"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.82">
            <measurement>
              <speed unit="per_min" value="3000"/>
              <adiabaticHead unit="kJ_per_kg" value="12.96440362720219"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.059298318705278"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3275"/>
              <adiabaticHead unit="kJ_per_kg" value="14.0780155515538"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.337805046222449"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3550"/>
              <adiabaticHead unit="kJ_per_kg" value="15.18355317811831"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.614292447074284"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3825"/>
              <adiabaticHead unit="kJ_per_kg" value="16.28183203636432"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.888964479604367"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4100"/>
              <adiabaticHead unit="kJ_per_kg" value="17.37362187361643"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.162013652355131"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4375"/>
              <adiabaticHead unit="kJ_per_kg" value="18.45965195084131"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.433622348507726"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4650"/>
              <adiabaticHead unit="kJ_per_kg" value="19.54061572440634"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.703963996757856"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4925"/>
              <adiabaticHead unit="kJ_per_kg" value="20.61717500714571"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.973204111969937"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5200"/>
              <adiabaticHead unit="kJ_per_kg" value="21.68996368657478"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.241501225077111"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.82">
            <measurement>
              <speed unit="per_min" value="3000"/>
              <adiabaticHead unit="kJ_per_kg" value="12.00562374297905"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.358215141647144"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3275"/>
              <adiabaticHead unit="kJ_per_kg" value="12.98377507421073"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.723289093281513"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3550"/>
              <adiabaticHead unit="kJ_per_kg" value="13.9505718426502"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.084125198505738"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3825"/>
              <adiabaticHead unit="kJ_per_kg" value="14.90738640823148"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.441235661155964"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4100"/>
              <adiabaticHead unit="kJ_per_kg" value="15.85547195856506"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.795088206561068"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4375"/>
              <adiabaticHead unit="kJ_per_kg" value="16.79598051562305"/>
              <volumetricFlowrate unit="m_cube_per_s" value="6.146112802150739"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4650"/>
              <adiabaticHead unit="kJ_per_kg" value="17.72997795289318"/>
              <volumetricFlowrate unit="m_cube_per_s" value="6.494707262285266"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4925"/>
              <adiabaticHead unit="kJ_per_kg" value="18.65845663273058"/>
              <volumetricFlowrate unit="m_cube_per_s" value="6.841241964875383"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5200"/>
              <adiabaticHead unit="kJ_per_kg" value="19.58234613476265"/>
              <volumetricFlowrate unit="m_cube_per_s" value="7.18606385552869"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.82">
            <measurement>
              <speed unit="per_min" value="3000"/>
              <adiabaticHead unit="kJ_per_kg" value="10.71369077536061"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.654786607529086"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3275"/>
              <adiabaticHead unit="kJ_per_kg" value="11.53425758257685"/>
              <volumetricFlowrate unit="m_cube_per_s" value="6.091318523603127"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3550"/>
              <adiabaticHead unit="kJ_per_kg" value="12.34225263343341"/>
              <volumetricFlowrate unit="m_cube_per_s" value="6.521162412762298"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3825"/>
              <adiabaticHead unit="kJ_per_kg" value="13.13943479025025"/>
              <volumetricFlowrate unit="m_cube_per_s" value="6.94525396912912"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4100"/>
              <adiabaticHead unit="kJ_per_kg" value="13.9273646849258"/>
              <volumetricFlowrate unit="m_cube_per_s" value="7.364423430567124"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4375"/>
              <adiabaticHead unit="kJ_per_kg" value="14.70744077119186"/>
              <volumetricFlowrate unit="m_cube_per_s" value="7.779414758057565"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4650"/>
              <adiabaticHead unit="kJ_per_kg" value="15.48092795553556"/>
              <volumetricFlowrate unit="m_cube_per_s" value="8.190900867014069"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4925"/>
              <adiabaticHead unit="kJ_per_kg" value="16.24898063567589"/>
              <volumetricFlowrate unit="m_cube_per_s" value="8.599495883481879"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5200"/>
              <adiabaticHead unit="kJ_per_kg" value="17.0126614713045"/>
              <volumetricFlowrate unit="m_cube_per_s" value="9.005765129951813"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.7649999999999999">
            <measurement>
              <speed unit="per_min" value="3000"/>
              <adiabaticHead unit="kJ_per_kg" value="9.17355429948252"/>
              <volumetricFlowrate unit="m_cube_per_s" value="6.888640582060503"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3275"/>
              <adiabaticHead unit="kJ_per_kg" value="9.833487627692456"/>
              <volumetricFlowrate unit="m_cube_per_s" value="7.37992588023517"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3550"/>
              <adiabaticHead unit="kJ_per_kg" value="10.48168223748174"/>
              <volumetricFlowrate unit="m_cube_per_s" value="7.862472326266818"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3825"/>
              <adiabaticHead unit="kJ_per_kg" value="11.11997165632047"/>
              <volumetricFlowrate unit="m_cube_per_s" value="8.337644883934892"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4100"/>
              <adiabaticHead unit="kJ_per_kg" value="11.74994903925663"/>
              <volumetricFlowrate unit="m_cube_per_s" value="8.806629572522453"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4375"/>
              <adiabaticHead unit="kJ_per_kg" value="12.37301636419432"/>
              <volumetricFlowrate unit="m_cube_per_s" value="9.270470090086871"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4650"/>
              <adiabaticHead unit="kJ_per_kg" value="12.99042213173813"/>
              <volumetricFlowrate unit="m_cube_per_s" value="9.730095878990856"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4925"/>
              <adiabaticHead unit="kJ_per_kg" value="13.60329074707111"/>
              <volumetricFlowrate unit="m_cube_per_s" value="10.1863439991494"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5200"/>
              <adiabaticHead unit="kJ_per_kg" value="14.2126457808546"/>
              <volumetricFlowrate unit="m_cube_per_s" value="10.63997644453383"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.71">
            <measurement>
              <speed unit="per_min" value="3000"/>
              <adiabaticHead unit="kJ_per_kg" value="7.491277167739237"/>
              <volumetricFlowrate unit="m_cube_per_s" value="8.022374410761312"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3275"/>
              <adiabaticHead unit="kJ_per_kg" value="8.000723011821419"/>
              <volumetricFlowrate unit="m_cube_per_s" value="8.553927312650938"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3550"/>
              <adiabaticHead unit="kJ_per_kg" value="8.500476582904474"/>
              <volumetricFlowrate unit="m_cube_per_s" value="9.075367351910634"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3825"/>
              <adiabaticHead unit="kJ_per_kg" value="8.992180655210561"/>
              <volumetricFlowrate unit="m_cube_per_s" value="9.58840858983873"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4100"/>
              <adiabaticHead unit="kJ_per_kg" value="9.477243837477104"/>
              <volumetricFlowrate unit="m_cube_per_s" value="10.09452076079601"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4375"/>
              <adiabaticHead unit="kJ_per_kg" value="9.956892061480325"/>
              <volumetricFlowrate unit="m_cube_per_s" value="10.59498299503889"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4650"/>
              <adiabaticHead unit="kJ_per_kg" value="10.43220713108214"/>
              <volumetricFlowrate unit="m_cube_per_s" value="11.09092404057611"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4925"/>
              <adiabaticHead unit="kJ_per_kg" value="10.90415615647708"/>
              <volumetricFlowrate unit="m_cube_per_s" value="11.58335297469496"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5200"/>
              <adiabaticHead unit="kJ_per_kg" value="11.37361443902618"/>
              <volumetricFlowrate unit="m_cube_per_s" value="12.07318308186693"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.655">
            <measurement>
              <speed unit="per_min" value="3000"/>
              <adiabaticHead unit="kJ_per_kg" value="5.761143804188654"/>
              <volumetricFlowrate unit="m_cube_per_s" value="9.04126751509683"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3275"/>
              <adiabaticHead unit="kJ_per_kg" value="6.136231442912857"/>
              <volumetricFlowrate unit="m_cube_per_s" value="9.60207605119392"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3550"/>
              <adiabaticHead unit="kJ_per_kg" value="6.504062533382527"/>
              <volumetricFlowrate unit="m_cube_per_s" value="10.1520350316576"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3825"/>
              <adiabaticHead unit="kJ_per_kg" value="6.865946407322038"/>
              <volumetricFlowrate unit="m_cube_per_s" value="10.69310209073599"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4100"/>
              <adiabaticHead unit="kJ_per_kg" value="7.222997601378456"/>
              <volumetricFlowrate unit="m_cube_per_s" value="11.22694361676327"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4375"/>
              <adiabaticHead unit="kJ_per_kg" value="7.57618054257123"/>
              <volumetricFlowrate unit="m_cube_per_s" value="11.75500156316342"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4650"/>
              <adiabaticHead unit="kJ_per_kg" value="7.926342542704995"/>
              <volumetricFlowrate unit="m_cube_per_s" value="12.27854277971691"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4925"/>
              <adiabaticHead unit="kJ_per_kg" value="8.274238690843337"/>
              <volumetricFlowrate unit="m_cube_per_s" value="12.7986962302942"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5200"/>
              <adiabaticHead unit="kJ_per_kg" value="8.620551007671052"/>
              <volumetricFlowrate unit="m_cube_per_s" value="13.31648163130909"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.6">
            <measurement>
              <speed unit="per_min" value="3000"/>
              <adiabaticHead unit="kJ_per_kg" value="4.051672234327648"/>
              <volumetricFlowrate unit="m_cube_per_s" value="9.946000000000002"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3275"/>
              <adiabaticHead unit="kJ_per_kg" value="4.309627383302317"/>
              <volumetricFlowrate unit="m_cube_per_s" value="10.52821696169844"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3550"/>
              <adiabaticHead unit="kJ_per_kg" value="4.562658696980452"/>
              <volumetricFlowrate unit="m_cube_per_s" value="11.09932059444164"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3825"/>
              <adiabaticHead unit="kJ_per_kg" value="4.811700658596131"/>
              <volumetricFlowrate unit="m_cube_per_s" value="11.6614200710508"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4100"/>
              <adiabaticHead unit="kJ_per_kg" value="5.057546167943378"/>
              <volumetricFlowrate unit="m_cube_per_s" value="12.21630500383194"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4375"/>
              <adiabaticHead unit="kJ_per_kg" value="5.300879824850465"/>
              <volumetricFlowrate unit="m_cube_per_s" value="12.76552056695034"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4650"/>
              <adiabaticHead unit="kJ_per_kg" value="5.542302321600198"/>
              <volumetricFlowrate unit="m_cube_per_s" value="13.31042255127585"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4925"/>
              <adiabaticHead unit="kJ_per_kg" value="5.782348730074633"/>
              <volumetricFlowrate unit="m_cube_per_s" value="13.85221863933274"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5200"/>
              <adiabaticHead unit="kJ_per_kg" value="6.0215025"/>
              <volumetricFlowrate unit="m_cube_per_s" value="14.392"/>
            </measurement>
          </adiabaticEfficiency>
        </characteristicDiagramMeasurements>
      </turboCompressor>
    </compressors>
    <drives>
      <gasTurbine id="drive_19">
        <energy_rate_fun_coeff_1 value="0.01"/>
        <energy_rate_fun_coeff_2 value="0"/>
        <energy_rate_fun_coeff_3 value="0"/>
        <power_fun_coeff_1 value="-1416.075290448184"/>
        <power_fun_coeff_2 value="5.73643612007718"/>
        <power_fun_coeff_3 value="-0.0004349825775855806"/>
        <power_fun_coeff_4 value="8.518542504685646"/>
        <power_fun_coeff_5 value="-0.03450810507315997"/>
        <power_fun_coeff_6 value="2.616681189873551e-06"/>
        <power_fun_coeff_7 value="-0.0283128133463892"/>
        <power_fun_coeff_8 value="0.0001146935097566927"/>
        <power_fun_coeff_9 value="-8.696981446667253e-09"/>
      </gasTurbine>
    </drives>
    <configurations>
      <configuration nrOfSerialStages="1" confId="config_1">
        <stage nrOfParallelUnits="1" stageNr="1">
          <compressor nominalSpeed="5200" id="compressor_19"/>
        </stage>
      </configuration>
    </configurations>
  </compressorStation>
  <compressorStation id="compressorStation_5">
    <compressors>
      <turboCompressor drive="drive_20" id="compressor_20">
        <speedMin unit="per_min" value="3000"/>
        <speedMax unit="per_min" value="5200"/>
        <n_isoline_coeff_1 value="0"/>
        <n_isoline_coeff_2 value="0.007249176923076923"/>
        <n_isoline_coeff_3 value="0"/>
        <n_isoline_coeff_4 value="0"/>
        <n_isoline_coeff_5 value="0"/>
        <n_isoline_coeff_6 value="0"/>
        <n_isoline_coeff_7 value="-0.5113644204235059"/>
        <n_isoline_coeff_8 value="2.458482790497625e-05"/>
        <n_isoline_coeff_9 value="0"/>
        <eta_ad_isoline_coeff_1 value="0.8094193264934713"/>
        <eta_ad_isoline_coeff_2 value="-1.062615549738566e-05"/>
        <eta_ad_isoline_coeff_3 value="8.932538570679569e-10"/>
        <eta_ad_isoline_coeff_4 value="0.03571570957506372"/>
        <eta_ad_isoline_coeff_5 value="-2.153317926229404e-06"/>
        <eta_ad_isoline_coeff_6 value="-8.185720215752887e-11"/>
        <eta_ad_isoline_coeff_7 value="-0.009272496520610291"/>
        <eta_ad_isoline_coeff_8 value="2.09936681863687e-06"/>
        <eta_ad_isoline_coeff_9 value="-1.456326977701545e-10"/>
        <surgeline_coeff_1 value="5.920765251923079"/>
        <surgeline_coeff_2 value="36.67944378867073"/>
        <surgeline_coeff_3 value="0"/>
        <chokeline_coeff_1 value="-4.08377056037564"/>
        <chokeline_coeff_2 value="1.573260565162901"/>
        <chokeline_coeff_3 value="0"/>
        <efficiencyOfChokeline value="0.8"/>
        <surgelineMeasurements>
          <measurement>
            <speed unit="per_min" value="3000"/>
            <adiabaticHead unit="kJ_per_kg" value="21.66688367596169"/>
            <volumetricFlowrate unit="m_cube_per_s" value="0.4292900000000041"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="3275"/>
            <adiabaticHead unit="kJ_per_kg" value="23.64050160920794"/>
            <volumetricFlowrate unit="m_cube_per_s" value="0.4830971936046097"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="3550"/>
            <adiabaticHead unit="kJ_per_kg" value="25.61234968081492"/>
            <volumetricFlowrate unit="m_cube_per_s" value="0.5368561350696933"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="3825"/>
            <adiabaticHead unit="kJ_per_kg" value="27.58254914987337"/>
            <volumetricFlowrate unit="m_cube_per_s" value="0.5905701303093646"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="4100"/>
            <adiabaticHead unit="kJ_per_kg" value="29.55122038454427"/>
            <volumetricFlowrate unit="m_cube_per_s" value="0.6442424609481123"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="4375"/>
            <adiabaticHead unit="kJ_per_kg" value="31.51848291505489"/>
            <volumetricFlowrate unit="m_cube_per_s" value="0.6978763857656489"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="4650"/>
            <adiabaticHead unit="kJ_per_kg" value="33.48445548568479"/>
            <volumetricFlowrate unit="m_cube_per_s" value="0.7514751421142153"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="4925"/>
            <adiabaticHead unit="kJ_per_kg" value="35.44925610579942"/>
            <volumetricFlowrate unit="m_cube_per_s" value="0.805041947309923"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="5200"/>
            <adiabaticHead unit="kJ_per_kg" value="37.4130020999999"/>
            <volumetricFlowrate unit="m_cube_per_s" value="0.8585799999999973"/>
          </measurement>
        </surgelineMeasurements>
        <characteristicDiagramMeasurements>
          <adiabaticEfficiency value="0.8100000000000001">
            <measurement>
              <speed unit="per_min" value="3000"/>
              <adiabaticHead unit="kJ_per_kg" value="21.19225016259112"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.126451935302188"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3275"/>
              <adiabaticHead unit="kJ_per_kg" value="23.08868778051987"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.230504690446451"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3550"/>
              <adiabaticHead unit="kJ_per_kg" value="24.97960140599638"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.334254358039287"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3825"/>
              <adiabaticHead unit="kJ_per_kg" value="26.86546158541037"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.437726755775837"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4100"/>
              <adiabaticHead unit="kJ_per_kg" value="28.74672757802465"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.54094708205502"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4375"/>
              <adiabaticHead unit="kJ_per_kg" value="30.62384827615546"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.643939966467509"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4650"/>
              <adiabaticHead unit="kJ_per_kg" value="32.4972630731412"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.746729517418992"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4925"/>
              <adiabaticHead unit="kJ_per_kg" value="34.3674026841535"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.849339367166004"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5200"/>
              <adiabaticHead unit="kJ_per_kg" value="36.2346899244498"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.951792714516686"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.8200000000000001">
            <measurement>
              <speed unit="per_min" value="3000"/>
              <adiabaticHead unit="kJ_per_kg" value="20.18429183030799"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.89003172812128"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3275"/>
              <adiabaticHead unit="kJ_per_kg" value="21.94005004122386"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.044536109030642"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3550"/>
              <adiabaticHead unit="kJ_per_kg" value="23.68547630158125"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.198131292070559"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3825"/>
              <adiabaticHead unit="kJ_per_kg" value="25.42162541866215"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.350910098875054"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4100"/>
              <adiabaticHead unit="kJ_per_kg" value="27.14950205929637"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.502960938785226"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4375"/>
              <adiabaticHead unit="kJ_per_kg" value="28.87006622618917"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.654368290758784"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4650"/>
              <adiabaticHead unit="kJ_per_kg" value="30.58423817493946"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.80521313606109"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4925"/>
              <adiabaticHead unit="kJ_per_kg" value="32.2929028500767"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.955573348630487"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5200"/>
              <adiabaticHead unit="kJ_per_kg" value="33.99691390674705"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.105524048981321"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.83">
            <measurement>
              <speed unit="per_min" value="3000"/>
              <adiabaticHead unit="kJ_per_kg" value="18.5898298354139"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.68622205389243"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3275"/>
              <adiabaticHead unit="kJ_per_kg" value="20.15057433725494"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.886779825656595"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3550"/>
              <adiabaticHead unit="kJ_per_kg" value="21.69709902515079"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.085510332166018"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3825"/>
              <adiabaticHead unit="kJ_per_kg" value="23.23111399471589"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.282633323011694"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4100"/>
              <adiabaticHead unit="kJ_per_kg" value="24.75420559010384"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.47835264555514"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4375"/>
              <adiabaticHead unit="kJ_per_kg" value="26.26785356330904"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.672858449921766"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4650"/>
              <adiabaticHead unit="kJ_per_kg" value="27.77344574553928"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.866329074292032"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4925"/>
              <adiabaticHead unit="kJ_per_kg" value="29.27229068779293"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.058932669232647"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5200"/>
              <adiabaticHead unit="kJ_per_kg" value="30.76562863498132"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.250828607886084"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.84">
            <measurement>
              <speed unit="per_min" value="3000"/>
              <adiabaticHead unit="kJ_per_kg" value="16.46078714387946"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.475766056736064"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3275"/>
              <adiabaticHead unit="kJ_per_kg" value="17.79532246818371"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.714839575906525"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3550"/>
              <adiabaticHead unit="kJ_per_kg" value="19.11409232240593"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.951088811339233"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3825"/>
              <adiabaticHead unit="kJ_per_kg" value="20.41927202821901"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.184903458082493"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4100"/>
              <adiabaticHead unit="kJ_per_kg" value="21.71283346229245"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.41663676530563"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4375"/>
              <adiabaticHead unit="kJ_per_kg" value="22.99657854569615"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.646611535712778"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4650"/>
              <adiabaticHead unit="kJ_per_kg" value="24.27216672110541"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.875125047909473"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4925"/>
              <adiabaticHead unit="kJ_per_kg" value="25.5411377418322"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.102453138912722"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5200"/>
              <adiabaticHead unit="kJ_per_kg" value="26.80493077205942"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.328853625836543"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.83">
            <measurement>
              <speed unit="per_min" value="3000"/>
              <adiabaticHead unit="kJ_per_kg" value="13.93328767122985"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.225711773762044"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3275"/>
              <adiabaticHead unit="kJ_per_kg" value="15.03570571225296"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.495008181975859"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3550"/>
              <adiabaticHead unit="kJ_per_kg" value="16.1231468713243"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.760646068317054"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3825"/>
              <adiabaticHead unit="kJ_per_kg" value="17.19791757686796"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.023188842370103"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4100"/>
              <adiabaticHead unit="kJ_per_kg" value="18.26207315721832"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.283138575506802"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4375"/>
              <adiabaticHead unit="kJ_per_kg" value="19.31746417242194"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.540947318723394"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4650"/>
              <adiabaticHead unit="kJ_per_kg" value="20.3657732827447"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.797026108803557"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4925"/>
              <adiabaticHead unit="kJ_per_kg" value="21.40854498993665"/>
              <volumetricFlowrate unit="m_cube_per_s" value="6.051752233453301"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5200"/>
              <adiabaticHead unit="kJ_per_kg" value="22.44720994484563"/>
              <volumetricFlowrate unit="m_cube_per_s" value="6.305475169114773"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.8200000000000001">
            <measurement>
              <speed unit="per_min" value="3000"/>
              <adiabaticHead unit="kJ_per_kg" value="11.17252970862268"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.915827359660393"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3275"/>
              <adiabaticHead unit="kJ_per_kg" value="12.05488297103197"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.20803059972462"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3550"/>
              <adiabaticHead unit="kJ_per_kg" value="12.9244944111625"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.496014212670331"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3825"/>
              <adiabaticHead unit="kJ_per_kg" value="13.78350641578391"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.780487678908856"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4100"/>
              <adiabaticHead unit="kJ_per_kg" value="14.63380720999723"/>
              <volumetricFlowrate unit="m_cube_per_s" value="6.062076309770708"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4375"/>
              <adiabaticHead unit="kJ_per_kg" value="15.47708130277928"/>
              <volumetricFlowrate unit="m_cube_per_s" value="6.341337953231189"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4650"/>
              <adiabaticHead unit="kJ_per_kg" value="16.31484881185267"/>
              <volumetricFlowrate unit="m_cube_per_s" value="6.618776016874037"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4925"/>
              <adiabaticHead unit="kJ_per_kg" value="17.14849661074705"/>
              <volumetricFlowrate unit="m_cube_per_s" value="6.894849782662821"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5200"/>
              <adiabaticHead unit="kJ_per_kg" value="17.97930337428061"/>
              <volumetricFlowrate unit="m_cube_per_s" value="7.169982701091553"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.8100000000000001">
            <measurement>
              <speed unit="per_min" value="3000"/>
              <adiabaticHead unit="kJ_per_kg" value="8.325775213540235"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.538103591214663"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3275"/>
              <adiabaticHead unit="kJ_per_kg" value="9.008941270627101"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.847495864502088"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3550"/>
              <adiabaticHead unit="kJ_per_kg" value="9.682131824377285"/>
              <volumetricFlowrate unit="m_cube_per_s" value="6.152370431409774"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3825"/>
              <adiabaticHead unit="kJ_per_kg" value="10.34715071893939"/>
              <volumetricFlowrate unit="m_cube_per_s" value="6.453544216953246"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4100"/>
              <adiabaticHead unit="kJ_per_kg" value="11.00557799826202"/>
              <volumetricFlowrate unit="m_cube_per_s" value="6.751732791503844"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4375"/>
              <adiabaticHead unit="kJ_per_kg" value="11.65881641072346"/>
              <volumetricFlowrate unit="m_cube_per_s" value="7.047571431807391"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4650"/>
              <adiabaticHead unit="kJ_per_kg" value="12.30812720313819"/>
              <volumetricFlowrate unit="m_cube_per_s" value="7.341631331375424"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4925"/>
              <adiabaticHead unit="kJ_per_kg" value="12.95465815799428"/>
              <volumetricFlowrate unit="m_cube_per_s" value="7.634432297990458"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5200"/>
              <adiabaticHead unit="kJ_per_kg" value="13.59946592257264"/>
              <volumetricFlowrate unit="m_cube_per_s" value="7.926452866118467"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.8">
            <measurement>
              <speed unit="per_min" value="3000"/>
              <adiabaticHead unit="kJ_per_kg" value="5.501948737105401"/>
              <volumetricFlowrate unit="m_cube_per_s" value="6.0929"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3275"/>
              <adiabaticHead unit="kJ_per_kg" value="6.009129976361528"/>
              <volumetricFlowrate unit="m_cube_per_s" value="6.415275867346304"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3550"/>
              <adiabaticHead unit="kJ_per_kg" value="6.509050845827121"/>
              <volumetricFlowrate unit="m_cube_per_s" value="6.733036879435125"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3825"/>
              <adiabaticHead unit="kJ_per_kg" value="7.003109864212094"/>
              <volumetricFlowrate unit="m_cube_per_s" value="7.047071966390869"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4100"/>
              <adiabaticHead unit="kJ_per_kg" value="7.492528640895548"/>
              <volumetricFlowrate unit="m_cube_per_s" value="7.358157610765852"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4375"/>
              <adiabaticHead unit="kJ_per_kg" value="7.978389711591756"/>
              <volumetricFlowrate unit="m_cube_per_s" value="7.666981896745398"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4650"/>
              <adiabaticHead unit="kJ_per_kg" value="8.461665450375447"/>
              <volumetricFlowrate unit="m_cube_per_s" value="7.974162887285035"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4925"/>
              <adiabaticHead unit="kJ_per_kg" value="8.943240578418809"/>
              <volumetricFlowrate unit="m_cube_per_s" value="8.280262931172869"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5200"/>
              <adiabaticHead unit="kJ_per_kg" value="9.423929999999995"/>
              <volumetricFlowrate unit="m_cube_per_s" value="8.585799999999999"/>
            </measurement>
          </adiabaticEfficiency>
        </characteristicDiagramMeasurements>
      </turboCompressor>
    </compressors>
    <drives>
      <gasTurbine id="drive_20">
        <energy_rate_fun_coeff_1 value="0.01"/>
        <energy_rate_fun_coeff_2 value="0"/>
        <energy_rate_fun_coeff_3 value="0"/>
        <power_fun_coeff_1 value="-1487.100402976049"/>
        <power_fun_coeff_2 value="6.024154593583228"/>
        <power_fun_coeff_3 value="-0.0004567996989837642"/>
        <power_fun_coeff_4 value="8.945801170979584"/>
        <power_fun_coeff_5 value="-0.0362389043198362"/>
        <power_fun_coeff_6 value="2.74792426516335e-06"/>
        <power_fun_coeff_7 value="-0.0297328796150911"/>
        <power_fun_coeff_8 value="0.0001204461130904509"/>
        <power_fun_coeff_9 value="-9.133189952012183e-09"/>
      </gasTurbine>
    </drives>
    <configurations>
      <configuration nrOfSerialStages="1" confId="config_1">
        <stage nrOfParallelUnits="1" stageNr="1">
          <compressor nominalSpeed="5250" id="compressor_20"/>
        </stage>
      </configuration>
    </configurations>
  </compressorStation>
  <compressorStation id="compressorStation_6">
    <compressors>
      <turboCompressor drive="drive_21" id="compressor_21">
        <speedMin unit="per_min" value="5723"/>
        <speedMax unit="per_min" value="10926"/>
        <n_isoline_coeff_1 value="0"/>
        <n_isoline_coeff_2 value="0.004017081274025261"/>
        <n_isoline_coeff_3 value="0"/>
        <n_isoline_coeff_4 value="0"/>
        <n_isoline_coeff_5 value="0"/>
        <n_isoline_coeff_6 value="0"/>
        <n_isoline_coeff_7 value="-0.52390721536052"/>
        <n_isoline_coeff_8 value="1.198762619807157e-05"/>
        <n_isoline_coeff_9 value="0"/>
        <eta_ad_isoline_coeff_1 value="0.960747056887603"/>
        <eta_ad_isoline_coeff_2 value="-3.156900424048566e-05"/>
        <eta_ad_isoline_coeff_3 value="1.444578137884578e-09"/>
        <eta_ad_isoline_coeff_4 value="0.02875271179437678"/>
        <eta_ad_isoline_coeff_5 value="1.666875846855086e-05"/>
        <eta_ad_isoline_coeff_6 value="-1.098048605609135e-09"/>
        <eta_ad_isoline_coeff_7 value="-0.04651329612177183"/>
        <eta_ad_isoline_coeff_8 value="4.479071045641365e-06"/>
        <eta_ad_isoline_coeff_9 value="-1.259581682913123e-10"/>
        <surgeline_coeff_1 value="2.227346032657195"/>
        <surgeline_coeff_2 value="45.15957154818997"/>
        <surgeline_coeff_3 value="0"/>
        <chokeline_coeff_1 value="-1.260289027432611"/>
        <chokeline_coeff_2 value="1.336510453236964"/>
        <chokeline_coeff_3 value="0"/>
        <efficiencyOfChokeline value="0.45"/>
        <surgelineMeasurements>
          <measurement>
            <speed unit="per_min" value="5723"/>
            <adiabaticHead unit="kJ_per_kg" value="22.89439815382869"/>
            <volumetricFlowrate unit="m_cube_per_s" value="0.457645000000002"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="6373.375"/>
            <adiabaticHead unit="kJ_per_kg" value="25.48368428253606"/>
            <volumetricFlowrate unit="m_cube_per_s" value="0.5149813749907243"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="7023.75"/>
            <adiabaticHead unit="kJ_per_kg" value="28.07097120692514"/>
            <volumetricFlowrate unit="m_cube_per_s" value="0.5722734802009826"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="7674.125"/>
            <adiabaticHead unit="kJ_per_kg" value="30.65641620388803"/>
            <volumetricFlowrate unit="m_cube_per_s" value="0.6295247983230764"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="8324.5"/>
            <adiabaticHead unit="kJ_per_kg" value="33.24017554446049"/>
            <volumetricFlowrate unit="m_cube_per_s" value="0.6867387897759254"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="8974.875"/>
            <adiabaticHead unit="kJ_per_kg" value="35.82240456073792"/>
            <volumetricFlowrate unit="m_cube_per_s" value="0.7439188941868348"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="9625.25"/>
            <adiabaticHead unit="kJ_per_kg" value="38.40325771166665"/>
            <volumetricFlowrate unit="m_cube_per_s" value="0.8010685318483589"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="10275.625"/>
            <adiabaticHead unit="kJ_per_kg" value="40.98288864778689"/>
            <volumetricFlowrate unit="m_cube_per_s" value="0.8581911051519495"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="10926"/>
            <adiabaticHead unit="kJ_per_kg" value="43.56145027500018"/>
            <volumetricFlowrate unit="m_cube_per_s" value="0.9152900000000042"/>
          </measurement>
        </surgelineMeasurements>
        <characteristicDiagramMeasurements>
          <adiabaticEfficiency value="0.88">
            <measurement>
              <speed unit="per_min" value="5723"/>
              <adiabaticHead unit="kJ_per_kg" value="22.43873118551054"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.100109301307129"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6373.375"/>
              <adiabaticHead unit="kJ_per_kg" value="24.93227513442762"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.223678744869319"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="7023.75"/>
              <adiabaticHead unit="kJ_per_kg" value="27.41736468694704"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.346829224467001"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="7674.125"/>
              <adiabaticHead unit="kJ_per_kg" value="29.89477280851231"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.469599044983388"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="8324.5"/>
              <adiabaticHead unit="kJ_per_kg" value="32.36525138158677"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.59202546651877"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="8974.875"/>
              <adiabaticHead unit="kJ_per_kg" value="34.82953309189399"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.71414479786458"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="9625.25"/>
              <adiabaticHead unit="kJ_per_kg" value="37.28833319466173"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.835992484030937"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="10275.625"/>
              <adiabaticHead unit="kJ_per_kg" value="39.74235117369562"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.957603188463286"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="10926"/>
              <adiabaticHead unit="kJ_per_kg" value="42.19227230482675"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.079010870520223"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.88">
            <measurement>
              <speed unit="per_min" value="5723"/>
              <adiabaticHead unit="kJ_per_kg" value="21.48491932604553"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.818004310846344"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6373.375"/>
              <adiabaticHead unit="kJ_per_kg" value="23.79473797136896"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.009811053716656"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="7023.75"/>
              <adiabaticHead unit="kJ_per_kg" value="26.08654600055906"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.200122199681722"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="7674.125"/>
              <adiabaticHead unit="kJ_per_kg" value="28.36231086573326"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.389101125456493"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="8324.5"/>
              <adiabaticHead unit="kJ_per_kg" value="30.62388272997734"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.576901468105062"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="8974.875"/>
              <adiabaticHead unit="kJ_per_kg" value="32.87300907404949"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.763668337977603"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="9625.25"/>
              <adiabaticHead unit="kJ_per_kg" value="35.11134750673954"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.949539382479281"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="10275.625"/>
              <adiabaticHead unit="kJ_per_kg" value="37.34047707061467"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.134645724896452"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="10926"/>
              <adiabaticHead unit="kJ_per_kg" value="39.56190828355324"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.319112798243039"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.88">
            <measurement>
              <speed unit="per_min" value="5723"/>
              <adiabaticHead unit="kJ_per_kg" value="19.95319430430397"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.582505591181045"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6373.375"/>
              <adiabaticHead unit="kJ_per_kg" value="21.99836482514569"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.837874574555683"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="7023.75"/>
              <adiabaticHead unit="kJ_per_kg" value="24.01683384077664"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.089909490589355"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="7674.125"/>
              <adiabaticHead unit="kJ_per_kg" value="26.01209075679703"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.339046041807411"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="8324.5"/>
              <adiabaticHead unit="kJ_per_kg" value="27.9872926934194"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.58567844012072"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="8974.875"/>
              <adiabaticHead unit="kJ_per_kg" value="29.94531912560424"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.830166229433233"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="9625.25"/>
              <adiabaticHead unit="kJ_per_kg" value="31.8888166793703"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.072839879106254"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="10275.625"/>
              <adiabaticHead unit="kJ_per_kg" value="33.82023625756754"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.314005419645685"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="10926"/>
              <adiabaticHead unit="kJ_per_kg" value="35.74186413448551"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.553948325311536"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.88">
            <measurement>
              <speed unit="per_min" value="5723"/>
              <adiabaticHead unit="kJ_per_kg" value="17.86493848731075"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.35497597584406"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6373.375"/>
              <adiabaticHead unit="kJ_per_kg" value="19.5948890208321"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.663926964855102"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="7023.75"/>
              <adiabaticHead unit="kJ_per_kg" value="21.29396360393921"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.967363833530162"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="7674.125"/>
              <adiabaticHead unit="kJ_per_kg" value="22.96685263912022"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.266124238472411"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="8324.5"/>
              <adiabaticHead unit="kJ_per_kg" value="24.61765382706756"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.560939985971725"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="8974.875"/>
              <adiabaticHead unit="kJ_per_kg" value="26.2499909137192"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.852458238978585"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="9625.25"/>
              <adiabaticHead unit="kJ_per_kg" value="27.86710551223772"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.141257915544784"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="10275.625"/>
              <adiabaticHead unit="kJ_per_kg" value="29.47192926627057"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.427862576423514"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="10926"/>
              <adiabaticHead unit="kJ_per_kg" value="31.06714143496785"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.712750709148491"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.7725">
            <measurement>
              <speed unit="per_min" value="5723"/>
              <adiabaticHead unit="kJ_per_kg" value="15.33923322767668"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.099168457066228"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6373.375"/>
              <adiabaticHead unit="kJ_per_kg" value="16.74121367568117"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.449854993118751"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="7023.75"/>
              <adiabaticHead unit="kJ_per_kg" value="18.11331646890032"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.793068036030222"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="7674.125"/>
              <adiabaticHead unit="kJ_per_kg" value="19.46062762897659"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.130079785648102"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="8324.5"/>
              <adiabaticHead unit="kJ_per_kg" value="20.78747341651611"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.461972397824263"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="8974.875"/>
              <adiabaticHead unit="kJ_per_kg" value="22.09759333924275"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.789681260075765"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="9625.25"/>
              <adiabaticHead unit="kJ_per_kg" value="23.39426815484289"/>
              <volumetricFlowrate unit="m_cube_per_s" value="6.114027009773337"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="10275.625"/>
              <adiabaticHead unit="kJ_per_kg" value="24.6804166122184"/>
              <volumetricFlowrate unit="m_cube_per_s" value="6.43573973266351"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="10926"/>
              <adiabaticHead unit="kJ_per_kg" value="25.95867000887388"/>
              <volumetricFlowrate unit="m_cube_per_s" value="6.755477612395372"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.665">
            <measurement>
              <speed unit="per_min" value="5723"/>
              <adiabaticHead unit="kJ_per_kg" value="12.54189845137434"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.790312328980844"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6373.375"/>
              <adiabaticHead unit="kJ_per_kg" value="13.63192025351913"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.171969119726534"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="7023.75"/>
              <adiabaticHead unit="kJ_per_kg" value="14.69653827867874"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.544731112241669"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="7674.125"/>
              <adiabaticHead unit="kJ_per_kg" value="15.74045138453149"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.910243549711431"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="8324.5"/>
              <adiabaticHead unit="kJ_per_kg" value="16.76758606852663"/>
              <volumetricFlowrate unit="m_cube_per_s" value="6.269881243550055"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="8974.875"/>
              <adiabaticHead unit="kJ_per_kg" value="17.78128678347821"/>
              <volumetricFlowrate unit="m_cube_per_s" value="6.62481520990171"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="9625.25"/>
              <adiabaticHead unit="kJ_per_kg" value="18.78445260319991"/>
              <volumetricFlowrate unit="m_cube_per_s" value="6.976060521314203"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="10275.625"/>
              <adiabaticHead unit="kJ_per_kg" value="19.77963786953518"/>
              <volumetricFlowrate unit="m_cube_per_s" value="7.324511546972185"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="10926"/>
              <adiabaticHead unit="kJ_per_kg" value="20.76912802770403"/>
              <volumetricFlowrate unit="m_cube_per_s" value="7.670968505445942"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.5575">
            <measurement>
              <speed unit="per_min" value="5723"/>
              <adiabaticHead unit="kJ_per_kg" value="9.630855338487528"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.41670979755721"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6373.375"/>
              <adiabaticHead unit="kJ_per_kg" value="10.43959524554237"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.820898798409807"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="7023.75"/>
              <adiabaticHead unit="kJ_per_kg" value="11.22882594708393"/>
              <volumetricFlowrate unit="m_cube_per_s" value="6.21533756162104"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="7674.125"/>
              <adiabaticHead unit="kJ_per_kg" value="12.00238444914098"/>
              <volumetricFlowrate unit="m_cube_per_s" value="6.601943731688855"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="8324.5"/>
              <adiabaticHead unit="kJ_per_kg" value="12.76344356415174"/>
              <volumetricFlowrate unit="m_cube_per_s" value="6.982303004926877"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="8974.875"/>
              <adiabaticHead unit="kJ_per_kg" value="13.51468348268188"/>
              <volumetricFlowrate unit="m_cube_per_s" value="7.357754876934834"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="9625.25"/>
              <adiabaticHead unit="kJ_per_kg" value="14.25841271751499"/>
              <volumetricFlowrate unit="m_cube_per_s" value="7.729453087583019"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="10275.625"/>
              <adiabaticHead unit="kJ_per_kg" value="14.99665577818599"/>
              <volumetricFlowrate unit="m_cube_per_s" value="8.098409438662086"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="10926"/>
              <adiabaticHead unit="kJ_per_kg" value="15.73121834870779"/>
              <volumetricFlowrate unit="m_cube_per_s" value="8.465526368163113"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.45">
            <measurement>
              <speed unit="per_min" value="5723"/>
              <adiabaticHead unit="kJ_per_kg" value="6.727298870815442"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.976449999999999"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6373.375"/>
              <adiabaticHead unit="kJ_per_kg" value="7.28943434018978"/>
              <volumetricFlowrate unit="m_cube_per_s" value="6.397049381032054"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="7023.75"/>
              <adiabaticHead unit="kJ_per_kg" value="7.837995602765758"/>
              <volumetricFlowrate unit="m_cube_per_s" value="6.807492308169205"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="7674.125"/>
              <adiabaticHead unit="kJ_per_kg" value="8.375781884828069"/>
              <volumetricFlowrate unit="m_cube_per_s" value="7.209873210435862"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="8324.5"/>
              <adiabaticHead unit="kJ_per_kg" value="8.905095529847625"/>
              <volumetricFlowrate unit="m_cube_per_s" value="7.605914740629347"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="8974.875"/>
              <adiabaticHead unit="kJ_per_kg" value="9.427873938414448"/>
              <volumetricFlowrate unit="m_cube_per_s" value="7.997066495036266"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="9625.25"/>
              <adiabaticHead unit="kJ_per_kg" value="9.945781597758041"/>
              <volumetricFlowrate unit="m_cube_per_s" value="8.384573871495046"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="10275.625"/>
              <adiabaticHead unit="kJ_per_kg" value="10.46027621074015"/>
              <volumetricFlowrate unit="m_cube_per_s" value="8.769527548240353"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="10926"/>
              <adiabaticHead unit="kJ_per_kg" value="10.9726575"/>
              <volumetricFlowrate unit="m_cube_per_s" value="9.152900000000001"/>
            </measurement>
          </adiabaticEfficiency>
        </characteristicDiagramMeasurements>
      </turboCompressor>
    </compressors>
    <drives>
      <gasTurbine id="drive_21">
        <energy_rate_fun_coeff_1 value="0.01"/>
        <energy_rate_fun_coeff_2 value="0"/>
        <energy_rate_fun_coeff_3 value="0"/>
        <power_fun_coeff_1 value="-1617.833747727916"/>
        <power_fun_coeff_2 value="3.119118359100923"/>
        <power_fun_coeff_3 value="-0.0001125650848717027"/>
        <power_fun_coeff_4 value="9.732240678511724"/>
        <power_fun_coeff_5 value="-0.0187633683733985"/>
        <power_fun_coeff_6 value="6.771465235578401e-07"/>
        <power_fun_coeff_7 value="-0.0323467440141636"/>
        <power_fun_coeff_8 value="6.23632207285885e-05"/>
        <power_fun_coeff_9 value="-2.250610725849393e-09"/>
      </gasTurbine>
    </drives>
    <configurations>
      <configuration nrOfSerialStages="1" confId="config_1">
        <stage nrOfParallelUnits="1" stageNr="1">
          <compressor nominalSpeed="6500" id="compressor_21"/>
        </stage>
      </configuration>
    </configurations>
  </compressorStation>
  <compressorStation id="compressorStation_7">
    <compressors>
      <turboCompressor drive="drive_22" id="compressor_22">
        <speedMin unit="per_min" value="3000"/>
        <speedMax unit="per_min" value="6500"/>
        <n_isoline_coeff_1 value="0"/>
        <n_isoline_coeff_2 value="0.005185323076923077"/>
        <n_isoline_coeff_3 value="0"/>
        <n_isoline_coeff_4 value="0"/>
        <n_isoline_coeff_5 value="0"/>
        <n_isoline_coeff_6 value="0"/>
        <n_isoline_coeff_7 value="-0.274934460632196"/>
        <n_isoline_coeff_8 value="1.057440233200754e-05"/>
        <n_isoline_coeff_9 value="0"/>
        <eta_ad_isoline_coeff_1 value="0.8355196189380975"/>
        <eta_ad_isoline_coeff_2 value="-2.708458282801834e-05"/>
        <eta_ad_isoline_coeff_3 value="2.331703153811374e-09"/>
        <eta_ad_isoline_coeff_4 value="0.02968453324936042"/>
        <eta_ad_isoline_coeff_5 value="7.580803311787667e-06"/>
        <eta_ad_isoline_coeff_6 value="-1.1149691321731e-09"/>
        <eta_ad_isoline_coeff_7 value="-0.01442911589769477"/>
        <eta_ad_isoline_coeff_8 value="2.493662843725977e-06"/>
        <eta_ad_isoline_coeff_9 value="-1.206872626687376e-10"/>
        <surgeline_coeff_1 value="-2.488955076923084"/>
        <surgeline_coeff_2 value="32.46066290669619"/>
        <surgeline_coeff_3 value="0"/>
        <chokeline_coeff_1 value="-0.01413520775517796"/>
        <chokeline_coeff_2 value="0.7623021114111304"/>
        <chokeline_coeff_3 value="0"/>
        <efficiencyOfChokeline value="0.7"/>
        <surgelineMeasurements>
          <measurement>
            <speed unit="per_min" value="3000"/>
            <adiabaticHead unit="kJ_per_kg" value="15.48143021153853"/>
            <volumetricFlowrate unit="m_cube_per_s" value="0.5536050000000022"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="3437.5"/>
            <adiabaticHead unit="kJ_per_kg" value="17.73196531784549"/>
            <volumetricFlowrate unit="m_cube_per_s" value="0.6229361505305944"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="3875"/>
            <adiabaticHead unit="kJ_per_kg" value="19.98102074405802"/>
            <volumetricFlowrate unit="m_cube_per_s" value="0.6922217172695467"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="4312.5"/>
            <adiabaticHead unit="kJ_per_kg" value="22.22873192929046"/>
            <volumetricFlowrate unit="m_cube_per_s" value="0.761465872624389"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="4750"/>
            <adiabaticHead unit="kJ_per_kg" value="24.47523356631726"/>
            <volumetricFlowrate unit="m_cube_per_s" value="0.8306727660105181"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="5187.5"/>
            <adiabaticHead unit="kJ_per_kg" value="26.72065965793924"/>
            <volumetricFlowrate unit="m_cube_per_s" value="0.8998465255876453"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="5625"/>
            <adiabaticHead unit="kJ_per_kg" value="28.9651435725325"/>
            <volumetricFlowrate unit="m_cube_per_s" value="0.9689912599710662"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="6062.5"/>
            <adiabaticHead unit="kJ_per_kg" value="31.20881809882852"/>
            <volumetricFlowrate unit="m_cube_per_s" value="1.038111059919242"/>
          </measurement>
          <measurement>
            <speed unit="per_min" value="6500"/>
            <adiabaticHead unit="kJ_per_kg" value="33.45181550000024"/>
            <volumetricFlowrate unit="m_cube_per_s" value="1.107210000000008"/>
          </measurement>
        </surgelineMeasurements>
        <characteristicDiagramMeasurements>
          <adiabaticEfficiency value="0.8100000000000001">
            <measurement>
              <speed unit="per_min" value="3000"/>
              <adiabaticHead unit="kJ_per_kg" value="15.19615207757032"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.216323502280781"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3437.5"/>
              <adiabaticHead unit="kJ_per_kg" value="17.37040351621615"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.379670993621597"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3875"/>
              <adiabaticHead unit="kJ_per_kg" value="19.53653378402979"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.542408356410301"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4312.5"/>
              <adiabaticHead unit="kJ_per_kg" value="21.6953468023492"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.704595987770913"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4750"/>
              <adiabaticHead unit="kJ_per_kg" value="23.84762272778427"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.866292499427364"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5187.5"/>
              <adiabaticHead unit="kJ_per_kg" value="25.99412027218433"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.027554891998367"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5625"/>
              <adiabaticHead unit="kJ_per_kg" value="28.13557886361462"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.188438717347582"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6062.5"/>
              <adiabaticHead unit="kJ_per_kg" value="30.27272066684094"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.348998230378896"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6500"/>
              <adiabaticHead unit="kJ_per_kg" value="32.40625247984168"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.509286531517863"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.8200000000000001">
            <measurement>
              <speed unit="per_min" value="3000"/>
              <adiabaticHead unit="kJ_per_kg" value="14.61478206696632"/>
              <volumetricFlowrate unit="m_cube_per_s" value="1.967189350203655"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3437.5"/>
              <adiabaticHead unit="kJ_per_kg" value="16.63852111243813"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.229593844329259"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3875"/>
              <adiabaticHead unit="kJ_per_kg" value="18.64312268495192"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.489516912343317"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4312.5"/>
              <adiabaticHead unit="kJ_per_kg" value="20.6308450598578"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.747251369469296"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4750"/>
              <adiabaticHead unit="kJ_per_kg" value="22.60378942216718"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.00306966209361"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5187.5"/>
              <adiabaticHead unit="kJ_per_kg" value="24.56392169885033"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.257226698611329"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5625"/>
              <adiabaticHead unit="kJ_per_kg" value="26.51309133372191"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.509962283838042"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6062.5"/>
              <adiabaticHead unit="kJ_per_kg" value="28.45304756139964"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.761503229143523"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6500"/>
              <adiabaticHead unit="kJ_per_kg" value="30.38545362673239"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.012065196188376"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.83">
            <measurement>
              <speed unit="per_min" value="3000"/>
              <adiabaticHead unit="kJ_per_kg" value="13.6736908894458"/>
              <volumetricFlowrate unit="m_cube_per_s" value="2.781954927193149"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3437.5"/>
              <adiabaticHead unit="kJ_per_kg" value="15.47360305043487"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.139060688683432"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3875"/>
              <adiabaticHead unit="kJ_per_kg" value="17.24322957351569"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.490157725958251"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4312.5"/>
              <adiabaticHead unit="kJ_per_kg" value="18.98691429774086"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.836107864381246"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4750"/>
              <adiabaticHead unit="kJ_per_kg" value="20.70849986518666"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.177673490948035"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5187.5"/>
              <adiabaticHead unit="kJ_per_kg" value="22.41142234947816"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.515536328753225"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5625"/>
              <adiabaticHead unit="kJ_per_kg" value="24.09878597349992"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.8503122611166"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6062.5"/>
              <adiabaticHead unit="kJ_per_kg" value="25.77342296509788"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.182563207060409"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6500"/>
              <adiabaticHead unit="kJ_per_kg" value="27.43794217588253"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.512806767366055"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.84">
            <measurement>
              <speed unit="per_min" value="3000"/>
              <adiabaticHead unit="kJ_per_kg" value="12.36436508645467"/>
              <volumetricFlowrate unit="m_cube_per_s" value="3.622535724036359"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3437.5"/>
              <adiabaticHead unit="kJ_per_kg" value="13.88929948245987"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.061295233857915"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3875"/>
              <adiabaticHead unit="kJ_per_kg" value="15.37754855203981"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.489499512003829"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4312.5"/>
              <adiabaticHead unit="kJ_per_kg" value="16.83533059426745"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.90893770944369"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4750"/>
              <adiabaticHead unit="kJ_per_kg" value="18.26788942113184"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.321118594281844"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5187.5"/>
              <adiabaticHead unit="kJ_per_kg" value="19.6797233387503"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.727336435040426"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5625"/>
              <adiabaticHead unit="kJ_per_kg" value="21.07475256265533"/>
              <volumetricFlowrate unit="m_cube_per_s" value="6.12871916997693"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6062.5"/>
              <adiabaticHead unit="kJ_per_kg" value="22.45644444615876"/>
              <volumetricFlowrate unit="m_cube_per_s" value="6.52626443823142"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6500"/>
              <adiabaticHead unit="kJ_per_kg" value="23.82790912989894"/>
              <volumetricFlowrate unit="m_cube_per_s" value="6.920867100452022"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.8049999999999999">
            <measurement>
              <speed unit="per_min" value="3000"/>
              <adiabaticHead unit="kJ_per_kg" value="10.74350829626445"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.448276507315224"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3437.5"/>
              <adiabaticHead unit="kJ_per_kg" value="11.97522797482079"/>
              <volumetricFlowrate unit="m_cube_per_s" value="4.951435995566579"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3875"/>
              <adiabaticHead unit="kJ_per_kg" value="13.17035052128795"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.439645495948096"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4312.5"/>
              <adiabaticHead unit="kJ_per_kg" value="14.33590107621249"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.915774789777583"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4750"/>
              <adiabaticHead unit="kJ_per_kg" value="15.47758319757913"/>
              <volumetricFlowrate unit="m_cube_per_s" value="6.382153789750898"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5187.5"/>
              <adiabaticHead unit="kJ_per_kg" value="16.60013657781255"/>
              <volumetricFlowrate unit="m_cube_per_s" value="6.840718667917891"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5625"/>
              <adiabaticHead unit="kJ_per_kg" value="17.70758337912941"/>
              <volumetricFlowrate unit="m_cube_per_s" value="7.293112484073606"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6062.5"/>
              <adiabaticHead unit="kJ_per_kg" value="18.80340321438018"/>
              <volumetricFlowrate unit="m_cube_per_s" value="7.74075666571622"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6500"/>
              <adiabaticHead unit="kJ_per_kg" value="19.89066091096669"/>
              <volumetricFlowrate unit="m_cube_per_s" value="8.184903199814801"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.77">
            <measurement>
              <speed unit="per_min" value="3000"/>
              <adiabaticHead unit="kJ_per_kg" value="8.909846137325173"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.227479726064721"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3437.5"/>
              <adiabaticHead unit="kJ_per_kg" value="9.858225747634245"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.778397481146687"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3875"/>
              <adiabaticHead unit="kJ_per_kg" value="10.77499422817074"/>
              <volumetricFlowrate unit="m_cube_per_s" value="6.310952196301804"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4312.5"/>
              <adiabaticHead unit="kJ_per_kg" value="11.6667707890201"/>
              <volumetricFlowrate unit="m_cube_per_s" value="6.828988998862054"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4750"/>
              <adiabaticHead unit="kJ_per_kg" value="12.5387901527284"/>
              <volumetricFlowrate unit="m_cube_per_s" value="7.335548761450814"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5187.5"/>
              <adiabaticHead unit="kJ_per_kg" value="13.39531118181914"/>
              <volumetricFlowrate unit="m_cube_per_s" value="7.833105475447844"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5625"/>
              <adiabaticHead unit="kJ_per_kg" value="14.23988683983758"/>
              <volumetricFlowrate unit="m_cube_per_s" value="8.323723072509802"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6062.5"/>
              <adiabaticHead unit="kJ_per_kg" value="15.07554938058946"/>
              <volumetricFlowrate unit="m_cube_per_s" value="8.809163001787782"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6500"/>
              <adiabaticHead unit="kJ_per_kg" value="15.90494161240273"/>
              <volumetricFlowrate unit="m_cube_per_s" value="9.290960481896066"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.735">
            <measurement>
              <speed unit="per_min" value="3000"/>
              <adiabaticHead unit="kJ_per_kg" value="6.968473215054769"/>
              <volumetricFlowrate unit="m_cube_per_s" value="5.942120315695041"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3437.5"/>
              <adiabaticHead unit="kJ_per_kg" value="7.65937639903389"/>
              <volumetricFlowrate unit="m_cube_per_s" value="6.527333973502579"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3875"/>
              <adiabaticHead unit="kJ_per_kg" value="8.325971974048173"/>
              <volumetricFlowrate unit="m_cube_per_s" value="7.09195842997956"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4312.5"/>
              <adiabaticHead unit="kJ_per_kg" value="8.973664751536381"/>
              <volumetricFlowrate unit="m_cube_per_s" value="7.640571706396089"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4750"/>
              <adiabaticHead unit="kJ_per_kg" value="9.606660255683529"/>
              <volumetricFlowrate unit="m_cube_per_s" value="8.176735995326148"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5187.5"/>
              <adiabaticHead unit="kJ_per_kg" value="10.22833727337156"/>
              <volumetricFlowrate unit="m_cube_per_s" value="8.703313220518218"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5625"/>
              <adiabaticHead unit="kJ_per_kg" value="10.84148760809449"/>
              <volumetricFlowrate unit="m_cube_per_s" value="9.222668114937067"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6062.5"/>
              <adiabaticHead unit="kJ_per_kg" value="11.44847703083226"/>
              <volumetricFlowrate unit="m_cube_per_s" value="9.736804550501086"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6500"/>
              <adiabaticHead unit="kJ_per_kg" value="12.05135732983856"/>
              <volumetricFlowrate unit="m_cube_per_s" value="10.247460447279"/>
            </measurement>
          </adiabaticEfficiency>
          <adiabaticEfficiency value="0.7">
            <measurement>
              <speed unit="per_min" value="3000"/>
              <adiabaticHead unit="kJ_per_kg" value="5.006424613104098"/>
              <volumetricFlowrate unit="m_cube_per_s" value="6.58605"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3437.5"/>
              <adiabaticHead unit="kJ_per_kg" value="5.471145890778382"/>
              <volumetricFlowrate unit="m_cube_per_s" value="7.195678742617567"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="3875"/>
              <adiabaticHead unit="kJ_per_kg" value="5.919242678467454"/>
              <volumetricFlowrate unit="m_cube_per_s" value="7.783499215605082"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4312.5"/>
              <adiabaticHead unit="kJ_per_kg" value="6.354571575879054"/>
              <volumetricFlowrate unit="m_cube_per_s" value="8.354570567625535"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="4750"/>
              <adiabaticHead unit="kJ_per_kg" value="6.780106819817763"/>
              <volumetricFlowrate unit="m_cube_per_s" value="8.912794449691114"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5187.5"/>
              <adiabaticHead unit="kJ_per_kg" value="7.19822252971075"/>
              <volumetricFlowrate unit="m_cube_per_s" value="9.461285269320349"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="5625"/>
              <adiabaticHead unit="kJ_per_kg" value="7.61087159307715"/>
              <volumetricFlowrate unit="m_cube_per_s" value="10.00260485533399"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6062.5"/>
              <adiabaticHead unit="kJ_per_kg" value="8.019704280661607"/>
              <volumetricFlowrate unit="m_cube_per_s" value="10.53891805906847"/>
            </measurement>
            <measurement>
              <speed unit="per_min" value="6500"/>
              <adiabaticHead unit="kJ_per_kg" value="8.42615"/>
              <volumetricFlowrate unit="m_cube_per_s" value="11.0721"/>
            </measurement>
          </adiabaticEfficiency>
        </characteristicDiagramMeasurements>
      </turboCompressor>
    </compressors>
    <drives>
      <gasTurbine id="drive_22">
        <energy_rate_fun_coeff_1 value="0.01"/>
        <energy_rate_fun_coeff_2 value="0"/>
        <energy_rate_fun_coeff_3 value="0"/>
        <power_fun_coeff_1 value="-1442.648933634083"/>
        <power_fun_coeff_2 value="4.675267484609608"/>
        <power_fun_coeff_3 value="-0.0002836130111153655"/>
        <power_fun_coeff_4 value="8.678398912399521"/>
        <power_fun_coeff_5 value="-0.02812453903903422"/>
        <power_fun_coeff_6 value="1.706102427155179e-06"/>
        <power_fun_coeff_7 value="-0.02884412308996772"/>
        <power_fun_coeff_8 value="9.34766509443856e-05"/>
        <power_fun_coeff_9 value="-5.670519286990249e-09"/>
      </gasTurbine>
    </drives>
    <configurations>
      <configuration nrOfSerialStages="1" confId="config_1">
        <stage nrOfParallelUnits="1" stageNr="1">
          <compressor nominalSpeed="6500" id="compressor_22"/>
        </stage>
      </configuration>
    </configurations>
  </compressorStation>
</compressorStations>

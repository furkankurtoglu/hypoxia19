 
# This file is auto-generated from a Python script that parses a PhysiCell configuration (.xml) file.
#
# Edit at your own risk.
#
import os
from ipywidgets import Label,Text,Checkbox,Button,HBox,VBox,FloatText,IntText,BoundedIntText,BoundedFloatText,Layout,Box
    
class UserTab(object):

    def __init__(self):
        
        micron_units = Label('micron')   # use "option m" (Mac, for micro symbol)

        constWidth = '180px'
        tab_height = '500px'
        stepsize = 10

        #style = {'description_width': '250px'}
        style = {'description_width': '25%'}
        layout = {'width': '400px'}

        name_button_layout={'width':'25%'}
        widget_layout = {'width': '15%'}
        units_button_layout ={'width':'15%'}
        desc_button_layout={'width':'45%'}

        param_name1 = Button(description='tumor_radius', disabled=True, layout=name_button_layout)
        param_name1.style.button_color = 'lightgreen'

        self.tumor_radius = FloatText(
          value=100.0,
          step=10,
          style=style, layout=widget_layout)

        param_name2 = Button(description='oncoprotein_mean', disabled=True, layout=name_button_layout)
        param_name2.style.button_color = 'tan'

        self.oncoprotein_mean = FloatText(
          value=1.0,
          step=0.1,
          style=style, layout=widget_layout)

        param_name3 = Button(description='oncoprotein_sd', disabled=True, layout=name_button_layout)
        param_name3.style.button_color = 'lightgreen'

        self.oncoprotein_sd = FloatText(
          value=0.25,
          step=0.01,
          style=style, layout=widget_layout)

        param_name4 = Button(description='oncoprotein_min', disabled=True, layout=name_button_layout)
        param_name4.style.button_color = 'tan'

        self.oncoprotein_min = FloatText(
          value=0.0,
          step=0.01,
          style=style, layout=widget_layout)

        param_name5 = Button(description='oncoprotein_max', disabled=True, layout=name_button_layout)
        param_name5.style.button_color = 'lightgreen'

        self.oncoprotein_max = FloatText(
          value=2,
          step=0.1,
          style=style, layout=widget_layout)

        param_name6 = Button(description='random_seed', disabled=True, layout=name_button_layout)
        param_name6.style.button_color = 'tan'

        self.random_seed = IntText(
          value=0,
          step=1,
          style=style, layout=widget_layout)

        param_name7 = Button(description='tumorphenotype', disabled=True, layout=name_button_layout)
        param_name7.style.button_color = 'lightgreen'

        self.tumorphenotype = Text(
          value='model1',
          style=style, layout=widget_layout)

        param_name8 = Button(description='color', disabled=True, layout=name_button_layout)
        param_name8.style.button_color = 'tan'

        self.color = Checkbox(
          value=True,
          style=style, layout=widget_layout)

        param_name9 = Button(description='default_production_rateRFP', disabled=True, layout=name_button_layout)
        param_name9.style.button_color = 'lightgreen'

        self.default_production_rateRFP = FloatText(
          value=206.54375,
          step=10,
          style=style, layout=widget_layout)

        param_name10 = Button(description='default_production_rateGFP', disabled=True, layout=name_button_layout)
        param_name10.style.button_color = 'tan'

        self.default_production_rateGFP = FloatText(
          value=1.6814e-4,
          step=1e-05,
          style=style, layout=widget_layout)

        param_name11 = Button(description='default_degradation_rateRFP', disabled=True, layout=name_button_layout)
        param_name11.style.button_color = 'lightgreen'

        self.default_degradation_rateRFP = FloatText(
          value=8.526e-5,
          step=1e-05,
          style=style, layout=widget_layout)

        param_name12 = Button(description='default_degradation_rateGFP', disabled=True, layout=name_button_layout)
        param_name12.style.button_color = 'tan'

        self.default_degradation_rateGFP = FloatText(
          value=1.4775e-8,
          step=1e-09,
          style=style, layout=widget_layout)

        param_name13 = Button(description='O2_proliferation_saturation', disabled=True, layout=name_button_layout)
        param_name13.style.button_color = 'lightgreen'

        self.O2_proliferation_saturation = FloatText(
          value=38.0,
          step=1,
          style=style, layout=widget_layout)

        param_name14 = Button(description='is_motile', disabled=True, layout=name_button_layout)
        param_name14.style.button_color = 'tan'

        self.is_motile = Checkbox(
          value=True,
          style=style, layout=widget_layout)

        param_name15 = Button(description='persistence_time', disabled=True, layout=name_button_layout)
        param_name15.style.button_color = 'lightgreen'

        self.persistence_time = FloatText(
          value=15.0,
          step=1,
          style=style, layout=widget_layout)

        param_name16 = Button(description='migration_bias', disabled=True, layout=name_button_layout)
        param_name16.style.button_color = 'tan'

        self.migration_bias = FloatText(
          value=0.5,
          step=0.1,
          style=style, layout=widget_layout)

        param_name17 = Button(description='migration_speed', disabled=True, layout=name_button_layout)
        param_name17.style.button_color = 'lightgreen'

        self.migration_speed = FloatText(
          value=0.05,
          step=0.01,
          style=style, layout=widget_layout)

        param_name18 = Button(description='O2_secretion_rate_constant', disabled=True, layout=name_button_layout)
        param_name18.style.button_color = 'tan'

        self.O2_secretion_rate_constant = FloatText(
          value=0.0,
          step=0.01,
          style=style, layout=widget_layout)

        param_name19 = Button(description='O2_uptake_rate_constant', disabled=True, layout=name_button_layout)
        param_name19.style.button_color = 'lightgreen'

        self.O2_uptake_rate_constant = FloatText(
          value=10.0,
          step=1,
          style=style, layout=widget_layout)

        param_name20 = Button(description='O2_saturation_density', disabled=True, layout=name_button_layout)
        param_name20.style.button_color = 'tan'

        self.O2_saturation_density = FloatText(
          value=38.0,
          step=1,
          style=style, layout=widget_layout)

        param_name21 = Button(description='VEGF_secretion_rate_constant_normoxia', disabled=True, layout=name_button_layout)
        param_name21.style.button_color = 'lightgreen'

        self.VEGF_secretion_rate_constant_normoxia = FloatText(
          value=0.0,
          step=0.01,
          style=style, layout=widget_layout)

        param_name22 = Button(description='VEGF_uptake_rate_constant', disabled=True, layout=name_button_layout)
        param_name22.style.button_color = 'tan'

        self.VEGF_uptake_rate_constant = FloatText(
          value=0,
          step=0.01,
          style=style, layout=widget_layout)

        param_name23 = Button(description='VEGF_saturation_density', disabled=True, layout=name_button_layout)
        param_name23.style.button_color = 'lightgreen'

        self.VEGF_saturation_density = FloatText(
          value=1.0,
          step=0.1,
          style=style, layout=widget_layout)

        param_name24 = Button(description='O2_Dirichlet_Condition', disabled=True, layout=name_button_layout)
        param_name24.style.button_color = 'tan'

        self.O2_Dirichlet_Condition = FloatText(
          value=90.0,
          step=1,
          style=style, layout=widget_layout)

        param_name25 = Button(description='tumor_confluence', disabled=True, layout=name_button_layout)
        param_name25.style.button_color = 'lightgreen'

        self.tumor_confluence = FloatText(
          value=0.95,
          step=0.1,
          style=style, layout=widget_layout)

        param_name26 = Button(description='tumore_radius', disabled=True, layout=name_button_layout)
        param_name26.style.button_color = 'tan'

        self.tumore_radius = FloatText(
          value=250,
          step=10,
          style=style, layout=widget_layout)

        param_name27 = Button(description='leader_fraction', disabled=True, layout=name_button_layout)
        param_name27.style.button_color = 'lightgreen'

        self.leader_fraction = FloatText(
          value=0.1,
          step=0.01,
          style=style, layout=widget_layout)

        param_name28 = Button(description='FP_hypoxic_switch', disabled=True, layout=name_button_layout)
        param_name28.style.button_color = 'tan'

        self.FP_hypoxic_switch = FloatText(
          value=10.0,
          step=1,
          style=style, layout=widget_layout)

        param_name29 = Button(description='phenotype_hypoxic_switch', disabled=True, layout=name_button_layout)
        param_name29.style.button_color = 'lightgreen'

        self.phenotype_hypoxic_switch = FloatText(
          value=10.0,
          step=1,
          style=style, layout=widget_layout)

        param_name30 = Button(description='VEGF_secretion_rate_constant_hypoxia', disabled=True, layout=name_button_layout)
        param_name30.style.button_color = 'tan'

        self.VEGF_secretion_rate_constant_hypoxia = FloatText(
          value=10.0,
          step=1,
          style=style, layout=widget_layout)

        param_name31 = Button(description='max_vascular_density', disabled=True, layout=name_button_layout)
        param_name31.style.button_color = 'lightgreen'

        self.max_vascular_density = FloatText(
          value=1.0,
          step=0.1,
          style=style, layout=widget_layout)

        param_name32 = Button(description='vascular_degradation_rate_per_cell', disabled=True, layout=name_button_layout)
        param_name32.style.button_color = 'tan'

        self.vascular_degradation_rate_per_cell = FloatText(
          value=0.001,
          step=0.0001,
          style=style, layout=widget_layout)

        param_name33 = Button(description='rQ', disabled=True, layout=name_button_layout)
        param_name33.style.button_color = 'lightgreen'

        self.rQ = FloatText(
          value=0.004605,
          step=0.001,
          style=style, layout=widget_layout)

        param_name34 = Button(description='r1', disabled=True, layout=name_button_layout)
        param_name34.style.button_color = 'tan'

        self.r1 = FloatText(
          value=0.001282,
          step=0.0001,
          style=style, layout=widget_layout)

        param_name35 = Button(description='r2', disabled=True, layout=name_button_layout)
        param_name35.style.button_color = 'lightgreen'

        self.r2 = FloatText(
          value=0.0066667,
          step=0.001,
          style=style, layout=widget_layout)

        param_name36 = Button(description='rA', disabled=True, layout=name_button_layout)
        param_name36.style.button_color = 'tan'

        self.rA = FloatText(
          value=0.0000387,
          step=1e-05,
          style=style, layout=widget_layout)

        units_button1 = Button(description='micron', disabled=True, layout=units_button_layout) 
        units_button1.style.button_color = 'lightgreen'
        units_button2 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button2.style.button_color = 'tan'
        units_button3 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button3.style.button_color = 'lightgreen'
        units_button4 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button4.style.button_color = 'tan'
        units_button5 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button5.style.button_color = 'lightgreen'
        units_button6 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button6.style.button_color = 'tan'
        units_button7 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button7.style.button_color = 'lightgreen'
        units_button8 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button8.style.button_color = 'tan'
        units_button9 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button9.style.button_color = 'lightgreen'
        units_button10 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button10.style.button_color = 'tan'
        units_button11 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button11.style.button_color = 'lightgreen'
        units_button12 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button12.style.button_color = 'tan'
        units_button13 = Button(description='mmHg', disabled=True, layout=units_button_layout) 
        units_button13.style.button_color = 'lightgreen'
        units_button14 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button14.style.button_color = 'tan'
        units_button15 = Button(description='min', disabled=True, layout=units_button_layout) 
        units_button15.style.button_color = 'lightgreen'
        units_button16 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button16.style.button_color = 'tan'
        units_button17 = Button(description='micron/min', disabled=True, layout=units_button_layout) 
        units_button17.style.button_color = 'lightgreen'
        units_button18 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button18.style.button_color = 'tan'
        units_button19 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button19.style.button_color = 'lightgreen'
        units_button20 = Button(description='mmHg', disabled=True, layout=units_button_layout) 
        units_button20.style.button_color = 'tan'
        units_button21 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button21.style.button_color = 'lightgreen'
        units_button22 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button22.style.button_color = 'tan'
        units_button23 = Button(description='mmHg', disabled=True, layout=units_button_layout) 
        units_button23.style.button_color = 'lightgreen'
        units_button24 = Button(description='mmHg', disabled=True, layout=units_button_layout) 
        units_button24.style.button_color = 'tan'
        units_button25 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button25.style.button_color = 'lightgreen'
        units_button26 = Button(description='micron', disabled=True, layout=units_button_layout) 
        units_button26.style.button_color = 'tan'
        units_button27 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button27.style.button_color = 'lightgreen'
        units_button28 = Button(description='mmHg', disabled=True, layout=units_button_layout) 
        units_button28.style.button_color = 'tan'
        units_button29 = Button(description='mmHg', disabled=True, layout=units_button_layout) 
        units_button29.style.button_color = 'lightgreen'
        units_button30 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button30.style.button_color = 'tan'
        units_button31 = Button(description='mmHg', disabled=True, layout=units_button_layout) 
        units_button31.style.button_color = 'lightgreen'
        units_button32 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button32.style.button_color = 'tan'
        units_button33 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button33.style.button_color = 'lightgreen'
        units_button34 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button34.style.button_color = 'tan'
        units_button35 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button35.style.button_color = 'lightgreen'
        units_button36 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button36.style.button_color = 'tan'

        desc_button1 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button1.style.button_color = 'lightgreen'
        desc_button2 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button2.style.button_color = 'tan'
        desc_button3 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button3.style.button_color = 'lightgreen'
        desc_button4 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button4.style.button_color = 'tan'
        desc_button5 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button5.style.button_color = 'lightgreen'
        desc_button6 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button6.style.button_color = 'tan'
        desc_button7 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button7.style.button_color = 'lightgreen'
        desc_button8 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button8.style.button_color = 'tan'
        desc_button9 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button9.style.button_color = 'lightgreen'
        desc_button10 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button10.style.button_color = 'tan'
        desc_button11 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button11.style.button_color = 'lightgreen'
        desc_button12 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button12.style.button_color = 'tan'
        desc_button13 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button13.style.button_color = 'lightgreen'
        desc_button14 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button14.style.button_color = 'tan'
        desc_button15 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button15.style.button_color = 'lightgreen'
        desc_button16 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button16.style.button_color = 'tan'
        desc_button17 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button17.style.button_color = 'lightgreen'
        desc_button18 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button18.style.button_color = 'tan'
        desc_button19 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button19.style.button_color = 'lightgreen'
        desc_button20 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button20.style.button_color = 'tan'
        desc_button21 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button21.style.button_color = 'lightgreen'
        desc_button22 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button22.style.button_color = 'tan'
        desc_button23 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button23.style.button_color = 'lightgreen'
        desc_button24 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button24.style.button_color = 'tan'
        desc_button25 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button25.style.button_color = 'lightgreen'
        desc_button26 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button26.style.button_color = 'tan'
        desc_button27 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button27.style.button_color = 'lightgreen'
        desc_button28 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button28.style.button_color = 'tan'
        desc_button29 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button29.style.button_color = 'lightgreen'
        desc_button30 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button30.style.button_color = 'tan'
        desc_button31 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button31.style.button_color = 'lightgreen'
        desc_button32 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button32.style.button_color = 'tan'
        desc_button33 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button33.style.button_color = 'lightgreen'
        desc_button34 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button34.style.button_color = 'tan'
        desc_button35 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button35.style.button_color = 'lightgreen'
        desc_button36 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button36.style.button_color = 'tan'

        row1 = [param_name1, self.tumor_radius, units_button1, desc_button1] 
        row2 = [param_name2, self.oncoprotein_mean, units_button2, desc_button2] 
        row3 = [param_name3, self.oncoprotein_sd, units_button3, desc_button3] 
        row4 = [param_name4, self.oncoprotein_min, units_button4, desc_button4] 
        row5 = [param_name5, self.oncoprotein_max, units_button5, desc_button5] 
        row6 = [param_name6, self.random_seed, units_button6, desc_button6] 
        row7 = [param_name7, self.tumorphenotype, units_button7, desc_button7] 
        row8 = [param_name8, self.color, units_button8, desc_button8] 
        row9 = [param_name9, self.default_production_rateRFP, units_button9, desc_button9] 
        row10 = [param_name10, self.default_production_rateGFP, units_button10, desc_button10] 
        row11 = [param_name11, self.default_degradation_rateRFP, units_button11, desc_button11] 
        row12 = [param_name12, self.default_degradation_rateGFP, units_button12, desc_button12] 
        row13 = [param_name13, self.O2_proliferation_saturation, units_button13, desc_button13] 
        row14 = [param_name14, self.is_motile, units_button14, desc_button14] 
        row15 = [param_name15, self.persistence_time, units_button15, desc_button15] 
        row16 = [param_name16, self.migration_bias, units_button16, desc_button16] 
        row17 = [param_name17, self.migration_speed, units_button17, desc_button17] 
        row18 = [param_name18, self.O2_secretion_rate_constant, units_button18, desc_button18] 
        row19 = [param_name19, self.O2_uptake_rate_constant, units_button19, desc_button19] 
        row20 = [param_name20, self.O2_saturation_density, units_button20, desc_button20] 
        row21 = [param_name21, self.VEGF_secretion_rate_constant_normoxia, units_button21, desc_button21] 
        row22 = [param_name22, self.VEGF_uptake_rate_constant, units_button22, desc_button22] 
        row23 = [param_name23, self.VEGF_saturation_density, units_button23, desc_button23] 
        row24 = [param_name24, self.O2_Dirichlet_Condition, units_button24, desc_button24] 
        row25 = [param_name25, self.tumor_confluence, units_button25, desc_button25] 
        row26 = [param_name26, self.tumore_radius, units_button26, desc_button26] 
        row27 = [param_name27, self.leader_fraction, units_button27, desc_button27] 
        row28 = [param_name28, self.FP_hypoxic_switch, units_button28, desc_button28] 
        row29 = [param_name29, self.phenotype_hypoxic_switch, units_button29, desc_button29] 
        row30 = [param_name30, self.VEGF_secretion_rate_constant_hypoxia, units_button30, desc_button30] 
        row31 = [param_name31, self.max_vascular_density, units_button31, desc_button31] 
        row32 = [param_name32, self.vascular_degradation_rate_per_cell, units_button32, desc_button32] 
        row33 = [param_name33, self.rQ, units_button33, desc_button33] 
        row34 = [param_name34, self.r1, units_button34, desc_button34] 
        row35 = [param_name35, self.r2, units_button35, desc_button35] 
        row36 = [param_name36, self.rA, units_button36, desc_button36] 

        box_layout = Layout(display='flex', flex_flow='row', align_items='stretch', width='100%')
        box1 = Box(children=row1, layout=box_layout)
        box2 = Box(children=row2, layout=box_layout)
        box3 = Box(children=row3, layout=box_layout)
        box4 = Box(children=row4, layout=box_layout)
        box5 = Box(children=row5, layout=box_layout)
        box6 = Box(children=row6, layout=box_layout)
        box7 = Box(children=row7, layout=box_layout)
        box8 = Box(children=row8, layout=box_layout)
        box9 = Box(children=row9, layout=box_layout)
        box10 = Box(children=row10, layout=box_layout)
        box11 = Box(children=row11, layout=box_layout)
        box12 = Box(children=row12, layout=box_layout)
        box13 = Box(children=row13, layout=box_layout)
        box14 = Box(children=row14, layout=box_layout)
        box15 = Box(children=row15, layout=box_layout)
        box16 = Box(children=row16, layout=box_layout)
        box17 = Box(children=row17, layout=box_layout)
        box18 = Box(children=row18, layout=box_layout)
        box19 = Box(children=row19, layout=box_layout)
        box20 = Box(children=row20, layout=box_layout)
        box21 = Box(children=row21, layout=box_layout)
        box22 = Box(children=row22, layout=box_layout)
        box23 = Box(children=row23, layout=box_layout)
        box24 = Box(children=row24, layout=box_layout)
        box25 = Box(children=row25, layout=box_layout)
        box26 = Box(children=row26, layout=box_layout)
        box27 = Box(children=row27, layout=box_layout)
        box28 = Box(children=row28, layout=box_layout)
        box29 = Box(children=row29, layout=box_layout)
        box30 = Box(children=row30, layout=box_layout)
        box31 = Box(children=row31, layout=box_layout)
        box32 = Box(children=row32, layout=box_layout)
        box33 = Box(children=row33, layout=box_layout)
        box34 = Box(children=row34, layout=box_layout)
        box35 = Box(children=row35, layout=box_layout)
        box36 = Box(children=row36, layout=box_layout)

        self.tab = VBox([
          box1,
          box2,
          box3,
          box4,
          box5,
          box6,
          box7,
          box8,
          box9,
          box10,
          box11,
          box12,
          box13,
          box14,
          box15,
          box16,
          box17,
          box18,
          box19,
          box20,
          box21,
          box22,
          box23,
          box24,
          box25,
          box26,
          box27,
          box28,
          box29,
          box30,
          box31,
          box32,
          box33,
          box34,
          box35,
          box36,
        ])

    # Populate the GUI widgets with values from the XML
    def fill_gui(self, xml_root):
        uep = xml_root.find('.//user_parameters')  # find unique entry point into XML
        self.tumor_radius.value = float(uep.find('.//tumor_radius').text)
        self.oncoprotein_mean.value = float(uep.find('.//oncoprotein_mean').text)
        self.oncoprotein_sd.value = float(uep.find('.//oncoprotein_sd').text)
        self.oncoprotein_min.value = float(uep.find('.//oncoprotein_min').text)
        self.oncoprotein_max.value = float(uep.find('.//oncoprotein_max').text)
        self.random_seed.value = int(uep.find('.//random_seed').text)
        self.tumorphenotype.value = (uep.find('.//tumorphenotype').text)
        self.color.value = ('true' == (uep.find('.//color').text.lower()) )
        self.default_production_rateRFP.value = float(uep.find('.//default_production_rateRFP').text)
        self.default_production_rateGFP.value = float(uep.find('.//default_production_rateGFP').text)
        self.default_degradation_rateRFP.value = float(uep.find('.//default_degradation_rateRFP').text)
        self.default_degradation_rateGFP.value = float(uep.find('.//default_degradation_rateGFP').text)
        self.O2_proliferation_saturation.value = float(uep.find('.//O2_proliferation_saturation').text)
        self.is_motile.value = ('true' == (uep.find('.//is_motile').text.lower()) )
        self.persistence_time.value = float(uep.find('.//persistence_time').text)
        self.migration_bias.value = float(uep.find('.//migration_bias').text)
        self.migration_speed.value = float(uep.find('.//migration_speed').text)
        self.O2_secretion_rate_constant.value = float(uep.find('.//O2_secretion_rate_constant').text)
        self.O2_uptake_rate_constant.value = float(uep.find('.//O2_uptake_rate_constant').text)
        self.O2_saturation_density.value = float(uep.find('.//O2_saturation_density').text)
        self.VEGF_secretion_rate_constant_normoxia.value = float(uep.find('.//VEGF_secretion_rate_constant_normoxia').text)
        self.VEGF_uptake_rate_constant.value = float(uep.find('.//VEGF_uptake_rate_constant').text)
        self.VEGF_saturation_density.value = float(uep.find('.//VEGF_saturation_density').text)
        self.O2_Dirichlet_Condition.value = float(uep.find('.//O2_Dirichlet_Condition').text)
        self.tumor_confluence.value = float(uep.find('.//tumor_confluence').text)
        self.tumore_radius.value = float(uep.find('.//tumore_radius').text)
        self.leader_fraction.value = float(uep.find('.//leader_fraction').text)
        self.FP_hypoxic_switch.value = float(uep.find('.//FP_hypoxic_switch').text)
        self.phenotype_hypoxic_switch.value = float(uep.find('.//phenotype_hypoxic_switch').text)
        self.VEGF_secretion_rate_constant_hypoxia.value = float(uep.find('.//VEGF_secretion_rate_constant_hypoxia').text)
        self.max_vascular_density.value = float(uep.find('.//max_vascular_density').text)
        self.vascular_degradation_rate_per_cell.value = float(uep.find('.//vascular_degradation_rate_per_cell').text)
        self.rQ.value = float(uep.find('.//rQ').text)
        self.r1.value = float(uep.find('.//r1').text)
        self.r2.value = float(uep.find('.//r2').text)
        self.rA.value = float(uep.find('.//rA').text)


    # Read values from the GUI widgets to enable editing XML
    def fill_xml(self, xml_root):
        uep = xml_root.find('.//user_parameters')  # find unique entry point into XML 
        uep.find('.//tumor_radius').text = str(self.tumor_radius.value)
        uep.find('.//oncoprotein_mean').text = str(self.oncoprotein_mean.value)
        uep.find('.//oncoprotein_sd').text = str(self.oncoprotein_sd.value)
        uep.find('.//oncoprotein_min').text = str(self.oncoprotein_min.value)
        uep.find('.//oncoprotein_max').text = str(self.oncoprotein_max.value)
        uep.find('.//random_seed').text = str(self.random_seed.value)
        uep.find('.//tumorphenotype').text = str(self.tumorphenotype.value)
        uep.find('.//color').text = str(self.color.value)
        uep.find('.//default_production_rateRFP').text = str(self.default_production_rateRFP.value)
        uep.find('.//default_production_rateGFP').text = str(self.default_production_rateGFP.value)
        uep.find('.//default_degradation_rateRFP').text = str(self.default_degradation_rateRFP.value)
        uep.find('.//default_degradation_rateGFP').text = str(self.default_degradation_rateGFP.value)
        uep.find('.//O2_proliferation_saturation').text = str(self.O2_proliferation_saturation.value)
        uep.find('.//is_motile').text = str(self.is_motile.value)
        uep.find('.//persistence_time').text = str(self.persistence_time.value)
        uep.find('.//migration_bias').text = str(self.migration_bias.value)
        uep.find('.//migration_speed').text = str(self.migration_speed.value)
        uep.find('.//O2_secretion_rate_constant').text = str(self.O2_secretion_rate_constant.value)
        uep.find('.//O2_uptake_rate_constant').text = str(self.O2_uptake_rate_constant.value)
        uep.find('.//O2_saturation_density').text = str(self.O2_saturation_density.value)
        uep.find('.//VEGF_secretion_rate_constant_normoxia').text = str(self.VEGF_secretion_rate_constant_normoxia.value)
        uep.find('.//VEGF_uptake_rate_constant').text = str(self.VEGF_uptake_rate_constant.value)
        uep.find('.//VEGF_saturation_density').text = str(self.VEGF_saturation_density.value)
        uep.find('.//O2_Dirichlet_Condition').text = str(self.O2_Dirichlet_Condition.value)
        uep.find('.//tumor_confluence').text = str(self.tumor_confluence.value)
        uep.find('.//tumore_radius').text = str(self.tumore_radius.value)
        uep.find('.//leader_fraction').text = str(self.leader_fraction.value)
        uep.find('.//FP_hypoxic_switch').text = str(self.FP_hypoxic_switch.value)
        uep.find('.//phenotype_hypoxic_switch').text = str(self.phenotype_hypoxic_switch.value)
        uep.find('.//VEGF_secretion_rate_constant_hypoxia').text = str(self.VEGF_secretion_rate_constant_hypoxia.value)
        uep.find('.//max_vascular_density').text = str(self.max_vascular_density.value)
        uep.find('.//vascular_degradation_rate_per_cell').text = str(self.vascular_degradation_rate_per_cell.value)
        uep.find('.//rQ').text = str(self.rQ.value)
        uep.find('.//r1').text = str(self.r1.value)
        uep.find('.//r2').text = str(self.r2.value)
        uep.find('.//rA').text = str(self.rA.value)

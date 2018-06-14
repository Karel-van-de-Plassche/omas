# -*- coding: utf-8 -*-
"""
Time in OMAS
============
This example illustrates how OMAS can handle the time dimension
"""

from __future__ import print_function, division, unicode_literals

from omas import *

# test generation of a sample ods
ods = ODS()
ods['equilibrium.time_slice'][0]['time'] = 100
ods['equilibrium.time_slice.0.global_quantities.ip'] = 0.0
ods['equilibrium.time_slice'][1]['time'] = 200
ods['equilibrium.time_slice.1.global_quantities.ip'] = 1.0
ods['equilibrium.time_slice'][2]['time'] = 300
ods['equilibrium.time_slice.1.global_quantities.ip'] = 2.0

# get time information from children
extra_info = {}
print(ods.time('equilibrium', extra_info=extra_info))
print(extra_info)

# show use of .homogeneous_time property
print(ods.homogeneous_time('equilibrium'))

# time arrays can be set using `set_time_array` function
# this simplifies the logic in the code since one does not
# have to check if the array was already there or not
ods.set_time_array('equilibrium.time',0,100)
ods.set_time_array('equilibrium.time',1,200)
ods.set_time_array('equilibrium.time',2,300)

# get time information from explicitly set time array
extra_info = {}
print(ods.time('equilibrium', extra_info=extra_info))
print(extra_info)

# get time value from item in array of structures
extra_info = {}
print(ods['equilibrium.time_slice'][0].time(extra_info=extra_info))
print(extra_info)

# get time array from array of structures
extra_info = {}
print(ods['equilibrium.time_slice'].time(extra_info=extra_info))
print(extra_info)

# get time from parent
extra_info = {}
print(ods.time('equilibrium.time_slice.0.global_quantities.ip', extra_info=extra_info))
print(extra_info)

# slice at time
ods1 = ods['equilibrium'].slice_at_time(100)
print(ods.time('equilibrium'))
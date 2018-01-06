from __future__ import print_function, division, unicode_literals

import os
os.environ['OMAS_DEBUG_TOPIC'] = 'imas'

from omfit.classes.omfit_eqdsk import OMFITgeqdsk, OMFITsrc
from omas import *

# read gEQDSK file in OMFIT
eq = OMFITgeqdsk(OMFITsrc + '/../samples/g133221.01000')

# convert gEQDSK to OMAS data structure
ods = eq.to_omas()

# save OMAS data structure to IMAS
paths = save_omas_imas(ods, tokamak='DIII-D', shot=133221, new=True)

# load OMAS data structure from IMAS
ods1 = load_omas_imas(tokamak='DIII-D', shot=133221, paths=paths)

# generate gEQDSK file from OMAS data structure
eq1 = OMFITgeqdsk('g133221.02000').from_omas(ods1)

# save gEQDSK file
eq1.deploy('g133221.02000')

from distutils.core import setup

import sys
if sys.version_info < (2,7):
    sys.exit('Sorry, Python < 2.7 is not supported')

setup(
    name='telemarketer_tycoon',
    version='0.1',
    packages=['telemarketer_tycoon'],
    url='',
    license='',
    author='GrowthIntel Developers',
    author_email='developers@growthintel.com',
    description=''
)

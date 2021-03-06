import os

from NextBus import NextBus

### MAIN FUNCTION	

# data directory
sDirectory = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data/')

# MBTA information
sAgency = "mbta"
lLines = ['1', '83']

# instantiate a NextBus object
MBTA = NextBus(sAgency, sDirectory)

# iteratively poll for route predictions
for sLineID in lLines:
    MBTA.poll(sLineID)
    print MBTA.lines[sLineID]

exit()
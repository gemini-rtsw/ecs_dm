#!/bin/csh -f

# for two PLCs, where Plant Room PLC addresses are where they should be
#dm ECS_Sim.dl top=ec:,gis=gis:,m1=m1:,gws=ws:,pr=ec:thermalS &

# for one plc, where Plant Room PLC addresses are tacked on at the 
# top of the Carousel PLC by adding a "4" prefix
setenv EPICS_DISPLAY_PATH $GEMINI_TOP/share/dl/ecs
dm2-4 ECS_Sim.dl top=ec:,gis=gis:,m1=m1:,gws=ws:,th=ec:thermalS4 &



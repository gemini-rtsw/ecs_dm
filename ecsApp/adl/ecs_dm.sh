#!/bin/csh -f

# for two PLCs, where Plant Room PLC addresses are where they should be
#dm ECS_Master.dl top=ec:,m1=m1:,gws=ws:,sad=ec:sad:,pr=thermalword &

# for one plc, where Plant Room PLC addresses are tacked on at the 
# top of the Carousel PLC by adding a "4" prefix
setenv EPICS_DISPLAY_PATH $GEMINI_TOP/share/dl/ecs
dm2-4 ECS_Master.dl top=ec:,m1=m1:,gws=ws:,sad=ec:sad:,pr=thermalword4 &


#!/bin/bash

source /etc/profile

 #for two PLCs, where Plant Room PLC addresses are where they should be
export EPICS_DISPLAY_PATH=.:$GEMINI_TOP/share/dl/ecs

export EPICS_DISPLAY_PATH=.:$GEMINI_TOP/share/dl/ecs/data_CP
export EPICS_CA_ADDR_LIST="172.17.2.255"

#dm ECS_Master.dl top=ec:,m1=m1:,gws=ws:,sad=ec:sad:,pr=thermalword &

# for one plc, where Plant Room PLC addresses are tacked on at the 
# top of the Carousel PLC by adding a "4" prefix
dm2-4 -iconic ECS_Master.dl top=ec:,m1=m1:,gws=ws:,sad=ec:sad:,pr=pr1:, th=thermalword4, ahu=ahu:, elec=elec:, ch=ch:, ef=ef: &


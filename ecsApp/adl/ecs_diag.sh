#!/bin/csh -f

# For two PLC prstat should be 0
#dm2.4 Diag_Master.dl top=ec:,m1=m1:,gws=ws:,sad=ec:sad:,prstat=0 &

# For one PLC prstat should be 40
setenv EPICS_DISPLAY_PATH $GEMINI_TOP/share/dl/ecs
dm2-4 Diag_Master.dl top=ec:,m1=m1:,gws=ws:,sad=ec:sad:,prstat=40 &

#!/bin/csh -f
setenv EPICS_DISPLAY_PATH $GEMINI_TOP/share/dl/ecs
dm2-4 Test_Master.dl top=ec:

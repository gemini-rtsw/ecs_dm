TOP = ../../..

include $(TOP)/configure/CONFIG
INSTALL_DATA = $(INSTALL_LOCATION)/data_MK

DATA    =  colorsMK.dl template.dl \
           $(patsubst ../%.adl, %.dl, $(wildcard ../*.adl ../*.bit ../*.cfg ../*.tk ../*.test))

SCRIPTS_HOST  += $(wildcard ../*.sh)

include $(TOP)/configure/RULES


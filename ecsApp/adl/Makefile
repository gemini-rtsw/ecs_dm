TOP = ../..

include $(TOP)/configure/CONFIG

DATA    =  colors.dl template.dl \
           $(patsubst ../%.adl, %.dl, $(wildcard ../*.adl ../*.bit ../*.cfg ../*.tk ../*.test))

SCRIPTS_HOST  += $(wildcard ../*.sh)

include $(TOP)/configure/RULES
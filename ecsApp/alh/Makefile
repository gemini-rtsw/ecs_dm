TOP = ../..

include $(TOP)/configure/CONFIG

# Create an alarm file for the standard cr: database

MOD = ecs

# Alarm handler files to put into the DATA directory

DATA	= $(MOD).config

include $(TOP)/configure/RULES

$(MOD).config: ../$(MOD).alh
	sed -e 's/$$(top)/$(MOD):/' $^ > $@

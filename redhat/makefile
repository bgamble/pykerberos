RPMDIR := $(PWD)/redhat
PYTHON := python26
SUBDIRS := BUILD RPMS SOURCES SPECS SRPMS
DIRS := $(foreach subdir,$(SUBDIRS),$(RPMDIR)/$(subdir))

rpm: init
	python setup.py sdist -d $(RPMDIR)/SOURCES
	rpmbuild --define "_topdir $(RPMDIR)" --define "python $(PYTHON)" -ba $(RPMDIR)/kerberos.spec

init: testdir
	mkdir -p $(DIRS)

clean: testdir
	rm -rf $(DIRS)

testdir:
ifeq ($(wildcard setup.py),)
	$(error Must be run from same directory as setup.py)
endif

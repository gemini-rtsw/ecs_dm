%define debug_package %{nil}
%define _build_id_links none

%define name ecs
%define gemopt opt
%define version 3.2
%define release 1
%define repository gemini
%define _prefix /gemsoft
%define epics_arch linux-x86_64

# $GIT_HASH first: build_rpm.sh computes the hash on the HOST and passes it
# into the build container. A bare `git rev-parse` resolves to "nogit"
# whenever git is absent from the builder or trips dubious-ownership, and the
# Release would then no longer name the commit the package came from.
%define git_hash %(if [ -n "$GIT_HASH" ]; then echo "$GIT_HASH"; else git rev-parse --short HEAD 2>/dev/null || echo nogit; fi)

Summary: %{name} Package
Name: %{name}
Version: %{version}
Release: %{release}.%{git_hash}.%{repository}%{?dist}
License: GPL
Group: Gemini
BuildRoot: /var/tmp/%{name}-%{version}-root
Source0: %{name}-%{version}.tar.gz
BuildArch: x86_64
Prefix: %{_prefix}

## You may specify dependencies here
#
# Pinned exactly, and with %%{?dist}. The rpm-repo is flat -- el8 and el9 share
# one repo with no dist filtering -- so an unversioned epics-base-devel
# resolves to the highest EVR in it, which is the EPICS 7 build under
# /gem_base: a different tree entirely from the 3.14.12 one configure/RELEASE
# points at, and the build then fails on missing rules.
#
# opiGEM supplies adl2dl (.adl -> .dl) and dm2-4; alh is not needed to build
# ecs.config, but a dev image without it cannot open the alarm handler on it.
# perl IS the EPICS 3.14.12 build system -- convertRelease.pl and
# installEpics.pl drive every install step -- and the Rocky base image ships
# the interpreter without the core modules they use (FindBin, File::Copy).
BuildRequires: epics-base-devel = 3.14.12-10%{?dist}.gemini
BuildRequires: epics_extension-opiGEM-devel = 1.0-11%{?dist}.gemini
BuildRequires: epics_extension-alh = 1.3.0-1%{?dist}.gemini
BuildRequires: perl
Requires: epics_extension-opiGEM epics_extension-alh
## Switch dependency checking off
# AutoReqProv: no

%description
Package %{name} provides the DM screens for the module ecs.

%package ws
Summary: %{name}-ws Package
Group: Gemini
Requires: epics_extension-opiGEM epics_extension-alh
%description ws
Package %{name}-ws provides the DM screens for the module ecs.

%prep
%setup -n %{name}-%{version}

%build
# adl2dl lives in epics_extension-opiGEM. EPICS base defaults ADL2DL to the
# bare name "adl2dl" and the ADE profile points EPICS_EXTENSIONS at
# /gem_base/epics/extensions, which holds no converter -- so without this the
# build dies with "adl2dl: No such file or directory" on the first screen.
export PATH=%{_prefix}/%{gemopt}/epics/extensions/bin/%{epics_arch}:$PATH
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_prefix}/share/dl/%{name}/data_CP
mkdir -p $RPM_BUILD_ROOT/%{_prefix}/share/dl/%{name}/data_MK
mkdir -p $RPM_BUILD_ROOT/%{_prefix}/share/alh/%{name}
mkdir -p $RPM_BUILD_ROOT/%{_prefix}/bin/
mkdir -p $RPM_BUILD_ROOT/etc/profile.d/

cp -r bin/%{epics_arch}/* $RPM_BUILD_ROOT/%{_prefix}/bin/
cp -r data_CP/*.dl $RPM_BUILD_ROOT/%{_prefix}/share/dl/%{name}/data_CP
cp -r data_MK/*.dl $RPM_BUILD_ROOT/%{_prefix}/share/dl/%{name}/data_MK
cp -r data/*.config $RPM_BUILD_ROOT/%{_prefix}/share/alh/%{name}

# Create profile.d script to set PATH for all users
cat > $RPM_BUILD_ROOT/etc/profile.d/ecs-epics.sh << 'EOF'
#!/bin/bash
# Add EPICS extensions bin to PATH for ecs package. ecs<SITE>_dm.sh runs
# "dm2-4" by name, which lives there.
export PATH="%{_prefix}/%{gemopt}/epics/extensions/bin/%{epics_arch}:$PATH"
# ecs_dm.sh dispatches with "exec ecs${GEMINI_SITE}_dm.sh", i.e. by name, so
# the directory this package installs those scripts into has to be on PATH. A
# workstation already has it; a bare container does not. Appended, so it cannot
# shadow anything a site profile put ahead of it.
export PATH="$PATH:%{_prefix}/bin"
EOF

chmod 755 $RPM_BUILD_ROOT/etc/profile.d/ecs-epics.sh

chmod -R u+w $RPM_BUILD_ROOT/%{_prefix}/bin
chmod -R u+w $RPM_BUILD_ROOT/%{_prefix}/share

%clean
rm -rf $RPM_BUILD_ROOT

%files ws
%defattr(-,root,root)
/%{_prefix}/bin/*
/%{_prefix}/share/dl/*
/%{_prefix}/share/alh/*
/etc/profile.d/ecs-epics.sh

%changelog
## Write changes here, e.g.
# * Thu Dec 6 2007 John Doe <jdoe@gemini.edu> VERSION-RELEASE
# - change made
# - other change made
 * Thu Jan 23 2008 Javier Lührs
 - Initial release
 * Fri Apr 25 2008 Javier Lührs
 - Updated rpm build files.
 - Created subpackage ecs-ws for the workstation stuff.

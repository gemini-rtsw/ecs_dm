%define _prefix /gemsoft
%define gemopt opt
%define name ecs
%define version 3.2
%define release 0
%define repository gemini
%define debug_package %{nil}
%define _build_id_links none

Summary: %{name} Package
Name: %{name}
Version: %{version}
Release: %{release}.%{dist}.%{repository}
License: GPL
Group: Gemini
BuildRoot: /var/tmp/%{name}-%{version}-root
Source0: %{name}-%{version}.tar.gz
BuildArch: %{arch}
Requires: epics_extension-opiGEM%{?_isa} epics_extension-alh%{?_isa}

%description
Package %{name} provides the DM screens for the module ecs.

%package ws
Summary: %{name}-ws Package
Group: Gemini
BuildRequires: epics_extension-opiGEM%{?_isa}
Requires: epics_extension-opiGEM%{?_isa} epics_extension-alh%{?_isa}
%description ws
Package %{name}-ws provides the DM screens for the module ecs.


%prep
%setup -n %{name}

%build
make

%install
%if %{__isa_bits} == 64
host_arch=linux-x86_64
%else
host_arch=linux-x86
%endif
## Write install instructions here, e.g
## install -D zzz/zzz  $RPM_BUILD_ROOT/%{_prefix}/zzz/zzz
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_prefix}/share/dl/ecs/data_CP
mkdir -p $RPM_BUILD_ROOT/%{_prefix}/share/dl/ecs/data_MK
mkdir -p $RPM_BUILD_ROOT/%{_prefix}/share/alh/ecs
mkdir -p $RPM_BUILD_ROOT/%{_prefix}/bin/

cp -r bin/${host_arch}/* $RPM_BUILD_ROOT/%{_prefix}/bin/
cp -r data_CP/*.dl $RPM_BUILD_ROOT/%{_prefix}/share/dl/ecs/data_CP
cp -r data_MK/*.dl $RPM_BUILD_ROOT/%{_prefix}/share/dl/ecs/data_MK
cp -r data/*.config $RPM_BUILD_ROOT/%{_prefix}/share/alh/ecs


chmod -R u+w $RPM_BUILD_ROOT/%{_prefix}/bin
chmod -R u+w $RPM_BUILD_ROOT/%{_prefix}/share

%clean
## Usually you won't do much more here than
rm -rf $RPM_BUILD_ROOT

%files ws
%defattr(-,root,root)
## list files that are installed here, e.g
## %{_prefix}/zzz/zzz
/%{_prefix}/bin/*
/%{_prefix}/share/dl/*
/%{_prefix}/share/alh/*


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

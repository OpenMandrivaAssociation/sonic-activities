%define stable %([ "$(echo %{version} |cut -d. -f2)" -ge 80 -o "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)

%define libname %mklibname SonicDEActivities
%define devname %mklibname SonicDEActivities -d
#define git 20240222
%define gitbranch Plasma/6.6
%define gitbranchd %(echo %{gitbranch} | sed -e 's,/,-,g')

Name: sonic-activities
Version: 6.6.4
Release: %{?git:0.%{git}.}1
URL:     https://github.com/Sonic-DE/sonic-activities
# %if 0%{?git:1}
# Source0: https://invent.kde.org/plasma/plasma-activities/-/archive/%{gitbranch}/plasma-activities-%{gitbranchd}.tar.bz2#/plasma-activities-%{git}.tar.bz2
# %else
Source0: %url/archive/%version/%name-%version.tar.gz
# %endif
Summary: Core components for the SonicDE's Activities System
License: CC0-1.0 LGPL-2.0+ LGPL-2.1 LGPL-3.0
Group: System/Libraries
BuildRequires: python
BuildRequires: cmake(ECM)
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6QmlTools)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6GuiTools)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: doxygen
BuildRequires: cmake(Qt6ToolsTools)
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: cmake(Qt6Quick)
BuildRequires: cmake(Qt6Sql)
BuildRequires: cmake(KF6Config)

# pending rename
# BuildRequires: cmake(KF6CoreAddons)
BuildRequires: %{_lib}SonicFrameworksCoreAddons-devel

BuildRequires: %{_lib}SonicFrameworksWindowSystem-devel
BuildRequires: boost-devel
BuildSystem: cmake
BuildOption: -DBUILD_QCH:BOOL=ON
BuildOption: -DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON
Requires: %{libname} = %{EVRD}

Conflicts:     plasma-activites

%description
%summary

%package -n %{libname}
Summary: Core components for the SonicDE's Activities System
Group: System/Libraries
Requires: %{name} = %{EVRD}
Conflicts:    %{_lib}PlasmaActivities

%description -n %{libname}
%summary

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}
Conflicts:    %{_lib}PlasmaActivities-devel

%description -n %{devname}
%summary

%package doc
Summary: API documentation for %{name} in Qt Assistant format
Group: Development/C++

%description doc
%summary

%files
%{_bindir}/plasma-activities-cli6
%{_datadir}/qlogging-categories6/plasma-activities.categories
%{_datadir}/qlogging-categories6/plasma-activities.renamecategories

%files -n %{devname}
%{_includedir}/PlasmaActivities
%{_libdir}/cmake/PlasmaActivities
%{_libdir}/pkgconfig/PlasmaActivities.pc

%files doc
%doc %{_qtdir}/doc/PlasmaActivities.*

%files -n %{libname}
%{_libdir}/libPlasmaActivities.so*
%{_qtdir}/qml/org/kde/activities

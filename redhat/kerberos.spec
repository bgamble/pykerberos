%define modname kerberos
%define version 1.1.2+DSE1
%define unmangled_version 1.1.2+DSE1
%define release 1
%{!?python: %define python python26}

Summary: Kerberos high-level interface
Name: %{python}-%{modname}
Version: %{version}
Release: %{release}
Source0: %{modname}-%{unmangled_version}.tar.gz
License: ASL 2.0
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: UNKNOWN <UNKNOWN>

%description

This Python package is a high-level wrapper for Kerberos (GSSAPI)
operations.  The goal is to avoid having to build a module that wraps the
entire Kerberos.framework, and instead offer a limited set of functions
that do what is needed for client/server Kerberos authentication based
on <http://www.ietf.org/rfc/rfc4559.txt>.

%prep
%setup -n %{modname}-%{unmangled_version}

%build
env CFLAGS="$RPM_OPT_FLAGS" %{python} setup.py build

%install
%{python} setup.py install -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
%doc README.txt LICENSE

Summary:	Python utilities for PowerPC platforms from IBM
Summary(pl.UTF-8):	Narzędzia w Pythonie dla platform PowerPC firmy IBM
Name:		powerpc-utils-python
Version:	1.2.1
Release:	1
License:	CPL v1.0
Group:		Applications/System
Source0:	http://downloads.sourceforge.net/powerpc-utils/%{name}-%{version}.tar.gz
# Source0-md5:	6b112ab981f2c4af3b452a9fec72d81b
URL:		http://powerpc-utils.sourceforge.net/
BuildRequires:	python-devel
BuildRequires:	sed >= 4.0
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python-pygtk-gtk >= 2:2.0
# uses ppc-specific /proc and /sys entries
ExclusiveArch:	ppc ppc64
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python based utilities for maintaining and servicing PowerPC systems
on IBM hardware.

%description -l pl.UTF-8
Narzędzia w Pythonie do administrowania i serwisowania systemów
PowerPC na sprzęcie firmy IBM.

%prep
%setup -q

sed -i -e '1s,/usr/bin/env python,/usr/bin/python,' scripts/amsvis/amsvis

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean

%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/packages

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYRIGHT README
%attr(755,root,root) %{_bindir}/amsvis
%dir %{py_sitescriptdir}/powerpcAMS
%{py_sitescriptdir}/powerpcAMS/*.py[co]
%{py_sitescriptdir}/powerpcAMS-%{version}-py*.egg-info
%{_mandir}/man1/amsvis.1*

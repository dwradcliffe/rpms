# $Id$
# Authority: matthias

Summary: Mouse and keyboard sharing utility
Name: synergy
Version: 1.0.14
Release: 2
License: GPL
Group: System Environment/Daemons
URL: http://synergy2.sourceforge.net/
Source: http://dl.sf.net/synergy2/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gcc-c++, XFree86-devel

%description
Synergy lets you easily share a single mouse and keyboard between
multiple computers with different operating systems, each with its
own display, without special hardware.  It's intended for users
with multiple computers on their desk since each system uses its
own display.


%prep
%setup


%build
%configure
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%makeinstall


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc AUTHORS BUGS COPYING ChangeLog FAQ HISTORY NEWS README TODO
%doc examples/synergy.conf
%{_bindir}/*


%changelog
* Wed May 19 2004 Matthias Saou <http://freshrpms.net/> 1.0.14-2
- Rebuilt for Fedora Core 2.

* Wed Jan 21 2004 Matthias Saou <http://freshrpms.net/> 1.0.14-1
- Initial RPM package.


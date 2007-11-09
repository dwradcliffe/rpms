# $Id$
# Authority: dries
# Upstream: Daisuke Maki <dmaki@cpan.org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name DateTime-Util-Astro
%define real_version 0.11001

Summary: Astronomical Calendar Calculations
Name: perl-DateTime-Util-Astro
Version: 0.11.1
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/DateTime-Util-Astro/

Source: http://www.cpan.org/modules/by-module/DateTime/DateTime-Util-Astro-%{real_version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(DateTime)
BuildRequires: perl(DateTime::Util::Calc) >= 0.13
BuildRequires: perl(Module::Build)

%description
This module contains functions for astronomical calendar calculations.

%prep
%setup -n %{real_name}-%{real_version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES LICENSE MANIFEST META.yml
%doc %{_mandir}/man3/DateTime::Util::Astro.3pm*
%dir %{perl_vendorlib}/DateTime/
%dir %{perl_vendorlib}/DateTime/Util/
%{perl_vendorlib}/DateTime/Util/Astro/
#%{perl_vendorlib}/DateTime/Util/Astro.pm

%changelog
* Fri Nov 09 2007 Dag Wieers <dag@wieers.com> - 0.11.1-1
- Updated to release 0.11001.

* Fri Mar  4 2005 Dries Verachtert <dries@ulyssis.org> - 0.06-1
- Updated to release 0.06.

* Sun Dec 05 2004 Dries Verachtert <dries@ulyssis.org> - 0.02-1
- Initial package.

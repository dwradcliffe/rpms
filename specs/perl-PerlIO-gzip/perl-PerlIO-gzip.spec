# $Id$

# Authority: dries
# Upstream: Nicholas Clark <nick$talking,bollo,cx>


%define real_name PerlIO-gzip
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: PerlIO layer to gzip and gunzip
Name: perl-PerlIO-gzip
Version: 0.18
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/PerlIO-gzip/

Source: http://www.cpan.org/modules/by-module/PerlIO/PerlIO-gzip-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl, zlib-devel

%description
This module contains a layer for the PerlIO system to
transparently gzip/gunzip files.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod
%{__rm} -f %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorarch}/PerlIO/gzip.pm
%{perl_vendorarch}/auto/PerlIO

%changelog
* Tue Nov 14 2006 Dries Verachtert <dries@ulyssis.org> - 0.18-1
- Updated to release 0.18.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.17-1.2
- Rebuild for Fedora Core 5.

* Wed Oct 22 2004 Dries Verachtert <dries@ulyssis.org> - 0.17-1
- Update to release 0.17.

* Wed Jun 16 2004 Dries Verachtert <dries@ulyssis.org> - 0.15-1
- Initial package.

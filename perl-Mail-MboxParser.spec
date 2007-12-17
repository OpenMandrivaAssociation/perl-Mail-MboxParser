%define	module	Mail-MboxParser
%define	name	perl-%{module}
%define	version	0.55
%define	release	%mkrel 2

%define _requires_exceptions perl(Mail::MboxParser::Mail)
%define _provides_exceptions perl(Mail::MboxParser::Mail)\\|perl(Mail::MboxParser::Base)\\|perl(Mail::MboxParser::Mail::Body)\\|perl(Mail::MboxParser::Mail::Convertable)

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Read-only access to UNIX-mailboxes 
License:	GPL or Artistic
Group:		Development/Perl
Url:            http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/Mail/%{module}-%{version}.tar.bz2
%if %{mdkversion} < 1010
Buildrequires:	perl-devel
%endif
BuildRequires:	perl-MIME-tools
BuildArch:	noarch


%description
This module attempts to provide a simplified access to standard UNIX-mailboxes.
It offers only a subset of methods to get 'straight to the point'. More
sophisticated things can still be done by invoking any method from MIME::Tools
on the appropriate return values.

Mail::MboxParser has not been derived from Mail::Box and thus isn't acquainted
with it in any way. It, however, incorporates some invaluable hints by the
author of Mail::Box, Mark Overmeer.

%prep
%setup -q -n %{module}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot} 
%makeinstall_std

%clean 
rm -rf %{buildroot} 

%files
%defattr(-,root,root)
%doc Changelog README
%{perl_vendorlib}/Mail
%{_mandir}/man3*/*



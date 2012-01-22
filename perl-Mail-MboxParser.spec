%define	upstream_name	 Mail-MboxParser
%define	upstream_version 0.55

%define _requires_exceptions perl(Mail::MboxParser::Mail)
%define _provides_exceptions perl(Mail::MboxParser::Mail)\\|perl(Mail::MboxParser::Base)\\|perl(Mail::MboxParser::Mail::Body)\\|perl(Mail::MboxParser::Mail::Convertable)

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 4

Summary:	Read-only access to UNIX-mailboxes 
License:	GPL+ or Artistic
Group:		Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Mail/%{upstream_name}-%{upstream_version}.tar.bz2
Patch0: Mail-MboxParser-0.55-debian_bug_395268.diff
%if %{mdkversion} < 1010
Buildrequires:	perl-devel
%endif
BuildRequires:	perl-MIME-tools
BuildArch:	noarch
Requires: perl-Mail-Mbox-MessageParser
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This module attempts to provide a simplified access to standard UNIX-mailboxes.
It offers only a subset of methods to get 'straight to the point'. More
sophisticated things can still be done by invoking any method from MIME::Tools
on the appropriate return values.

Mail::MboxParser has not been derived from Mail::Box and thus isn't acquainted
with it in any way. It, however, incorporates some invaluable hints by the
author of Mail::Box, Mark Overmeer.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
%patch0 -p0

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

#%%check
#%{__make} test <- https://rt.cpan.org/Public/Bug/Display.html?id=66576

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

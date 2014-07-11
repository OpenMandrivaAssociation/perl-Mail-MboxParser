%define	upstream_name	 Mail-MboxParser
%define	upstream_version 0.55

# Not sure we need it but it was there for a long time already
%if %{_use_internal_dependency_generator}
%define __noautoreq 'perl\\(Mail::MboxParser::Mail\\)|perl\\(Mail::MboxParser::Base\\)|perl\\(Mail::MboxParser::Mail::Body\\)|perl\\(Mail::MboxParser::Mail::Convertable\\)'
%define __noautoprov 'perl\\(Mail::MboxParser::Mail\\)|perl\\(Mail::MboxParser::Base\\)|perl\\(Mail::MboxParser::Mail::Body\\)|perl\\(Mail::MboxParser::Mail::Convertable\\)'
%else
%define _requires_exceptions perl(Mail::MboxParser::Mail)
%define _provides_exceptions perl(Mail::MboxParser::Mail)\\|perl(Mail::MboxParser::Base)\\|perl(Mail::MboxParser::Mail::Body)\\|perl(Mail::MboxParser::Mail::Convertable)
%endif

Summary:	Read-only access to UNIX-mailboxes 
Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	13
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Mail/%{upstream_name}-%{upstream_version}.tar.bz2
Patch0:	Mail-MboxParser-0.55-debian_bug_395268.diff
BuildArch:	noarch
BuildRequires:	perl-devel
BuildRequires:	perl-MIME-tools
Requires:	perl-Mail-Mbox-MessageParser

%description
This module attempts to provide a simplified access to standard UNIX-mailboxes.
It offers only a subset of methods to get 'straight to the point'. More
sophisticated things can still be done by invoking any method from MIME::Tools
on the appropriate return values.

Mail::MboxParser has not been derived from Mail::Box and thus isn't acquainted
with it in any way. It, however, incorporates some invaluable hints by the
author of Mail::Box, Mark Overmeer.

%prep
%setup -qn %{upstream_name}-%{upstream_version}
%patch0 -p0

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
#%{__make} test <- https://rt.cpan.org/Public/Bug/Display.html?id=66576

%install
%makeinstall_std

%files
%doc Changelog README
%{perl_vendorlib}/Mail
%{_mandir}/man3*/*


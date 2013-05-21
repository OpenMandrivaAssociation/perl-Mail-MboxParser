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

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	7

Summary:	Read-only access to UNIX-mailboxes 
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Mail/%{upstream_name}-%{upstream_version}.tar.bz2
Patch0:		Mail-MboxParser-0.55-debian_bug_395268.diff

BuildRequires:	perl-devel
BuildRequires:	perl-MIME-tools
BuildArch:	noarch
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
%setup -q -n %{upstream_name}-%{upstream_version}
%patch0 -p0

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

#%%check
#%{__make} test <- https://rt.cpan.org/Public/Bug/Display.html?id=66576

%install
%makeinstall_std

%files
%doc Changelog README
%{perl_vendorlib}/Mail
%{_mandir}/man3*/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.550.0-4mdv2012.0
+ Revision: 765422
- rebuilt for perl-5.14.2
- rebuilt for perl-5.14.x

* Sat May 21 2011 Oden Eriksson <oeriksson@mandriva.com> 0.550.0-2
+ Revision: 676492
- also add the patch...
- disable tests for now
- added a patch from debian to make it work with recent Mail::Mbox::MessageParser
- fix deps
- mass rebuild

* Sat Aug 01 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.550.0-1mdv2011.0
+ Revision: 405861
- rebuild using %%perl_convert_version

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 0.55-4mdv2009.0
+ Revision: 223809
- rebuild

* Thu Mar 06 2008 Oden Eriksson <oeriksson@mandriva.com> 0.55-3mdv2008.1
+ Revision: 180440
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Fri Jan 12 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.55-2mdv2007.0
+ Revision: 107907
- rebuild
- Import perl-Mail-MboxParser

* Wed Dec 14 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.55-1mdk
- new version
- spec cleanup
- %%mkrel
- better summary and description
- fix directory ownership

* Thu Jul 21 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.54-1mdk
- 0.54

* Tue May 03 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.53-1mdk
- 0.53

* Fri Feb 11 2005 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.52-1mdk
- 0.52

* Tue Jan 25 2005 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.51-1mdk
- 0.51
- remove requires_exceptions and provides_exceptions for internal modules

* Wed Aug 25 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.49-1mdk
- 0.49

* Wed Jul 14 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.48-1mdk
- 0.48

* Fri Jun 04 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.47-1mdk
- 0.47
- drop PREFIX and use %%makeinstall_std macro
- cosmetics


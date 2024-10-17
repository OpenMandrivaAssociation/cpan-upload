Name:       cpan-upload
Version:    2.2
Release:    7
Summary:    Upload one or more files to CPAN, using PAUSE
License:    GPL or Artistic
Group:      Development/Perl
URL:        https://search.cpan.org/CPAN/authors/id/N/NE/NEILB/scripts
Source:     http://search.cpan.org/CPAN/authors/id/N/NE/NEILB/scripts/%{name}-%{version}.tar.gz
BuildRequires:  perl-devel
BuildRequires: perl(AppConfig::Std) >= 1.05
BuildRequires: perl(Pod::Usage) >= 1.14
BuildRequires: perl(Net::FTP) >= 2.28
BuildRequires: perl(HTTP::Request::Common)
BuildRequires: perl(File::Basename) >= 2.28
BuildRequires: perl(Term::ReadKey)
BuildArch:      noarch

%description
cpan-upload is a script which automates the process of uploading a file to
CPAN using PAUSE, the Perl Authors Upload Server.

%prep
%setup -q

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
%makeinstall_std

%files
%defattr(-,root,root)
%doc README ChangeLog
%{_mandir}/*/*
%{_bindir}/%name




%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 2.2-5mdv2011.0
+ Revision: 617434
- the mass rebuild of 2010.0 packages

* Wed Sep 02 2009 Thierry Vignaud <tv@mandriva.org> 2.2-4mdv2010.0
+ Revision: 425081
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 2.2-3mdv2009.0
+ Revision: 243696
- rebuild

* Thu Feb 14 2008 Thierry Vignaud <tv@mandriva.org> 2.2-1mdv2008.1
+ Revision: 168407
- fix summary-not-capitalized
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Jul 25 2007 Olivier Thauvin <nanardon@mandriva.org> 2.2-1mdv2008.0
+ Revision: 55259
- initial mdv pkg
- Create cpan-upload


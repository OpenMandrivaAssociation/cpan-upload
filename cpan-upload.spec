%define name        cpan-upload
%define version     2.2
%define release     %mkrel 5

Name:       %{name}
Version:    %{version}
Release:    %{release}
Summary:    Upload one or more files to CPAN, using PAUSE
License:    GPL or Artistic
Group:      Development/Perl
URL:        http://search.cpan.org/CPAN/authors/id/N/NE/NEILB/scripts
Source:     http://search.cpan.org/CPAN/authors/id/N/NE/NEILB/scripts/%{name}-%{version}.tar.gz
%if %{mdkversion} < 1010
BuildRequires:  perl-devel
%endif
BuildRequires: perl(AppConfig::Std) >= 1.05
BuildRequires: perl(Pod::Usage) >= 1.14
BuildRequires: perl(Net::FTP) >= 2.28
BuildRequires: perl(HTTP::Request::Common)
BuildRequires: perl(File::Basename) >= 2.28
BuildRequires: perl(Term::ReadKey)
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}

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
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README ChangeLog
%{_mandir}/*/*
%{_bindir}/%name



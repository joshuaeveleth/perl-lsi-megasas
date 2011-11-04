Name:           perl-LSI-MegaSAS
Version:        1.00
Release:        1%{?dist}
Summary:        Monitor LSI MegaRAID controllers
License:        Public Domain
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/LSI-MegaSAS/
Source0:        http://www.cpan.org/modules/by-module/LSI/LSI-MegaSAS-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
LSI has published a Linux tool called "MegaCli". This tool reports the
status of MegaRAID arrays. This package is a Perl wrapper around that
tool.

%prep
%setup -q -n LSI-MegaSAS-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes README
%{_bindir}/megasas-list
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Thu Nov 03 2011 kdreyer@usgs.gov 1.00-1
- Specfile autogenerated by cpanspec 1.78.

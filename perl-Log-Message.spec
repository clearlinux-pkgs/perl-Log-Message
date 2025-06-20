#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v21
# autospec commit: 94c6be0
#
Name     : perl-Log-Message
Version  : 0.08
Release  : 31
URL      : https://cpan.metacpan.org/authors/id/B/BI/BINGOS/Log-Message-0.08.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/B/BI/BINGOS/Log-Message-0.08.tar.gz
Summary  : 'Powerful and flexible message logging mechanism'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Log-Message-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
message logging module.
Please type "perldoc Log::Message" after installation to see the module
usage information.

%package dev
Summary: dev components for the perl-Log-Message package.
Group: Development
Provides: perl-Log-Message-devel = %{version}-%{release}
Requires: perl-Log-Message = %{version}-%{release}

%description dev
dev components for the perl-Log-Message package.


%package perl
Summary: perl components for the perl-Log-Message package.
Group: Default
Requires: perl-Log-Message = %{version}-%{release}

%description perl
perl components for the perl-Log-Message package.


%prep
%setup -q -n Log-Message-0.08
cd %{_builddir}/Log-Message-0.08

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Log::Message.3
/usr/share/man/man3/Log::Message::Config.3
/usr/share/man/man3/Log::Message::Handlers.3
/usr/share/man/man3/Log::Message::Item.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*

#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Log-Message
Version  : 0.08
Release  : 8
URL      : https://cpan.metacpan.org/authors/id/B/BI/BINGOS/Log-Message-0.08.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/B/BI/BINGOS/Log-Message-0.08.tar.gz
Summary  : 'Powerful and flexible message logging mechanism'
Group    : Development/Tools
License  : Artistic-1.0-Perl
BuildRequires : buildreq-cpan

%description
message logging module.
Please type "perldoc Log::Message" after installation to see the module
usage information.

%package dev
Summary: dev components for the perl-Log-Message package.
Group: Development
Provides: perl-Log-Message-devel = %{version}-%{release}

%description dev
dev components for the perl-Log-Message package.


%prep
%setup -q -n Log-Message-0.08

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
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
/usr/lib/perl5/vendor_perl/5.28.1/Log/Message.pm
/usr/lib/perl5/vendor_perl/5.28.1/Log/Message/Config.pm
/usr/lib/perl5/vendor_perl/5.28.1/Log/Message/Handlers.pm
/usr/lib/perl5/vendor_perl/5.28.1/Log/Message/Item.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Log::Message.3
/usr/share/man/man3/Log::Message::Config.3
/usr/share/man/man3/Log::Message::Handlers.3
/usr/share/man/man3/Log::Message::Item.3

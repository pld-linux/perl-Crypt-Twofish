#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define		pdir	Crypt
%define		pnam	Twofish
Summary:	Crypt::Twofish Perl module - the Twofish encryption algorithm
Summary(pl):	Modu³ Perla Crypt::Twofish - algorytm szyfrowania Twofish
Name:		perl-Crypt-Twofish
Version:	2.12
Release:	1
License:	Artistic
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module implements Twofish encryption. It supports the Crypt::CBC
interface. Twofish is a 128-bit symmetric block cipher with a variable
length (128, 192, or 256-bit) key, developed by Counterpane Labs. It
is unpatented and free for all uses, as described at
<http://www.counterpane.com/twofish.html>.

%description -l pl
Ten modu³ jest implementacj± szyfrowania Twofish. Obs³uguje interfejs
Crypt::CBC. Twofish jest 128-bitowym symetrycznym szyfrem blokowym ze
zmienn± d³ugo¶ci± klucza (128, 192 lub 256 bitów), opracowanym przez
Counterpane Labs. Nie jest opatentowany i mo¿na go swobodnie u¿ywaæ
do dowolnych celów, zgodnie z opisem pod adresem
<http://www.counterpane.com/twofish.html>.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"
%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_sitearch}/Crypt/Twofish.pm
%dir %{perl_sitearch}/auto/Crypt/Twofish
%{perl_sitearch}/auto/Crypt/Twofish/*.bs
%attr(755,root,root) %{perl_sitearch}/auto/Crypt/Twofish/*.so
%{_mandir}/man3/*

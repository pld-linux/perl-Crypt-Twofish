#
# Conditional build:
%bcond_without	tests	# Do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Crypt
%define		pnam	Twofish
Summary:	Crypt::Twofish Perl module - the Twofish encryption algorithm
Summary(pl):	Modu³ Perla Crypt::Twofish - algorytm szyfrowania Twofish
Name:		perl-Crypt-Twofish
Version:	2.12
Release:	3
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	39937a00e4d5e6a5d700d1cd9991517c
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
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
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/Crypt/Twofish.pm
%dir %{perl_vendorarch}/auto/Crypt/Twofish
%{perl_vendorarch}/auto/Crypt/Twofish/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Crypt/Twofish/*.so
%{_mandir}/man3/*

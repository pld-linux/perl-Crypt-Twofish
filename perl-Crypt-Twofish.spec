#
# Conditional build:
%bcond_without	tests	# Do not perform "make test"
#
%define		pdir	Crypt
%define		pnam	Twofish
Summary:	Crypt::Twofish Perl module - the Twofish encryption algorithm
Summary(pl.UTF-8):	Moduł Perla Crypt::Twofish - algorytm szyfrowania Twofish
Name:		perl-Crypt-Twofish
Version:	2.17
Release:	7
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Crypt/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	bb6e7ec9ff6db6aea27dce7175a852e2
Patch0:		no-dot-in-inc.patch
URL:		http://search.cpan.org/dist/Crypt-Twofish/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module implements Twofish encryption. It supports the Crypt::CBC
interface. Twofish is a 128-bit symmetric block cipher with a variable
length (128, 192, or 256-bit) key, developed by Counterpane Labs. It
is unpatented and free for all uses, as described at
<http://www.counterpane.com/twofish.html>.

%description -l pl.UTF-8
Ten moduł jest implementacją szyfrowania Twofish. Obsługuje interfejs
Crypt::CBC. Twofish jest 128-bitowym symetrycznym szyfrem blokowym ze
zmienną długością klucza (128, 192 lub 256 bitów), opracowanym przez
Counterpane Labs. Nie jest opatentowany i można go swobodnie używać
do dowolnych celów, zgodnie z opisem pod adresem
<http://www.counterpane.com/twofish.html>.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch -P0 -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
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
%attr(755,root,root) %{perl_vendorarch}/auto/Crypt/Twofish/*.so
%{_mandir}/man3/*

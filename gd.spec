Summary:	Library for PNG creation
Summary(pl):	Biblioteka do tworzenia PNGów
Name:		gd
Version:	1.6.3
Release:	2
License:	BSD-style
Group:		Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
Source0:	ftp://ftp.boutell.com/pub/boutell/gd/%{name}-%{version}.tar.gz
URL:		http://www.boutell.com/gd/
BuildRequires:	zlib-devel
BuildRequires:	libpng-devel
BuildRequires:	freetype-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This library allows you to easily create and manipulate PNG image
files from your C programs.

%description -l pl
Biblioteka pozwalaj±ca na proste tworzenie i manipulowanie plikami
graficznymi w formacie PNG.

%package devel
Summary:	Development part of the GD library
Summary(pl):	Czê¶æ biblioteki GD przeznaczona dla developerów.
Group:		Development/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
This package contains the files needed for development of programs
linked against GD.

%description -l pl devel
Pakiet ten zawiera pliki potrzebne do rozwoju programów korzystaj±cych
z biblioteki GD.

%package static
Summary:	Static GD library
Summary(pl):	Statyczna biblioteka GD.
Group:		Development/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
This package contains static GD library.

%description -l pl static
Pakiet ten zawiera statyczn± bibliotekê GD.

%prep
%setup -q 

%build
CFLAGS="$RPM_OPT_FLAGS -I/usr/include/freetype"
LDFLAGS="-s"
export CFLAGS LDFLAGS
%configure
make

%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR="$RPM_BUILD_ROOT" install

strip --strip-unneeded $RPM_BUILD_ROOT%{_libdir}/lib*.so.*.*

gzip -9nf NEWS README index.html 

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc {NEWS,README}.gz
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc index.html.gz 
%attr(755,root,root) %{_libdir}/*.so
%attr(755,root,root) %{_libdir}/libgd.la
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

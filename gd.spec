Summary:	Library for PNG, JPEG creation
Summary(pl):	Biblioteka do tworzenia grafiki w formacie PNG, JPEG
Name:		gd
Version:	1.8.3
Release:	7
License:	BSD-style
Group:		Libraries
Group(de):	Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
Source0:	ftp://ftp.boutell.com/pub/boutell/gd/%{name}-%{version}.tar.gz
Patch0:		%{name}-ac_am.patch
URL:		http://www.boutell.com/gd/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	zlib-devel
BuildRequires:	libpng-devel
BuildRequires:	freetype-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define shlibver %(echo %{version} | cut -f-2 -d.)

%description
gd library creates PNG, JPEG and WBMP images, not GIF images. This is
a good thing. PNG is a more compact format, and full compression is
available. JPEG works well with photographic images, and is still more
compatible with the major Web browsers than even PNG is. WBMP is
intended for wireless devices (not regular web browsers). Existing
code will need modification to call or gdImageJpeg instead of
gdImageGif.

This library allows you to easily create and manipulate PNG, JPEG
image files from your C programs.

%description -l pl
Biblioteka pozwalająca na proste tworzenie i manipulowanie plikami
graficznymi w formacie PNG.

%package devel
Summary:	Development part of the GD library
Summary(pl):	Część biblioteki GD przeznaczona dla developerów
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	libpng-devel
Requires:	zlib-devel
Requires:	%{name} = %{version}

%description devel
This package contains the files needed for development of programs
linked against GD.

%description -l pl devel
Pakiet ten zawiera pliki potrzebne do rozwoju programów korzystających
z biblioteki GD.

%package static
Summary:	Static GD library
Summary(pl):	Statyczna biblioteka GD
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
This package contains static GD library.

%description -l pl static
Pakiet ten zawiera statyczną bibliotekę GD.

%prep
%setup -q 
%patch0 -p1 

%build
libtoolize --copy --force
automake -a -c
aclocal
autoconf
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
        DESTDIR=$RPM_BUILD_ROOT

gzip -9nf readme.txt index.html 

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc readme.txt.gz
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc index.html.gz 
%attr(755,root,root) %{_libdir}/*.so
%attr(755,root,root) %{_libdir}/*.la
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

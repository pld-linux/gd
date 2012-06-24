Summary:	Library for GIF creation
Summary(pl):	Biblioteka do tworzenia GIF�w
Name:		gd
Version:	1.3
Release:	8
Copyright:	BSD-style
Group:		Libraries
Group(pl):	Biblioteki
Source0:	ftp://ftp.boutell.com/pub/boutell/gd/%{name}%{version}.tar.gz
Source1:	gd-ref.html
Patch0:		gd-shared.patch
Patch1:		gd-non-root.patch
Patch2:		gd-nodemo.patch
URL:		http://www.boutell.com/gd/
BuildRoot:	/tmp/%{name}-%{version}-root

%description
This library allows you to easily create and manipulate GIF image files
from your C programs.

%description -l pl
Biblioteka pozwalaj�ca na proste tworzenie i manipulowanie plikami graficznymi
w formacie GIF.

%package devel
Summary:	Development part of the GD library
Summary(pl):	Cz�� biblioteki GD przeznaczona dla developer�w.
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
This package contains the files needed for development of programs linked
against GD.

%description -l pl devel
Pakiet ten zawiera pliki potrzebne do rozwoju program�w
korzystaj�cych z biblioteki GD.

%prep
%setup -q -n %{name}%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
CFLAGS="$RPM_OPT_FLAGS" make

install %{SOURCE1} .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_includedir},%{_libdir}}

install {gd,gdfontg,gdfontl,gdfontmb,gdfonts,gdfontt}.h $RPM_BUILD_ROOT%{_includedir}
install -s libgd.so.*.* $RPM_BUILD_ROOT%{_libdir}
mv libgd.so $RPM_BUILD_ROOT%{_libdir}

gzip -9nf readme.txt

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%attr(755,root,root) %{_libdir}/*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc readme.txt.gz index.html gd-ref.html
%attr(755,root,root) %{_libdir}/*.so
%{_includedir}/*

%changelog
* Wed May 26 1999 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.3-8]
- based on RH spec,
- spec rewrited by PLD team,
- pl translation by Arkadiusz Mi�kiewicz <misiek@misiek.eu.org>.

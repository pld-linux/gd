Summary:	Library for GIF creation
Summary(pl):	Biblioteka do tworzenia GIFów
Name:		gd
Version:	1.3
Release:	7
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
Biblioteka pozwalaj±ca na proste tworzenie i manipulowanie plikami graficznymi
w formacie GIF.

%package devel
Summary:	Development part of the GD library
Summary(pl):	Czê¶æ biblioteki GD przeznaczona dla developerów.
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
This package contains the files needed for development of programs linked
against GD.

%description -l pl devel
Pakiet ten zawiera pliki potrzebne do rozwoju programów
korzystaj±cych z biblioteki GD.

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
install -d $RPM_BUILD_ROOT/usr/{include,lib}

install {gd,gdfontg,gdfontl,gdfontmb,gdfonts,gdfontt}.h $RPM_BUILD_ROOT/usr/include
install -s libgd.so.*.* $RPM_BUILD_ROOT/usr/lib
mv libgd.so $RPM_BUILD_ROOT/usr/lib

gzip -9nf readme.txt

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%attr(755,root,root) /usr/lib/*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc readme.txt.gz index.html gd-ref.html
%attr(755,root,root) /usr/lib/*.so
/usr/include/*

%changelog
* Sun Apr 25 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.3-7]
- recompiled on new rpm.

* Thu Apr 15 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.3-6]
- added gd-ref.html do delel,
- gzipping some %doc.

* Mon Jan 11 1999 Arkadiusz Mi¶kiewicz <misiek@misiek.eu.org>
- added polish translation

* Mon Dec 21 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.3-5]
- removed compiling demo programs.

* Thu Sep 24  1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.3-4]
- added -q %setup parameter,
- changed Buildroot to /tmp/%%{name}-%%{version}-root,
- added using %%{name} and %%{version} in Source and %setup,
- added %postun,
- changed dependencies to "Requires: %%{name} = %%{version}" in devel
  subpackage,
- added stripping shared libraries,
- added %attr and %defattr macros in %files (allows build package from
  non-root account).

* Fri Sep 11 1998 Cristian Gafton <gafton@redhat.com>
- built for 5.2

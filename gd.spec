Summary:     Library for GIF creation
Name:        gd
Version:     1.3
Release:     3
Source:      ftp://ftp.boutell.com/pub/boutell/gd/%{name}%{version}.tar.gz
URL:         http://www.boutell.com/gd/
Patch0:      gd-shared.patch
Patch1:      gd-non-root.patch
Copyright:   BSD-style
Group:       Libraries
BuildRoot:   /tmp/%{name}-%{version}-root

%description
This library allows you to easily create and manipulate GIF image files
from your C programs.

%package devel
Summary:     Development part of the GD library
Group:       Development/Libraries
Requires:    %{name} = %{version}

%description devel
This package contains the files needed for development of programs linked
against GD.

%prep
%setup -q -n %{name}%{version}
%patch0 -p1
%patch1 -p1

%build
CFLAGS="$RPM_OPT_FLAGS" make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/{include,lib}

install {gd,gdfontg,gdfontl,gdfontmb,gdfonts,gdfontt}.h $RPM_BUILD_ROOT/usr/include
install -s libgd.so* $RPM_BUILD_ROOT/usr/lib

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%attr(755, root, root) /usr/lib/*.so.*

%files devel
%defattr(644, root, root, 755)
%doc readme.txt index.html
%attr(755, root, root) /usr/lib/*.so
/usr/include/*

%changelog
* Thu Sep 24  1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.3-4]
- added -q %setup parameter,
- changed Buildroot to /tmp/%%{name}-%%{version}-root,
- added using %%{name} and %%{version} in Source and %setup,
- added %postun,
- changed dependencies to "Requires: %%{name} = %%{version}" in devel
  subpackage,
- added striping shared libraries,
- added %attr and %defattr macros in %files (allow build package from
  non-root account).

* Fri Sep 11 1998 Cristian Gafton <gafton@redhat.com>
- built for 5.2

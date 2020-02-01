#
# Conditional build:
%bcond_without	fontconfig	# fontconfig support
%bcond_with	libimagequant	# LIQ quantization method support (breaks transparency in TrueColor->palette conversion)
%bcond_with	sse		# SSE math on ix86
%bcond_without	xpm		# XPM support (requires X11 libs)
%bcond_without	tests		# "make check"
#
%ifarch pentium3 pentium4
%define	with_sse	1
%endif
Summary:	Library for PNG, JPEG creation
Summary(es.UTF-8):	Biblioteca para manipulación de imágenes
Summary(pl.UTF-8):	Biblioteka do tworzenia grafiki w formacie PNG, JPEG
Summary(pt_BR.UTF-8):	Biblioteca para manipulação de imagens
Name:		gd
Version:	2.2.5
Release:	5
License:	BSD-like
Group:		Libraries
#Source0Download: https://github.com/libgd/libgd/releases
Source0:	https://github.com/libgd/libgd/releases/download/%{name}-%{version}/lib%{name}-%{version}.tar.xz
# Source0-md5:	8d8d6a6189513ecee6e893b1fb109bf8
Patch0:		%{name}-fontpath.patch
Patch2:		%{name}-loop.patch
Patch3:		%{name}-liq.patch
Patch4:		0004-Fix-OOB-read-due-to-crafted-GD-GD2-images.patch
Patch5:		0005-Fix-tiff_invalid_read-check.patch
Patch6:		bmp-check-return-value-in-gdImageBmpPtr.patch
Patch7:		Fix-420-Potential-infinite-loop-in-gdImageCreateFrom.patch
Patch8:		gd-2.2.5-heap-based-buffer-overflow.patch
Patch9:		gd-2.2.5-null-pointer.patch
Patch10:	gd-2.2.5-potential-double-free.patch
Patch11:	gd-2.2.5-upstream.patch
URL:		https://libgd.github.io/
BuildRequires:	autoconf >= 2.54
BuildRequires:	automake
%{?with_fontconfig:BuildRequires:	fontconfig-devel}
BuildRequires:	freetype-devel >= 1:2.1.10
BuildRequires:	gettext-tools
%{?with_libimagequant:BuildRequires:	libimagequant-devel}
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel >= 2:1.4.0
BuildRequires:	libtiff-devel >= 4
BuildRequires:	libtool >= 2:2
BuildRequires:	libwebp-devel
BuildRequires:	pkgconfig
BuildRequires:	sed >= 4
BuildRequires:	tar >= 1:1.22
%{?with_xpm:BuildRequires:	xorg-lib-libXpm-devel}
BuildRequires:	xz
BuildRequires:	zlib-devel
Requires:	freetype >= 1:2.1.10
Provides:	gd(gif) = %{version}-%{release}
# versioned by php version rotate_from_php code comes from
Provides:	gd(imagerotate) = 5.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gd is the image manipulating library. It was created to allow graphs,
charts and the like to be generated on the fly for use on the World
wide Web, but is useful for any application in which custom images are
useful. It is not a paint program; it is a library. gd library creates
PNG, JPEG, GIF and WBMP images. PNG is a more compact format, and full
compression is available. JPEG works well with photographic images,
and is still more compatible with the major Web browsers than even PNG
is. WBMP is intended for wireless devices (not regular web browsers).

%description -l es.UTF-8
Esta es la biblioteca gd para el manejo de imágenes. Fue creada para
uso en la Web, creando gráficos automáticamente. Pero es útil para
cualquier programa que necesite de imágenes personalizados. No es un
programa de dibujo; es una biblioteca.

%description -l pl.UTF-8
gd to biblioteka do obróbki obrazów. Została stworzona, aby umożliwić
dynamiczne generowanie wykresów i podobnych rzeczy na potrzeby WWW,
ale może być przydatna także dla każdej aplikacji tworzącej własne
obrazy. Biblioteka ta pozwala na tworzenie plików graficznych w
formatach PNG, JPEG, GIF i WBMP. PNG jest zwartym formatem z
bezstratną kompresją. JPEG dobrze nadaje się do obrazów
fotograficznych i jest obsługiwany nawet przez więcej przeglądarek WWW
niż PNG. WBMP jest przeznaczony dla urządzeń bezprzewodowych (a nie
zwykłych przeglądarek WWW).

%description -l pt_BR.UTF-8
Esta é a biblioteca gd para manipulação de imagens. Ela foi criada
para uso na Web, gerando gráficos automaticamente. Mas é útil para
qualquer programa que precise de imagens personalizados. Não é um
programa de desenho; é uma biblioteca.

%package devel
Summary:	Development part of the GD library
Summary(es.UTF-8):	Archivos de inclusión y bibliotecas para desarrollar programas usando gd
Summary(pl.UTF-8):	Część biblioteki GD przeznaczona dla developerów
Summary(pt_BR.UTF-8):	Arquivos de inclusão e bibliotecas para desenvolver programas usando gd
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	fontconfig-devel
Requires:	freetype-devel >= 1:2.1.10
%{?with_libimagequant:Requires:	libimagequant-devel}
Requires:	libjpeg-devel
Requires:	libpng-devel
Requires:	libtiff-devel >= 4
Requires:	libwebp-devel
%{?with_xpm:Requires:	xorg-lib-libXpm-devel}
Requires:	zlib-devel
Provides:	gd-devel(gif) = %{version}-%{release}
Provides:	gd-devel(imagerotate) = 5.2.0

%description devel
This package contains the files needed for development of programs
linked against GD.

%description devel -l es.UTF-8
Este paquete contiene los archivos de inclusión y las bibliotecas
necesarias para desarrollar programas usando gd.

%description devel -l pl.UTF-8
Pakiet ten zawiera pliki potrzebne do rozwoju programów korzystających
z biblioteki GD.

%description devel -l pt_BR.UTF-8
Este pacote contém os arquivos de inclusão e as bibliotecas
necessárias para desenvolver programas usando gd.

%package static
Summary:	Static GD library
Summary(pl.UTF-8):	Statyczna biblioteka GD
Summary(pt_BR.UTF-8):	Bibliotecas estáticas para desenvolvimento com libgd
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Provides:	gd-static(gif) = %{version}-%{release}
Provides:	gd-static(imagerotate) = 5.2.0

%description static
This package contains static gd library.

%description static -l pl.UTF-8
Ten pakiet zawiera statyczną bibliotekę gd.

%description static -l pt_BR.UTF-8
Este pacote contem bibliotecas estáticas para desenvolvimento com
libgd.

%package progs
Summary:	Utility programs that use libgd
Summary(es.UTF-8):	Programas utilitarios libgd
Summary(pl.UTF-8):	Narzędzia używające libgd
Summary(pt_BR.UTF-8):	Programas utilitários libgd
Group:		Applications/Graphics
Requires:	%{name} = %{version}-%{release}

%description progs
These are utility programs supplied with gd, the image manipulation
library. The libgd-progs package contains a group of scripts for
manipulating the graphics files in formats which are supported by the
libgd library.

%description progs -l pl.UTF-8
Ten pakiet zawiera programy używające biblioteki gd, służące do
obróbki plików graficznych w formatach obsługiwanych przez libgd.

%description progs -l pt_BR.UTF-8
Este pacote inclui vários utilitários para manipulação de arquivos gd
para uso pelos programas que usam a libgd.

%prep
%setup -q -n libgd-%{version}
%patch0 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1

# hack to avoid inclusion of -s in --ldflags
%{__sed} -i -e 's,@LDFLAGS@,,g' config/gdlib-config.in
# disable error caused by subdir-objects warning in automake 1.14
%{__sed} -i -e '/AM_INIT_AUTOMAKE/s/-Werror//' configure.ac

%build
%{__libtoolize}
%{__aclocal}
%{__automake}
%{__autoheader}
%{__autoconf}
%ifarch %{ix86}
%if %{with sse}
CFLAGS="%{rpmcflags} -msse -mfpmath=sse"
%endif
%endif
%configure \
	%{!?with_fontconfig:--without-fontconfig} \
	%{!?with_libimagequant:--without-liq} \
	%{!?with_xpm:--without-xpm}
%{__make}

%if %{with tests}
%ifarch %{ix86}
# https://github.com/libgd/libgd/issues/359
XFAIL_TESTS="$XFAIL_TESTS gdimagegrayscale/basic"
%if %{without sse}
# 387 arithmetic is inexact, https://github.com/libgd/libgd/issues/242
XFAIL_TESTS="$XFAIL_TESTS gdimagecopyresampled/bug00201 gdimagerotate/bug00067"
%endif
%endif
export XFAIL_TESTS
%{__make} check
%endif

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CONTRIBUTORS COPYING README.md
%attr(755,root,root) %{_libdir}/libgd.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgd.so.3

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gdlib-config
%attr(755,root,root) %{_libdir}/libgd.so
%{_libdir}/libgd.la
%{_includedir}/entities.h
%{_includedir}/gd*.h
%{_pkgconfigdir}/gdlib.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgd.a

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/annotate
%attr(755,root,root) %{_bindir}/bdftogd
%attr(755,root,root) %{_bindir}/gd2copypal
%attr(755,root,root) %{_bindir}/gd2togif
%attr(755,root,root) %{_bindir}/gd2topng
%attr(755,root,root) %{_bindir}/gdcmpgif
%attr(755,root,root) %{_bindir}/gdparttopng
%attr(755,root,root) %{_bindir}/gdtopng
%attr(755,root,root) %{_bindir}/giftogd2
%attr(755,root,root) %{_bindir}/pngtogd
%attr(755,root,root) %{_bindir}/pngtogd2
%attr(755,root,root) %{_bindir}/webpng

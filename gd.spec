Summary:	Library for PNG, JPEG creation
Summary(es):	Biblioteca para manipulación de imágenes
Summary(pl):	Biblioteka do tworzenia grafiki w formacie PNG, JPEG
Summary(pt_BR):	Biblioteca para manipulação de imagens
Name:		gd
Version:	2.0.1
Release:	4
License:	BSD-like
Group:		Libraries
Source0:	http://www.boutell.com/ftp-materials/boutell/gd/%{name}-%{version}.tar.gz
Patch0:		%{name}-ac_am.patch
URL:		http://www.boutell.com/gd/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	zlib-devel
BuildRequires:	libpng-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libtiff-devel
BuildRequires:	freetype-devel >= 2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		shlibver	%(echo %{version} | cut -f-2 -d.)

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

%description -l es
Esta es la biblioteca gd para el manejo de imágenes. Fue creada para
uso en la Web, creando gráficos automáticamente. Pero es útil para
cualquier programa que necesite de imágenes personalizados. No es un
programa de dibujo; es una biblioteca.

%description -l pl
Biblioteka pozwalaj±ca na proste tworzenie i manipulowanie plikami
graficznymi w formacie PNG, JPEG i WBMP, ale nie GIF.

%description -l pt_BR
Esta é a biblioteca gd para manipulação de imagens. Ela foi criada
para uso na Web, gerando gráficos automaticamente. Mas é útil para
qualquer programa que precise de imagens personalizados. Não é um
programa de desenho; é uma biblioteca.

%package devel
Summary:	Development part of the GD library
Summary(es):	Archivos de inclusión y bibliotecas para desarrollar programas usando gd
Summary(pl):	Czê¶æ biblioteki GD przeznaczona dla developerów
Summary(pt_BR):	Arquivos de inclusão e bibliotecas para desenvolver programas usando gd
Group:		Development/Libraries
Requires:	libpng-devel
Requires:	zlib-devel
Requires:	libjpeg-devel
Requires:	freetype-devel >= 2.0
Requires:	%{name} = %{version}

%description devel
This package contains the files needed for development of programs
linked against GD.

%description devel -l es
Este paquete contiene los archivos de inclusión y las bibliotecas
necesarias para desarrollar programas usando gd.

%description devel -l pl
Pakiet ten zawiera pliki potrzebne do rozwoju programów korzystaj±cych
z biblioteki GD.

%description devel -l pt_BR
Este pacote contém os arquivos de inclusão e as bibliotecas
necessárias para desenvolver programas usando gd.

%package static
Summary:	Static GD library
Summary(es):	Static libraries for libgd development
Summary(pl):	Statyczna biblioteka GD
Summary(pt_BR):	Bibliotecas estáticas para desenvolvimento com libgd
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
This package contains static GD library. This is the gd image
manipulating library. It was created to allow graphs, charts and the
like to be generated on the fly for use on the World wide Web, but is
useful for any application in which custom images are useful. It is
not a paint program; it is a library.

This package contains static libraries for libgd development.

%description static -l pl
Pakiet ten zawiera statyczn± bibliotekê GD.

%description static -l pt_BR
Este pacote contem bibliotecas estáticas para desenvolvimento com
libgd.

%package progs
Summary:	Utility programs that use libgd
Summary(es):	Programas utilitarios libgd
Summary(pl):	Narzêdzia które u¿ywaj± libgd
Summary(pt_BR):	Programas utilitários libgd
Group:		Applications/Graphics
Requires:	%{name} = %{version}

%description progs
These are utility programs supplied with gd, the .jpeg graphics
library. The libgd-progs package contains a group of scripts for
manipulating the graphics files in formats which are supported by the
libgd library.

%description progs -l pl
Pakiet ten zawiera dodatkowe programy uzywaj±ce libgd.

%description progs -l pt_BR
Este pacote inclui vários utilitários para manipulação de arquivos gd
para uso pelos programas que usam a libgd.

%prep
%setup -q
%patch0 -p1

%build
libtoolize --copy --force
aclocal
automake -a -c -f
autoconf
if [ -f %{_pkgconfigdir}/libpng12.pc ] ; then
	CPPFLAGS="`pkg-config libpng12 --cflags`"
fi
%configure CPPFLAGS="$CPPFLAGS"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

gzip -9nf readme.txt index.html

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc readme.txt.gz
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

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*

#
# _without_gif	- without GIF support (patch from http://www.rhyme.com.au/gd/)
# _without_lzw	- without LZW compression in GIF creation functions
#
Summary:	Library for PNG, JPEG creation
Summary(es):	Biblioteca para manipulación de imágenes
Summary(pl):	Biblioteka do tworzenia grafiki w formacie PNG, JPEG
Summary(pt_BR):	Biblioteca para manipulação de imagens
Name:		gd
Version:	2.0.11
Release:	1
License:	BSD-like
Group:		Libraries
Source0:	http://www.boutell.com/ftp-materials/boutell/gd/%{name}-%{version}.tar.gz
#updated from http://downloads.rhyme.com.au/gd/patch_%{name}2.0.7_gif_20021118.gz
Patch0:		%{name}-gif.patch
Patch1:		%{name}-fontpath.patch
Patch2:		%{name}-fixes.patch
URL:		http://www.boutell.com/gd/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	freetype-devel >= 2.0
BuildRequires:	libpng-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libtiff-devel
BuildRequires:	libtool >= 1:1.4.3
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
%{!?_without_gif:Provides:	gd(gif) = %{version}}

%define		shlibver	%(echo %{version} | cut -f-2 -d.)

%description
gd is the image manipulating library. It was created to allow graphs,
charts and the like to be generated on the fly for use on the World
wide Web, but is useful for any application in which custom images are
useful. It is not a paint program; it is a library. gd library creates
PNG, JPEG and WBMP images. This is a good thing. PNG is a more compact
format, and full compression is available. JPEG works well with
photographic images, and is still more compatible with the major Web
browsers than even PNG is. WBMP is intended for wireless devices (not
regular web browsers).
%{!?_without_gif:This version has additional GIF images support.}

%description -l es
Esta es la biblioteca gd para el manejo de imágenes. Fue creada para
uso en la Web, creando gráficos automáticamente. Pero es útil para
cualquier programa que necesite de imágenes personalizados. No es un
programa de dibujo; es una biblioteca.

%description -l pl
gd to biblioteka do obróbki obrazów. Zosta³a stworzona, aby umo¿liwiæ
dynamiczne generowanie wykresów i podobnych rzeczy na potrzeby WWW,
ale mo¿e byæ przydatna tak¿e dla ka¿dej aplikacji tworz±cej w³asne
obrazy. Biblioteka ta pozwala na tworzenie plików graficznych w
formatach PNG, JPEG i WBMP. PNG jest zwartym formatem z bezstratn±
kompresj±. JPEG dobrze nadaje siê do obrazów fotograficznych i jest
obs³ugiwany nawet przez wiêcej przegl±darek WWW ni¿ PNG. WBMP jest
przeznaczony dla urz±dzeñ bezprzewodowych (a nie zwyk³ych przegl±darek
WWW).
%{!?_without_gif:Ta wersja ma dodatkowo obs³ugê formatu GIF.}

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
Requires:	%{name} = %{version}
Requires:	freetype-devel >= 2.0
Requires:	libjpeg-devel
Requires:	libpng-devel
Requires:	zlib-devel
%{!?_without_gif:Provides:	gd-devel(gif) = %{version}}

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
Summary(pl):	Statyczna biblioteka GD
Summary(pt_BR):	Bibliotecas estáticas para desenvolvimento com libgd
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}
%{!?_without_gif:Provides:	gd-static(gif) = %{version}}

%description static
This package contains static gd library.

%description static -l pl
Ten pakiet zawiera statyczn± bibliotekê gd.

%description static -l pt_BR
Este pacote contem bibliotecas estáticas para desenvolvimento com
libgd.

%package progs
Summary:	Utility programs that use libgd
Summary(es):	Programas utilitarios libgd
Summary(pl):	Narzêdzia u¿ywaj±ce libgd
Summary(pt_BR):	Programas utilitários libgd
Group:		Applications/Graphics
Requires:	%{name} = %{version}
%{!?_without_gif:Provides:	gd-progs(gif) = %{version}}

%description progs
These are utility programs supplied with gd, the image manipulation
library. The libgd-progs package contains a group of scripts for
manipulating the graphics files in formats which are supported by the
libgd library.

%description progs -l pl
Ten pakiet zawiera programy u¿ywaj±ce biblioteki gd, s³u¿±ce do
obróbki plików graficznych w formatach obs³ugiwanych przez libgd.

%description progs -l pt_BR
Este pacote inclui vários utilitários para manipulação de arquivos gd
para uso pelos programas que usam a libgd.

%prep
%setup -q
%{!?_without_gif:%patch0 -p1}
%patch1 -p1
%patch2 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__automake}
%{__autoconf}
%{!?_without_lzw:CPPFLAGS="-DLZW_LICENCED"}
%configure
%{__make}

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
%doc COPYING index.html
%attr(755,root,root) %{_libdir}/*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gdlib-config
%attr(755,root,root) %{_libdir}/*.so
%{_libdir}/*.la
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/[!g]*
%{!?_without_gif:%attr(755,root,root) %{_bindir}/gif*}
%attr(755,root,root) %{_bindir}/gd[!l]*

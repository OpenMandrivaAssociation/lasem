%define url_ver %(echo %{version}|cut -d. -f1,2)

%define	api	0.4
%define	major	4
%define libname	%mklibname %{name} %{api} %{major}
%define girname	%mklibname %{name}-gir %{api}
%define devname	%mklibname %{name} -d

Summary:	SVG and Mathml rendering library
Name:		lasem
Version:	0.4.1
Release:	2
Group:		Graphics
License:	GPLv2
Url:		http://blogs.gnome.org/emmanuel/category/lasem
Source0:	http://ftp.gnome.org/pub/GNOME/sources/lasem/%{url_ver}/%{name}-%{version}.tar.xz

BuildRequires:	flex
BuildRequires:	gtk-doc
BuildRequires:	intltool
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(pangocairo)

%description
Lasem aims to be a C/Gobject based SVG/Mathml renderer and editor, supporting
CSS style sheets. It uses cairo and pango as it's rendering abstraction layer,
and then support numerous output formats: xlib, PNG, SVG, PDF, PS, EPS...

%package -n %{libname}
Summary:	SVG and Mathml rendering library
Group:		System/Libraries

%description -n %{libname}
SVG and Mathml rendering library.

%package -n %{girname}
Summary:	GObject Introspection interface library for %{name}
Group:		System/Libraries

%description -n %{girname}
GObject Introspection interface library for %{name}.

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Requires:	%{girname} = %{version}-%{release}

%description -n %{devname}
This package contains the development files for %{name}.

%prep
%setup -q

%build
%configure2_5x \
	--disable-static

%make

%install
%makeinstall_std
rm -fr %{buildroot}/usr/doc/
%find_lang %{name}-%{api}

%files -f %{name}-%{api}.lang
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README
%{_bindir}/lasem-render*

%files -n %{libname}
%{_libdir}/lib%{name}-%{api}.so.*

%files -n %{girname}
%{_libdir}/girepository-1.0/Lasem-%{api}.typelib

%files -n %{devname}
%{_includedir}/%{name}-%{api}
%{_libdir}/pkgconfig/*.pc
%{_libdir}/lib%{name}-%{api}.so
%{_datadir}/gir-1.0/Lasem-%{api}.gir
%{_datadir}/gtk-doc/html/lasem-%{api}


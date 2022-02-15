Name:           edi
Version:        0.8.0
Release:        1
Summary:        Development environment for EFL
License:        GPL-2.0
Group:          Enlightenment/Development/Tools/IDE
Url:            http://enlightenment.org
Source:         https://download.enlightenment.org/rel/apps/edi/%{name}-%{version}.tar.xz
BuildRequires:  meson  
BuildRequires:  ImageMagick
BuildRequires:  doxygen
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(efl)

%description
EDI is a development environment designed for and built using the EFL.
    
%prep
%autosetup -p1
  
%build
%meson
%meson_build
  
%install
%meson_install
  
%files

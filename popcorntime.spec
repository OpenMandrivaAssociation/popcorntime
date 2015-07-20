%define debug_package	%{nil}

Summary:	Watch movies in steaming
Name:		popcorntime
Version:	0.3.8
Release:	1
License:	GPLv3
Group:		Video
Url:		https://popcorntime.io/
# git clone https://git.popcorntime.io/popcorntime/desktop.git
%ifarch %{ix86}
Source0:	http://get.popcorntime.io/build/Popcorn-Time-%{version}-0-Linux-32.tar.xz
%else
Source0:	http://get.popcorntime.io/build/Popcorn-Time-%{version}-0-Linux-64.tar.xz
%endif




%description
Allow any computer user to watch movies easily streaming 
from torrents, without any particular knowledge.

%prep
%setup -qc

%build
# Nothing to build

%install
# install all
mkdir -p %{buildroot}%{_datadir}/%{name}
install -Dm755 "Popcorn-Time"		"%{buildroot}%{_datadir}/%{name}/"
install -Dm644 "nw.pak"			"%{buildroot}%{_datadir}/%{name}/"
install -Dm644 "libffmpegsumo.so"	"%{buildroot}%{_datadir}/%{name}/"
install -Dm644 "CHANGELOG.md"		"%{buildroot}%{_datadir}/%{name}/"
install -Dm644 "icudtl.dat"		"%{buildroot}%{_datadir}/%{name}/"
install -Dm644 "install"		"%{buildroot}%{_datadir}/%{name}/"
install -Dm644 "LICENSE.txt"		"%{buildroot}%{_datadir}/%{name}/"
install -Dm644 "package.json"		"%{buildroot}%{_datadir}/%{name}/"
install -Dm644 "popcorntime.png"	"%{buildroot}%{_datadir}/%{name}/"
install -Dm644 "README.md"		"%{buildroot}%{_datadir}/%{name}/"
cp -a "locales"				"%{buildroot}%{_datadir}/%{name}/"
cp -a "node_modules"			"%{buildroot}%{_datadir}/%{name}/"
cp -a "src"				"%{buildroot}%{_datadir}/%{name}/"



# icon
mkdir -p  %{buildroot}%{_datadir}/pixmaps
install -Dm644 popcorntime.png %{buildroot}%{_datadir}/pixmaps/%{name}.png

# menu entry
mkdir -p %{buildroot}%{_datadir}/applications
cat << EOF > %{buildroot}%{_datadir}/applications/%{name}.desktop
[Desktop Entry]
Name=%{name}
Comment=Watch movies in steaming
Exec=%{name}
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=X-MandrivaLinux-Multimedia-Video;AudioVideo;Video;
EOF

# wrapper
mkdir -p %{buildroot}%{_bindir}
cat << EOF > %{buildroot}%{_bindir}/%{name}
#!/bin/bash
cd %{_datadir}/%{name} && ./Popcorn-Time
EOF
chmod +x %{buildroot}%{_bindir}/%{name} 

find %{buildroot} -size 0 -delete


%files
%doc LICENSE.txt CHANGELOG.md README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/%{name}
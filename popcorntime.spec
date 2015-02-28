%define debug_package	%{nil}

Summary:	Watch movies in steaming
Name:		popcorntime
Version:	0.3.7.2
Release:	1
License:	GPLv3
Group:		Video
Url:		https://popcorntime.io/
# git clone https://git.popcorntime.io/popcorntime/desktop.git
%ifarch x86_64
Source0:	http://212.47.235.197/build/Popcorn-Time-0.3.7.2-Linux64.tar.xz
%else
Source0:	http://31.7.184.36/build/Popcorn-Time-0.3.7.2-Linux32.tar.xz
%endif
Source1:	https://git.popcorntime.io/popcorntime/desktop/raw/master/LICENSE.txt
Source2:	https://git.popcorntime.io/popcorntime/desktop/raw/master/src/app/images/icons/local-icon.png


%description
Allow any computer user to watch movies easily streaming 
from torrents, without any particular knowledge.

%prep
%setup -qc
cp -R %{SOURCE1} LICENSE.txt

%build
# Nothing to build

%install
# install all
mkdir -p %{buildroot}%{_datadir}/%{name}
mv  libffmpegsumo.so nw.pak package.nw Popcorn-Time %{buildroot}%{_datadir}/%{name}/
chmod +x %{buildroot}%{_datadir}/%{name}/Popcorn-Time


# icon
mkdir -p  %{buildroot}%{_datadir}/pixmaps
cp %{SOURCE2} %{buildroot}%{_datadir}/pixmaps/%{name}.png

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



%files
%doc LICENSE.txt
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/%{name}/Popcorn-Time
%{_datadir}/%{name}/libffmpegsumo.so
%{_datadir}/%{name}/nw.pak
%{_datadir}/%{name}/package.nw
Name:		wlogout
Version:	1.2.2
Release:	1
Source0:	https://github.com/ArtsyMacaw/wlogout/archive/%{version}/%{name}-v%{version}.tar.gz
Summary:	A wayland based logout menu
URL:		https://github.com/ArtsyMacaw/wlogout
License:	MIT
Group:		Window Manager/Utility
BuildRequires:	meson
BuildSystem:	meson

%description
wlogout is a logout menu for wayland environments.

%prep
%autosetup -p1

%files
%{_sysconfdir}/wlogout
%{_bindir}/wlogout
%{_datadir}/bash-completion/completions/wlogout.bash
%{_datadir}/fish/completions/wlogout.fish
%{_mandir}/man1/wlogout.1.zst
%{_mandir}/man5/wlogout.5.zst
%{_datadir}/wlogout
%{_datadir}/zsh/site-functions/_wlogout

%global tl_name create-theorem
%global tl_revision 76924

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Initializing and configuring theorem-like environments, with multilingual sup...
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/create-theorem
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/create-theorem.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/create-theorem.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(crefthe)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides commands for naming, initializing and configuring
theorem-like environments. These commands have key-value based
interfaces and are especially useful in multilingual documents, allowing
the easy declaration of theorem-like environments that can automatically
adapt to the language settings.

